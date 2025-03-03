%global dist .el8

Name:           bc
Version:        1.08.1
Release:        1%{?dist}
Summary:        An arbitrary precision calculator language
License:        GPLv2+
URL:            https://git.savannah.gnu.org/cgit/bc.git
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  readline-devel
Requires:       readline
BuildArch:      x86_64

%description
bc is an arbitrary precision calculator language.  Syntax is similar to C, but 
differs in a few important areas.  It includes an interactive environment.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/bin/bc
/usr/bin/dc
/usr/share/man/man1/bc.1*
/usr/share/man/man1/dc.1*
/usr/share/info/bc.info*

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 1.08.1-1
- Initial package build.
