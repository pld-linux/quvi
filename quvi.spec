Summary:	Command line tool for parsing flash video download links
Summary(pl.UTF-8):	Narzędzie linii poleceń do analizy odnośników do pobierania filmów flashowych
Name:		quvi
Version:	0.9.5
Release:	3
License:	AGPL v3+
Group:		Applications/WWW
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	baa1d7b25e9fd173e952e27d4aa4b933
URL:		http://quvi.sourceforge.net/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	curl-devel >= 7.18.2
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.24
BuildRequires:	json-glib-devel >= 0.12
BuildRequires:	libquvi-devel >= 0.9
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	curl-libs >= 7.18.2
Requires:	glib2 >= 1:2.24
Requires:	json-glib >= 0.12
Requires:	libquvi >= 0.9
Requires:	libxml2 >= 1:2.7.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
quvi is a command line tool for parsing video download links. It
supports YouTube and other similar video websites.

%description -l pl.UTF-8
quvi to narzędzie linii poleceń do analizy odnośników do pobierania
filmów flashowych. Obsługuje YouTube i inne podobne serwisy WWW.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/quvi
%{_mandir}/man1/quvi.1*
%{_mandir}/man1/quvi-dump.1*
%{_mandir}/man1/quvi-get.1*
%{_mandir}/man1/quvi-info.1*
%{_mandir}/man1/quvi-scan.1*
%{_mandir}/man5/quvirc.5*
