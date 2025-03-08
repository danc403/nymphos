Name:       lxappearance
Version:    0.6.3
Release:    1%{?dist}
Summary:    nymphOS theme switcher
License:    GPL-2.0-or-later
URL:        https://lxde.org/
Source0:    lxappearance-%{version}.tar.gz

BuildRequires:  gtk3-devel libfm-devel libxrandr-devel libxinerama-devel

%description
LXAppearance is the standard theme switcher of nymphOS. It allows you to change the look of GTK+ applications, icon themes, and fonts.

%prep
%autosetup -n lxappearance-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/lxappearance
%{_datadir}/applications/lxappearance.desktop
%{_datadir}/icons/hicolor/*/apps/lxappearance.png
%{_mandir}/man1/lxappearance.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
