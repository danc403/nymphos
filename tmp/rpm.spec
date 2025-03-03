name: rpm
version: 4.20.1
release: 1%{?dist}
summary: The RPM Package Manager
license: GPLv2+
url: https://rpm.org/
source0: rpm-%{version}.tar.bz2
buildrequires:
  - autoconf
  - automake
  - bzip2
  - coreutils
  - dbus-glib-devel
  - gettext
  - gmp-devel
  - libcap-devel
  - libtool
  - lua-devel
  - ncurses-devel
  - openssl-devel
  - perl
  - pkg-config
  - python3-devel
  - readline-devel
  - zlib-devel
requires:
  - bash
  - coreutils
  - dbus
  - findutils
  - gzip
  - libcap
  - ncurses
  - perl
  - readline
  - sed
  - zlib
description: The RPM Package Manager (RPM) is a powerful command line driven package management system capable of installing, uninstalling, verifying, querying, and updating computer software packages. Each software package consists of an archive of files along with package meta-data used to install and erase packages.
prep:
  - %setup -q
build:
  - ./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --mandir=%{_mandir}
  - %{__make} %{?_smp_mflags}
install:
  - %{__make} install DESTDIR=%{buildroot}
files:
  - %license COPYING
  - %doc AUTHORS ChangeLog README
  - %{_bindir}/rpm
  - %{_bindir}/rpm2cpio
  - %{_bindir}/rpmdb
  - %{_bindir}/rpmkeys
  - %{_bindir}/rpmqv
  - %{_bindir}/rpmsign
  - %{_mandir}/man1/rpm.1*
  - %{_mandir}/man8/rpm2cpio.8*
  - %{_mandir}/man8/rpmdb.8*
  - %{_mandir}/man8/rpmkeys.8*
  - %{_mandir}/man8/rpmqv.8*
  - %{_mandir}/man8/rpmsign.8*
  - %{_libdir}/librpm.so.*
  - %{_libdir}/librpmio.so.*
  - %{_libdir}/libzstd.so.*
  - %{_libdir}/rpm-plugins/*
changelog:
  - * %{today} Dan Carpenter <DanC403@gmail.com> - 4.20.1-1
  - - Initial RPM spec file.
