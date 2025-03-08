# Building RPMs with `build_rpm.py`

This document outlines how to use the `build_rpm.py` script to build RPM packages for this project. This script is designed to be highly flexible and can run in various environments.

## Prerequisites

* **Python 3:** The script is written in Python 3.
* **RPM Build Tools:** If building directly on the host, you'll need the RPM build tools installed (e.g., `rpmbuild`, `rpmdevtools`).
* **Docker (Optional):** If using Docker, you'll need Docker installed.

## Directory Structure

* **`tarballs/`:** This directory contains subdirectories for each package. Each subdirectory contains the spec files and source tarballs for that package.
* **`rpms/`:** This directory will contain the built RPM packages.
* **`srpms/`:** This directory will contain the built SRPM packages.
* **`build_rpm.py`:** This is the build script.
* **`Dockerfile` (Optional):** This Dockerfile is used to create a consistent build environment.

## Usage

The `build_rpm.py` script can be used in several ways:

### 1. Building with an Existing Dockerfile

If a `Dockerfile` is present in the same directory as the script, the script will build and run a Docker container to build the RPMs.

```bash
python3 build_rpm.py [package1] [package2] ...
• Replace [package1] [package2] ... with the names of the packages you want to build. If no packages are specified, all packages will be built.
2. Generating and Building with a Dockerfile
If no Dockerfile is present and the -d flag is passed, the script will generate a basic Dockerfile, build a Docker image, and run a container to build the RPMs.
Bash
python3 build_rpm.py -d [package1] [package2] ...
• Replace [package1] [package2] ... with the names of the packages you want to build. If no packages are specified, all packages will be built.
3. Building Directly on the Host
If no Dockerfile is present and the -d flag is not passed, the script will attempt to build the RPMs directly on the host system.
Bash
python3 build_rpm.py [package1] [package2] ...
• Replace [package1] [package2] ... with the names of the packages you want to build. If no packages are specified, all packages will be built.
• Note: You must have the necessary RPM build tools and dependencies installed on your host system.
How It Works
The script detects its environment and adapts accordingly:
1. Container Detection: It checks for the container=docker environment variable to determine if it's running inside a Docker container.
2. Dockerfile Detection: It checks for the existence of a Dockerfile in the current directory.
3. Command-Line Arguments: It parses command-line arguments to determine which packages to build.
4. RPM Build Process: It parses spec files, finds source tarballs, and runs rpmbuild to build RPMs and SRPMs.
5. Output: Built RPMs are placed in the rpms/ directory, and SRPMs are placed in the srpms/ directory.
Customizing the Build
• Dockerfile: You can customize the Dockerfile to install specific dependencies or build tools.
• Script Arguments: Use command-line arguments to build specific packages.
• Spec Files: Modify the spec files to customize the build process for individual packages.
GitHub Actions
This script can be used in GitHub Actions workflows to automate the build process. See the .github/workflows/ directory for examples.
Contributing
Feel free to contribute to the development of this build script by submitting pull requests or reporting issues.
Examples
• 
Build all packages using an existing Dockerfile:
Bash
python3 build_rpm.py
• 
Build specific packages using an existing Dockerfile:
Bash
python3 build_rpm.py firefox vlc
• 
Generate a Dockerfile and build all packages:
Bash
python3 build_rpm.py -d
• 
Build a specific package directly on the host:
Bash
python3 build_rpm.py firefox
