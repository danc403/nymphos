name: perl-devel
version: 5.40.1
release: 1%{?dist}
summary: Development files for Perl
license: Artistic License 1.0 or GPL
url: https://www.perl.org/
source0: %{name}-%{version}.tar.gz
requires:
  - perl = %{version}
provides:
  - perl(:MODULE_COMPAT_%{version})
description: This package contains the header files and libraries needed to develop Perl extensions.
files:
  - %{_includedir}/perl*
  - %{_libdir}/perl5/CORE/*
  - %{_libdir}/pkgconfig/perl.pc
changelog:
  - * %{date} Dan Carpenter DanC403@gmail.com - %{version}-%{release}
  - - Initial package build.
