Name:       bc
Version:    1.08.1
Release:    1%{?dist}
Summary:    An arbitrary precision calculator language

License:    GPLv3+
URL:        https://www.gnu.org/software/bc/
Source0:    bc-%{version}.tar.gz

%description
Bc is an arbitrary precision calculator language. Syntax is similar to C,
but differs in many substantial areas. It is particularly useful for
doing monetary calculations. Bc allows the definition of functions,
and can execute most instructions available in the POSIX bc language.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/bc
%{_bindir}/dc
%{_mandir}/man1/bc.1*
%{_mandir}/man1/dc.1*
%{_infodir}/bc.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
