# Nymph Power Menu

Nymph Power Menu is a simple GTK+ 3 application for NymphOS that provides a graphical interface for logging out, shutting down, and rebooting the system.

## Features

* **Log Out:** Logs the current user out of Openbox.
* **Shut Down:** Shuts down the system.
* **Reboot:** Reboots the system.
* **Localization:** Supports multiple languages (French, Spanish, German, Japanese).

## Requirements

* NymphOS
* GTK+ 3
* Vala compiler
* `gettext` (for localization)
* `sudo`

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd nymph-power-menu
    ```

2.  **Create the Source Archive:**

    ```bash
    ./create_source_archive.sh
    ```

e3.  **Build the RPM Package:**

    ```bash
    rpmbuild -ba nymph-power-menu.spec
    ```

4.  **Install the RPM Package:**

    ```bash
    sudo rpm -ivh /path/to/nymph-power-menu-*.rpm
    ```

## Usage

1.  Launch "Nymph Power Menu" from your application menu.
2.  Click the desired button (Log Out, Shut Down, or Reboot).

## Localization

Follow the same localization instructions as for `nymph-wallpaper-switcher`.

## Contributing

Follow the same contributing instructions as for `nymph-wallpaper-switcher`.

## Development

Follow the same development instructions as for `nymph-wallpaper-switcher`.

## License

This project is licensed under the GPL license. See the
