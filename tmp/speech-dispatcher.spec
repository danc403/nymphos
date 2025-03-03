name: speech-dispatcher
version: 0.10.1
release: 1%{?dist}
summary: Speech Dispatcher - A device independent layer for speech synthesis (Text-To-Speech) - LGPL
license: LGPLv2+
url: https://github.com/brailletec/speechd
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkg-config
  - gettext
  - libcap-ng-devel
  - espeak-ng-devel
  - alsa-lib-devel
  - dbus-devel
  - dbus-glib-devel
  - python3-devel
  - libspeechd-devel
Requires:
  - alsa-utils
  - dbus
  - dbus-glib
  - espeak-ng
  - libcap-ng
  - python3
  - libspeechd
Requires(post): dbus-daemon
Requires(preun): dbus-daemon
Requires(postun): dbus-daemon
BuildArch: x86_64
Description: Speech Dispatcher is a high-level device independent layer for speech synthesis. It provides a common easy to use interface to speech synthesizers.
Conflicts: orca < 3.32
%prep: rm -rf %{SOURCE0/.tar.gz/}
tar -xzf %{SOURCE0}
pushd %{SOURCE0/.tar.gz/}
autoreconf -fi
popd
%build: pushd %{SOURCE0/.tar.gz/}
%configure
make %{?_smp_mflags}
popd
%install: pushd %{SOURCE0/.tar.gz/}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/usr/lib64/speech-dispatcher-modules/sd_*_flite.so
find %{buildroot} -type f -name '*.la' -delete
popd
%post: systemctl --no-reload --global enable speech-dispatcher.service > /dev/null 2>&1 || :
systemctl --no-reload --global enable speech-dispatcher.socket > /dev/null 2>&1 || :
dbus-update-activation-environment --systemd > /dev/null 2>&1 || :
%preun: systemctl --no-reload --global disable speech-dispatcher.service > /dev/null 2>&1 || :
systemctl --no-reload --global disable speech-dispatcher.socket > /dev/null 2>&1 || :
%postun: dbus-update-activation-environment --systemd > /dev/null 2>&1 || :
%files:
  - %{_bindir}/spd-confedit
  - %{_bindir}/spd-say
  - %{_sysconfdir}/speech-dispatcher/
  - %{_libdir}/speech-dispatcher-modules/
  - %{_libexecdir}/speech-dispatcher/
  - %{_mandir}/man1/spd-say.1*
  - %{_datadir}/applications/speech-dispatcher.desktop
  - %{_datadir}/dbus-1/system-services/org.a11y.SpeechD.service
  - %{_datadir}/icons/hicolor/*/apps/speech-dispatcher*
  - %{_unitdir}/speech-dispatcher.service
  - %{_unitdir}/speech-dispatcher.socket
  - %{_datadir}/speech-dispatcher/
  - %license LICENSE
%changelog: * %{date} Dan Carpenter DanC403@gmail.com - 0.10.1-1
- Initial package build
