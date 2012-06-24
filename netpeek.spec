Summary: NetPeek is a GUI-based network monitoring and diagnosis tool.
Summary(pt_BR): NetPeek � uma ferramenta gr�fica para monitora��o e diagn�stico de redes
Summary(es): NetPeek is a GUI-based network monitoring and diagnosis tool.
Name: netpeek
Version: 0.0.4
Release: 1cl
Copyright: See LICENSE 
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
Source: netpeek-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-%{version}

%description
NetPeek is a GUI-based network monitoring and diagnosis tool.  It captures
packets from the local network and displays them to the user in two forms:
   - A short one-line form, similar to that produced by "tcpdump".
   - A long form, detailing all fields in a packet, with explainatory
     comments where necessary.  The display is similar to that produced
     by the commercial EtherPeek program.

%description -l pt_BR
O NetPeek � uma ferramenta gr�fica para monitora��o e diagn�stico de redes.
Com o NetPeek � poss�vel capturar pacotes de uma rede local e mostr�-los
para o usu�rio em duas maneiras diferentes:
- Forma reduzida, similar �quela do "tcpdump".
- Forma longa, detalhando todos os campos do pacote, acompanhado (quando
  necess�rio) de um coment�rio explicativo. Esta sa�da � similar a de um
  programa comercial chamado "EtherPeek".

%description -l es
NetPeek is a GUI-based network monitoring and diagnosis tool.  It captures
packets from the local network and displays them to the user in two forms:
   - A short one-line form, similar to that produced by "tcpdump".
   - A long form, detailing all fields in a packet, with explainatory
     comments where necessary.  The display is similar to that produced
     by the commercial EtherPeek program.

%prep 
%setup -q

%build
./configure --prefix=/usr
make

%install
mkdir -p $RPM_BUILD_DIR/usr/{bin,doc}
make install prefix=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/netpeek
%doc README LICENSE ChangeLog OTHER-LICENSES 
%changelog

* Thu Dec 02 1999 Fl�vio Bruno Leitner <lander@conectiva.com>
- First build for Conectiva
