Name:       gmp
Version:    6.3.0
Release:    1%{?dist}
Summary:    GNU Multiple Precision Arithmetic Library

License:    LGPLv3+ or GPLv3+
URL:        https://gmplib.org/
Source0:    gmp-%{version}.tar.xz

%package devel
Summary:    Development files for gmp
Requires:   gmp = %{version}-%{release}

%description
The GNU Multiple Precision Arithmetic Library provides arbitrary precision
arithmetic for signed integers, rational numbers, and floating-point numbers.

%description devel
This package contains the development files for gmp.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --enable-cxx
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libgmp.so.*

%files devel
%{_includedir}/gmp.h
%{_libdir}/libgmp.so
%{_libdir}/libgmpxx.so.*
%{_libdir}/libgmpxx.a
%{_libdir}/libgmp.a
%{_libdir}/pkgconfig/gmp.pc
%{_libdir}/pkgconfig/gmpxx.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
