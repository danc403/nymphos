Name:           lightdm-gtk-greeter
Version:        2.0.7
Release:        1%{?dist}
Summary:        GTK+ greeter for LightDM

License:        GPL-2.0-or-later
URL:            https://github.com/lightdm/lightdm-gtk-greeter
Source0:        lightdm-gtk-greeter-%{version}.tar.gz

BuildRequires:  gtk3-devel
BuildRequires:  liblightdm-gobject-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig

Requires:       lightdm
Requires:       gtk3
Requires:       nymph-accessibility

%description
lightdm-gtk-greeter is a GTK+ greeter for the LightDM display manager.

%prep
%setup -q -n lightdm-gtk-greeter-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/lightdm-gtk-greeter
%{_libdir}/lightdm/lightdm-gtk-greeter
%{_datadir}/lightdm/lightdm-gtk-greeter.conf
%{_datadir}/applications/lightdm-gtk-greeter.desktop
%{_datadir}/locale/*

%post
cat <<EOF > /etc/lightdm/lightdm-gtk-greeter.conf
[greeter]
background = /usr/share/backgrounds/default.png
reader = /usr/local/bin/orca-login-wrapper
a11y-states = +reader
EOF

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 2.0.7-1
- Initial build for custom distribution.
- Added nymph-accessibility dependency.
- Created lightdm-gtk-greeter.conf file in %post section.
