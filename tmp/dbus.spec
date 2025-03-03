name: dbus
version: 1.16.0
release: 1%{?dist}
summary: Message bus system, providing a simple way for applications to talk to one another [License: AFL-2.1 or GPL-2.0-or-later]
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
  - glib2
  - libcap
  - systemd
description: D-Bus is a message bus system, providing a simple way for applications to talk to one another.
prep:
  - %autosetup
build:
  - ./configure --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --libexecdir=%{_libexecdir} --with-system-socket=%{_localstatedir}/run/dbus/system_bus_socket
  - %make_build
install:
  - %make_install
files:
  - %license COPYING
  - %{_bindir}/dbus-*
  - %{_sbindir}/dbus-*
  - %{_libexecdir}/dbus-*
  - %{_sysconfdir}/dbus-*
  - %{_localstatedir}/run/dbus
  - %{_datadir}/dbus-*
  - %{_mandir}/man1/dbus-*.1*
  - %{_mandir}/man5/dbus-*.5*
  - %{_mandir}/man8/dbus-*.8*
pre:
  - getent group dbus >/dev/null || groupadd -r dbus
post:
  - /sbin/ldconfig
postun:
  - /sbin/ldconfig
changelog:
  - * %{_isodate} Dan Carpenter <DanC403@gmail.com> - 1.16.0-1
  - - Initial package build.
