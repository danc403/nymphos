Name:           nymph-keybindings
Version:        1.0
Release:        2%{?dist}
Summary:        Keybinding Editor for Openbox

License:        GPLv3+
URL:            https://github.com/danc403/nymph-keybindings
Source0:        %{name}-%{version}.tar.xz

BuildRequires:    valac >= 0.40
BuildRequires:    glib2-devel
BuildRequires:    gtk3-devel
BuildRequires:    libgee-devel
BuildRequires:    libxml2-devel
BuildRequires:    desktop-file-utils
BuildRequires:    xdg-utils
BuildRequires:    gettext
BuildRequires:    intltool

Requires:         glib2
Requires:         gtk3
Requires:         libgee
Requires:         libxml2

%description
nymph-keybindings is a tool for managing keybindings in the Openbox window manager.

%package devel
Summary:        Development files for nymph-keybindings
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for nymph-keybindings, including header files and documentation.

%prep
%setup -q

# Initialize gettext
intltoolize --force --copy --automake
autoreconf -i

%build
# Compile the source code
valac --pkg gtk-3.0 --pkg gee-0.8 --pkg libxml-2.0 \
       --directory . \
       main.vala common.vala nymph-OS.vala nymph-TTS.vala NVDA.vala macOS.vala orca.vala -o %{name}

desktop-file-validate %{name}.desktop

# Handle translations FIRST to avoid parallel build issues
mkdir -p po
cat > po/Makefile <<EOF
all: \$(patsubst %.po,%.mo,\$(wildcard *.po))

%.mo: %.po
    msgfmt \$< -o \$@

install:
    mkdir -p \${DESTDIR}%{_datadir}/locale
    find . -name "*.mo" -exec install -Dm 644 {} \${DESTDIR}%{_datadir}/locale/{} \;

clean:
    rm -f *.mo
EOF
chmod +x po/Makefile
make -C po

# No need for a second 'make' here unless your project has a separate build process
# make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
#mkdir -p %{buildroot}%{_datadir}/locale  # Handled by po/Makefile install

# Install binary and desktop file
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install translations using the generated Makefile
make -C po install DESTDIR=%{buildroot}

# Clean up generated .mo files (optional, but good practice)
make -C po clean

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%files devel
# %{_datadir}/include/%{name} # No header files are created.  Remove this line.

%changelog
* %{_date} Dan Carpenter <danc403@gmail.com> - 1.0-2
- Corrected the locale handling to use the makefile properly.
* %{_date} Dan Carpenter <danc403@gmail.com> - 1.0-1
- Initial package release
