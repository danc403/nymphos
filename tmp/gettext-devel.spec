spec_content: Name:       gettext-devel
Version:    0.21.1
Release:    1%{?dist}
Summary:    Development files for gettext
License:    GPLv3+
URL:        https://www.gnu.org/software/gettext/

Source0:    gettext-%{version}.tar.xz

BuildRequires:  gettext = %{version}

Requires:       gettext = %{version}
Requires:       glibc-devel

%description
This package contains the header files and libraries needed to develop
applications that use gettext.

%prep
%autosetup -n gettext-%{version}

%build
# Intentionally empty, as the build is part of the main package

%install
# Intentionally empty, as the install is part of the main package

%files
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%{_mandir}/man7/*

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 0.21.1-1
- Initial package build

package_name: gettext-devel
