#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Arping
Summary:	Net::Arping - Ping remote host by ARP packets
Summary(pl.UTF-8):	Net::Arping - Pingowanie zdalnego hosta przy użyciu pakietów ARP
Name:		perl-Net-Arping
Version:	0.03
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RA/RADEK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bf26415f1406dec2689d5e8aa3ca2744
URL:		http://search.cpan.org/dist/Net-Arping/
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module contains function for testing remote host reachability by
sending ARP packets.

The program must be run as root or be setuid to root.

%description -l pl.UTF-8
Ten moduł zawiera funkcję do sprawdzania dostępności zdalnego hosta
poprzez wysyłanie pakietów ARP.

Program musi być uruchamiany przez roota lub mieć ustawiony suid root.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/*.pm
%dir %{perl_vendorarch}/auto/Net/Arping
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Arping/*.so
%{_mandir}/man3/*
