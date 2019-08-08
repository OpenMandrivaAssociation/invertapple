Name:		invertapple
Version:	1.1.1
Release:	%mkrel 1
Summary:	Puzzle game about inverting apple colors
Group:		Games/Puzzles
License:	GPLv3+
URL:		http://dansoft.krasnokamensk.ru/more.html?id=1015
Source0:	https://bitbucket.org/admsasha/invertapple/downloads/%{name}-%{version}.tar.gz

BuildRequires:  qt5-linguist-tools
BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)


%description
Puzzle game in which you need to turn all red apples on the playing
field to green.

%prep
%setup -q

%build
%qmake_qt5
%make

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README* CONTRIBUTORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
