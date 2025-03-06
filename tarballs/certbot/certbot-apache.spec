Name:       certbot-apache
Version:    2.11.1
Release:    1%{?dist}
Summary:    Apache plugin for Certbot

License:    Apache-2.0
URL:        https://certbot.eff.org/
Source0:    certbot_apache-%{version}.tar.gz

BuildRequires:  certbot = %{version}-%{release}
BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-pyOpenSSL

%description
Certbot Apache plugin.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed --root=%{buildroot}

%files
%{python3_sitelib}/certbot_apache/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
