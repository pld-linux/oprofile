# TODO:
# - java agents
# Warning: The user account 'oprofile:oprofile' does not exist on the system.
#         To profile JITed code, this special user account must exist.
#         Please ask your system administrator to add the following user and group:
#               user name : 'oprofile'
#               group name: 'oprofile'
#             The 'oprofile' group must be the default group for the 'oprofile' user.
#
Summary:	System-wide profiler
Summary(pl.UTF-8):	Ogólnosystemowy profiler
Name:		oprofile
Version:	1.4.0
Release:	10
License:	GPL v2 (oprofile), LGPL v2.1+ (libopagent)
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/oprofile/%{name}-%{version}.tar.gz
# Source0-md5:	ac0ff685ec9735e30d6a4d19de0efed7
Patch0:		gcc14.patch
URL:		http://oprofile.sourceforge.net/
# not used directly, but build fails without it
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	binutils-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	linux-libc-headers >= 7:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.217
Requires:	uname(release) >= 2.6.31
Conflicts:	kernel < 2.6.31
ExclusiveArch:	alpha %{arm} %{ix86} ia64 mips ppc ppc64 %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	oprofile_arch	%(echo "%{_target_base_arch}" | sed -e 's#x86_64#x86-64#')

%description
It consists of a kernel driver and a daemon for collecting sample
data, and several post-profiling tools for turning data into
information.

OProfile leverages the hardware performance counters of the CPU to
enable profiling of a wide variety of interesting statistics, which
can also be used for basic time-spent profiling. All code is profiled:
hardware and software interrupt handlers, kernel modules, the kernel,
shared libraries, and applications.

%description -l pl.UTF-8
Pakiet składa się ze sterownika dla jądra oraz demona zbierającego
próbki danych, a także kilku narzędzi do postprocesingu,
przekształcających dane na informacje.

OProfile utrzymuje liczniki wydajności sprzętu dla CPU, aby umożliwić
profilowanie wielorakich interesujących statystyk, których można
używać także do podstawowego profilowania czasu wykonywania.
Profilowany jest cały kod: procedury obsługi przerwań sprzętowych i
programowych, moduły jądra, jądro, biblioteki współdzielone oraz
aplikacje.

%package devel
Summary:	Header file for libopagent library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libopagent
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libopagent library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libopagent.

%package static
Summary:	Static libopagent library
Summary(pl.UTF-8):	Statyczna biblioteka libopagent
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libopagent library.

%description static -l pl.UTF-8
Statyczna biblioteka libopagent.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_var}/lib/oprofile

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ "$1" = 0 ]; then
	%{_bindir}/opcontrol --shutdown 2>/dev/null 1>&2
	rm -rf %{_var}/lib/oprofile/*
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog* README TODO doc/*.html doc/*.png doc/*.xsd
%attr(755,root,root) %{_bindir}/ocount
%attr(755,root,root) %{_bindir}/op-check-perfevents
%attr(755,root,root) %{_bindir}/opannotate
%attr(755,root,root) %{_bindir}/oparchive
%attr(755,root,root) %{_bindir}/operf
%attr(755,root,root) %{_bindir}/opgprof
%attr(755,root,root) %{_bindir}/ophelp
%attr(755,root,root) %{_bindir}/opimport
%attr(755,root,root) %{_bindir}/opjitconv
%attr(755,root,root) %{_bindir}/opreport
%dir %{_libdir}/oprofile
%attr(755,root,root) %{_libdir}/oprofile/libopagent.so.*.*.*
%attr(755,root,root) %{_libdir}/oprofile/libopagent.so.1
%{_datadir}/%{name}
%dir %{_var}/lib/oprofile
%{_mandir}/man1/op-check-perfevents.1*
%{_mandir}/man1/ocount.1*
%{_mandir}/man1/opannotate.1*
%{_mandir}/man1/oparchive.1*
%{_mandir}/man1/operf.1*
%{_mandir}/man1/opgprof.1*
%{_mandir}/man1/ophelp.1*
%{_mandir}/man1/opimport.1*
%{_mandir}/man1/opjitconv.1*
%{_mandir}/man1/opreport.1*
%{_mandir}/man1/oprofile.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/oprofile/libopagent.so
%{_libdir}/oprofile/libopagent.la
%{_includedir}/opagent.h

%files static
%defattr(644,root,root,755)
%{_libdir}/oprofile/libopagent.a
