%define lname	inotifytools
%define major	0
# Rust release builds do not leave a debugsource manifest.
%define _empty_manifest_terminate_build 0

%define oldlibname	%mklibname %lname 0
%define libname	%mklibname %lname
%define devname	%mklibname %lname -d

Summary:	Simple interface to inotify
Name:		inotify-tools
Version:	4.26.270
Release:	1
URL:		https://github.com/inotify-tools/inotify-tools/
Source0:	https://github.com/inotify-tools/inotify-tools/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz
License:	GPLv2
Group:		File tools
BuildRequires:	cargo
BuildRequires:	rust
BuildRequires:	make
BuildRequires:	gcc

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
%autosetup -p1 -a 1

cp README.md README
mkdir -p .cargo
cat > .cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%make_build prefix=%{_prefix} libdir=%{_libdir} ENABLE_STATIC=0 CARGOFLAGS="--offline --locked"

%install
%make_install prefix=%{_prefix} libdir=%{_libdir} ENABLE_STATIC=0 CARGOFLAGS="--offline --locked"

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
%doc AUTHORS ChangeLog NEWS
%{_includedir}/inotifytools
%{_libdir}/*.so
