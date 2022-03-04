%define		kdeappsver	21.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kmailtransport
Summary:	KMail Transport
Name:		ka5-%{kaname}
Version:	21.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	72679b35f460a466f47b2f1a6a658f62
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Keychain-devel >= 0.12.0
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-ksmtp-devel >= %{kdeappsver}
BuildRequires:	ka5-ksmtp-devel >= %{kdeappsver}
BuildRequires:	ka5-libkgapi-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail transport service.

%description -l pl.UTF-8
Usługa przesyłania poczty elektronicznej.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5MailTransport.so.5
%attr(755,root,root) %{_libdir}/libKF5MailTransport.so.*.*.*
%ghost %{_libdir}/libKF5MailTransportAkonadi.so.5
%attr(755,root,root) %{_libdir}/libKF5MailTransportAkonadi.so.*.*.*
%{_libdir}/qt5/plugins/kcm_mailtransport.so
%dir %{_libdir}/qt5/plugins/mailtransport
%{_libdir}/qt5/plugins/mailtransport/mailtransport_akonadiplugin.so
%{_libdir}/qt5/plugins/mailtransport/mailtransport_smtpplugin.so
%{_datadir}/config.kcfg/mailtransport.kcfg
%{_datadir}/kservices5/kcm_mailtransport.desktop
%{_datadir}/qlogging-categories5/kmailtransport.categories
%{_datadir}/qlogging-categories5/kmailtransport.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/MailTransport
%{_includedir}/KF5/MailTransportAkonadi
%{_includedir}/KF5/mailtransport
%{_includedir}/KF5/mailtransport_version.h
%{_includedir}/KF5/mailtransportakonadi
%{_includedir}/KF5/mailtransportakonadi_version.h
%{_libdir}/cmake/KF5MailTransport
%{_libdir}/cmake/KF5MailTransportAkonadi
%{_libdir}/libKF5MailTransport.so
%{_libdir}/libKF5MailTransportAkonadi.so
%{_libdir}/qt5/mkspecs/modules/qt_KMailTransport.pri
%{_libdir}/qt5/mkspecs/modules/qt_KMailTransportAkonadi.pri
