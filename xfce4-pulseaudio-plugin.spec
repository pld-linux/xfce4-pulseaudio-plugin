Summary:	Xfce panel plugin for pulseaudio mixer control
Name:		xfce4-pulseaudio-plugin
Version:	0.4.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-pulseaudio-plugin/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	83317e672e843e0b14d0da24ed301b3b
URL:		http://git.xfce.org/panel-plugins/xfce4-pulseaudio-plugin/
BuildRequires:	exo-devel >= 0.11.0
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gtk+3-devel
BuildRequires:	keybinder3-devel >= 0.2.2
BuildRequires:	libwnck-devel >= 3.20
BuildRequires:	libxfce4ui-devel >= 4.14.0
BuildRequires:	libxfce4util-devel >= 4.14.0
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
BuildRequires:	xfconf-devel >= 4.14.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.14.0
Obsoletes:	xfce4-mixer < 4.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xfce PulseAudio Plugin is a plugin for the Xfce panel which
provides a convenient way to adjust the audio volume of the PulseAudio
sound system and to an auto mixer tool like pavucontrol. It can
optionally handle multimedia keys for controlling the audio volume.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm}  $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.so
%{_datadir}/xfce4/panel/plugins/pulseaudio.desktop
%{_iconsdir}/hicolor/*/apps/xfce4-pulseaudio-plugin*
%{_iconsdir}/hicolor/*/status/audio-volume-*
%{_iconsdir}/hicolor/*/status/microphone-sensitivity-*-symbolic.svg
