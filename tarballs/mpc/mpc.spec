Name:       mpc
Version:    1.3.1
Release:    1%{?dist}
Summary:    A C library for the arbitrary precision complex arithmetic

License:    LGPLv3+
URL:        https://www.multiprecision.org/mpc/
Source0:    mpc-%{version}.tar.gz

BuildRequires: gmp-devel
BuildRequires: mpfr-devel

%package devel
Summary:    Development files for mpc
Requires:   mpc = %{version}-%{release}

%description
MPC is a C library for the arithmetic of complex numbers with arbitrary
high precision and correct rounding of the result.

%description devel
This package contains the development files for mpc.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libmpc.so.*

%files devel
%{_includedir}/mpc.h
%{_libdir}/libmpc.so
%{_libdir}/libmpc.a
%{_libdir}/pkgconfig/mpc.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
