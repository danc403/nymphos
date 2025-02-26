#!/bin/bash

# Script to build packages inside the NymphOS chroot

# Root directory for NymphOS
NYMPH_ROOTDIR="nymph"

# Chroot directory
CHROOT_DIR="$NYMPH_ROOTDIR/chroot"

# Specs directory inside chroot
CHROOT_SPECS_DIR="$CHROOT_DIR/specs"

# Architecture
ARCH="x86_64"

# Function to build a package
build_package() {
  local spec_file="$1"
  local package_name="$(basename "$spec_file" .spec)"

  echo "Building package: $package_name"

  # Enter chroot and build the package
  chroot "$CHROOT_DIR" /bin/bash -c "
    cd '$CHROOT_SPECS_DIR/$package_name'
    rpmbuild -ba '$package_name.spec'
  "

  # Check if build was successful
  if [ $? -eq 0 ]; then
    echo "Package $package_name built successfully."
  else
    echo "Error building package $package_name."
  fi
}

# Find and build all spec files
find "$CHROOT_SPECS_DIR" -name "*.spec" | while read spec_file; do
  build_package "$spec_file"
done

echo "Package build process completed."
