Name:       sed
Version:    4.9
Release:    1%{?dist}
Summary:    The GNU stream editor

License:    GPLv3+
URL:        https://www.gnu.org/software/sed/
Source0:    %{name}-%{version}.tar.xz

%description
Sed (stream editor) is a non-interactive text editor that reads input
streams (files or input from the pipeline) and modifies the stream
according to a list of commands.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/sed
%{_mandir}/man1/sed.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
