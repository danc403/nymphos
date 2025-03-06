Name:       vim
Version:    9.0.1635
Release:    1%{?dist}
Summary:    Vi IMproved, a highly configurable text editor

License:    Vim
URL:        https://www.vim.org/
Source0:    %{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel

%description
Vim is a highly configurable text editor built to enable efficient text
editing.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --enable-multibyte
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/vim
%{_bindir}/vi
%{_bindir}/view
%{_mandir}/man1/vim.1*
%{_mandir}/man1/vi.1*
%{_mandir}/man1/view.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
