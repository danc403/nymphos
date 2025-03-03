spec: Name:           less
Version:        608
Release:        1%{?dist}
Summary:        A program similar to more (1) but which allows backward movement in the file - GPL License

License:        GPLv3
URL:            http://www.greenwoodsoftware.com/less/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel
BuildRequires:  groff

Requires:       ncurses
Requires:       bash

%description
less is a program similar to more (1), but which allows backward
movement in the file as well as forward movement.  Also, less does
not have to read the entire input file before starting, so with large
input files it starts up faster than text editors like vi.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/less
%{_bindir}/lessecho
%{_mandir}/man1/less.1*
%{_mandir}/man1/lessecho.1*
%{_datadir}/less/*
%{_infodir}/less.info*
%license LICENSE

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 608-1
- Initial package build.

