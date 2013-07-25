%define upstream_name    Net-DAAP-DMAP
%define upstream_version 1.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.27
Release:	1

Summary:	Perl module for reading and writing DAAP structures
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/R/RC/RCLAMP/Net-DAAP-DMAP-1.27.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl module for reading and writing DAAP structures.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes y | perl Makefile.PL INSTALLDIRS=vendor
%make

#check
#make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DAAP/DMAP.pm

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.260.0-1mdv2010.0
+ Revision: 404068
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.26-4mdv2009.0
+ Revision: 258004
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.26-3mdv2009.0
+ Revision: 246057
- rebuild

* Sun Mar 23 2008 Stefan van der Eijk <stefan@mandriva.org> 1.26-1mdv2008.1
+ Revision: 189543
- spec file fixes
- fix Group
- import perl-Net-DAAP-DMAP



