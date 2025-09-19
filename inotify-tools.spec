%define lname	inotifytools
%define major	0

%define oldlibname	%mklibname %lname 0
%define libname	%mklibname %lname
%define devname	%mklibname %lname -d

Summary:	Simple interface to inotify
Name:		inotify-tools
Version:	4.25.9.0
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
%rename %{oldlibname}

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
%autosetup -p1

cp README.md README

%build
#export CC=gcc
#export CXX=g++
autoreconf -vfi
%configure --disable-static

%make_build

%install
%make_install

mv %{buildroot}%{_docdir}/%{name} api

%files
%defattr(-,root,root)
%doc README
%{_bindir}/inotifywait
%{_bindir}/inotifywatch
%{_bindir}/fsnotifywait
%{_bindir}/fsnotifywatch
%{_mandir}/man1/inotifywait.1*
%{_mandir}/man1/inotifywatch.1*
%{_mandir}/man1/fsnotifywait.1.*
%{_mandir}/man1/fsnotifywatch.1.*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS api
%{_includedir}/inotifytools
%{_libdir}/*.so
