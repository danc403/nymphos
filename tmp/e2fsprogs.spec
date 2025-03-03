name: e2fsprogs
version: 1.47.2
release: 1%{?dist}
summary: Ext2/ext3/ext4 file system utilities
License: GPLv2+
URL: https://e2fsprogs.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
BuildRequires: e2fsprogs-devel
Requires: perl
Provides: debuginfo(uuid)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%description: The e2fsprogs package contains the ext2fs filesystem utilities.
%prep: %setup -q
%build: %configure
make %{?_smp_mflags}: None
%install: make install DESTDIR=%{buildroot}
%files:
  - /etc/mke2fs.conf
  - /usr/sbin/*
  - /usr/lib64/*
  - /usr/share/man/man8/*
  - /usr/share/man/man5/*
  - /usr/bin/*
  - /usr/share/doc/%{name}/*
  - /usr/lib64/lib*.so.*
%changelog:
  - * Tue Oct 24 2023 Dan Carpenter DanC403@gmail.com - 1.47.2-1
  - - Initial build
