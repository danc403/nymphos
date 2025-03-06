Name:           git-accessibility
Version:        2.48.1
Release:        1%{?dist}
Summary:        Git Version Control System with Accessibility Enhancements
License:        GPLv2+
URL:            https://git-scm.com/
Source0:        git-%{version}.tar.gz
BuildRequires:  asciidoc, xmlto, perl-ExtUtils-MakeMaker, zlib-devel, openssl-devel, curl-devel, expat-devel, gettext-devel
Requires:       zlib, openssl, curl, expat, gettext
BuildArch:      x86_64 # or whatever arch you need. adjust as needed.

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations and
full access from programs. This package provides Git with accessibility
enhancements, focusing on improving the experience for blind users.

%prep
%setup -q -n git-%{version}

%build
make prefix=%{_prefix} \
    NO_PERL= \
    NO_PYTHON= \
    NO_TCLTK= \
    NO_INSTALL_HARDLINKS= \
    NO_FINALIZE= \
    all

%install
make prefix=%{_prefix} \
    NO_PERL= \
    NO_PYTHON= \
    NO_TCLTK= \
    NO_INSTALL_HARDLINKS= \
    NO_FINALIZE= \
    install

%files
%license COPYING
%{_bindir}/git
%{_bindir}/git-*
%{_mandir}/man1/git*.1*
%{_mandir}/man7/git*.7*
%{_datadir}/git-core/templates
%{_datadir}/git-core/samples
%{_infodir}/git.info*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package creation for Git with accessibility focus.
- Disabled perl, python, tcltk, hardlinks and finalize.
- Included man pages and info files.
