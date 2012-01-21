%define upstream_name    XML-LibXSLT
%define upstream_version 1.70

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    Perl interface to the gnome libxslt library
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  libgdbm-devel
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
