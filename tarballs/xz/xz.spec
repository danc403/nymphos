Name: xz
Version: 5.4.1
Release: 1%{?dist}
Summary: XZ data compression utility
License: LGPL-2.1-or-later
URL: https://tukaani.org/xz/
Source0: %{name}-%{version}.tar.xz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
Requires:
  - glibc

%description
XZ Utils is a collection of command-line tools for compressing and
decompressing .xz files, which use the LZMA2 compression algorithm.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc AUTHORS NEWS README.md
/usr/bin/xz
/usr/bin/unxz
/usr/bin/xzcat
/usr/bin/lzma
/usr/bin/unlzma
/usr/bin/lzcat
/usr/lib/liblzma.so.*
/usr/share/man/man1/xz.1*
/usr/share/man/man1/unxz.1*
/usr/share/man/man1/xzcat.1*
/usr/share/man/man1/lzma.1*
/usr/share/man/man1/unlzma.1*
/usr/share/man/man1/lzcat.1*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of xz.
