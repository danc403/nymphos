Name:       diffutils
Version:    3.9
Release:    1%{?dist}
Summary:    The GNU diff utilities

License:    GPLv3+
URL:        https://www.gnu.org/software/diffutils/
Source0:    %{name}-%{version}.tar.xz

%description
The GNU diff utilities compare files line by line, and output the
differences between them.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/cmp
%{_bindir}/diff
%{_bindir}/diff3
%{_bindir}/sdiff
%{_mandir}/man1/cmp.1*
%{_mandir}/man1/diff.1*
%{_mandir}/man1/diff3.1*
%{_mandir}/man1/sdiff.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
