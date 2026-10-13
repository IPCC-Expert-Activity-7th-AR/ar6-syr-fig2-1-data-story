# Data provenance and licences

Every CEDA file under `data/` is an unmodified copy of the published record and is
also readable **live** from `https://dap.ceda.ac.uk/badc/ar6_wg1/data/<CEDA path>`
(the archive sends `Access-Control-Allow-Origin: *`, so the notebook fetches it
directly from the browser and falls back to the bundled copy). The WGIII panel-(a)
CSV is rebuilt from the published source workbook by
`scripts/build_wgiii_spm1_from_essd.py`.

All CEDA records were re-checked against `catalogue.ceda.ac.uk` on **2026-10-13**:
publication state, DOI resolution (all `10.5285/<uuid>` DOIs resolve to the
catalogue record) and byte-identity of the bundled copies.

## Final data (tier 4)

| Folder | Record | Version | DOI | Host | State (2026-10-13) | Licence | Files |
|---|---|---|---|---|---|---|---|
| `final/wgi_spm1/` | WGI – data for Figure SPM.1 | v20221116 (supersedes v20210809) | 10.5285/0b2759059ad6474098e40dad73e0a8ec | CEDA · `spm/spm_01/v20221116/` | citable, DOI minted 2023-07-03 | CC BY 4.0 | `SPM1_1850-2020_obs.csv`, `SPM1_1-2000_recon.csv`, `spm1_6500_recon.csv`, `gmst_changes_model_and_obs.csv`, README, License |
| `final/wgi_spm2/` | WGI – data for Figure SPM.2 | v20210809 | 10.5285/c1eb6dad1598427f8f9f3eae346ece2f | CEDA · `spm/spm_02/v20210809/` | published | CC BY 4.0 | `SPM2a.csv`, `SPM2b.csv`, `SPM2c_data.csv`, README, License |
| `final/wgi_ch2_fig2_5/` | WGI Chapter 2 – data for Figure 2.5 | v20221116 | 10.5285/c6f19b27f8e74e98968c17c8e1f74c60 | CEDA · `ch_02/ch2_fig05/v20221116/` | citable | CC BY 4.0 | `Data_Figure_2.5.csv`, README, License |
| `final/wgiii_spm1/` | rebuilt from Minx et al. 2021 ESSD dataset (source of WGIII Figure SPM.1) | Zenodo v. 2022-04-25 | source 10.5281/zenodo.6483002; official figure record 10.48490/vfxm-tm28 | Zenodo / IPCC Data Catalogue (MetadataWorks) | – | CC BY 4.0 | `global_ghg_emissions_by_gas_1970-2019.csv` |
| `final/syr_fig2_1/` | SYR LR Figure 2.1 (c), (d) | v1.0.0 (2025-04) | 10.7927/nq55-cr83, 10.7927/b38b-zp83 | CIESIN / SEDAC | browser-only | see landing page | **to be downloaded** (see README) |

## Intermediate tier (3) – chapter-level CEDA records that form the chain to Figure 2.1

CEDA catalogues these as *data for Figure x.y* of their own chapter; relative to
SYR Figure 2.1 they are the intermediate products (ice-core composites, four-dataset
mean, lines of evidence, forcing → warming by agent).

| Folder | Record | Version | DOI | CEDA path | State | Files |
|---|---|---|---|---|---|---|
| `intermediate/wgi_ch2_fig2_4/` | WGI Chapter 2 – data for Figure 2.4 (ice-core GHG concentrations, Ahn) | v20221219 | 10.5285/60eeb3cce51a457cb5ee1c577a0c8674 | `ch_02/ch2_fig04/v20221219/` | citable, DOI 2023-07-03 | `fig2_4b_data_v2.csv` (0–2000 CE: Law Dome, EDML, WAIS Divide, H15, GISP2, Styx, NEEM, EURO cores + composites), README, License |
| `intermediate/wgi_ch2_fig2_11/` | WGI Chapter 2 – data for Figure 2.11 (Trewin, Kaufman) | v20220510 | 10.5285/f3515388768344bfb2be0521f82388be | `ch_02/ch2_fig11/v20220510/` | citable, DOI 2023-07-03 | `Figure2_11_panel_a.csv` (AR6 4-dataset mean 1850–2020), `Figure_2_11a-PAGES_2k_Consortium.csv`, `Figure_2_11c-land_and_ocean_time_series.csv`, README, License |
| `intermediate/wgi_ch3_fig3_8/` | WGI Chapter 3 – data for Figure 3.8 (Gillett, Malinina) | v20220613 | 10.5285/bf3d0b8a8c0d4ae19cfd994b6fef4a5c | `ch_03/ch3_fig08/v20220613/` | citable, DOI 2023-02-08 | `drivers_observed_warming.csv` (assessed ranges + Ribes/Haustein/Gillett/Ch.7 estimates + 13 CMIP6 models), README, License |
| `intermediate/wgi_ch7_fig7_6/` | WGI Chapter 7 – data for Figure 7.6 (ERF 1750–2019) | v20220721 | 10.5285/0dd364e74c254b64bb5fddb5dceed364 | `ch_07/ch7_fig06/v20220721/` | citable, DOI 2023-07-06 | `AR6_ERF_1750-2019.csv` (best estimate; 5 % / 95 % files remain online), README, LICENSE |
| `intermediate/wgi_ch7_fig7_8/` | WGI Chapter 7 – data for Figure 7.8 (attributed GSAT change 1750–2019) | v20220721 | 10.5285/5ef11ad195844a59b83393870a5860e1 | `ch_07/ch7_fig08/v20220721/` | citable, DOI 2023-07-06 | `fig7.8.csv` (p05 / best / p95 per agent), README, LICENSE |

