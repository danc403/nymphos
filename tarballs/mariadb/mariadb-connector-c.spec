Name:           mariadb-connector-c
Version:        3.4.4
Release:        1%{?dist}
Summary:        MariaDB Connector/C

License:        LGPL-2.1-or-later
URL:            https://mariadb.org/
Source0:        mariadb-connector-c-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  gcc

%description
MariaDB Connector/C is a C library for connecting to MariaDB servers.

%prep
%setup -q -n mariadb-connector-c-%{version}

%build
cmake . \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DWITH_SSL=SYSTEM
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libmariadb.so*
%{_includedir}/mariadb/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 3.4.4-1
- Initial build for custom distribution.
