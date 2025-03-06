Name:       libcap-ng
Version:    0.8.5
Release:    1%{?dist}
Summary:    Library for manipulating POSIX capabilities

License:    LGPLv2.1+
URL:        https://people.redhat.com/sgrubb/libcap-ng/
Source0:    libcap-ng-%{version}.tar.gz

%package devel
Summary:    Development files for libcap-ng
Requires:   libcap-ng = %{version}-%{release}

%description
Libcap-ng is a library for manipulating POSIX capabilities.
It provides a simple API for setting and getting capabilities on files
and processes.

%description devel
This package contains the development files for libcap-ng.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libcap-ng.so.*

%files devel
%{_includedir}/cap-ng.h
%{_libdir}/libcap-ng.so
%{_libdir}/pkgconfig/libcap-ng.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
