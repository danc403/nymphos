name: libffi-devel
version: 3.4.4
release: 1%{?dist}
summary: Development files for libffi
license: MIT
URL: https://sourceware.org/libffi/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - libffi
Requires:
  - libffi = %{version}-%{release}
BuildArch: x86_64
Description: Development files for the libffi package.
Prep:
  - %autosetup
Build:
  - ./configure
  - %{__make} %{?_smp_mflags}
Install:
  - %{__make} install DESTDIR=%{buildroot}
Files:
  - %{buildroot}/usr/include/ffi.h
  - %{buildroot}/usr/include/ffitarget.h
  - %{buildroot}/usr/lib64/libffi.a
  - %{buildroot}/usr/lib64/libffi.la
  - %{buildroot}/usr/lib64/pkgconfig/libffi.pc
Changelog:
  -
    date: Wed Oct 25 2023
    author: Dan Carpenter <DanC403@gmail.com>
    comment: Initial build
