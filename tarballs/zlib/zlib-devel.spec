Name: zlib-devel
Version: 1.3.1
Release: 1%{?dist}
Summary: Header files and static libraries for zlib
License: Zlib
URL: https://www.zlib.net/
Source0: zlib-1.3.1.tar.gz
Requires:
  - zlib = %{version}-%{release}

%description
Header files and static libraries for zlib.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license zlib.h
/usr/include/zlib.h
/usr/lib/libz.so
/usr/lib/pkgconfig/zlib.pc
/usr/lib/libz.a

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of zlib-devel.
