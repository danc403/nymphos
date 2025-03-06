Name:       dbus
Version:    1.16.0
Release:    1%{?dist}
Summary:    A message bus system

License:    LGPLv2.1+
URL:        https://www.freedesktop.org/wiki/Software/dbus
Source0:    dbus-%{version}.tar.xz

BuildRequires: pkg-config
BuildRequires: glib2-devel

%description
D-Bus is a message bus system that allows applications to communicate with each other.
It is used by many applications, including desktop environments.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc --disable-systemd
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/dbus-daemon
%{_bindir}/dbus-run-session
%{_bindir}/dbus-send
%{_bindir}/dbus-update-activation-state
%{_libdir}/libdbus-1.so.*
%{_includedir}/dbus-1.0/
%{_mandir}/man1/dbus-daemon.1*
%{_mandir}/man1/dbus-run-session.1*
%{_mandir}/man1/dbus-send.1*
%{_mandir}/man1/dbus-update-activation-state.1*
%{_mandir}/man3/dbus-connection.3*
%{_mandir}/man3/dbus-daemon.3*
%{_mandir}/man3/dbus-glib-*.3*
%{_datadir}/dbus-1/
/etc/dbus-1/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
