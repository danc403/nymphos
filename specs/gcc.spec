Name:           gcc
Version:        13.2.0
Release:        1%{?dist}
Summary:        The GNU Compiler Collection

License:        GPL+ and FDL
URL:            https://gcc.gnu.org/
Source0:        %{name}-%{version}.tar.xz

BuildArch:      x86_64

BuildRequires:  glibc-devel, glibc-headers, make, perl, texinfo, zlib-devel, gmp-devel, mpfr-devel, mpc-devel
Requires:       glibc

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, and Go, as well as libraries for these languages.

%prep
%setup -q

%build
./contrib/download_prerequisites
mkdir build && cd build
../configure --prefix=/usr --enable-languages=c,c++,fortran,objc,obj-c++,ada,go --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --disable-libgcj --with-isl --enable-multilib --with-tune=generic --with-arch_32=i686
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%license COPYING COPYING3 COPYING3.LIB COPYING.LIB COPYING.RUNTIME
%doc README
%{_bindir}/gcc
%{_bindir}/g++
%{_libdir}/libgcc_s.so.*
%{_libdir}/libstdc++.so.*
%{_includedir}/c++
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/g++.1*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 13.2.0-1
- Initial package
