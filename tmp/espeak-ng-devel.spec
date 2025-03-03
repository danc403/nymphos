name: espeak-ng-devel
version: 1.52.0
release: 1%{?dist}
summary: Development files for eSpeak NG
License: GPLv3+
URL: http://espeak.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
Requires:
  - espeak-ng = %{version}-%{release}
BuildRequires:
  - autoconf
  - automake
  - libtool
  - gcc
  - make
  - pkg-config
  - alsa-lib-devel
BuildArch: x86_64
Description: This package contains the header files and libraries needed to develop
prep:
  - %autosetup
build:
  - %configure
install:
  - make install DESTDIR=%{buildroot}
files:
  - %{_includedir}/espeak-ng/*
  - %{_libdir}/libespeak-ng.a
  - %{_libdir}/pkgconfig/espeak-ng.pc
changelog:
  - * %{date} Dan Carpenter DanC403@gmail.com - 1.52.0-1
  - - Initial package build
