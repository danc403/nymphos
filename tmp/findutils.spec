content: Name:           findutils
Version:        4.9.0
Release:        1%{?dist}
Summary:        GNU Find Utilities - Tools for finding files matching certain criteria
License:        GPLv3+
URL:            https://www.gnu.org/software/findutils/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gettext

Requires:       coreutils

%description
The GNU Find Utilities are the basic file locating utilities of the GNU
system.  These programs are typically used to find files matching
certain criteria, such as name, size, last access time, and so on.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove info dir entries, it is handled by texinfo package
rm -rf %{buildroot}/%{_infodir}

%files
%{_bindir}/find
%{_bindir}/locate
%{_bindir}/updatedb
%{_bindir}/xargs
%{_mandir}/man1/find.1*
%{_mandir}/man1/locate.1*
%{_mandir}/man1/updatedb.1*
%{_mandir}/man1/xargs.1*
%{_datadir}/locate
%{_datadir}/findutils
%{_sysconfdir}/updatedb.conf
%{_datadir}/gettext/its/findutils.its
%{_infodir}/find.info*
%{_infodir}/locate.info*
%{_infodir}/xargs.info*
%{_mandir}/man5/updatedb.conf.5*
%{_datadir}/aclocal/findutils.m4
%{_datadir}/doc/findutils

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 4.9.0-1
- Initial package build.

