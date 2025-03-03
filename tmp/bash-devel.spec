content: Name:           bash-devel
Version:        5.2.15
Release:        1%{?dist}
Summary:        Development files for bash.

License:        GPLv3+
URL:            https://www.gnu.org/software/bash/
Source0:        %{name}-%{version}.tar.gz

Requires:       bash = %{version}-%{release}
Requires:       readline-devel

%description
This package contains the header files and libraries necessary for
developing applications that use bash.

%prep
%setup -q

%build
./configure --prefix=/usr --without-bash-malloc
make

%install
make install DESTDIR=%{buildroot}

%files
/usr/include/bash
/usr/include/bash/*.h
/usr/lib64/bash/*


%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 5.2.15-1
- Initial package build.

