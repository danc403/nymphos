Name: alsa-utils-devel
Version: 1.2.10
Release: 1%{?dist}
Summary: Development files for ALSA sound utilities
License: GPL-2.0-or-later
URL: https://www.alsa-project.org/
Source0: alsa-utils-1.2.10.tar.bz2
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - alsa-lib-devel
  - ncurses-devel
Requires:
  - alsa-utils = %{version}-%{release}

%description
Development files for ALSA sound utilities.

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
/usr/lib/pkgconfig/alsa-utils.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of alsa-utils-devel.
