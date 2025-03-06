Name:       geany
Version:    2.0
Release:    1%{?dist}
Summary:    A fast and lightweight IDE

License:    GPLv2+
URL:        https://www.geany.org/
Source0:    geany-%{version}.tar.gz

BuildRequires:  gtk3-devel
BuildRequires:  scintilla-devel
BuildRequires:  vte3-devel

%description
Geany is a small and lightweight integrated development environment.
It was developed to provide a small and fast IDE, which has only a few
dependencies from other packages or desktop environments.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/geany
%{_datadir}/geany/
%{_mandir}/man1/geany.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
