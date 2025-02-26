#!/bin/bash

# Script to set up a build chroot for NymphOS on Rocky 9

# Root directory for NymphOS
NYMPH_ROOTDIR="/repos/nymphos"

# Tarballs directory
TARBALLS_DIR="$NYMPH_ROOTDIR/tarballs"

# Specs directory
SPECS_DIR="$NYMPH_ROOTDIR/specs"

# Chroot directory
CHROOT_DIR="$NYMPH_ROOTDIR/chroot"

# Create chroot directory
mkdir -p "$CHROOT_DIR"

# Install minimal Rocky 9 system into chroot
dnf --installroot="$CHROOT_DIR" --releasever 9 -y groupinstall "Minimal Install"

# Install build dependencies inside chroot
dnf --installroot="$CHROOT_DIR" --releasever 9 -y install \
    gcc make rpm-build rpm-devel binutils patch \
    tar gzip xz bzip2 which findutils diffutils \
    coreutils sed grep awk \
    glibc-devel kernel-headers ncurses-devel \
    zlib-devel openssl-devel \
    perl python3 python3-devel \
    pkgconfig autoconf automake libtool \
    meson ninja
#Added meson and ninja to the list.

# Copy tarballs and spec files into chroot
cp -r "$TARBALLS_DIR" "$CHROOT_DIR/"
cp -r "$SPECS_DIR" "$CHROOT_DIR/"

echo "Chroot setup complete. You can now chroot into $CHROOT_DIR."
echo "Example: chroot $CHROOT_DIR /bin/bash"
