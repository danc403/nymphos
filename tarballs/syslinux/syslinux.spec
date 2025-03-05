Name: syslinux
Version: 6.03
Release: 1%{?dist}
Summary: Bootloaders for Linux/DOS
License: GPLv2+
URL: https://www.syslinux.org/
Source0: %{name}-%{version}.tar.xz
BuildRequires:
  - make
  - gcc
  - binutils
  - mtools
  - perl
Requires:
  - mtools

%description
Syslinux is a suite of bootloaders for Linux and DOS. It supports
booting from various media, including floppy disks, hard drives,
and CD-ROMs.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install PREFIX=%{buildroot}/usr SBINDIR=%{buildroot}/usr/bin LIBDIR=%{buildroot}/usr/lib DATADIR=%{buildroot}/usr/share

install -Dm 644 isolinux/isolinux.bin %{buildroot}/usr/lib/syslinux/isolinux.bin
install -Dm 644 isolinux/isohdpfx.bin %{buildroot}/usr/lib/syslinux/isohdpfx.bin
install -Dm 644 isolinux/ldlinux.c32 %{buildroot}/usr/lib/syslinux/ldlinux.c32

%files
%license COPYING
%doc README CHANGES
/usr/bin/syslinux
/usr/bin/extlinux
/usr/bin/mbr.bin
/usr/lib/syslinux/
/usr/share/man/man1/syslinux.1*
/usr/share/man/man1/extlinux.1*

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of Syslinux.
