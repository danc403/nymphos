Name:       tar
Version:    1.34
Release:    1%{?dist}
Summary:    The GNU tape archiving utility

License:    GPLv3+
URL:        https://www.gnu.org/software/tar/
Source0:    %{name}-%{version}.tar.xz

%description
Tar provides the ability to create tar archives, as well as various other
kinds of manipulation.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/tar
%{_mandir}/man1/tar.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
