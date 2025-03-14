Name: nymph-wallpaper-switcher
Version: 1.0
Release: 1%{?dist}
Summary: A simple wallpaper switcher for NymphOS
License: GPLv3
Source0: nymph-wallpaper-switcher-1.0.tar.xz

BuildRequires: vala gtk3-devel gettext

Requires: feh

%description
A simple wallpaper switcher for NymphOS.

%prep
%setup -q -n nymph-wallpaper-switcher-1.0

%build
valac --pkg gtk-3.0 nymph-wallpaper-switcher.vala

%install
rm -rf %{buildroot}

install -Dm 755 nymph-wallpaper-switcher %{buildroot}%{_bindir}/%{name}
install -Dm 644 nymph-wallpaper-switcher.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install system-wide default configuration files (if needed)
install -Dm 755 -d %{buildroot}%{_sysconfdir}/nymph-wallpaper-switcher
install -Dm 644 config %{buildroot}%{_sysconfdir}/nymph-wallpaper-switcher/config
install -Dm 755 autostart.sh %{buildroot}%{_sysconfdir}/nymph-wallpaper-switcher/autostart.sh

# Install .mo files
mkdir -p %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES
install -m 644 po/fr.mo %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo

mkdir -p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES
install -m 644 po/de.mo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo

mkdir -p %{buildroot}%{_datadir}/locale/es/LC_MESSAGES
install -m 644 po/es.mo %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/%{name}.mo

mkdir -p %{buildroot}%{_datadir}/locale/ja/LC_MESSAGES
install -m 644 po/ja.mo %{buildroot}%{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_sysconfdir}/nymph-wallpaper-switcher/config
%{_sysconfdir}/nymph-wallpaper-switcher/autostart.sh
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/es/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo

%changelog
* Mon Oct 23 2023 Dan Carpenter <danc403@gmail.com> - 1.0-1
- Initial release.
