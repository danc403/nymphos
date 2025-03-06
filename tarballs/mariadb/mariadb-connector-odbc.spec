Name:           mariadb-connector-odbc
Version:        3.2.5
Release:        1%{?dist}
Summary:        MariaDB Connector/ODBC

License:        LGPL-2.1-or-later
URL:            https://mariadb.org/
Source0:        mariadb-connector-odbc-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  unixODBC-devel
BuildRequires:  openssl-devel
BuildRequires:  gcc

%description
MariaDB Connector/ODBC is an ODBC driver for connecting to MariaDB servers.

%prep
%setup -q -n mariadb-connector-odbc-%{version}

%build
cmake . \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DWITH_SSL=SYSTEM
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libmaodbc.so*
%{_libdir}/odbc/libmaodbc.so*
%{_includedir}/maodbc/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 3.2.5-1
- Initial build for custom distribution.
