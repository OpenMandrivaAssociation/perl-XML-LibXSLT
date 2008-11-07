%define module  XML-LibXSLT
%define name    perl-%{module}
%define version 1.68
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl interface to the gnome libxslt library
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
Requires:       perl(XML::LibXML) >= 1.59
BuildRequires:  perl-devel
BuildRequires:  perl(XML::LibXML) >= 1.59
BuildRequires:  libxslt-devel
BuildRequires:  libgdbm-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module is a fast XSLT library, based on the Gnome libxslt engine.

%prep
%setup -q -n %{module}-%{version}

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


