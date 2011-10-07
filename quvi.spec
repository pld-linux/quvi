#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Command line tool for parsing flash video download links
Name:		quvi
Version:	0.2.16.2
Release:	1
License:	LGPL v2
Group:		Applications/WWW
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	45ac7d1314d932970276c9ec46da66e2
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.10
BuildRequires:	curl-devel >= 7.18.0
BuildRequires:	doxygen
BuildRequires:	libtool >= 2:2.2
BuildRequires:	lua51-devel
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
quvi is a command line tool for parsing video download links. It
supports YouTube and other similar video websites.

%package devel
Summary:	Header files for quvi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki quvi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for quvi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki quvi.

%package static
Summary:	Static quvi library
Summary(pl.UTF-8):	Statyczna biblioteka quvi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static quvi library.

%description static -l pl.UTF-8
Statyczna biblioteka quvi.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/quvi

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog* NEWS README
%attr(755,root,root) %{_bindir}/quvi
%attr(755,root,root) %{_libdir}/libquvi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libquvi.so.0
%{_datadir}/quvi
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/libquvi.so
%{_includedir}/quvi
%{_pkgconfigdir}/libquvi.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libquvi.a
%endif
