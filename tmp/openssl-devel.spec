name: openssl-devel
version: 3.1.1
release: 1%{?dist}
summary: Development files for openssl
license: Apache License
url: https://www.openssl.org/
source0: %{name}-%{version}.tar.gz
requires:
  - openssl = %{version}-%{release}
buildrequires:
  - perl
  - zlib-devel
  - krb5-devel
description: Development files for openssl
prep:
  - %setup -q
build:
  - ./config --prefix=%{_prefix} --openssldir=%{_sysconfdir}/ssl shared zlib
  - make
install:
  - make install
files:
  - %{_includedir}/openssl/*.h
  - %{_libdir}/libssl.a
  - %{_libdir}/libcrypto.a
  - %{_libdir}/pkgconfig/libssl.pc
  - %{_libdir}/pkgconfig/libcrypto.pc
changelog:
  - * %{date} Dan Carpenter <DanC403@gmail.com> 3.1.1-1
  - - Initial package build
