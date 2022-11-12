Name:		texlive-exceltex
Version:	26313
Release:	1
Summary:	Get data from Excel files into LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exceltex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exceltex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exceltex.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/exceltex/exceltex exceltex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
