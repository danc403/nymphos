spec_content: Name:           openrc-devel
Version:        0.56
Release:        1%{?dist}
Summary:        Development files for OpenRC

License:        MIT
URL:            https://github.com/OpenRC/openrc

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  sed
BuildRequires:  pkg-config
Requires: openrc = %{version}-%{release}


%description
This package contains the header files and static libraries for
developing applications that use OpenRC.


%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove unneeded files
rm -f %{buildroot}/etc/init.d/functions

# Ensure proper permissions
chmod +x %{buildroot}/usr/bin/rc

#Install include files and libraries
mkdir -p %{buildroot}/%{_includedir}
cp -r librc/rc.h %{buildroot}/%{_includedir}/

%files
%{_includedir}/rc.h

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 0.56-1
- Initial package build.

