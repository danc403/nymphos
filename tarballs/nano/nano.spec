Name:       nano
Version:    6.4
Release:    1%{?dist}
Summary:    A small, easy to use editor

License:    GPLv3+
URL:        https://www.nano-editor.org/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  ncurses-devel

%description
GNU nano is a small, friendly editor.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/nano
%{_mandir}/man1/nano.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
