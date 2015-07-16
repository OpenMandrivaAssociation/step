Summary:	Interactive physical simulator
Name:		step
Version:	15.04.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/step/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
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

%files
%doc README AUTHORS ChangeLog COPYING COPYING.DOC DESIGN TODO                                          
%doc %{_docdir}/HTML/en/step                                                                           
%{_datadir}/applications/kde4/step.desktop                                                             
%{_datadir}/apps/step                                                                                  
%{_bindir}/step                                                                                        
%{_datadir}/config/step.knsrc                                                                          
%{_datadir}/appdata/step.appdata.xml                                                                   
%{_datadir}/config.kcfg/step.kcfg                                                                      
%{_iconsdir}/hicolor/*/apps/step.png

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
