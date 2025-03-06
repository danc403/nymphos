Name:           mariadb-server
Version:        11.7.2
Release:        1%{?dist}
Summary:        MariaDB database server

License:        GPL-2.0-or-later with exceptions
URL:            https://mariadb.org/
Source0:        server-mariadb-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel
BuildRequires:  libaio-devel
BuildRequires:  ncurses-devel

%description
MariaDB is a community developed fork of MySQL intended to remain free under the GNU GPL.

%prep
%setup -q -n mariadb-server-%{version}

%build
cmake . \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DMYSQL_DATADIR=%{_localstatedir}/lib/mysql \
    -DSYSCONFDIR=/etc \
    -DWITH_SSL=system \
    -DWITH_ZLIB=system \
    -DWITH_PCRE=system \
    -DWITH_LIBWRAP=OFF \
    -DWITH_TOKUDB=OFF \
    -DWITH_ROCKSDB=OFF \
    -DWITH_MROONGA=OFF \
    -DWITH_SPIDER=OFF \
    -DWITH_OQGRAPH=OFF
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Install my.cnf
install -Dm644 support-files/my-default.cnf %{buildroot}/etc/my.cnf

# Install OpenRC init script (adjust as needed)
install -Dm755 support-files/mysql.server %{buildroot}%{_initrddir}/mariadb

# Create data directory
mkdir -p %{buildroot}%{_localstatedir}/lib/mysql

# Create log directory
mkdir -p %{buildroot}%{_localstatedir}/log/mariadb

%files
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/mysql/*
/etc/my.cnf
%{_localstatedir}/lib/mysql/
%{_localstatedir}/log/mariadb/
%{_initrddir}/mariadb
%{_mandir}/man1/*
%{_mandir}/man8/*

%pre
# Create user and group
getent group mysql >/dev/null || groupadd -r mysql
getent passwd mysql >/dev/null || useradd -r -g mysql -d %{_localstatedir}/lib/mysql -s /sbin/nologin -c "MariaDB Server" mysql

%post
# Initialize database
%{_sbindir}/mysql_install_db --user=mysql --datadir=%{_localstatedir}/lib/mysql

# Enable OpenRC service
rc-update add mariadb default

%preun
# Stop service before uninstall
if [ $1 -eq 0 ]; then
    /etc/init.d/mariadb stop >/dev/null 2>&1
fi

%postun
# Remove OpenRC service
if [ $1 -eq 0 ]; then
    rc-update del mariadb
fi

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 11.7.2-1
- Initial build for custom distribution.
