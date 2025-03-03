name: gperf-devel
version: 3.1
release: 1%{?dist}
summary: Development files for gperf - GNU perfect hash function generator
license: GPLv3+
url: https://www.gnu.org/software/gperf/
Requires:
  - gperf = %{version}-%{release}
BuildArch: x86_64
Description: This package contains the development files for gperf.
Prefix: /usr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
package: gperf-devel
files:
  - %{_includedir}/*
  - %{_libdir}/lib*.so
  - %{_libdir}/pkgconfig/*
changelog:
  - * %{today} Dan Carpenter <DanC403@gmail.com> - 3.1-1
  - - Initial package build.
