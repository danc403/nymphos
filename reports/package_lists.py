#!/usr/bin/env python3
"""
package_lists.py

This script analyzes specified directories for build-related files,
such as spec files, tarballs, SRPMs, and RPMs. It writes the results
to a text file and XML file (for rpms/ and srpms/) named after the analyzed directory.

Usage:
    python package_lists.py <directory>

Arguments:
    <directory>: The directory to analyze.

You can add the following to your .git/hooks/post-commit to run automatically on changes:
#!/bin/bash

# Check for changes in the tarballs directory
if git diff --name-only HEAD~1 HEAD | grep '^tarballs/' > /dev/null; then
    python reports/package_lists.py tarballs
    git add reports/tarballs.txt
    git commit -m "Update tarballs.txt"
fi

# Check for changes in the srpms directory
if git diff --name-only HEAD~1 HEAD | grep '^srpms/' > /dev/null; then
    python reports/package_lists.py srpms
    git add reports/srpms.txt reports/srpms.xml
    git commit -m "Update srpms.txt and srpms.xml"
fi

# Check for changes in the rpms directory
if git diff --name-only HEAD~1 HEAD | grep '^rpms/' > /dev/null; then
    python reports/package_lists.py rpms
    git add reports/rpms.txt reports/rpms.xml
    git commit -m "Update rpms.txt and rpms.xml"
fi

# Check for changes in the src directory
if git diff --name-only HEAD~1 HEAD | grep '^src/' > /dev/null; then
    python reports/package_lists.py src
    git add reports/src.txt
    git commit -m "Update src.txt"
fi

# Check for changes in the docs directory
if git diff --name-only HEAD~1 HEAD | grep '^docs/' > /dev/null; then
    python reports/package_lists.py docs
    git add reports/docs.txt
    git commit -m "Update docs.txt"
fi
"""

import os
import sys
import datetime
import xml.etree.ElementTree as ET

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
    #change to go up one directory then down to directory
    full_directory = os.path.join(".", directory)
    directories = [d for d in os.listdir(full_directory) if os.path.isdir(os.path.join(full_directory, d))]

    for pkg_dir in directories:
        pkg_path = os.path.join(full_directory, pkg_dir)
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

def write_package_status(package_data, directory, filename):
    """
    Writes the package build status to a file.

    Args:
        package_data (dict): The dictionary returned by analyze_build_directory.
        directory (str): the directory the files are from.
        filename (str): The name of the file to write to.
    """
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open(os.path.join("reports", filename), "w") as f:
        f.write(f"Generated: {datetime.datetime.now()}\n")
        f.write("Package Build Status:\n")
        f.write("-" * 30 + "\n")

        built_packages = []
        missing_spec = []

        sorted_packages = sorted(package_data.items()) # Sort the packages

        for pkg, info in sorted_packages:
            f.write(f"Package: {pkg}\n")
            if info["spec_file"]:
                f.write("    - Spec file: Found\n")
                built_packages.append(pkg)
            else:
                f.write("    - Spec file: Missing\n")
                missing_spec.append(pkg)

            if info["tarballs"]:
                f.write(f"    - Tarballs: {', '.join(info['tarballs'])}\n")
            else:
                f.write("    - Tarballs: None\n")
            if info["srpms"]:
                f.write(f"    - SRPMs: {', '.join(info['srpms'])}\n")
            else:
                f.write("    - SRPMs: None\n")
            if info["rpms"]:
                f.write(f"    - RPMs: {', '.join(info['rpms'])}\n")
            else:
                f.write("    - RPMs: None\n")
            f.write("-" * 10 + "\n")

        # Summary Statistics
        f.write("\nSummary:\n")
        f.write(f"Total Packages: {len(package_data)}\n")
        f.write(f"Packages with Missing Spec Files: {len(missing_spec)}\n")

def write_xml_package_status(package_data, directory, filename):
    """
    Writes the package build status to an XML file.

    Args:
        package_data (dict): The dictionary returned by analyze_build_directory.
        directory (str): the directory the files are from.
        filename (str): The name of the file to write to.
    """
    if not os.path.exists("reports"):
        os.makedirs("reports")

    root = ET.Element("packages")
    sorted_packages = sorted(package_data.items())
    for pkg, info in sorted_packages:
        package_element = ET.SubElement(root, "package")
        name_element = ET.SubElement(package_element, "name")
        name_element.text = pkg
        spec_element = ET.SubElement(package_element, "spec_file")
        spec_element.text = "Found" if info["spec_file"] else "Missing"
        tarballs_element = ET.SubElement(package_element, "tarballs")
        tarballs_element.text = ", ".join(info["tarballs"]) if info["tarballs"] else "None"
        srpms_element = ET.SubElement(package_element, "srpms")
        srpms_element.text = ", ".join(info["srpms"]) if info["srpms"] else "None"
        rpms_element = ET.SubElement(package_element, "rpms")
        rpms_element.text = ", ".join(info["rpms"]) if info["rpms"] else "None"

    tree = ET.ElementTree(root)
    tree.write(os.path.join("reports", filename))

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "tarballs"

    package_status = analyze_build_directory(directory)
    write_package_status(package_status, directory, f"{directory}.txt")

    if directory in ["rpms", "srpms"]:
        write_xml_package_status(package_status, directory, f"{directory}.xml")
