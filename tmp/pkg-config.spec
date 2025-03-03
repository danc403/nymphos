content: Name:           pkg-config
Version:        0.29.2
Release:        1%{?dist}
Summary:        A system for managing library compile/link flags - MIT License

License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/pkg-config/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
pkg-config is a helper tool used when compiling applications and
libraries. It helps you insert the correct compiler options on the
command line so an application can be compiled with the correct
semantics.

pkg-config retrieves information about installed libraries. It is
typically used to determine the compiler and linker flags that should
be used to compile and link programs that use the libraries.

%prep
%autosetup

%build
./configure --prefix=%{_prefix} --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/pkg-config
%{_datadir}/pkgconfig
%{_mandir}/man1/pkg-config.1.*
%{_datadir}/aclocal/pkg-config.m4
%{_datadir}/pkg-config/*

%changelog
* %{?epoch:%{epoch}:}%{version}-%{release} %{?date:%{date}} Dan Carpenter DanC403@gmail.com
- Initial package build

filename: pkg-config.spec
