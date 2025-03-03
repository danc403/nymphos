%global dist .el8

Name:           cronie
Version:        1.7.2
Release:        1%{?dist}
Summary:        Enhanced versions of standard UNIX daemons crond and crontab
License:        GPLv2+
URL:            https://github.com/cronie-org/cronie
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pam-devel
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
Requires:       pam
Requires:       libcap
Requires:       shadow-utils
BuildRoot:      %{_tmppdir}/%{name}-%{version}-%{release}-root

%description
Cronie contains the standard UNIX daemons crond and crontab,
which are used to execute programs at scheduled times. It is a fork
of the Vixie Cron project, and has been enhanced with several new
features and security improvements.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/crond
%{_sbindir}/crontab
%{_sysconfdir}/cron.d/*
%{_sysconfdir}/cron.hourly/*
%{_sysconfdir}/cron.daily/*
%{_sysconfdir}/cron.weekly/*
%{_sysconfdir}/cron.monthly/*
%{_mandir}/man1/crontab.1*
%{_mandir}/man5/crontab.5*
%{_mandir}/man8/crond.8*
%{_initrddir}/cronie
%license COPYING

%post
rc-update add cronie default

%preun
rc-service cronie stop

%postun
rc-update del cronie default

%changelog
* Tue Oct 24 2023 Dan Carpenter <DanC403@gmail.com> - 1.7.2-1
- Initial package build.
