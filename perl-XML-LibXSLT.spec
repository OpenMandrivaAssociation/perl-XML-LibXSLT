%define modname	XML-LibXSLT
%define modver	1.80

Summary:	Perl interface to the gnome libxslt library
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.gz
BuildRequires:	gdbm-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	perl(XML::LibXML) >= 1.59
BuildRequires:	perl-devel
Requires:	perl(XML::LibXML) >= 1.59

%description
This module is a fast XSLT library, based on the Gnome libxslt engine.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README example/*
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/XML
%{_mandir}/man3/*

