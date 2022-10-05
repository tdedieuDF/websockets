%global debug_package ${nil}

%define __python3 /usr/bin/python3.8

Name:           python3-websocket
Version:        10.3
Release:        0
Summary:        websocket package
Group:          Application/Network
License:        GPL
URL:            https://github.com/aaugustin/websockets
Vendor:         aaugustin
Source:         packagesource.tar.gz
Prefix:         %{_prefix}
Packager:       Dragonfly
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      x86_64
BuildRequires:  python38-devel, python38
Requires:       python38

%description
Websocket middleware

%prep
%setup -c .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --root %{buildroot}

%check
%{__python3} setup.py test

%files
%{python3_sitearch}/*

%changelog
* Wed Jul 06 2022 Dragonfly <dragonfly@upnext.com> - 10.3-0
- First package websocket

