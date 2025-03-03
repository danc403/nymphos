%global dist .el8

Name:           cronie-devel
Version:        1.7.2
Release:        1%{?dist}
Summary:        Development files for cronie
License:        GPLv2+
URL:            https://github.com/cronie-org/cronie
Source0:        cronie-%{version}.tar.gz
BuildRequires:  cronie = %{version}-%{release}
Requires:       cronie = %{version}-%{release}
BuildArch:      x86_64

%description
This package contains the header files and static libraries needed to develop
applications that interact with the cronie daemon.

%prep
%setup -q -n cronie-%{version}

%build
# No build required for devel package, files are already built by cronie

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_includedir}/cronie.h
%{_libdir}/libcronie.a
%license COPYING

%changelog
* Tue Oct 24 2023 Dan Carpenter <DanC403@gmail.com> - 1.7.2-1
- Initial package build for cronie-devel
