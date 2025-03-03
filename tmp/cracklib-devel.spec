content: Name:           cracklib-devel
Version:        2.9.7
Release:        1%{?dist}
Summary:        Development files for cracklib
License:        LGPLv2+
URL:            http://cracklib.sourceforge.net/

Source0:        %{name}-%{version}.tar.gz

Requires:       cracklib = %{version}-%{release}
BuildRequires:  bzip2-devel
BuildRequires:  libtool

%description
This package contains the header files and libraries needed to develop
applications that use cracklib.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_includedir}/crack.h
%{_libdir}/libcrack.a
%{_libdir}/libcrack.so
%{_libdir}/pkgconfig/cracklib.pc

%changelog
* %{DATE} Dan Carpenter <DanC403@gmail.com> - 2.9.7-1
- Initial package build

