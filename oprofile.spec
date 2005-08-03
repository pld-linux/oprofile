Summary:	System-wide profiler
Summary(pl):	Ogólnosystemowy profiler
Name:		oprofile
Version:	0.9.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/oprofile/%{name}-%{version}.tar.gz
# Source0-md5:	c25a05406e30e81a6afbd3264191fa37
URL:		http://oprofile.sourceforge.net/
BuildRequires:	popt-devel
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.217
Conflicts:	kernel < 2.6
ExclusiveArch:	alpha arm %{ix86} ia64 mips ppc ppc64 %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It consists of a kernel driver and a daemon for collecting sample
data, and several post-profiling tools for turning data into
information.

OProfile leverages the hardware performance counters of the CPU to
enable profiling of a wide variety of interesting statistics, which
can also be used for basic time-spent profiling. All code is profiled:
hardware and software interrupt handlers, kernel modules, the kernel,
shared libraries, and applications.

%description -l pl
Pakiet sk³ada siê ze sterownika dla j±dra oraz demona zbieraj±cego
próbki danych, a tak¿e kilku narzêdzi do postprocesingu,
przekszta³caj±cych dane na informacje.

OProfile utrzymuje liczniki wydajno¶ci sprzêtu dla CPU, aby umo¿liwiæ
profilowanie wielorakich interesuj±cych statystyk, których mo¿na
u¿ywaæ tak¿e do podstawowego profilowania czasu wykonywania.
Profilowany jest ca³y kod: procedury obs³ugi przerwañ sprzêtowych i
programowych, modu³y j±dra, j±dro, biblioteki wspó³dzielone oraz
aplikacje.

%package gui
Summary:	GUI for OProfile
Summary(pl):	Graficzny interfejs u¿ytkownika do OProfile
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gui
GUI for OProfile.

%description gui -l pl
Graficzny interfejs u¿ytkownika do OProfile.

%prep
%setup -q

%build
%configure \
	--with-kernel-support \
	--with-qt-includes=%{_includedir}/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%exclude  %{_bindir}/oprof_start
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{_target_base_arch}
%{_datadir}/%{name}/rtc
%{_datadir}/%{name}/stl.pat
%{_mandir}/man1/*.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oprof_start
