name: fontconfig-devel
version: 2.15.0
release: 1%{?dist}
summary: Development files for fontconfig
license: MIT
url: https://gitlab.freedesktop.org/fontconfig/fontconfig
source0: %{name}-%{version}.tar.xz
requires:
  - fontconfig = %{version}-%{release}
buildrequires:
  - pkg-config
description: Development files for fontconfig
prep:
  - %autosetup
build:
  - ./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %{_includedir}/fontconfig/*.h
  - %{_libdir}/libfontconfig.so
  - %{_libdir}/pkgconfig/fontconfig.pc
changelog:
  - * Fri Oct 27 2023 Dan Carpenter DanC403@gmail.com - 2.15.0-1
  - - Initial package build
