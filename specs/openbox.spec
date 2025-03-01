# specs/openbox/openbox-3.6.1.spec
Name:           openbox
Version:        3.6.1
Release:        1%{?dist}
Summary:        A highly configurable, next generation window manager.
License:        GPLv2+
URL:            http://openbox.org/
Source0:        openbox-3.6.1.tar.xz

BuildRequires:  libX11-devel, libXext-devel, libXrender-devel, libXft-devel, libxml2-devel, pango-devel, libstartup-notification-devel

%description
Openbox is a highly configurable, next generation window manager for the X Window System.

%prep
%setup -q

%build
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/openbox
%{_bindir}/openbox-menu
%{_bindir}/openbox-config-tools
%{_datadir}/openbox/
%{_mandir}/man1/openbox.1*
%{_mandir}/man1/openbox-menu.1*
%{_mandir}/man1/openbox-config-tools.1*

%changelog
* Fri Nov 24 2023 User <user@example.com> - 3.6.1-1
- Initial package.
