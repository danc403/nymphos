Name: python3
Version: 3.13.2
Release: 1%{?dist}
Summary: The Python 3 interpreter
License: PSF-2.0
URL: https://www.python.org/
Source0: %{name}-%{version}.tar.xz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
  - bzip2-devel
  - xz-devel
  - openssl-devel
  - libffi-devel
  - readline-devel
  - ncurses-devel
  - libxcrypt-devel
Requires:
  - zlib
  - bzip2
  - xz
  - openssl
  - libffi
  - readline
  - ncurses
  - libxcrypt

%description
Python 3 is an interpreted, interactive, object-oriented programming
language that combines remarkable power with very clear syntax.

%prep
%setup -q

%build
./configure --enable-optimizations --enable-shared --with-system-ffi --with-computed-gotos
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

#create symlinks
ln -sf /usr/bin/python3.%{version} %{buildroot}/usr/bin/python3
ln -sf /usr/bin/python3 %{buildroot}/usr/bin/python
ln -sf /usr/bin/pip3.%{version} %{buildroot}/usr/bin/pip3
ln -sf /usr/bin/pip3 %{buildroot}/usr/bin/pip

%files
%license LICENSE
%doc README.rst NEWS.d
/usr/bin/python3.%{version}
/usr/bin/python3
/usr/bin/python
/usr/bin/pip3.%{version}
/usr/bin/pip3
/usr/bin/pip
/usr/lib/libpython3.%{version}.so.*
/usr/lib/python3.%{version}/
/usr/include/python3.%{version}/
/usr/share/man/man1/python3.1*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of python3.
