import os

def analyze_build_directory(directory="."):
    """
    Analyzes a directory to identify built packages (spec files)
    and available tarballs.

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

        package_info[pkg_dir] = {
            "spec_file": os.path.exists(spec_file),
            "tarballs": tarballs,
        }

    return package_info

def write_package_status(package_data, filename="packages.txt"):
    """
    Writes the package build status to a file.

    Args:
        package_data (dict): The dictionary returned by analyze_build_directory.
        filename (str): The name of the file to write to. Defaults to "packages.txt".
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
            f.write("-" * 10 + "\n")

        f.write("\nBuilt Packages:\n")
        f.write(", ".join(built_packages) + "\n")

        f.write("\nPackages with Missing Spec Files:\n")
        f.write(", ".join(missing_spec) + "\n")

# Example usage:
if __name__ == "__main__":
    package_status = analyze_build_directory()
    write_package_status(package_status)
