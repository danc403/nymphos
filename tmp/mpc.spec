name: mpc
version: 1.3.1
release: 1%{?dist}
summary: Command-line client for Music Player Daemon (MPD)
license: GPLv2+
url: https://www.musicpd.org/clients/mpc/
source0: %{name}-%{version}.tar.gz
buildrequires:
  - pkgconfig(libmpdclient)
requires:
  - libmpdclient
description: mpc is a command-line client for MPD, the Music Player Daemon. It allows one to control MPD and query its database from a console.
build:
  - %configure
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %{_bindir}/mpc
  - %{_mandir}/man1/mpc.1*
  - %license COPYING
changelog:
  - * Mon Oct 23 2023 Dan Carpenter DanC403@gmail.com - 1.3.1-1
  - - Initial package build
