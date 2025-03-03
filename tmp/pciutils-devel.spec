%global dist .el8

Name:           pciutils-devel
Version:        3.9.0
Release:        1%{?dist}
Summary:        Development files for pciutils
License:        GPLv2+
URL:            https://mj.ucw.cz/pciutils.shtml
Source0:        pciutils-%{version}.tar.xz
Requires:       pciutils = %{version}-%{release}
BuildRequires:  pciutils = %{version}-%{release}

%description
This package contains the header files and static libraries needed to develop
applications that use the pciutils library.

%prep
%setup -q -n pciutils-%{version}

%build
# No build required for devel package, files are already built by pciutils

%install
%make_install

%files
%defattr(-,root,root,-)
%{_includedir}/pci/pci.h
%{_includedir}/pci/access.h
%{_libdir}/libpci.a
%{_libdir}/libpciaccess.a
%{_libdir}/pkgconfig/libpci.pc
%{_libdir}/pkgconfig/libpciaccess.pc
%license COPYING

%changelog
* %{today} Dan Carpenter <DanC403@gmail.com> - 3.9.0-1
- Initial build for pciutils-devel
