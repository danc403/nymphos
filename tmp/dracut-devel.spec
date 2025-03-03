name: dracut-devel
version: 059
release: 1%{?dist}
summary: Development files for dracut
license: GPLv2+
url: https://github.com/dracutdevs/dracut
source0: %{name:dracut}-%{version}.tar.gz
requires:
  - dracut = %{version}-%{release}
description: This package contains the header files and libraries needed to develop programs that use dracut.
prep:
  - %autosetup
build:
  - ./autogen.sh
  - %configure
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - /usr/include/*
  - /usr/lib64/pkgconfig/*
changelog:
  - * Wed Oct 25 2023 Dan Carpenter <DanC403@gmail.com> - 059-1
  - - Initial RPM build
