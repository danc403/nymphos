Name:       obconf
Version:    2.0.3
Release:    1%{?dist}
Summary:    Openbox configuration tool
License:    GPL-2.0-or-later
URL:        http://openbox.org/
Source0:    obconf-%{version}.tar.gz

BuildRequires:  gtk2-devel libxml2-devel

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%prep
%autosetup -n obconf-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/obconf
%{_datadir}/applications/obconf.desktop
%{_datadir}/icons/hicolor/*/apps/obconf.png
%{_mandir}/man1/obconf.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
