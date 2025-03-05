Name: alsa-utils
Version: 1.2.10
Release: 1%{?dist}
Summary: ALSA sound utilities
License: GPL-2.0-or-later
URL: https://www.alsa-project.org/
Source0: %{name}-%{version}.tar.bz2
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - alsa-lib-devel
  - ncurses-devel
Requires:
  - alsa-lib
  - ncurses

%description
ALSA sound utilities.

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
/usr/bin/alsactl
/usr/bin/amixer
/usr/bin/aplay
/usr/bin/arecord
/usr/bin/aseqdump
/usr/bin/iecset
/usr/bin/speaker-test
/usr/share/man/man1/alsactl.1*
/usr/share/man/man1/amixer.1*
/usr/share/man/man1/aplay.1*
/usr/share/man/man1/arecord.1*
/usr/share/man/man1/aseqdump.1*
/usr/share/man/man1/iecset.1*
/usr/share/man/man1/speaker-test.1*

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of alsa-utils.
