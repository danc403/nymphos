Name:           firefox
Version:        136.0
Release:        1%{?dist}
Summary:        Mozilla Firefox web browser

License:        MPLv2.0
URL:            https://www.mozilla.org/firefox/
Source1:        firefox.desktop
Source2:        firefox-256.png
Source3:        firefox-wrapper.sh

%define extension tar.xz

Requires:       gtk3, libX11, libasound2, libpulse, libdbus-glib-1, libstdc++, libexpat, libffi, libzstd, libevent, libvpx, libopus, libogg, libvorbis, libjpeg-turbo, libpng, libwebp, nss, nspr, fontconfig, freetype, glibc

%description
Mozilla Firefox is a free and open-source web browser developed by
the Mozilla Foundation and its subsidiary, the Mozilla Corporation.

%install
mkdir -p %{buildroot}/%{_prefix}/lib
for locale_dir in locale/*; do
    locale=$(basename "$locale_dir")
    tar -xJf "$locale_dir/%{name}-%{version}.%{extension}" -C %{buildroot}/%{_prefix}/lib
    mv %{buildroot}/%{_prefix}/lib/firefox %{buildroot}/%{_prefix}/lib/firefox-$locale
done

mkdir -p %{buildroot}%{_datadir}/applications/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

mkdir -p %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/

%files
%{_prefix}/lib/firefox-*
%{_datadir}/applications/firefox.desktop
%{_datadir}/icons/hicolor/256x256/apps/firefox-256.png
%{_bindir}/firefox-wrapper.sh

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Corrected spec file with dependencies and desktop integration.
- Added desktop file and icon.
- Added support for multiple language archives.
- Used standard macros for tarball name.
- Resized icon to 256x256 pixels.
- Added wrapper script.
