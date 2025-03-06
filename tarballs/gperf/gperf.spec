Name:       gperf
Version:    3.1
Release:    1%{?dist}
Summary:    Perfect hash function generator

License:    GPLv3+
URL:        https://www.gnu.org/software/gperf/
Source0:    gperf-%{version}.tar.gz

%description
Gperf is a perfect hash function generator. It reads a set of keywords from
a file, and produces C or C++ code for a perfect hash function.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
