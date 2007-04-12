%define realname   Locale-Maketext-Fuzzy

Name:		perl-%{realname}
Version:    0.02
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Maketext from already interpolated strings 
Source0:    http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch: noarch

%description
This module is a subclass of Locale::Maketext, with additional support for 
localizing messages that already contains interpolated variables. 
This is most useful when the messages are returned by external modules 
-- for example, to match 
  dir: command not found 
against 
  [_1]: command not found.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

