Name:       groff
Version:    1.22.4
Release:    1%{?dist}
Summary:    GNU troff text-formatting system

License:    GPLv3+
URL:        https://www.gnu.org/software/groff/
Source0:    %{name}-%{version}.tar.gz

%description
Groff is a typesetting system that reads plain text mixed with formatting
commands and outputs formatted text.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
