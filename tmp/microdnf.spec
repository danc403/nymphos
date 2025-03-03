content: Name:           microdnf
Version:        3.10.1
Release:        1%{?dist}
Summary:        Micro DNF is a lightweight version of DNF package manager

License:        GPLv2+
URL:            https://github.com/rpm-software-management/microdnf

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  libcomps-devel

Requires:       python3
Requires:       rpm
Requires:       libcomps
Requires:       libsolve
Requires:       libdnf

%description
Micro DNF is a lightweight version of the DNF package manager, designed for
embedded systems and minimal container images. It provides a subset of DNF
functionality, focusing on package installation, removal, and updates.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/microdnf
%{_mandir}/man8/microdnf.8.gz
%{_sysconfdir}/microdnf.conf
%{_datadir}/bash-completion/completions/microdnf
%{_datadir}/zsh/site-functions/_microdnf
%{_datadir}/microdnf/

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 3.10.1-1
- Initial package build.

