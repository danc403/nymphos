content: Name:           automake-devel
Version:        1.16.5
Release:        1%{?dist}
Summary:        Development files for automake
License:        GPLv2+
URL:            https://www.gnu.org/software/automake/

Source0:        automake-%{version}.tar.gz

BuildRequires:  automake = %{version}

Requires:       automake = %{version}

%description
This package contains the development files for automake.

%prep
# No prep needed

%build
# No build needed

%install
# No install needed

%files
%{_datadir}/aclocal/autoconf.m4

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 1.16.5-1
- Initial package build

filename: automake-devel.spec
