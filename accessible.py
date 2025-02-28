import os

accessibility_packages = {
    "speech-dispatcher": ("speech-dispatcher-0.10.1.tar.gz", "0.10.1", ["glibc", "dbus", "libpulse"], "speech-dispatcher"),
    "espeak-ng": ("espeak-ng-1.52.0.tar.gz", "1.52.0", ["glibc", "libpulse"], "espeak-ng"),
    "orca": ("orca-47.3.tar.gz", "47.3", ["glibc", "python3", "at-spi2-core", "at-spi2-atk", "pygobject3"], "orca"),
    "libspiel": ("libspiel-SPIEL_1_0_3.tar.gz", "SPIEL_1_0_3", ["glibc"], "libspiel"),
}

template = """
Name:           {package_name}
Version:        {version}
Release:        1%{{?dist}}
Summary:        Accessibility utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        {tarball_path}

BuildArch:      x86_64

BuildRequires:  {build_requires}
Requires:       {requires}

%description
This package provides the {package_name} accessibility utilities for the Nymph Linux distribution.

%prep
%setup -q

%build
%configure
make %{{?_smp_mflags}}

%install
make DESTDIR=%{{buildroot}} install
install -Dm755 {init_script_name} %{{buildroot}}/etc/init.d/{init_script_name}

%files
%license COPYING
%doc README
%{{_bindir}}/*
%{{_libdir}}/*
%{{_sbindir}}/*
%{{_mandir}}/man*
/etc/init.d/{init_script_name}

%changelog
* <date> Your Name <your.email@example.com> - {version}-1
- Initial package for Nymph Linux.
"""

init_script_template = """
#!/sbin/openrc-run

name="{init_script_name}"
command="{command_path}"
pidfile="/run/${{RC_SVCNAME}}.pid"
command_args=""

depend() {
        need net dbus
        use logger
}
"""

for package_name, (tarball, version, dependencies, init_script_name) in accessibility_packages.items():
    tar_extension = tarball.split(".")[-1]
    spec_file = f"specs/{package_name}/{package_name}-{version}.spec"
    tarball_path = f"tarballs/{package_name}/{tarball}"

    build_requires = "\nBuildRequires: ".join(dependencies)
    requires = "\nRequires: ".join(dependencies)

    if init_script_name == "libspiel":
        command_path = "/usr/bin/libspiel" #this is a library, so this is not a command.
    else:
        command_path = f"/usr/bin/{init_script_name}"

    spec_content = template.format(
        package_name=package_name,
        version=version,
        tarball_path=tarball_path,
        build_requires=build_requires,
        requires=requires,
        init_script_name=init_script_name,
        command_path=command_path,
    )

    init_script_content = init_script_template.format(
        init_script_name=init_script_name,
        command_path=command_path,
    )

    os.makedirs(os.path.dirname(spec_file), exist_ok=True)

    with open(spec_file, "w") as f:
        f.write(spec_content)
    print(f"Created {spec_file}")

    init_script_path = f"specs/{package_name}/{init_script_name}"
    with open(init_script_path, "w") as f:
        f.write(init_script_content)
    print(f"Created {init_script_path}")
