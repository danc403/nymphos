Name:       firefox
Version:    136.0b9
Release:    1%{?dist}
Summary:    Mozilla Firefox Web Browser
License:    MPL-2.0
URL:        https://www.mozilla.org/firefox/
Source0:    %{name}-%{version}.en_US.tar.xz

BuildRequires:  gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libasound2-devel
BuildRequires:  libpulse-devel
BuildRequires:  libvpx-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libwebp-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  fontconfig-devel
BuildRequires:  nss-devel
BuildRequires:  nspr-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  libstdc++-devel

%description
Mozilla Firefox is a fast, full-featured Web browser. Firefox includes
pop-up blocking, tab-browsing, integrated search, improved privacy
features, automatic updating and more.

%prep
%setup -q -n firefox

%build
# Firefox is a pre-built binary package, no build step required

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 755 firefox %{buildroot}%{_bindir}/firefox
install -m 644 firefox.desktop %{buildroot}%{_datadir}/applications/firefox.desktop
install -m 644 browser/chrome/icons/default/default256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/firefox.png

%files
%{_bindir}/firefox
%{_datadir}/applications/firefox.desktop
%{_datadir}/icons/hicolor/256x256/apps/firefox.png
%license LICENSE

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 136.0b9-1
- Initial build for x86_64 and OpenRC.
