Name:       brasero
Version:    3.12.3
Release:    1%{?dist}
Summary:    A CD/DVD burning application for the GNOME desktop
License:    GPL-2.0-or-later
URL:        https://wiki.gnome.org/Apps/Brasero
Source0:    brasero-%{version}.tar.xz

BuildRequires:  gtk3-devel libcanberra-devel libnotify-devel libsoup-devel gstreamer1-devel gstreamer1-plugins-base-devel libburn-devel libisofs-devel iso-codes-devel gnome-common intltool

%description
Brasero is a simple application to burn CD/DVD media. It is designed to be as simple as possible and has some unique features to enable users to create their discs easily and quickly.

%prep
%autosetup -n brasero-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/brasero
%{_datadir}/applications/org.gnome.Brasero.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.brasero.gschema.xml
%{_datadir}/icons/hicolor/*/apps/brasero.png
%{_datadir}/metainfo/org.gnome.Brasero.appdata.xml
%{_datadir}/brasero/
%{_mandir}/man1/brasero.1*
%{_libdir}/brasero/

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
