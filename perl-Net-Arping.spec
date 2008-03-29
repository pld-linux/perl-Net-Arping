%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Arping
Summary:	Net::Arping - Ping remote host by ARP packets
Summary(pl.UTF-8):	Net::Arping - Pingowanie zdalnego hosta poprzez pakiety ARP
Name:		perl-Net-Arping
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4d60bb746995f5c4ec827f6fc865ed8
Patch0:		%{name}-libnet11.patch
URL:		http://search.cpan.org/dist/Net-Arping/Arping.pm
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module contains function for testing remote host reachability by
sending ARP packets.

The program must be run as root or be setuid to root.

# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

# "make test" removed -- requires root privileges

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
