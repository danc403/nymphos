Name:       automake
Version:    1.16.5
Release:    1%{?dist}
Summary:    A tool for automatically generating Makefiles

License:    GPLv2+
URL:        https://www.gnu.org/software/automake/
Source0:    automake-%{version}.tar.gz

BuildRequires: autoconf >= 2.69
BuildRequires: m4 >= 1.4

%description
Automake is a tool for automatically generating `Makefile.in' files from
`configure.ac'.  These `Makefile.in' files are then used by `configure'
to create `Makefile' files.  Automake requires the use of GNU Autoconf.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/aclocal
%{_bindir}/automake
%{_datadir}/automake-*/
%{_mandir}/man1/aclocal.1*
%{_mandir}/man1/automake.1*
%{_infodir}/automake.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
