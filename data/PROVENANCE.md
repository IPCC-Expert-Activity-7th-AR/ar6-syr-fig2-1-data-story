# Data provenance and licences

Every file under `data/final/` is an unmodified copy of a published record,
except the WGIII panel-(a) CSV which is rebuilt from the published source
workbook by `scripts/build_wgiii_spm1_from_essd.py`.

| Folder | Record | Version | DOI | Host (DDC) | Licence | Files |
|---|---|---|---|---|---|---|
| `final/wgi_spm1/` | WGI – data for Figure SPM.1 | v20221116 | 10.5285/0b2759059ad6474098e40dad73e0a8ec | CEDA | CC BY 4.0 | `SPM1_1850-2020_obs.csv`, `SPM1_1-2000_recon.csv`, `spm1_6500_recon.csv`, `gmst_changes_model_and_obs.csv`, README, License |
| `final/wgi_spm2/` | WGI – data for Figure SPM.2 | v20210809 | 10.5285/c1eb6dad1598427f8f9f3eae346ece2f | CEDA | CC BY 4.0 | `SPM2a.csv`, `SPM2b.csv`, `SPM2c_data.csv`, README, License |
| `final/wgi_ch2_fig2_5/` | WGI Chapter 2 – data for Figure 2.5 | v20221116 | 10.5285/c6f19b27f8e74e98968c17c8e1f74c60 | CEDA | CC BY 4.0 | `Data_Figure_2.5.csv`, README, License |
| `final/wgiii_spm1/` | rebuilt from Minx et al. 2021 ESSD dataset (source of WGIII Figure SPM.1) | Zenodo v. 2022-04-25 | source 10.5281/zenodo.6483002; official figure record 10.48490/vfxm-tm28 | Zenodo / IPCC Data Catalogue (MetadataWorks) | CC BY 4.0 | `global_ghg_emissions_by_gas_1970-2019.csv` |
| `final/syr_fig2_1/` | SYR LR Figure 2.1 (c), (d) | v1.0.0 (2025-04) | 10.7927/nq55-cr83, 10.7927/b38b-zp83 | CIESIN / SEDAC | see landing page | **to be downloaded** (see README) |
| `input/` | documentation only | – | – | DKRZ (CMIP6), originating networks | – | README |
| `intermediate/` | documentation only | – | – | DKRZ, CSIC, CEDA | – | README |

## How to cite

CEDA records require two citations: the dataset and the report component. Example for SPM.1:

> Gillett, N.P.; Kaufman, D.; Neukom, R. (2022): Summary for Policymakers of the Working Group I Contribution to the IPCC Sixth Assessment Report – data for Figure SPM.1 (v20221116). NERC EDS Centre for Environmental Data Analysis. https://doi.org/10.5285/0b2759059ad6474098e40dad73e0a8ec
>
> IPCC, 2021: Summary for Policymakers. In: Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [Masson-Delmotte, V., et al. (eds.)]. Cambridge University Press, pp. 3−32, doi:10.1017/9781009157896.001.

For the figure itself:

> IPCC, 2023: Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [Core Writing Team, H. Lee and J. Romero (eds.)]. IPCC, Geneva, Switzerland, pp. 35–115, doi:10.59327/IPCC/AR6-9789291691647. Figure 2.1.

Reproduction of IPCC figure *images* is governed by the IPCC copyright policy
(https://www.ipcc.ch/copyright/); this project redraws the panels from the
openly licensed data instead of reusing the published image.
