%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Interactive physical simulator
Name:		step
Version:	18.12.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/step/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Plotting)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(libqalculate)

%description
Step is an interactive physical simulator. It works like this:
you place some bodies on the scene, add some forces such as gravity
or springs, then click "Simulate" and Step shows you how your scene
will evolve according to the laws of physics. You can change every
property of bodies/forces in your experiment (even during simulation)
and see how this will change evolution of the experiment. With Step
you can not only learn but feel how physics works!

%files -f step.lang
%doc README AUTHORS ChangeLog COPYING COPYING.DOC DESIGN TODO
%{_datadir}/applications/org.kde.step.desktop
%{_bindir}/step
%{_sysconfdir}/xdg/step.knsrc
%{_datadir}/metainfo/org.kde.step.appdata.xml
%{_datadir}/config.kcfg/step.kcfg
%{_iconsdir}/hicolor/*/apps/step.png
%{_iconsdir}/hicolor/22x22/actions/step_object_*
%{_datadir}/step/examples/*
%{_datadir}/step/objinfo/*
%{_datadir}/step/tutorials/tutorial*
%{_iconsdir}/hicolor/22x22/actions/pointer.png
%{_datadir}/kxmlgui5/step/stepui.rc
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/step/step.js

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang step --with-html
TOP="$(pwd)"
cd %{buildroot}
find .%{_datadir}/locale -name "*.qm" |while read r; do
	echo "%%lang($(echo $r |cut -d/ -f5)) $(echo $r |cut -b2-)" >>${TOP}/step.lang
done
