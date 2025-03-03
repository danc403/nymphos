name: gcc-devel
version: 13.2.0
release: 1%{?dist}
summary: Development files for GCC
license: GPLv3+
url: https://gcc.gnu.org/
requires:
  - gcc = %{version}-%{release}
description: This package contains the header files and libraries needed to develop applications that use the GNU Compiler Collection.
files:
  - /usr/include/*
  - /usr/lib64/lib*.so
  - /usr/lib64/pkgconfig/*
changelog:
  - * %{date} Dan Carpenter DanC403@gmail.com - 13.2.0-1
  - - Initial build
