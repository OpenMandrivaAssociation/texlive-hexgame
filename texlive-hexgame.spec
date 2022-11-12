Name:		texlive-hexgame
Version:	15878
Release:	1
Summary:	Provide an environment to draw a hexgame-board
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hexgame
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexgame.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexgame.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Hex is a mathematical game invented by the Danish mathematician
Piet Hein and independently by the mathematician John Nash.
This package defines an environment that enables the user to
draw such a game in a trivial way.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hexgame/hexgame.sty
%doc %{_texmfdistdir}/doc/latex/hexgame/README
%doc %{_texmfdistdir}/doc/latex/hexgame/hexgame.pdf
%doc %{_texmfdistdir}/doc/latex/hexgame/hexgame.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
