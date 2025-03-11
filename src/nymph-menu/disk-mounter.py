#!/usr/bin/env python3

import subprocess
import re
import os
import shutil
    import sys
import signal

def find_desktop_file(desktop_name):
    """Finds the full path to a .desktop file."""
    locations = [
        "/usr/share/applications/",
        "/usr/local/share/applications/",
        os.path.expanduser("~/.local/share/applications/")
    ]
    for location in locations:
        full_path = os.path.join(location, desktop_name)
        if os.path.exists(full_path):
            return full_path
    return None

def send_refresh_signal():
    """Sends SIGUSR1 to the docklet associated with the desktop file."""
    script_name = os.path.basename(__file__)
    desktop_name = script_name.replace(".py", ".desktop")
    desktop_file_path = find_desktop_file(desktop_name)
    if desktop_file_path:
        try:
            file_name = os.path.basename(desktop_file_path)
            pid_file_name = file_name.replace(".desktop","")
            pid_file_name = re.sub(r'[^a-zA-Z0-9]', '-', pid_file_name)
            pid_file_path = f"/tmp/nymph-plank-docklet-{pid_file_name}.pid"
            with open(pid_file_path, "r") as f:
                pid = int(f.read().strip())
            os.kill(pid, signal.SIGUSR1)
        except FileNotFoundError:
            print("PID file not found.")
        except ProcessLookupError:
            print("Docklet process not found.")
        except Exception as e:
            print(f"Error sending signal: {e}")
    else:
        print(f"desktop file: {desktop_name} was not found")

# Environment variable retrieval and defaults
def get_removable_regex():
    regex = os.environ.get('OBDEVICEMENU_REMOVABLE_REGEX')
    if regex:
        try:
            re.compile(regex)
            return regex
        except re.error:
            return r'/dev/sd[a-z][0-9]*'
    else:
        return r'/dev/sd[a-z][0-9]*'

def get_optical_regex():
    regex = os.environ.get('OBDEVICEMENU_OPTICAL_REGEX')
    if regex:
        try:
            re.compile(regex)
            return regex
        except re.error:
            return r'/dev/sr[0-9]*'
    else:
        return r'/dev/sr[0-9]*'

def get_show_internal():
    return os.environ.get('OBDEVICEMENU_SHOW_INTERNAL', '0') == '1'

def get_blacklist():
    blacklist = os.environ.get('OBDEVICEMENU_BLACKLIST', '')
    return blacklist.split()

def get_filemanager():
    filemanager = os.environ.get('FILEMANAGER')
    if filemanager:
        return filemanager

    desktop_session = os.environ.get('DESKTOP_SESSION')
    xdg_desktop = os.environ.get('XDG_CURRENT_DESKTOP')

    if desktop_session == 'xfce' or xdg_desktop == 'XFCE':
        if shutil.which('thunar'):
            return 'thunar'
    elif desktop_session == 'gnome' or xdg_desktop == 'GNOME':
        if shutil.which('nautilus'):
            return 'nautilus'
    elif desktop_session == 'kde' or xdg_desktop == 'KDE':
        if shutil.which('dolphin'):
            return 'dolphin'

    if shutil.which('thunar'):
        return 'thunar'
    elif shutil.which('caja'):
        return 'caja'

    return None

# Command execution
def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

# Device retrieval
def get_devices(regex):
    output = run_command(['udisks', '--enumerate-device-files'])
    if output:
        devices = re.findall(regex, output, re.MULTILINE)
        return sorted(devices)
    return []

# Device information retrieval
def get_device_info(device, key):
    output = run_command(['udisks', '--show-info', device])
    if output:
        match = re.search(rf'^\s*{key}:\s*(.+)', output, re.MULTILINE)
        if match:
            return match.group(1).strip()
    return None

# Fancy sort
def fancy_sort(devices):
    temp_devices = []
    for device in devices:
        devmajor = re.sub(r'[0-9]+$', '', device)
        if device == devmajor:
            temp_devices.append(device)
        else:
            partition_number = int(re.search(r'[0-9]+$', device).group(0))
            temp_devices.append(f"{devmajor}{partition_number:02}")
    temp_devices.sort()
    sorted_devices = []
    for device in temp_devices:
        devmajor = re.sub(r'[0-9]+$', '', device)
        if device == devmajor:
            sorted_devices.append(device)
        else:
            partition_number = int(re.search(r'[0-9]+$', device).group(0))
            sorted_devices.append(f"{devmajor}{partition_number}")
    return sorted_devices

# Display options tracking (using a simple file)
DISPLAY_OPTIONS_FILE = "/tmp/obdevicemenu_display_options"
def get_display_options():
    try:
        with open(DISPLAY_OPTIONS_FILE, "r") as f:
            return f.read().split(",")
    except FileNotFoundError:
        return ["label", "label"]  # Default: label for both removable and optical

def set_display_options(removable, optical):
    with open(DISPLAY_OPTIONS_FILE, "w") as f:
        f.write(f"{removable},{optical}")

