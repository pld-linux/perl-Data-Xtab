#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Xtab
Summary:	Data::Xtab - pivot (cross-tabulate) a table of data
Summary(pl):	Data::Xtab - obracanie tabel z danymi
Name:		perl-Data-Xtab
Version:	1.01
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2056f54082c33f72538606d3038a068a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to feed it tables of data to be pivoted in such
a way that they can be easily used in a report or graph.

%description -l pl
Ten modu� pozwala na przekazanie tabeli danych, kt�ra jest obracana w
ten spos�b, �e mo�e by� �atwo u�yta w raporcie lub do wykresu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Data/Xtab.pm
%{_mandir}/man3/*
