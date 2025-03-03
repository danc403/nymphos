spec_content: Name:           sed-devel
Version:        4.9
Release:        1%{?dist}
Summary:        Development files for sed.
License:        GPLv3+
URL:            https://www.gnu.org/software/sed/

Requires:       sed = %{version}-%{release}

%description
This package contains the development files for sed.

%package -n sed-devel
Summary: Development files for sed.

%description -n sed-devel
This package contains the development files for sed.


%files -n sed-devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 4.9-1
- Initial package build.

