Name: alsa-lib
Version: 1.2.13
Release: 1%{?dist}
Summary: Advanced Linux Sound Architecture library
License: LGPL-2.1-or-later
URL: https://www.alsa-project.org/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
Requires:
  - zlib

%description
ALSA library.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README
/usr/lib/libasound.so.*
/usr/share/alsa/
/usr/share/man/man3/alsa*.3*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of alsa-lib.
