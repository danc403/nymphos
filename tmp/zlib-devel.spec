content:
  - Name:           zlib-devel
  - Version:        1.3.1
  - Release:        1%{?dist}
  - Summary:        Development files for zlib
  - 
  - License:        zlib
  - URL:            https://zlib.net/
  - 
  - Source0:        %{name:zlib}-%{version}.tar.gz
  - 
  - Requires:       zlib = %{version}-%{release}
  - 
  - %description
  - The zlib-devel package contains the header files and static libraries
  - necessary for developing applications which use the zlib compression
  - library.
  - 
  - %prep
  - %autosetup -n zlib-%{version}
  - 
  - %build
  - mkdir -p build
  - cd build
  - CFLAGS="%{optflags}" \
  - CXXFLAGS="%{optflags}" \
  - ../configure --prefix=%{buildroot}%{_prefix} --static
  - make %{?_smp_mflags}
  - 
  - %install
  - cd build
  - make install
  - 
  - rm -f %{buildroot}%{_libdir}/*.la
  - 
  - %files
  - %license zlib.h
  - %{_includedir}/zlib.h
  - %{_libdir}/libz.so
  - %{_libdir}/libz.a
  - %{_libdir}/pkgconfig/zlib.pc
  - 
  - %changelog
  - * Tue Oct 24 2023 Dan Carpenter DanC403@gmail.com - 1.3.1-1
  - - Initial package build
