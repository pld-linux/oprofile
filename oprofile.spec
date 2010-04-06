Summary:	System-wide profiler
Summary(pl.UTF-8):	Ogólnosystemowy profiler
Name:		oprofile
Version:	0.9.4
Release:	12
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/oprofile/%{name}-%{version}.tar.gz
# Source0-md5:	82b059379895cf125261d7d773465915
Patch0:		%{name}-fortify.patch
Patch1:		%{name}-basename.patch
URL:		http://oprofile.sourceforge.net/
# not used directly, but build fails without it
BuildRequires:	autoconf
BuildRequires:	binutils-devel
BuildRequires:	popt-devel
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.217
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

%package gui
Summary:	GUI for OProfile
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do OProfile
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gui
GUI for OProfile.

%description gui -l pl.UTF-8
Graficzny interfejs użytkownika do OProfile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-kernel-support \
	--with-qt-includes=%{_includedir}/qt

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
%doc ChangeLog README TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%exclude  %{_bindir}/oprof_start
%dir %{_libdir}/oprofile
%attr(755,root,root) %{_libdir}/oprofile/lib*.so.*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
%dir %{_var}/lib/oprofile

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oprof_start
