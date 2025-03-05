Name: glib2-devel
Version: 2.83.5
Release: 1%{?dist}
Summary: Development files for GLib
License: LGPL-2.1-or-later
URL: https://www.gtk.org/
Source0: glib2-2.83.5.tar.gz
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
  - glib2 = %{version}-%{release}

%description
Development files for GLib.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/include/glib-2.0/
/usr/lib/libglib-2.0.so
/usr/lib/libgobject-2.0.so
/usr/lib/libgmodule-2.0.so
/usr/lib/libgio-2.0.so
/usr/lib/pkgconfig/glib-2.0.pc
/usr/lib/pkgconfig/gobject-2.0.pc
/usr/lib/pkgconfig/gmodule-2.0.pc
/usr/lib/pkgconfig/gio-2.0.pc
/usr/lib/glib-2.0/include/

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of glib2-devel.
