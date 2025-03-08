Name:       ffmpeg
Version:    7.1.1
Release:    1%{?dist}
Summary:    A complete, cross-platform solution to record, convert and stream audio and video.
License:    GPL-2.0-or-later
URL:        https://ffmpeg.org/
Source0:    ffmpeg-%{version}.tar.xz

BuildRequires:  alsa-lib-devel amrwb-devel aom-devel bzip2-devel fontconfig-devel \
                freetype-devel fribidi-devel gnutls-devel lame-devel libass-devel \
                libbluray-devel libcaca-devel libcdio-paranoia-devel libdav1d-devel \
                libgsm-devel libmodplug-devel libmp3lame-devel \
                libopencore-amrnb-devel libopencore-amrwb-devel libopenh264-devel \
                libopenjpeg2-devel libopus-devel libpulse-devel librtmp-devel \
                libshine-devel libsnappy-devel libsoxr-devel libssh-devel libtheora-devel \
                libva-devel libvdpau-devel libvorbis-devel libvpx-devel libwebp-devel \
                libx264-devel libx265-devel libxcb-devel libxml2-devel lzma-devel \
                opencore-amr-devel openssl-devel pulseaudio-libs-devel speex-devel \
                srt-devel zlib-devel

%description
FFmpeg is a complete, cross-platform solution to record, convert and stream audio and video. It includes libavcodec - the leading audio/video codec library.

%package devel
Summary:    Development files for FFmpeg
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files for FFmpeg.

%prep
%autosetup -n ffmpeg-%{version}

%build
%configure --enable-gpl --enable-version3 --enable-nonfree --enable-postproc --enable-swscale \
           --enable-avfilter --enable-pthreads --enable-shared --enable-libmp3lame \
           --enable-libx264 --enable-libx265 --enable-libvpx --enable-libopus \
           --enable-libvorbis --enable-libtheora --enable-libass --enable-libfreetype \
           --enable-fontconfig --enable-libbluray --enable-gnutls --enable-librtmp \
           --enable-libssh --enable-libvdpau --enable-libva --enable-libwebp \
           --enable-libaom --enable-libdav1d --enable-libopenjpeg --enable-libmodplug \
           --enable-libpulse --enable-alsa --enable-libcaca --enable-libopencore-amrnb \
           --enable-libopencore-amrwb --enable-libopenh264 --enable-libshine \
           --enable-libsnappy --enable-libsoxr --enable-srt --enable-speex \
           --enable-zlib --enable-bzlib --enable-lzma --enable-fribidi
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
make install-libs DESTDIR=%{buildroot}
make install-headers DESTDIR=%{buildroot}

%files
%license LICENSE.md
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
%{_bindir}/ffplay
%{_libdir}/libavcodec.so.*
%{_libdir}/libavdevice.so.*
%{_libdir}/libavfilter.so.*
%{_libdir}/libavformat.so.*
%{_libdir}/libavutil.so.*
%{_libdir}/libpostproc.so.*
%{_libdir}/libswresample.so.*
%{_libdir}/libswscale.so.*
%{_mandir}/man1/ffmpeg.1*
%{_mandir}/man1/ffprobe.1*
%{_mandir}/man1/ffplay.1*

%files devel
%{_includedir}/libavcodec/
%{_includedir}/libavdevice/
%{_includedir}/libavfilter/
%{_includedir}/libavformat/
%{_includedir}/libavutil/
%{_includedir}/libpostproc/
%{_includedir}/libswresample/
%{_includedir}/libswscale/
%{_libdir}/libav*.a
%{_libdir}/pkgconfig/libav*.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
