# specs/rxvt-unicode/rxvt-unicode-9.31.spec
Name:           rxvt-unicode
Version:        9.31
Release:        1%{?dist}
Summary:        A Unicode-enabled version of the rxvt terminal emulator
License:        GPLv3+
URL:            https://rxvt.sourceforge.io/
Source0:        rxvt-unicode-9.31.tar.bz2

BuildRequires:  perl, pkgconfig, libX11-devel, libXft-devel, libXrender-devel, libXext-devel, libXpm-devel, fontconfig-devel, imlib2-devel

%description
rxvt-unicode (urxvt) is a highly configurable, Unicode-enabled version of
the rxvt terminal emulator.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --disable-wtmp --disable-utmp --enable-font-rendering=Xft --enable-unicode3 --enable-combining --enable-pixbuf --enable-frills
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/urxvt
%{_bindir}/urxvtc
%{_mandir}/man1/urxvt.1*
%{_mandir}/man1/urxvtc.1*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 9.31-1
- Initial package.
