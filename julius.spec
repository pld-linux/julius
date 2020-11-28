Summary:	An open source re-implementation of Caesar III
Name:		julius
Version:	1.5.1
Release:	1
License:	AGPL v3+
Group:		X11/Applications/Games
Source0:	https://github.com/bvschaik/julius/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4e21f6e2f49a88cb8b6c92afd9c368cc
URL:		https://github.com/bvschaik/julius
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	cmake >= 3.0.2
BuildRequires:	libpng-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Julius is a fully working open-source version of Caesar 3, with the
same logic as the original, but with some UI enhancements, that can be
played on multiple platforms.

%prep
%setup -q

%{__rm} -r ext/{SDL2,png,zlib}

%build
mkdir -p build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/julius
%{_desktopdir}/com.github.bvschaik.julius.desktop
%{_iconsdir}/hicolor/*x*/apps/com.github.bvschaik.julius.png
%{_datadir}/metainfo/com.github.bvschaik.julius.metainfo.xml
