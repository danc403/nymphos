Name:       rxvt-unicode
Version:    9.31
Release:    1%{?dist}
Summary:    A Unicode-enabled version of the rxvt terminal emulator

License:    GPLv3+
URL:        http://software.schmorp.de/pkg/rxvt-unicode.html
Source0:    rxvt-unicode-%{version}.tar.bz2

BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  perl

%description
Rxvt-unicode is a Unicode-enabled version of the rxvt terminal emulator,
a popular replacement for the standard xterm.

%prep
%setup -q -n rxvt-unicode-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/urxvt
%{_mandir}/man1/urxvt.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
