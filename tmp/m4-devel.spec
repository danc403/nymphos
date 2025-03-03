spec_content: %define debug_package %{nil}

Name:           m4-devel
Version:        1.4.19
Release:        1%{?dist}
Summary:        Development files for m4

License:        GPLv3+
URL:            https://www.gnu.org/software/m4/
Source0:        %{name:m4}-%{version}.tar.gz

BuildRequires:  m4 = %{version}-%{release}

Requires:       m4 = %{version}-%{release}

%description
This package contains the development files for m4.

%prep
%setup -q -n m4-%{version}

%install

%files
%{_includedir}/m4.h
%{_libdir}/libm4.a
%{_infodir}/m4.info*

%changelog
* %{DATE} Dan Carpenter DanC403@gmail.com - 1.4.19-1
- Initial package build.

