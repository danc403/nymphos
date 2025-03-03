content: Name:           findutils-devel
Version:        4.9.0
Release:        1%{?dist}
Summary:        Development files for findutils

License:        GPLv3+
URL:            https://www.gnu.org/software/findutils/

Source0:        %{name}-%{version}.tar.xz

Requires:       findutils = %{version}-%{release}

%description
This package contains the development files for findutils.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove info dir entries, it is handled by texinfo package
rm -rf %{buildroot}/%{_infodir}

rm -rf %{buildroot}/%{_includedir}
rm -rf %{buildroot}/%{_libdir}
rm -rf %{buildroot}/%{_datadir}/aclocal

%files
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/findutils.m4

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 4.9.0-1
- Initial package build.

