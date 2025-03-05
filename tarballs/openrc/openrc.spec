Name: openrc
Version: 0.56
Release: 1%{?dist}
Summary: Service manager for Linux
License: GPL-2.0+
URL: https://github.com/OpenRC/openrc
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - util-linux
  - bash
  - coreutils
  - grep
  - sed
  - awk
Requires:
  - util-linux
  - bash
  - coreutils
  - grep
  - sed
  - awk

%description
OpenRC is a dependency based init system that works with the system's
init program, normally /sbin/init. OpenRC is compatible with the
init scripts provided with Gentoo Linux.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README.md
/sbin/rc
/sbin/rc-update
/sbin/rc-service
/etc/init.d/
/etc/rc.conf
/etc/rc.d/
/usr/share/man/man8/rc.8*
/usr/share/man/man8/rc-update.8*
/usr/share/man/man8/rc-service.8*

%post
# Enable essential services (example, adjust as needed)
/sbin/rc-update add udev default
/sbin/rc-update add devfs default
/sbin/rc-update add procfs default
/sbin/rc-update add sysfs default
/sbin/rc-update add brltty default
/sbin/rc-update add speakup default

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of OpenRC.
- Added accessibility services to default runlevel.
