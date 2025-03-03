name: espeak-ng
version: 1.52.0
release: 1%{?dist}
summary: eSpeak NG is a compact open source software speech synthesizer
license: GPLv3+
url: http://espeak.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - gcc
  - make
  - pkg-config
  - alsa-lib-devel
Requires:
  - alsa-lib
BuildArch: x86_64
Description: eSpeak NG is a compact open source software speech synthesizer.
package: {'configure_options': ['--disable-static']}
prep:
  - %autosetup
build:
  - %configure %{?configure_options: --enable-shared}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %license COPYING
  - %{_bindir}/espeak-ng
  - %{_bindir}/phoneme
  - %{_libdir}/libespeak-ng.so.*
  - %{_datadir}/espeak-ng/*
  - %{_datadir}/espeak-ng-data/*
  - %{_mandir}/man1/espeak-ng.1*
  - %{_mandir}/man1/phoneme.1*
changelog:
  - * %{date} Dan Carpenter DanC403@gmail.com - 1.52.0-1
  - - Initial package build
