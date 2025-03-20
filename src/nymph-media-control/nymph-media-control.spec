Name:           media-control
Version:        0.1
Release:        1%{?dist}
Summary:        A simple media control application

License:        MIT  # Or your chosen license (e.g., GPLv3)
URL:            https://example.com/media-control  # Replace with your project URL
Source0:        %{name}-%{version}.tar.gz  # Source tarball

BuildRequires:  vala >= 0.46
BuildRequires:  gtk3-devel >= 3.0
BuildRequires:  libpulse-devel >= 14.0
BuildRequires:  meson
BuildRequires:  ninja

Requires:       gtk3 >= 3.0
Requires:       libpulse >= 14.0

%description
A simple media control application written in Vala.

%prep
%autosetup -n %{name}-%{version}

%build
meson setup builddir
meson compile -C builddir

%install
meson install -C builddir --destdir=%{buildroot}

%files
%{_bindir}/media-control
%{_datadir}/applications/media-control.desktop #if you have a desktop file
%{_datadir}/icons/hicolor/scalable/apps/media-control.png #If you have icons

%changelog
* Mon Oct 23 2023 Your Name <your.email@example.com> - 0.1-1
- Initial package.
