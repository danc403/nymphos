Name:           syslinux
Version:        6.03
Release:        1%{?dist}
Summary:        SYSLINUX is a collection of boot loaders for Linux

License:        GPL
URL:            https://www.kernel.org/pub/linux/utils/boot/syslinux/
Source0:        ../../tarballs/syslinux/syslinux-%{version}.tar.xz

BuildRequires:  gcc, make, nasm, perl, mtools, dosfstools, extlinux, e2fsprogs

ExclusiveArch:  x86_64
BuildArch:      x86_64

%description
SYSLINUX is a collection of boot loaders for Linux. It includes ISOLINUX, which is used for booting from CD-ROMs, and PXELINUX, which is used for network booting.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/usr/bin/extlinux
/usr/lib/syslinux/
/usr/share/man/man1/extlinux.1.gz
/usr/share/man/man1/isohybrid.1.gz
/usr/share/man/man1/isohybrid-debug.1.gz
/usr/share/man/man1/isolinux.1.gz
/usr/share/man/man1/mkdiskimage.1.gz
/usr/share/man/man1/mkisofs.1.gz
/usr/share/man/man1/pxelinux.1.gz
/usr/share/man/man1/syslinux.1.gz
/usr/share/man/man1/syslinux-debug.1.gz
/usr/share/man/man1/syslinux-install_update.1.gz
/usr/share/man/man1/syslinux-menu.c32.1.gz
/usr/share/man/man1/syslinux-menu.c32.debug.1.gz
/usr/share/man/man1/syslinux-menu.c32.debug.static.1.gz
/usr/share/man/man1/syslinux-menu.c32.static.1.gz
/usr/share/man/man1/syslinux-menu.c32.static.debug.1.gz
/usr/share/man/man1/syslinux-menu.c32.static.debug.static.1.gz
/usr/share/man/man1/syslinux-menu.c32.static.static.1.gz
/usr/share/man/man1/syslinux-menu.c32.static.static.debug.1.gz
/usr/share/man/man1/syslinux-menu.c32.static.static.debug.static.1.gz
/usr/share/man/man1/syslinux-menu.c32.static.static.static.1.gz
/usr/share/man/man1/syslinux-menu.c32.static.static.static.debug.1.gz

%changelog
* Sun Oct 01 2023 Your Name <your.email@example.com> - 6.03-1
- Initial build of syslinux 6.03 for x86_64
