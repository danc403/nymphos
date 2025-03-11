import os
import subprocess
import argparse

def create_system_pipe_menu_launcher(app_name, script_path, icon_name, dock_number=1):
    """
    Creates a system-wide .desktop file and adds its path to Plank config for DynamicDocklet.
    """

    desktop_file_path = f"/usr/share/applications/{app_name.lower().replace(' ', '-')}.desktop"
    plank_config_path = f"/etc/xdg/plank/dock{dock_number}/settings"

    # Create the .desktop file (requires root)
    desktop_content = f"""
    [Desktop Entry]
    Type=Application
    Name={app_name}
    Name[xx_XX]=Translate Here
    Exec={script_path}
    Icon={icon_name}
    Comment=A dynamic pipe menu
    Comment[xx_XX]=Translate Here
    Terminal=false
    """

    try:
        subprocess.run(["sudo", "tee", desktop_file_path], input=desktop_content.encode(), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating desktop file: {e}")
        return

    # Make the script executable (requires root)
    try:
        subprocess.run(["sudo", "chmod", "+x", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error making script executable: {e}")
        return

    update_plank_config(desktop_file_path, plank_config_path)

def use_existing_desktop_file(desktop_file_path, dock_number=1):
    """
    Uses an existing .desktop file and adds its path to Plank config for DynamicDocklet.
    """

    plank_config_path = f"/etc/xdg/plank/dock{dock_number}/settings"
    update_plank_config(desktop_file_path, plank_config_path)

def update_plank_config(desktop_file_path, plank_config_path):
    """
    Updates the Plank configuration file.
    """
    try:
        # Create the plank config directory if it does not exist.
        if not os.path.exists(os.path.dirname(plank_config_path)):
            subprocess.run(["sudo", "mkdir", "-p", os.path.dirname(plank_config_path)], check=True)

        # Create the plank config file if it does not exist.
        if not os.path.exists(plank_config_path):
            subprocess.run(["sudo", "touch", plank_config_path], check=True)

        # Read the existing config
        config_lines = []
        if os.path.exists(plank_config_path):
            with open(plank_config_path, "r") as f:
                config_lines = f.readlines()

        # Add or update the DynamicDocklet.desktop_file setting
        found = False
        for i, line in enumerate(config_lines):
            if "DynamicDocklet.desktop_file=" in line:
                config_lines[i] = f"DynamicDocklet.desktop_file='{desktop_file_path}'\n"
                found = True
                break
        if not found:
            config_lines.append(f"DynamicDocklet.desktop_file='{desktop_file_path}'\n")

        # Write the updated config
        process = subprocess.Popen(["sudo", "tee", plank_config_path], stdin=subprocess.PIPE)
        process.communicate(input="".join(config_lines).encode())
        if process.returncode != 0:
            print(f"Error writing to Plank config file: {plank_config_path}")
            return

        print(f"Launcher added to Plank (dock{dock_number}) for DynamicDocklet.")

    except FileNotFoundError:
        print(f"Error: Plank config file not found: {plank_config_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_plank_configs():
    """Lists installed Plank configuration files."""
    plank_dir = "/etc/xdg/plank"
    if os.path.exists(plank_dir) and os.path.isdir(plank_dir):
        configs = [f for f in os.listdir(plank_dir) if os.path.isdir(os.path.join(plank_dir, f))]
        if configs:
            print("Installed Plank configurations:")
            for config in configs:
                print(f"- {config}")
        else:
            print("No Plank configurations found.")
    else:
        print("Plank configurations directory not found.")

def print_plank_config(dock_number):
    """Prints the contents of a selected Plank configuration file."""
    plank_config_path = f"/etc/xdg/plank/dock{dock_number}/settings"
    if os.path.exists(plank_config_path):
        try:
            with open(plank_config_path, "r") as f:
                print(f"Contents of {plank_config_path}:")
                print(f.read())
        except Exception as e:
            print(f"Error reading config file: {e}")
    else:
        print(f"Plank configuration file not found: {plank_config_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create system-wide pipe menu launcher.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--create", nargs=3, metavar=("app_name", "script_path", "icon_name"), help="Create a new .desktop file and add to Plank")
    group.add_argument("--use", metavar="desktop_file_path", help="Use an existing .desktop file and add to Plank")
    parser.add_argument("--dock", type=int, default=1, help="Dock number (e.g., 1, 2)")
    parser.add_argument("-l", "--list", action="store_true", help="List installed Plank configurations")
    parser.add_argument("-p", "--print", type=int, help="Print contents of a Plank configuration")

    args = parser.parse_args()

    if args.list:
        list_plank_configs()
    elif args.print is not None:
        print_plank_config(args.print)
    elif args.create:
        create_system_pipe_menu_launcher(args.create[0], args.create[1], args.create[2], args.dock)
    elif args.use:
        use_existing_desktop_file(args.use, args.dock)
    else:
        parser.print_help()
