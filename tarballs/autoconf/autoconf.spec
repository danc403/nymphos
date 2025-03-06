Name:       autoconf
Version:    2.71
Release:    1%{?dist}
Summary:    A tool for automatically configuring source code

License:    GPLv3+
URL:        https://www.gnu.org/software/autoconf/
Source0:    autoconf-%{version}.tar.gz

BuildRequires: m4 >= 1.4.19

%description
Autoconf is a tool for producing shell scripts that automatically configure
software source code packages to adapt to many kinds of UNIX-like systems.
Autoconf creates a configuration script from a template file that lists
the operating system features that the package can use, in the form of
m4 macro calls.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/autoconf
%{_bindir}/autoheader
%{_bindir}/autom4te
%{_bindir}/autoreconf
%{_bindir}/autoscan
%{_datadir}/autoconf/
%{_mandir}/man1/autoconf.1*
%{_mandir}/man1/autoheader.1*
%{_mandir}/man1/autom4te.1*
%{_mandir}/man1/autoreconf.1*
%{_mandir}/man1/autoscan.1*
%{_infodir}/autoconf.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
