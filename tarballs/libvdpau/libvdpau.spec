Name:           libvdpau
Version:        1.5
Release:        1%{?dist}
Summary:        VDPAU library
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/VDPAU/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig

%description
libvdpau is an implementation of the VDPAU (Video Decode and Presentation API for Unix) library. It provides an interface to access video decode acceleration capabilities.

%package devel
Summary:        Development files for libvdpau
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libvdpau.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_libdir}/libvdpau.so.*

%files devel
%{_includedir}/vdpau/
%{_libdir}/libvdpau.a
%{_libdir}/pkgconfig/vdpau.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
