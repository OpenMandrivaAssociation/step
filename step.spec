%define eigen_version 2.0.3

Summary:	Interactive physical simulator
Name:		step
Version:	15.04.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/step/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(eigen2) >= %{eigen_version}
BuildRequires:	pkgconfig(libqalculate)

%description
Step is an interactive physical simulator. It works like this:
you place some bodies on the scene, add some forces such as gravity
or springs, then click "Simulate" and Step shows you how your scene
will evolve according to the laws of physics. You can change every
property of bodies/forces in your experiment (even during simulation)
and see how this will change evolution of the experiment. With Step
you can not only learn but feel how physics works!

%files
%doc README AUTHORS ChangeLog COPYING COPYING.DOC DESIGN TODO
%doc %{_kde_docdir}/HTML/en/step
%{_kde_applicationsdir}/step.desktop
%{_kde_appsdir}/step
%{_kde_bindir}/step
%{_kde_configdir}/step.knsrc
%{_kde_datadir}/appdata/step.appdata.xml
%{_kde_datadir}/config.kcfg/step.kcfg
%{_kde_iconsdir}/hicolor/*/apps/step.png

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
