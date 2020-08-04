Name:    ofono
Summary: Open Source Telephony
Version: 1.31
Release: 1
License: GPLv2
URL:     http://ofono.org/
Source0: https://git.kernel.org/pub/scm/network/ofono/ofono.git/snapshot/ofono-%{version}.tar.gz
BuildRequires: automake libtool
BuildRequires: pkgconfig(ell)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libudev) >= 145
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(mobile-broadband-provider-info)
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
oFono.org is a place to bring developers together around designing an
infrastructure for building mobile telephony (GSM/UMTS) applications.
oFono includes a high-level D-Bus API for use by telephony applications.
oFono also includes a low-level plug-in API for integrating with telephony
stacks, cellular modems and storage back-ends.

%package devel
Summary: Development files for oFono
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q

%build
if [ ! -f configure ]; then
./bootstrap
fi
%configure \
	--enable-bluetooth \
	--enable-pie \
	--enable-external-ell \
	--disable-silent-rules

%make_build


%install
%make_install

# create/own this
mkdir -p %{buildroot}%{_libdir}/ofono/plugins


%check
make check

%files
%doc ChangeLog AUTHORS README
%license COPYING
%{_sysconfdir}/dbus-1/system.d/ofono.conf
%dir %{_sysconfdir}/ofono/
%config(noreplace) %{_sysconfdir}/ofono/phonesim.conf
%{_sbindir}/ofonod
%{_unitdir}/ofono.service
%{_mandir}/man8/ofonod.8*
%dir %{_libdir}/ofono
%dir %{_libdir}/ofono/plugins

%files devel
%{_includedir}/ofono
%{_libdir}/pkgconfig/ofono.pc
