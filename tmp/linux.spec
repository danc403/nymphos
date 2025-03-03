name: linux
version: 6.5.3
release: 1%{?dist}
summary: The Linux kernel
license: GPLv2
url: https://www.kernel.org/
source0: %{name}-%{version}.tar.xz
exclusivearch: x86_64
buildrequires:
  - gcc
  - make
  - binutils
  - bc
  - openssl
  - perl
  - python
  - util-linux
  - findutils
  - grep
  - gawk
  - sed
  - xz
  - gzip
  - bzip2
  - tar
requires:
  - coreutils
  - util-linux
  - findutils
  - grep
  - gawk
  - sed
  - xz
  - gzip
  - bzip2
  - tar
description: The Linux kernel.
prep:
  - %setup -q
build:
  - make -j %{nproc}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %doc
  - /boot/vmlinuz-%{version}
  - /boot/System.map-%{version}
  - /boot/config-%{version}
  - /usr/lib/modules/%{version}
changelog:
  - * Mon Oct 23 2023 Dan Carpenter DanC403@gmail.com - 6.5.3-1
  - - Initial package build
