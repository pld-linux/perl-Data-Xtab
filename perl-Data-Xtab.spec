%include	/usr/lib/rpm/macros.perl
Summary:	Data-Xtab perl module
Summary(pl):	Modu� perla Data-Xtab
Name:		perl-Data-Xtab
Version:	1.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-Xtab-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-Xtab perl module.

%description -l pl
Modu� perla Data-Xtab.

%prep
%setup -q -n Data-Xtab-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Data/Xtab
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Data/Xtab.pm
%{perl_sitearch}/auto/Data/Xtab

%{_mandir}/man3/*