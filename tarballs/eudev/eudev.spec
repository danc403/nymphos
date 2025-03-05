Name: eudev
Version: 3.2.14
Release: 1%{?dist}
Summary: A systemd-free implementation of udev
License: GPL-2.0+
URL: https://www.freedesktop.org/software/eudev/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - libkmod-devel
  - acl-devel
  - attr-devel
  - libblkid-devel
  - libcap-ng-devel
Requires:
  - libkmod
  - acl
  - attr
  - libblkid
  - libcap-ng

%description
eudev is a fork of udev, designed to be independent of systemd. It
provides dynamic device management for Linux systems.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README.md
/usr/sbin/udevadm
/usr/lib/libudev.so.*
/usr/lib/udev/
/etc/udev/
/usr/share/man/man8/udevadm.8*
/usr/share/man/man7/udev.7*
/usr/share/man/man5/udev.rules.5*
/usr/share/man/man5/udev.conf.5*
/usr/share/doc/eudev/

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Sat Mar 1 2025 Dan Carpenter <DanC403@gmail.com> - 3.2.14-1
- Initial RPM build of eudev.
