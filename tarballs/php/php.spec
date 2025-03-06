Name:           php
Version:        8.4.4
Release:        1%{?dist}
Summary:        PHP scripting language for creating dynamic web pages

License:        PHP-3.01
URL:            https://www.php.net/
Source0:        php-src-php-%{version}.tar.gz

BuildRequires:  libxml2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  openssl-devel
BuildRequires:  mariadb-devel
BuildRequires:  pcre-devel
BuildRequires:  gcc
BuildRequires:  make

%description
PHP is a widely-used general-purpose scripting language that is especially
suited for web development and can be embedded into HTML.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix}/php8 \
    --with-config-file-path=/etc/php8 \
    --enable-fpm \
    --enable-cli \
    --enable-mbstring \
    --enable-zip \
    --with-openssl \
    --with-mysqli=mysqlnd \
    --with-pdo-mysql=mysqlnd \
    --with-gd \
    --with-curl \
    --with-pcre-regex
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Install php-fpm configuration
install -Dm644 sapi/fpm/php-fpm.conf %{buildroot}/etc/php8/php-fpm.conf

# Install php.ini
install -Dm644 php.ini-production %{buildroot}/etc/php8/php.ini

# Install php-fpm OpenRC init script (adjust as needed)
install -Dm755 sapi/fpm/php-fpm %{buildroot}%{_initrddir}/php-fpm

# Create php-fpm log directory
mkdir -p %{buildroot}/var/log/php-fpm

%files
%{_prefix}/php8/bin/*
%{_prefix}/php8/sbin/*
%{_prefix}/php8/lib/php/extensions/*
/etc/php8/
/var/log/php-fpm/
%{_initrddir}/php-fpm
%{_mandir}/man1/php.1*
%{_mandir}/man8/php-fpm.8*

%pre
# Create user and group
getent group php-fpm >/dev/null || groupadd -r php-fpm
getent passwd php-fpm >/dev/null || useradd -r -g php-fpm -d /var/www -s /sbin/nologin -c "PHP-FPM Server" php-fpm

%post
# Enable OpenRC service
rc-update add php-fpm default

%preun
# Stop service before uninstall
if [ $1 -eq 0 ]; then
    /etc/init.d/php-fpm stop >/dev/null 2>&1
fi

%postun
# Remove OpenRC service
if [ $1 -eq 0 ]; then
    rc-update del php-fpm
fi

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 8.4.4-1
- Initial build for custom distribution.
