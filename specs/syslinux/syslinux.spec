Name: syslinux
Version: <version> # Replace with actual version
Release: 1%{?dist} # For RPM-based systems
Summary: Bootloader for Linux/DOS
License: GPLv2+
URL: http://www.syslinux.org/
Source0: syslinux-<version>.tar.bz2 # Replace with source tarball
BuildRequires: make, gcc # Adjust as needed
#If you are cross compiling, you will need to add those cross compiling tools here.

%description
Syslinux is a suite of bootloaders for booting Linux/DOS from floppies, hard disks, and CD-ROMs.

%prep
%setup -q -n syslinux-<version>

%build
make # Add any specific flags if needed.

%install
make install PREFIX=%{buildroot}/usr # Adjust PREFIX as needed

# Copy necessary files to boot directory, if needed
mkdir -p %{buildroot}/boot/extlinux
cp %{buildroot}/usr/lib/syslinux/extlinux.bin %{buildroot}/boot/extlinux/
cp %{buildroot}/usr/lib/syslinux/ldlinux.sys %{buildroot}/boot/extlinux/
cp %{buildroot}/usr/lib/syslinux/libutil.c32 %{buildroot}/boot/extlinux/
cp %{buildroot}/usr/lib/syslinux/menu.c32 %{buildroot}/boot/extlinux/
cp %{buildroot}/usr/lib/syslinux/libcom32.c32 %{buildroot}/boot/extlinux/
cp %{buildroot}/usr/lib/syslinux/libpci.c32 %{buildroot}/boot/extlinux/
cp %{buildroot}/usr/lib/syslinux/libmenu.c32 %{buildroot}/boot/extlinux/

%files
/usr/lib/syslinux/* # Adjust as needed
/boot/extlinux/*

%changelog
* <date> <your name> <email> - <version>-1
- Initial build.
