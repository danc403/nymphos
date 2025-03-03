name: inetutils-devel
version: 2.3
release: 1%{?dist}
summary: Development files for inetutils
license: GPLv3+
url: https://www.gnu.org/software/inetutils/
source0: %{name}-%{version}.tar.xz
requires:
  - inetutils
buildrequires:
  - inetutils
description: Development files for inetutils
prep:
  - %autosetup
build:
  - ./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %{_includedir}/*
  - %{_libdir}/*.so
  - %{_libdir}/*.a
  - %{_libdir}/pkgconfig/*
changelog:
  -
    date: YYYY-MM-DD
    author: Dan Carpenter <DanC403@gmail.com>
    comment: Initial build
