Name: feh
Version: 3.10.3
Release: %{?dist}
Summary: An image viewer aimed at command line users.
License: MIT
Source0: feh-3.10.3.tar.gz
URL: https://feh.finalrewind.org/
BuildRequires: imlib2-devel, libcurl-devel, libpng-devel, libX11-devel, libXt-devel
Requires: imlib2, libcurl, libpng, libX11, libXt

%description
feh is an image viewer aimed at command line users. It is capable of displaying
single images or multiple images in a slideshow. It does not have a fancy
graphical user interface, but is fast and light.

%prep
%setup -q -n feh-1.0

%build
make curl=1 xinerama=1 app=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license COPYING
%{_bindir}/feh
%{_mandir}/man1/feh.1*
%{_datadir}/applications/feh.desktop
%{_datadir}/icons/hicolor/16x16/apps/feh.png
%{_datadir}/icons/hicolor/32x32/apps/feh.png
%{_datadir}/icons/hicolor/48x48/apps/feh.png
%{_datadir}/icons/hicolor/scalable/apps/feh.svg

%changelog
* %{date -u +%Y-%m-%d} Dan Carpenter <danc403@gmail.com> - 1.0-1
- Initial build for NymphOS.
