spec_content: Name:           openrc
Version:        0.56
Release:        1%{?dist}
Summary:        Service supervision daemon (OpenRC) - MIT License

License:        MIT
URL:            https://github.com/OpenRC/openrc

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  sed
BuildRequires:  pkg-config

Requires:       bash
Requires:       coreutils
Requires:       procps
Requires:       util-linux
Requires:       grep
Requires:       sed
Requires:       awk


%description
OpenRC is a dependency based init system for Linux. It's
compatible with sysvinit scripts, but offers far better
parallelization and service management.


%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove unneeded files
rm -f %{buildroot}/etc/init.d/functions

# Ensure proper permissions
chmod +x %{buildroot}/usr/bin/rc

%files
%license LICENSE
%{_sbindir}/openrc
%{_sbindir}/rc
%{_sbindir}/rc-service
%{_sbindir}/rc-update
%{_sbindir}/rc-status
%{_sbindir}/rc-run
%{_sbindir}/rc-config
%{_sbindir}/rc-parallel
%{_sbindir}/rc-sysinit
%{_sbindir}/rc-shutdown
%{_sbindir}/rc-reboot
%{_sbindir}/rc-halt
%{_sbindir}/rc-boot
%{_sbindir}/rc-single
%{_sysconfdir}/init.d
%{_mandir}/man8/rc.8*
%{_mandir}/man8/rc-service.8*
%{_mandir}/man8/rc-update.8*
%{_mandir}/man8/rc-status.8*
%{_mandir}/man8/rc-config.8*
%{_mandir}/man8/openrc.8*

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 0.56-1
- Initial package build.

