Name:       bison
Version:    3.8
Release:    1%{?dist}
Summary:    A general-purpose parser generator

License:    GPLv3+
URL:        https://www.gnu.org/software/bison/
Source0:    bison-%{version}.tar.xz

%description
Bison is a general-purpose parser generator that converts a grammar
specification into a deterministic finite-state automaton. Bison-generated
parsers are typically faster and smaller than hand-written parsers.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/bison
%{_bindir}/bisonc
%{_bindir}/bison-config
%{_infodir}/bison.info*
%{_mandir}/man1/bison.1*
%{_mandir}/man1/bisonc.1*
%{_mandir}/man1/bison-config.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
