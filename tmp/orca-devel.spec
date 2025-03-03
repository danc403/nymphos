content: Name:           orca-devel
Version:        47.3
Release:        1%{?dist}
Summary:        Development files for orca - Accessibility

License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/Orca

Source0:        %{name:orca}-%{version}.tar.gz

BuildRequires:  gtk3-devel
BuildRequires:  speech-dispatcher-devel
BuildRequires:  python3-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libcanberra-devel

Requires:       orca = %{version}-%{release}

%description
This package contains the development files for orca.

%prep
%setup -q -n orca-%{version}

%build
%configure
%make_build

%install
%make_install

# Fix permissions
find %{buildroot} -type f -exec chmod 644 {} + 
find %{buildroot} -type d -exec chmod 755 {} + 

%files
%{_includedir}/orca
%{_libdir}/liborca-*.so
%{_libdir}/pkgconfig/orca.pc

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 47.3-1
- Initial package build.

filename: orca-devel.spec
