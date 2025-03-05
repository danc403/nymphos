Name: libkmod-devel
Version: 34
Release: 1%{?dist}
Summary: Development files for libkmod
License: LGPLv2+
URL: https://www.kernel.org/pub/linux/utils/kernel/kmod/
Source0: kmod-34.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
Requires:
  - libkmod = %{version}-%{release}

%description
Development files for libkmod.

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
/usr/include/libkmod.h
/usr/lib/libkmod.so
/usr/lib/pkgconfig/libkmod.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of libkmod-devel.
