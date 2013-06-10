Summary:	Graphical User Interface tool supporting SpatiaLite
Summary(pl.UTF-8):	Graficzny interfejs użytkownika obsługujący bazy SpatiaLite
Name:		spatialite_gui
Version:	1.7.0
Release:	1
License:	GPL v3+
Group:		Applications/Databases
Source0:	http://www.gaia-gis.it/gaia-sins/spatialite-gui-sources/%{name}-%{version}.tar.gz
# Source0-md5:	34fd2c3fb60c7460de979f8d34d853a4
URL:		https://www.gaia-gis.it/fossil/spatialite_gui
BuildRequires:	freexl-devel
BuildRequires:	geos-devel
BuildRequires:	libgaiagraphics-devel
BuildRequires:	libspatialite-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 4
BuildRequires:	wxGTK2-unicode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical User Interface tool supporting SpatiaLite.

%description -l pl.UTF-8
Graficzny interfejs użytkownika obsługujący bazy SpatiaLite.

%prep
%setup -q

mkdir wx-bin
ln -sf /usr/bin/wx-gtk2-unicode-config wx-bin/wx-config

%build
# configure refers to wx-config with no option to override
PATH=$(pwd)/wx-bin:$PATH
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
sed -ne '2,$p' gnome_resource/spatialite-gui.desktop >$RPM_BUILD_ROOT%{_desktopdir}/spatialite-gui.desktop
cp -p gnome_resource/spatialite-gui.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spatialite_gui
%{_desktopdir}/spatialite-gui.desktop
%{_pixmapsdir}/spatialite-gui.png
