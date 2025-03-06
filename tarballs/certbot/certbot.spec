Name:       certbot
Version:    2.11.1
Release:    1%{?dist}
Summary:    Free and automated TLS certificates using the ACME protocol

License:    Apache-2.0
URL:        https://certbot.eff.org/
Source0:    certbot-%{version}.tar.gz

BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-pyOpenSSL

%description
Certbot is a free, open source software tool for automatically using
Let's Encrypt certificates on manually-administrated websites to
enable HTTPS.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed --root=%{buildroot}

%files
%{python3_sitelib}/certbot/
%{_bindir}/certbot
%{_mandir}/man1/certbot.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
