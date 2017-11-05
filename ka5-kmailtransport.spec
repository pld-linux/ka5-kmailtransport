%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		kmailtransport
Summary:	KMail Transport
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	841483d2ea69d7164c25547e9142ed95
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMail Transport.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
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
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kmailtransport.categories
/etc/xdg/kmailtransport.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5MailTransport.so.5
%attr(755,root,root) %{_libdir}/libKF5MailTransport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5MailTransportAkonadi.so.5
%attr(755,root,root) %{_libdir}/libKF5MailTransportAkonadi.so.*.*.*
%{_libdir}/qt5/plugins/kcm_mailtransport.so
%{_libdir}/qt5/plugins/kf5/kio/smtp.so
%dir %{_libdir}/qt5/plugins/mailtransport
%{_libdir}/qt5/plugins/mailtransport/mailtransport_akonadiplugin.so
%{_libdir}/qt5/plugins/mailtransport/mailtransport_smtpplugin.so
%{_datadir}/config.kcfg/mailtransport.kcfg
%{_datadir}/kservices5/kcm_mailtransport.desktop
%{_datadir}/kservices5/smtp.protocol
%{_datadir}/kservices5/smtps.protocol

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
%attr(755,root,root) %{_libdir}/libKF5MailTransport.so
%attr(755,root,root) %{_libdir}/libKF5MailTransportAkonadi.so
%{_libdir}/qt5/mkspecs/modules/qt_KMailTransport.pri
%{_libdir}/qt5/mkspecs/modules/qt_KMailTransportAkonadi.pri
