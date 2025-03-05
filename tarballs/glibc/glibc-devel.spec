Name: glibc-devel
Version: 2.41
Release: 1%{?dist}
Summary: Development files for the GNU C Library
License: LGPLv2.1+ and GPLv2+
URL: https://www.gnu.org/software/libc/
Source0: glibc-2.41.tar.xz
Source1: glibc-crypt-2.1.tar.gz
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
  - glibc = %{version}-%{release}

%description
Development files for the GNU C Library.

%prep
%setup -q
tar -xzf %{SOURCE1} -C %{_builddir}/%{name}-%{version}/crypt

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
/usr/include/
/usr/lib/libc.so
/usr/lib/libm.so
/usr/lib/libpthread.so
/usr/lib/libdl.so
/usr/lib/libutil.so
/usr/lib/libnss_*
/usr/lib/libresolv.so
/usr/lib/librt.so
/usr/lib/ld-linux-x86-64.so
/usr/lib/crt1.o
/usr/lib/crti.o
/usr/lib/crtn.o
/usr/lib/Scrt1.o
/usr/lib/gcrt1.o
/usr/lib/gmon.a
/usr/lib/libmcheck.a
/usr/lib/libpcprofile.so
/usr/lib/libSegFault.so
/usr/lib/libcidn.a
/usr/lib/libnsl.a
/usr/lib/libsunmath.a
/usr/lib/libthread_db.so
/usr/lib/libanl.a
/usr/lib/libmemusage.so
/usr/lib/libpcprofile.a
/usr/lib/libresolv.a
/usr/lib/librt.a
/usr/lib/libutil.a
/usr/lib/libdl.a
/usr/lib/libpthread.a
/usr/lib/libc.a
/usr/lib/libm.a
/usr/lib/libcrypt.a
/usr/lib/libcrypt.so
/usr/include/crypt.h #add crypt.h

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of glibc-devel.
- disabled profile, obsolete add-ons, and enabled obsolete rpc.
- set kernel version to 4.15 minimum.
- Added glibc-crypt 2.1
