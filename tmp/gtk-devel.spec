content: Name:           gtk-devel
Version:        4.9.4
Release:        1%{?dist}
Summary:        Development files for GTK+ Graphical Toolkit Library

License:        LGPL-2.1-or-later
URL:            https://www.gtk.org/

Source0:        gtk-%{version}.tar.xz

BuildRequires:  pkg-config
Requires:       gtk = %{version}-%{release}

%description
This package contains the development files for the GTK+ toolkit.

%prep
%autosetup -n gtk-%{version}

%build

%install

%files
%{_includedir}/gtk-4.0
%{_libdir}/libgtk-4.so
%{_libdir}/pkgconfig/gtk4.pc
%{_datadir}/gir-1.0/Gtk-4.0.gir
%{_libdir}/girepository-1.0/Gtk-4.0.typelib

filename: gtk-devel.spec
