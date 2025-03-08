Name:       python3
Version:    3.13.2
Release:    1%{?dist}
Summary:    An interpreted, interactive, object-oriented programming language
License:    PSF-2.0
URL:        https://www.python.org/
Source0: %{name}-%{version}.tar.xz

BuildRequires:  zlib-devel bzip2-devel openssl-devel libffi-devel readline-devel sqlite-devel gdbm-devel ndbm-devel
BuildRequires:  pkgconfig

%description
Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax. Python's basic philosophy is that code is read much more often than it is written.

%prep
%autosetup -n Python-%{version}

%build
./configure --enable-optimizations --prefix=/usr --exec-prefix=/usr --enable-shared --with-ensurepip=yes --enable-ipv6 --enable-loadable-sqlite-extensions --with-computed-gotos --with-dbmliborder=bdb:gdbm:ndbm --enable-big-digits=30 --with-lto --enable-profiling
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%{_bindir}/python3
%{_bindir}/python3.13
%{_libdir}/libpython3.13.so.1.0
%{_libdir}/python3.13/
%{_includedir}/python3.13/
%{_mandir}/man1/python3.13.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
