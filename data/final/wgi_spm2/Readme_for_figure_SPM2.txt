# Creation date (YYYY-MM-DD): 2021-07-12 
# File created by: 
# Sophie Szopa
# email: sophie.szopa@lsce.ipsl.fr
# -
# Lina Sitz
# email: linasitz@gmail.com
#-
# Elizaveta Malinina
# email: ---
# ========================
# GENERAL INFORMATION 
# 
# *Title 
# Readme for data for Figure SPM2 from the Summary for Policymakers of the Working Group I (WGI) Contribution to the Intergovernmental Panel on Climate Change (IPCC) Sixth Assessment Report (AR6).
# 
# ========================
# DATA & FILE OVERVIEW
#
# List of all files and subfolders
# 
# --------------------------
# Panel a
#
# --------------------------
#
# *Data creators
# Name: Nathan Gillett
# Name: Peter Thorne
# Name: Blair Trewin
#
# --------------------------
# filename 1: ‘SPM2a.csv’
# --------------------------
# N° of columns: 2
# Column headings: --, Observed warming (observations)
#        
#
# column_name 1: --
# type (int/float/char): char
# comments: Mean is the best estimate, top and bottom are borders of the likely range.
#
# column_name 2: Observations
# units: Degrees C
# type (int/float/char): float
# comments: The global surface temperature warming (2010-2019) relative to 1850-1900 calculated from HadCRUT4.6 observations.
#
# --------------------------
# Panel b
#
# --------------------------
#
# *Data creators: Same for panel a.
#
# --------------------------
# filename 1: ‘SPM2b.csv’
# --------------------------
# N° of columns: 6
# Column headings: ---, Total human influence, Well-mixed greenhouse gases, Other human drivers, Solar and volcanic drivers, Internal variability
#        
#
# column_name 1: ----
# type (int/float/char): str
# comments: For total human influence the mean value is the assessed best estimate, and for the other bars it is the mid-point of the assessed likely range. Top and bottom are the borders of the likely range.
#
# column_name 2: Total human influence
# units: Degrees C
# type (int/float/char): float
# comments: The global surface temperature warming (2010-2019) relative to 1850-1900 calculated from CMIP6 model ensemble simulated with anthropogenic and natural forcings (historical-ssp245).
#
# column_name 3: Well-mixed greenhouse gases
# units: Degrees C
# type (int/float/char): float
# comments: The global surface temperature warming (2010-2019) relative to 1850-1900 calculated from CMIP6 model ensemble simulated with anthropogenic greenhouse gases forcings (hist-GHG).
#
# column_name 4: Other human drivers
# units: Degrees C
# type (int/float/char): float
# comments: The global surface temperature warming (2010-2019) relative to 1850-1900 calculated from CMIP6 model ensemble simulated with anthropogenic aerosol forcings (hist-aer).
#
# column_name 5: Solar and volcanic drivers
# units: Degrees C
# type (int/float/char): float
# comments: The global surface temperature warming (2010-2019) relative to 1850-1900 calculated from CMIP6 model ensemble simulated with natural forcings only (hist-nat).
#
# column_name 6: Internal variability
# units: Degrees C
# type (int/float/char): float
# comments: The global surface temperature warming  internal variability was calculated from CMIP6 model ensemble. Its assessment of is presented in AR6 WGI Chapter 3. 
#
# --------------------------
# Panel c
#
# --------------------------
#
# *Data creators
# Name: Sophie Szopa
# Institution: Laboratoire des Sciences du Climat et de l’Environnement
# email: sophie.szopa@lsce.ipsl.fr
#
# Name: Chris Smith
# Institution: School of Earth and Environment, University of Leeds
# email: C.J.Smith1@leeds.ac.uk 
#
# Name: Sara Blichner
# Institution: University of Oslo
# email: s.m.blichner@geo.uio.no
#
# Name: Terje Berntsen 
# Institution: University of Oslo 
# email: t.k.berntsen@geo.uio.no 
#
# Name: Bill Collins
# Institution: University of Reading
# email: w.collins@reading.ac.uk
#
# *Comments
# Data based on Chapter 6 for emission-based GSAT effects, same methodology as in Figure 6.12 for all data - Data based on Chapter 7 for surface reflectance from land-use and light-absorbing aerosol on snow and ice, and contrails and aviation induced cirrus, same methodology as in Figure 7.7.
# Note that Figures in chapters 6 and 7 are for a different time period
# Data from Chapter 6: estimate of historical emission-based ERF timeseries combining ESM aerchemmip results and constrains from multiple line of evidence from chapter 7 with a methodology described in 6.SM.1 are used to estimate the GSAT change based on Impulse Response Functions as described in 6.SM.2
# Data from Chapter 7: best estimate of historical ERF timeseries described in 7.SM.1.3. are used in constrained emulator (two-layer energy balance model) to infer an ensemble of temperature change timeseries as described in 7.SM.2.2 and 7.SM.7.3
#
# --------------------------
# filename 1: ‘SPM2c_data.csv’
# --------------------------
# N° of columns: 4
# Column headings: Driver, Total GSAT effect, 5% very likely lower limit, 95% very likely upper limit
#        
# column_name 1: Driver
# type (int/float/char): str
# comments: Drivers are emission (for CO2, CH4, N2O, Halogenated gases, NOx, NMVOC+CO, Organic carbon, Black carbon, Ammonia) or change in land-use or change in contrails due to aviation.
#
# column_name 2: Total GSAT effect
# long_name: 50th percentile of the temperature change in 2010-2019 relative to 1850-1900 considered as the best estimate
# units: °C
# missing_value: -
# type (int/float/char): float
# comments: The GSAT effect due to aerosols consider both the effect through radiation and the effect though cloud changes. For CH4, GSAT change accounts for effect of CH4 emissions on concentrations of CH4 (incl. effect on its own lifetime), CO2, O3, stratospheric H2O and aerosols; For N2O, GSAT change accounts for effect of N2O emissions on concentrations of N2O, CH4, O3 and aerosols; For halogenated gases, GSAT change accounts for effect of halogenated gases emissions on concentrations of halogenated gases, CH4, O3 and aerosols; For NOx, GSAT change accounts for effect of NOx emissions on concentrations of CH4, O3 and aerosols; For NMVOC+CO, GSAT change accounts for effect of NMVOC+CO emissions on concentrations of CO2, CH4, O3 and aerosols; For SO2, for OC and for ammonia, GSAT change accounts for effect on concentrations of aerosols;  For black carbon, GSAT change accounts for effect on concentrations of aerosols and deposition on snow and ice
#
# column_name 3: 5% very likely lower limit
# long_name: 5th percentile of the temperature change in 2010-2019 relative to 1850-1900 considered as the lower limit of the very likely range
# units: °C
# missing_value: -
# type (int/float/char): float
# comments: For black carbon, the uncertainty is computed as the square root of (BC_LAP_uncertainty^2 + BC_(aci+ari)_uncertainty^2)
#
# column_name 4: 95% very likely lower limit
# long_name: 95th percentile of the temperature change in 2010-2019 relative to 1850-1900 considered as the upper limit of the very likely range
# units: °C
# missing_value: -
# type (int/float/char): float
# comments: For black carbon, the uncertainty is computed as the square root of (BC_LAP_uncertainty^2 + BC_(aci+ari)_uncertainty^2)
#
# ========================
