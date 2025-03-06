Name:       libtool
Version:    2.4.7
Release:    1%{?dist}
Summary:    A generic library support script

License:    GPLv2+
URL:        https://www.gnu.org/software/libtool/
Source0:    libtool-%{version}.tar.xz

%description
GNU libtool is a generic library support script. Libtool hides the
complexity of using shared libraries across different operating systems.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/libtool
%{_bindir}/libtoolize
%{_mandir}/man1/libtool.1*
%{_mandir}/man1/libtoolize.1*
%{_infodir}/libtool.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
