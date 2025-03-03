content: Name:           mpfr-devel
Version:        4.2.0
Release:        1%{?dist}
Summary:        Development files for mpfr

License:        LGPLv3+
URL:            https://www.mpfr.org/

Source0:        %{name:mpfr}-%{version}.tar.xz

Requires:       mpfr = %{version}-%{release}
Requires:       gmp-devel

%description
This package contains the development files for mpfr.

%prep
%setup -q -n mpfr-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_includedir}/mpfr.h
%{_libdir}/libmpfr.la
%{_libdir}/pkgconfig/mpfr.pc
%{_datadir}/aclocal/mpfr.m4

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 4.2.0-1
- Initial package build

