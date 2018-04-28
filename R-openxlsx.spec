#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-openxlsx
Version  : 4.0.17
Release  : 6
URL      : https://cran.r-project.org/src/contrib/openxlsx_4.0.17.tar.gz
Source0  : https://cran.r-project.org/src/contrib/openxlsx_4.0.17.tar.gz
Summary  : Read, Write and Edit XLSX Files
Group    : Development/Tools
License  : GPL-3.0
Requires: R-openxlsx-lib
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers

%description
level interface to writing, styling and editing worksheets. Through the use of
    'Rcpp', read/write times are comparable to the 'xlsx' and 'XLConnect' packages
    with the added benefit of removing the dependency on Java.

%package lib
Summary: lib components for the R-openxlsx package.
Group: Libraries

%description lib
lib components for the R-openxlsx package.


%prep
%setup -q -c -n openxlsx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522685817

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522685817
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library openxlsx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library openxlsx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library openxlsx
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library openxlsx|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/openxlsx/DESCRIPTION
/usr/lib64/R/library/openxlsx/INDEX
/usr/lib64/R/library/openxlsx/Meta/Rd.rds
/usr/lib64/R/library/openxlsx/Meta/features.rds
/usr/lib64/R/library/openxlsx/Meta/hsearch.rds
/usr/lib64/R/library/openxlsx/Meta/links.rds
/usr/lib64/R/library/openxlsx/Meta/nsInfo.rds
/usr/lib64/R/library/openxlsx/Meta/package.rds
/usr/lib64/R/library/openxlsx/Meta/vignette.rds
/usr/lib64/R/library/openxlsx/NAMESPACE
/usr/lib64/R/library/openxlsx/NEWS
/usr/lib64/R/library/openxlsx/R/openxlsx
/usr/lib64/R/library/openxlsx/R/openxlsx.rdb
/usr/lib64/R/library/openxlsx/R/openxlsx.rdx
/usr/lib64/R/library/openxlsx/build_font_size_lookup.R
/usr/lib64/R/library/openxlsx/conditional_formatting_testing.R
/usr/lib64/R/library/openxlsx/doc/Introduction.Rnw
/usr/lib64/R/library/openxlsx/doc/Introduction.pdf
/usr/lib64/R/library/openxlsx/doc/formatting.Rnw
/usr/lib64/R/library/openxlsx/doc/formatting.pdf
/usr/lib64/R/library/openxlsx/doc/index.html
/usr/lib64/R/library/openxlsx/doc/installation.Rnw
/usr/lib64/R/library/openxlsx/doc/installation.pdf
/usr/lib64/R/library/openxlsx/einstein.jpg
/usr/lib64/R/library/openxlsx/help/AnIndex
/usr/lib64/R/library/openxlsx/help/aliases.rds
/usr/lib64/R/library/openxlsx/help/figures/tableoptions.pdf
/usr/lib64/R/library/openxlsx/help/figures/tableoptions.png
/usr/lib64/R/library/openxlsx/help/openxlsx.rdb
/usr/lib64/R/library/openxlsx/help/openxlsx.rdx
/usr/lib64/R/library/openxlsx/help/paths.rds
/usr/lib64/R/library/openxlsx/html/00Index.html
/usr/lib64/R/library/openxlsx/html/R.css
/usr/lib64/R/library/openxlsx/libs/symbols.rds
/usr/lib64/R/library/openxlsx/loadExample.xlsx
/usr/lib64/R/library/openxlsx/load_xlsx_testing.R
/usr/lib64/R/library/openxlsx/namedRegions.xlsx
/usr/lib64/R/library/openxlsx/readTest.xlsx
/usr/lib64/R/library/openxlsx/stack_style_testing.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/openxlsx/libs/openxlsx.so
/usr/lib64/R/library/openxlsx/libs/openxlsx.so.avx2
/usr/lib64/R/library/openxlsx/libs/openxlsx.so.avx512
