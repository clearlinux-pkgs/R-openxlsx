#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-openxlsx
Version  : 4.2.4
Release  : 44
URL      : https://cran.r-project.org/src/contrib/openxlsx_4.2.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/openxlsx_4.2.4.tar.gz
Summary  : Read, Write and Edit xlsx Files
Group    : Development/Tools
License  : MIT
Requires: R-openxlsx-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-stringi
Requires: R-zip
BuildRequires : R-Rcpp
BuildRequires : R-stringi
BuildRequires : R-zip
BuildRequires : buildreq-R

%description
providing a high level interface to writing, styling and editing
    worksheets. Through the use of 'Rcpp', read/write times are comparable
    to the 'xlsx' and 'XLConnect' packages with the added benefit of
    removing the dependency on Java.

%package lib
Summary: lib components for the R-openxlsx package.
Group: Libraries

%description lib
lib components for the R-openxlsx package.


%prep
%setup -q -c -n openxlsx
cd %{_builddir}/openxlsx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623855448

%install
export SOURCE_DATE_EPOCH=1623855448
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc openxlsx || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/openxlsx/DESCRIPTION
/usr/lib64/R/library/openxlsx/INDEX
/usr/lib64/R/library/openxlsx/LICENSE
/usr/lib64/R/library/openxlsx/Meta/Rd.rds
/usr/lib64/R/library/openxlsx/Meta/features.rds
/usr/lib64/R/library/openxlsx/Meta/hsearch.rds
/usr/lib64/R/library/openxlsx/Meta/links.rds
/usr/lib64/R/library/openxlsx/Meta/nsInfo.rds
/usr/lib64/R/library/openxlsx/Meta/package.rds
/usr/lib64/R/library/openxlsx/Meta/vignette.rds
/usr/lib64/R/library/openxlsx/NAMESPACE
/usr/lib64/R/library/openxlsx/NEWS.md
/usr/lib64/R/library/openxlsx/R/openxlsx
/usr/lib64/R/library/openxlsx/R/openxlsx.rdb
/usr/lib64/R/library/openxlsx/R/openxlsx.rdx
/usr/lib64/R/library/openxlsx/R/sysdata.rdb
/usr/lib64/R/library/openxlsx/R/sysdata.rdx
/usr/lib64/R/library/openxlsx/WORDLIST
/usr/lib64/R/library/openxlsx/doc/Formatting.R
/usr/lib64/R/library/openxlsx/doc/Formatting.Rmd
/usr/lib64/R/library/openxlsx/doc/Formatting.html
/usr/lib64/R/library/openxlsx/doc/Introduction.R
/usr/lib64/R/library/openxlsx/doc/Introduction.Rmd
/usr/lib64/R/library/openxlsx/doc/Introduction.html
/usr/lib64/R/library/openxlsx/doc/index.html
/usr/lib64/R/library/openxlsx/extdata/build_font_size_lookup.R
/usr/lib64/R/library/openxlsx/extdata/cloneEmptyWorksheetExample.xlsx
/usr/lib64/R/library/openxlsx/extdata/cloneWorksheetExample.xlsx
/usr/lib64/R/library/openxlsx/extdata/conditional_formatting_testing.R
/usr/lib64/R/library/openxlsx/extdata/einstein.jpg
/usr/lib64/R/library/openxlsx/extdata/groupTest.xlsx
/usr/lib64/R/library/openxlsx/extdata/loadExample.xlsx
/usr/lib64/R/library/openxlsx/extdata/loadPivotTables.xlsx
/usr/lib64/R/library/openxlsx/extdata/loadThreadComment.xlsx
/usr/lib64/R/library/openxlsx/extdata/load_xlsx_testing.R
/usr/lib64/R/library/openxlsx/extdata/namedRegions.xlsx
/usr/lib64/R/library/openxlsx/extdata/namedRegions2.xlsx
/usr/lib64/R/library/openxlsx/extdata/namedRegions3.xlsx
/usr/lib64/R/library/openxlsx/extdata/readTest.xlsx
/usr/lib64/R/library/openxlsx/extdata/read_failure_test.xlsx
/usr/lib64/R/library/openxlsx/extdata/stack_style_testing.R
/usr/lib64/R/library/openxlsx/help/AnIndex
/usr/lib64/R/library/openxlsx/help/aliases.rds
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/openxlsx/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/openxlsx/help/figures/tableoptions.pdf
/usr/lib64/R/library/openxlsx/help/figures/tableoptions.png
/usr/lib64/R/library/openxlsx/help/openxlsx.rdb
/usr/lib64/R/library/openxlsx/help/openxlsx.rdx
/usr/lib64/R/library/openxlsx/help/paths.rds
/usr/lib64/R/library/openxlsx/html/00Index.html
/usr/lib64/R/library/openxlsx/html/R.css
/usr/lib64/R/library/openxlsx/tests/testthat.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-Workbook_properties.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-Worksheet_naming.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-activeSheet.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-border_parsing.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-build_workbook.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-cloneWorksheet.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-conditionalFormatting.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-date_time_conversion.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-deleting_tables.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-encoding.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-fill_merged_cells.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-fontSizeLookupTables.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-freeze_pane.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-getBaseFont.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-getCellRefs.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-load_read_file_read_equality.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-loading_workbook.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-loading_workbook_tables.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-loading_workbook_unzipped.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-named_regions.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-options.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-outlines.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-page_setup.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-protect-workbook.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-protect-worksheet.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-read_from_created_wb.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-read_from_loaded_workbook.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-read_sources.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-read_write_logicals.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-read_xlsx_correct_sheet.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-remove_worksheets.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-saveWorkbook.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-skip_empty_cols.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-skip_empty_rows.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-style_replacing.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-table_overlaps.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-trying_to_break_openxlsx.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-v3_0_0_bugs.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-validate_table_name.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-worksheet_ordering.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-worksheet_renaming.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write_data_to_sheetData.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write_data_to_sheetData_NAs.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write_read_equality.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write_xlsx_vector_args.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-writing_posixct.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-writing_sheet_data.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/openxlsx/libs/openxlsx.so
/usr/lib64/R/library/openxlsx/libs/openxlsx.so.avx2
/usr/lib64/R/library/openxlsx/libs/openxlsx.so.avx512
