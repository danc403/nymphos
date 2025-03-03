name: iproute2-devel
version: 6.1.0
release: 1%{?dist}
summary: Development files for iproute2
license: GPLv2+
requires: iproute2 = %{version}-%{release}
buildrequires:
  - libcap-devel
  - libmnl-devel
  - pkgconfig(libelf)
  - pkgconfig(libxtables)
  - pkgconfig(json-c)
description: This package contains the development files for iproute2.
files:
  - %{_includedir}/*
  - %{_libdir}/pkgconfig/*
changelog:
  - * %{date} Dan Carpenter DanC403@gmail.com - 6.1.0-1
  - - Initial build
