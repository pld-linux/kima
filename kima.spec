Summary:	Kima - Kicker monitoring applet
Summary(pl.UTF-8):	Kima - aplet monitorujący dla Kickera
Name:		kima
Version:	0.7.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.elliptique.net/~ken/kima/%{name}-%{version}.tar.gz
# Source0-md5:	ed93c3a6871b514726fcdc6fbf49bba4
Patch0:		kde-ac260-lt.patch
URL:		http://www.elliptique.net/~ken/kima/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
Obsoletes:	cpuinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This applet monitors various temperature, frequency and fan sources in
your Kicker panel. Make sure you have enabled a supported kernel
module.

%description -l pl.UTF-8
Ten aplet panelu Kickera monitoruje różne źródła temperatury,
częstotliwości i działanie wiatraków. Wymaga obsługiwanego
modułu jądra.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# TODO: pass proper dirs to make install instead of moving
install -D $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/kima/index.cache.bz2 $RPM_BUILD_ROOT%{_kdedocdir}/en/kima/index.cache.bz2
install -D $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/kima/index.docbook $RPM_BUILD_ROOT%{_kdedocdir}/en/kima/index.docbook
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/kima/index.cache.bz2 $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/kima/index.docbook

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/libkima.la
%attr(755,root,root) %{_libdir}/kde3/libkima.so
%{_datadir}/apps/kicker/applets/kima.desktop
