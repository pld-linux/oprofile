#
# Conditional build:
%bcond_with	qt3	# Qt 3 instead of Qt 4
%bcond_without	gui	# no Qt-based GUI
#
Summary:	System-wide profiler
Summary(pl.UTF-8):	Ogólnosystemowy profiler
Name:		oprofile
Version:	0.9.7
Release:	5
License:	GPL v2 (oprofile), LGPL v2.1+ (libopagent)
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/oprofile/%{name}-%{version}.tar.gz
# Source0-md5:	8b5d1d9b65f84420bcc3234777ad3be3
URL:		http://oprofile.sourceforge.net/
# not used directly, but build fails without it
BuildRequires:	autoconf
BuildRequires:	binutils-devel
BuildRequires:	libstdc++-devel
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.217
%if %{with gui}
%if %{with qt3}
BuildRequires:	qt-devel >= 3.0
%else
BuildRequires:	Qt3Support-devel >= 4
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	qt4-build >= 4
%endif
%endif
Requires:	uname(release) >= 2.6
Conflicts:	kernel < 2.6
ExclusiveArch:	alpha arm %{ix86} ia64 mips ppc ppc64 %{x8664}
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

%package gui
Summary:	Qt-based GUI for OProfile
Summary(pl.UTF-8):	Oparty na Qt graficzny interfejs użytkownika do OProfile
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gui
Qt-based GUI for OProfile.

%description gui -l pl.UTF-8
Oparty na Qt graficzny interfejs użytkownika do OProfile.

%prep
%setup -q

%build
%configure \
	--enable-gui%{?with_gui:%{!?with_qt3:=qt4}}%{!?with_gui:=no} \
	--with-kernel-support \
	%{?with_qt3:--with-qt-includes=%{_includedir}/qt}

%{__make} \
	%{?with_gui:%{!?with_qt3:UIC=uic3}}

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
%doc ChangeLog* README TODO doc/*.html
%attr(755,root,root) %{_bindir}/opannotate
%attr(755,root,root) %{_bindir}/oparchive
%attr(755,root,root) %{_bindir}/opcontrol
%attr(755,root,root) %{_bindir}/opgprof
%attr(755,root,root) %{_bindir}/ophelp
%attr(755,root,root) %{_bindir}/opimport
%attr(755,root,root) %{_bindir}/opjitconv
%attr(755,root,root) %{_bindir}/opreport
%attr(755,root,root) %{_bindir}/oprofiled
%exclude  %{_bindir}/oprof_start
%dir %{_libdir}/oprofile
%attr(755,root,root) %{_libdir}/oprofile/libopagent.so.*.*.*
%attr(755,root,root) %{_libdir}/oprofile/libopagent.so.1
%{_datadir}/%{name}
%dir %{_var}/lib/oprofile
%{_mandir}/man1/opannotate.1*
%{_mandir}/man1/oparchive.1*
%{_mandir}/man1/opcontrol.1*
%{_mandir}/man1/opgprof.1*
%{_mandir}/man1/ophelp.1*
%{_mandir}/man1/opimport.1*
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

%if %{with gui}
%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oprof_start
%endif
