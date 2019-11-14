%define lname	inotifytools
%define major	0

%define libname	%mklibname %lname %major
%define devname	%mklibname %lname -d

Summary:	Simple interface to inotify
Name:		inotify-tools
Version:	3.20.1
Release:	1
URL:		https://github.com/rvoicilas/inotify-tools/
Source0:	https://github.com/rvoicilas/inotify-tools/archive/%{version}/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		File tools
BuildRequires:	doxygen

%description
This is a package of some commandline utilities relating to inotify.

The general purpose of this package is to allow inotify's features
to be used from within shell scripts.  Read the man pages for
further details.

%package -n	%{libname}
Summary:	Inotify interface library
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with libinotifytools.

%package -n	%{devname}
Summary:	Development files for inotifytools
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{lname}-devel = %{version}-%{release}

%description -n	%{devname}
Development files for inotifytools.

%prep
%setup -q
%autopatch -p1

%build
export CC=gcc
export CXX=g++
autoreconf -vfi
%configure --disable-static

%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

mv %{buildroot}%{_docdir}/%{name} api

%files
%defattr(-,root,root)
%doc README
%{_bindir}/inotifywait
%{_bindir}/inotifywatch
%{_mandir}/man1/inotifywait.1*
%{_mandir}/man1/inotifywatch.1*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS api
%{_includedir}/inotifytools
%{_libdir}/*.so



%changelog
* Wed Oct 26 2011 Alexander Khrukin <akhrukin@mandriva.org> 3.14-1mdv2012.0
+ Revision: 707323
- updated to upstream release

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.13-4mdv2011.0
+ Revision: 619633
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.13-3mdv2010.0
+ Revision: 429512
- rebuild

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 3.13-2mdv2009.0
+ Revision: 217205
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jan 03 2008 Anssi Hannula <anssi@mandriva.org> 3.13-2mdv2008.1
+ Revision: 141085
- more devel provides

* Thu Jan 03 2008 Anssi Hannula <anssi@mandriva.org> 3.13-1mdv2008.1
+ Revision: 140931
- initial Mandriva release

