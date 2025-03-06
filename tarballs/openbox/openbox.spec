Name:       openbox
Version:    3.6.1
Release:    1%{?dist}
Summary:    A highly configurable, next generation window manager

License:    GPLv2+
URL:        http://openbox.org/
Source0:    openbox-%{version}.tar.xz

BuildRequires:  libxml2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXft-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel

%description
Openbox is a highly configurable, next generation window manager with
extensive standards support.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/openbox
%{_bindir}/openbox-menu
%{_bindir}/openbox-restart
%{_bindir}/openbox-reconfigure
%{_bindir}/openbox-client
%{_datadir}/openbox/
%{_mandir}/man1/openbox.1*
%{_mandir}/man1/openbox-menu.1*
%{_mandir}/man1/openbox-restart.1*
%{_mandir}/man1/openbox-reconfigure.1*
%{_mandir}/man1/openbox-client.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
