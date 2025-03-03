content: Name:           automake
Version:        1.16.5
Release:        1%{?dist}
Summary:        A tool for automatically generating Makefiles
License:        GPLv2+
URL:            https://www.gnu.org/software/automake/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  perl

Requires:       autoconf

%description
Automake is a tool for automatically generating Makefiles from
template files. It is part of the GNU build system.


%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/automake
%{_bindir}/aclocal
%{_datadir}/automake-%{version}
%{_infodir}/automake.info*
%{_mandir}/man1/automake.1*
%{_mandir}/man1/aclocal.1*
%{_datadir}/aclocal
%{_datadir}/aclocal/obsolete
%{_datadir}/aclocal/dirlist
%{_datadir}/aclocal/index.cache

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 1.16.5-1
- Initial package build

filename: automake.spec
