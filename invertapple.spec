%define		oname	InvertApple

Name:		invertapple
Version:	1.0
Release:	%mkrel 1
Summary:	Puzzle game about inverting apple colors
Group:		Games/Puzzles
License:	GPLv3+
URL:		http://qt-apps.org/content/show.php/ipQalc?content=107286
Source0:	%{oname}-%{version}.tar.gz
Source1:	%{oname}-icon.png
Patch0:		InvertApple-1.0-datapath.patch
BuildRequires:	qt4-devel
BuildRequires:	imagemagick

%description
Puzzle game in which you need to turn all red apples on the playing
field to green.

%prep
%setup -q -n %{oname}
%patch0 -p1

%build
%qmake_qt4 %{oname}.pro
%make

%install
%__rm -rf %{buildroot}

# install binary
%__mkdir_p %{buildroot}%{_gamesbindir}
%__cp Bin/%{oname} %{buildroot}%{_gamesbindir}/%{name}

# install locales
%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}
%__cp Bin/*.qm %{buildroot}%{_gamesdatadir}/%{name}/

# install records file
%__mkdir_p %{buildroot}%{_var}/games/%{name}/
%__cp Bin/records.xml %{buildroot}%{_var}/games/%{name}/

# create and install icons
for N in 16 32 48 64 128; do convert %{SOURCE1} -scale ${N}x${N}! $N.png; done
%__install -D 16.png -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D 32.png -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D 48.png -m 644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D 64.png -m 644 %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D 128.png -m 644 %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# XDG menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=Invert Apple
Comment=Puzzle game
Icon=%{name}
Exec=%{_gamesbindir}/%{name}
Terminal=false
Categories=Game;LogicGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%dir %{_var}/games/%{name}
%attr(666,root,root) %{_var}/games/%{name}/records.xml

