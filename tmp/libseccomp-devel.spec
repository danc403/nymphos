name: libseccomp-devel
version: 2.6.0
release: 1%{?dist}
summary: Development files for libseccomp
license: LGPLv2.1
url: https://github.com/seccomp/libseccomp
source0: %{name|gsub(devel$,)}-%{version}.tar.gz
requires:
  - libseccomp = %{version}-%{release}
buildrequires:
  - autoconf
  - automake
  - libtool
description: Development files for libseccomp.
prep:
  - %autosetup -n libseccomp-%{version}
build:
  - ./autogen.sh
  - %configure
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - /usr/include/seccomp.h
  - /usr/lib64/libseccomp.so
  - /usr/lib64/pkgconfig/libseccomp.pc
changelog:
  -
    date: * %{?epoch:%epoch:}%{expand:%(%{strftime %%Y-%%m-%%d})} Dan Carpenter DanC403@gmail.com
    comment: - Initial package build
