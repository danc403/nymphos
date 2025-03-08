Name:       vlc
Version:    3.0.20
Release:    1%{?dist}
Summary:    The cross-platform multimedia player and framework
License:    GPL-2.0-or-later
URL:        https://www.videolan.org/vlc/
Source0:    vlc-%{version}.tar.xz

BuildRequires:  alsa-lib-devel aom-devel avcodec-devel avformat-devel avutil-devel \
                bluray-devel faad2-devel fontconfig-devel freetype-devel fribidi-devel \
                gcc-c++ gnutls-devel libass-devel libcddb-devel libdca-devel libdvbpsi-devel \
                libgcrypt-devel libgpg-error-devel libmad-devel libmkv-devel libmodplug-devel \
                libmp4v2-devel libmpeg2-devel libogg-devel libpng-devel libsamplerate-devel \
                libshout-devel libsndfile-devel libssh-devel libtheora-devel libtool \
                libva-devel libvdpau-devel libvorbis-devel libvpx-devel libxml2-devel \
                lua-devel opus-devel speex-devel taglib-devel twolame-devel upnp-devel \
                vcdimager-devel wavpack-devel webm-devel xcb-devel xcb-util-devel \
                xcb-util-keysyms-devel zlib-devel

%description
VLC media player is a highly portable multimedia player and framework capable of playing various audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX, mp3, ogg, etc.), as well as DVDs, VCDs, and various streaming protocols. It provides a rich set of features, including codec support, hardware acceleration, and a command-line interface, making it a versatile tool for multimedia playback.

%package cli
Summary:    Command-line interface for VLC media player
Requires:   %{name} = %{version}-%{release}

%description cli
This package contains the command-line interface (cvlc) for VLC media player, providing a text-based way to control and use VLC.

%prep
%autosetup -n vlc-%{version}

%build
./configure --prefix=%{_prefix} --enable-release --enable-lua --enable-vdpau --enable-vaapi --enable-avcodec --enable-avformat --enable-swscale --enable-postproc --enable-aom --enable-bluray --enable-dvdnav --enable-dvdread --enable-gnutls --enable-libass --enable-libcddb --enable-libdca --enable-libdvbpsi --enable-libgcrypt --enable-libmad --enable-libmkv --enable-libmodplug --enable-libmp4v2 --enable-libmpeg2 --enable-libogg --enable-libpng --enable-libsamplerate --enable-libshout --enable-libsndfile --enable-libssh --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libxml2 --enable-opus --enable-speex --enable-taglib --enable-twolame --enable-upnp --enable-vcdimager --enable-wavpack --enable-webm --enable-xcb --enable-xcb-keysyms --enable-alsa --enable-faad --enable-freetype --enable-fontconfig --enable-fribidi --enable-cli
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/vlc
%{_bindir}/cvlc
%{_libdir}/vlc/
%{_datadir}/applications/vlc.desktop
%{_datadir}/icons/hicolor/*/apps/vlc.png
%{_mandir}/man1/vlc.1*
%{_mandir}/man1/cvlc.1*

%files cli
%{_bindir}/cvlc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