## Input tier (2)

| Folder | Record | Version | DOI | CEDA path | State | Files |
|---|---|---|---|---|---|---|
| `input/wgi_ch2_fig2_11_input/` | WGI Chapter 2 – **Input data** for Figure 2.11 (Trewin, Kaufman) | v20220428 | 10.5285/033cd690801741c9bc745b8da55faef4 | `ch_02/inputdata_ch2_fig11/v20220428/` | citable, DOI 2023-07-03 | `Figure_2_11c-lower_panel.csv` (HadCRUT5, NOAAGlobalTemp, Berkeley Earth, Kadow 1850–2020 + decadal means); HadCRUT trend/significance grids remain online |
| `input/README.md` | documentation of every other input (EDGAR, bookkeeping models, networks, PAGES 2k, CMIP6 at DKRZ) | – | – | – | – | – |

## Other CEDA records checked but not bundled

| Record | DOI | Why not bundled |
|---|---|---|
| WGI SPM.1 v20210809 | 10.5285/76cad0b4f6f141ada1c44a4ce9e7d4bd | superseded by v20221116 (same values, BADC-CSV headers added) |
| WGI Chapter 3 – data for Figure 3.4 | 10.5285/06a4ad1656774087a5b6db3c7a57211e | NetCDF only (observed vs simulated GSAT); SPM.1(b) carries the same envelopes as CSV |
| WGI Chapter 2 – Input data for Figure 2.2 | 10.5285/fe8d7ad6c1284677994c6643e1e55bbb | solar / volcanic forcing inputs, not used by Figure 2.1 |
| WGI Chapter 7 – Input data for Figures 7.3, 7.4, 7.5 | 10.5285/6842c53c…, d32090ff…, 7b3d379f… | energy-budget / aerosol ERF inputs, upstream of Figure 7.6 |
| IPCC AR6 Synthesis Report (SYR) dataset collection | uuid 9177e927f0664da9bf1e25f57561d0d8 | **not yet published** (2026-10-13) |

## How to cite

CEDA records require two citations: the dataset and the report component. Example for SPM.1:

> Gillett, N.P.; Kaufman, D.; Neukom, R. (2022): Summary for Policymakers of the Working Group I Contribution to the IPCC Sixth Assessment Report – data for Figure SPM.1 (v20221116). NERC EDS Centre for Environmental Data Analysis. https://doi.org/10.5285/0b2759059ad6474098e40dad73e0a8ec
>
> IPCC, 2021: Summary for Policymakers. In: Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [Masson-Delmotte, V., et al. (eds.)]. Cambridge University Press, pp. 3−32, doi:10.1017/9781009157896.001.

Chapter-level records cite the chapter instead, e.g. Gulev et al. (2021) *Changing State of the Climate System* (Chapter 2),
Eyring et al. (2021) *Human Influence on the Climate System* (Chapter 3), Forster et al. (2021) *The Earth's Energy Budget,
Climate Feedbacks, and Climate Sensitivity* (Chapter 7) — the exact text is in each record's `License.txt`.

For the figure itself:

> IPCC, 2023: Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [Core Writing Team, H. Lee and J. Romero (eds.)]. IPCC, Geneva, Switzerland, pp. 35–115, doi:10.59327/IPCC/AR6-9789291691647. Figure 2.1.

Reproduction of IPCC figure *images* is governed by the IPCC copyright policy
(https://www.ipcc.ch/copyright/); this project redraws the panels from the
openly licensed data instead of reusing the published image.
