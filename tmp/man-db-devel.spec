name: man-db-devel
version: 2.11.2
release: 1%{?dist}
summary: Development files for man-db
license: GPLv2+
url: https://man-db.nongnu.org/
source0: man-db-2.11.2.tar.xz
requires:
  - man-db = %{version}-%{release}
buildrequires:
  - pkgconfig(libpipeline)
  - pkgconfig(gdbm)
description: This package contains header files and libraries for developing applications that use man-db.
prep:
  - %setup -q
build:
  - %configure --disable-debug
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %{_includedir}/man-db.h
  - %{_libdir}/libman-db.so
changelog:
  -
    date: * Mon Oct 30 2023
    name: Dan Carpenter
    email: DanC403@gmail.com
    changes: - Initial RPM build