def generate_menu():
    removable_regex = get_removable_regex()
    optical_regex = get_optical_regex()
    show_internal = get_show_internal()
    blacklist = get_blacklist()
    filemanager = get_filemanager()
    removable_display, optical_display = get_display_options()

    print('<openbox_pipe_menu>')

    print('<menu id="display_options" label="Display Options">')
    print(f'<item label="Show Removable Filename" {"checked" if removable_display == "filename" else ""}>')
    print(f'<action name="Execute"><command>./disk-mounter.py --toggle-removable-filename</command></action>')
    print('</item>')
    print(f'<item label="Show Optical Filename" {"checked" if optical_display == "filename" else ""}>')
    print(f'<action name="Execute"><command>./disk-mounter.py --toggle-optical-filename</command></action>')
    print('</item>')
    print('</menu>')

    print('<separator label="Removable media" />')
    removable_devices = get_devices(removable_regex)
    removable_devices = fancy_sort(removable_devices)

    mounted_removable = []
    total_removable = 0

    for device in removable_devices:
        total_removable += 1
        devmajor = re.sub(r'[0-9]+$', '', device)
        internal = get_device_info(devmajor, 'system internal')
        if internal == '1' and not show_internal:
            continue

        skip = False
        for bl in blacklist:
            if bl in run_command(['udisks', '--show-info', device]):
                skip = True
                break
        if skip:
            continue

        label = get_device_info(device, 'label') or get_device_info(devmajor, 'model') or get_device_info(devmajor, 'vendor') or 'No label'
        if not get_device_info(device, 'label') and label != 'No label':
            label = f'No label ({label})'

        mounted = get_device_info(device, 'is mounted') == '1'
        mounted_text = ' (Mounted)' if mounted else ' (Unmounted)'

        if sys.argv[1] == '--mount-device' and sys.argv[2].replace("_", "/") == device:
            if mount_device(device) == False:
                mounted_text = " (Mount Failed)"

        if sys.argv[1] == '--unmount-device' and sys.argv[2].replace("_", "/") == device:
            run_command(['udisks', '--unmount', device])
            if get_device_info(device, "is mounted") == '1':
                mounted_text = " (Unmount Failed)"
            else:
                mounted_text = " (Unmounted)"

        display_label = f'{device.replace("/dev/", "")}: {label}{mounted_text}' if removable_display == "filename" else f'{label}{mounted_text}'

        print(f'<menu id="mount{device.replace("/", "_")}" label="{display_label}" execute="./disk-mounter.py --mount-menu removable {device.replace("/", "_")}" />')
        if mounted:
            mounted_removable.append(device)

    if total_removable == 0:
        print('<item label="None" />')
    elif mounted_removable:
        print('<item label="Unmount all">')
        print('<action name="Execute">')
        print(f'<command>./disk-mounter.py --unmount-all-removable {" ".join(mounted_removable)}</command>')
        print('<prompt>Unmount all removable devices?</prompt>')
        print('</action>')
        print('</item>')

    print('<separator label="Optical media" />')
    optical_devices = get_devices(optical_regex)
    mounted_optical = []

    for device in optical_devices:
        has_media = get_device_info(device, 'has media') == '1'

        skip = False
        for bl in blacklist:
            if bl in run_command(['udisks', '--show-info', device]):
                skip = True
                break
        if skip:
            continue

        if not has_media:
            print(f'<item label="{device.replace("/dev/", "")}: None" />')
            continue

        blank = get_device_info(device, 'blank') == '1'
        label = 'Blank media' if blank else get_device_info(device, 'label') or get_device_info(device, 'model') or get_device_info(device, 'vendor') or 'No label'
        mounted = get_device_info(device, 'is mounted') == '1'
        mounted_text = ' (Mounted)' if mounted else ' (Unmounted)'

        if sys.argv[1] == '--mount-device' and sys.argv[2].replace("_", "/") == device:
            if mount_device(device) == False:
                mounted_text = " (Mount Failed)"

        if sys.argv[1] == '--unmount-device' and sys.argv[2].replace("_", "/") == device:
            run_command(['udisks', '--unmount', device])
            if get_device_info(device, "is mounted") == '1':
                mounted_text = " (Unmount Failed)"
            else:
                mounted_text = " (Unmounted)"

        display_label = f'{device.replace("/dev/", "")}: {label}{mounted_text}' if optical_display == "filename" else f'{label}{mounted_text}'

        print(f'<menu id="mount{device.replace("/", "_")}" label="{display_label}" execute="./disk-mounter.py --mount-menu optical {device.replace("/", "_")}" />')
        if mounted:
            mounted_optical.append(device)

    if mounted_optical:
        print('<item label="Unmount all">')
        print('<action name="Execute">')
        print(f'<command>./disk-mounter.py --unmount-all-optical {" ".join(mounted_optical)}</command>')
        print('<prompt>Unmount all optical devices?</prompt>')
        print('</action>')
        print('</item>')

    print('</openbox_pipe_menu>')

