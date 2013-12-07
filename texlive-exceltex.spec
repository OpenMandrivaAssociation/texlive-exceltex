# revision 26313
# category Package
# catalog-ctan /macros/latex/contrib/exceltex
# catalog-date 2012-05-07 22:43:29 +0200
# catalog-license gpl
# catalog-version 0.5.1
Name:		texlive-exceltex
Version:	0.5.1
Release:	3
Summary:	Get data from Excel files into LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exceltex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exceltex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exceltex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-exceltex.bin = %{EVRD}

%description
Exceltex is a LaTeX package combined with a helper program
written in Perl. It provides an easy to use yet powerfull and
flexible way to get data from Spreadsheets into LaTeX. In
contrast to other solutions, exceltex does not seek to make the
creation of tables in LaTeX easier, but to get data from
Spreadsheets into LaTeX as easily as possible. The Excel (TM)
file format only acts as an interface between the spreadsheet
application and exceltex beacause it is easily accessible (via
the Spreadsheet::ParseExcel Perl module) and because most
spreadsheet applications are able to read and write Excel
files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/exceltex
%{_texmfdistdir}/scripts/exceltex/exceltex
%{_texmfdistdir}/tex/latex/exceltex/exceltex.sty
%doc %{_texmfdistdir}/doc/latex/exceltex/CHANGES
%doc %{_texmfdistdir}/doc/latex/exceltex/INSTALL
%doc %{_texmfdistdir}/doc/latex/exceltex/README
%doc %{_texmfdistdir}/doc/latex/exceltex/README.TEXLIVE

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/exceltex/exceltex exceltex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5.1-2
+ Revision: 812254
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5.1-1
+ Revision: 790568
- Import texlive-exceltex
- Import texlive-exceltex

