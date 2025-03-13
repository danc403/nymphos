Name:           nymph-theme-switcher
Version:        1.0
Release:        1%{?dist}
Summary:        A graphical tool to switch Openbox themes.
License:        GPLv3
URL:            https://example.com/nymph-theme-switcher  # Replace with your project URL
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  valac, gtk3-devel, openbox, gettext-devel
Requires:       gtk3, openbox

%description
Nymph Theme Switcher is a graphical tool to easily change Openbox themes.
It allows users to switch themes and administrators to apply them system-wide.

%prep
%setup -q

%build
valac nymph_theme_switcher.vala --pkg gtk+-3.0

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 nymph_theme_switcher %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 nymph-theme-switcher.desktop %{buildroot}%{_datadir}/applications

mkdir -p %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/
install -m 644 po/es.mo %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/nymph-theme-switcher.mo

mkdir -p %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/
install -m 644 po/fr.mo %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/nymph-theme-switcher.mo

mkdir -p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/
install -m 644 po/de.mo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/nymph-theme-switcher.mo

mkdir -p %{buildroot}%{_datadir}/locale/ja/LC_MESSAGES/
install -m 644 po/ja.mo %{buildroot}%{_datadir}/locale/ja/LC_MESSAGES/nymph-theme-switcher.mo

mkdir -p %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/
install -m 644 po/zh_CN.mo %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/nymph-theme-switcher.mo

mkdir -p %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES/
install -m 644 po/ru.mo %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES/nymph-theme-switcher.mo

mkdir -p %{buildroot}%{_datadir}/locale/pt/LC_MESSAGES/
install -m 644 po/pt.mo %{buildroot}%{_datadir}/locale/pt/LC_MESSAGES/nymph-theme-switcher.mo

mkdir -p %{buildroot}%{_datadir}/locale/it/LC_MESSAGES/
install -m 644 po/it.mo %{buildroot}%{_datadir}/locale/it/LC_MESSAGES/nymph-theme-switcher.mo

mkdir -p %{buildroot}%{_datadir}/doc/%{name}
install -m 644 README.md %{buildroot}%{_datadir}/doc/%{name}

%files
%{_bindir}/nymph_theme_switcher
%{_datadir}/applications/nymph-theme-switcher.desktop
%{_datadir}/locale/*/LC_MESSAGES/nymph-theme-switcher.mo
%{_datadir}/doc/%{name}/README.md

%changelog
* Mon Jun 25 2024 Dan Carpenter <danc403@gmail.com> - 1.0-1
- Initial package.
