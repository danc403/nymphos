name: man-db
version: 2.11.2
release: 1%{?dist}
summary: An utility for accessing the on-line manuals (man pages)
license: GPLv2+
url: https://man-db.nongnu.org/
source0: man-db-2.11.2.tar.xz
buildrequires:
  - gettext
  - groff
  - less
  - gzip
  - bzip2
  - xz
  - zlib-devel
  - pkgconfig(libpipeline)
  - pkgconfig(gdbm)
requires:
  - less
  - gzip
  - bzip2
  - xz
  - zlib
description: The man-db package includes utilities for accessing the on-line system documentation. These utilities make it easier to find and read the on-line manual pages.
prep:
  - %setup -q
build:
  - %configure --disable-debug
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %license COPYING
  - %doc README NEWS AUTHORS
  - %{_bindir}/man
  - %{_bindir}/mandb
  - %{_bindir}/whatis
  - %{_bindir}/apropos
  - %{_bindir}/manpath
  - %{_sysconfdir}/man_db.conf
  - %{_datadir}/man
  - %{_datadir}/man-db
changelog:
  -
    date: * Mon Oct 30 2023
    name: Dan Carpenter
    email: DanC403@gmail.com
    changes: - Initial RPM build
