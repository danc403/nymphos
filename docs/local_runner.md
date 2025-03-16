# RPM Build Automation with Docker

This document explains how to use the `local_runner.py` script to automate the building of RPM packages for your projects using Docker. The script is designed to be run within a Git repository and leverages Docker for a consistent build environment.

## Prerequisites

* **Docker:** Docker must be installed and running on your system.
* **Git Repository:** The script must be run from within a Git repository.
* **Dockerfile:** A Dockerfile named `d-nymph` should be located one level above the root of your Git repository. This Dockerfile should define an environment suitable for building RPMs (e.g., based on Rocky Linux with `rpm-build` and other necessary tools installed).
* **Project Structure:**
    * At the root of your Git repository, you should have a directory named `tarballs`.
    * Inside the `tarballs` directory, create subdirectories for each package you intend to build. The name of each subdirectory should correspond to the name of the package.
    * Within each package subdirectory, place the `.spec` file and the source tarball (e.g., `.tar.gz`, `.tar.xz`) for that package.
* **RPM Output Directories:** At the root of your Git repository, you should have directories named `rpms` and `srpms`. The built RPMs and SRPMs will be placed in these directories.

## Script Location

The `local_runner.py` script is intended to be placed in the `.git/workflows/` directory of your Git repository. This location is a common place for automation scripts and is used by the `local_runner.yml` GitHub Actions workflow.

## How it Works

The `local_runner.py` script performs the following steps:

1.  **Locates Repository Root:** It uses Git commands to find the root directory of the current Git repository.
2.  **Locates Dockerfile:** It assumes the `d-nymph` Dockerfile is located one level above the repository root.
3.  **Builds Docker Image (if needed):**
    * It checks if the `d-nymph` Dockerfile exists. If so, it builds the Docker image `nymph-rpm-builder`.
    * If the Dockerfile doesn't exist, it checks if the `nymph-rpm-builder` image already exists.
    * If the image doesn't exist, it generates a basic Dockerfile and builds the image.
4.  **Runs Docker Container:** It runs a Docker container named `nymph-rpm-builder`, mounting the following directories from your host system into the container:
    * The root of your Git repository (to `/build/src`).
    * The `tarballs` directory from your repository (to `/build/tarballs`).
    * The `rpms` directory from your repository (to `/build/RPMS`).
    * The `srpms` directory from your repository (to `/build/SRPMS`).
5.  **Builds Packages:**
    * It iterates through the subdirectories within the `tarballs` directory. Each subdirectory is assumed to represent a package to be built.
    * You can specify specific packages to build using the `-p` or `--package` option. If no package is specified or if `*` is used, it will attempt to build all packages found in the `tarballs` directory.
    * It parses the `.spec` file to extract the package name, version, and source tarball name.
    * It copies the source tarball into the container's source directory within the Docker container.
    * It uses `rpmbuild` within the container to build the SRPM and RPM packages.
    * The resulting SRPMs are moved to the `srpms` directory on your host.
    * The resulting RPMs are moved to a subdirectory within the `rpms` directory on your host, named after the package.
6.  **Cleans Up:** After building a package, it cleans up the source directory within the container.

## Usage

Navigate to the root of your Git repository in your terminal and run the script:

```bash
python .git/workflows/local_runner.py
This will attempt to build all packages found in the tarballs directory.
Build Specific Packages
To build only specific packages, use the -p or --package option followed by a comma-separated list of the package subdirectory names in the tarballs directory:
Bash
Copy code
python .git/workflows/local_runner.py -p <package_name1>,<package_name2>,<package_name3>
For example, if you have packages in tarballs/my-app and tarballs/another-app, you would run:
Bash
Copy code
python .git/workflows/local_runner.py -p my-app,another-app
To build a single package:
Bash
Copy code
python .git/workflows/local_runner.py -p my-app
GitHub Actions Integration
To automate the RPM build process in your CI/CD pipeline, you can use the local_runner.yml GitHub Actions workflow. This workflow will trigger on pushes or pull requests that modify files within the tarballs directory.
local_runner.yml Workflow
YAML
Copy code
name: Local RPM Build

on:
  push:
    paths:
      - 'tarballs/**'
  pull_request:
    paths:
      - 'tarballs/**'

jobs:
  build_rpm:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Determine changed package(s)
        id: changed_package
        run: |
          changed_files=$(git diff --name-only HEAD^ HEAD)
          packages_changed=""
          while IFS= read -r file; do
            if [[ "<span class="math-inline">file" \=\~ ^tarballs\\/\(\[^/\]\+\)\\/ \]\]; then
package\_name\="</span>{BASH_REMATCH[1]}"
              if [[ -z "$packages_changed" ]]; then
                packages_changed="$package_name"
              else
                packages_changed="$packages_changed,$package_name"
              fi
            fi
          done <<< "$changed_files"
          echo "packages=$packages_changed" >> "<span class="math-inline">GITHUB\_OUTPUT"
\- name\: Build RPM\(s\)
run\: \|
python \.git/workflows/local\_runner\.py \-p "</span>{{ steps.changed_package.outputs.packages }}"
        env:
          DOCKER_BUILDKIT: 1 # Optional: Enable BuildKit for potentially faster builds
This workflow will:
1. Trigger when changes are made in the tarballs directory.
2. Use git diff to determine which package subdirectories were modified.
3. Pass the list of changed package names to the local_runner.py script using the -p option.
Customization
• Dockerfile (d-nymph): Customize the d-nymph Dockerfile to include the specific tools and dependencies required to build your RPM packages.
• Directory Names: If you use different names for your tarballs, RPMs, or SRPMs directories, you will need to modify the script accordingly.
• RPM Build Options: If you need to pass specific options to rpmbuild, you would need to modify the build_rpm function in the script.
• GitHub Actions Workflow:
• You can adjust the triggers (on) to suit your workflow needs.
• You can add additional steps to the workflow, such as uploading the built RPMs and SRPMs as artifacts or publishing them to a repository.
This setup provides a powerful and flexible system for automating your RPM build process, both locally and in your CI/CD pipeline.

