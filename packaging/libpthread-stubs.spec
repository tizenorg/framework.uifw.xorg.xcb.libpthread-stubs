
Name:       libpthread-stubs
Summary:    PThread Stubs for XCB
Version:    0.3
Release:    2.8
Group:      System/X11
License:    MIT
URL:        http://xcb.freedesktop.org
Source0:    http://xcb.freedesktop.org/dist/libpthread-stubs-%{version}.tar.bz2

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
PThread Stubs for XCB



%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/pthread-stubs.pc


%changelog
* Sat Feb 27 2010 Anas Nashif <anas.nashif@intel.com> - 0.3
- Updated with latest spectacle
- Include YAML file in source rpm
* Mon Feb  8 2010 Austin Zhang <austin.zhang@intel.com> 0.3
- update to 0.3
* Wed Nov 26 2008 Peng Li <peng.li@intel.com> 0.1
- initial import libpthread-stubs 0.1
