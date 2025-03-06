Name:       curl
Version:    8.12.1
Release:    1%{?dist}
Summary:    A command line tool for transferring data with URLs

License:    curl
URL:        https://curl.se/
Source0:    curl-%{version}.tar.xz

BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  libnghttp2-devel # For HTTP/2 support
BuildRequires:  brotli-devel # For Brotli compression support
BuildRequires:  libidn2-devel # For IDN support
BuildRequires:  libpsl-devel # For Public Suffix List support

%description
curl is a command line tool for transferring data with URLs.

%package libcurl
Summary:    A library for transferring data with URLs
Requires:   curl = %{version}-%{release}

%package libcurl-devel
Summary:    Development files for libcurl
Requires:   libcurl = %{version}-%{release}

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/curl
%{_mandir}/man1/curl.1*
/etc/curlrc

%files libcurl
%{_libdir}/libcurl.so.*

%files libcurl-devel
%{_includedir}/curl/
%{_libdir}/libcurl.so
%{_libdir}/pkgconfig/libcurl.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
