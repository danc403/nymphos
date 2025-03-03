content: Name:           bzip2
Version:        1.0.8
Release:        1%{?dist}
Summary:        A high-quality data compression program - MIT License

License:        MIT
URL:            http://www.bzip.org/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
bzip2 is a compression utility based on the Burrows-Wheeler transform.  bzip2 compresses better than more conventional LZ77/LZ78-based compressors like gzip, and achieves performance comparable to proprietary compressors like PKZIP.

%prep
%setup -q

%build
make -f Makefile-libbz2_so
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_docdir}/%{name}

install -m 755 bzip2 %{buildroot}%{_bindir}/bzip2
install -m 755 bzip2recover %{buildroot}%{_bindir}/bzip2recover
install -m 755 bzcat %{buildroot}%{_bindir}/bzcat
install -m 755 libbz2.so.1.0.8 %{buildroot}%{_libdir}/libbz2.so.1.0.8
ln -s libbz2.so.1.0.8 %{buildroot}%{_libdir}/libbz2.so.1
ln -s libbz2.so.1 %{buildroot}%{_libdir}/libbz2.so
install -m 644 bzip2.1 %{buildroot}%{_mandir}/man1/bzip2.1
install -m 644 bzip2recover.1 %{buildroot}%{_mandir}/man1/bzip2recover.1
install -m 644 bzcat.1 %{buildroot}%{_mandir}/man1/bzcat.1
install -m 644 README %{buildroot}%{_docdir}/%{name}/README
install -m 644 LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE
install -m 644 CHANGELOG %{buildroot}%{_docdir}/%{name}/CHANGELOG


%post
ldconfig

%postun
ldconfig

%files
%{_bindir}/bzip2
%{_bindir}/bzip2recover
%{_bindir}/bzcat
%{_libdir}/libbz2.so.1.0.8
%{_libdir}/libbz2.so.1
%{_libdir}/libbz2.so
%{_mandir}/man1/bzip2.1
%{_mandir}/man1/bzip2recover.1
%{_mandir}/man1/bzcat.1
%{_docdir}/%{name}/README
%{_docdir}/%{name}/LICENSE
%{_docdir}/%{name}/CHANGELOG

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 1.0.8-1
- Initial package build.

