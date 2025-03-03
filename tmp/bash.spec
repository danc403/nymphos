content: Name:           bash
Version:        5.2.15
Release:        1%{?dist}
Summary:        The GNU Bourne Again Shell - The standard shell for GNU/Linux systems.

License:        GPLv3+
URL:            https://www.gnu.org/software/bash/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  readline-devel
BuildRequires:  ncurses-devel

# Runtime Dependencies - based on description and common usage
Requires:       readline
Requires:       ncurses
Requires:       coreutils

%description
Bash is the GNU Project's Bourne Again Shell, a complete implementation
of the POSIX shell specification, with GNU extensions.  It is a fully
functional scripting language, and is used extensively as the default
login shell on GNU/Linux systems.

%prep
%setup -q

%build
./configure --prefix=/usr --without-bash-malloc
make

%install
make install DESTDIR=%{buildroot}

# Create necessary symlinks for OpenRC compatibility (if needed. Usually not necessary for bash).
# This is just a placeholder.
#mkdir -p %{buildroot}/etc/init.d
#ln -s /lib/rc/init.d/single %{buildroot}/etc/init.d/bash

%files
/usr/bin/bash
/usr/share/man/man1/bash.1*
/usr/share/doc/%{name}/*
/etc/profile.d/bash_completion.sh
/etc/profile.d/bash.sh

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 5.2.15-1
- Initial package build.

