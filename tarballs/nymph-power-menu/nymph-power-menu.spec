Name:           nymph-power-menu
Version:        1.0
Release:        1%{?dist}
Summary:        A simple power menu for NymphOS.
License:        GPLv3+
URL:            https://github.com/your-repo/nymph-power-menu  # Replace with your repository URL
Source0:        nymph-power-menu-1.0.tar.xz
BuildRequires:  vala, gtk3-devel, gettext
Requires:       gtk3, glibc, sudo

%description
Nymph Power Menu is a simple GTK+ 3 application for NymphOS that provides options to log out, shut down, and reboot the system.

%prep
%setup -q

%build
valac --pkg gtk+-3.0 nymph-power-menu.vala

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 nymph-power-menu %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 nymph-power-menu.desktop %{buildroot}%{_datadir}/applications

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
%{_bindir}/nymph-power-menu
%{_datadir}/applications/nymph-power-menu.desktop
%{_datadir}/doc/%{name}/README.md
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/es/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo

%changelog
* Mon Jun 25 2024 Dan Carpenter <danc403@gmail.com> - 1.0-1
- Initial package.
