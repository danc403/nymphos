name: dbus-glib-devel
version: 0.112
release: 1%{?dist}
summary: Development files for dbus-glib
license: GPLv2+
url: https://dbus.freedesktop.org/doc/dbus-glib/
source0: dbus-glib-%{version}.tar.gz
buildrequires:
  - glib2-devel
  - dbus-devel
  - libxml2-devel
requires:
  - dbus-glib = %{version}-%{release}
description: Development files for dbus-glib.
prep: %setup -q
build: %configure
make: %{?_smp_mflags}
install: %{__make} install DESTDIR=%{buildroot}
files:
  - %{_includedir}/dbus-glib-1/dbus/*.h
  - %{_libdir}/libdbus-glib-1.so
  - %{_libdir}/pkgconfig/dbus-glib-1.pc
  - %{_datadir}/gir-1.0/DBusGLib-1.0.gir
changelog:
  -
    date: 2023-10-27
    name: Dan Carpenter
    email: DanC403@gmail.com
    changes: Initial build
