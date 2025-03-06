Name:       dbus-glib
Version:    0.112
Release:    1%{?dist}
Summary:    GLib bindings for D-Bus

License:    LGPLv2.1+
URL:        https://www.freedesktop.org/wiki/Software/DBusBindings
Source0:    dbus-glib-%{version}.tar.gz

BuildRequires:  dbus-devel
BuildRequires:  glib2-devel
BuildRequires:  pkg-config

%description
D-Bus GLib bindings provide a high-level API for using D-Bus from GLib-based
applications.

%package devel
Summary:    Development files for dbus-glib
Requires:   dbus-glib = %{version}-%{release}

%description devel
This package contains the development files for dbus-glib.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libdbus-glib-1.so.*

%files devel
%{_includedir}/dbus-glib-1/
%{_libdir}/libdbus-glib-1.so
%{_libdir}/pkgconfig/dbus-glib-1.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
