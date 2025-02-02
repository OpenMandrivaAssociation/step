%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Interactive physical simulator
Name:		step
Version:	23.08.5
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/step/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	pkgconfig(shared-mime-info)
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
%doc README AUTHORS ChangeLog DESIGN TODO
%{_datadir}/applications/org.kde.step.desktop
%{_bindir}/step
%{_datadir}/knsrcfiles/step.knsrc
%{_datadir}/metainfo/org.kde.step.appdata.xml
%{_datadir}/config.kcfg/step.kcfg
%{_iconsdir}/hicolor/*/apps/step.png
%{_iconsdir}/hicolor/22x22/actions/step_object_*
%{_datadir}/mime/packages/org.kde.step.xml
%{_datadir}/step/examples/*
%{_datadir}/step/objinfo/*
%dir %{_datadir}/step/tutorials
%{_datadir}/step/tutorials/*.step
%{_iconsdir}/hicolor/22x22/actions/pointer.png
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/step/step.js

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang step --with-html --all-name
TOP="$(pwd)"
cd %{buildroot}
find .%{_datadir}/locale -name "*.qm" |while read r; do
	echo "%%lang($(echo $r |cut -d/ -f5)) $(echo $r |cut -b2-)" >>${TOP}/step.lang
done
for i in .%{_datadir}/step/tutorials/*; do
	echo $i |grep -qE '\.step$' && continue
	echo "%%lang($(basename $i)) %{_datadir}/step/tutorials/$(basename $i)" >>${TOP}/step.lang
done
