Name:           openbox-xdgmenu
Version:        0.1
Release:        1%{?dist}
Summary:        XDG menu generator for Openbox
License:        GPLv2+
URL:            https://github.com/trizen/openbox-xdgmenu
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3

%description
openbox-xdgmenu is a Python script that generates an XDG menu for the Openbox window manager.

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 openbox-xdgmenu.py %{buildroot}%{_bindir}/openbox-xdgmenu

%files
%{_bindir}/openbox-xdgmenu

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
