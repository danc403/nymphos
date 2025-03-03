content: Name:           firefox-devel
Version:        136.0b9
Release:        1%{?dist}
Summary:        Development files for Firefox

License:        MPLv2.0
URL:            https://www.mozilla.org/en-US/firefox/

Source0:        %{name}-%{version}.en_US.tar.xz

BuildRequires:  pkgconfig(gtk3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  alsa-utils
BuildRequires:  zlib-devel
BuildRequires:  bzip2
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libffi-devel
BuildRequires:  openssl-devel

Requires:       firefox = %{version}-%{release}

%description
This package contains the development files for Firefox.

%prep
%autosetup -n %{name}-%{version}.en_US

%build

%install

%files

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 136.0b9-1
- Initial package build.

filename: firefox-devel.spec
