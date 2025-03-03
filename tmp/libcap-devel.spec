%global dist .el8

Name:           libcap-devel
Version:        2.73
Release:        1%{?dist}
Summary:        Development files for the POSIX 1003.1e capabilities library
License:        BSD
URL:            https://sites.google.com/site/fullycapabilities/
Source0:        libcap-%{version}.tar.xz
BuildRequires:  libcap = %{version}-%{release}
Requires:       libcap = %{version}-%{release}
BuildRoot:      %{_tmppdir}/%{name}-%{version}-build
BuildArch:      x86_64

%description
This package contains the header files and static libraries needed to develop
applications that use the POSIX 1003.1e capabilities library.

%prep
%setup -q -n libcap-%{version}

%build
# No build required for devel package, files are already built by libcap

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_includedir}/sys/capability.h
%{_libdir}/libcap.a
%{_libdir}/libcap.so
%{_libdir}/pkgconfig/libcap.pc
%license LICENSE

%changelog
* Tue Oct 24 2023 Dan Carpenter <DanC403@gmail.com> - 2.73-1
- Initial package build for libcap-devel
