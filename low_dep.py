import os

low_dependency_packages = {
    "coreutils": ("coreutils-9.3.tar.xz", "9.3", ["glibc"]),
    "findutils": ("findutils-4.9.0.tar.xz", "4.9.0", ["glibc"]),
    "nano": ("nano-6.4.tar.xz", "6.4", ["glibc", "ncurses"]),
    "vim-tiny": ("vim-9.0.1635.tar.gz", "9.0.1635", ["glibc", "ncurses"]),
    "grep": ("grep-3.9.tar.xz", "3.9", ["glibc"]),
    "gzip": ("gzip-1.12.tar.xz", "1.12", ["glibc", "zlib"]),
    "xz": ("xz-5.4.1.tar.xz", "5.4.1", ["glibc", "liblzma"]),
    "tar": ("tar-1.34.tar.xz", "1.34", ["glibc", "liblzma", "zlib", "bzip2"]),
}

template = """
Name:           {package_name}
Version:        {version}
Release:        1%{{?dist}}
Summary:        Basic {package_name} utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        {tarball_path}

BuildArch:      x86_64

BuildRequires:  {build_requires}
Requires:       {requires}

%description
This package provides the core {package_name} utilities for the Nymph Linux distribution.

%prep
%setup -q

%build
%configure
make %{{?_smp_mflags}}

%install
make DESTDIR=%{{buildroot}} install

%files
%license COPYING
%doc README
%{{_bindir}}/*
%{{_mandir}}/man1/*

%changelog
* <date> Your Name <your.email@example.com> - {version}-1
- Initial package for Nymph Linux.
"""

for package_name, (tarball, version, dependencies) in low_dependency_packages.items():
    tar_extension = tarball.split(".")[-1]
    spec_file = f"specs/{package_name}/{package_name}-{version}.spec"
    tarball_path = f"tarballs/{package_name}/{tarball}"

    build_requires = "\nBuildRequires: ".join(dependencies)
    requires = "\nRequires: ".join(dependencies)

    spec_content = template.format(
        package_name=package_name,
        version=version,
        tarball_path=tarball_path,
        build_requires=build_requires,
        requires=requires,
    )

    os.makedirs(os.path.dirname(spec_file), exist_ok=True)

    with open(spec_file, "w") as f:
        f.write(spec_content)
    print(f"Created {spec_file}")
