Summary:	System-wide profiler
Summary(pl):	Ogólnosystemowy profiler
Name:		oprofile
Version:	0.5.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/oprofile/%{name}-%{version}.tar.gz
# Source0-md5:	be655a8b09207ef8a47706ff23c9c0d8
URL:		http://oprofile.sourceforge.net/
BuildRequires:	popt-devel
BuildRequires:	qt-devel
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
u¿ywaæ tak¿e do podstawego profilowania czasu wykonywania. Profilowany
jest ca³y kod: procedury obs³ugi przerwañ sprzêtowych i programowych,
modu³y j±dra, j±dro, biblioteki wspó³dzielone oraz aplikacje.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
