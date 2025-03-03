spec_content: Name:           diffutils-devel
Version:        3.9
Release:        1%{?dist}
Summary:        Development files for diffutils

License:        GPLv3+
URL:            https://www.gnu.org/software/diffutils/

Source0:        %{name:diffutils}-%{version}.tar.xz

BuildRequires:  diffutils = %{version}

Requires:       diffutils = %{version}

%description
This package contains the development files for diffutils.

%prep
%autosetup -n diffutils-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_includedir}/diffutils.h
%{_mandir}/man3/diffutils.3*

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 3.9-1
- Initial package build

package_name: diffutils-devel
