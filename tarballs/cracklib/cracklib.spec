Name:       cracklib
Version:    2.9.7
Release:    1%{?dist}
Summary:    A password checking library

License:    LGPLv2+
URL:        https://github.com/cracklib/cracklib
Source0:    cracklib-%{version}.tar.gz

%description
CrackLib is a library that checks passwords for weakness. It is used
by programs like passwd to prevent users from choosing easily guessed
passwords.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libcrack.so.*
%{_bindir}/cracklib-unpacker
%{_bindir}/cracklib-packer
%{_mandir}/man3/cracklib.3*
%{_mandir}/man8/cracklib-unpacker.8*
%{_mandir}/man8/cracklib-packer.8*

%files devel
%{_includedir}/crack.h
%{_libdir}/libcrack.so
%{_libdir}/pkgconfig/cracklib.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
