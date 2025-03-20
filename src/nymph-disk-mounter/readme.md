# Nymph Disk Mounter

Nymph Disk Mounter is a simple GTK3 application for managing and mounting disks. It provides a user-friendly interface to list removable and optical devices, mount/unmount them, and open them in your file manager.

## Features

*   **List Disks:** Displays a list of removable and optical media devices connected to your system.
*   **Mount/Unmount:**  Allows mounting and unmounting of supported devices.
*   **Open in File Manager:** Mounts the device and opens it in your default file manager (e.g., Thunar, Nautilus, Dolphin).
*   **Eject:** Ejects removable media (if the device supports it).
*   **Device Information:** Displays detailed information about a selected device.
*   **Display Options:** Allows you to choose whether to display the device label or filename in the list.
*   **Unmount All:** Provides a convenient button to unmount all mounted removable or optical devices.
*   **Configuration via Environment Variables:** Customizable behavior using environment variables.

## Requirements

*   GTK3
*   Vala (for compilation)
*   udisks (for disk management)
*   A file manager (Thunar, Nautilus, Dolphin, etc.)
*   pkexec (for mounting devices if necessary)

## Installation

1.  **Install Dependencies:**

    ```bash
    # Debian/Ubuntu
    sudo apt update
    sudo apt install valac libgtk-3-dev udisks2

    # Fedora
    sudo dnf install vala gtk3-devel udisks2
    ```

## Usage

1.  **Run the Application:**

    ```bash
    ./nymph-disk-mounter  # Or, if installed: nymph-disk-mounter
    ```

2.  **Device List:**

    The main window will display a list of connected removable and optical media.

3.  **Device Actions:**

    *   Click on a device entry to open a menu with options like "Mount", "Unmount", "Open" (in file manager), "Eject", and "Info".
    *   Use "Display Options" to switch between showing the device label or filename in the main list.

## Configuration

The behavior of Nymph Disk Mounter can be customized using environment variables:

*   `OBDEVICEMENU_REMOVABLE_REGEX`: Regular expression to identify removable devices.  Default: `/dev/sd[a-z][0-9]*`
*   `OBDEVICEMENU_OPTICAL_REGEX`: Regular expression to identify optical devices. Default: `/dev/sr[0-9]*`
*   `OBDEVICEMENU_SHOW_INTERNAL`: Set to `1` to show internal devices in the removable media list. Default: `0` (hidden).
*   `OBDEVICEMENU_BLACKLIST`:  Space-separated list of strings. If a device's `udisks --show-info` output contains any of these strings, the device will be ignored. This is useful for excluding certain devices.
*   `FILEMANAGER`: Specifies the file manager to use when opening a mounted device.  If not set, the application attempts to detect a suitable file manager (Thunar, Nautilus, Dolphin) based on your desktop environment. It defaults to `thunar` if none are found.

**Example:**

```bash
export OBDEVICEMENU_SHOW_INTERNAL=1
export FILEMANAGER=nautilus
./nymph-disk-mounter
```

## Localization

The application uses `gettext` for localization.  Make sure you have the appropriate locale files installed on your system. The application looks for translation files in `/usr/share/locale`.

## License

This program is licensed under the GNU General Public License, version 3 or later.  See the `COPYING` file for details.
