Name: eudev-devel
Version: 3.2.14
Release: 1%{?dist}
Summary: Development files for eudev
License: GPL-2.0+
URL: https://www.freedesktop.org/software/eudev/
Source0: eudev-3.2.14.tar.gz
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
  - eudev = %{version}-%{release}

%description
Development files for eudev.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-selinux --disable-introspection --disable-gudev --disable-manpages
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/include/libudev.h
/usr/lib/libudev.so
/usr/lib/pkgconfig/libudev.pc

%changelog
* Sat Mar 1 2025 Dan Carpenter <DanC403@gmail.com> - 3.2.14-1
- Initial RPM build of eudev-devel.
