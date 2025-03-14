# Nymph Theme Switcher

This application provides a simple graphical interface for changing Openbox themes. It allows users to easily switch between available themes and, for administrators, apply themes system-wide.

**Features:**

* **Theme Listing:** Automatically scans standard theme directories and displays available Openbox themes in a dropdown menu.
* **User Theme Switching:** Allows regular users to change their personal Openbox theme.
* **System Theme Switching (Admin):** Provides a checkbox for administrators to apply themes system-wide, affecting all users.
* **Current Theme Display:** Shows the currently active theme when the application is launched.
* **Uses `openbox --show-current-theme`:** This command is the most reliable way to get the current Openbox theme.
* **Localization:** The application's user interface is localized for multiple languages, including Spanish, French, German, Japanese, Simplified Chinese, Russian, Portuguese, and Italian.
* **Desktop Integration:** Includes a `.desktop` file for easy launching from application menus.

**Requirements:**

* Openbox window manager
* Vala compiler
* GTK+ 3.0 development libraries
* `gettext` for localization

**How it Works:**

The application scans the standard XDG data directories (e.g., `/usr/share/themes`, `~/.themes`) for Openbox theme directories. A theme directory is identified by the presence of an `openbox-3/themerc` file. The application then displays the list of found themes in a `ComboBox`.

When a user selects a theme and clicks "Apply Theme," the application executes the `openbox --reconfigure --theme <theme_path>` command. If the "System Theme (Admin)" checkbox is checked, the application uses `sudo` to execute the command, allowing administrators to change the system-wide theme. The application uses the command `openbox --show-current-theme` to get the current applied theme.

**Compilation and Installation:**

1.  **Clone or download the project:**
    * Place the `nymph_theme_switcher.vala` and the `nymph-theme-switcher.desktop` file into the same directory.
    * Create a directory called `po` in the same directory.
    * Place the `nymph-theme-switcher.pot` and the .po files into the `po` directory.

2.  **Compile the application:**

    ```bash
    valac nymph_theme_switcher.vala --pkg gtk+-3.0
    ```

    This will generate an executable file named `nymph_theme_switcher`.

3.  **Install the executable:**

    ```bash
    sudo cp nymph_theme_switcher /usr/bin/
    ```

4.  **Install the `.desktop` file:**

    ```bash
    sudo cp nymph-theme-switcher.desktop /usr/share/applications/
    ```

5.  **Install the localization files:**

    * Navigate to the `po` directory.
    * Compile the `.po` files to `.mo` files:

        ```bash
        msgfmt es.po --output-file=es.mo
        # Repeat for other languages (fr.po, de.po, etc.)
        ```

    * Install the `.mo` files:

        ```bash
        sudo mkdir -p /usr/share/locale/es/LC_MESSAGES/
        sudo cp es.mo /usr/share/locale/es/LC_MESSAGES/nymph-theme-switcher.mo
        # Repeat for other languages
        ```

6.  **Optional: Install an icon:**

    * Copy the icon files to the appropriate subdirectories within `/usr/share/icons/hicolor/`.
    * Update the icon cache: `sudo gtk-update-icon-cache /usr/share/icons/hicolor/`

7.  **Optional: install the README:**
    * sudo mkdir -p /usr/share/doc/nymph-theme-switcher/
    * sudo cp README.md /usr/share/doc/nymph-theme-switcher/

**Usage:**

1.  **Launch the application:** Open the application from your application menu.
2.  **Select a theme:** Choose a theme from the dropdown menu.
3.  **Apply the theme:** Click the "Apply Theme" button.
4.  **System-wide theme (Admin):** Check the "System Theme (Admin)" checkbox before applying the theme to change it system-wide. You will be prompted for your administrator password.

**Important Notes:**

* This application is specifically designed for the Openbox window manager.
* System-wide theme changes require administrator privileges.
* The application uses the command `openbox --show-current-theme` to get the current theme. This command is the most reliable way to get the current Openbox theme.
* The application uses the command `openbox --reconfigure --theme <theme_path>` to change the theme.
* The application has localization for multiple languages, make sure the correct locale is set on the computer.
