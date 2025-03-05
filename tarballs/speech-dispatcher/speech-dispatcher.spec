Name: speech-dispatcher
Version: 0.10.1
Release: 1%{?dist}
Summary: System-wide speech dispatcher
License: GPL-2.0-or-later
URL: https://freebsoft.org/speechd
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - alsa-lib-devel
  - glib2-devel
Requires:
  - alsa-lib
  - glib2

%description
Speech Dispatcher is a system-wide high-level device independent layer for
speech synthesis. It provides a common interface for various speech synthesizers.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README NEWS
/usr/bin/spd-say
/usr/bin/speech-dispatcher
/usr/bin/sd_espeak
/usr/lib/speech-dispatcher/
/etc/speech-dispatcher/
/usr/share/man/man1/spd-say.1*
/usr/share/man/man1/speech-dispatcher.1*

%post
# Enable speech-dispatcher in OpenRC (adjust runlevel as needed)
/sbin/rc-update add speechd default

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of speech-dispatcher.
- Enabled speech-dispatcher in OpenRC default runlevel.
