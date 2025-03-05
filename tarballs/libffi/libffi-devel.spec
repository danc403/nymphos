Name: libffi-devel
Version: 3.4.4
Release: 1%{?dist}
Summary: Development files for libffi
License: MIT
URL: https://sourceware.org/libffi/
Source0: libffi-3.4.4.tar.gz
Requires:
  - libffi = %{version}-%{release}

%description
Development files for libffi.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
/usr/include/ffi.h
/usr/include/ffitarget.h
/usr/lib/libffi.so
/usr/lib/pkgconfig/libffi.pc
/usr/lib/libffi.a

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of libffi-devel.
