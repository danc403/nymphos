Name:           libva
Version:        2.22.0
Release:        1%{?dist}
Summary:        Video Acceleration (VA) API for Linux
License:        MIT
URL:            https://01.org/libva
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig

%description
libva is an implementation for VA-API (Video Acceleration API). It consists of an API specification and a library which provides an interface to access hardware video acceleration capabilities.

%package devel
Summary:        Development files for libva
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libva.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_libdir}/libva.so.*
%{_libdir}/va.drv/

%files devel
%{_includedir}/va/
%{_libdir}/libva.a
%{_libdir}/pkgconfig/va.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
