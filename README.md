# NymphOS / NymphDesktop

Welcome to the NymphOS and NymphDesktop project! This initiative aims to create a fully accessible and user-friendly Linux distribution, with a strong focus on empowering blind and visually impaired users. We are building a complete operating system from the ground up, integrating server capabilities and a customizable desktop environment.

## Project Goals

* **Accessibility First:** Provide a fully accessible installation and user experience for blind and visually impaired users.
* **User Empowerment:** Enable users to install, configure, and manage their systems independently.
* **Server Integration:** Include a complete LAMP stack and other server tools for versatile deployment.
* **Customizable Desktop:** Offer a lightweight and highly customizable desktop environment (NymphDesktop) based on Openbox.
* **Future AI Integration:** Integrate an AI assistant with voice recognition and a custom TTS engine with neural voices.

## Current Status

This repository is currently in active development. We are using the `main` branch for development until a stable release is ready. At that point, `main` will become the release branch, and development will continue on a `dev` branch.

## Directory Structure

* **`src/`:** Contains the source code for all packages, including NymphOS and NymphDesktop components.
    * Each package has its own subdirectory (e.g., `src/nymph-plank`, `src/openbox`).
* **`tarballs/`:** Holds the tarballs for pre-packaged software and testing.
* **`SRPMs/`:** Contains Source RPMs (SRPMs) for building packages.
* **`RPMs/`:** Contains binary RPMs for installation.

## Development Workflow

1.  **Development Branch (`main` initially):** All development work occurs in the `main` branch (which will be `dev` after the first release).
2.  **Source Code:** Source code is managed within the `src/` directory.
3.  **Tarballs and RPMs:** Tarballs, SRPMs, and RPMs are built and tested in the development branch.
4.  **Release Branch (`main` after release):** Once a release is deemed stable, the RPMs are moved to the `main` branch for distribution.

## Key Components

* **NymphOS:** The core operating system, including the Linux kernel, system utilities, and server components.
* **NymphDesktop:** A lightweight and accessible desktop environment based on Openbox, featuring custom docklets, menus, and themes.
* **Nymph Accessibility:** A set of tools and configurations to enhance accessibility.
* **Dynamic Docklet:** A Plank docklet that dynamically loads and executes `.desktop` files.
* **Dynamic Launcher Tool:** A python tool that builds the dynamic docklets `.desktop` files.

## Contributing

Contributions are welcome! Please submit pull requests to the `main` branch (or `dev` after the first release).

* **Bug Reports:** If you find a bug, please open an issue.
* **Feature Requests:** If you have a feature request, please open an issue.
* **Code Contributions:** Follow the project's coding standards and submit pull requests with clear descriptions.
* **Translations:** Help translate the project into different languages.

## Building

Instructions for building NymphOS and NymphDesktop will be provided in the documentation.

## Installation

Installation instructions will be provided in the documentation.

## Future Plans

* Implement the AI assistant and custom TTS engine.
* Expand hardware compatibility.
* Enhance accessibility features.
* Build a strong community around the project.

## License

Varied

## Contact

Copyright (c) 2025 Dan Carpenter <danc403@gmail.com>
