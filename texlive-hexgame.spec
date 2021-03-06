# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hexgame
# catalog-date 2008-08-22 10:38:02 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-hexgame
Version:	1.0
Release:	11
Summary:	Provide an environment to draw a hexgame-board
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hexgame
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexgame.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexgame.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752546
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718615
- texlive-hexgame
- texlive-hexgame
- texlive-hexgame
- texlive-hexgame

