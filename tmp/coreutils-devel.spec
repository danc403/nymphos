spec_content: Name:           coreutils-devel
Version:        9.3
Release:        1%{?dist}
Summary:        Development files for coreutils

License:        GPLv3+
URL:            https://www.gnu.org/software/coreutils/

Source0:        %{name:%{realname}}-%{version}.tar.xz

Requires:       coreutils = %{version}-%{release}


%description
This package contains the header files and libraries necessary to develop
applications that use the coreutils libraries.


%prep
%autosetup -n %{realname}-%{version}

%build

%install


%files


%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 9.3-1
- Initial package build.

