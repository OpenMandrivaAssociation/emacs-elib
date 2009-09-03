%define fname   elib
%define elibdir %{_datadir}/emacs/site-lisp/%{fname}

Name:           emacs-%{fname}
Version:        1.0
Release:        %mkrel 11
Epoch:          0
Summary:        Emacs Lisp Library
Requires:       emacs >= 0:20.7
License:        GPL
URL:            http://jdee.sunsite.dk/
Source:         http://jdee.sunsite.dk/%{fname}-%{version}.tar.bz2
Patch:          emacs-elib-1.0-direntry.patch
Group:          Editors
Obsoletes:      elib < %{epoch}:%{version}-%{release}
Provides:       elib = %{epoch}:%{version}-%{release}
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  emacs-bin
BuildRequires:  texinfo

%description
The Emacs Lisp Library.

%prep
%setup -q -n %{fname}-%{version}
%patch -p1

%build
%{make}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/%{fname}
%{__mkdir_p} %{buildroot}{%{elibdir},%{_infodir}}

%{__install} -m 644 *.el *.elc %{buildroot}%{elibdir}
%{__install} -m 644 *.info* %{buildroot}%{_infodir}

%clean
%{__rm} -rf %{buildroot}

%post
%_install_info %{fname}.info

%postun
%_remove_install_info %{fname}.info

%files
%defattr(-,root,root)
%doc ChangeLog COPYING INSTALL NEWS README RELEASING TODO
%{elibdir}
%{_infodir}/*info*
