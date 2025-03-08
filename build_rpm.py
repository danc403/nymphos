#!/usr/bin/env python3
"""
#Build the Image:
docker build -t rpm-builder .
#Run the Container:
docker run -v $(pwd)/rpms:/build/RPMS -v $(pwd)/srpms:/build/SRPMS -v $(pwd)/specs:/build/SPECS rpm-builder
#This command mounts the current rpms, srpms, and specs directories to the container, so the built packages are available on your host system.

###
# Copyright (c) 2025 Dan Carpenter <danc403@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Build the Image:
"""

import os
import subprocess
import shutil
import re
import sys

SPEC_DIR = "/build/TARBALLS"
SOURCE_DIR = "/build/SOURCES"
RPM_DIR = "/build/RPMS"
SRPM_DIR = "/build/SRPMS"

def is_running_in_container():
    return os.environ.get('container') == 'docker'

def dockerfile_exists():
    return os.path.exists("Dockerfile")

def generate_dockerfile():
    """Generates a Dockerfile."""
    dockerfile_content = """
FROM fedora:latest

# Copyright (c) 2025 Dan Carpenter <danc403@gmail.com>
# Free for any purpose.
# Install base build tools and dependencies
RUN dnf install -y \
    rpm-build rpmdevtools gcc make cmake ninja-build \
    autoconf automake libtool pkgconfig \
    zlib-devel bzip2-devel xz-devel openssl-devel \
    ncurses-devel readline-devel libffi-devel \
    gmp-devel mpfr-devel mpc-devel \
    libcap-devel libseccomp-devel \
    glib2-devel gtk4-devel pcre2-devel \
    alsa-lib-devel pulseaudio-libs-devel \
    libvpx-devel libx264-devel libx265-devel \
    opus-devel vorbis-devel theora-devel \
    lame-devel faac-devel aom-devel \
    fontconfig-devel freetype-devel \
    gstreamer1-devel gstreamer1-plugins-base-devel \
    gstreamer1-plugins-good-devel \
    gtk3-devel libappstream-glib-devel \
    libxml2-devel libxslt-devel \
    git wget tar unzip

# Create build directories
RUN mkdir -p /build/SPECS /build/SOURCES /build/RPMS /build/SRPMS

# Set working directory
WORKDIR /build/SPECS

# Copy a script that will do the heavy lifting /P.
COPY build_rpm.py /build/

# Run the build script
CMD ["python", "/build/build_rpm.py"]
"""
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)

def parse_spec_file(spec_path):
    """Parses the spec file and extracts package name, version, and source tarball."""
    package_name = None
    version = None
    source_tarball = None

    with open(spec_path, 'r') as f:
        for line in f:
            package_match = re.search(r'^Name:\s*(\S+)', line)
            version_match = re.search(r'^Version:\s*(\S+)', line)
            source_match = re.search(r'^Source\d*:\s*(\S+)', line)

            if package_match:
                package_name = package_match.group(1)
            if version_match:
                version = version_match.group(1)
            if source_match:
                source_tarball = source_match.group(1)

    return package_name, version, source_tarball

def build_rpm(spec_file, package_dir):
    spec_path = os.path.join(package_dir, spec_file)
    package_name, version, source_tarball = parse_spec_file(spec_path)

    if not package_name or not version or not source_tarball:
        print(f"Error: Could not extract information from {spec_file}")
        return

    # Find the tarball in the same directory
    tarball_path = os.path.join(package_dir, source_tarball)

    if not os.path.exists(tarball_path):
        print(f"Error: Tarball {source_tarball} not found in {package_dir}")
        return

    # Copy the tarball to SOURCES
    shutil.copy(tarball_path, os.path.join(SOURCE_DIR, source_tarball))

    try:
        # Build SRPM
        subprocess.run(["rpmbuild", "-bs", spec_path], check=True)

        # Move SRPM
        srpms = [f for f in os.listdir("/build") if f.endswith(".src.rpm")]
        for srpm in srpms:
            shutil.move(os.path.join("/build", srpm), os.path.join(SRPM_DIR, srpm))

        # Build RPM
        subprocess.run(["rpmbuild", "-ba", spec_path], check=True)

        # Move RPMs
        rpms = [f for f in os.listdir("/build/RPMS/x86_64/") if f.endswith(".rpm")]
        for rpm in rpms:
            shutil.move(os.path.join("/build/RPMS/x86_64/", rpm), os.path.join(RPM_DIR, rpm))

    except subprocess.CalledProcessError as e:
        print(f"Build failed for {spec_file}: {e}")

    # Clean up source directory
    shutil.rmtree(SOURCE_DIR, ignore_errors=True)
    os.makedirs(SOURCE_DIR, exist_ok=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build RPM packages.")
    parser.add_argument(
        "-p",
        "--package",
        default="test",
        help="Package(s) to build. Use '.' or '*' for all packages.",
    )
    parser.add_argument("-d", "--docker", action="store_true", help="Generate and run Dockerfile")
    args = parser.parse_args()

    if is_running_in_container():
        # Inside container: Build RPMs
        packages_to_build = (
           
            if args.package in [".", "*"]
            else [pkg.strip() for pkg in args.package.split(",")]
        )
        for package_dir in os.listdir(SPEC_DIR):
            full_package_dir = os.path.join(SPEC_DIR, package_dir)
            if os.path.isdir(full_package_dir):
                for spec_file in os.listdir(full_package_dir):
                    if spec_file.endswith(".spec"):
                        package_name = os.path.splitext(spec_file)[0]
                        if (
                            not packages_to_build
                            or package_name in packages_to_build
                            or package_dir in packages_to_build
                        ):
                            build_rpm(spec_file, full_package_dir)

    elif dockerfile_exists():
        # Dockerfile exists, not in container: Build and run the container
        subprocess.run(["docker", "build", "-t", "rpm-builder", "."], check=True)
        docker_run_command = [
            "docker",
            "run",
            "-v",
            f"{os.getcwd()}/rpms:/build/RPMS",
            "-v",
            f"{os.getcwd()}/srpms:/build/SRPMS",
            "-v",
            f"{os.getcwd()}/tarballs:/build/TARBALLS",
            "rpm-builder",
            "-p",
            args.package,
        ]
        subprocess.run(docker_run_command, check=True)

    elif args.docker:
        # -d flag, no Dockerfile, not in container: Generate and run
        generate_dockerfile()
        subprocess.run(["docker", "build", "-t", "rpm-builder", "."], check=True)
        docker_run_command = [
            "docker",
            "run",
            "-v",
            f"{os.getcwd()}/rpms:/build/RPMS",
            "-v",
            f"{os.getcwd()}/srpms:/build/SRPMS",
            "-v",
            f"{os.getcwd()}/tarballs:/build/TARBALLS",
            "rpm-builder",
            "-p",
            args.package,
        ]
        subprocess.run(docker_run_command, check=True)

    else:
        # No Dockerfile, no -d flag, not in container: Build directly on host
        packages_to_build = (
           
            if args.package in [".", "*"]
            else [pkg.strip() for pkg in args.package.split(",")]
        )
        # ... (Your direct host RPM build logic here) ...
        print("Direct host build logic not implemented yet.")
