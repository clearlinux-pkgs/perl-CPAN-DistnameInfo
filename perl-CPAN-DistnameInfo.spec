#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CPAN-DistnameInfo
Version  : 0.12
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/G/GB/GBARR/CPAN-DistnameInfo-0.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GB/GBARR/CPAN-DistnameInfo-0.12.tar.gz
Summary  : Extract distribution name and version from a distribution filename
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-CPAN-DistnameInfo-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
CPAN::DistnameInfo - Extract distribution name and version from a
distribution filename

%package dev
Summary: dev components for the perl-CPAN-DistnameInfo package.
Group: Development
Provides: perl-CPAN-DistnameInfo-devel = %{version}-%{release}
Requires: perl-CPAN-DistnameInfo = %{version}-%{release}

%description dev
dev components for the perl-CPAN-DistnameInfo package.


%package perl
Summary: perl components for the perl-CPAN-DistnameInfo package.
Group: Default
Requires: perl-CPAN-DistnameInfo = %{version}-%{release}

%description perl
perl components for the perl-CPAN-DistnameInfo package.


%prep
%setup -q -n CPAN-DistnameInfo-0.12
cd %{_builddir}/CPAN-DistnameInfo-0.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CPAN::DistnameInfo.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/CPAN/DistnameInfo.pm
