spec_content: Name:           groff-devel
Version:        1.22.4
Release:        1%{?dist}
Summary:        Development files for groff

License:        GPLv3+
URL:            https://www.gnu.org/software/groff/

Source0:        groff-%{version}.tar.gz

BuildRequires:  groff == %{version}-%{release}

Requires: groff == %{version}-%{release}

%description
This package contains the header files and libraries needed to develop
applications that use groff.

%prep
%setup -q -n groff-%{version}

%build
# Nothing to build

%install
# Nothing to install

%files
%{_includedir}/groff.h
%{_libdir}/libgroff.a
%{_libdir}/pkgconfig/groff.pc

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 1.22.4-1
- Initial package build.
package_name: groff-devel
