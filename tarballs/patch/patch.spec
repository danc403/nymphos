Name:       patch
Version:    2.7.6
Release:    1%{?dist}
Summary:    A program for applying diff files to original files

License:    GPLv3+
URL:        https://www.gnu.org/software/patch/
Source0:    %{name}-%{version}.tar.xz

%description
Patch takes a patch file containing a difference listing produced by the
diff program and applies those differences to one or more original files,
producing patched versions.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/patch
%{_mandir}/man1/patch.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
