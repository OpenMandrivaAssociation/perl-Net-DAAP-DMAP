%define upstream_name    Net-DAAP-DMAP
%define upstream_version 1.27
Name:		perl-%{upstream_name}
Version:	1.27
Release:	1

Summary:	Perl module for reading and writing DAAP structures
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Net-DAAP-DMAP
Source0:	https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Net-DAAP-DMAP-1.27.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl module for reading and writing DAAP structures.

%prep
%setup -q -n %{upstream_name}-%{version}

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

