%define fname   elib
%define elibdir %{_datadir}/emacs/site-lisp/%{fname}

Name:           emacs-%{fname}
Version:        1.0
Release:        %mkrel 12
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


%postun
%_remove_install_info %{fname}.info

%files
%defattr(-,root,root)
%doc ChangeLog COPYING INSTALL NEWS README RELEASING TODO
%{elibdir}
%{_infodir}/*info*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.0-12mdv2011.0
+ Revision: 618049
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0:1.0-11mdv2010.0
+ Revision: 428556
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:1.0-10mdv2009.0
+ Revision: 244698
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0:1.0-8mdv2008.1
+ Revision: 136403
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild

* Mon Sep 10 2007 David Walluck <walluck@mandriva.org> 0:1.0-7mdv2008.0
+ Revision: 83983
- rebuild
- Import emacs-elib



* Fri Sep 08 2006 David Walluck <walluck@mandriva.org> 0:1.0-6mdv2007.0
- rebuild
- bunzip2 patch
- version elib provides
- use macros

* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-5mdk
- rebuild for new emacs

* Fri Sep 03 2004 David Walluck <walluck@mandrake.org> 0:1.0-4mdk
- rebuild

* Mon Apr 28 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0-3mdk
- fixed dir ownership (Olivier Thauvin <thauvin@aerov.jussieu.fr>)

* Fri Apr 25 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0-2mdk
- fixed buildrequires (Stefan van der Eijk <stefan@eijk.nu>)

* Sun Mar 23 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0-1mdk
- contributed by David Walluck <david@anti-microsoft.org
