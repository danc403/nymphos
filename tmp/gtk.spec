content: Name:           gtk
Version:        4.9.4
Release:        1%{?dist}
Summary:        GTK+ Graphical Toolkit Library (GTK), LGPL License

License:        LGPL-2.1-or-later
URL:            https://www.gtk.org/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  gobject-introspection-devel
BuildRequires:  glib2-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  at-spi2-core-devel
BuildRequires:  atk-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  wayland-devel
BuildRequires:  libepoxy-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  libinput-devel
BuildRequires:  libnotify-devel
BuildRequires:  libcolord-devel
BuildRequires:  cups-devel
BuildRequires:  graphene-devel
BuildRequires:  sassc
BuildRequires:  python3-devel
BuildRequires:  vala-devel

Requires:       glib2
Requires:       cairo
Requires:       pango
Requires:       gdk-pixbuf2
Requires:       at-spi2-core
Requires:       atk
Requires:       libxkbcommon
Requires:       wayland
Requires:       libepoxy
Requires:       mesa-libGL
Requires:       hicolor-icon-theme
Requires:       libnotify
Requires:       libcolord
Requires:       cups
Requires:       graphene

%description
The GTK+ toolkit is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application suites.

%prep
%autosetup

%build
./autogen.sh
%configure --enable-introspection=yes --enable-gtk-doc=no --disable-cloudproviders --disable-printbackends
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove libtool archives
find %{buildroot}%{_libdir} -name '*.la' -delete

%files
%{_bindir}/gtk4-demo
%{_bindir}/gtk4-builder-tool
%{_bindir}/gtk4-widget-factory
%{_libdir}/libgtk-4.so.*
%{_libdir}/gtk-4.0
%{_datadir}/gtk-4.0
%{_datadir}/applications/org.gtk.Demo4.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.enums.xml
%{_mandir}/man1/gtk4-demo.1*
%{_mandir}/man1/gtk4-builder-tool.1*
%{_mandir}/man1/gtk4-widget-factory.1*
%{_sharedstatedir}/gtk-4.0
%{_datadir}/metainfo/org.gtk.Demo4.appdata.xml
%{_datadir}/themes/*/*/*/*
%{_datadir}/themes/*/*/*/*/*
%license COPYING

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 4.9.4-1
- Initial build.

filename: gtk.spec
