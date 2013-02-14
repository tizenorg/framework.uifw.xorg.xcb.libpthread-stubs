#sbs-git:slp/pkgs/xorg/xcb/libpthread-stubs libpthread-stubs 0.3 ce726f595116dd79d38db013c49c113555b1a15d

Name:       libpthread-stubs
Summary:    PThread Stubs for XCB
Version: 0.3
Release:    2.8
Group:      System/X11
License:    MIT
URL:        http://xcb.freedesktop.org
Source:    %{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
PThread Stubs for XCB



%prep
%setup -q

%build

%configure --disable-static
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
%make_install




%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/pthread-stubs.pc
/usr/share/license/%{name}