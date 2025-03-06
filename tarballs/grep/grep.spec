Name:       grep
Version:    3.9
Release:    1%{?dist}
Summary:    The GNU grep utilities

License:    GPLv3+
URL:        https://www.gnu.org/software/grep/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  pcre2-devel

%description
The GNU grep utilities search one or more input files for lines containing a
match to a specified pattern.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/grep
%{_bindir}/egrep
%{_bindir}/fgrep
%{_mandir}/man1/grep.1*
%{_mandir}/man1/egrep.1*
%{_mandir}/man1/fgrep.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
