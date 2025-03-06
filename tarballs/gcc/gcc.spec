Name:       gcc
Version:    13.2.0
Release:    1%{?dist}
Summary:    The GNU Compiler Collection

License:    GPLv3+ and others
URL:        https://gcc.gnu.org/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  binutils >= 2.40
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  mpc-devel
BuildRequires:  zlib-devel

%description
The GNU Compiler Collection (GCC) includes front ends for C, C++, Objective-C,
Fortran, Java, Ada, and Go, as well as libraries for these languages.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --enable-languages=c,c++ --disable-multilib
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_includedir}/*
%{_mandir}/man1/*

%package devel
Summary:    Development files for GCC
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files for GCC.

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
