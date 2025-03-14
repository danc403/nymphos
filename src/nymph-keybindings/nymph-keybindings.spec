Name:           nymph-keybindings
Version:        1.0
Release:        1%{?dist}
Summary:        Keybinding Editor for Openbox

License:        GPLv3+
URL:            https://github.com/danc403/nymph-keybindings
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  valac >= 0.40
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libgee-devel
BuildRequires:  libxml2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  xdg-utils
BuildRequires:  gettext

Requires:       glib2
Requires:       gtk3
Requires:       libgee
Requires:       libxml2

%description
nymph-keybindings is a tool for managing keybindings in the Openbox window manager.

%package devel
Summary:        Development files for nymph-keybindings
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for nymph-keybindings, including header files and documentation.

%prep
%setup -q

# Check if po directory exists and has .po files
if [ -d "po" ] && [ "$(find po -name '*.po')" ]; then
    # Initialize gettext
    intltoolize --force --copy --automake
    autoreconf -i
    cd po
    make %{?_smp_mflags} all
    cd ..
fi

%build
# Compile the source code
valac --pkg gtk-3.0 --pkg gee-0.8 --pkg libxml-2.0 -o %{name} src/nymph-keybindings.vala
desktop-file-validate %{name}.desktop

# Check if po directory exists and has .po files
if [ -d "po" ] && [ "$(find po -name '*.po')" ]; then
    # Compile localization files
    cd po
    make %{?_smp_mflags} all
    cd ..
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications

# Install binary and desktop file
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# Check if po directory exists and has .po files
if [ -d "po" ] && [ "$(find po -name '*.po')" ]; then
    # Install localization files
    cd po
    for lang in $(find . -name "*.mo" -exec basename {} .mo \;); do
        mkdir -p %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
        install -m 0644 $lang.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/%{name}.mo
    done
    cd ..
fi

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%if [ -d "po" ] && [ "$(find po -name '*.po')" ]; then
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%endif

%files devel
%{_datadir}/include/%{name}

%changelog
* %{_date} Dan Carpenter <danc403@gmail.com> - 1.0-1
- Initial package release
