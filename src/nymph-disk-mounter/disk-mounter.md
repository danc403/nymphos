# drive-mounter.py

A dynamic Openbox pipe menu for mounting, unmounting, and managing removable and optical drives.

## User Guide

This application is included as a core component of your distribution. It is available in your application dock or bottom dock. Click the icon to access the device management menu.

### Usage

1.  Click the device management icon in your application dock or bottom dock.
2.  Choose a device from the list to mount, unmount, eject, or view device information.
3.  Use the "Display Options" menu to toggle between displaying device labels or filenames.
4.  Use the "Unmount all" options to unmount all removable or optical devices.

## Development

## Development

### Overview

`drive-mounter.py` generates a dynamic Openbox pipe menu by querying `udisks2` for device information. It uses regular expressions to filter and sort devices. The menu supports mounting, unmounting, ejecting, and displaying device information.

### Location

The script is installed as a system package and is typically located at `/usr/bin/drive-mounter.py`.

### Desktop File Location

The desktop file, which integrates the application with the desktop environment, is typically located at `/usr/share/applications/drive-mounter.desktop`.

### Dependencies

* Python 3
* `udisks2`
* A file manager (e.g., `thunar`, `nautilus`, `dolphin`)
* `pkexec`

### Environment Variables

* `OBDEVICEMENU_REMOVABLE_REGEX`: Regular expression for removable devices (default: `/dev/sd[a-z][0-9]*`).
* `OBDEVICEMENU_OPTICAL_REGEX`: Regular expression for optical devices (default: `/dev/sr[0-9]*`).
* `OBDEVICEMENU_SHOW_INTERNAL`: Set to `1` to show internal drives (default: `0`).
* `OBDEVICEMENU_BLACKLIST`: Space-separated list of strings to blacklist devices (e.g., `loop iso`).
* `FILEMANAGER`: Specify the file manager to use (if not set, the script will attempt to auto-detect).
* `DESKTOP_SESSION`: used to detect the desktop environment.
* `XDG_CURRENT_DESKTOP`: used to detect the desktop environment.

### Regular Expressions

* **Removable Devices:** The default regex `/dev/sd[a-z][0-9]*` matches devices like `/dev/sdb`, `/dev/sdc1`, etc.
* **Optical Devices:** The default regex `/dev/sr[0-9]*` matches devices like `/dev/sr0`, `/dev/sr1`, etc.
* These regexes can be customized using the `OBDEVICEMENU_REMOVABLE_REGEX` and `OBDEVICEMENU_OPTICAL_REGEX` environment variables.

### Information Sources

* **`udisks2`:** The script uses `udisks2` to enumerate devices and retrieve device information.
* **`/tmp/obdevicemenu_display_options`:** A temporary file stores the display options (filename or label).
* **Environment Variables:** The script reads environment variables for configuration.

### Privilege Escalation

* The script uses `pkexec` to elevate privileges when mounting internal drives that require root access.
* This ensures that users are prompted for their password in a secure and controlled manner.

### Error Handling

* The script handles `subprocess.CalledProcessError` exceptions to catch errors during command execution.
* It also handles `re.error` exceptions to catch errors during regex compilation.
* It handles `FileNotFoundError` exceptions to catch errors when the display option file is missing.
* It displays error messages to the user when mount or unmount operations fail.

### Menu Updates

* The menu is refreshed after each mount, unmount, or eject operation to reflect the updated device status.
* Menu labels include the device's mount status (e.g., "Device Name (Mounted)").
* Errors in mount and unmount operations are also reflected in the menu labels.

### Signal-Based Menu Refresh

* To ensure immediate menu updates, the script sends a `SIGUSR1` signal to the Plank docklet after each mount, unmount, or eject operation.
* The docklet, when receiving the signal, triggers a menu refresh by re-launching the `.desktop` file.
* The script dynamically determines the `.desktop` file name using `__file__` and searches the standard system locations for it.
* The docklet's process ID (PID) is saved to `/tmp/nymph-plank-docklet-<desktop_file_name>.pid`, where `<desktop_file_name>` is derived from the `.desktop` file's name.

### Localization

* The script generates menu labels that can be localized using `.desktop` file localization.
* This allows the menu to be displayed in the user's preferred language.

### Pipe Menu Integration

* This script is designed to function as an Openbox pipe menu.
* It is called each time the menu is opened, and generates menu items dynamically.
* To update the menu after an action, the menu must be closed and reopened.
