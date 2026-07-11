%global tl_name hexgame
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Provide an environment to draw a hexgame-board
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hexgame
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hexgame.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hexgame.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hex is a mathematical game invented by the Danish mathematician Piet
Hein and independently by the mathematician John Nash. This package
defines an environment that enables the user to draw such a game in a
trivial way.

