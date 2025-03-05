Name: bzip2-devel
Version: 1.0.8
Release: 1%{?dist}
Summary: Development files for bzip2
License: BSD-like
URL: https://sourceware.org/bzip2/
Source0: bzip2-1.0.8.tar.gz
Requires:
  - bzip2 = %{version}-%{release}

%description
Development files for bzip2.

%prep
%setup -q

%build
make -f Makefile-libbz2_so %{?_smp_mflags}
make %{?_smp_mflags}

%install
make install PREFIX=%{buildroot}/usr
install -m 644 bzlib.h %{buildroot}/usr/include/

%files
%license LICENSE
/usr/include/bzlib.h
/usr/lib/libbz2.so
/usr/lib/libbz2.a
/usr/lib/pkgconfig/bzip2.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of bzip2-devel.
