name: geany-devel
version: 2.0
release: 1%{?dist}
summary: Development files for Geany
license: GPL-2.0-or-later
url: https://www.geany.org/
source0: %{name}-%{version}.tar.gz
buildrequires:
  - gtk3-devel
  - glib2-devel
  - vte3-devel
  - pcre-devel
  - gcc
  - make
  - pkg-config
  - gettext
requires:
  - geany = %{version}-%{release}
description: This package contains the header files and libraries needed to develop applications that use Geany.
prep:
  - %setup -q
build:
  - %configure
  - %make_build
install:
  - %make_install
files:
  - %{_includedir}/geany/*.h
  - %{_libdir}/pkgconfig/geany.pc
changelog:
  - * %{DATE} Dan Carpenter <DanC403@gmail.com> - 2.0-1
  - - Initial RPM build.
