spec_content:
  - Name:           gmp
  - Version:        6.3.0
  - Release:        1%{?dist}
  - Summary:        GNU Multiple Precision Arithmetic Library - LGPL license
  - 
  - License:        LGPLv3+
  - URL:            https://gmplib.org/
  - 
  - Source0:        %{name}-%{version}.tar.xz
  - 
  - BuildRequires:  m4
  - BuildRequires:  autoconf
  - BuildRequires:  automake
  - BuildRequires:  libtool
  - 
  - Provides:       libgmp = %{version}
  - Obsoletes:      libgmp < %{version}
  - 
  - %description
  - The GNU Multiple Precision Arithmetic Library (GMP) is a free library
  - for arbitrary precision arithmetic, operating on signed integers,
  - rational numbers, and floating point numbers.
  - 
  - %prep
  - %autosetup
  - 
  - %build
  - ./configure --prefix=%{_prefix}
  - make %{?_smp_mflags}
  - 
  - %install
  - make install DESTDIR=%{buildroot}
  - 
  - rm -f %{buildroot}%{_libdir}/*.la
  - 
  - %files
  - %license COPYING.LESSERv3
  - %doc AUTHORS NEWS README
  - %{_bindir}/gmp-chroot
  - %{_libdir}/libgmp.so.*
  - %{_infodir}/gmp.info*
  - 
  - %changelog
  - * %{_isodate} Dan Carpenter <DanC403@gmail.com> - %{version}-%{release}
  - - Initial package build
