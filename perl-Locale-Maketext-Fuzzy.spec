%define upstream_name    Locale-Maketext-Fuzzy
%define upstream_version 0.11
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.11
Release:	3

Summary:	Maketext from already interpolated strings 
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AU/AUDREYT/Locale-Maketext-Fuzzy-0.11.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module is a subclass of Locale::Maketext, with additional support for 
localizing messages that already contains interpolated variables. 
This is most useful when the messages are returned by external modules 
-- for example, to match 
  dir: command not found 
against 
  [_1]: command not found.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 406068
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 257644
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 245699
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 0.10-1mdv2008.1
+ Revision: 100860
- New version 0.10

* Thu Jun 21 2007 Michael Scherer <misc@mandriva.org> 0.02-3mdv2008.0
+ Revision: 41999
- rebuild


* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 0.02-2mdk
- Do not ship empty dir

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 0.02-1mdk
- First mandriva package


