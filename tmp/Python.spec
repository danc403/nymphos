# -*- mode: rpm-spec -*-

Name:       python3.13
Version:    3.13.2
Release:    1%{?dist}
Summary:    A high-level scripting language
License:    Python-2.0
URL:        https://www.python.org/
Source0:    Python-%{version}.tar.xz
BuildRequires: pkg-config
Requires:     libtool-ltdl # Add more requires as needed (zlib, openssl, etc.)
Conflicts:    python3 # Avoid conflicts with generic python3 packages
Provides:
    - python(abi) = 3.13
Obsoletes:  python3 < %{version}
Prefix:     /usr
BuildRoot:  %{_tmppdir}/%{name}-%{version}-%{release}-root

%description
Python is an interpreted, interactive, object-oriented programming language often compared to Tcl, Perl, Java, or Scheme.

Python includes modules, classes, exceptions, very high level dynamic data types, and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems (X11, Motif, Tk, Mac, MFC).

This package provides Python 3.13.2. It is configured to be the default Python 3 on this system.

%build
%configure --enable-shared --with-system-ffi --with-dbmliborder=bdb --with-ensurepip=install
make

%install
make install DESTDIR=%{buildroot}
# Remove unnecessary files
rm -f %{buildroot}/usr/bin/idle3
rm -f %{buildroot}/usr/bin/pydoc3
rm -f %{buildroot}/usr/bin/2to3
rm -f %{buildroot}/usr/share/man/man1/idle3.1
rm -f %{buildroot}/usr/share/man/man1/pydoc3.1
rm -f %{buildroot}/usr/share/man/man1/2to3.1

# Create symlinks to make python3.13 the default python3 and python.
ln -s /usr/bin/python3.13 %{buildroot}/usr/bin/python3
ln -s /usr/bin/python3 %{buildroot}/usr/bin/python

%files
%license LICENSE.txt
%doc README.rst
/usr/bin/python3.13
/usr/bin/python3
/usr/bin/python
/usr/lib64/libpython3.13.so.1.0
/usr/lib64/python3.13/*
/usr/share/doc/Python-%{version}
/usr/share/man/man1/python3.1.gz
/usr/share/man/man1/python3.gz

%changelog
* %{DATE} Dan Carpenter DanC403@gmail.com - 3.13.2-1
- Initial build.
- Added symlinks to make this the default python3 and python.
