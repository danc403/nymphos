#!/usr/bin/env python3
"""
package_lists.py

This script analyzes specified directories for build-related files,
such as spec files, tarballs, SRPMs, and RPMs. It writes the results
to a text file named after the analyzed directory.

Usage:
    python package_lists.py <directory>

Arguments:
    <directory>: The directory to analyze.

You can add the following to your .git/hooks/post-commit to run automatically on changes:
#!/bin/bash

# Check for changes in the tarballs directory
if git diff --name-only HEAD~1 HEAD | grep '^tarballs/' > /dev/null; then
  python3 package_lists.py tarballs
  git add tarballs.txt
  git commit -m "Update tarballs.txt"
fi

# Check for changes in the srpms directory
if git diff --name-only HEAD~1 HEAD | grep '^srpms/' > /dev/null; then
  python3 package_lists.py srpms
  git add srpms.txt
  git commit -m "Update srpms.txt"
fi

# Check for changes in the rpms directory
if git diff --name-only HEAD~1 HEAD | grep '^rpms/' > /dev/null; then
  python3 package_lists.py rpms
  git add rpms.txt
  git commit -m "Update rpms.txt"
fi

# Check for changes in the src directory
if git diff --name-only HEAD~1 HEAD | grep '^src/' > /dev/null; then
  python3 package_lists.py src
  git add src.txt
  git commit -m "Update src.txt"
fi

# Check for changes in the docs directory
if git diff --name-only HEAD~1 HEAD | grep '^docs/' > /dev/null; then
  python3 package_lists.py docs
  git add docs.txt
  git commit -m "Update docs.txt"
fi
"""

import os
import sys

def analyze_build_directory(directory="."):
    """
    Analyzes a directory to identify built packages (spec files)
    and available tarballs, SRPMs, and RPMs.

    Args:
        directory (str): The directory to analyze. Defaults to the current directory.

    Returns:
        dict: A dictionary containing package information.
    """

    package_info = {}
    directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

    for pkg_dir in directories:
        pkg_path = os.path.join(directory, pkg_dir)
        spec_file = os.path.join(pkg_path, f"{pkg_dir}.spec")
        tarballs = [f for f in os.listdir(pkg_path) if f.endswith(('.tar.gz', '.tar.xz', '.tar.bz2'))]
        srpms = [f for f in os.listdir(pkg_path) if f.endswith('.src.rpm')]
        rpms = [f for f in os.listdir(pkg_path) if f.endswith('.rpm')]

        if directory == "tarballs": # only look for spec files in the tarballs directory.
            package_info[pkg_dir] = {
                "spec_file": os.path.exists(spec_file),
                "tarballs": tarballs,
                "srpms": srpms,
                "rpms": rpms,
            }
        else: # otherwise, do not look for spec files.
            package_info[pkg_dir] = {
                "spec_file": False,
                "tarballs": tarballs,
                "srpms": srpms,
                "rpms": rpms,
            }

    return package_info

def write_package_status(package_data, filename="tarballs.txt"):
    """
    Writes the package build status to a file.

    Args:
        package_data (dict): The dictionary returned by analyze_build_directory.
        filename (str): The name of the file to write to. Defaults to "tarballs.txt".
    """

    with open(filename, "w") as f:
        f.write("Package Build Status:\n")
        f.write("-" * 30 + "\n")

        built_packages = []
        missing_spec = []

        for pkg, info in package_data.items():
            f.write(f"Package: {pkg}\n")
            if info["spec_file"]:
                f.write("  - Spec file: Found\n")
                built_packages.append(pkg)
            else:
                f.write("  - Spec file: Missing\n")
                missing_spec.append(pkg)

            if info["tarballs"]:
                f.write(f"  - Tarballs: {', '.join(info['tarballs'])}\n")
            else:
                f.write("  - Tarballs: None\n")
            if info["srpms"]:
                f.write(f"  - SRPMs: {', '.join(info['srpms'])}\n")
            else:
                f.write("  - SRPMs: None\n")
            if info["rpms"]:
                f.write(f"  - RPMs: {', '.join(info['rpms'])}\n")
            else:
                f.write("  - RPMs: None\n")
            f.write("-" * 10 + "\n")

        f.write("\nBuilt Packages:\n")
        f.write(", ".join(built_packages) + "\n")

        f.write("\nPackages with Missing Spec Files:\n")
        f.write(", ".join(missing_spec) + "\n")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "tarballs"

    package_status = analyze_build_directory(directory)
    write_package_status(package_status, f"{directory}.txt")
