content: Name:           syslinux-devel
Version:        6.03
Release:        1%{?dist}
Summary:        Development files for Syslinux - GPLv2

License:        GPLv2
URL:            https://www.syslinux.org/

Source0:        %{name}.tar.xz

BuildRequires:  syslinux = %{version}

Requires:       syslinux = %{version}

%description
This package contains the development files for syslinux.

%prep
#%setup -q

%build
#make all

%install
#make install DESTDIR=%{buildroot}

# Remove unwanted files
#rm -rf %{buildroot}/usr/share/doc
#find %{buildroot} -name "*.txt" -delete

%files
#%{_includedir}/syslinux/*.h
#%{_libdir}/libsyslinux.a
#%{_libdir}/pkgconfig/syslinux.pc

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - %{version}-1
- Initial package build

filename: syslinux-devel.spec
