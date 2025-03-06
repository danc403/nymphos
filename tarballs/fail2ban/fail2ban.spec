Name:       fail2ban
Version:    1.1.0
Release:    1%{?dist}
Summary:    Daemon to ban hosts that cause multiple authentication errors

License:    GPLv2+
URL:        https://www.fail2ban.org/
Source0:    fail2ban-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pyinotify
BuildRequires:  iptables

%description
Fail2ban monitors log files like /var/log/pwdfail or /var/log/apache/error_log
and bans IP addresses that show a malicious sign -- too many password failures,
seeking for exploits, etc.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%{_bindir}/fail2ban-client
%{_bindir}/fail2ban-server
%{_mandir}/man1/fail2ban-client.1*
%{_mandir}/man1/fail2ban-server.1*
/etc/fail2ban/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
