Name:       cronie
Version:    1.7.2
Release:    1%{?dist}
Summary:    An enhanced version of vixie-cron

License:    GPLv2+
URL:        https://github.com/cronie-ie/cronie
Source0:    cronie-%{version}.tar.gz

BuildRequires: shadow-utils

%description
Cronie contains the standard UNIX daemon crond that runs specified programs
at scheduled times and related tools. It is based on the original vixie-cron,
but has several security and configuration enhancements.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/crond
%{_sbindir}/anacron
%{_bindir}/crontab
%{_mandir}/man1/crontab.1*
%{_mandir}/man8/crond.8*
%{_mandir}/man8/anacron.8*
%{_mandir}/man5/crontab.5*
%{_unitdir}/crond.service
/etc/cron.allow
/etc/cron.deny
/etc/anacrontab

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
