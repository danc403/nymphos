content: Name:           orca
Version:        47.3
Release:        1%{?dist}
Summary:        A free, open source, flexible, extensible screen reader - Accessibility

License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/Orca

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gtk3-devel
BuildRequires:  speech-dispatcher-devel
BuildRequires:  python3-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libcanberra-devel

Requires:       gtk3
Requires:       speech-dispatcher
Requires:       python3
Requires:       alsa-lib
Requires:       libcanberra

%description
Orca is a free, open source, flexible, and extensible screen reader.
It uses Speech Dispatcher for speech and supports multiple synthesizers.
Orca works with applications implementing the Assistive Technology Service Provider Interface (AT-SPI).

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

# Fix permissions
find %{buildroot} -type f -exec chmod 644 {} + 
find %{buildroot} -type d -exec chmod 755 {} + 

%files
%license COPYING
%{_bindir}/orca
%{_datadir}/orca
%{_datadir}/applications/org.gnome.Orca.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.orca.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Orca.png
%{_datadir}/metainfo/org.gnome.Orca.appdata.xml
%{_datadir}/sounds/orca
%{_mandir}/man1/orca.1.*

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 47.3-1
- Initial package build.

filename: orca.spec
