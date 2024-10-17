%define modname	XML-LibXSLT
%define modver 1.96

Summary:	Perl interface to the gnome libxslt library

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.gz
BuildRequires:	gdbm-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	perl(XML::LibXML) >= 1.59
BuildRequires:	perl-devel
Requires:	perl(XML::LibXML) >= 1.59

%description
This module is a fast XSLT library, based on the Gnome libxslt engine.

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" LIBS="-llibxslt"
%make_build

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README example/*
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/XML
%{_mandir}/man3/*
