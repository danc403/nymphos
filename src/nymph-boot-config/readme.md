# Nymph Boot Configuration Tool

This is a GTK# application for configuring the bootloader on NymphOS. It allows users to view and modify boot entries, manage persistent boot settings, and creates a revert script for non-persistent boot changes.

**Disclaimer:** This application is currently in development and may contain bugs or incomplete features. Use with caution and always back up your boot configuration before making changes.

## Features

*   **Boot Entry Management:**
    *   Displays boot entries from various sources (extlinux.conf, EFI boot variables).
    *   Categorizes boot entries into types: legacy, EFI, Windows, macOS, Linux.
*   **Boot Entry Editing:**
    *   Allows modification of boot entry labels, kernel paths, and append options.
    *   Supports updating both Extlinux and EFI boot configurations.
*   **Persistent Boot Option:**
    *   Provides a toggle to enable/disable persistent boot changes.
*   **Revert Script Creation:**
    *   Generates a revert script ( `/usr/local/bin/revert_boot.sh` ) to undo boot configuration changes (only for non-persistent mode).
    *   Adds the revert script to OpenRC to run on next boot.

## Requirements

*   Mono runtime environment (required for GTK# applications)
*   GTK# libraries
*   `efibootmgr` (for EFI boot variable management)
*   Root privileges (required to modify boot configuration files and EFI variables)

## Usage

1.  **Build the application:**

    *   This assumes you have a development environment set up.
    *   Use a suitable build tool for GTK# applications (e.g., `xbuild`, `msbuild`, or an IDE like MonoDevelop or Visual Studio).

2.  **Run the application:**

    *   Navigate to the compiled executable in your terminal.
    *   Execute the application with root privileges: `sudo ./NymphBootConfig.exe` (replace with the actual executable name).

3.  **Interact with the UI:**

    *   The main window displays a list of boot entries in a treeview.
    *   Select a boot entry to view and edit its details in the Details Panel.
    *   Modify the label, kernel, and append fields as needed.
    *   Click the "Update" button to save the changes.
    *   Toggle the "Persistent Boot" option to control whether changes are permanent.

## Important Notes

*   **Backup:**  Always back up your existing boot configuration files (e.g., `extlinux.conf`) and EFI boot variables before using this tool.
*   **Root Privileges:** The application requires root privileges to modify boot configuration.
*   **Revert Script:**  If "Persistent Boot" is disabled, the application creates a revert script that will automatically restore the original boot configuration on the next reboot.  Ensure you understand the implications before disabling persistent boot.
*   **EFI Partition Detection**: The script attempts to identify the EFI partition, but user verification may be needed.

## Known Issues and Future Development

This application is a work in progress, and there are several areas that require further development:

*   **Error Handling:**  Improved error handling and user feedback are needed. The application should gracefully handle unexpected situations and provide informative error messages.
*   **Data Validation:**  Input validation should be implemented to prevent invalid or dangerous values from being entered into the boot entry fields.
*   **Config File Parsing**: Improve parsing for extlinux and especially EFI configuration.  The EFI parsing is extremely brittle and relies on fragile regexes against the output of efibootmgr.
*   **EFI Partition Handling**: Refine the process of identifying the EFI partition.
*   **Revert Script Reliability:** Enhanced testing and robustness of the generated revert script, especially handling edge cases and error conditions.
*   **Boot Entry Creation:**  Implement functionality to add new boot entries.
*   **Boot Entry Deletion:**  Implement functionality to delete existing boot entries.
*   **GUI Improvements:**  Enhance the user interface with better layout, icons, and usability features.
*   **Windows/macOS/Linux Boot Detection:** Implement the parsing of Windows, MacOS, and Linux boot configurations.
*   **Chainloading Support:** Add a GUI for creating chainload boot entries.
*   **Configuration File:** Implement a configuration file for application settings, such as default kernel paths and mount points.
*   **Logging:** Implement logging for debugging purposes.
*   **Security:** Review for potential security vulnerabilities.

## Contributing

Contributions are welcome!  If you find a bug, have a feature request, or would like to contribute code, please open an issue or submit a pull request on [Insert link to your repository here].

## License

MIT License

