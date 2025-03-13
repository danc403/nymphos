Name:           nymph-wallpaper-switcher
Version:        1.0
Release:        1%{?dist}
Summary:        A simple wallpaper switcher for NymphOS.
License:        GPLv3+
URL:            https://github.com/your-repo/nymph-wallpaper-switcher  # Replace with your repository URL
Source0:        nymph-wallpaper-switcher-1.0.tar.xz
BuildRequires:  vala, gtk3-devel, gettext
Requires:       gtk3, glibc

%description
Nymph Wallpaper Switcher is a simple GTK+ 3 application for NymphOS that allows users to easily change their desktop wallpaper.

%prep
%setup -q

%build
valac --pkg gtk+-3.0 nymph-wallpaper-switcher.vala

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 nymph-wallpaper-switcher %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 nymph-wallpaper-switcher.desktop %{buildroot}%{_datadir}/applications

mkdir -p %{buildroot}%{_datadir}/doc/%{name}
install -m 644 README.md %{buildroot}%{_datadir}/doc/%{name}

mkdir -p %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES
install -m 644 po/fr.mo %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo

mkdir -p %{buildroot}%{_datadir}/locale/es/LC_MESSAGES
install -m 644 po/es.mo %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/%{name}.mo

mkdir -p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES
install -m 644 po/de.mo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo

mkdir -p %{buildroot}%{_datadir}/locale/ja/LC_MESSAGES
install -m 644 po/ja.mo %{buildroot}%{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo

%files
%{_bindir}/nymph-wallpaper-switcher
%{_datadir}/applications/nymph-wallpaper-switcher.desktop
%{_datadir}/doc/%{name}/README.md
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/es/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo

%changelog
* Mon Jun 25 2024 Dan Carpenter <danc403@gmail.com> - 1.0-1
- Initial package.
