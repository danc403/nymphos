# Dynamic Docklet

The Dynamic Docklet is a custom Plank docklet that allows you to dynamically load and execute `.desktop` files. Instead of adding static launchers to Plank's `Items` list, this docklet uses a configuration setting to specify the path to a `.desktop` file.

## Features

* **Dynamic Launcher Loading:** Loads `.desktop` files based on a configuration setting.
* **Accessibility:** Ensures accessible labels for buttons and uses notifications for error messages.
* **Localization Support:** Leverages `.desktop` file localization for application names.
* **Configuration-Based Management:** Uses Plank's configuration for easy launcher management.
* **Optional Signal-based Menu Refresh:** Refreshes the menu when receiving a `SIGUSR1` signal, providing an optional mechanism for dynamic updates.

## Usage

1.  **Create or Provide a `.desktop` File:**
    * You can either create a new `.desktop` file or use an existing one. If creating a new one, ensure it is an Openbox pipe menu.
2.  **Use the `dynamic-launcher` Tool:** Use the `dynamic-launcher` tool (see below) to add the `.desktop` file path to Plank's configuration.
3.  **Add the Docklet to Plank:** Add the "Dynamic Dock Item" docklet to your Plank dock.
4.  **Launch:** Click the docklet to launch the application.

## Configuration

The docklet uses the `DynamicDocklet.desktop_file` setting in Plank's configuration file (e.g., `/etc/xdg/plank/dock1/settings`).

## Optional Signal Handling

* The docklet listens for the `SIGUSR1` signal.
* When the signal is received, the docklet refreshes the menu by re-launching the `.desktop` file.
* **Note:** Signal handling is an optional feature. Applications that do not require dynamic menu updates do not need to send signals.

## Process ID Management

* The docklet saves its process ID (PID) to a file named `/tmp/nymph-plank-docklet-<desktop_file_name>.pid`, where `<desktop_file_name>` is derived from the `.desktop` file's name.
* This allows external scripts to send signals to the docklet for menu refresh.

## Localization

The docklet uses the system's `.desktop` file localization. Localize the `.desktop` files using standard `.desktop` localization. The docklet name and error messages are localized using gettext.

## Building

To build the docklet, use the standard Plank build process.

## Contributing

Contributions are welcome! Please submit pull requests or bug reports.

## License

MIT - Free for any purpose.

## Dynamic Launcher Tool

The `dynamic-launcher` tool is a Python script that simplifies the process of creating `.desktop` files and configuring the Dynamic Docklet in Plank.

### Usage

```bash
./dynamic-launcher.py --create <app_name> <script_path> <icon_name> [--dock <dock_number>]
# OR
./dynamic-launcher.py --use <desktop_file_path> [--dock <dock_number>]
