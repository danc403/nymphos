Name:           WhiteSur-theme
Version:        20231027 # Replace with the actual release date or version
Release:        1%{?dist}
Summary:        WhiteSur GTK, icon, and cursor themes

License:        GPL-3.0-or-later
Source0:        WhiteSur-gtk-theme-%{version}.tar.gz
Source1:        WhiteSur-icon-theme-%{version}.tar.gz
Source2:        WhiteSur-cursor-theme-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides the WhiteSur GTK, icon, and cursor themes,
offering a modern and consistent look for your desktop.

%install
# GTK Themes
tar -xzf %{SOURCE0} -C %{buildroot}/usr/share/themes/
# Icon Themes
tar -xzf %{SOURCE1} -C %{buildroot}/usr/share/icons/
# Cursor Themes
tar -xzf %{SOURCE2} -C %{buildroot}/usr/share/icons/

%files
/usr/share/themes/WhiteSur-dark/
/usr/share/themes/WhiteSur-light/
/usr/share/icons/WhiteSur-icons/
/usr/share/icons/WhiteSur-cursors/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-1
- Initial package creation.
