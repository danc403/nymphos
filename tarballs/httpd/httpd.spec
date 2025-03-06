Name:           httpd
Version:        2.4.63
Release:        1%{?dist}
Summary:        Apache HTTP Server

License:        Apache-2.0
URL:            http://httpd.apache.org/
Source0:        httpd-%{version}.tar.gz

BuildRequires:  apr-devel >= 1.6.5
BuildRequires:  apr-util-devel >= 1.6.3
BuildRequires:  pcre-devel
BuildRequires:  openssl-devel
BuildRequires:  gcc
BuildRequires:  make

%description
The Apache HTTP Server is a powerful and flexible web server.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir}/httpd \
    --localstatedir=%{_localstatedir}/httpd \
    --enable-so \
    --enable-ssl \
    --enable-rewrite \
    --enable-cgi \
    --enable-mime-magic \
    --enable-modules=most \
    --enable-mpms-shared=all \
    --with-mpm=event \
    --with-pcre \
    --with-ssl \
    --with-included-apr \
    --with-included-apr-util
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Debian-style virtual host directories
mkdir -p %{buildroot}%{_sysconfdir}/httpd/sites-available
mkdir -p %{buildroot}%{_sysconfdir}/httpd/sites-enabled

# Copy default configuration
install -Dm644 support/httpd.conf %{buildroot}%{_sysconfdir}/httpd/httpd.conf

# Create default virtual host file
cat > %{buildroot}%{_sysconfdir}/httpd/sites-available/000-default.conf <<EOF
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot %{_datadir}/www/html
    ErrorLog \${APACHE_LOG_DIR}/error.log
    CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF

# Enable default virtual host
ln -s %{_sysconfdir}/httpd/sites-available/000-default.conf %{buildroot}%{_sysconfdir}/httpd/sites-enabled/000-default.conf

# OpenRC init script (example, adjust as needed)
install -Dm755 support/apachectl %{buildroot}%{_initrddir}/httpd

# Create log directory
mkdir -p %{buildroot}%{_localstatedir}/log/httpd

%files
%{_bindir}/apachectl
%{_bindir}/apxs
%{_sbindir}/httpd
%{_libdir}/httpd/modules/*.so
%{_sysconfdir}/httpd/
%{_localstatedir}/log/httpd/
%{_mandir}/man8/httpd.8*
%{_mandir}/man8/apachectl.8*
%{_mandir}/man8/apxs.8*
%doc CHANGES LICENSE NOTICE README.md

%pre
# Create user and group
getent group apache >/dev/null || groupadd -r apache
getent passwd apache >/dev/null || useradd -r -g apache -d %{_localstatedir}/www -s /sbin/nologin -c "Apache HTTP Server" apache

%post
# Enable OpenRC service
rc-update add httpd default

%preun
# Stop service before uninstall
if [ $1 -eq 0 ]; then
    /etc/init.d/httpd stop >/dev/null 2>&1
fi

%postun
# Remove OpenRC service
if [ $1 -eq 0 ]; then
    rc-update del httpd
fi

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 2.4.63-1
- Initial build for custom distribution.
