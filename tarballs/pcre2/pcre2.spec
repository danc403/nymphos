Name: pcre2
Version: 10.45
Release: 1%{?dist}
Summary: Perl Compatible Regular Expressions library
License: BSD-3-Clause
URL: https://www.pcre.org/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
  - bzip2-devel
  - libbz2
Requires:
  - zlib
  - libbz2

%description
PCRE2 is a library of functions to support regular expressions whose
syntax and semantics are as close as possible to those of Perl 5.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENCE
%doc AUTHORS ChangeLog NEWS README.md
/usr/lib/libpcre2-8.so.*
/usr/lib/libpcre2-16.so.*
/usr/lib/libpcre2-32.so.*
/usr/bin/pcre2grep
/usr/bin/pcre2test
/usr/share/man/man1/pcre2grep.1*
/usr/share/man/man1/pcre2test.1*
/usr/share/man/man3/pcre2*.3*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of pcre2.
