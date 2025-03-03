name: speech-dispatcher-devel
version: 0.10.1
release: 1%{?dist}
summary: Development files for Speech Dispatcher
License: LGPLv2+
URL: https://github.com/brailletec/speechd
Source0: speech-dispatcher-%{version}.tar.gz
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
Requires: speech-dispatcher = %{version}-%{release}
BuildArch: x86_64
Description: This package contains the development files for Speech Dispatcher.
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
popd
%files:
  - %{_includedir}/*
  - %{_libdir}/pkgconfig/speech-dispatcher.pc
  - %{_libdir}/libspeechd.so
  - %{_libdir}/libspeechd.a
  - %{_mandir}/man3/libspeechd.3*
%changelog: * %{date} Dan Carpenter DanC403@gmail.com - 0.10.1-1
- Initial package build
