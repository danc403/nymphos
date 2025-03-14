#!/usr/bin/env python3

import os
import re
import subprocess
import shutil
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Environment variable defaults
DEFAULT_EXTLINUX_CONFIG = os.environ.get("DEFAULT_EXTLINUX_CONFIG", "/boot/extlinux/extlinux.conf")
DEFAULT_EFI_KERNEL_LABEL = os.environ.get("DEFAULT_EFI_KERNEL_LABEL", "Nymph-Linux")
DEFAULT_EFI_KERNEL_PATH = os.environ.get("DEFAULT_EFI_KERNEL_PATH", "\\EFI\\nymph\\vmlinuz-linux.efi")
PERSISTENT_BOOT_VAR = os.environ.get("PERSISTENT_BOOT", "false").lower() == "true"
REVERT_SCRIPT_PATH = os.environ.get("REVERT_SCRIPT_PATH", "/etc/init.d/revert-boot") # Changed for clarity
EFI_MOUNT_POINT = "/boot/efi"

def check_root():
    """Check if the script is run as root or with sudo."""
    if os.geteuid() != 0:
        logging.error("This script must be run as root or with sudo.")
        sys.exit(1)

def find_efi_partition():
    """Dynamically finds the EFI system partition."""
    try:
        result = subprocess.run(["findmnt", EFI_MOUNT_POINT, "-n", "-o", "SOURCE"], capture_output=True, text=True, check=True)
        device = result.stdout.strip()
        if not device:
            raise ValueError(f"No device found mounted at {EFI_MOUNT_POINT}")

        # Extract disk and partition number
        match = re.match(r"(/dev/[a-z]+)(\d+)?", device)
        if not match:
            raise ValueError(f"Unexpected device format: {device}")
        disk = match.group(1)
        partition = match.group(2) or "1" # Default to partition 1 if not specified

        logging.info(f"EFI partition found: disk={disk}, partition={partition}")
        return disk, partition
    except (subprocess.CalledProcessError, ValueError) as e:
        logging.error(f"Error finding EFI partition: {e}")
        return None, None

