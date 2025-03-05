%global commit 4.4.38

Name:           libxcrypt
Version:        %{commit}
Release:        1%{?dist}
Summary:        Modern replacement for traditional libcrypt

License:        LGPLv2+ and BSD-3-Clause
URL:            https://github.com/bminor/libxcrypt
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  make

%description
libxcrypt is a modern replacement for the traditional libcrypt. It provides
implementations of various cryptographic hash functions for password storage,
including bcrypt, scrypt, and yescrypt.

%package devel
Summary:        Development files for libxcrypt
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libxcrypt.

%prep
%autosetup

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%check
%make_check

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%license COPYING
%{_libdir}/libxcrypt.so.*

%files devel
%{_includedir}/xcrypt.h
%{_libdir}/libxcrypt.a
%{_libdir}/libxcrypt.so
%{_libdir}/pkgconfig/libxcrypt.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-1
- Initial package.
