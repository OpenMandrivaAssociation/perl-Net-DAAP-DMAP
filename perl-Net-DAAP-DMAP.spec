%define realname Net-DAAP-DMAP

Summary: Perl module for reading and writing DAAP structures
Name: perl-Net-DAAP-DMAP
Version: 1.26
Release: %mkrel 3
License: Artistic/GPL
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-DAAP-DMAP/
Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Net-DAAP-DMAP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Perl module for reading and writing DAAP structures.

%prep
%setup -q -n %{realname}-%{version}

%build
yes y | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

#check
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DAAP/DMAP.pm
