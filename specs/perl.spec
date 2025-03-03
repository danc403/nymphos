# specs/perl/perl-5.40.1.spec
Name:           perl
Version:        5.40.1
Release:        1%{?dist}
Summary:        Practical Extraction and Report Language
License:        GPLv1+ or Artistic
URL:            https://www.perl.org/
Source0:        perl-5.40.1.tar.gz

BuildRequires:  gdbm-devel, openssl-devel, zlib-devel, bzip2-devel, db4-devel, readline-devel, ncurses-devel, libxcrypt-devel

Requires:       gdbm, openssl, zlib, bzip2, db4, readline, ncurses, libxcrypt

%description
Perl is a highly capable, feature-rich programming language with over
25 years of development.

%prep
%setup -q

%build
sh Configure -des -Dprefix=%{_prefix} -Dvendorprefix=%{_prefix} -Dsiteprefix=%{_prefix} -Duseshrplib -Doptimize="%{optflags}" -Dccflags="%{optflags} -D_GNU_SOURCE -fwrapv" -Dlocincpth="%{_includedir}" -Dloclibpth="%{_libdir}"
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/a2p
%{_bindir}/c2ph
%{_bindir}/dprofpp
%{_bindir}/enc2xs
%{_bindir}/find2perl
%{_bindir}/h2ph
%{_bindir}/h2xs
%{_bindir}/instmodsh
%{_bindir}/json_pp
%{_bindir}/perl
%{_bindir}/perl5.40.1
%{_bindir}/perlbug
%{_bindir}/perldoc
%{_bindir}/perlivp
%{_bindir}/piconv
%{_bindir}/pl2pm
%{_bindir}/pod2html
%{_bindir}/pod2man
%{_bindir}/pod2text
%{_bindir}/pod2usage
%{_bindir}/prove
%{_libdir}/perl5/
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 5.40.1-1
- Initial package.
