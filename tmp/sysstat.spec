name: sysstat
version: 12.6.1
release: 1%{?dist}
summary: System Performance Tools
license: GPLv2+
url: https://github.com/sysstat/sysstat
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - gettext
  - perl
Requires:
  - coreutils
  - procps
  - cronie
BuildArch: x86_64
Autoreqprov: 0
Description: The sysstat utilities are a collection of performance monitoring tools for Linux. These tools include sar, iostat, mpstat, pidstat, and sadf.
Provides: config(sysstat)
Conflicts: procps < 3.2.7
Obsoletes: sysstat-oem
%prep:  %setup -q
%build:  %autoreconf -fvi
 %configure --disable-static
 make %{?_smp_mflags}
%install:  make install DESTDIR=%{buildroot}
%files:  %license COPYING
 %config(noreplace) %{_sysconfdir}/sysstat
 %{_sbindir}/*
 %{_bindir}/*
 %{_mandir}/man1/*
 %{_mandir}/man5/*
 %{_mandir}/man8/*
 %{_datadir}/sysstat/*
%changelog: * %{date} Dan Carpenter DanC403@gmail.com - 12.6.1-1
 - Initial build.
