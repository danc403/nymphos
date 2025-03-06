Name:       libcap
Version:    2.73
Release:    1%{?dist}
Summary:    POSIX 1003.1e capabilities

License:    BSD-3-Clause
URL:        https://sites.google.com/site/fullycapable/
Source0:    libcap-%{version}.tar.xz

%package devel
Summary:    Development files for libcap
Requires:   libcap = %{version}-%{release}

%description
Libcap provides support for getting and setting POSIX 1003.1e capabilities.

%description devel
This package contains the development files for libcap.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libcap.so.*
%{_sbindir}/capsh
%{_sbindir}/getcap
%{_sbindir}/setcap
%{_mandir}/man8/capsh.8*
%{_mandir}/man8/getcap.8*
%{_mandir}/man8/setcap.8*

%files devel
%{_includedir}/sys/capability.h
%{_libdir}/libcap.so
%{_libdir}/libcap.a
%{_libdir}/pkgconfig/libcap.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
