%global dist .el8

Name:           patch-devel
Version:        2.7.6
Release:        1%{?dist}
Summary:        Development files for patch
License:        GPLv3+
URL:            https://savannah.gnu.org/projects/patch
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  patch = %{version}-%{release}
Requires:       patch = %{version}-%{release}

%description
This package contains the header files and static libraries needed to develop
applications that use the patch library.

%prep
%setup -q -n %{name}-%{version}

%build
# No build required for devel package, files are already built by patch

%install
%make_install

%files
%defattr(-,root,root,-)
%{_includedir}/patch.h
%{_libdir}/libpatch.a
%license COPYING

%changelog
* %{?epoch:%epoch:}%(date '+%%a %%b %%d %%Y') Dan Carpenter <DanC403@gmail.com> - 2.7.6-1
- Initial build for patch-devel
