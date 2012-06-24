Summary:	Command line tool for parsing flash video download links
Name:		quvi
Version:	0.4.2
Release:	1
License:	LGPL v2
Group:		Applications/WWW
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	66cb0dda70f2900c58c4b87b2d76007b
Patch0:		%{name}-automake-1.12.patch
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.10
BuildRequires:	curl-devel >= 7.18.2
BuildRequires:	libquvi-devel >= 0.4.0
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libquvi >= 0.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
quvi is a command line tool for parsing video download links. It
supports YouTube and other similar video websites.

%prep
%setup -q
%patch0 -p1

%build
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
%{_mandir}/man1/*.1*
