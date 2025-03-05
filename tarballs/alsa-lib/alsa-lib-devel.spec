Name: alsa-lib-devel
Version: 1.2.13
Release: 1%{?dist}
Summary: Development files for Advanced Linux Sound Architecture library
License: LGPL-2.1-or-later
URL: https://www.alsa-project.org/
Source0: alsa-lib-1.2.13.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
Requires:
  - alsa-lib = %{version}-%{release}

%description
Development files for ALSA library.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/include/alsa/
/usr/lib/libasound.so
/usr/lib/pkgconfig/alsa.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of alsa-lib-devel.
