%define _buildid .1

Name:		perl-TAP-Parser-SourceHandler-pgTAP
Version:	3.30
Release:	1%{?_buildid}%{?dist}
Summary:	Stream TAP from pgTAP test scripts
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/TAP-Parser-SourceHandler-pgTAP/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/TAP-Parser-SourceHandler-pgTAP-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Module::Build) > 0.36
BuildRequires:	perl(TAP::Parser::SourceHandler)
BuildRequires:	perl(Test::More)
Requires:	perl(TAP::Parser::SourceHandler)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Stream TAP from pgTAP test scripts

%prep
%setup -q -n TAP-Parser-SourceHandler-pgTAP-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}

%check
AUTHOR_TESTING=1 ./Build test

%files
%doc Changes
%{perl_vendorlib}/TAP/Parser/SourceHandler/
%{_bindir}/pg_*
%{_mandir}/man3/TAP::Parser::SourceHandler::pgTAP.3pm*
%{_mandir}/man1/pg_prove.1*
%{_mandir}/man1/pg_tapgen.1*

%changelog
