content: Name:           readline
Version:        8.2
Release:        1%{?dist}
Summary:        GNU Readline library - a set of functions for use by applications that allow users to edit command lines as they are typed in. GPLv3+
License:        GPLv3+
URL:            https://tiswww.case.edu/php/chet/readline/rltop.html

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel
Requires:       ncurses

%description
The GNU Readline library provides a set of functions for use by
applications that allow users to edit command lines as they are typed
in.  Both Emacs and vi editing modes are available.

Install Readline if you want to provide command line editing
capabilities in your programs.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove libtool archive
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_bindir}/rlwrap
%{_libdir}/libreadline.so.*
%{_libdir}/libhistory.so.*
%{_mandir}/man1/rlwrap.1.*
%{_infodir}/readline.info.*
%{_datadir}/readline
%license COPYING

%changelog
* %{_isodate} Dan Carpenter DanC403@gmail.com - 8.2-1
- Initial package build

filename: readline.spec
