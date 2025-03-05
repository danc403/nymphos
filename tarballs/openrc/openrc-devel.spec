Name: openrc-devel
Version: 0.56
Release: 1%{?dist}
Summary: Development files for OpenRC
License: GPL-2.0+
URL: https://github.com/OpenRC/openrc
Source0: openrc-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - util-linux
  - bash
  - coreutils
  - grep
  - sed
  - awk
Requires:
  - openrc = %{version}-%{release}

%description
Development files for OpenRC.

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
/usr/include/openrc/
/usr/lib/libopenrc.so
/usr/lib/pkgconfig/libopenrc.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of OpenRC-devel.
