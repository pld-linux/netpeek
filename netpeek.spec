Summary:	NetPeek is a GUI-based network monitoring and diagnosis tool
Summary(pl.UTF-8):	Graficzne narzędzie do monitorowania i diagnostyki sieci
Summary(pt_BR.UTF-8):	NetPeek é uma ferramenta gráfica para monitoração e diagnóstico de redes
Name:		netpeek
Version:	0.0.4
Release:	1
License:	BSD-like
Group:		X11/Applications/Networking
Source0:	http://www.nyerk.com/netpeek/%{name}-%{version}.tar.gz
# Source0-md5:	e6990620201fe00a66dd4ea9522ff3c6
Source0:	http://linuxberg.surfnet.nl/files/gnome/network/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
NetPeek is a GUI-based network monitoring and diagnosis tool. It
captures packets from the local network and displays them to the user
in two forms:
   - A short one-line form, similar to that produced by "tcpdump".
   - A long form, detailing all fields in a packet, with explainatory
     comments where necessary. The display is similar to that produced by
     the commercial EtherPeek program.

%description -l pl.UTF-8
NetPeek jest graficznym narzędziem do monitorowania i diagnostyki
sieci. Lapie pakiety z lokalnej sieci i pokazuje użytkownikowi w dwóch
postaciach:
- krótkiej, jednoliniowej, podobnej do wyjścia z tcpdumpa
- długiej, szczegółowo pokazującej wszystkie pola w pakiecie z
  komentarzami gdzie trzeba - podobnej do wyjścia z komercyjnego
  programu EtherPeek.

%description -l pt_BR.UTF-8
O NetPeek é uma ferramenta gráfica para monitoração e diagnóstico de
redes. Com o NetPeek é possível capturar pacotes de uma rede local e
mostrá-los para o usuário em duas maneiras diferentes:
- Forma reduzida, similar àquela do "tcpdump".
- Forma longa, detalhando todos os campos do pacote, acompanhado
  (quando necessário) de um comentário explicativo. Esta saída é similar
  a de um programa comercial chamado "EtherPeek".

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fpermissive"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_DIR%{_prefix}/{bin,doc}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE ChangeLog OTHER-LICENSES
%attr(755,root,root) %{_bindir}/netpeek
