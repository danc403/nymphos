content: Name:           pkg-config-devel
Version:        0.29.2
Release:        1%{?dist}
Summary:        Development files for pkg-config

License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/pkg-config/

Source0:        %{name:pkg-config}-%{version}.tar.gz
Requires:       pkg-config = %{version}-%{release}

%description
This package contains the header files and libraries needed to develop
applications that use pkg-config.

%prep
%autosetup -n pkg-config-%{version}

%build
# Nothing to do

%install
# Nothing to do

%files
%{_includedir}/pkg-config.h
%{_libdir}/pkgconfig/pkg-config.pc

%changelog
* %{?epoch:%{epoch}:}%{version}-%{release} %{?date:%{date}} Dan Carpenter DanC403@gmail.com
- Initial package build

filename: pkg-config-devel.spec
