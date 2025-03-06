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

def print_package_status(package_data):
    """
    Prints the package build status in a readable format.

    Args:
        package_data (dict): The dictionary returned by analyze_build_directory.
    """

    print("Package Build Status:")
    print("-" * 30)

    built_packages = []
    missing_spec = []

    for pkg, info in package_data.items():
        print(f"Package: {pkg}")
        if info["spec_file"]:
            print("  - Spec file: Found")
            built_packages.append(pkg)
        else:
            print("  - Spec file: Missing")
            missing_spec.append(pkg)

        if info["tarballs"]:
            print(f"  - Tarballs: {', '.join(info['tarballs'])}")
        else:
            print("  - Tarballs: None")
        print("-" * 10)

    print("\nBuilt Packages:")
    print(", ".join(built_packages))

    print("\nPackages with Missing Spec Files:")
    print(", ".join(missing_spec))

# Example usage:
if __name__ == "__main__":
    package_status = analyze_build_directory()
    print_package_status(package_status)
