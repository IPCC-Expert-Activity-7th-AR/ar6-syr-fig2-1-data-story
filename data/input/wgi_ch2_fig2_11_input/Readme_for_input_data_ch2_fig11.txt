# Creation date (YYYY-MM-DD): 2021-10-29
# File created by: Blair Trewin; Darrell Kaufman
# email: blair.trewin@bom.gov.au; darrell.kaufman@nau.edu
# ========================
# GENERAL INFORMATION 
# 
# *Title 
# Readme for Input data for Figure 2.11 (panel b and c) in the IPCC Working Group I Contribution to the Sixth Assessment Report: Chapter 2
# 
#
# ========================
# DATA & FILE OVERVIEW
#
# List of all files and subfolders
# 
# --------------------------
# Panel b 
#
# --------------------------
# filename 1: IndermediateData_Figure-2_11-HadCRUT_significance_overlay_1981-2020.txt
# -----------------------
# --------------------------
# filename 2: IntermediateData_Figure-2_11-HadCRUT_significance_overlay_1900-1980.txt
# -----------------------
# --------------------------
# filename 3: IntermediateData_Figure-2_11-HadCRUT_trends_1900-1980.txt
# -----------------------
# --------------------------
# filename 4: IntermediateData_Figure-2_11-HadCRUT_trends_1981-2020.txt
# -----------------------
# --------------------------
# filename 5: Figure_2_11-notes_on_HadCRUT_trend_files.pdf
# -----------------------
#
# comments:
Notes on HadCRUT trend maps
For each time period, there are two plain text files: one showing the trend values (in °C per decade), the other an indicator of significant (1 = significant, 0 = non-significant, -99 = missing data). Gridpoints with insufficient data for trend calcula)on are shown with a trend of -999.0. The values are on a 5-degree grid, with rows from longitude -177.5 to 177.5 and columns from latitudes -87.5 to 87.5.
#
# --------------------------
# Panel c 
#
# --------------------------
# --------------------------
# filename 6: Figure_2_11c-lower_panel.csv (lower)
# -----------------------
#
# N° of columns: 7
# Column headings: Year, HadCRUT, NOAA, Berkeley, Kadow, HadCRUT confidence limit lower, HadCRUT confidence limit upper
#        
#
# column_name 1: Year
# long_name: Year
# units: none
# missing_value: N/A
# type (int/float/str): int
# comments: decadal means shown at bottom of file
#
# column_name 2: HadCRUT
# long_name: HadCRUT
# units: degrees C
# missing_value: N/A
# type (int/float/str): float
# comments: decadal means shown at bottom of file
#
# column_name 3: NOAA
# long_name: NOAA
# units: degrees C
# missing_value: N/A
# type (int/float/str): float
# comments: decadal means shown at bottom of file
#
# column_name 4: Berkeley
# long_name: Berkeley
# units: degrees C
# missing_value: N/A
# type (int/float/str): float
# comments: decadal means shown at bottom of file
#
# column_name 5: Kadow
# long_name: Kadow
# units: degrees C
# missing_value: N/A
# type (int/float/str): float
# comments: decadal means shown at bottom of file
#
# column_name 6: HadCRUT confidence limit upper
# long_name: HadCRUT confidence limit upper
# units: degrees C
# missing_value: N/A
# type (int/float/str): float
#
# column_name 7: HadCRUT confidence limit upper
# long_name: HadCRUT confidence limit upper
# units: degrees C
# missing_value: N/A
# type (int/float/str): float 
#
# --------------------------
# filename 7: Figure_2_11c-lower_panel.xlsx
# -----------------------
# comments: same as Figure_2_11c-lower_panel.csv but with the format used by the code that generates the figure
#
# NetCDF and BADC-CSV files contain metadata, providing information about what is available in the files
# --------------------------
