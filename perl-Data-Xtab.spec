%include	/usr/lib/rpm/macros.perl
Summary:	Data-Xtab perl module
Summary(pl):	Modu� perla Data-Xtab
Name:		perl-Data-Xtab
Version:	1.01
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-Xtab-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-Xtab perl module.

%description -l pl
Modu� perla Data-Xtab.

%prep
%setup -q -n Data-Xtab-%{version}

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
