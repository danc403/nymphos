Name:           caja
Version:        1.26.4
Release:        1%{?dist}
Summary:        Caja File Manager with Accessibility Enhancements
License:        GPLv2+
URL:            https://mate-desktop.org/
Source0:        caja-%{version}.tar.xz
BuildRequires:  gtk3-devel, libexif-devel, libnotify-devel, libjpeg-devel, libpng-devel, libxml2-devel, gdk-pixbuf2-devel, glib2-devel, libmount-devel, libuuid-devel, intltool, docbook-xsl-stylesheets, libmate-desktop-devel, libmate-panel-applet-devel, libgudev-devel, libsecret-devel
Requires:       gtk3, libexif, libnotify, libjpeg, libpng, libxml2, gdk-pixbuf2, glib2, libmount, libuuid, libmate-desktop, libmate-panel-applet, libgudev, libsecret
BuildArch:      x86_64 # or whatever arch you need. adjust as needed.
# Optional for remote mounts, if plugin is available
#BuildRequires:  gvfs-devel
#Requires:       gvfs

%description
Caja is the official file manager for the MATE Desktop Environment.
This package provides Caja with accessibility enhancements, focusing on
improving the experience for blind users.

%prep
%setup -q -n caja-%{version}

%build
%configure --disable-silent-rules --enable-accessibility --disable-selinux
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_bindir}/caja
%{_bindir}/caja-autorun-software
%{_bindir}/caja-connect-server
%{_bindir}/caja-desktop
%{_bindir}/caja-file-management-properties
%{_bindir}/caja-image-properties
%{_bindir}/caja-media-eject
%{_bindir}/caja-rename
%{_bindir}/caja-run-software
%{_bindir}/caja-scripts
%{_bindir}/caja-sendto
%{_datadir}/applications/caja.desktop
%{_datadir}/applications/caja-autorun-software.desktop
%{_datadir}/applications/caja-connect-server.desktop
%{_datadir}/applications/caja-file-management-properties.desktop
%{_datadir}/applications/caja-image-properties.desktop
%{_datadir}/applications/caja-media-eject.desktop
%{_datadir}/applications/caja-rename.desktop
%{_datadir}/applications/caja-run-software.desktop
%{_datadir}/applications/caja-scripts.desktop
%{_datadir}/applications/caja-sendto.desktop
%{_datadir}/icons/hicolor/*/apps/caja.png
%{_datadir}/mime/packages/caja.xml
%{_datadir}/caja/accels/caja.accels
%{_datadir}/caja/extensions/*.so
%{_datadir}/help/C/caja/
%{_mandir}/man1/caja.1*
%{_mandir}/man1/caja-autorun-software.1*
%{_mandir}/man1/caja-connect-server.1*
%{_mandir}/man1/caja-desktop.1*
%{_mandir}/man1/caja-file-management-properties.1*
%{_mandir}/man1/caja-image-properties.1*
%{_mandir}/man1/caja-media-eject.1*
%{_mandir}/man1/caja-rename.1*
%{_mandir}/man1/caja-run-software.1*
%{_mandir}/man1/caja-scripts.1*
%{_mandir}/man1/caja-sendto.1*
%{_datadir}/glib-2.0/schemas/org.mate.caja.gschema.xml
%{_libdir}/girepository-1.0/Caja-2.0.typelib
%{_datadir}/gir-1.0/Caja-2.0.gir

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package creation for Caja with accessibility focus.
- Disabled silent rules for verbose build output.
- Enabled accessibility options in configure.
- Included extension directory.
- Added schemas compilation.
- Added gir and typelib files.
