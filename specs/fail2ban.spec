# specs/fail2ban/fail2ban-1.1.0.spec
Name:           fail2ban
Version:        1.1.0
Release:        1%{?dist}
Summary:        Daemon to ban hosts that cause multiple authentication errors
License:        GPLv2+
URL:            https://www.fail2ban.org/
Source0:        fail2ban-1.1.0.tar.gz

BuildRequires:  python3-devel, systemd-units, nftables, python3-inotify, python3-pyinotify

Requires:       python3, nftables, python3-inotify, python3-pyinotify

%description
Fail2ban monitors log files like /var/log/pwdfail or /var/log/apache/error_log
and bans IP addresses that generate too many errors.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed --root=%{buildroot}
# Remove systemd unit files
rm -rf %{buildroot}%{_unitdir}

# Install OpenRC service file
install -Dm 755 fail2ban.openrc %{buildroot}/etc/init.d/fail2ban

#Install nftables action file.
install -Dm 644 files/action.d/nftables-multiport.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/nftables-multiport.conf

%files
%{python3_sitelib}/fail2ban/
%{python3_sitelib}/Fail2Ban-*.egg-info
%{_bindir}/fail2ban-client
%{_bindir}/fail2ban-server
%{_sysconfdir}/fail2ban/
/etc/init.d/fail2ban
%{_mandir}/man1/fail2ban-client.1*
%{_mandir}/man1/fail2ban-server.1*

%post
/sbin/rc-update add fail2ban default

%preun
/sbin/rc-update del fail2ban default

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 1.1.0-1
- Initial package.
