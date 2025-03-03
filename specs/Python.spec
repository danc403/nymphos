Name:           python3
Version:        3.13.2
Release:        1%{?dist}
Summary:        An interpreted, interactive, object-oriented programming language
License:        PSF-2.0
URL:            https://www.python.org/
Source0:        Python-3.13.2.tar.xz

BuildArch:      x86_64

BuildRequires:  zlib-devel, bzip2-devel, xz-devel, openssl-devel, ncurses-devel, sqlite-devel, gdbm-devel, libffi-devel, readline-devel, libtirpc-devel, tk-devel, libxcrypt-devel

Requires:       zlib, bzip2, xz, openssl, ncurses, sqlite, gdbm, libffi, readline, libtirpc, tk, libxcrypt

%description
Python is an interpreted, interactive, object-oriented programming language
that combines remarkable power with very clear syntax.

%prep
%setup -q

%build
%configure --enable-optimizations --enable-shared --with-system-ffi --without-ensurepip --enable-loadable-sqlite-extensions --enable-ipv6 --with-computed-gotos
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} altinstall

# remove ensurepip
rm -rf %{buildroot}%{python3_sitelib}/ensurepip
rm -rf %{buildroot}%{_bindir}/pip3*

# remove systemd files
rm -rf %{buildroot}%{_libdir}/systemd

%files
%license LICENSE
%doc README.rst
%{_bindir}/python3*
%{_bindir}/idle3
%{_libdir}/libpython3*.so*
%{_libdir}/python3*
%{_includedir}/python3*
%{_mandir}/man1/python3.1*
%{_mandir}/man1/idle3.1*
%{_mandir}/man1/pydoc3.1*
%{_mandir}/man1/python3-config.1*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 3.13.2-1
- Initial package.
