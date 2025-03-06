Name:       findutils
Version:    4.9.0
Release:    1%{?dist}
Summary:    The GNU find utilities

License:    GPLv3+
URL:        https://www.gnu.org/software/findutils/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  gettext-devel

%description
The GNU find utilities consist of find, xargs, and locate.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/find
%{_bindir}/xargs
%{_bindir}/locate
%{_bindir}/updatedb
%{_mandir}/man1/find.1*
%{_mandir}/man1/xargs.1*
%{_mandir}/man1/locate.1*
%{_mandir}/man1/updatedb.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
