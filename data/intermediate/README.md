# Intermediate data behind SYR Figure 2.1

"Intermediate data" are products created by IPCC authors while processing the
input data (ensemble means, assessed ranges, composites, emulator output …).
The DDC archives them at DKRZ and CSIC; for WGI, CEDA publishes them as
chapter-level *data for Figure x.y* and *Input data for Figure x.y* records.

## Where to look

| Archive | Collection | Access |
|---|---|---|
| DKRZ / WDCC | **IPCC-DDC_AR6_Supplements** – "input/source and intermediate datasets underlying the AR6", quality-checked by the DDC | https://www.wdc-climate.de/ui/project?acronym=IPCC-DDC_AR6_Supplements (click *Find data*) |
| DKRZ / WDCC | example entry: *IPCC AR6 WGI assessed GSAT projections* (Fig. 4.11) | doi:10.26050/WDCC/AR6.IPCC-DDC_AR6_Sup_GSATPr |
| CEDA | WGI chapter-level records, `https://dap.ceda.ac.uk/badc/ar6_wg1/data/ch_0N/` (figure data) and `…/inputdata_chN_figNN/` (input data) | index: https://github.com/IPCC-WG1/CEDA_IPCC_AR6_WGI_Figures_data ; catalogue: https://catalogue.ceda.ac.uk |
| CSIC-IFCA | Interactive Atlas regional products | https://interactive-atlas.ipcc.ch/ |
| Zenodo / GitHub | figure-generation code (WGI) | https://github.com/IPCC-WG1 ; Zenodo records "IPCC AR6 WGI – Figure x.y" |

## The chain for the four panels (records in this folder, all CC BY 4.0, verified 2026-10-13)

| Panel | Record here | Role in the chain | Live path under `dap.ceda.ac.uk/badc/ar6_wg1/data/` |
|---|---|---|---|
| (a) WGIII SPM.1 | none – no DDC record | the Zenodo workbook (country × sector × gas, GWP100 applied) is the processed table; R code at github.com/mcc-apsis/AR6-Emissions-trends-and-drivers | – |
| (b) concentrations | `wgi_ch2_fig2_4/` – WGI Fig 2.4 (doi:10.5285/60eeb3cce51a457cb5ee1c577a0c8674) | ice-core CO₂ / CH₄ / N₂O composites 0–2000 CE → the pre-instrumental part of the 1850–2019 series; per-network modern means are columns of the Fig 2.5 final file | `ch_02/ch2_fig04/v20221219/fig2_4b_data_v2.csv` |
| (c) temperature | `wgi_ch2_fig2_11/` – WGI Fig 2.11 (doi:10.5285/f3515388768344bfb2be0521f82388be) | the AR6 four-dataset mean 1850–2020 (annual), PAGES 2k 1–2000 CE, land vs ocean; the SPM.1 file carries the same annual series plus CMIP6 envelopes | `ch_02/ch2_fig11/v20220510/Figure2_11_panel_a.csv` |
| (d) attribution | `wgi_ch3_fig3_8/` – WGI Fig 3.8 (doi:10.5285/bf3d0b8a8c0d4ae19cfd994b6fef4a5c) | assessed likely ranges per driver **and** the lines of evidence they were assessed from (Ribes et al. 2021, Haustein et al. 2017, Gillett et al. 2021, Chapter 7 emulator, 13 CMIP6 models) | `ch_03/ch3_fig08/v20220613/drivers_observed_warming.csv` |
| (d), (b) scaling | `wgi_ch7_fig7_6/`, `wgi_ch7_fig7_8/` – WGI Figs 7.6, 7.8 (doi:10.5285/0dd364e74c254b64bb5fddb5dceed364, 10.5285/5ef11ad195844a59b83393870a5860e1) | effective radiative forcing 1750–2019 by agent → two-layer emulator → attributed GSAT change by agent (concentration-based); SPM.2(c) uses the emission-based Chapter 6 variant of the same chain | `ch_07/ch7_fig06/v20220721/AR6_ERF_1750-2019.csv`, `ch_07/ch7_fig08/v20220721/fig7.8.csv` |

So the intermediate tier for Figure 2.1 is **published, but under the chapter
figures** rather than under the SPM or SYR figure. The notebook (sections 3a, 3b)
and the story map (Step 3) show these records.

## Open items

- [ ] Browse the DKRZ *Find data* list for IPCC-DDC_AR6_Supplements and record
      any entry relevant to GMST or attribution (the list is rendered by
      JavaScript and could not be read programmatically on 2026-10-13).
