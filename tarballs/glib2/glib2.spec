Name: glib2
Version: 2.83.5
Release: 1%{?dist}
Summary: GLib library of C routines
License: LGPL-2.1-or-later
URL: https://www.gtk.org/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
  - libffi-devel
  - pcre-devel
  - python3
Requires:
  - zlib
  - libffi
  - pcre

%description
GLib is a general-purpose utility library, which provides many useful
data types, macros, type conversions, string utilities, file utilities,
and main loop abstraction.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README NEWS
/usr/lib/libglib-2.0.so.*
/usr/lib/libgobject-2.0.so.*
/usr/lib/libgmodule-2.0.so.*
/usr/lib/libgio-2.0.so.*
/usr/bin/gapplication
/usr/bin/gdbus
/usr/bin/gio
/usr/bin/glib-compile-resources
/usr/bin/glib-compile-schemas
/usr/bin/gsettings
/usr/share/glib-2.0/
/usr/share/man/man1/gapplication.1*
/usr/share/man/man1/gdbus.1*
/usr/share/man/man1/gio.1*
/usr/share/man/man1/glib-compile-resources.1*
/usr/share/man/man1/glib-compile-schemas.1*
/usr/share/man/man1/gsettings.1*
/usr/share/man/man3/glib*.3*
/usr/share/man/man3/gobject*.3*
/usr/share/man/man3/gio*.3*

%post
/sbin/ldconfig
glib-compile-schemas /usr/share/glib-2.0/schemas

%postun
/sbin/ldconfig
glib-compile-schemas /usr/share/glib-2.0/schemas

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of glib2.
