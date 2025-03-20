import tarfile
import os
import argparse

def create_tarxz_archive(version, files, output_dir="."):
    """
    Creates a tar.xz archive containing the specified files within a versioned directory.

    Args:
        version (str): The version number (e.g., "1.0").  Used for the directory name.
        files (list): A list of file paths to include in the archive.
        output_dir (str, optional): The directory where the archive will be created. Defaults to the current directory.

    Returns:
        str: The path to the created tar.xz archive.  Returns None on error.
    """

    archive_name = f"nymph-disk-mounter-{version}.tar.xz"
    archive_path = os.path.join(output_dir, archive_name)
    version_dir = version # or "nymph-boot-config-" + version

    try:
        # Create the archive in xz compressed format
        with tarfile.open(archive_path, "w:xz") as tar:

            # Create the version directory within the archive.  We do this by 
            # adding an empty file at the path of the directory name
            #tarinfo = tarfile.TarInfo(version_dir)
            #tarinfo.type = tarfile.DIRTYPE
            #tarinfo.mode = 0o755  # Common directory permissions (rwxr-xr-x)
            #tar.addfile(tarinfo)

            # Add files to the version directory within the archive
            for file_path in files:
                if not os.path.exists(file_path):
                    print(f"Warning: File not found: {file_path}")
                    continue  # Skip if the file doesn't exist

                # Calculate the arcname (path inside the archive).
                # We want the files to be placed inside the versioned directory.
                arcname = os.path.join(version_dir, os.path.basename(file_path))
                tar.add(file_path, arcname=arcname)
        print(f"Successfully created archive: {archive_path}")
        return archive_path

    except Exception as e:
        print(f"Error creating archive: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a tar.xz archive for nymph-boot-config project.")
    parser.add_argument("-v", "--version", help="The version number for the archive (e.g., 1.0).")
    parser.add_argument("-o", "--output_dir", default=".", help="The directory to save the archive to (default: current directory).")
    args = parser.parse_args()

    files_to_archive = [
        "readme.md",
        "meson.build",
        "nymph-disk-mounter.vala",
        "nymph-disk-mounter.desktop",
        "nymph-disk-mounter.spec",
    ]

    create_tarxz_archive(args.version, files_to_archive, args.output_dir)
