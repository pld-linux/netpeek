Summary: NetPeek is a GUI-based network monitoring and diagnosis tool.
Summary(pt_BR): NetPeek é uma ferramenta gráfica para monitoração e diagnóstico de redes
Summary(es): NetPeek is a GUI-based network monitoring and diagnosis tool.
Name: netpeek
Version: 0.0.4
Release: 1cl
Copyright: See LICENSE 
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
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
O NetPeek é uma ferramenta gráfica para monitoração e diagnóstico de redes.
Com o NetPeek é possível capturar pacotes de uma rede local e mostrá-los
para o usuário em duas maneiras diferentes:
- Forma reduzida, similar àquela do "tcpdump".
- Forma longa, detalhando todos os campos do pacote, acompanhado (quando
  necessário) de um comentário explicativo. Esta saída é similar a de um
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

* Thu Dec 02 1999 Flávio Bruno Leitner <lander@conectiva.com>
- First build for Conectiva
