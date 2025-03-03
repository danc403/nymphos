name: gperf
version: 3.1
release: 1%{?dist}
summary: GNU perfect hash function generator
license: GPLv3+
url: https://www.gnu.org/software/gperf/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
Requires:
  - glibc
BuildArch: x86_64
Description: Gperf is a perfect hash function generator.  For a given list of strings, it produces a hash function and associated code that can be used to look up whether a string is in the list.
Provides: config(gperf)
Conflicts: config(gperf)
Prefix: /usr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
package: gperf
prep:
  - %setup -q
build:
  - ./configure --prefix=%{_prefix}
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
clean:
  - rm -rf %{buildroot}
files:
  - %{_bindir}/gperf
  - %{_infodir}/gperf.info*
  - %license COPYING
changelog:
  - * %{today} Dan Carpenter <DanC403@gmail.com> - 3.1-1
  - - Initial package build.
