# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hexgame
# catalog-date 2008-08-22 10:38:02 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-hexgame
Version:	1.0
Release:	1
Summary:	Provide an environment to draw a hexgame-board
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hexgame
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexgame.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexgame.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Hex is a mathematical game invented by the Danish mathematician
Piet Hein and independently by the mathematician John Nash.
This package defines an environment that enables the user to
draw such a game in a trivial way.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hexgame/hexgame.sty
%doc %{_texmfdistdir}/doc/latex/hexgame/README
%doc %{_texmfdistdir}/doc/latex/hexgame/hexgame.pdf
%doc %{_texmfdistdir}/doc/latex/hexgame/hexgame.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}