Name:       lightdm
Version:    1.32.0
Release:    1%{?dist}
Summary:    A display manager

License:    GPLv2+
URL:        https://github.com/canonical/lightdm
Source0:    lightdm-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  libxcb-devel
BuildRequires:  libx11-devel
BuildRequires:  libxau-devel
BuildRequires:  libxdmcp-devel
BuildRequires:  libpam-devel
BuildRequires:  libgobject-2.0-devel
BuildRequires:  libgee-devel
BuildRequires:  libaccountsservice-devel
BuildRequires:  accountsservice
BuildRequires:  libgcrypt-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  consolekit2-devel

%description
LightDM is a cross-desktop display manager. Its aim is to be light, fast,
extensible and multi-desktop.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc --disable-systemd --enable-consolekit
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/lightdm
%{_libdir}/lightdm/
%{_mandir}/man1/lightdm.1*
/etc/lightdm/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
