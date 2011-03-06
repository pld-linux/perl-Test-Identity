#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Identity
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Identity - assert the referential identity of a reference
Summary(pl.UTF-8):	Test::Identity - sprawdzenie identyczności referencji
Name:		perl-Test-Identity
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/PEVANS/Test-Identity-%{version}.tar.gz
# Source0-md5:	ecef85c791cf5847e4c374983cf22a74
URL:		http://search.cpan.org/dist/Test-Identity/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a single testing function, identical. It asserts
that a given reference is as expected; that is, it either refers to
the same object or is undef. It is similar to Test::More::is except
that it uses refaddr, ensuring that it behaves correctly even if the
references under test are objects that overload stringification or
numification. It also provides better diagnostics if the test fails.

%description -l pl.UTF-8
Ten moduł udostępnia pojedynczą funkcję testującą: identical, służącą
do upewnienia się, że podana referencja jest zgodna z oczekiwaniami,
tzn. albo odnosi się do tego samego obiektu, albo jest równa undef.
Jest podobna do Test::More::is, ale używa refaddr, więc działa
poprawnie nawet jeśli testowane referencje są obiektami
przeciążającymi konwersję na łańcuch lub liczbę. Moduł zapewnia także
lepszą diagnostykę w przypadku niepowodzenia testu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Identity.pm
%{_mandir}/man3/Test::Identity.3pm*
