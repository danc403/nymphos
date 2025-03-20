Name:           nymph-apps
Version:        1.0
Release:        1%{?dist}
Summary:        A simple application launcher using the Nymph toolkit

License:        GPLv3+  ; # Or the specific license used for your project.
URL:            https://example.com/nymph-apps  ; # Replace with your project's URL if available

Source0:        nymph-apps-%{version}.tar.xz

BuildRequires:  vala
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libhandy-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)

Requires:       gtk3
Requires:       libhandy
Requires:       glib2

%description
This is a simple application launcher using the Nymph toolkit.

%prep
%autosetup

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 nymph-apps %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 nymph-apps.desktop %{buildroot}%{_datadir}/applications

# Install icons (if you have any)
# mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
# install -m 644 <icon_file.svg> %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/nymph-apps.svg

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/nymph-apps.desktop

%files
%{_bindir}/nymph-apps
%{_datadir}/applications/nymph-apps.desktop
# %{_datadir}/icons/hicolor/scalable/apps/nymph-apps.svg  # If you have icons

%changelog
* Wed Oct 25 2023 Your Name <your.email@example.com> - 1.0-1
- Initial package.
