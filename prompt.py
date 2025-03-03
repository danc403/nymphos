#!/usr/bin/env python3

def generate_prompt(package_name, package_version, package_filename):
    """Generates the prompt for creating .spec files, incorporating filename."""

    prompt_tpl = """
"You are an expert RPM spec file creator. I need you to generate .spec files for building RPM and SRPM packages for an x86_64 Linux distribution. The system uses OpenRC as the init system, LightDM as the display manager, and GTK for accessibility. The packages will be built from source tarballs.

Here are the specific requirements:

1.  **Package Type:** Create two spec files for each source tarball: one for the main package and another for the development package (-devel).
2.  **Dependencies:** Ensure that the spec files include all necessary build and runtime dependencies. Pay close attention to GTK, X11, audio, and network dependencies.
3.  **Accessibility:** Consider any accessibility-related dependencies.
4.  **OpenRC and LightDM:** Configure the spec files for compatibility with OpenRC and LightDM.
5.  **Standard Build Process:** Use the standard `configure`, `make`, and `make install` build process unless otherwise specified, or you are aware of it requiring another method.
6.  **File Locations:** Install binaries in `/usr/bin`, libraries in `/usr/lib64`, configuration files in `/etc`, and documentation in `/usr/share/doc`.
7.  **Development Packages:** For -devel packages, include header files, static libraries, and pkg-config files in the `/usr/include` and `/usr/lib64/pkgconfig` directories.
8.  **License:** Include the appropriate license file in the `%files` section. If possible, please include the license name in the spec file summary.
9.  **Changelog:** Add a basic changelog entry with the current date, Dan Carpenter DanC403@gmail.com , and the initial build information.
10. **Source Tarball:** The source tarball is '{package_filename}'. The beginning of the tarball name will match the package name.
11. **System packages:** The system will contain the following packages: Python, alsa-utils, audit, autoconf, automake, bash, bc, binutils, bison, bzip2, coreutils, cracklib, cronie, dbus, dbus-glib, dejavu-fonts-ttf, dhcpcd, diffutils, dracut, e2fsprogs, espeak-ng, fail2ban, findutils, firefox, flex, fontconfig, gawk, gcc, geany, gettext, gmp, gperf, grep, groff, gtk, gzip, inetutils, iproute2, less, libcap, libcap-ng, libffi, libseccomp, libspiel, libtool, lightdm, linux, linux-pam, m4, make, man-db, microdnf, mpc, mpfr, nano, ncurses, net-tools, openbox, openrc, openssl, orca, patch, pciutils, perl, pkg-config, polkit, readline, rpm, rxvt-unicode, sed, shadow, speech-dispatcher, syslinux, sysstat, tar, texinfo, usbutils, util-linux, vim, xorg-server, xz, zlib.
12. **Example:** if the package name is 'example' and version is '1.2.3', then create 'example.spec' and 'example-devel.spec'.

Please provide the .spec files for the following package: {package_name} version {package_version} ({package_filename})."
    """.format(package_name=package_name, package_version=package_version, package_filename=package_filename)

    return prompt_tpl