def create_revert_script(efi_boot_vars=None, backup_path=None, config_path=None, boot_type=None):
    """Creates the revert script with the appropriate commands."""
    try:
        with open(REVERT_SCRIPT_PATH, "w") as f:
            f.write("#!/bin/sh\n")
            f.write("# Revert Boot Script - Auto-generated\n\n")

            # Export necessary environment variables before anything else.
            f.write(f"export DEFAULT_EXTLINUX_CONFIG=\"{DEFAULT_EXTLINUX_CONFIG}\"\n")
            f.write(f"export DEFAULT_EFI_KERNEL_LABEL=\"{DEFAULT_EFI_KERNEL_LABEL}\"\n")
            f.write(f"export DEFAULT_EFI_KERNEL_PATH=\"{DEFAULT_EFI_KERNEL_PATH}\"\n")
            f.write(f"export REVERT_SCRIPT_PATH=\"{REVERT_SCRIPT_PATH}\"\n")

            f.write("set -e\n")  # Exit immediately if a command exits with a non-zero status.

            if boot_type == "extlinux":
                f.write(f"backup_path=\"{backup_path}\"\n")
                f.write(f"config_path=\"{config_path}\"\n")
                f.write("if [ -f \"$backup_path\" ]; then\n")
                f.write("  mv \"$backup_path\" \"$config_path\"\n")
                f.write("  echo \"Reverted extlinux.conf to backup.\" \n")
                f.write("else\n")
                f.write("  echo \"Backup file not found: $backup_path\" \n")
                f.write("fi\n")

            elif boot_type == "efi":
                disk, partition = find_efi_partition()
                if not disk or not partition:
                    f.write("  echo \"Error: Could not determine EFI partition.  Manual intervention required.\"\n")
                    f.write("  exit 1\n")
                    return  # Exit the function if no EFI partition is found

                f.write("efi_boot_vars=\"\"\"\n")
                f.write(efi_boot_vars)
                f.write("\"\"\"\n")
                f.write("if [ -n \"$efi_boot_vars\" ]; then\n")
                f.write("  current_bootnum=$(efibootmgr | grep \"^BootCurrent\" | cut -d '*' -f1 | cut -d 't' -f2)\n")
                f.write("  if [ -n \"$current_bootnum\" ]; then\n")
                f.write("    efibootmgr --delete-bootnum \"$current_bootnum\"\n")
                f.write("    echo \"Deleted current boot entry.\"\n")
                f.write("  else\n")
                f.write("    echo \"Warning: Could not determine current boot entry.\"\n")
                f.write("  fi\n")
                # Create a new boot entry based on our environment variables.
                f.write(f"  efibootmgr --create --disk {disk} --part {partition} --loader '{DEFAULT_EFI_KERNEL_PATH}' --label '{DEFAULT_EFI_KERNEL_LABEL}'\n")
                f.write("  echo \"Created default boot entry.\"\n")

                # Restore the EFI boot variables based on the backup.
                f.write("  echo \"Restoring EFI boot variables...\"\n")

                #Iterate through the backed up variables and recreate each boot entry.
                f.write("  echo \"$efi_boot_vars\" | while read line; do\n")
                f.write("    if [[ \"$line\" =~ ^Boot([0-9A-Fa-f]{4})\\* ]]; then\n")
                f.write("      bootnum=${BASH_REMATCH[1]}\n")
                f.write("      loader=$(echo \"$line\" | awk '{print $4}')\n")
                f.write("      label=$(echo \"$line\" | awk '{print $2}')\n")
                f.write(f"      efibootmgr --create --disk {disk} --part {partition} --loader \"$loader\" --label \"$label\"\n")
                f.write("    fi\n")
                f.write("  done\n")
                f.write("  echo \"EFI boot variables restored.\"\n")

            else:
                f.write("echo \"Error: Unsupported boot type. Manual intervention required.\"\n")
                f.write("exit 1\n")
                return

            #Clean up and remove the revert script.
            f.write("  rc-update del revert-boot default\n")
            f.write("  rm \"$revert_script_path\"\n")
            f.write("  echo \"Revert script removed.\"\n")
            f.write("fi\n")  # closes the if statement.

        os.chmod(REVERT_SCRIPT_PATH, 0o755)
        subprocess.run(["rc-update", "add", "revert-boot", "default"], check=True)
        logging.info(f"Revert script created at {REVERT_SCRIPT_PATH} and added to OpenRC.")
    except (OSError, subprocess.CalledProcessError) as e:
        logging.error(f"Error creating revert script: {e}")

def update_extlinux_temp(new_config):
    """Updates extlinux.conf temporarily with robust error handling."""
    config_path = DEFAULT_EXTLINUX_CONFIG
    backup_path = config_path + ".bak"

    try:
        shutil.copy2(config_path, backup_path)
        logging.info(f"Backed up {config_path} to {backup_path}")
        with open(config_path, "w") as f:
            f.write(new_config)
        logging.info(f"Updated {config_path} with new configuration.")

        if not PERSISTENT_BOOT_VAR:
            create_revert_script(backup_path=backup_path, config_path=config_path, boot_type="extlinux")

        subprocess.run(["reboot"], check=True)

    except (OSError, subprocess.CalledProcessError) as e:
        logging.error(f"Error: {e}")
        if os.path.exists(backup_path):
            try:
                shutil.move(backup_path, config_path)
                logging.info("Reverted to original extlinux.conf.")
            except OSError as revert_err:
                logging.error(f"Error reverting extlinux.conf: {revert_err}")

        if os.path.exists(REVERT_SCRIPT_PATH):
            try:
                subprocess.run(["rc-update", "del", "revert-boot", "default"], check=True)
                os.remove(REVERT_SCRIPT_PATH)
                logging.info("Reverted OpenRC service.")
            except (OSError, subprocess.CalledProcessError) as revert_err:
                logging.error(f"Error reverting OpenRC service: {revert_err}")

        sys.exit(1)

