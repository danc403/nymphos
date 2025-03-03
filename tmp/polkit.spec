content: Name:           polkit
Version:        1.23
Release:        1%{?dist}
Summary:        Application authorization framework (BSD License)

License:        BSD
URL:            https://www.freedesktop.org/software/polkit/

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  glib2-devel
BuildRequires:  libselinux-devel
BuildRequires:  pam-devel
BuildRequires:  systemd-devel

Requires:       dbus
Requires:       glib2
Requires:       libselinux
Requires:       pam

%description
PolicyKit is an application-level toolkit for defining and handling
the concept of privileges. It provides a consistent mechanism for
non-privileged processes to execute privileged processes.

%prep
%autosetup

%build
./autogen.sh
%configure --disable-static --with-console-helper-group=wheel
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# OpenRC init script (example, adjust as needed)
mkdir -p %{buildroot}/etc/init.d
# install -m 755 %{SOURCE_DIR}/openrc.init %{buildroot}/etc/init.d/%{name}

# Remove systemd user files
rm -rf %{buildroot}%{_libdir}/systemd
rm -rf %{buildroot}%{_datadir}/dbus-1/system.d

%post
%sysrcd_enable polkit

%preun
%sysrcd_disable polkit

%files
%{_bindir}/pkaction
%{_bindir}/pkcheck
%{_bindir}/pkexec
%{_libdir}/libpolkit*.so.*
%{_datadir}/polkit-1
%{_mandir}/man1/pkaction.1.*
%{_mandir}/man1/pkcheck.1.*
%{_mandir}/man1/pkexec.1.*
%{_mandir}/man8/polkitd.8.*
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.PolicyKit1.service
%{_unitdir}/polkit.service
%{_unitdir}/polkit.socket
/etc/init.d/polkit
%{_datadir}/doc/%{name}
%license COPYING

%changelog
* %{_isodate} Dan Carpenter <DanC403@gmail.com> - 1.23-1
- Initial build

filename: polkit.spec
