Name:       make
Version:    4.4.1
Release:    1%{?dist}
Summary:    GNU make utility to maintain groups of programs

License:    GPLv3+
URL:        https://www.gnu.org/software/make/
Source0:    make-%{version}.tar.gz

%description
GNU make is a tool which controls the generation of executables and
other non-source files of a program from the program's source files.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/make
%{_mandir}/man1/make.1*
%{_infodir}/make.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
