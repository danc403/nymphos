Name:       texinfo
Version:    7.0
Release:    1%{?dist}
Summary:    Utilities for creating and reading Texinfo documents

License:    GPLv3+
URL:        https://www.gnu.org/software/texinfo/
Source0:    %{name}-%{version}.tar.xz

%description
Texinfo is a documentation system that uses a single source file to
produce both on-line information and printed output.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