package_list = [
    {"name": "Python", "version": "3.13.2", "filename": "Python-3.13.2.tar.xz"},
    {"name": "alsa-utils", "version": "1.2.10", "filename": "alsa-utils-1.2.10.tar.bz2"},
    {"name": "audit", "version": "3.0.9", "filename": "audit-3.0.9.tar.gz"},
    {"name": "autoconf", "version": "2.71", "filename": "autoconf-2.71.tar.gz"},
    {"name": "automake", "version": "1.16.5", "filename": "automake-1.16.5.tar.gz"},
    {"name": "bash", "version": "5.2.15", "filename": "bash-5.2.15.tar.gz"},
    {"name": "bc", "version": "1.08.1", "filename": "bc-1.08.1.tar.gz"},
    {"name": "binutils", "version": "2.40", "filename": "binutils-2.40.tar.xz"},
    {"name": "bison", "version": "3.8", "filename": "bison-3.8.tar.xz"},
    {"name": "bzip2", "version": "1.0.8", "filename": "bzip2-1.0.8.tar.gz"},
    {"name": "coreutils", "version": "9.3", "filename": "coreutils-9.3.tar.xz"},
    {"name": "cracklib", "version": "2.9.7", "filename": "cracklib-2.9.7.tar.gz"},
    {"name": "cronie", "version": "1.7.2", "filename": "cronie-1.7.2.tar.gz"},
    {"name": "dbus", "version": "1.16.0", "filename": "dbus-1.16.0.tar.xz"},
    {"name": "dbus-glib", "version": "0.112", "filename": "dbus-glib-0.112.tar.gz"},
    {"name": "dejavu-fonts-ttf", "version": "2.37", "filename": "dejavu-fonts-ttf-2.37.tar.bz2"},
    {"name": "dragonfly-fonts-ttf", "version": "0", "filename": "dragonfly-fonts-ttf.tar.xz"},
    {"name": "luciole-fonts-ttf", "version": "0", "filename": "luciole-fonts-ttf.tar.xz"},
    {"name": "dhcpcd", "version": "10.2.0", "filename": "dhcpcd-10.2.0.tar.gz"},
    {"name": "diffutils", "version": "3.9", "filename": "diffutils-3.9.tar.xz"},
    {"name": "dracut", "version": "059", "filename": "dracut-059.tar.gz"},
    {"name": "e2fsprogs", "version": "1.47.2", "filename": "e2fsprogs-1.47.2.tar.gz"},
    {"name": "espeak-ng", "version": "1.52.0", "filename": "espeak-ng-1.52.0.tar.gz"},
    {"name": "fail2ban", "version": "1.1.0", "filename": "fail2ban-1.1.0.tar.gz"},
    {"name": "findutils", "version": "4.9.0", "filename": "findutils-4.9.0.tar.xz"},
    {"name": "firefox", "version": "136.0b9.en_US", "filename": "firefox-136.0b9.en_US.tar.xz"},
    {"name": "flex", "version": "2.6.4", "filename": "flex-2.6.4.tar.gz"},
    {"name": "fontconfig", "version": "2.15.0", "filename": "fontconfig-2.15.0.tar.xz"},
    {"name": "gawk", "version": "5.2.1", "filename": "gawk-5.2.1.tar.xz"},
    {"name": "gcc", "version": "13.2.0", "filename": "gcc-13.2.0.tar.xz"},
    {"name": "geany", "version": "2.0", "filename": "geany-2.0.tar.gz"},
    {"name": "gettext", "version": "0.21.1", "filename": "gettext-0.21.1.tar.xz"},
    {"name": "gmp", "version": "6.3.0", "filename": "gmp-6.3.0.tar.xz"},
    {"name": "gperf", "version": "3.1", "filename": "gperf-3.1.tar.gz"},
    {"name": "grep", "version": "3.9", "filename": "grep-3.9.tar.xz"},
    {"name": "groff", "version": "1.22.4", "filename": "groff-1.22.4.tar.gz"},
    {"name": "gtk", "version": "4.9.4", "filename": "gtk-4.9.4.tar.xz"},
    {"name": "gzip", "version": "1.12", "filename": "gzip-1.12.tar.xz"},
    {"name": "inetutils", "version": "2.3", "filename": "inetutils-2.3.tar.xz"},
    {"name": "iproute2", "version": "6.1.0", "filename": "iproute2-6.1.0.tar.xz"},
    {"name": "less", "version": "608", "filename": "less-608.tar.gz"},
    {"name": "libcap", "version": "2.73", "filename": "libcap-2.73.tar.xz"},
    {"name": "libcap-ng", "version": "0.8.5", "filename": "libcap-ng-0.8.5.tar.gz"},
    {"name": "libffi", "version": "3.4.4", "filename": "libffi-3.4.4.tar.gz"},
    {"name": "libseccomp", "version": "2.6.0", "filename": "libseccomp-2.6.0.tar.gz"},
    {"name": "libspiel", "version": "SPIEL_1_0_3", "filename": "libspiel-SPIEL_1_0_3.tar.gz"},
    {"name": "libtool", "version": "2.4.7", "filename": "libtool-2.4.7.tar.xz"},
    {"name": "lightdm", "version": "1.32.0", "filename": "lightdm-1.32.0.tar.xz"},
    {"name": "linux", "version": "6.5.3", "filename": "linux-6.5.3.tar.xz"},
    {"name": "linux-pam", "version": "1.7.0", "filename": "linux-pam-1.7.0.tar.gz"},
    {"name": "m4", "version": "1.4.19", "filename": "m4-1.4.19.tar.gz"},
    {"name": "make", "version": "4.4.1", "filename": "make-4.4.1.tar.gz"},
    {"name": "man-db", "version": "2.11.2", "filename": "man-db-2.11.2.tar.xz"},
    {"name": "microdnf", "version": "3.10.1", "filename": "microdnf-3.10.1.tar.gz"},
    {"name": "mpc", "version": "1.3.1", "filename": "mpc-1.3.1.tar.gz"},
    {"name": "mpfr", "version": "4.2.0", "filename": "mpfr-4.2.0.tar.xz"},
    {"name": "nano", "version": "6.4", "filename": "nano-6.4.tar.xz"},
    {"name": "ncurses", "version": "6.4", "filename": "ncurses-6.4.tar.gz"},
    {"name": "net-tools", "version": "2.10", "filename": "net-tools-2.10.tar.xz"},
    {"name": "openbox", "version": "3.6.1", "filename": "openbox-3.6.1.tar.xz"},
    {"name": "openrc", "version": "0.56", "filename": "openrc-0.56.tar.gz"},
    {"name": "openssl", "version": "3.1.1", "filename": "openssl-3.1.1.tar.gz"},
    {"name": "orca", "version": "47.3", "filename": "orca-47.3.tar.gz"},
    {"name": "patch", "version": "2.7.6", "filename": "patch-2.7.6.tar.xz"},
    {"name": "pciutils", "version": "3.9.0", "filename": "pciutils-3.9.0.tar.xz"},
    {"name": "perl", "version": "5.40.1", "filename": "perl-5.40.1.tar.gz"},
    {"name": "pkg-config", "version": "0.29.2", "filename": "pkg-config-0.29.2.tar.gz"},
    {"name": "polkit", "version": "1.23", "filename": "polkit-1.23.tar.bz2"},
    {"name": "readline", "version": "8.2", "filename": "readline-8.2.tar.gz"},
    {"name": "rpm", "version": "4.20.1", "filename": "rpm-4.20.1.tar.bz2"},
    {"name": "rxvt-unicode", "version": "9.31", "filename": "rxvt-unicode-9.31.tar.bz2"},
    {"name": "sed", "version": "4.9", "filename": "sed-4.9.tar.xz"},
    {"name": "shadow", "version": "4.17.2", "filename": "shadow-4.17.2.tar.xz"},
    {"name": "speech-dispatcher", "version": "0.10.1", "filename": "speech-dispatcher-0.10.1.tar.gz"},
    {"name": "syslinux", "version": "6.03", "filename": "syslinux-6.03.tar.xz"},
    {"name": "sysstat", "version": "12.6.1", "filename": "sysstat-12.6.1.tar.gz"},
    {"name": "tar", "version": "1.34", "filename": "tar-1.34.tar.xz"},
    {"name": "texinfo", "version": "7.0", "filename": "texinfo-7.0.tar.xz"},
    {"name": "usbutils", "version": "017", "filename": "usbutils-017.tar.xz"},
    {"name": "util-linux", "version": "2.39", "filename": "util-linux-2.39.tar.xz"},
    {"name": "vim", "version": "9.0.1635", "filename": "vim-9.0.1635.tar.gz"},
    {"name": "xorg-server", "version": "21.1.16", "filename": "xorg-server-21.1.16.tar.xz"},
    {"name": "xz", "version": "5.4.1", "filename": "xz-5.4.1.tar.xz"},
    {"name": "zlib", "version": "1.3.1", "filename": "zlib-1.3.1.tar.gz"}
]
if __name__ == "__main__":
    for package in package_list:
        package_name = package["name"]
        package_version = package["version"]
        package_filename = package["filename"]

        # Your work with the variables goes here
        print(f"Processing: {package_name} {package_version} {package_filename}")
        prompt = generate_prompt(package_name, package_version, package_filename)
        # Write the prompt to a file
        filename = f"{package_name}.prompt"
        try:
            with open(filename, "w") as f:
                f.write(prompt)
            print(f"Prompt written to {filename}") #confirmation
        except Exception as e:
            print(f"Error writing to {filename}: {e}")

