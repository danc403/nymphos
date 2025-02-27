#!/bin/bash
set -e # Exit on error

mkdir -p srpms/linux srpms/dracut srpms/syslinux srpms/openrc

# Build Linux Kernel SRPM
mkdir tmp-kernel
cp tarballs/linux/linux-*.tar.xz tmp-kernel/
cd tmp-kernel
tar xf linux-*.tar.xz
cd linux-*
cp ../../../specs/linux/.config .config
rpmbuild -bs ../../../specs/linux/*.spec
mv ../../../rpmbuild/SRPMS/*.src.rpm ../../../srpms/linux/
cd ../..
rm -rf tmp-kernel

# Build Dracut SRPM
mkdir tmp-dracut
cp tarballs/dracut/dracut-*.tar.gz tmp-dracut/
cd tmp-dracut
tar xf dracut-*.tar.gz
cd dracut-*
rpmbuild -bs ../../../specs/dracut/*.spec
mv ../../../rpmbuild/SRPMS/*.src.rpm ../../../srpms/dracut/
cd ../..
rm -rf tmp-dracut

# Build Syslinux SRPM
mkdir tmp-syslinux
cp tarballs/syslinux/syslinux-*.tar.xz tmp-syslinux/
cd tmp-syslinux
tar xf syslinux-*.tar.xz
cd syslinux-*
rpmbuild -bs ../../../specs/syslinux/*.spec
mv ../../../rpmbuild/SRPMS/*.src.rpm ../../../srpms/syslinux/
cd ../..
rm -rf tmp-syslinux

# Build OpenRC SRPM
mkdir tmp-openrc
cp tarballs/openrc/openrc-*.tar.gz tmp-openrc/
cd tmp-openrc
tar xf openrc-*.tar.gz
cd openrc-*
rpmbuild -bs ../../../specs/openrc/*.spec
mv ../../../rpmbuild/SRPMS/*.src.rpm ../../../srpms/openrc/
cd ../..
rm -rf tmp-openrc
