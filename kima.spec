# TODO:
# - polish translation
Summary:	Kima - Kicker monitoring applet
Name:		kima
Version:	0.7.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.elliptique.net/~ken/kima/%{name}-%{version}.tar.gz
# Source0-md5:	b5e4274e008f65ee8d60fdbc9790e144
Patch0:		kde-ac260-lt.patch
Patch1:		%{name}-am110.patch
URL:		http://www.elliptique.net/~ken/kima/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This applet monitors various temperature, frequency and fan sources in
your kicker panel. Make sure you have enabled a supported kernel
module.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
