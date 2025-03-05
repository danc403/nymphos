Name: openssl
Version: 3.1.1
Release: 1%{?dist}
Summary: OpenSSL cryptographic library and tools
License: Apache-2.0
URL: https://www.openssl.org/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - make
  - gcc
  - perl
  - zlib-devel
Requires:
  - zlib

%description
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, full-featured toolkit implementing the Secure Sockets
Layer (SSL) and Transport Layer Security (TLS) protocols as well as a
full-strength general purpose cryptography library.

%prep
%setup -q

%build
./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib shared zlib
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE.txt
%doc CHANGES.md README.md
/usr/bin/openssl
/usr/lib/libcrypto.so.*
/usr/lib/libssl.so.*
/etc/ssl/
/usr/share/man/man1/openssl.1*
/usr/share/man/man3/crypto.3*
/usr/share/man/man3/ssl.3*

%post
/sbin/ldconfig
update-ca-trust force-anchor # If you are using update-ca-trust

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of openssl.
