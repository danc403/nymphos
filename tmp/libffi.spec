name: libffi
version: 3.4.4
release: 1%{?dist}
summary: A portable, high level programming interface to various calling conventions [MIT]
license: MIT
URL: https://sourceware.org/libffi/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
Requires:
BuildArch: x86_64
Description: The Foreign Function Interface (ffi) library provides a portable, high level programming interface to various calling conventions.  This allows a programmer to call functions that adhere to calling conventions that were not known at the time of compilation.
Prep:
  - %autosetup
Build:
  - ./configure
  - %{__make} %{?_smp_mflags}
Install:
  - %{__make} install DESTDIR=%{buildroot}
Files:
  - %{buildroot}/usr/lib64/libffi.so.*
  - %{buildroot}/usr/share/doc/%{name}-%{version}/LICENSE
  - %license LICENSE
Changelog:
  -
    date: Wed Oct 25 2023
    author: Dan Carpenter <DanC403@gmail.com>
    comment: Initial build
