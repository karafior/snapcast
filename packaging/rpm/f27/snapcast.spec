%define debug_package %{nil}

Name:           snapcast
Version:        0.12.0
Release:        1%{?dist}
Summary:        Synchronous audio player

License:        GPLv3
URL:            https://github.com/badaix/snapcast
Source0:        snapcast-0.12.0.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libstdc++-static
BuildRequires:  flac-devel
BuildRequires:  asio-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  avahi-devel
BuildRequires:  libatomic

Requires:       flac
Requires:       asio
Requires:       alsa-lib
Requires:       libogg
Requires:       libvorbis
Requires:       avahi

%description
Snapcast is a multi-room client-server audio player, where all clients are
time synchronized with the server to play perfectly synced audio. It's not
a standalone player, but an extension that turns your existing audio player
into a Sonos-like multi-room solution.

%package client
Summary:        Snapcast client

%description client
Snapcast client

%package server
Summary:        Snapcast server

%description server
Snapcast server daemon

%prep
%setup

%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
# Snapcast client
install -D client/snapclient $RPM_BUILD_ROOT/%{_sbindir}/snapclient
install -D client/snapclient.1 $RPM_BUILD_ROOT/%{_mandir}/man1/snapclient.1

# Snapcast server
install -D server/snapserver $RPM_BUILD_ROOT/%{_sbindir}/snapserver
install -D server/snapserver.1 $RPM_BUILD_ROOT/%{_mandir}/man1/snapserver.1

# Systemd services
install -D client/fedora/snapclient.service $RPM_BUILD_ROOT/%{_unitdir}/snapclient.service
install -D server/fedora/snapserver.service $RPM_BUILD_ROOT/%{_unitdir}/snapserver.service

install -D client/fedora/snapclient.default $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/snapclient
install -D server/fedora/snapserver.default $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/snapserver


%files
%license LICENSE
%doc README.md

%files client
%defattr(-,root,root,-)
%{_sbindir}/snapclient
%{_mandir}/man1/snapclient.1.gz
%{_unitdir}/snapclient.service
%{_sysconfdir}/sysconfig/snapclient

%files server
%defattr(-,root,root,-)
%{_sbindir}/snapserver
%{_mandir}/man1/snapserver.1.gz
%{_unitdir}/snapserver.service
%{_sysconfdir}/sysconfig/snapserver

%changelog
* Sat Jan 13 2018 Jakub Raczkowski <jakubr@gmail.com>
- Update to 0.12.0

* Fri Sep  9 2016 Sylvain Baubeau <sbaubeau@redhat.com>
- Initial release

