content: Name:           xz-devel
Version:        5.4.1
Release:        1%{?dist}
Summary:        Development files for xz
License:        LGPLv2+ and GPLv2+
URL:            https://tukaani.org/xz/

Source0:        %{name:xz}-%{version}.tar.xz

Requires:       xz = %{version}-%{release}
BuildRequires:  gettext

%description
This package contains the header files and libraries needed to develop
applications that use xz.

%prep
%autosetup -n xz-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_includedir}/lzma.h
%{_libdir}/liblzma.a
%{_libdir}/pkgconfig/liblzma.pc

%changelog
* %{today} Dan Carpenter DanC403@gmail.com - 5.4.1-1
- Initial package build

filename: xz-devel.spec
