%global dist .el8

Name:           shadow-devel
Version:        4.17.2
Release:        1%{?dist}
Summary:        Development files for shadow
License:        BSD-3-Clause
URL:            https://github.com/shadow-maint/shadow
Source0:        shadow-%{version}.tar.xz
Requires:       shadow = %{version}-%{release}
BuildRequires:  shadow = %{version}-%{release}

%description
This package contains the header files and static libraries needed to develop
applications that use the shadow utilities.

%prep
%setup -q -n shadow-%{version}

%build
# No build required for devel package, files are already built by shadow

%install
make install DESTDIR=%{buildroot} SBINDIR=/usr/bin MANDIR=/usr/share/man

%files
%defattr(-,root,root,-)
%{_includedir}/shadow.h
%{_libdir}/libshadow.a
%license COPYING

%changelog
* Tue Oct 24 2023 Dan Carpenter <DanC403@gmail.com> - 4.17.2-1
- Initial build for shadow-devel
