Name:       gawk
Version:    5.2.1
Release:    1%{?dist}
Summary:    GNU awk - pattern scanning and text processing language

License:    GPLv3+
URL:        https://www.gnu.org/software/gawk/
Source0:    gawk-%{version}.tar.xz

%description
GNU Awk is a pattern scanning and text processing language. 
Originally developed as an extension to the AWK scripting language 
developed by Aho, Weinberger, and Kernighan, GNU Awk is now the 
de facto standard for AWK interpreters.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/gawk
%{_mandir}/man1/gawk.1*
%{_infodir}/gawk.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
