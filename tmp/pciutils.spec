%global dist .el8

Name:           pciutils
Version:        3.9.0
Release:        1%{?dist}
Summary:        Utilities for inspecting and manipulating PCI devices
License:        GPLv2+
URL:            https://mj.ucw.cz/pciutils.shtml
Source0:        pciutils-%{version}.tar.xz
BuildRequires:  zlib-devel
Requires:       libpci >= %{version}

%description
The PCI Utilities package contains a library for accessing PCI configuration space and several utilities based on it. These utilities allow you to examine and manipulate PCI devices.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%license COPYING
/usr/sbin/*
/usr/share/man/man8/*
/usr/share/pci.ids
/usr/share/hwdata/pci.ids
%{_libdir}/libpci.so.*
%{_libdir}/libpciaccess.so.*
/usr/share/man/man3/*

%changelog
* %{today} Dan Carpenter <DanC403@gmail.com> - 3.9.0-1
- Initial RPM build
