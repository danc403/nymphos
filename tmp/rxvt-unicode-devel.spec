name: rxvt-unicode-devel
version: 9.31
release: 1%{?dist}
summary: Development files for rxvt-unicode
license: GPLv3+
url: http://rxvt.perltk.org/
source0: rxvt-unicode-%{version}.tar.bz2
requires:
  - rxvt-unicode = %{version}-%{release}
buildrequires:
  - pkgconfig(x11)
  - pkgconfig(fontconfig)
  - pkgconfig(freetype2)
  - pkgconfig(xft)
  - pkgconfig(xrender)
  - pkgconfig(xext)
description: This package contains the development files for rxvt-unicode.
prep:
  - %setup -q -n rxvt-unicode-%{version}
build:
  - %configure
  - %make_build
install:
  - %make_install
files:
  - %{_includedir}/*
  - %{_libdir}/pkgconfig/*
changelog:
  -
    date: 2023-10-27
    name: Dan Carpenter
    email: DanC403@gmail.com
    changes: - Initial package build
