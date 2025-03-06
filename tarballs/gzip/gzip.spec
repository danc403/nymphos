Name:       gzip
Version:    1.12
Release:    1%{?dist}
Summary:    The GNU compression utility

License:    GPLv3+
URL:        https://www.gnu.org/software/gzip/
Source0:    %{name}-%{version}.tar.xz

%description
Gzip reduces the size of the named files using Lempel-Ziv coding (LZ77).

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/gzip
%{_bindir}/gunzip
%{_bindir}/zcat
%{_mandir}/man1/gzip.1*
%{_mandir}/man1/gunzip.1*
%{_mandir}/man1/zcat.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
