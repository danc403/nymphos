Name:           thunar
Version:        4.20.2
Release:        1%{?dist}
Summary:        Thunar File Manager with Accessibility Enhancements
License:        GPLv2+
URL:            https://docs.xfce.org/xfce/thunar/start
Source0:        thunar-%{version}.tar.bz2
BuildRequires:  gtk3-devel, libexif-devel, libnotify-devel, libjpeg-devel, libpng-devel, libxml2-devel, gdk-pixbuf2-devel, glib2-devel, libmount-devel, libuuid-devel, intltool, docbook-xsl-stylesheets, libxfce4ui-devel, libxfce4util-devel, exo-devel, libwnck3-devel, libgudev-devel
Requires:       gtk3, libexif, libnotify, libjpeg, libpng, libxml2, gdk-pixbuf2, glib2, libmount, libuuid, libxfce4ui, libxfce4util, exo, libwnck3, libgudev
BuildArch:      x86_64 # or whatever arch you need. adjust as needed.
# Optional for remote mounts, if plugin is available
#BuildRequires:  gvfs-devel
#Requires:       gvfs

%description
Thunar is a modern file manager for the XFCE Desktop Environment.
This package provides Thunar with accessibility enhancements, focusing on
improving the experience for blind users.

%prep
%setup -q -n thunar-%{version}

%build
%configure --disable-silent-rules
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_bindir}/thunar
%{_bindir}/thunar-volman
%{_datadir}/applications/Thunar.desktop
%{_datadir}/applications/Thunar-Settings.desktop
%{_datadir}/icons/hicolor/*/apps/Thunar.png
%{_datadir}/icons/hicolor/*/apps/Thunar-Settings.png
%{_datadir}/mime/packages/thunar.xml
%{_datadir}/thunar/accels/thunar.accels
%{_datadir}/thunar/plugins/*.so
%{_datadir}/help/C/thunar/
%{_mandir}/man1/thunar.1*
%{_mandir}/man1/thunar-volman.1*
%{_datadir}/glib-2.0/schemas/org.xfce.thunar.gschema.xml
%{_libdir}/girepository-1.0/ThunarX-1.0.typelib
%{_datadir}/gir-1.0/ThunarX-1.0.gir

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package creation for Thunar with accessibility focus.
- Disabled silent rules for verbose build output.
- Included plugin directory.
- Added schemas compilation.
- Added gir and typelib files.
