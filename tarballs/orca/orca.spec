Name:       orca
Version:    47.3
Release:    1%{?dist}
Summary:    A screen reader for the visually impaired

License:    GPLv2+
URL:        https://wiki.gnome.org/Projects/Orca
Source0:    orca-%{version}.tar.gz

BuildRequires:  gtk4-devel
BuildRequires:  speech-dispatcher-devel
BuildRequires:  python3-devel
BuildRequires:  pkg-config

%description
Orca is a free, open source, flexible, and extensible screen reader that
provides access to the graphical desktop environment via speech and
braille.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/orca
%{_datadir}/orca/
%{_mandir}/man1/orca.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
