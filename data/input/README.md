# Input data behind SYR Figure 2.1

"Input data" are the observations, inventories and model simulations the IPCC
authors started from. The IPCC Data Distribution Centre (DDC) archives model
input at DKRZ; observational inputs stay with the originating institutions and
are cited in the report (WGI Annex III, WGI Chapter 2 FAIR tables, WGIII
Chapter 2 Supplementary Material). Nothing in this folder is redistributed;
this file documents where everything comes from.

## Panel (a) – global GHG emissions 1990–2019 (via WGIII Figure SPM.1)

| Component | Source | Access |
|---|---|---|
| CO2 fossil fuel & industry, CH4, N2O, F-gases | EDGAR v6.0 (EU Joint Research Centre), country × sector × gas | https://edgar.jrc.ec.europa.eu/ |
| CO2 land use, land-use change and forestry | mean of three bookkeeping models: BLUE, Houghton & Nassikas 2017, OSCAR (Global Carbon Budget) | https://globalcarbonbudget.org/ |
| Harmonised compilation used by WGIII Ch. 2 | Minx et al. (2021) ESSD 13, 5213–5252, doi:10.5194/essd-13-5213-2021 | Zenodo doi:10.5281/zenodo.6483002 (xlsx); code https://github.com/mcc-apsis/AR6-Emissions-trends-and-drivers |
| GWP100 metric | IPCC AR6 WGI Chapter 7 Table 7.15 | included in the Zenodo workbook, sheet `100_yr_gwps` |

## Panel (b) – CO2, CH4, N2O concentrations (via WGI Figure 2.5)

Globally averaged dry-air mole fractions assessed in WGI Chapter 2 (Section 2.2.3).

| Network | Species | Period | Access |
|---|---|---|---|
| NOAA Global Monitoring Laboratory | CO2, CH4, N2O | CO2 1979–2019 (global), CH4 1983–, N2O 1978– | https://gml.noaa.gov/ccgg/trends/ |
| Scripps Institution of Oceanography (SIO) | CO2 (Mauna Loa, from 1958) | 1958–2019 | https://scrippsco2.ucsd.edu/ |
| CSIRO (incl. Cape Grim) | CO2, CH4, N2O | 1992–2019 | https://www.csiro.au/greenhouse-gases |
| AGAGE | CH4, N2O | 1987–/1979– | https://agage.mit.edu/ |
| UCI (Blake/Rowland) | CH4 | 1978–2019 | https://ps.uci.edu/~rowlandblake/ |

The CEDA record for Figure 2.5 (`../final/wgi_ch2_fig2_5/`) keeps each network's series as separate columns.

## Panel (c) – observed global surface temperature (via WGI Figure SPM.1)

| Component | Source |
|---|---|
| 1850–2020 GMST, AR6 Chapter 2 assessed mean | average of HadCRUT5 (Morice et al. 2021), NOAAGlobalTemp-Interim (Vose et al. 2021), Berkeley Earth (Rohde & Hausfather 2020), Kadow et al. (2020) |
| 1–2000 CE reconstruction | PAGES 2k Consortium (2019), Nature Geoscience 12, 643–649, doi:10.1038/s41561-019-0400-0 |
| Mid-Holocene (~6500 yr BP) warm period range | WGI Chapter 2 assessment (Section 2.3.1.1) |
| CMIP6 historical+ssp245 and hist-nat ensembles (SPM.1 panel b) | IPCC DDC at DKRZ, project **IPCC-AR6_CMIP6**, https://www.wdc-climate.de/ui/project?acronym=IPCC-AR6_CMIP6 – per-model/per-experiment DOIs `10.26050/WDCC/AR6.*`, CC BY 4.0; 65,118 archived datasets (see https://github.com/IPCC-WG1/DDC-AR6-CMIP6-Data-Archival) |

## Panel (d) – contributions to observed warming (via WGI Figure SPM.2)

| Component | Source |
|---|---|
| Observed warming 2010–2019 vs 1850–1900 | HadCRUT4.6 (Morice et al. 2012) – 1.06 °C, likely 0.88–1.21 |
| Total human influence, GHG, other human drivers, natural | CMIP6 DAMIP experiments historical-ssp245, hist-GHG, hist-aer, hist-nat (Gillett et al. 2021, Nature Climate Change, doi:10.1038/s41558-020-00965-9) – archived at DKRZ in **IPCC-AR6_CMIP6** |
| Per-driver contributions (SPM.2 panel c) | WGI Chapter 7 effective radiative forcing × climate response (Smith et al.; Chapter 7 code https://github.com/IPCC-WG1/Chapter-7) |

## Not in the DDC

Observational networks (NOAA, SIO, CSIRO, AGAGE, UCI, HadCRUT, Berkeley Earth,
PAGES 2k) and inventories (EDGAR, Global Carbon Budget) publish their own data;
the IPCC cites them rather than re-hosting them. Re-users should go to the
originating institution and follow its licence.
