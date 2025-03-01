Name:       microdnf
Version:    3.10.1
Release:    1%{?dist}
Summary:    A lightweight DNF package manager

License:    GPLv2+
URL:        https://github.com/rpm-software-management/microdnf
Source0:    %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libcomps-devel
BuildRequires:  libdnf-devel
BuildRequires:  libsolv-devel
BuildRequires:  rpm-devel
BuildRequires:  zlib-devel

%description
Microdnf is a lightweight version of DNF, designed for minimal
environments such as containers. It provides a subset of DNF's
functionality for installing, updating, and removing packages.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_bindir}/microdnf
%{_mandir}/man8/microdnf.8*

%changelog
* Mon Nov 20 2023 Your Name <your.email@example.com> - 3.10.1-1
- Initial build for OpenRC.
