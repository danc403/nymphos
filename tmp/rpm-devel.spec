name: rpm-devel
version: 4.20.1
release: 1%{?dist}
summary: Development files for RPM
license: GPLv2+
url: https://rpm.org/
source0: rpm-%{version}.tar.bz2
requires:
  - rpm = %{version}-%{release}
buildrequires:
  - pkg-config
description: This package contains the header files and libraries needed to develop applications that use the RPM Package Manager.
prep:
  - %setup -q
build:
  - ./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --mandir=%{_mandir}
  - %{__make} %{?_smp_mflags}
install:
  - %{__make} install DESTDIR=%{buildroot}
files:
  - %{_includedir}/rpm/*.h
  - %{_libdir}/librpm.so
  - %{_libdir}/librpmio.so
  - %{_libdir}/pkgconfig/rpm.pc
  - %{_libdir}/pkgconfig/rpmio.pc
changelog:
  - * %{today} Dan Carpenter <DanC403@gmail.com> - 4.20.1-1
  - - Initial RPM -devel spec file.
