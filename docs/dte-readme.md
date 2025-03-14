# Nymph Desktop Environment (DTE)

## Introduction

The Nymph Desktop Environment (DTE) is a custom Linux desktop environment designed with a primary focus on accessibility for blind and low-vision users. It leverages the lightweight and highly configurable Openbox window manager, enhanced with custom tools and scripts to provide a user-friendly and accessible experience.

## Key Features

* **Accessibility First:**
    * Integrated accessibility from the kernel level with `speckup` and `brltty`.
    * Custom tools and menus designed for screen reader compatibility.
    * `orca` screen reader and `speech-dispatcher` for text-to-speech.
    * `luciole-fonts-ttf` for improved font readability.
* **Lightweight and Customizable:**
    * Openbox window manager for a responsive and flexible environment.
    * Plank dock with custom docklets for dynamic menus and system access.
    * Custom Python scripts for system management and configuration.
* **Dynamic Menus and Tools:**
    * Pipe menus for up-to-date system information and actions.
    * `drive-mounter.py` for accessible device management.
    * `media-menu` for accessible media management.
    * `keybindings.py` for accessible keybinding management.
* **Application Suite:**
    * Thunar and Caja file managers.
    * Unicode terminal emulator.
    * Firefox web browser.
    * Geany text editor/IDE.
    * Full LAMP stack available.
* **Package Management:**
    * Microdnf for efficient package management.
* **Theming:**
    * Whitesur theme with light and dark options.
* **System Integration:**
    * Files and configurations placed in standard system locations for consistency.
* **Installation:**
    * Full custom distribution.
    * Warning about overwriting sda drive.

## Installation

(To be filled with detailed installation instructions)

## Configuration

* **Openbox:** Configuration files located in `~/.config/openbox/`.
* **Plank:** Configuration files located in `/etc/xdg/plank/`.
* **Custom Tools:** Configuration options available through environment variables and command-line arguments.
* **Keybindings:** managed by `keybindings.py`

## Custom Tools

* **`dynamic-launcher.py`:** Creates `.desktop` files and configures the Dynamic Docklet.
* **`drive-mounter.py`:** Manages mount and unmount operations for removable and optical drives.
* **`media-menu`:** Provides an accessible menu for media control.
* **`keybindings.py`:** Manages system keybindings.
* (Add other custom tools here)

## Package List

(Insert the list of packages you provided earlier)

## Development

(To be filled with information about contributing and building the DTE)

## Contributing

(To be filled with guidelines for contributing to the project)

## Roadmap

* (Add future development goals here)
* Merge openbox, plank, custom scripts, and other related items into a single package.
* Accessible method for dual boot installation.
* Comprehensive testing on varied hardware.
* Community building.

## License

(Specify the license here)
