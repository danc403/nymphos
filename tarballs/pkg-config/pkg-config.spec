Name:       pkg-config
Version:    0.29.2
Release:    1%{?dist}
Summary:    Manage compile and link flags for libraries

License:    GPLv2+
URL:        https://www.freedesktop.org/wiki/Software/pkg-config/
Source0:    pkg-config-%{version}.tar.gz

%description
pkg-config is a helper tool used to retrieve information about installed
libraries in the system. It is typically used to extract compilation
and linking flags from installed libraries.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/pkg-config
%{_mandir}/man1/pkg-config.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
