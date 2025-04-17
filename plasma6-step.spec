%global optflags %{optflags} -Wno-missing-template-arg-list-after-template-kw
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Interactive physical simulator
Name:		plasma6-step
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/step/
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/step/-/archive/%{gitbranch}/step-%{gitbranchd}.tar.bz2#/step-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/step-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Plotting)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(Eigen3)
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
%autosetup -p1 -n step-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DEigen3_DIR=%{_datadir}/cmake/eigen \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang step --with-html --all-name
TOP="$(pwd)"
cd %{buildroot}
find .%{_datadir}/locale -name "*.qm" |while read r; do
	echo "%%lang($(echo $r |cut -d/ -f6)) $(echo $r |cut -b2-)" >>${TOP}/step.lang
done
for i in .%{_datadir}/step/tutorials/*; do
	echo $i |grep -qE '\.step$' && continue
	echo "%%lang($(basename $i)) %{_datadir}/step/tutorials/$(basename $i)" >>${TOP}/step.lang
done
