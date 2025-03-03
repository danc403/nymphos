name: libspiel-devel
version: SPIEL_1_0_3
release: 1%{?dist}
summary: Development files for libspiel
license: LGPL-2.1+
url: https://example.com/libspiel
source0: %{name:libspiel}-%{version}.tar.gz
requires:
  - libspiel = %{version}
buildrequires:
  - autoconf
  - automake
  - libtool
description: This package contains the header files and static libraries needed to develop programs that use libspiel.
prep:
  - %autosetup -n libspiel-%{version}
build:
  - ./autogen.sh
  - %configure
  - %make_build
install:
  - %make_install
files:
  - /usr/include/*
  - /usr/lib64/libspiel.so
  - /usr/lib64/pkgconfig/*
changelog:
  -
    date: Thu Oct 26 2023
    name: Dan Carpenter
    email: DanC403@gmail.com
    changes: - Initial build
