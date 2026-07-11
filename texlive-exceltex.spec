%global tl_name exceltex
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.1
Release:	%{tl_revision}.1
Summary:	Get data from Excel files into LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exceltex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exceltex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exceltex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(exceltex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Exceltex is a LaTeX package combined with a helper program written in
Perl. It provides an easy to use yet powerful and flexible way to get
data from Spreadsheets into LaTeX. In contrast to other solutions,
exceltex does not seek to make the creation of tables in LaTeX easier,
but to get data from Spreadsheets into LaTeX as easily as possible. The
Excel (TM) file format only acts as an interface between the spreadsheet
application and exceltex because it is easily accessible (via the
Spreadsheet::ParseExcel Perl module) and because most spreadsheet
applications are able to read and write Excel files.

