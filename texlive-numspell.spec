Name:		texlive-numspell
Version:	70936
Release:	1
Summary:	Spelling cardinal and ordinal numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/numspell
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numspell.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numspell.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package supports the spelling of cardinal and ordinal
numbers. Supported languages are English, French, German,
Hungarian, Italian, and Latin. The package requires xstring and
iflang.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/numspell
%doc %{_texmfdistdir}/doc/latex/numspell

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
