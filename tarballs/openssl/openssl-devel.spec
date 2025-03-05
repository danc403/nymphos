Name: openssl-devel
Version: 3.1.1
Release: 1%{?dist}
Summary: Development files for OpenSSL
License: Apache-2.0
URL: https://www.openssl.org/
Source0: openssl-3.1.1.tar.gz
BuildRequires:
  - make
  - gcc
  - perl
  - zlib-devel
Requires:
  - openssl = %{version}-%{release}

%description
Development files for OpenSSL.

%prep
%setup -q

%build
./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib shared zlib
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE.txt
/usr/include/openssl/
/usr/lib/libcrypto.so
/usr/lib/libssl.so
/usr/lib/pkgconfig/libcrypto.pc
/usr/lib/pkgconfig/libssl.pc
/usr/lib/engines-3/

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of openssl-devel.
