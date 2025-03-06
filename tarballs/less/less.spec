Name:       less
Version:    608
Release:    1%{?dist}
Summary:    A program similar to more (1), but which allows backward movement in the file, as well as forward movement

License:    GPLv3+
URL:        http://www.greenwoodsoftware.com/less/
Source0:    %{name}-%{version}.tar.gz

%description
Less is a program similar to more (1), but which allows backward movement
in the file, as well as forward movement.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/less
%{_mandir}/man1/less.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
