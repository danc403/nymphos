Name:           nymph-disk-mounter
Version:        0.1  # Or your actual version
Release:        1%{?dist}
Summary:        A GTK3 application to mount and manage disks

License:        GPL-3.0-or-later
URL:            https://example.com/nymph-disk-mounter  # Replace with your project URL
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  gee-devel

Requires:       gtk3
Requires:       glib2
Requires:       udisks  # Or udisks2, depending on your system

%description
Nymph Disk Mounter is a GTK3 application that allows you to easily mount and manage disks.  It supports removable and optical media.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

#remove rpath
chrpath --delete %{buildroot}%{_bindir}/nymph-disk-mounter

%files
%{_bindir}/nymph-disk-mounter
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/glib-2.0/schemas/com.example.nymph-disk-mounter.gschema.xml

%post
gtk-update-icon-cache -q %{_datadir}/icons/hicolor

%postun
gtk-update-icon-cache -q %{_datadir}/icons/hicolor

%changelog
* Tue Oct 24 2024 Your Name <your.email@example.com> - 0.1.0-1
- Initial RPM release.
