# specs/gtk/gtk-4.9.4.spec
Name:           gtk
Version:        4.9.4
Release:        1%{?dist}
Summary:        The GTK+ toolkit.
License:        LGPLv2+
URL:            https://www.gtk.org/
Source0:        gtk-4.9.4.tar.xz

BuildRequires:  meson, ninja-build, pkgconfig, glib2-devel, pango-devel, cairo-devel, libxkbcommon-devel, libXi-devel, libXrandr-devel, libepoxy-devel, libjpeg-turbo-devel, libtiff-devel, libpng-devel, gdk-pixbuf2-devel, wayland-devel, libdrm-devel, vulkan-headers, vulkan-validationlayers

%description
The GTK+ toolkit is a multi-platform toolkit for creating graphical user interfaces.

%prep
%setup -q

%build
meson build --prefix=%{_prefix} --buildtype=release
ninja -C build

%install
ninja -C build install DESTDIR=%{buildroot}

%files
%{_libdir}/libgtk-4.so.*
%{_libdir}/girepository-1.0/
%{_libdir}/gtk-4.0/
%{_includedir}/gtk-4.0/
%{_datadir}/gtk-4.0/
%{_bindir}/gtk4-demo
%{_bindir}/gtk4-builder-tool
%{_bindir}/gtk4-print-editor
%{_mandir}/man1/gtk4-demo.1*
%{_mandir}/man1/gtk4-builder-tool.1*
%{_mandir}/man1/gtk4-print-editor.1*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 4.9.4-1
- Initial package.
