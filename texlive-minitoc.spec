Name:		texlive-minitoc
Version:	61719
Release:	2
Summary:	Produce a table of contents for each chapter, part or section
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minitoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minitoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minitoc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The minitoc package allows you to add mini-tables-of-contents
(minitocs) at the beginning of every chapter, part or section.
There is also provision for mini-lists of figures and of
tables. At the part level, they are parttocs, partlofs and
partlots. If the type of document does not use chapters, the
basic provision is section level secttocs, sectlofs and
sectlots. The package has provision for language-specific
configuration of its own "fixed names", using .mld files
(analagous to babel .ldf files that do that job for LaTeX"s own
fixed names).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/minitoc
%doc %{_texmfdistdir}/doc/latex/minitoc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
