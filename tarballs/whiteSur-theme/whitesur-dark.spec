Name: whitesur-dark
Version: 0.1
Release: 1%{?dist}
Summary: A macOS like dark theme for various desktop environments
License: GPL-3.0-or-later
URL: https://github.com/vinceliuice/WhiteSur-gtk-theme
Source0: whitesur-dark.tar.xz

BuildArch: noarch

%description
This package provides the Whitesur dark theme for various desktop environments, 
including Cinnamon, GTK, Metacity, Unity, Xfwm4, and Openbox.

%prep
%autosetup -p1 -c -a -S

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/themes/Whitesur-dark
cp -r cinnamon gtk gtk-2.0 gtk-3.0 gtk-4.0 metacity unity xfwm4 openbox %{buildroot}%{_datadir}/themes/Whitesur-dark/

%files
%license COPYING
%{_datadir}/themes/Whitesur-dark/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 0.1-1
- Initial package.
