Name:           libjpeg-turbo
Version:        3.1.0
Release:        1%{?dist}
Summary:        A SIMD-accelerated JPEG codec
License:        BSD
URL:            https://libjpeg-turbo.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake

%description
libjpeg-turbo is a JPEG image codec that uses SIMD instructions (MMX, SSE2, AVX2, NEON) to accelerate baseline JPEG compression and decompression on x86, x86-64, Arm, and PowerPC systems.

%package devel
Summary:        Development files for libjpeg-turbo
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libjpeg-turbo.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -G "Unix Makefiles"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE.md
%{_libdir}/libjpeg.so.*
%{_libdir}/libturbojpeg.so.*
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/tjbench
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/tjbench.1*

%files devel
%{_includedir}/turbojpeg.h
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h
%{_libdir}/libjpeg.a
%{_libdir}/libturbojpeg.a
%{_libdir}/pkgconfig/libjpeg.pc
%{_libdir}/pkgconfig/libturbojpeg.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
