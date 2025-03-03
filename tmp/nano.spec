spec_content: Name:           nano
Version:        6.4
Release:        1%{?dist}
Summary:        Small, easy to use editor - License: GPLv3+

License:        GPLv3+
URL:            https://www.nano-editor.org/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  ncurses-devel
BuildRequires:  gettext
Requires:       ncurses

%description
GNU nano is a small, easy to use editor for Linux.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/nano
%{_mandir}/man1/nano.1.*
%{_datadir}/nano/

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 6.4-1
- Initial package build
package_name: nano
