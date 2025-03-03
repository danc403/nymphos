content: Name:           gzip-devel
Version:        1.12
Release:        1%{?dist}
Summary:        Development files for gzip.
License:        GPLv3+
Requires:       gzip = %{version}-%{release}


URL:            https://www.gnu.org/software/gzip/
Source0:        %{name:gzip}-%{version}.tar.xz

BuildRequires:  gettext

%description
This package contains the development files for gzip.

%prep
%setup -q -n gzip-%{version}

%build
%configure
%make_build

%install
%make_install

# No development files for gzip
%files


%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 1.12-1
- Initial package build.

filename: gzip-devel.spec
