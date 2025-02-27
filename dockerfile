FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    rpm rpm-build gcc make patch tar xz bzip2 gzip \
    binutils libelf-dev openssl libssl-dev zlib1g-dev \
    libncurses5-dev perl python3 python3-dev bc bison flex \
    libtool autoconf automake pkg-config git libmnl-dev \
    libcap-ng-dev libselinux1-dev libkmod-dev libaudit-dev \
    pciutils libudev-dev libmount-dev e2fsprogs-dev libblkid-dev \
    libdevmapper-dev libnl-3-dev libcap-dev libtirpc-dev \
    libseccomp-dev libbpf-dev

WORKDIR /app

COPY . /app

CMD ["/app/build_srpms.sh"]
