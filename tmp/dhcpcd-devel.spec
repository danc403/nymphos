name: dhcpcd-devel
version: 10.2.0
release: 1%{?dist}
summary: Development files for dhcpcd
License: BSD-2-Clause
URL: https://roy.marples.name/projects/dhcpcd
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
Requires:
  - dhcpcd = %{version}-%{release}
BuildArch: x86_64
Epoch: 0
Description: This package contains the development files for dhcpcd.
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%prep:
  - %setup -q
%build:
  - ./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
  - make
%install:
  - make install DESTDIR=%{buildroot}
%clean:
  - rm -rf %{buildroot}
%files:
  - %{_includedir}/dhcpcd.h
  - %{_libdir}/libdhcpcd.a
%changelog:
  - * %{today} Dan Carpenter DanC403@gmail.com - 10.2.0-1
  - - Initial build.
