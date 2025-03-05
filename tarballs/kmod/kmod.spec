Name: libkmod
Version: 34
Release: 1%{?dist}
Summary: Library to handle kernel module loading and unloading
License: LGPLv2+
URL: https://www.kernel.org/pub/linux/utils/kernel/kmod/
Source0: kmod-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
Requires:
  - zlib

%description
libkmod is a library to handle kernel module loading and unloading.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README.md
/usr/lib/libkmod.so.*
/usr/lib/pkgconfig/libkmod.pc
/usr/sbin/kmod
/usr/share/man/man8/kmod.8*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of libkmod.
