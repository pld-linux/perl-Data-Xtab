%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Xtab
Summary:	Data::Xtab - Pivot (cross-tabulate) a table of data.
Name:		perl-Data-Xtab
Version:	1.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to feed it tables of data to be pivoted in such
a way that they can be easily used in a report or graph. Here is an
example of input data:

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Data/Xtab.pm
%{_mandir}/man3/*
