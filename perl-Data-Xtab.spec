%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Xtab
Summary:	Data::Xtab - Pivot (cross-tabulate) a table of data
Summary(pl):	Modu³ Data::Xtab - obracaj±cy tabele z danymi
Name:		perl-Data-Xtab
Version:	1.01
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2056f54082c33f72538606d3038a068a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to feed it tables of data to be pivoted in such
a way that they can be easily used in a report or graph.

%description -l pl
Ten modu³ pozwala na przekazanie tabeli danych, która jest obracana w
ten sposób, ¿e mo¿e byæ ³atwo u¿yta w raporcie lub do wykresu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Data/Xtab.pm
%{_mandir}/man3/*
