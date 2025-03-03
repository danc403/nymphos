name: dbus-devel
version: 1.16.0
release: 1%{?dist}
summary: Development files for dbus [License: AFL-2.1 or GPL-2.0-or-later]
license: AFL-2.1 or GPL-2.0-or-later
url: https://www.freedesktop.org/wiki/Software/dbus
source0: dbus-%{version}.tar.xz
buildrequires:
  - autoconf
  - automake
  - libtool
  - pkg-config
  - glib2-devel
  - libcap-devel
  - systemd-devel
requires:
  - dbus = %{version}-%{release}
description: This package contains the header files, static libraries, and pkg-config files needed to develop applications that use dbus.
prep:
  - %autosetup
build:
  - ./configure --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --libexecdir=%{_libexecdir} --with-system-socket=%{_localstatedir}/run/dbus/system_bus_socket
  - %make_build
install:
  - %make_install
files:
  - %{_includedir}/*
  - %{_libdir}/libdbus-*.so
  - %{_libdir}/pkgconfig/dbus-*.pc
changelog:
  - * %{_isodate} Dan Carpenter <DanC403@gmail.com> - 1.16.0-1
  - - Initial package build.
