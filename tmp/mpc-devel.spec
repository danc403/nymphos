name: mpc-devel
version: 1.3.1
release: 1%{?dist}
summary: Development files for mpc
license: GPLv2+
url: https://www.musicpd.org/clients/mpc/
requires:
  - libmpdclient-devel
buildrequires:
  - pkgconfig(libmpdclient)
description: Development files for mpc
build:
install:
files:
changelog:
  - * Mon Oct 23 2023 Dan Carpenter DanC403@gmail.com - 1.3.1-1
  - - Initial package build
