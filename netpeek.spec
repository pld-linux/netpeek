Summary:	NetPeek is a GUI-based network monitoring and diagnosis tool
Summary(es):	NetPeek is a GUI-based network monitoring and diagnosis tool
Summary(pl):	Graficzne narzêdzie do monitorowania i diagnostyki sieci
Summary(pt_BR): NetPeek é uma ferramenta gráfica para monitoração e diagnóstico de redes
Name:		netpeek
Version:	0.0.4
Release:	1
License:	BSD-style
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://www.nyerk.com/netpeek/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
NetPeek is a GUI-based network monitoring and diagnosis tool. It
captures packets from the local network and displays them to the user
in two forms:
   - A short one-line form, similar to that produced by "tcpdump".
   - A long form, detailing all fields in a packet, with explainatory
     comments where necessary. The display is similar to that produced by
     the commercial EtherPeek program.

%description -l es
NetPeek is a GUI-based network monitoring and diagnosis tool. It
captures packets from the local network and displays them to the user
in two forms:
   - A short one-line form, similar to that produced by "tcpdump".
   - A long form, detailing all fields in a packet, with explainatory
     comments where necessary. The display is similar to that produced by
     the commercial EtherPeek program.

%description -l pt_BR
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

gzip -9nf README LICENSE ChangeLog OTHER-LICENSES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/netpeek
