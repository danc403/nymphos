name: dracut
version: 059
release: 1%{?dist}
summary: Low-level initramfs generator
license: GPLv2+
url: https://github.com/dracutdevs/dracut
source0: %{name}-%{version}.tar.gz
buildrequires:
  - make
  - automake
  - autoconf
  - gettext
  - pkg-config
  - util-linux
  - bash
  - coreutils
  - eudev
requires:
  - bash
  - coreutils
  - kmod
  - util-linux
  - eudev
  - findutils
  - gzip
  - xz
  - rpm
  - grep
description: Dracut is an event-driven initramfs infrastructure. It provides much more functionality than previous implementations and allows for a more flexible and extensible initramfs. Dracut's primary focus is on providing early boot functionality.
prep:
  - %autosetup
build:
  - ./autogen.sh
  - %configure
  - make %{?_smp_mflags}
install:
  - make install DESTDIR=%{buildroot}
files:
  - %license COPYING
  - %doc README
  - /usr/bin/dracut
  - /usr/lib/dracut
  - /etc/dracut.conf*
  - /usr/share/man/man8/dracut.8*
  - /usr/share/dracut/*
%post
  # Configure dracut for OpenRC (replace with actual configuration)
  if [ -f /etc/dracut.conf.d/openrc.conf ]; then
    echo "Dracut already configured for OpenRC"
  else
    echo "Adding OpenRC configuration to dracut"
    mkdir -p /etc/dracut.conf.d/
    cat > /etc/dracut.conf.d/openrc.conf <<EOF
    # OpenRC configuration for dracut
    omit_dracutmodules+=" systemd "
    omit_dracutmodules+=" systemd-udev "
    omit_dracutmodules+=" busybox "
    force_drivers+=" /lib/modules/\$kernel/fs/nfsd/nfsd.ko "
    add_dracutmodules+=" nfs "
    EOF
  fi

%changelog
  - * Sat Mar 1 2025 Dan Carpenter <DanC403@gmail.com> - 059-1
  - - Initial RPM build
  - - Added OpenRC support
  - - Removed systemd dependencies