def mount_menu(media_type, device_name):
    device = device_name.replace("_", "/")
    label = get_device_info(device, 'label') or get_device_info(re.sub(r'[0-9]+$', '', device), 'model') or get_device_info(re.sub(r'[0-9]+$', '', device), 'vendor') or 'No label'

    print('<openbox_pipe_menu>')

    removable_display, optical_display = get_display_options()

    if media_type == 'removable':
        if removable_display == "filename":
            print(f'<separator label="{device}" />')
        else:
            print(f'<separator label="{label}" />')
    elif media_type == 'optical':
        if optical_display == "filename":
            print(f'<separator label="{device}" />')
        else:
            print(f'<separator label="{label}" />')

    mounted = get_device_info(device, 'is mounted') == '1'
    ejectable = get_device_info(device, 'ejectable') == '1'
    filemanager = get_filemanager()

    if not mounted:
        print('<item label="Open">')
        print(f'<action name="Execute"><command>./disk-mounter.py --mount-and-open {device.replace("/", "_")}</command></action>')
        print('</item>')

        print('<item label="Mount">')
        print(f'<action name="Execute"><command>./disk-mounter.py --mount-device {device.replace("/", "_")}</command></action>')
        print('</item>')
    else:
        print('<item label="Open">')
        print(f'<action name="Execute"><command>{filemanager} "{get_device_info(device, "mount paths").split()[0]}"</command></action>')
        print('</item>')

        print('<item label="Unmount">')
        print(f'<action name="Execute"><command>./disk-mounter.py --unmount-device {device.replace("/", "_")}</command></action>')
        print('</item>')

    if ejectable:
        print('<item label="Eject">')
        print(f'<action name="Execute"><command>./disk-mounter.py --eject-device {device.replace("/", "_")}</command></action>')
        print('</item>')

    print(f'<menu id="showinfo{device.replace("/", "_")}" label="Info" execute="./disk-mounter.py --show-info {device.replace("/", "_")}" />')

    print('</openbox_pipe_menu>')

def info_menu(device):
    output = run_command(['udisks', '--show-info', device])
    if output:
        print('<openbox_pipe_menu>')
        print(f'<separator label="Info: {device}" />')
        for line in output.splitlines():
            if line:
                key, value = line.split(':', 1)
                print(f'<item label="{key.strip()}: {value.strip()}" />')
        print('</openbox_pipe_menu>')

def mount_device(device):
    try:
        subprocess.run(['udisks', '--mount', device], check=True)
    except subprocess.CalledProcessError:
        try:
            subprocess.run(['pkexec', 'udisks', '--mount', device], check=True)
        except subprocess.CalledProcessError:
            print("Failed to mount device (insufficient privileges or incorrect password).")

def mount_device(device):
    try:
        subprocess.run(['udisks', '--mount', device], check=True)
        return True #mount success
    except subprocess.CalledProcessError:
        try:
            subprocess.run(['pkexec', 'udisks', '--mount', device], check=True)
            return True #mount success
        except subprocess.CalledProcessError:
            print("Failed to mount device (insufficient privileges or incorrect password).")
            return False #mount failed

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '--mount-menu':
            mount_menu(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == '--mount-device':
            mount_device(sys.argv[2].replace("_", "/"))
            send_refresh_signal()
        elif sys.argv[1] == '--unmount-device':
            run_command(['udisks', '--unmount', sys.argv[2].replace("_", "/")])
            send_refresh_signal()
        elif sys.argv[1] == '--eject-device':
            run_command(['udisks', '--eject', sys.argv[2].replace("_", "/")])
            send_refresh_signal()
        elif sys.argv[1] == '--mount-and-open':
            device = sys.argv[2].replace("_", "/")
            mount_device(device)
            if get_device_info(device, "is mounted") == '1':
                mount_path = get_device_info(device, "mount paths").split()[0]
                run_command([get_filemanager(), mount_path])
            send_refresh_signal()
        elif sys.argv[1] == '--show-info':
            device = sys.argv[2].replace("_", "/")
            info_menu(device)
        elif sys.argv[1] == '--unmount-all-removable':
            for device in sys.argv[2:]:
                run_command(['udisks', '--unmount', device.replace("_", "/")])
                send_refresh_signal()
        elif sys.argv[1] == '--unmount-all-optical':
            for device in sys.argv[2:]:
                run_command(['udisks', '--unmount', device.replace("_", "/")])
                send_refresh_signal()
        elif sys.argv[1] == '--toggle-removable-filename':
            removable, optical = get_display_options()
            removable = "filename" if removable == "label" else "label"
            set_display_options(removable, optical)
        elif sys.argv[1] == '--toggle-optical-filename':
            removable, optical = get_display_options()
            optical = "filename" if optical == "label" else "label"
            set_display_options(removable, optical)
        else:
            generate_menu()
