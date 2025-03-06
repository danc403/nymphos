Name:       m4
Version:    1.4.19
Release:    1%{?dist}
Summary:    GNU m4 macro processor

License:    GPLv3+
URL:        https://www.gnu.org/software/m4/
Source0:    m4-%{version}.tar.gz

%description
GNU m4 is an implementation of the traditional Unix macro processor. It
is mostly SVR4 compatible although it has some extensions.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/m4
%{_mandir}/man1/m4.1*
%{_infodir}/m4.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
