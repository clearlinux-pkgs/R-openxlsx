#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : R-openxlsx
Version  : 4.2.8
Release  : 69
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/openxlsx_4.2.8.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/openxlsx_4.2.8.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
high level interface to writing, styling and editing worksheets.
    Through the use of 'Rcpp', read/write times are comparable to the
    'xlsx' and 'XLConnect' packages with the added benefit of removing the
    dependency on Java.

%package lib
Summary: lib components for the R-openxlsx package.
Group: Libraries

%description lib
lib components for the R-openxlsx package.


%prep
%setup -q -n openxlsx
pushd ..
cp -a openxlsx buildavx2
popd
pushd ..
cp -a openxlsx buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737996534

%install
export SOURCE_DATE_EPOCH=1737996534
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/openxlsx/DESCRIPTION
/usr/lib64/R/library/openxlsx/INDEX
/usr/lib64/R/library/openxlsx/LICENSE
/usr/lib64/R/library/openxlsx/Meta/Rd.rds
/usr/lib64/R/library/openxlsx/Meta/data.rds
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
/usr/lib64/R/library/openxlsx/data/Rdata.rdb
/usr/lib64/R/library/openxlsx/data/Rdata.rds
/usr/lib64/R/library/openxlsx/data/Rdata.rdx
/usr/lib64/R/library/openxlsx/doc/Formatting.R
/usr/lib64/R/library/openxlsx/doc/Formatting.Rmd
/usr/lib64/R/library/openxlsx/doc/Formatting.html
/usr/lib64/R/library/openxlsx/doc/Introduction.R
/usr/lib64/R/library/openxlsx/doc/Introduction.Rmd
/usr/lib64/R/library/openxlsx/doc/Introduction.html
/usr/lib64/R/library/openxlsx/doc/index.html
/usr/lib64/R/library/openxlsx/extdata/ColorTabs3.xlsx
/usr/lib64/R/library/openxlsx/extdata/build_font_size_lookup.R
/usr/lib64/R/library/openxlsx/extdata/cloneEmptyWorksheetExample.xlsx
/usr/lib64/R/library/openxlsx/extdata/cloneWorksheetExample.xlsx
/usr/lib64/R/library/openxlsx/extdata/conditional_formatting_testing.R
/usr/lib64/R/library/openxlsx/extdata/einstein.jpg
/usr/lib64/R/library/openxlsx/extdata/gh_issue_288.xlsx
/usr/lib64/R/library/openxlsx/extdata/groupTest.xlsx
/usr/lib64/R/library/openxlsx/extdata/inlineStr.xlsx
/usr/lib64/R/library/openxlsx/extdata/loadExample.xlsx
/usr/lib64/R/library/openxlsx/extdata/loadPivotTables.xlsx
/usr/lib64/R/library/openxlsx/extdata/loadThreadComment.xlsx
/usr/lib64/R/library/openxlsx/extdata/load_xlsx_testing.R
/usr/lib64/R/library/openxlsx/extdata/na_convert.xlsx
/usr/lib64/R/library/openxlsx/extdata/namedRegions.xlsx
/usr/lib64/R/library/openxlsx/extdata/namedRegions2.xlsx
/usr/lib64/R/library/openxlsx/extdata/namedRegions3.xlsx
/usr/lib64/R/library/openxlsx/extdata/nested_grouped_rowscols.xlsx
/usr/lib64/R/library/openxlsx/extdata/readTest.xlsx
/usr/lib64/R/library/openxlsx/extdata/read_failure_test.xlsx
/usr/lib64/R/library/openxlsx/extdata/silent_worksheet_entries.xlsx
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
/usr/lib64/R/library/openxlsx/help/figures/logo.png
/usr/lib64/R/library/openxlsx/help/figures/tableoptions.pdf
/usr/lib64/R/library/openxlsx/help/figures/tableoptions.png
/usr/lib64/R/library/openxlsx/help/openxlsx.rdb
/usr/lib64/R/library/openxlsx/help/openxlsx.rdx
/usr/lib64/R/library/openxlsx/help/paths.rds
/usr/lib64/R/library/openxlsx/html/00Index.html
/usr/lib64/R/library/openxlsx/html/R.css
/usr/lib64/R/library/openxlsx/tests/testthat.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-CommentClass.R
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
/usr/lib64/R/library/openxlsx/tests/testthat/test-grouped_rows.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-insertImage.R
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
/usr/lib64/R/library/openxlsx/tests/testthat/test-read_xlsx_random_seed.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-remove_worksheets.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-saveWorkbook.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-setColWidths.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-setWindowSize.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-silent_worksheet_entries.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-skip_empty_cols.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-skip_empty_rows.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-styles.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-table_overlaps.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-trying_to_break_openxlsx.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-v3_0_0_bugs.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-validate_data.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-validate_table_name.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-worksheet_ordering.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-worksheet_renaming.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-wrappers.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write-permissions.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-writeData.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-writeDataTable.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write_data_to_sheetData.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write_data_to_sheetData_NAs.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write_read_equality.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-write_xlsx_vector_args.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-writing_posixct.R
/usr/lib64/R/library/openxlsx/tests/testthat/test-writing_sheet_data.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/openxlsx/libs/openxlsx.so
/V4/usr/lib64/R/library/openxlsx/libs/openxlsx.so
/usr/lib64/R/library/openxlsx/libs/openxlsx.so
