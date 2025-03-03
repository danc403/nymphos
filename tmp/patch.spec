%global dist .el8

Name:           patch
Version:        2.7.6
Release:        1%{?dist}
Summary:        Apply a diff file to an original file
License:        GPLv3+
URL:            https://savannah.gnu.org/projects/patch
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make

%description
The patch utility applies diff files to originals. Diff files
(also known as patches) contain instructions for changing a file, and
patch changes the file according to the instructions.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
/usr/bin/patch
/usr/share/man/man1/patch.1*
/usr/share/info/patch.info*

%changelog
* %{?epoch:%epoch:}%(date '+%%a %%b %%d %%Y') Dan Carpenter <DanC403@gmail.com> - 2.7.6-1
- Initial build
