content: Name:           firefox
Version:        136.0b9
Release:        1%{?dist}
Summary:        Mozilla Firefox Web Browser (en_US) - MPLv2.0

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
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Requires:       gtk3
Requires:       alsa-utils
Requires:       zlib
Requires:       bzip2
Requires:       libcap
Requires:       libseccomp
Requires:       libffi
Requires:       openssl

%description
Mozilla Firefox is a standalone web browser from Mozilla.

%prep
%autosetup -n %{name}-%{version}.en_US

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove the .desktop file as we don't want it
rm -f %{buildroot}%{_datadir}/applications/firefox.desktop

%files
%{_bindir}/firefox
%{_libdir}/firefox
%{_datadir}/applications/firefox.desktop
%{_datadir}/icons/hicolor/*/apps/firefox.png
%{_datadir}/pixmaps/firefox.png
%{_datadir}/mozilla/%{name}
%{_sharedstatedir}/mozilla/%{name}
%license LICENSE
%{_mandir}/man1/firefox.1*
%doc README.mozilla

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 136.0b9-1
- Initial package build.

filename: firefox.spec
