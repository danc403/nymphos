spec_content: Name:           nano-devel
Version:        6.4
Release:        1%{?dist}
Summary:        Development files for nano - License: GPLv3+

License:        GPLv3+
URL:            https://www.nano-editor.org/

Source0:        %{name:nano}-%{version}.tar.xz

BuildRequires:  ncurses-devel
BuildRequires:  gettext
Requires:       nano = %{version}-%{release}
Requires:       pkgconfig

%description
This package contains the header files and libraries needed to develop
applications that use nano.

%prep
%autosetup -n nano-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_includedir}/nano/
%{_libdir}/libnano.so
%{_libdir}/pkgconfig/nano.pc

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 6.4-1
- Initial package build
package_name: nano-devel
