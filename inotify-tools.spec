
%define name	inotify-tools
%define lname	inotifytools
%define version	3.13
%define rel	3
%define major	0

%define libname	%mklibname %lname %major
%define devname	%mklibname %lname -d

Summary:	Simple interface to inotify
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
URL:		http://inotify-tools.sourceforge.net/
Source:		http://downloads.sourceforge.net/inotify-tools/inotify-tools-%{version}.tar.gz
License:	LGPLv2.1+
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-root
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

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mv %{buildroot}%{_docdir}/%{name} api

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so

