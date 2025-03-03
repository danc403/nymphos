content: Name:           texinfo-devel
Version:        7.0
Release:        1%{?dist}
Summary:        Development files for texinfo
License:        GPLv3+
URL:            https://www.gnu.org/software/texinfo/

Source0:        %{name:texinfo}-%{version}.tar.xz

BuildRequires:  texinfo = %{version}-%{release}

Requires:       texinfo = %{version}-%{release}

%description
This package contains the development files for texinfo.

%prep
# No prep needed

%build
# No build needed

%install
# No install needed. Already handled by main package.

%files
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 7.0-1
- Initial package build.

filename: texinfo-devel.spec
