content: Name:           cracklib
Version:        2.9.7
Release:        1%{?dist}
Summary:        Password checking library
License:        LGPLv2+
URL:            http://cracklib.sourceforge.net/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  bzip2-devel
BuildRequires:  libtool

#Runtime dependencies are detected by autoscan


%description
CrackLib is a password checking library.  It tries to prevent
users from choosing easily guessable passwords.


%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/cracklib-packer
%{_bindir}/cracklib-unpacker
%{_libdir}/libcrack.so.*
%{_datadir}/cracklib/*
%{_mandir}/man5/cracklib.5.gz
%{_mandir}/man8/cracklib-packer.8.gz
%{_mandir}/man8/cracklib-unpacker.8.gz

%changelog
* %{DATE} Dan Carpenter <DanC403@gmail.com> - 2.9.7-1
- Initial package build

