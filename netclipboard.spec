# TODO: optflags
Summary:	Transparent cross-platform clipboard synchronization
Summary(pl.UTF-8):	Przezroczysta, wieloplatformowa synchronizacja schowka
Name:		netclipboard
Version:	0.60
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/netclipboard/%{name}-%{version}.tar
# Source0-md5:	c59fbf9e44bc838bb5e5973c5c01efb6
URL:		http://netclipboard.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Transparent cross-platform clipboard synchronization.

%description -l pl.UTF-8
Przezroczysta, wieloplatformowa synchronizacja schowka.

%prep
%setup -q -n %{name}

%build
qmake
QTDIR=/usr %{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install netclip $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING-EXCEPTION README
%attr(755,root,root) %{_bindir}/*
