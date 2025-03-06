Name:       man-db
Version:    2.11.2
Release:    1%{?dist}
Summary:    The on-line manual pager

License:    GPLv2+
URL:        https://www.nongnu.org/man-db/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  zlib-devel
BuildRequires:  gdbm-devel # or db-devel, depending on your system's database library

%description
Man-db is the on-line manual pager.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
