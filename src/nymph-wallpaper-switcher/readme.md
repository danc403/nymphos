# Nymph Wallpaper Switcher

Nymph Wallpaper Switcher is a simple GTK+ 3 application for NymphOS that allows users to easily change their desktop wallpaper. It scans common wallpaper directories and provides a user-friendly interface to select and apply wallpapers.

## Features

* **Easy Wallpaper Selection:** Provides a dropdown list of available wallpapers.
* **Wallpaper Application:** Applies the selected wallpaper with a single click.
* **Automatic Wallpaper Detection:** Scans standard system wallpaper directories.
* **Localization:** Supports multiple languages (French, Spanish, German, Japanese).
* **Persistent Wallpaper:** Remembers the last selected wallpaper.

## Requirements

* NymphOS
* GTK+ 3
* Vala compiler
* `gettext` (for localization)

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd nymph-wallpaper-switcher
    ```

2.  **Create the Source Archive:**

    ```bash
    ./create_source_archive.sh
    ```

3.  **Build the RPM Package:**

    ```bash
    rpmbuild -ba nymph-wallpaper-switcher.spec
    ```

4.  **Install the RPM Package:**

    ```bash
    sudo rpm -ivh /path/to/nymph-wallpaper-switcher-*.rpm
    ```

## Usage

1.  Launch "Nymph Wallpaper Switcher" from your application menu.
2.  Select a wallpaper from the dropdown list.
3.  Click "Apply Wallpaper" to change your desktop background.

## Configuration

* **Wallpaper Directories:** The application automatically scans standard system wallpaper directories. To add custom directories, you can modify the `nymph-wallpaper-switcher.vala` source code.
* **Wallpaper Setting Commands:** The application tries several common wallpaper setting commands. If your system requires a different command, you can modify the `set_wallpaper` function in `nymph-wallpaper-switcher.vala`.

## Localization

This application supports localization. To contribute translations:

1.  **Generate the `.pot` File:**

    ```bash
    xgettext --package-name=nymph-wallpaper-switcher --package-version=1.0 --output=po/nymph-wallpaper-switcher.pot nymph-wallpaper-switcher.vala
    ```

2.  **Create or Update `.po` Files:**

    ```bash
    msginit --locale=<locale_code> --input=po/nymph-wallpaper-switcher.pot --output=po/<locale_code>.po
    ```

    or

    ```bash
    msgmerge -U po/<locale_code>.po po/nymph-wallpaper-switcher.pot
    ```

3.  **Translate the Strings:**

    Edit the `.po` files and fill in the `msgstr` fields.

4.  **Compile `.po` to `.mo`:**

    ```bash
    msgfmt po/<locale_code>.po --output-file=po/<locale_code>.mo
    ```

5.  **Submit a Pull Request:**

    Include the updated `.po` and `.mo` files in your pull request.

## Contributing

Contributions are welcome! Here's how you can help:

* **Report Bugs:** If you find a bug, please open an issue on GitHub.
* **Suggest Features:** Have an idea for a new feature? Open an issue to discuss it.
* **Submit Pull Requests:** If you want to contribute code, please fork the repository and submit a pull request.
* **Improve Documentation:** Help improve the documentation by submitting pull requests with corrections and updates.
* **Provide Translations:** As described in the Localization section.

## Development

To develop this application:

1.  **Install Dependencies:**

    ```bash
    sudo dnf install vala gtk3-devel gettext
    ```

2.  **Compile the Application:**

    ```bash
    valac --pkg gtk+-3.0 nymph-wallpaper-switcher.vala
    ```

3.  **Run the Application:**

    ```bash
    ./nymph-wallpaper-switcher
    ```

## License

This project is licensed under the [License Name] license. See the `LICENSE` file for details.
