content:
  - Name:           libtool-devel
  - Version:        2.4.7
  - Release:        1%{?dist}
  - Summary:        Development files for libtool
  - 
  - License:        GPLv2+
  - URL:            https://www.gnu.org/software/libtool/
  - 
  - Requires:       libtool = %{version}-%{release}
  - 
  - %description
  - This package contains the development files for libtool.
  - 
  - %prep
  - %setup -q -n libtool-%{version}
  - 
  - %build
  - ./configure --prefix=%{_prefix}
  - make %{?_smp_mflags}
  - 
  - %install
  - make install DESTDIR=%{buildroot}
  - 
  - %files
  - %{_includedir}/ltdl.h
  - %{_libdir}/libltdl.so
  - %{_libdir}/libltdl.a
  - %{_libdir}/pkgconfig/libltdl.pc
  - 
  - %changelog
  - * %{date} Dan Carpenter <DanC403@gmail.com> - 2.4.7-1
  - - Initial package build
