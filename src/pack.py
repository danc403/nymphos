import argparse
import os
import shutil
import subprocess
import tarfile
import re

def run_command(command, cwd=None):
    """Runs a shell command and prints output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, text=True)
    stdout, stderr = process.communicate()
    if stdout:
        print(stdout)
    if stderr:
        print(stderr)
    if process.returncode != 0:
        raise Exception(f"Command '{command}' failed with exit code {process.returncode}")

def find_spec_file(file_list_path):
    """Finds the .spec file name from the list of files."""
    spec_file = None
    try:
        with open(file_list_path, "r") as f:
            for line in f:
                item = line.strip()
                if item.endswith(".spec"):
                    if spec_file:
                        print(f"Warning: Multiple .spec files found: {spec_file}, {item}. Using the first one.")
                    spec_file = item
                    break
        if not spec_file:
            print("Error: No .spec file found in the list of files.")
    except FileNotFoundError:
        print(f"Error: File list '{file_list_path}' not found.")
    return spec_file

def extract_package_info(spec_file):
    """Extracts package name and version from the spec file."""
    name = None
    version = None
    try:
        with open(spec_file, "r") as f:
            for line in f:
                if line.startswith("Name:"):
                    name = line.split(":")[1].strip()
                elif line.startswith("Version:"):
                    version = line.split(":")[1].strip()
                if name and version:
                    break
    except FileNotFoundError:
        print(f"Error: Spec file '{spec_file}' not found.")
        return None, None
    return name, version

def generate_makefile(po_dir, pot_filename, po_files):
    """Generates a Makefile in the specified directory."""
    gettext_package = pot_filename.replace(".pot", "")
    makefile_content = f"""
GETTEXT_PACKAGE = {gettext_package}
LOCALEDIR = ./locale

.PHONY: all install clean update-po {' '.join([f.replace('.po', '.mo') for f in po_files])}

all: {' '.join([f.replace('.po', '.mo') for f in po_files])}

"""

    for po_file in po_files:
        lang_code = po_file.replace(".po", "")
        mo_file = lang_code + ".mo"
        makefile_content += f"""
{po_file}: {pot_filename}
\t@echo "Updating {po_file}..."
\tmsgmerge --update {po_file} {pot_filename} --no-wrap

{mo_file}: {po_file}
\t@echo "Building {mo_file}..."
\tmsgfmt {po_file} -o {mo_file}

"""

    makefile_content += """
install:
\tinstall -d "$(LOCALEDIR)"
"""
    for po_file in po_files:
        lang_code = po_file.replace(".po", "")
        mo_file = lang_code + ".mo"
        makefile_content += f"""
\tinstall -d "$(LOCALEDIR)/{lang_code}/LC_MESSAGES"
\tinstall -m 644 {mo_file} "$(LOCALEDIR)/{lang_code}/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"
"""

    makefile_content += """
update-po:
"""
    for po_file in po_files:
        makefile_content += f"""
\tmake {po_file}
"""

    makefile_content += """
clean:
\trm -f *.mo
"""
    for po_file in po_files:
        lang_code = po_file.replace(".po", "")
        makefile_content += f"""
\trm -f "$(LOCALEDIR)/{lang_code}/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"
"""

    makefile_path = os.path.join(po_dir, "Makefile")
    with open(makefile_path, "w") as f:
        f.write(makefile_content)
    print(f"Makefile generated in '{po_dir}' directory.")

def create_tarball(archive_name, file_list_path, base_dir="."):
    """Creates a tarball from the list of files."""
    with tarfile.open(archive_name, "w:xz") as tar:
        with open(file_list_path, "r") as f:
            for line in f:
                item = line.strip()
                if item:
                    filepath = os.path.join(base_dir, item)
                    if os.path.exists(filepath):
                        tar.add(filepath, arcname=item)
                    else:
                        print(f"Warning: File/directory '{filepath}' not found.")
    print(f"Tarball '{archive_name}' created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Packages a project into a tarball.")
    parser.add_argument("-f", "--filelist", required=True, help="Path to the file containing the list of files to package.")
    args = parser.parse_args()

    file_list_path = args.filelist
    spec_file_name = find_spec_file(file_list_path)

    if spec_file_name:
        package_name, package_version = extract_package_info(spec_file_name)
        if package_name and package_version:
            archive_base_name = package_name
            archive_name = f"{package_name}-{package_version}.tar.xz"
            build_dir_name = f"{package_name}-{package_version}"

            if os.path.isdir("po"):
                po_dir = "po"
                pot_files_po = [f for f in os.listdir(po_dir) if f.endswith(".pot")]
                po_files_po = [f for f in os.listdir(po_dir) if f.endswith(".po")]

                if pot_files_po and po_files_po:
                    pot_filename_po = pot_files_po[0] # Assuming one pot file
                    print("Localization setup detected. Generating Makefile...")
                    generate_makefile(po_dir, pot_filename_po, po_files_po)

            try:
                os.makedirs(build_dir_name, exist_ok=True)
                with open(file_list_path, "r") as f:
                    for line in f:
                        item = line.strip()
                        if item:
                            source_path = item
                            dest_path = os.path.join(build_dir_name, item)
                            if os.path.isdir(source_path):
                                shutil.copytree(source_path, dest_path)
                            else:
                                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                                shutil.copy2(source_path, dest_path)

                create_tarball(archive_name, file_list_path, base_dir=build_dir_name)
                shutil.rmtree(build_dir_name)
                print(f"Packaging process complete. Tarball: {archive_name}")

            except Exception as e:
                print(f"An error occurred: {e}")
                if os.path.exists(build_dir_name):
                    shutil.rmtree(build_dir_name)
                exit(1)

        else:
            print("Could not extract package name and version from the spec file. Tarball not created.")
            exit(1)

    else:
        print("Aborting due to missing spec file information.")
        exit(1)
