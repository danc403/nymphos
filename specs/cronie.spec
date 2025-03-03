
Name:           cronie
Version:        1.7.2
Release:        1%{?dist}
Summary:        <short_description>

License:        <license>
URL:            <upstream_url>
Source0:        tarballs/cronie/cronie-1.7.2.tar.gz

BuildArch:      x86_64

BuildRequires:  <build_time_dependencies>
Requires:       <runtime_dependencies>

%description
<full_description>

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%license COPYING
%doc README
%{_bindir}/<binary_name>
%{_libdir}/lib<library_name>.so
%{_includedir}/<header_files>
%{_mandir}/man1/<man_page>.1*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 1.7.2-1
- Initial package
