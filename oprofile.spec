Summary:	System-wide profiler
Summary(pl):	Ogólnosystemowy profiler
Name:		oprofile
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/oprofile/%{name}-%{version}.tar.gz
# Source0-md5:	de7c5fd12b339e5c6eecb714ea823977
URL:		http://oprofile.sourceforge.net/
BuildRequires:	popt-devel
BuildRequires:	qt-devel
# Requires:	kernel >= 2.6
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
u¿ywaæ tak¿e do podstawowego profilowania czasu wykonywania. Profilowany
jest ca³y kod: procedury obs³ugi przerwañ sprzêtowych i programowych,
modu³y j±dra, j±dro, biblioteki wspó³dzielone oraz aplikacje.

%package gui
Summary:	GUI for OProfile
Summary(pl):	Graficzny interfejs u¿ytkownika do OProfile
Group:		X11/Applications
Requires:	%{name} = %{version}

%description gui
GUI for OProfile.

%description gui -l pl
Graficzny interfejs u¿ytkownika do OProfile.

%prep
%setup -q

%build
%configure \
	--with-kernel-support \
	--with-qt-includes=/usr/include/qt

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
%attr(755,root,root) %{_bindir}/op_help
%attr(755,root,root) %{_bindir}/opannotate
%attr(755,root,root) %{_bindir}/opcontrol
%attr(755,root,root) %{_bindir}/opgprof
%attr(755,root,root) %{_bindir}/opreport
%attr(755,root,root) %{_bindir}/oprofiled
# XXX: keep only %{arch}-specific data?
%{_datadir}/oprofile
%{_mandir}/man1/*.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oprof_start
