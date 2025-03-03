name: audit-devel
version: 3.0.9
release: 1%{?dist}
summary: Development files for audit
License: GPLv2+
url: https://people.redhat.com/sgrubb/audit/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - libcap-ng-devel
  - python3-devel
Requires: audit = %{version}-%{release}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: x86_64
Description: The audit-devel package contains the header files and libraries needed to develop applications that use the audit library.
%prep:
  - %setup -q
%build:
  - ./autogen.sh
  - %configure --disable-static
  - make %{?_smp_mflags}
%install:
  - rm -rf $RPM_BUILD_ROOT
  - make install DESTDIR=$RPM_BUILD_ROOT
  - find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} \;
%files:
  - %{_includedir}/libaudit.h
  - %{_libdir}/libaudit.so
  - %{_mandir}/man3/libaudit.3*
  - %{_libdir}/pkgconfig/libaudit.pc
%changelog:
  - * Mon Oct 26 2023 Dan Carpenter DanC403@gmail.com - 3.0.9-1
  - - Initial build
