#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmailtransport
Summary:	KMail Transport
Name:		ka5-%{kaname}
Version:	23.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f63d37a0827527847d5e3a5013dd1dde
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Keychain-devel >= 0.12.0
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 3.20
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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


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
%{_datadir}/config.kcfg/mailtransport.kcfg
%{_datadir}/qlogging-categories5/kmailtransport.categories
%{_datadir}/qlogging-categories5/kmailtransport.renamecategories
%dir %{_libdir}/qt5/plugins/pim5/mailtransport
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/mailtransport/mailtransport_smtpplugin.so
%ghost %{_libdir}/libKPim5MailTransport.so.5
%attr(755,root,root) %{_libdir}/libKPim5MailTransport.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/qt5/mkspecs/modules/qt_KMailTransport.pri
%{_includedir}/KPim5/MailTransport
%{_libdir}/cmake/KF5MailTransport
%{_libdir}/cmake/KPim5MailTransport
%{_libdir}/libKPim5MailTransport.so
