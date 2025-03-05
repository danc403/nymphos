Name: glibc
Version: 2.41
Release: 1%{?dist}
Summary: The GNU C Library
License: LGPLv2.1+ and GPLv2+
URL: https://www.gnu.org/software/libc/
Source0: %{name}-%{version}.tar.xz
Source1: glibc-crypt-2.1.tar.gz # Add Source1
BuildRequires:
  - kernel-headers
  - make
  - gcc
  - binutils
  - tar
  - gzip
  - sed
  - awk
  - perl
Requires:
  - kernel-headers

%description
The GNU C Library provides the core libraries for the C programming
language. It is a fundamental part of the GNU system and is used by
virtually every application on the system.

%prep
%setup -q
tar -xzf %{SOURCE1} -C %{_builddir}/%{name}-%{version}/crypt # Extract glibc-crypt

%build
mkdir build
cd build
../configure --prefix=/usr --disable-profile --enable-add-ons= --enable-kernel=4.15 --with-headers=/usr/include --enable-obsolete-rpc
make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

%files
%license COPYING COPYING.LIB
%doc NEWS README ChangeLog
/usr/lib/libc.so.*
/usr/lib/libm.so.*
/usr/lib/libpthread.so.*
/usr/lib/libdl.so.*
/usr/lib/libutil.so.*
/usr/lib/libnss_*
/usr/lib/libresolv.so.*
/usr/lib/librt.so.*
/usr/lib/ld-linux-x86-64.so.*
/usr/bin/ldconfig
/usr/sbin/nscd
/etc/nsswitch.conf
/etc/ld.so.conf.d/
/usr/share/man/man3/*
/usr/share/man/man7/*
/usr/share/zoneinfo/
/usr/lib/locale/
/usr/lib/libcrypt.so.* #add libcrypt

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of glibc.
- disabled profile, obsolete add-ons, and enabled obsolete rpc.
- set kernel version to 4.15 minimum.
- added glibc-crypt 2.1
