Summary:	Graphical User Interface tool supporting SpatiaLite
Summary(pl.UTF-8):	Graficzny interfejs użytkownika obsługujący bazy SpatiaLite
Name:		spatialite_gui
%define	beta	beta1
Version:	2.1.0
Release:	0.%{beta}.3
License:	GPL v3+
Group:		Applications/Databases
Source0:	http://www.gaia-gis.it/gaia-sins/spatialite-gui-sources/%{name}-%{version}-%{beta}.tar.gz
# Source0-md5:	9e8157f68c1f9ef77c31b229936b147f
URL:		https://www.gaia-gis.it/fossil/spatialite_gui
BuildRequires:	freexl-devel
BuildRequires:	geos-devel
BuildRequires:	libgaiagraphics-devel
BuildRequires:	libspatialite-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 4
BuildRequires:	sqlite3-devel
BuildRequires:	virtualpg-devel
BuildRequires:	wxGTK3-unicode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical User Interface tool supporting SpatiaLite.

%description -l pl.UTF-8
Graficzny interfejs użytkownika obsługujący bazy SpatiaLite.

%prep
%setup -q -n %{name}-%{version}-%{beta}

%build
%configure \
	--with-wxconfig=/usr/bin/wx-gtk3-unicode-config \
	--disable-xlsxwriter

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/40x40

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spatialite_gui
%{_desktopdir}/spatialite-gui.desktop
%{_iconsdir}/hicolor/*x*/apps/spatialite-gui.png