def update_efi_temp(new_boot_entry):
    """Updates EFI boot variables temporarily with robust error handling."""
    try:
        efibootmgr_output = subprocess.check_output(["efibootmgr", "-v"]).decode()
        disk, partition = find_efi_partition()
        if not disk or not partition:
            logging.error("Could not determine EFI partition. Aborting.")
            sys.exit(1)

        subprocess.run(["efibootmgr", "-c", "-l", new_boot_entry["kernel"], "-L", new_boot_entry["label"]], check=True)
        logging.info(f"Created temporary EFI boot entry: {new_boot_entry['label']}")

        if not PERSISTENT_BOOT_VAR:
             create_revert_script(efi_boot_vars=efibootmgr_output, boot_type="efi")

        subprocess.run(["reboot"], check=True)

    except (OSError, subprocess.CalledProcessError) as e:
        logging.error(f"Error: {e}")
        if os.path.exists(REVERT_SCRIPT_PATH):
            try:
                subprocess.run(["rc-update", "del", "revert-boot", "default"], check=True)
                os.remove(REVERT_SCRIPT_PATH)
                logging.info("Reverted OpenRC service.")
            except (OSError, subprocess.CalledProcessError) as revert_err:
                logging.error(f"Error reverting OpenRC service: {revert_err}")

        sys.exit(1)

def get_partition_info():
    """Gets partition information using blkid and fdisk."""
    partitions = {}
    try:
        blkid_output = subprocess.check_output(["blkid"]).decode()
        for line in blkid_output.splitlines():
            parts = line.split(":")
            if len(parts) > 1:
                device = parts[0]
                uuid_match = re.search(r'UUID="([^"]+)"', line)
                fstype_match = re.search(r'TYPE="([^"]+)"', line)
                if uuid_match:
                    uuid = uuid_match.group(1)
                    fstype = fstype_match.group(1) if fstype_match else "unknown"
                    partitions[device] = {"uuid": uuid, "fstype": fstype, "partition": device}
    except subprocess.CalledProcessError:
        logging.warning("blkid command failed.")

    try:
        fdisk_output = subprocess.check_output(["fdisk", "-l"]).decode()
        for line in fdisk_output.splitlines():
            if line.startswith("/dev/"):
                parts = line.split()
                if len(parts) > 1:
                    device = parts[0]
                    if device in partitions:
                        partitions[device]["partition"] = device
    except subprocess.CalledProcessError:
        logging.warning("fdisk command failed.")

    return partitions

def detect_os_on_partition(partition):
    """Detects OS on a given partition."""
    try:
        blkid_output = subprocess.check_output(["blkid", partition]).decode()
        fstype_match = re.search(r'TYPE="([^"]+)"', blkid_output)
        if fstype_match:
            fstype = fstype_match.group(1)
            if fstype == "ntfs":
                if os.path.exists(os.path.join(partition, "Windows")):
                    return "Windows"
            elif fstype == "hfs+":
                if os.path.exists(os.path.join(partition, "System/Library")):
                    return "macOS"
            elif fstype == "ext4":
                if os.path.exists(os.path.join(partition, "etc/os-release")):
                    return "Linux"
                elif os.path.exists(os.path.join(partition, "etc/issue")):
                    return "Linux"
    except subprocess.CalledProcessError:
        pass
    return "Unknown"

def detect_boot_type():
    """Detects the boot configuration type."""
    if os.path.exists("/boot/extlinux/extlinux.conf"):
        return "extlinux"
    elif os.path.exists("/boot/efi/EFI/BOOT/BOOTX64.EFI"):
        return "efi"
    else:
        return None

