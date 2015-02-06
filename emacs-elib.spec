%define fname   elib
%define elibdir %{_datadir}/emacs/site-lisp/%{fname}

Name:           emacs-%{fname}
Version:        1.0
Release:        15
Epoch:          0
Summary:        Emacs Lisp Library
Requires:       emacs >= 0:20.7
License:        GPL
URL:            http://jdee.sunsite.dk/
Source:         http://jdee.sunsite.dk/%{fname}-%{version}.tar.bz2
Patch0:         emacs-elib-1.0-direntry.patch
Patch1:		emacs-elib-1.0-texi.patch
Group:          Editors
Obsoletes:      elib < %{epoch}:%{version}-%{release}
Provides:       elib = %{epoch}:%{version}-%{release}
BuildArch:      noarch
BuildRequires:  emacs-bin
BuildRequires:  texinfo

%description
The Emacs Lisp Library.

%prep
%setup -q -n %{fname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%make

%install
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/%{fname}
%{__mkdir_p} %{buildroot}{%{elibdir},%{_infodir}}

%{__install} -m 644 *.el *.elc %{buildroot}%{elibdir}
%{__install} -m 644 *.info* %{buildroot}%{_infodir}

%files
%doc ChangeLog COPYING INSTALL NEWS README RELEASING TODO
%{elibdir}
%{_infodir}/*info*


