Name:       mpfr
Version:    4.2.0
Release:    1%{?dist}
Summary:    Multiple Precision Floating-Point Reliably

License:    LGPLv3+
URL:        https://www.mpfr.org/
Source0:    mpfr-%{version}.tar.xz

BuildRequires: gmp-devel

%package devel
Summary:    Development files for mpfr
Requires:   mpfr = %{version}-%{release}

%description
MPFR is a C library for multiple-precision floating-point computations
with correct rounding.

%description devel
This package contains the development files for mpfr.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libmpfr.so.*

%files devel
%{_includedir}/mpfr.h
%{_libdir}/libmpfr.so
%{_libdir}/libmpfr.a
%{_libdir}/pkgconfig/mpfr.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
