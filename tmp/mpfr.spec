content: Name:           mpfr
Version:        4.2.0
Release:        1%{?dist}
Summary:        C library for multiple-precision floating-point computations with correct rounding - LGPL License

License:        LGPLv3+
URL:            https://www.mpfr.org/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gmp-devel

%description
The MPFR library is a C library for multiple-precision floating-point
computations with correct rounding.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libmpfr.so.*
%{_includedir}/mpfr.h
%{_datadir}/aclocal/mpfr.m4
%{_mandir}/man3/mpfr.3*
%{_infodir}/mpfr.info*
%{_libdir}/libmpfr.la
%{_datadir}/mpfr/mpfr.info
%{_docdir}/%{name}/COPYING.LESSER

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 4.2.0-1
- Initial package build

