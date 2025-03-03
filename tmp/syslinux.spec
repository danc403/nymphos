content: Name:           syslinux
Version:        6.03
Release:        1%{?dist}
Summary:        Collection of bootloaders (Syslinux, Isolinux, PXELINUX, Memdisk) - GPLv2

License:        GPLv2
URL:            https://www.syslinux.org/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  binutils
BuildRequires:  m4
BuildRequires:  perl

Requires:       util-linux
Requires:       perl

%description
Syslinux is a suite of lightweight bootloaders for booting from various media,
including floppy disks, hard disks, and CD-ROMs. It includes SYSLINUX, ISOLINUX,
PXELINUX, and MEMDISK.

%prep
%setup -q

%build
make all

%install
make install DESTDIR=%{buildroot}

# Remove unwanted files
rm -rf %{buildroot}/usr/share/doc
find %{buildroot} -name "*.txt" -delete

%files
%license COPYING
%{_bindir}/syslinux
%{_bindir}/ldlinux.sys
%{_bindir}/isolinux
%{_bindir}/pxelinux.0
%{_bindir}/memdisk
%{_bindir}/mbr.bin
%{_bindir}/chain.c32
%{_bindir}/menu.c32
%{_bindir}/vesamenu.c32
%{_bindir}/reboot.c32
%{_bindir}/poweroff.c32
%{_bindir}/hdt.c32
%{_bindir}/libutil.c32
%{_bindir}/libcom32.c32
%{_bindir}/modules/bios/ldlinux.c32
%{_mandir}/man1/syslinux.1*
%{_mandir}/man1/ldlinux.1*
%{_mandir}/man1/isolinux.1*
%{_mandir}/man1/pxelinux.1*
%{_mandir}/man1/memdisk.1*

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - %{version}-1
- Initial package build

filename: syslinux.spec
