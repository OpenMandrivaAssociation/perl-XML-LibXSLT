%define upstream_name    XML-LibXSLT
%define upstream_version 1.77

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Perl interface to the gnome libxslt library
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  devel(libgdbm)
BuildRequires:  libxslt-devel
BuildRequires:  perl(XML::LibXML) >= 1.59
BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

Requires:       perl(XML::LibXML) >= 1.59

%description
This module is a fast XSLT library, based on the Gnome libxslt engine.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files 
%defattr(-,root,root)
%doc Changes README example/*
%{_mandir}/*/*
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/XML


%changelog
* Fri May 25 2012 Crispin Boylan <crisb@mandriva.org> 1.770.0-1
+ Revision: 800700
- New release

* Fri Feb 03 2012 Crispin Boylan <crisb@mandriva.org> 1.760.0-1
+ Revision: 770860
- New release

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.700.0-6
+ Revision: 765846
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.700.0-4
+ Revision: 667439
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.700.0-3mdv2011.0
+ Revision: 564595
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.700.0-2mdv2011.0
+ Revision: 556192
- rebuild for perl 5.12

* Sat Nov 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1.700.0-1mdv2010.1
+ Revision: 462463
- update to 1.70

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.680.0-1mdv2010.0
+ Revision: 408241
- rebuild using %%perl_convert_version

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.68-1mdv2009.1
+ Revision: 300655
- update to new version 1.68

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Feb 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.66-1mdv2008.1
+ Revision: 161177
- update to new version 1.66

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.63-2mdv2008.1
+ Revision: 152423
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.63-1mdv2008.1
+ Revision: 98010
- new version

