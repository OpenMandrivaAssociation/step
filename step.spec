%define eigen_version 2.0.3

Name: step
Summary: Interactive physical simulator
Version: 4.7.80
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://edu.kde.org/step/
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: pkgconfig(eigen2) >= %eigen_version
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(gsl)

%description
Step is an interactive physical simulator. It works like this: 
you place some bodies on the scene, add some forces such as gravity 
or springs, then click "Simulate" and Step shows you how your scene 
will evolve according to the laws of physics. You can change every 
property of bodies/forces in your experiment (even during simulation) 
and see how this will change evolution of the experiment. With Step 
you can not only learn but feel how physics works !

%files
%doc README AUTHORS ChangeLog COPYING COPYING.DOC DESIGN TODO
%_kde_bindir/step
%_kde_datadir/applications/kde4/step.desktop                      
%_kde_appsdir/step
%_kde_datadir/config.kcfg/step.kcfg
%_kde_datadir/config/step.knsrc
%_kde_docdir/HTML/en/step
%_kde_iconsdir/hicolor/*/apps/step.png

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

