# Intermediate data behind SYR Figure 2.1

"Intermediate data" are products created by IPCC authors while processing the
input data (ensemble means, assessed ranges, regridded fields, …). They have
high reuse potential and are archived by the DDC at DKRZ and CSIC, and for
some WGI figures at CEDA.

## Where to look

| Archive | Collection | Access |
|---|---|---|
| DKRZ / WDCC | **IPCC-DDC_AR6_Supplements** – "input/source and intermediate datasets underlying the AR6", quality-checked by the DDC | https://www.wdc-climate.de/ui/project?acronym=IPCC-DDC_AR6_Supplements (click *Find data*) |
| DKRZ / WDCC | example entry: *IPCC AR6 WGI assessed GSAT projections* (Fig. 4.11) | doi:10.26050/WDCC/AR6.IPCC-DDC_AR6_Sup_GSATPr |
| CEDA | WGI intermediate data for Chapters 2, 3, 6, 7, 8, 12 and TS figures | table "Intermediate Data" in https://github.com/IPCC-WG1/CEDA_IPCC_AR6_WGI_Figures_data |
| CSIC-IFCA | Interactive Atlas regional products | https://interactive-atlas.ipcc.ch/ |
| Zenodo / GitHub | figure-generation code (WGI) | https://github.com/IPCC-WG1 ; Zenodo records "IPCC AR6 WGI – Figure x.y" |

## What exists for the four panels of Figure 2.1

| Panel | Intermediate record found? | Closest available material |
|---|---|---|
| (a) WGIII SPM.1 | no DDC record | the Zenodo ESSD workbook is itself an author-processed product (country × sector × gas, GWP100 applied); R code at github.com/mcc-apsis/AR6-Emissions-trends-and-drivers |
| (b) WGI Fig 2.5 | no | network-level global means are included in the CEDA final-data CSV (one column per network) |
| (c) WGI SPM.1 | no | CMIP6 ensemble mean and 5–95 % range (historical+ssp245, hist-nat) are stored *inside* the CEDA final-data file `gmst_changes_model_and_obs.csv` |
| (d) WGI SPM.2 | no | assessed likely ranges per driver are in `SPM2b.csv` / `SPM2c_data.csv`; attribution method in Gillett et al. (2021) and WGI Chapter 3 code (github.com/IPCC-WG1/Chapter-3_Fig*) |

So for this particular figure the "intermediate" tier is thin: the processed
ensemble statistics were archived together with the final data rather than as
separate intermediate datasets. The story notebook points this out explicitly.

## TODO

- [ ] Browse the DKRZ *Find data* list for IPCC-DDC_AR6_Supplements and record
      any entry relevant to GMST or attribution (the list is rendered by
      JavaScript and could not be read programmatically).
