# revision 16836
# category Package
# catalog-ctan /macros/latex/contrib/minitoc
# catalog-date 2009-05-26 00:38:29 +0200
# catalog-license lppl
# catalog-version 60
Name:		texlive-minitoc
Version:	60
Release:	9
Summary:	Produce a table of contents for each chapter, part or section
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minitoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minitoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minitoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minitoc.source.tar.xz
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
%{_texmfdistdir}/bibtex/bst/minitoc/en-mtc.bst
%{_texmfdistdir}/bibtex/bst/minitoc/fr-mtc.bst
%{_texmfdistdir}/makeindex/minitoc/minitoc-fr.ist
%{_texmfdistdir}/makeindex/minitoc/minitoc.ist
%{_texmfdistdir}/tex/latex/minitoc/UKenglish.mld
%{_texmfdistdir}/tex/latex/minitoc/USenglish.mld
%{_texmfdistdir}/tex/latex/minitoc/acadian.mld
%{_texmfdistdir}/tex/latex/minitoc/acadien.mld
%{_texmfdistdir}/tex/latex/minitoc/afrikaan.mld
%{_texmfdistdir}/tex/latex/minitoc/afrikaans.mld
%{_texmfdistdir}/tex/latex/minitoc/albanian.mld
%{_texmfdistdir}/tex/latex/minitoc/american.mld
%{_texmfdistdir}/tex/latex/minitoc/arab.mld
%{_texmfdistdir}/tex/latex/minitoc/arab2.mld
%{_texmfdistdir}/tex/latex/minitoc/arabi.mld
%{_texmfdistdir}/tex/latex/minitoc/arabic.mld
%{_texmfdistdir}/tex/latex/minitoc/armenian.mld
%{_texmfdistdir}/tex/latex/minitoc/australian.mld
%{_texmfdistdir}/tex/latex/minitoc/austrian.mld
%{_texmfdistdir}/tex/latex/minitoc/bahasa.mld
%{_texmfdistdir}/tex/latex/minitoc/bahasai.mld
%{_texmfdistdir}/tex/latex/minitoc/bahasam.mld
%{_texmfdistdir}/tex/latex/minitoc/bangla.mld
%{_texmfdistdir}/tex/latex/minitoc/basque.mld
%{_texmfdistdir}/tex/latex/minitoc/bengali.mld
%{_texmfdistdir}/tex/latex/minitoc/bicig.mld
%{_texmfdistdir}/tex/latex/minitoc/bicig2.mld
%{_texmfdistdir}/tex/latex/minitoc/bicig3.mld
%{_texmfdistdir}/tex/latex/minitoc/bithe.mld
%{_texmfdistdir}/tex/latex/minitoc/boldsc.sty
%{_texmfdistdir}/tex/latex/minitoc/brazil.mld
%{_texmfdistdir}/tex/latex/minitoc/brazilian.mld
%{_texmfdistdir}/tex/latex/minitoc/breton.mld
%{_texmfdistdir}/tex/latex/minitoc/british.mld
%{_texmfdistdir}/tex/latex/minitoc/bulgarian.mld
%{_texmfdistdir}/tex/latex/minitoc/bulgarianb.mld
%{_texmfdistdir}/tex/latex/minitoc/buryat.mld
%{_texmfdistdir}/tex/latex/minitoc/buryat2.mld
%{_texmfdistdir}/tex/latex/minitoc/canadian.mld
%{_texmfdistdir}/tex/latex/minitoc/canadien.mld
%{_texmfdistdir}/tex/latex/minitoc/castillan.mld
%{_texmfdistdir}/tex/latex/minitoc/castillian.mld
%{_texmfdistdir}/tex/latex/minitoc/catalan.mld
%{_texmfdistdir}/tex/latex/minitoc/chinese1.mld
%{_texmfdistdir}/tex/latex/minitoc/chinese1.mlo
%{_texmfdistdir}/tex/latex/minitoc/chinese2.mld
%{_texmfdistdir}/tex/latex/minitoc/chinese2.mlo
%{_texmfdistdir}/tex/latex/minitoc/croatian.mld
%{_texmfdistdir}/tex/latex/minitoc/czech.mld
%{_texmfdistdir}/tex/latex/minitoc/danish.mld
%{_texmfdistdir}/tex/latex/minitoc/dblaccnt.sty
%{_texmfdistdir}/tex/latex/minitoc/devanagari.mld
%{_texmfdistdir}/tex/latex/minitoc/dutch.mld
%{_texmfdistdir}/tex/latex/minitoc/english.mld
%{_texmfdistdir}/tex/latex/minitoc/english1.mld
%{_texmfdistdir}/tex/latex/minitoc/english2.mld
%{_texmfdistdir}/tex/latex/minitoc/esperant.mld
%{_texmfdistdir}/tex/latex/minitoc/esperanto.mld
%{_texmfdistdir}/tex/latex/minitoc/estonian.mld
%{_texmfdistdir}/tex/latex/minitoc/ethiopia.mld
%{_texmfdistdir}/tex/latex/minitoc/ethiopian.mld
%{_texmfdistdir}/tex/latex/minitoc/ethiopian2.mld
%{_texmfdistdir}/tex/latex/minitoc/farsi1.mld
%{_texmfdistdir}/tex/latex/minitoc/farsi1.mlo
%{_texmfdistdir}/tex/latex/minitoc/farsi2.mld
%{_texmfdistdir}/tex/latex/minitoc/farsi2.mlo
%{_texmfdistdir}/tex/latex/minitoc/farsi3.mld
%{_texmfdistdir}/tex/latex/minitoc/finnish.mld
%{_texmfdistdir}/tex/latex/minitoc/finnish2.mld
%{_texmfdistdir}/tex/latex/minitoc/franc.sty
%{_texmfdistdir}/tex/latex/minitoc/francais.mld
%{_texmfdistdir}/tex/latex/minitoc/frbib.sty
%{_texmfdistdir}/tex/latex/minitoc/french.mld
%{_texmfdistdir}/tex/latex/minitoc/french1.mld
%{_texmfdistdir}/tex/latex/minitoc/french2.mld
%{_texmfdistdir}/tex/latex/minitoc/frenchb.mld
%{_texmfdistdir}/tex/latex/minitoc/frenchle.mld
%{_texmfdistdir}/tex/latex/minitoc/frenchpro.mld
%{_texmfdistdir}/tex/latex/minitoc/frnew.sty
%{_texmfdistdir}/tex/latex/minitoc/galician.mld
%{_texmfdistdir}/tex/latex/minitoc/german.mld
%{_texmfdistdir}/tex/latex/minitoc/germanb.mld
%{_texmfdistdir}/tex/latex/minitoc/germanb2.mld
%{_texmfdistdir}/tex/latex/minitoc/greek-mono.mld
%{_texmfdistdir}/tex/latex/minitoc/greek-polydemo.mld
%{_texmfdistdir}/tex/latex/minitoc/greek-polykatha.mld
%{_texmfdistdir}/tex/latex/minitoc/greek.mld
%{_texmfdistdir}/tex/latex/minitoc/guarani.mld
%{_texmfdistdir}/tex/latex/minitoc/hangul-u8.mld
%{_texmfdistdir}/tex/latex/minitoc/hangul-u8.mlo
%{_texmfdistdir}/tex/latex/minitoc/hangul1.mld
%{_texmfdistdir}/tex/latex/minitoc/hangul1.mlo
%{_texmfdistdir}/tex/latex/minitoc/hangul2.mld
%{_texmfdistdir}/tex/latex/minitoc/hangul2.mlo
%{_texmfdistdir}/tex/latex/minitoc/hangul3.mld
%{_texmfdistdir}/tex/latex/minitoc/hangul3.mlo
%{_texmfdistdir}/tex/latex/minitoc/hangul4.mld
%{_texmfdistdir}/tex/latex/minitoc/hangul4.mlo
%{_texmfdistdir}/tex/latex/minitoc/hanja-u8.mld
%{_texmfdistdir}/tex/latex/minitoc/hanja-u8.mlo
%{_texmfdistdir}/tex/latex/minitoc/hanja1.mld
%{_texmfdistdir}/tex/latex/minitoc/hanja1.mlo
%{_texmfdistdir}/tex/latex/minitoc/hanja2.mld
%{_texmfdistdir}/tex/latex/minitoc/hanja2.mlo
%{_texmfdistdir}/tex/latex/minitoc/hebrew.mld
%{_texmfdistdir}/tex/latex/minitoc/hebrew2.mld
%{_texmfdistdir}/tex/latex/minitoc/hindi-modern.mld
%{_texmfdistdir}/tex/latex/minitoc/hindi.mld
%{_texmfdistdir}/tex/latex/minitoc/hungarian.mld
%{_texmfdistdir}/tex/latex/minitoc/icelandic.mld
%{_texmfdistdir}/tex/latex/minitoc/indon.mld
%{_texmfdistdir}/tex/latex/minitoc/indonesian.mld
%{_texmfdistdir}/tex/latex/minitoc/interlingua.mld
%{_texmfdistdir}/tex/latex/minitoc/irish.mld
%{_texmfdistdir}/tex/latex/minitoc/italian.mld
%{_texmfdistdir}/tex/latex/minitoc/italian2.mld
%{_texmfdistdir}/tex/latex/minitoc/japanese.mld
%{_texmfdistdir}/tex/latex/minitoc/japanese.mlo
%{_texmfdistdir}/tex/latex/minitoc/japanese2.mld
%{_texmfdistdir}/tex/latex/minitoc/japanese2.mlo
%{_texmfdistdir}/tex/latex/minitoc/japanese3.mld
%{_texmfdistdir}/tex/latex/minitoc/japanese3.mlo
%{_texmfdistdir}/tex/latex/minitoc/japanese4.mld
%{_texmfdistdir}/tex/latex/minitoc/japanese4.mlo
%{_texmfdistdir}/tex/latex/minitoc/japanese5.mld
%{_texmfdistdir}/tex/latex/minitoc/japanese5.mlo
%{_texmfdistdir}/tex/latex/minitoc/japanese6.mld
%{_texmfdistdir}/tex/latex/minitoc/japanese6.mlo
%{_texmfdistdir}/tex/latex/minitoc/kannada.mld
%{_texmfdistdir}/tex/latex/minitoc/khalkha.mld
%{_texmfdistdir}/tex/latex/minitoc/latin.mld
%{_texmfdistdir}/tex/latex/minitoc/latin2.mld
%{_texmfdistdir}/tex/latex/minitoc/latinc.mld
%{_texmfdistdir}/tex/latex/minitoc/latinc2.mld
%{_texmfdistdir}/tex/latex/minitoc/latvian.mld
%{_texmfdistdir}/tex/latex/minitoc/latvian2.mld
%{_texmfdistdir}/tex/latex/minitoc/letton.mld
%{_texmfdistdir}/tex/latex/minitoc/letton2.mld
%{_texmfdistdir}/tex/latex/minitoc/lithuanian.mld
%{_texmfdistdir}/tex/latex/minitoc/lithuanian2.mld
%{_texmfdistdir}/tex/latex/minitoc/lowersorbian.mld
%{_texmfdistdir}/tex/latex/minitoc/lsorbian.mld
%{_texmfdistdir}/tex/latex/minitoc/magyar.mld
%{_texmfdistdir}/tex/latex/minitoc/magyar2.mld
%{_texmfdistdir}/tex/latex/minitoc/magyar3.mld
%{_texmfdistdir}/tex/latex/minitoc/malay.mld
%{_texmfdistdir}/tex/latex/minitoc/malayalam-b.mld
%{_texmfdistdir}/tex/latex/minitoc/malayalam-keli.mld
%{_texmfdistdir}/tex/latex/minitoc/malayalam-keli2.mld
%{_texmfdistdir}/tex/latex/minitoc/malayalam-mr.mld
%{_texmfdistdir}/tex/latex/minitoc/malayalam-omega.mld
%{_texmfdistdir}/tex/latex/minitoc/malayalam-omega.mlo
%{_texmfdistdir}/tex/latex/minitoc/malayalam-rachana.mld
%{_texmfdistdir}/tex/latex/minitoc/malayalam-rachana2.mld
%{_texmfdistdir}/tex/latex/minitoc/malayalam-rachana3.mld
%{_texmfdistdir}/tex/latex/minitoc/manju.mld
%{_texmfdistdir}/tex/latex/minitoc/mexican.mld
%{_texmfdistdir}/tex/latex/minitoc/meyalu.mld
%{_texmfdistdir}/tex/latex/minitoc/minitoc.sty
%{_texmfdistdir}/tex/latex/minitoc/mongol.mld
%{_texmfdistdir}/tex/latex/minitoc/mongolb.mld
%{_texmfdistdir}/tex/latex/minitoc/mongolian.mld
%{_texmfdistdir}/tex/latex/minitoc/mtcmess.sty
%{_texmfdistdir}/tex/latex/minitoc/mtcoff.sty
%{_texmfdistdir}/tex/latex/minitoc/mtcpatchmem.sty
%{_texmfdistdir}/tex/latex/minitoc/mypatches.sty
%{_texmfdistdir}/tex/latex/minitoc/naustrian.mld
%{_texmfdistdir}/tex/latex/minitoc/newzealand.mld
%{_texmfdistdir}/tex/latex/minitoc/ngerman.mld
%{_texmfdistdir}/tex/latex/minitoc/ngermanb.mld
%{_texmfdistdir}/tex/latex/minitoc/ngermanb2.mld
%{_texmfdistdir}/tex/latex/minitoc/norsk.mld
%{_texmfdistdir}/tex/latex/minitoc/norsk2.mld
%{_texmfdistdir}/tex/latex/minitoc/nynorsk.mld
%{_texmfdistdir}/tex/latex/minitoc/nynorsk2.mld
%{_texmfdistdir}/tex/latex/minitoc/occitan.mld
%{_texmfdistdir}/tex/latex/minitoc/occitan2.mld
%{_texmfdistdir}/tex/latex/minitoc/polish.mld
%{_texmfdistdir}/tex/latex/minitoc/polish2.mld
%{_texmfdistdir}/tex/latex/minitoc/polski.mld
%{_texmfdistdir}/tex/latex/minitoc/portuges.mld
%{_texmfdistdir}/tex/latex/minitoc/portuguese.mld
%{_texmfdistdir}/tex/latex/minitoc/romanian.mld
%{_texmfdistdir}/tex/latex/minitoc/romanian2.mld
%{_texmfdistdir}/tex/latex/minitoc/romanian3.mld
%{_texmfdistdir}/tex/latex/minitoc/russian-cca.mld
%{_texmfdistdir}/tex/latex/minitoc/russian-cca.mlo
%{_texmfdistdir}/tex/latex/minitoc/russian-cca1.mld
%{_texmfdistdir}/tex/latex/minitoc/russian-cca1.mlo
%{_texmfdistdir}/tex/latex/minitoc/russian-lh.mld
%{_texmfdistdir}/tex/latex/minitoc/russian-lh.mlo
%{_texmfdistdir}/tex/latex/minitoc/russian-lhcyralt.mld
%{_texmfdistdir}/tex/latex/minitoc/russian-lhcyralt.mlo
%{_texmfdistdir}/tex/latex/minitoc/russian-lhcyrkoi.mld
%{_texmfdistdir}/tex/latex/minitoc/russian-lhcyrkoi.mlo
%{_texmfdistdir}/tex/latex/minitoc/russian-lhcyrwin.mld
%{_texmfdistdir}/tex/latex/minitoc/russian-lhcyrwin.mlo
%{_texmfdistdir}/tex/latex/minitoc/russian.mld
%{_texmfdistdir}/tex/latex/minitoc/russian2m.mld
%{_texmfdistdir}/tex/latex/minitoc/russian2o.mld
%{_texmfdistdir}/tex/latex/minitoc/russianb.mld
%{_texmfdistdir}/tex/latex/minitoc/russianc.mld
%{_texmfdistdir}/tex/latex/minitoc/samin.mld
%{_texmfdistdir}/tex/latex/minitoc/scottish.mld
%{_texmfdistdir}/tex/latex/minitoc/serbian.mld
%{_texmfdistdir}/tex/latex/minitoc/serbianc.mld
%{_texmfdistdir}/tex/latex/minitoc/slovak.mld
%{_texmfdistdir}/tex/latex/minitoc/slovene.mld
%{_texmfdistdir}/tex/latex/minitoc/spanish.mld
%{_texmfdistdir}/tex/latex/minitoc/spanish2.mld
%{_texmfdistdir}/tex/latex/minitoc/spanish3.mld
%{_texmfdistdir}/tex/latex/minitoc/spanish4.mld
%{_texmfdistdir}/tex/latex/minitoc/swahili.mld
%{_texmfdistdir}/tex/latex/minitoc/swedish.mld
%{_texmfdistdir}/tex/latex/minitoc/swedish2.mld
%{_texmfdistdir}/tex/latex/minitoc/thai.mld
%{_texmfdistdir}/tex/latex/minitoc/thai.mlo
%{_texmfdistdir}/tex/latex/minitoc/turkish.mld
%{_texmfdistdir}/tex/latex/minitoc/uighur.mld
%{_texmfdistdir}/tex/latex/minitoc/uighur2.mld
%{_texmfdistdir}/tex/latex/minitoc/uighur3.mld
%{_texmfdistdir}/tex/latex/minitoc/ukraineb.mld
%{_texmfdistdir}/tex/latex/minitoc/ukrainian.mld
%{_texmfdistdir}/tex/latex/minitoc/uppersorbian.mld
%{_texmfdistdir}/tex/latex/minitoc/usorbian.mld
%{_texmfdistdir}/tex/latex/minitoc/vietnam.mld
%{_texmfdistdir}/tex/latex/minitoc/vietnamese.mld
%{_texmfdistdir}/tex/latex/minitoc/welsh.mld
%{_texmfdistdir}/tex/latex/minitoc/xalx.mld
%{_texmfdistdir}/tex/latex/minitoc/xalx2.mld
%{_texmfdistdir}/tex/latex/minitoc/xalx3.mld
%doc %{_texmfdistdir}/doc/latex/minitoc/CATALOG
%doc %{_texmfdistdir}/doc/latex/minitoc/INSTALL
%doc %{_texmfdistdir}/doc/latex/minitoc/README
%doc %{_texmfdistdir}/doc/latex/minitoc/TODO
%doc %{_texmfdistdir}/doc/latex/minitoc/aaland-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/acadian-m.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/acadie-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/acadien-m.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/afghan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/africa-lf.png
%doc %{_texmfdistdir}/doc/latex/minitoc/africa-lo.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/afrsud-l.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/afrsud-p.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/alb2.png
%doc %{_texmfdistdir}/doc/latex/minitoc/alba-eth.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/albania-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/albania.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/algeria-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/allemand.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/alsace-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/andorra-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/anglo1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/angola-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/arab-l.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/arabw.png
%doc %{_texmfdistdir}/doc/latex/minitoc/argentina-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/armenia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/armeniad.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/armenian-l.png
%doc %{_texmfdistdir}/doc/latex/minitoc/armeniar.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/aruba-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/australia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/austria-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/azerbaijan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bahamas-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bahrain-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/baltes.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/bangla.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bangla1.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bangla2.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bangladesh-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/barbados-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/basque-de.png
%doc %{_texmfdistdir}/doc/latex/minitoc/basque-df.png
%doc %{_texmfdistdir}/doc/latex/minitoc/basque1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/basque2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/be-dg-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/belarus-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/belgique.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/belgium-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/belize-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bengali-m.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/benin-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bolivia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bolzano-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bosnia-hz-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bosnia.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/bozen-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/brazil-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/brazil.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/brazilp.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/bretagne.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/brussels-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bulgaria-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bulgariar.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/bulgarski.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bulgmap.png
%doc %{_texmfdistdir}/doc/latex/minitoc/bur-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/burkina-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/burundi-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/buryatia-l.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/buryatia.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/california-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/cambodia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/cameroon-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/canada-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/canada-l.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/canada-pe.png
%doc %{_texmfdistdir}/doc/latex/minitoc/canada-pf.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/canada.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/canada1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/cap-verde-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/castille-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/catalan-d.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/catalan-p.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/catalonia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/caucasus.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/central-africa-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/chad-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/chile-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/china-ae.png
%doc %{_texmfdistdir}/doc/latex/minitoc/china-af.png
%doc %{_texmfdistdir}/doc/latex/minitoc/china-ch.png
%doc %{_texmfdistdir}/doc/latex/minitoc/china-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/china-l.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/china-w.png
%doc %{_texmfdistdir}/doc/latex/minitoc/chine1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/chine2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/cis-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/cmk
%doc %{_texmfdistdir}/doc/latex/minitoc/colombia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/comoros-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/congo-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/corsica-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/costa-rica-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/cplp-0.png
%doc %{_texmfdistdir}/doc/latex/minitoc/cplpmap.png
%doc %{_texmfdistdir}/doc/latex/minitoc/croatia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/croatia-un.png
%doc %{_texmfdistdir}/doc/latex/minitoc/croatie2.png
%doc %{_texmfdistdir}/doc/latex/minitoc/cuba-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/cyprus-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/cyr-alf.png
%doc %{_texmfdistdir}/doc/latex/minitoc/cz1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/cz3.png
%doc %{_texmfdistdir}/doc/latex/minitoc/czech-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/czechd.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/dane-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/danemark.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/danishd.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/danishg.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/devanagari.png
%doc %{_texmfdistdir}/doc/latex/minitoc/djibouti-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/dominica-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/dominican-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/dutchw.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/east-timor-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ecosse1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/ecosse2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/ecosse3.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/ecuador-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/egypt-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/el-salvador-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/emk
%doc %{_texmfdistdir}/doc/latex/minitoc/england-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/equa-guinea-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/eritrea-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/espa-l.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/espa-o.png
%doc %{_texmfdistdir}/doc/latex/minitoc/esperanto-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/estonia-a.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/estonia-b.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/estonia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/eth2.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ethiolang.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ethiopia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ethiopia-p.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/ethiopia.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/euro-lan.png
%doc %{_texmfdistdir}/doc/latex/minitoc/euro-lan1.png
%doc %{_texmfdistdir}/doc/latex/minitoc/euro-lan2.png
%doc %{_texmfdistdir}/doc/latex/minitoc/eusk-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/euskara.png
%doc %{_texmfdistdir}/doc/latex/minitoc/faroe-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/farsi-logo.png
%doc %{_texmfdistdir}/doc/latex/minitoc/farsi.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/feroe.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/fiji-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/finland-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/finlande1.png
%doc %{_texmfdistdir}/doc/latex/minitoc/finlande2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/finnishd.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/finnishl.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/flanders-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/fmk
%doc %{_texmfdistdir}/doc/latex/minitoc/france-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/france-lr.png
%doc %{_texmfdistdir}/doc/latex/minitoc/franco.png
%doc %{_texmfdistdir}/doc/latex/minitoc/francophonie-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/fswahili.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/gabon-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/gael-ft.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/gaid.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/galicia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/galicia-m.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/galicia-mp.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/galician-l.png
%doc %{_texmfdistdir}/doc/latex/minitoc/galles1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/galles2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/georgia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/germ-w.png
%doc %{_texmfdistdir}/doc/latex/minitoc/german-c.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/german-d.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/german-m.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/germany-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/ghana-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/gibraltar-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/grece1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/grece2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/greece-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/greeka.png
%doc %{_texmfdistdir}/doc/latex/minitoc/greekm.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/greenland-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/guatemala-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/guinea-bissau-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/guinea-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/gwenn-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/haiti-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/hangul.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hanja.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hanzi.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hin.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hindi-b.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hindi-p.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hispano.png
%doc %{_texmfdistdir}/doc/latex/minitoc/honduras-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hrv.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hun1.png
%doc %{_texmfdistdir}/doc/latex/minitoc/hun2.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/hungary-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/iceland-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/imk
%doc %{_texmfdistdir}/doc/latex/minitoc/imongolia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/inde1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/inde2.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/india-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/indonesia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/indonesia1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/indonesia2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/iran-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/iranian.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/iraq-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ireland-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/irish.png
%doc %{_texmfdistdir}/doc/latex/minitoc/irlande.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/islam-pbc.png
%doc %{_texmfdistdir}/doc/latex/minitoc/islam-sw.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/islande.png
%doc %{_texmfdistdir}/doc/latex/minitoc/islandep.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/isr1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/isr2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/israel-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/italian.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/italo1.png
%doc %{_texmfdistdir}/doc/latex/minitoc/italy-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/italysm.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ivory-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ivrit.png
%doc %{_texmfdistdir}/doc/latex/minitoc/jamaica-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/japan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/japon1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/japon2.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/jordan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/jutland-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/kannada-n.png
%doc %{_texmfdistdir}/doc/latex/minitoc/karnad1.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/karnataka-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/karnataka.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/kazakhstan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/kenya-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/kerala-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/kerala.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/khalkha.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/kiribati-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/korea-n-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/korea-s-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/korean1.png
%doc %{_texmfdistdir}/doc/latex/minitoc/korean2.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/kos-alb.png
%doc %{_texmfdistdir}/doc/latex/minitoc/kos-ml.png
%doc %{_texmfdistdir}/doc/latex/minitoc/kosovo-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/kuwait-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/kyrgyzstan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/lamed3.png
%doc %{_texmfdistdir}/doc/latex/minitoc/lang-g.png
%doc %{_texmfdistdir}/doc/latex/minitoc/laos-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/latvia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/latvian-d.png
%doc %{_texmfdistdir}/doc/latex/minitoc/latvian-r1.png
%doc %{_texmfdistdir}/doc/latex/minitoc/lebanon-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/lettonie.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/leur.png
%doc %{_texmfdistdir}/doc/latex/minitoc/liberia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/libya-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/liech-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/lithuania-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/lituanie.png
%doc %{_texmfdistdir}/doc/latex/minitoc/lorraine-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/louisiana-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ls-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/luso1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/luso2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/lux-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/macau-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/macedonia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/madagascar-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/maine-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/malawi-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/malayalam.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/malayalam.png
%doc %{_texmfdistdir}/doc/latex/minitoc/malaysia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/malaysia1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/malaysia2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mali-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/malta1-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/manchu.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/manchuria.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/manjuc.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/manjui.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mauritania-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mauritius-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mex1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mex2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mex3.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mexico-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/mexip.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/meyalu.png
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc-fr.bib
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc-fr.lan
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc-fr.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc.bib
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc.bug
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc.l
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc.lan
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc.pre
%doc %{_texmfdistdir}/doc/latex/minitoc/minitoc.sum
%doc %{_texmfdistdir}/doc/latex/minitoc/moldova-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/monaco-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mondep.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mongasie.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mongolcy.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mongolia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mongolian.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mongols.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mongoltr.png
%doc %{_texmfdistdir}/doc/latex/minitoc/montenegro-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/morocco-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mozambique-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-2c.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-2c.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-2nd.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-2nd.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-3co.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-3co.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-add.bib
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-add.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-add.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-ads.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-ads.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-amm.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-amm.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-apx.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-apx.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-art.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-art.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-bk.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-bk.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-bo.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-bo.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-ch0.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-ch0.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-cri.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-cri.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-fko.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-fko.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-fo1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-fo1.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-fo2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-fo2.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-gap.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-gap.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hi1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hi1.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hi2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hi2.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hia.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hia.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hir.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hir.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hop.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-hop.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-liv.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-liv.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-mem.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-mem.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-mm1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-mm1.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-mu.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-mu.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-nom.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-nom.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-ocf.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-ocf.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-ofs.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-ofs.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-sbf.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-sbf.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-scr.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-scr.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-syn.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-syn.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-tbi.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-tbi.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-tlc.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-tlc.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-tlo.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-tlo.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-tsf.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-tsf.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-vti.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/mtc-vti.tex
%doc %{_texmfdistdir}/doc/latex/minitoc/namibia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/nbrunswick-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ncyprus-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/neder.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/netherlands-antilles-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/netherlands-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/new-york-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/newzealand-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/nicaragua-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/nice-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/niger-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/nigeria-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/nihongo.png
%doc %{_texmfdistdir}/doc/latex/minitoc/norvege-c.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/norvege-t.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/norway-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/norway-p.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/occ-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/occdial1.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/occdial2.png
%doc %{_texmfdistdir}/doc/latex/minitoc/occitanie.png
%doc %{_texmfdistdir}/doc/latex/minitoc/occtaur.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/oman-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/opole-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/pakistan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/palestine-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/panama-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/paraguay-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/paraguay.png
%doc %{_texmfdistdir}/doc/latex/minitoc/paraguayp.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/peru-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/philippines-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/pmk
%doc %{_texmfdistdir}/doc/latex/minitoc/poland-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/polish-d.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/polmin.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/pologne.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/polski-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/portu-a.png
%doc %{_texmfdistdir}/doc/latex/minitoc/portu-b.png
%doc %{_texmfdistdir}/doc/latex/minitoc/portu-p.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/portu-r.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/portugal-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/portugal.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/puerto-rico-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/qatar-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/quebec-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/rdcongo-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/rmk
%doc %{_texmfdistdir}/doc/latex/minitoc/romania-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/romanian.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/rus-cyr.png
%doc %{_texmfdistdir}/doc/latex/minitoc/rus-re.png
%doc %{_texmfdistdir}/doc/latex/minitoc/rus-su.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/russia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/russian-e.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/russian-n.png
%doc %{_texmfdistdir}/doc/latex/minitoc/russian-w.png
%doc %{_texmfdistdir}/doc/latex/minitoc/russian.png
%doc %{_texmfdistdir}/doc/latex/minitoc/rwanda-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/saint-lucia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/same-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/same.png
%doc %{_texmfdistdir}/doc/latex/minitoc/sami-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/samoa-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/san-marino-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/sao-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/saudi-arabia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/scotland-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/senegal-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/serb-a.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/serbia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/serbia-f2.png
%doc %{_texmfdistdir}/doc/latex/minitoc/serbia1.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/seychelles-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/singapore-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/slovak-ok.png
%doc %{_texmfdistdir}/doc/latex/minitoc/slovakia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/slovakia.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/slovenia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/slovenian.png
%doc %{_texmfdistdir}/doc/latex/minitoc/slovenie.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/solomon-islands-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/somalia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/sorabe-1.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/sorabe-2.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/sorben.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/sorbian.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/south-africa-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/spain-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/spain.png
%doc %{_texmfdistdir}/doc/latex/minitoc/spilhennig.png
%doc %{_texmfdistdir}/doc/latex/minitoc/start.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/stop.png
%doc %{_texmfdistdir}/doc/latex/minitoc/sudan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/suede-a.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/suede-fin.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/suisse-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/suriname-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/svenska.png
%doc %{_texmfdistdir}/doc/latex/minitoc/swahili-m.png
%doc %{_texmfdistdir}/doc/latex/minitoc/swahili.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/sweden-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/sweden.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/syria-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/taiwan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/tajikistan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/tanzania-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/thai.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/thai.png
%doc %{_texmfdistdir}/doc/latex/minitoc/thailand-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/tmk
%doc %{_texmfdistdir}/doc/latex/minitoc/togo-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/tonga-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/tunisia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/turkey-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/turkish.png
%doc %{_texmfdistdir}/doc/latex/minitoc/turkmenistan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/turquie.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/tuvalu-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/uae-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/uganda-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/uighur-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/uighur.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/uk-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ukra.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ukraine-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/ukraine.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/ukrainep.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/uruguay-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/us-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/usa-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/uzbekistan-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/vanuatu-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/vatican-f.jpg
%doc %{_texmfdistdir}/doc/latex/minitoc/venezuela-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/vermont-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/viet-w.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/viet2.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/viet3.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/viet4.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/vietnam-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/vojvodina-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/wales-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/wallonia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/wallonie.pdf
%doc %{_texmfdistdir}/doc/latex/minitoc/wiki.png
%doc %{_texmfdistdir}/doc/latex/minitoc/wikif.png
%doc %{_texmfdistdir}/doc/latex/minitoc/wrs-a.png
%doc %{_texmfdistdir}/doc/latex/minitoc/wrs-c.png
%doc %{_texmfdistdir}/doc/latex/minitoc/xinjiang.png
%doc %{_texmfdistdir}/doc/latex/minitoc/xinjiangc.png
%doc %{_texmfdistdir}/doc/latex/minitoc/xmk
%doc %{_texmfdistdir}/doc/latex/minitoc/xyugo.png
%doc %{_texmfdistdir}/doc/latex/minitoc/yemen-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/zambia-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/zanzibar-f.png
%doc %{_texmfdistdir}/doc/latex/minitoc/zimbabwe-f.png
#- source
%doc %{_texmfdistdir}/source/latex/minitoc/minitoc-fr.dtx
%doc %{_texmfdistdir}/source/latex/minitoc/minitoc.dtx
%doc %{_texmfdistdir}/source/latex/minitoc/minitoc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}
