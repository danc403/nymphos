Name: xz-devel
Version: 5.4.1
Release: 1%{?dist}
Summary: Development files for XZ Utils
License: LGPL-2.1-or-later
URL: https://tukaani.org/xz/
Source0: xz-5.4.1.tar.xz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
Requires:
  - xz = %{version}-%{release}

%description
Development files for XZ Utils.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/include/lzma.h
/usr/lib/liblzma.so
/usr/lib/liblzma.a
/usr/lib/pkgconfig/liblzma.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of xz-devel.
