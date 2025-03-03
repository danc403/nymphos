%global dist .el8

Name:           bc-devel
Version:        1.08.1
Release:        1%{?dist}
Summary:        Development files for the bc arbitrary precision calculator
License:        GPLv2+
URL:            https://git.savannah.gnu.org/cgit/bc.git
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  bc = %{version}-%{release}
Requires:       bc = %{version}-%{release}
BuildArch:      x86_64

%description
This package contains the header files and static libraries needed to develop
applications that use the bc arbitrary precision calculator library.

%prep
%setup -q -n %{name}-%{version}

%build
# No build required for devel package, files are already built by bc

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_includedir}/bc.h
%{_libdir}/libbc.a
%license COPYING

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 1.08.1-1
- Initial package build for bc-devel
