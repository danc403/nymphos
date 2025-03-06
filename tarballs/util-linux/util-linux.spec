Name:       util-linux
Version:    2.39
Release:    1%{?dist}
Summary:    A collection of basic system utilities

License:    GPLv2+
URL:        https://www.kernel.org/pub/linux/utils/util-linux/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  zlib-devel
BuildRequires:  libuuid-devel
BuildRequires:  libblkid-devel
BuildRequires:  pcre2-devel

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --without-python
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/libblkid.so.*
%{_libdir}/libfdisk.so.*
%{_libdir}/libmount.so.*
%{_libdir}/libsmartcols.so.*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%package devel
Summary:    Development files for util-linux
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files for util-linux.

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
