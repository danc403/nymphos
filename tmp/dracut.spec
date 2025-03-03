name: dracut
version: 059
release: 1%{?dist}
summary: Low-level initramfs generator
license: GPLv2+
url: https://github.com/dracutdevs/dracut
source0: %{name}-%{version}.tar.gz
buildrequires:
  - make
  - automake
  - autoconf
  - gettext
  - pkg-config
  - util-linux
  - bash
  - coreutils
requires:
  - bash
  - coreutils
  - kmod
  - util-linux
  - systemd-udev
  - udev
  - findutils
  - gzip
  - xz
  - rpm
  - grep
description: Dracut is an event-driven initramfs infrastructure.  It provides much more functionality than previous implementations and allows for a more flexible and extensible initramfs.  Dracut's primary focus is on providing early boot functionality.
prep:
  - %autosetup
build:
  - ./autogen.sh
  - %configure
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %license COPYING
  - %doc README
  - /usr/bin/dracut
  - /usr/lib/dracut
  - /etc/dracut.conf*
  - /usr/share/man/man8/dracut.8*
  - /usr/share/dracut/*
changelog:
  - * Wed Oct 25 2023 Dan Carpenter <DanC403@gmail.com> - 059-1
  - - Initial RPM build
