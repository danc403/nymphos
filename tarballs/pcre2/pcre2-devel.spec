Name: pcre2-devel
Version: 10.45
Release: 1%{?dist}
Summary: Development files for PCRE2
License: BSD-3-Clause
URL: https://www.pcre.org/
Source0: pcre2-10.45.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
  - bzip2-devel
  - libbz2
Requires:
  - pcre2 = %{version}-%{release}

%description
Development files for PCRE2.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENCE
/usr/include/pcre2.h
/usr/lib/libpcre2-8.so
/usr/lib/libpcre2-16.so
/usr/lib/libpcre2-32.so
/usr/lib/pkgconfig/libpcre2-8.pc
/usr/lib/pkgconfig/libpcre2-16.pc
/usr/lib/pkgconfig/libpcre2-32.pc
/usr/lib/libpcre2-posix.so
/usr/lib/pkgconfig/libpcre2-posix.pc
/usr/lib/libpcre2-8.a
/usr/lib/libpcre2-16.a
/usr/lib/libpcre2-32.a
/usr/lib/libpcre2-posix.a

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of pcre2-devel.