def parse_extlinux_config(config_file=None):
    """Parses extlinux.conf and returns a list of boot entries."""
    if config_file is None:
        config_file = DEFAULT_EXTLINUX_CONFIG
    boot_entries = []
    current_entry = {}

    if not os.path.exists(config_file):
        logging.warning(f"Configuration file not found at {config_file}")
        return []

    try:
        with open(config_file, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("label"):
                    if current_entry:
                        boot_entries.append(current_entry)
                    current_entry = {"label": line.split("label")[1].strip()}
                elif line.startswith("kernel"):
                    kernel_path = line.split("kernel")[1].strip()
                    current_entry["kernel"] = kernel_path
                    try:
                        current_entry["kernel_version"] = current_entry["kernel"].split("vmlinuz-")[1]
                    except IndexError:
                        current_entry["kernel_version"] = None
                    if "chain.c32" in kernel_path:
                        current_entry["chainload"] = True
                    else:
                        current_entry["chainload"] = False
                elif line.startswith("append"):
                    current_entry["append"] = line.split("append")[1].strip()
                    initrd_match = re.search(r"initrd=([^ ]+)", current_entry["append"])
                    root_match = re.search(r"root=UUID=([^ ]+)", current_entry["append"])
                    current_entry["initrd"] = initrd_match.group(1) if initrd_match else None
                    current_entry["root_uuid"] = root_match.group(1) if root_match else None
                    chain_match = re.search(r"hd(\d+) (\d+)", current_entry["append"])
                    if chain_match:
                        current_entry["chainload_disk"] = int(chain_match.group(1))
                        current_entry["chainload_partition"] = int(chain_match.group(2))

            if current_entry:
                boot_entries.append(current_entry)

    except IOError as e:
        logging.warning(f"Error reading configuration file: {e}")
        return []

    return boot_entries

def parse_efi_config():
    """Parses EFI boot configuration."""
    boot_entries = []
    try:
        efibootmgr_output = subprocess.check_output(["efibootmgr", "-v"]).decode()
        for line in efibootmgr_output.splitlines():
            boot_match = re.search(r'Boot(\d+)\* (.+)', line)
            if boot_match:
                boot_number = boot_match.group(1)
                boot_description = boot_match.group(2)
                file_match = re.search(r'\\(.+\.efi)', line)
                if file_match:
                    efi_file_path = "/boot/efi" + file_match.group(1)
                    chainload = False
                    chainload_type = "unknown"
                    if "grubx64.efi" in efi_file_path:
                        chainload = True
                        chainload_type = "grub"
                    elif "bootmgfw.efi" in efi_file_path:
                        chainload = True
                        chainload_type = "windows"
                    entry = {
                        "boot_type": "efi",
                        "label": boot_description,
                        "kernel": efi_file_path,
                        "chainload": chainload,
                        "chainload_path": efi_file_path,
                        "chainload_type": chainload_type,
                    }
                    boot_entries.append(entry)
    except subprocess.CalledProcessError:
        logging.warning("efibootmgr command failed.")
    return boot_entries

def get_default_extlinux_kernel(config_file=None):
    """Gets the default kernel from extlinux.conf."""
    if config_file is None:
        config_file = DEFAULT_EXTLINUX_CONFIG
    if not os.path.exists(config_file):
        return None

    try:
        with open(config_file, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("DEFAULT"):
                    return line.split("DEFAULT")[1].strip()
    except IOError:
        return None
    return None

def get_current_efi_boot_entry():
    """Gets the current EFI boot entry using efibootmgr."""
    try:
        output = subprocess.check_output(["efibootmgr", "-v"]).decode()
        for line in output.splitlines():
            if "BootCurrent:" in line:
                return line.split("BootCurrent:")[1].strip().split(",")[0]
    except subprocess.CalledProcessError:
        return None
    return None

def get_efi_boot_order():
    """Gets the EFI boot order using efibootmgr."""
    order = []
    try:
        output = subprocess.check_output(['efibootmgr', '-v']).decode()
        for line in output.splitlines():
            if 'BootOrder:' in line:
                order_string = line.split('BootOrder:')[1].strip()
                order = order_string.split(',')
    except subprocess.CalledProcessError:
        pass

    return order

def mark_default_kernels(boot_data):
    """Marks the default kernels in the boot data."""
    default_extlinux_label = get_default_extlinux_kernel()
    current_efi_boot_entry = get_current_efi_boot_entry()
    efi_boot_order = get_efi_boot_order()

    if default_extlinux_label:
        for entry in boot_data["legacy"]:
            if entry["label"] == default_extlinux_label:
                entry["label"] = f"* {entry['label']}"

    if current_efi_boot_entry:
        for entry in boot_data["efi"]:
            entry_number = re.search(r'Boot(\d+)', current_efi_boot_entry).group(1)
            if entry_number in entry["kernel"]:
                entry["label"] = f"* {entry['label']}"

    return boot_data

def build_boot_data():
    """Builds the complete boot data structure."""
    boot_data = {
        "legacy": parse_extlinux_config(),
        "efi": parse_efi_config(),
        "windows": [],
        "macos": [],
        "linux": [],
        "partitions": get_partition_info()
    }

    partitions = boot_data["partitions"]

    for partition_path, partition_info in partitions.items():
        os_type = detect_os_on_partition(partition_path)
        if os_type == "Windows":
            boot_data["windows"].append({"label": "Windows", "partition": partition_path, **partition_info})
        elif os_type == "macOS":
            boot_data["macos"].append({"label": "macOS", "partition": partition_path, **partition_info})
        elif os_type == "Linux":
            boot_data["linux"].append({"label": "Linux", "partition": partition_path, **partition_info})

    return boot_data

def generate_openbox_xml(boot_data):
    """Generates Openbox pipe menu XML with Python function calls."""
    xml = "<openbox_pipe_menu>\n"

    for boot_type, entries in boot_data.items():
        if boot_type == "partitions":
            continue
        if entries:
            xml += f"<menu id=\"{boot_type}\" label=\"{boot_type.capitalize()}\">\n"
            for i, entry in enumerate(entries):
                label = entry.get("label", "Unknown")
                xml += f"<menu id=\"{boot_type}_{i}\" label=\"{label}\">\n"

                # Edit Label
                xml += f"<item label=\"Edit Label\">\n"
                xml += f"<action name=\"Execute\"><command>python3 -c \"from __main__ import edit_label; edit_label({boot_data}, '{boot_type}', {i}, '{label}')\"</command></action>\n"
                xml += "</item>\n"

                # Edit Kernel
                if "kernel" in entry:
                    kernel = entry.get("kernel", "Unknown")
                    xml += f"<item label=\"Edit Kernel\">\n"
                    xml += f"<action name=\"Execute\"><command>python3 -c \"from __main__ import edit_kernel; edit_kernel({boot_data}, '{boot_type}', {i}, '{kernel}')\"</command></action>\n"
                    xml += "</item>\n"

                # Edit Append
                if "append" in entry:
                    append = entry.get("append", "")
                    xml += f"<item label=\"Edit Append\">\n"
                    xml += f"<action name=\"Execute\"><command>python3 -c \"from __main__ import edit_append; edit_append({boot_data}, '{boot_type}', {i}, '{append}')\"</command></action>\n"
                    xml += "</item>\n"

                # Chain-Loading Information
                if entry.get("chainload"):
                    if boot_type == "legacy":
                        xml += f"<item label=\"Chainload: hd{entry.get('chainload_disk', '?')} {entry.get('chainload_partition', '?')}\"/>\n"
                    elif boot_type == "efi":
                        xml += f"<item label=\"Chainload: {entry.get('chainload_type', 'unknown')} - {entry.get('chainload_path', 'unknown')}\"/>\n"

                # Partition Information
                if "partition" in entry:
                    partition = entry.get("partition", "Unknown")
                    xml += f"<item label=\"Partition: {partition}\"/>\n"
                    if "uuid" in entry:
                        uuid = entry.get("uuid", "Unknown")
                        xml += f"<item label=\"UUID: {uuid}\"/>\n"
                    if "fstype" in entry:
                        fstype = entry.get("fstype", "Unknown")
                        xml += f"<item label=\"Filesystem: {fstype}\"/>\n"

                # Persistence Checkbox (Simulated)
                xml += f"<item label=\"Persistent Change\">\n"
                xml += f"<action name=\"Execute\"><command>python3 -c \"from __main__ import toggle_persistence; toggle_persistence({boot_data}, '{boot_type}', {i})\"</command></action>\n"
                xml += "</item>\n"

                # Update Button
                xml += f"<item label=\"Update Entry\">\n"
                xml += f"<action name=\"Execute\"><command>python3 -c \"from __main__ import update_entry; update_entry({boot_data}, '{boot_type}', {i})\"</command></action>\n"
                xml += "</item>\n"

                xml += "</menu>\n"
            xml += "</menu>\n"

    xml += "</openbox_pipe_menu>"
    return xml

def edit_label(boot_data, boot_type, entry_index, current_label):
    """Edits the label of a boot entry."""
    new_label = input(f"Enter new label for {boot_type} entry {entry_index}: ")
    boot_data[boot_type][entry_index]["label"] = new_label

def edit_kernel(boot_data, boot_type, entry_index, current_kernel):
    """Edits the kernel path of a boot entry."""
    new_kernel = input(f"Enter new kernel path for {boot_type} entry {entry_index}: ")
    boot_data[boot_type][entry_index]["kernel"] = new_kernel

def edit_append(boot_data, boot_type, entry_index, current_append):
    """Edits the append options of a boot entry."""
    new_append = input(f"Enter new append options for {boot_type} entry {entry_index}: ")
    boot_data[boot_type][entry_index]["append"] = new_append

def toggle_persistence(boot_data, boot_type, entry_index):
    """Toggles the persistence flag of a boot entry."""
    if "persistent" in boot_data[boot_type][entry_index]:
        boot_data[boot_type][entry_index]["persistent"] = not boot_data[boot_type][entry_index]["persistent"]
    else:
        boot_data[boot_type][entry_index]["persistent"] = True

def update_entry(boot_data, boot_type, entry_index):
    """Updates a boot entry."""
    entry = boot_data[boot_type][entry_index]
    if boot_type == "efi":
        update_efi_boot_vars(entry)
    elif boot_type == "legacy":
        update_extlinux_conf(boot_data["legacy"]) #extlinux needs all entries to rewrite the file.

def update_efi_boot_vars(efi_entry):
    """Updates EFI boot variables with backup."""
    backup_file = "/tmp/efi_boot_vars.bak"

    try:
        # Create a backup of the current EFI boot variables
        efibootmgr_output = subprocess.check_output(["efibootmgr", "-v"]).decode()
        with open(backup_file, "w") as f:
            f.write(efibootmgr_output)

        boot_num_match = re.search(r'Boot(\d+)\*', efi_entry["label"])
        if boot_num_match:
            boot_num = boot_num_match.group(1)
        else:
            logging.error("Could not determine boot number from label.")
            return

        # Delete the existing boot entry
        subprocess.run(["efibootmgr", "-b", boot_num, "-B"], check=True)

        # Create a new boot entry with the updated values
        cmd = ["efibootmgr", "-c", "-l", efi_entry["kernel"], "-L", efi_entry["label"]]

        # Handle append options (if available)
        if "append" in efi_entry and efi_entry["append"]:
            cmd.extend(["-o", efi_entry["append"]]) # this might need to be adjusted based on how append is to be handled

        subprocess.run(cmd, check=True)

        # Update the boot order (optional, but recommended)
        boot_order_output = subprocess.check_output(["efibootmgr", "-v"]).decode()
        boot_order_match = re.search(r'BootOrder: ([\d,]+)', boot_order_output)
        if boot_order_match:
            boot_order = boot_order_match.group(1)
            new_boot_order = boot_order.replace(boot_num, boot_num) # Ensures boot number is in the order.
            subprocess.run(["efibootmgr", "-o", new_boot_order], check=True)
        else:
            logging.warning("Could not determine boot order.")

        logging.info(f"EFI boot entry {boot_num} updated successfully (backup created: {backup_file}).")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error updating EFI boot variables: {e}")
        # Restore the backup if an error occurs
        if os.path.exists(backup_file):
            try:
                subprocess.run(["efibootmgr", "-v"], check=True) #print current variables.
                logging.info("Original EFI boot variables restored from backup.")
            except:
                logging.error("Error printing original efi variables")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        if os.path.exists(backup_file):
            try:
                subprocess.run(["efibootmgr", "-v"], check=True) #print current variables.
                logging.info("Original EFI boot variables restored from backup.")
            except:
                logging.error("Error printing original efi variables")

def update_extlinux_conf(legacy_entries, config_file="/boot/extlinux/extlinux.conf"):
    """Updates extlinux.conf with backup."""
    backup_file = config_file + ".bak"

    try:
        # Create a backup of the original file
        shutil.copy2(config_file, backup_file)

        with open(config_file, "r") as f:
            lines = f.readlines()

        new_lines = []
        current_entry = {}
        entry_index = 0

        for line in lines:
            line = line.strip()

            if line.startswith("label"):
                if current_entry:
                    # Replace the old entry with the updated entry
                    if entry_index < len(legacy_entries):
                        new_lines.extend(generate_extlinux_entry_lines(legacy_entries[entry_index]))
                        entry_index += 1
                    else:
                        new_lines.extend(generate_extlinux_entry_lines(current_entry)) #if there is no entry to replace, write the old data.
                current_entry = {}
                current_entry["label"] = line.split("label")[1].strip()
                new_lines.append(line + "\n")

            elif line.startswith("kernel"):
                current_entry["kernel"] = line.split("kernel")[1].strip()
                new_lines.append(line + "\n")

            elif line.startswith("append"):
                current_entry["append"] = line.split("append")[1].strip()
                new_lines.append(line + "\n")

            else:
                new_lines.append(line + "\n")

        # Handle the last entry
        if current_entry:
            if entry_index < len(legacy_entries):
                new_lines.extend(generate_extlinux_entry_lines(legacy_entries[entry_index]))
            else:
                new_lines.extend(generate_extlinux_entry_lines(current_entry))

        # Write the updated configuration
        with open(config_file, "w") as f:
            f.writelines(new_lines)

        logging.info(f"extlinux.conf updated successfully (backup created: {backup_file}).")

    except OSError as e:
        logging.error(f"Error updating extlinux.conf: {e}")
        # Restore the backup if an error occurs
        if os.path.exists(backup_file):
            shutil.move(backup_file, config_file)
            logging.info("Original extlinux.conf restored from backup.")

def generate_extlinux_entry_lines(entry):
    """Generates a list of lines for an extlinux entry."""
    lines = []
    lines.append(f"label {entry.get('label', '')}\n")
    lines.append(f"kernel {entry.get('kernel', '')}\n")
    if "append" in entry and entry["append"]:
        lines.append(f"append {entry['append']}\n")
    return lines

if __name__ == "__main__":
    check_root()
    boot_data = build_boot_data()
    boot_data = mark_default_kernels(boot_data)
    xml_output = generate_openbox_xml(boot_data)
    print(xml_output)
