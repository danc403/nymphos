Name:       perl
Version:    5.40.1
Release:    1%{?dist}
Summary:    Practical Extraction and Report Language

License:    GPLv1+ or Artistic
URL:        https://www.perl.org/
Source0:    perl-%{version}.tar.gz

%description
Perl is a highly capable, feature-rich programming language with over
30 years of development. Perl runs on over 100 platforms from portables
to mainframes and is suitable for both rapid prototyping and large
scale development projects.

%prep
%setup -q -n perl-%{version}

%build
sh Configure -des -Dprefix=%{_prefix} -Dvendorprefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/a2p
%{_bindir}/c2ph
%{_bindir}/config_data
%{_bindir}/perl
%{_bindir}/perl5.40.1
%{_bindir}/perldoc
%{_bindir}/perlivp
%{_libdir}/perl5/
%{_mandir}/man1/a2p.1*
%{_mandir}/man1/c2ph.1*
%{_mandir}/man1/perl.1*
%{_mandir}/man1/perldoc.1*
%{_mandir}/man1/perlivp.1*
%{_mandir}/man3/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
