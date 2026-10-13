#!/usr/bin/env python3
"""Generate the JupyterGIS Story Map (storymap/ipcc_ar6_data_journey.jGIS).

Structure follows the IPCC data-management chain for SYR Figure 2.1:

  Step 1  The report and the figure           (IPCC, Geneva)
  Step 2  Input data        – DKRZ / CSIC + originating observatories & inventories
  Step 3  Intermediate data – DKRZ / CSIC / CEDA + code on GitHub/Zenodo
  Step 4  Final data        – CEDA (WGI), IPCC Data Catalogue (WGIII), CIESIN-SEDAC (SYR)
  Status  One-page availability dashboard and how to reuse

Each stop carries the concrete record details (catalogue, DOI, version, files,
licence) and an availability status:
  [AVAILABLE]  downloaded and bundled in this project
  [ONLINE]     exists, link only (not redistributed here)
  [PARTIAL]    exists but could not be fully verified / no Figure-2.1 entry
  [MISSING]    no record exists

The .jGIS format is the JSON document used by JupyterGIS (schemaVersion 0.6.0).
Coordinates are stored in EPSG:3857 (Web Mercator metres).
"""
import json
import math
import pathlib
import uuid

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "storymap" / "ipcc_ar6_data_journey.jGIS"

R = 6378137.0


def merc(lon: float, lat: float):
    x = math.radians(lon) * R
    y = math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)) * R
    return x, y


def extent(lon, lat, zoom, w_px=1200, h_px=800):
    x, y = merc(lon, lat)
    mpp = 2 * math.pi * R / 256 / 2 ** zoom
    dx, dy = w_px / 2 * mpp, h_px / 2 * mpp
    return [x - dx, y - dy, x + dx, y + dy]


def uid():
    return str(uuid.uuid4())


# ------------------------------------------------------------------ places --
# key: (name, lon, lat, colour)
PLACES = {
    "ipcc":   ("IPCC Secretariat, Geneva – Figure 2.1 published", 6.1400, 46.2220, "#1f4e79"),
    "mlo":    ("Mauna Loa Observatory (NOAA GML / SIO) – CO2 input", -155.5763, 19.5362, "#2e7d32"),
    "cgo":    ("Cape Grim (CSIRO / AGAGE) – CH4, N2O input", 144.6900, -40.6830, "#2e7d32"),
    "exeter": ("Met Office Hadley Centre, Exeter – HadCRUT input", -3.4740, 50.7270, "#2e7d32"),
    "ispra":  ("JRC Ispra – EDGAR emissions inventory input", 8.6280, 45.8100, "#2e7d32"),
    "mcc":    ("MCC Berlin – WGIII emissions compilation (Minx et al.)", 13.4050, 52.5200, "#2e7d32"),
    "dkrz":   ("DKRZ, Hamburg – DDC: CMIP6 input + intermediate archive", 9.9800, 53.5680, "#b26a00"),
    "csic":   ("CSIC-IFCA, Santander – DDC: Interactive Atlas", -3.8040, 43.4710, "#b26a00"),
    "ceda":   ("CEDA, Harwell – DDC: WGI final + intermediate figure data", -1.3140, 51.5740, "#c62828"),
    "ciesin": ("CIESIN / SEDAC, Palisades NY – DDC: SYR final figure data", -73.9120, 41.0040, "#c62828"),
}

WORLD = (10.0, 30.0, 1.4)   # lon, lat, zoom for full-screen markdown segments
EUROPE = (4.0, 49.5, 4.2)

# ---------------------------------------------------------------- segments --
# (title, place-key or (lon,lat,zoom) tuple, contentMode, markdown)
SEGMENTS = [
    # ------------------------------------------------------------------ intro
    (
        "The data behind IPCC AR6 SYR Figure 2.1",
        WORLD, "markdown",
        """
## From emissions to warming — and the data behind one IPCC figure

This story follows **IPCC AR6 Synthesis Report, Longer Report Figure 2.1** through the four steps of the IPCC data chain:

| Step | Question | Where to look |
|---|---|---|
| **1 · The report** | What is the figure and where does it come from? | ipcc.ch (SYR SPM → Longer Report → Figure 2.1) |
| **2 · Input data** | Which observations, inventories and simulations were used? | DKRZ, CSIC + the originating institutions |
| **3 · Intermediate data** | What did authors compute along the way? | DKRZ, CSIC, CEDA + code on GitHub/Zenodo |
| **4 · Final data** | Which numbers are plotted, and can I download them? | CEDA (WGI), IPCC Data Catalogue (WGIII), CIESIN-SEDAC (SYR) |

Every stop lists the concrete record (catalogue, DOI, version, files, licence) and a status flag:
`AVAILABLE` bundled in this project · `ONLINE` link only · `PARTIAL` incomplete / unverified · `MISSING` no record.

Use **▶ Next** to start at Step 1. The companion notebook `ar6_syr_fig2_1_data_story.ipynb` reproduces the four panels from the Step-4 data.
""",
    ),
    # ----------------------------------------------------------------- step 1
    (
        "Step 1 · The report: AR6 Synthesis Report → Figure 2.1",
        "ipcc", "map",
        """
**Status: `ONLINE` — figure and caption published; image under IPCC copyright policy.**

* Report: *Climate Change 2023: Synthesis Report* (approved 19 March 2023), doi:10.59327/IPCC/AR6-9789291691647
* Entry point: [Summary for Policymakers](https://www.ipcc.ch/report/ar6/syr/summary-for-policymakers/) → Longer Report Section 2.1
* Figure page: [ipcc.ch/report/ar6/syr/figures/figure-2-1](https://www.ipcc.ch/report/ar6/syr/figures/figure-2-1)
* Title: *The causal chain from emissions to resulting warming of the climate system*

**Four panels and their Working-Group sources** (from the caption's traceability tag
`{WGI SPM A.2.2, WGI Figure SPM.1, WGI Figure SPM.2, WGI TS2.2, WGI 2.1; WGIII Figure SPM.1, WGIII A.III.II.2.5.1}`):

| Panel | Content | Source figure |
|---|---|---|
| (a) | Global net anthropogenic GHG emissions 1990–2019 by gas | **WGIII Figure SPM.1** |
| (b) | CO₂, CH₄, N₂O concentrations, panel heights scaled to warming effect | **WGI Section 2.1 / Figure 2.5** |
| (c) | Global surface temperature vs 1850–1900 + warmest period of last 100 000 yr | **WGI Figure SPM.1** |
| (d) | Warming 1850–1900 → 2010–2019 attributed to human / natural drivers | **WGI Figure SPM.2** |

The SYR is a synthesis, so its data are re-publications of WG data. Steps 2–4 follow those references.
""",
    ),
    (
        "Step 1 · How the IPCC organises data: three tiers, five archives",
        WORLD, "markdown",
        """
## The IPCC Data Distribution Centre (DDC) model for AR6

| Tier | Definition (DDC) | AR6 archive | Identifier pattern |
|---|---|---|---|
| **Input data** | observations, inventories, model simulations the authors started from | **DKRZ** (CMIP6 subset), **CSIC** (Atlas inputs); observational inputs stay with originating networks | `10.26050/WDCC/AR6.*` |
| **Intermediate data** | products created by authors while processing inputs, with high reuse potential | **DKRZ** `IPCC-DDC_AR6_Supplements`, **CSIC**, selected WGI figures at **CEDA** | `10.26050/WDCC/AR6.IPCC-DDC_AR6_Sup_*`, `10.5285/*` |
| **Final data** | the numbers plotted in published figures/tables | WGI/WGII → **CEDA**; WGIII → **IPCC Data Catalogue (MetadataWorks)**; SYR → **CIESIN / NASA SEDAC** | `10.5285/*`, `10.48490/*`, `10.7927/*` |

DDC partners: DKRZ (Germany), CSIC-IFCA (Spain), CIESIN (USA), MetadataWorks (UK); CEDA (UK) is the WGI/WGII final-data archive.
Portal: [ipcc-data.org](https://ipcc-data.org) · Catalogue: [ipcc-browser.ipcc-data.org](https://ipcc-browser.ipcc-data.org)

**Overall status for Figure 2.1 (checked 2026-10-13)**

| Tier | (a) emissions | (b) concentrations | (c) temperature | (d) attribution |
|---|---|---|---|---|
| Input | `ONLINE` EDGAR, GCB bookkeeping, Zenodo workbook | `ONLINE` NOAA/SIO/CSIRO/AGAGE/UCI | `ONLINE` HadCRUT5 etc., PAGES2k; CMIP6 at DKRZ | `ONLINE` HadCRUT4.6; CMIP6 DAMIP at DKRZ |
| Intermediate | `PARTIAL` no DDC record; processed table = Zenodo workbook | `PARTIAL` per-network means inside final file | `PARTIAL` ensemble stats inside final file | `PARTIAL` assessed ranges inside final file |
| Final (WG) | `AVAILABLE`* WGIII SPM.1 (10.48490/vfxm-tm28) | `AVAILABLE` WGI Fig 2.5 (CEDA) | `AVAILABLE` WGI SPM.1 (CEDA) | `AVAILABLE` WGI SPM.2 (CEDA) |
| Final (SYR) | `MISSING` | `MISSING` | `PARTIAL` 10.7927/nq55-cr83 (xlsx not yet fetched) | `PARTIAL` 10.7927/b38b-zp83 (xlsx not yet fetched) |

\\* rebuilt from the published Zenodo source because the catalogue site is browser-only.
""",
    ),
    # ----------------------------------------------------------------- step 2
    (
        "Step 2 · Input data — overview",
        EUROPE, "markdown",
        """
## Step 2 · Input data: what the authors started from

The DDC archives **model** input at DKRZ (and Atlas inputs at CSIC). **Observational** input is not re-hosted:
the IPCC cites it to the producing institution (WGI Annex III, Chapter 2 FAIR tables, WGIII Chapter 2 SM).

| Panel | Input datasets | Holder | Status |
|---|---|---|---|
| (a) | EDGAR v6.0 (fossil CO₂, CH₄, N₂O, F-gases, country × sector); CO₂-LULUCF = mean of BLUE, Houghton & Nassikas, OSCAR; harmonised in Minx et al. (2021) workbook | JRC Ispra; Global Carbon Budget; MCC Berlin → Zenodo 10.5281/zenodo.6483002 | `ONLINE` (Zenodo workbook used to rebuild panel a) |
| (b) | Global mean dry-air mole fractions from NOAA GML, SIO, CSIRO, AGAGE, UCI | each network | `ONLINE` (network series are columns of the CEDA final file) |
| (c) | HadCRUT5, NOAAGlobalTemp-Interim, Berkeley Earth, Kadow et al. 2020 (Ch.2 assessed mean); PAGES 2k (1–2000 CE); mid-Holocene assessment; CMIP6 historical+ssp245, hist-nat | Met Office/UEA, NOAA, Berkeley Earth, PAGES; **DKRZ `IPCC-AR6_CMIP6`** | `ONLINE` |
| (d) | HadCRUT4.6; CMIP6 DAMIP hist-GHG, hist-aer, hist-nat, historical+ssp245 (Gillett et al. 2021) | Met Office/UEA; **DKRZ `IPCC-AR6_CMIP6`** | `ONLINE` |

Next stops visit the DDC input archive (DKRZ, CSIC) and five originating sites.
Full tables with links: `data/input/README.md` in the project.
""",
    ),
    (
        "Step 2 · DKRZ Hamburg — the CMIP6 input archive",
        "dkrz", "map",
        """
**Status: `ONLINE` — complete, citable, CC BY 4.0.**

* Archive: World Data Center for Climate (WDCC) at DKRZ, DDC project **`IPCC-AR6_CMIP6`**
  — [wdc-climate.de/ui/project?acronym=IPCC-AR6_CMIP6](https://www.wdc-climate.de/ui/project?acronym=IPCC-AR6_CMIP6)
* Content: the CMIP6 subset used by WGI authors — **65 118 datasets** from ~120 models / 45 institutions
  (lists compiled from chapter requests; documented at github.com/IPCC-WG1/DDC-AR6-CMIP6-Data-Archival)
* Granularity: one entry per model × experiment (e.g. *IPCC DDC: CAS FGOALS-g3 model output prepared for CMIP6*,
  doi:10.26050/WDCC/AR6.C6CMCASFGO); regional subsets also catalogued
* Relevance to Figure 2.1: panel (c) model envelopes (`historical`+`ssp245`, `hist-nat`) and panel (d) attribution
  experiments (`hist-GHG`, `hist-aer`, `hist-nat`) are computed from these files
* Access: *Find data* on the project page → entry → download (registration for bulk access); licence CC BY 4.0
""",
    ),
    (
        "Step 2 · CSIC-IFCA Santander — Atlas inputs",
        "csic", "map",
        """
**Status: `ONLINE` — not a direct source of Figure 2.1.**

* CSIC-IFCA hosts the WGI **Interactive Atlas** ([interactive-atlas.ipcc.ch](https://interactive-atlas.ipcc.ch))
  and, with DKRZ, the DDC long-term archive for input and intermediate datasets.
* The Atlas re-uses the same observational and CMIP6 inputs regionally; Figure 2.1 is global, so no Atlas product feeds it.
* Useful for readers who want regional versions of panels (c)/(d) (regional warming, attribution by region).
""",
    ),
    (
        "Step 2 · Mauna Loa — CO₂ since 1958 (panel b)",
        "mlo", "map",
        """
**Status: `ONLINE` — originating network, cited not re-hosted.**

* NOAA Global Monitoring Laboratory + Scripps Institution of Oceanography records; global means from the NOAA network
  ([gml.noaa.gov/ccgg/trends](https://gml.noaa.gov/ccgg/trends/), [scrippsco2.ucsd.edu](https://scrippsco2.ucsd.edu/))
* In the CEDA final file for WGI Figure 2.5 these appear as columns `NOAA_CO2`, `SIO_CO2`, `CSIRO_CO2` (1958/1979–2019)
* 2019 annual mean: ≈ 410 ppm (NOAA global); growth-rate columns (`*_gr`) are the inset of Figure 2.5
""",
    ),
    (
        "Step 2 · Cape Grim — CH₄ and N₂O (panel b)",
        "cgo", "map",
        """
**Status: `ONLINE` — originating network, cited not re-hosted.**

* CSIRO / Bureau of Meteorology baseline station; member of **AGAGE**
  ([csiro.au/greenhouse-gases](https://www.csiro.au/greenhouse-gases), [agage.mit.edu](https://agage.mit.edu/))
* CEDA Figure 2.5 columns: `AGAGE_CH4` (1987–), `AGAGE_N2O` (1979–), `CSIRO_CH4`, `CSIRO_N2O` (1992–), plus `UCI_CH4` (1978–)
* 2019 annual means: CH₄ ≈ 1867 ppb, N₂O ≈ 332 ppb (NOAA global)
""",
    ),
    (
        "Step 2 · Exeter — the surface temperature record (panels c, d)",
        "exeter", "map",
        """
**Status: `ONLINE` — originating datasets, cited not re-hosted.**

* **HadCRUT5** (Met Office Hadley Centre / UEA CRU, Morice et al. 2021) — one of four datasets in the AR6 Chapter 2
  assessed GMST (with NOAAGlobalTemp-Interim, Berkeley Earth, Kadow et al. 2020)
* **HadCRUT4.6** — the observational basis of WGI SPM.2 / SYR 2.1(d): 1.06 °C (likely 0.88–1.21) for 2010–2019 vs 1850–1900
* Palaeo context: **PAGES 2k Consortium (2019)** 1–2000 CE reconstruction (doi:10.1038/s41561-019-0400-0) and the
  Chapter 2 mid-Holocene assessment (0.2–1.0 °C very likely range) — both included in the CEDA SPM.1 final files
""",
    ),
    (
        "Step 2 · Ispra — EDGAR emissions inventory (panel a)",
        "ispra", "map",
        """
**Status: `ONLINE` — originating inventory, cited not re-hosted.**

* **EDGAR v6.0** (EU Joint Research Centre): fossil CO₂, CH₄, N₂O and F-gases, country × sector × year
  ([edgar.jrc.ec.europa.eu](https://edgar.jrc.ec.europa.eu/))
* **CO₂-LULUCF**: mean of three bookkeeping models — BLUE, Houghton & Nassikas (2017), OSCAR — from the Global Carbon Budget
* GWP100 (AR6 WGI Chapter 7 Table 7.15) converts gases to CO₂-eq
""",
    ),
    (
        "Step 2 · Berlin — the harmonised emissions workbook (panel a)",
        "mcc", "map",
        """
**Status: `ONLINE` — author-processed input, openly archived (CC BY 4.0).**

* Minx, Lamb, Andrew et al. (2021), *A comprehensive and synthetic dataset for global, regional and national GHG emissions by
  sector 1970–2018 with an extension to 2019*, ESSD 13, 5213–5252, doi:10.5194/essd-13-5213-2021
* Data: Zenodo **doi:10.5281/zenodo.6483002** — `essd_ghg_data_gwp100.xlsx` (14 MB, 196 639 rows: ISO × sector × year × gas),
  `essd_lulucf_data.xlsx` (regional CO₂-LULUCF 1850–2019, three models + mean)
* Code: github.com/mcc-apsis/AR6-Emissions-trends-and-drivers (R)
* This project rebuilds global totals by gas from it (`scripts/build_wgiii_spm1_from_essd.py`): 2019 = 59.1 Gt CO₂-eq, +54 % vs 1990, +12 % vs 2010 — matching WGIII SPM.
""",
    ),
    # ----------------------------------------------------------------- step 3
    (
        "Step 3 · Intermediate data — overview",
        EUROPE, "markdown",
        """
## Step 3 · Intermediate data: what the authors computed along the way

| Archive | Collection | Access | What it holds |
|---|---|---|---|
| **DKRZ / WDCC** | `IPCC-DDC_AR6_Supplements` — "input/source and intermediate datasets underlying the AR6", DDC quality-checked | [wdc-climate.de/ui/project?acronym=IPCC-DDC_AR6_Supplements](https://www.wdc-climate.de/ui/project?acronym=IPCC-DDC_AR6_Supplements) | e.g. assessed GSAT projections (Fig 4.11, doi:10.26050/WDCC/AR6.IPCC-DDC_AR6_Sup_GSATPr), sea-level projection distributions |
| **CSIC-IFCA** | Interactive Atlas regional products | interactive-atlas.ipcc.ch | regional means, indices |
| **CEDA** | WGI "intermediate data" records for Chapters 2, 3, 6, 7, 8, 12, TS | table in github.com/IPCC-WG1/CEDA_IPCC_AR6_WGI_Figures_data | e.g. Fig 2.11–2.29, 3.27, 3.28, 7.3–7.21 |
| **GitHub / Zenodo** | figure-generation code | github.com/IPCC-WG1 (137 repos), Zenodo "IPCC AR6 WGI – Figure x.y" | scripts that turn inputs into final numbers |

**Status for Figure 2.1: `PARTIAL` — no dedicated intermediate record for any of the four panels.**

| Panel | Intermediate record? | Where the processed numbers actually are |
|---|---|---|
| (a) | none in DDC | Zenodo workbook (country × sector × gas with GWP100 applied) |
| (b) | none | per-network global means as columns of the CEDA Fig 2.5 final file |
| (c) | none | CMIP6 ensemble mean + 5–95 % range as columns of `gmst_changes_model_and_obs.csv` (CEDA SPM.1) |
| (d) | none | assessed likely ranges per driver in `SPM2b.csv`, `SPM2c_data.csv` (CEDA SPM.2) |

Code: no SPM-specific repository exists under IPCC-WG1; the Chapter 2 and Chapter 3 figure repositories and
Gillett et al. (2021, doi:10.1038/s41558-020-00965-9) document the method.
""",
    ),
    (
        "Step 3 · DKRZ Hamburg — IPCC-DDC_AR6_Supplements",
        "dkrz", "map",
        """
**Status: `PARTIAL` — archive exists; no Figure 2.1 entry found; full list not machine-readable.**

* Project `IPCC-DDC_AR6_Supplements`: intermediate datasets created by IPCC authors, archived long-term with DDC
  technical quality assurance (checks of completeness, licence, citation, CF names — see redmine.dkrz.de wiki *Intermediate_datasets*)
* Example entries: *IPCC AR6 WGI assessed GSAT Projections* (Milinski & Marotzke, doi:10.26050/WDCC/AR6.IPCC-DDC_AR6_Sup_GSATPr),
  *Relative Sea Level Projection Distributions*, *Sea Level Projections global* — all CC BY 4.0
* Relevant to Figure 2.1? The SPM.1 / SPM.2 ensemble statistics were archived with the **final** data at CEDA instead.
* TODO: browse *Find data* on the project page (JavaScript list) and note any GMST / attribution entry.
""",
    ),
    (
        "Step 3 · CEDA Harwell — WGI intermediate records",
        "ceda", "map",
        """
**Status: `PARTIAL` — intermediate records exist for other WGI figures, none for SPM.1, SPM.2 or Fig 2.5.**

* CEDA's AR6 WGI archive (`/badc/ar6_wg1/data/`) has separate *intermediate* records for Chapter 2 figures 2.11, 2.12, 2.13, 2.15,
  2.23, 2.25, 2.27, 2.29 and for Chapters 3, 6, 7, 8, 12 and the TS (index: github.com/IPCC-WG1/CEDA_IPCC_AR6_WGI_Figures_data)
* For the Figure 2.1 sources the processing results travel *inside* the final files:
  `gmst_changes_model_and_obs.csv` (CMIP6 ensemble mean and 5–95 % range for human+natural and natural-only forcing, 1850–2020)
  and `SPM2b.csv` / `SPM2c_data.csv` (assessed contributions per driver).
* Chapter 2 input-data folders (`inputdata_ch2_fig02`, `…fig11`, …) show the same pattern: input and intermediate tiers are published only where authors supplied them.
""",
    ),
    # ----------------------------------------------------------------- step 4
    (
        "Step 4 · Final data — overview",
        EUROPE, "markdown",
        """
## Step 4 · Final data: the numbers plotted in Figure 2.1

| Panel | Record | Version | DOI | Host | Files | Licence | Status |
|---|---|---|---|---|---|---|---|
| (a) | WGIII *Data for Figure SPM.1* (Lamb et al.) | 0.0.1, 2022-04-04 | 10.48490/vfxm-tm28 | IPCC Data Catalogue (MetadataWorks) | CSV (browser download only) | per record | `AVAILABLE`* rebuilt from Zenodo source |
| (b) | WGI Chapter 2 *Data for Figure 2.5* (Hall, 2023) | v20221116 | 10.5285/c6f19b27f8e74e98968c17c8e1f74c60 | CEDA | `Data_Figure_2.5.csv` (30 columns, 5 networks), README, License | CC BY 4.0 | `AVAILABLE` |
| (c) | WGI *Data for Figure SPM.1* (Gillett, Kaufman, Neukom) | v20221116 (supersedes v20210809) | 10.5285/0b2759059ad6474098e40dad73e0a8ec | CEDA | `SPM1_1850-2020_obs.csv`, `SPM1_1-2000_recon.csv`, `spm1_6500_recon.csv`, `gmst_changes_model_and_obs.csv` | CC BY 4.0 | `AVAILABLE` |
| (c) | SYR LR *Figure 2.1 (c): Changes in global surface temperature* | 1.0.0, 2025-04-10 | 10.7927/nq55-cr83 | CIESIN / NASA SEDAC (catalogue id 8498) | Excel (~15.5 KB) | see record | `PARTIAL` not yet fetched |
| (d) | WGI *Data for Figure SPM.2* (Gillett, Thorne, Trewin; Szopa, Sitz, Malinina) | v20210809 | 10.5285/c1eb6dad1598427f8f9f3eae346ece2f | CEDA | `SPM2a.csv`, `SPM2b.csv`, `SPM2c_data.csv` | CC BY 4.0 | `AVAILABLE` |
| (d) | SYR LR *Figure 2.1 (d): Humans are responsible* | 1.0.0, 2025-04-09 | 10.7927/b38b-zp83 (verify) | CIESIN / NASA SEDAC (catalogue id 8493) | Excel | see record | `PARTIAL` not yet fetched |
| (a),(b) | SYR-level records | — | — | — | — | — | `MISSING` |

Also: the CEDA record for an *IPCC AR6 Synthesis Report (SYR) dataset collection* (uuid 9177e927…) exists but is **not yet published**.

\\* the official WGIII CSV sits behind a JavaScript-only site; the project rebuilds identical global totals from the Zenodo source workbook.
Next stops: CEDA (WGI), MetadataWorks catalogue (WGIII), CIESIN (SYR).
""",
    ),
    (
        "Step 4 · CEDA Harwell — WGI final figure data (panels b, c, d)",
        "ceda", "map",
        """
**Status: `AVAILABLE` — three records downloaded and bundled in `data/final/`.**

Archive path `https://dap.ceda.ac.uk/badc/ar6_wg1/data/` (BADC-CSV: metadata header, `data` … `end_data`), all **CC BY 4.0**,
each with `Readme_for_figure_*.txt`, `License.txt`, `00README_catalogue_and_licence.txt`.

* **SPM.1 v20221116** — `spm/spm_01/v20221116/` → panel (c)
  `panel_a/SPM1_1850-2020_obs.csv` (decadal-smoothed GMST), `SPM1_1-2000_recon.csv` (PAGES2k, with 5–95 %),
  `spm1_6500_recon.csv` (mid-Holocene 0.2–1.0 °C), `panel_b/gmst_changes_model_and_obs.csv` (annual obs + CMIP6 envelopes 1850–2020)
* **SPM.2 v20210809** — `spm/spm_02/v20210809/` → panel (d)
  `SPM2a.csv` (observed 1.06 [0.88, 1.21] °C), `SPM2b.csv` (human 1.07 [0.8, 1.3]; GHG 1.5 [1.0, 2.0]; other human −0.4 [−0.8, 0.0]; natural 0.0 [−0.1, 0.1]; internal 0.0 [−0.2, 0.2]),
  `SPM2c_data.csv` (per-driver GSAT effect, e.g. CO₂ 0.79, CH₄ 0.51, N₂O 0.09 °C)
* **Chapter 2 Figure 2.5 v20221116** — `ch_02/ch2_fig05/v20221116/Data_Figure_2.5.csv` → panel (b)
  1 971 rows, 30 columns: `{NOAA,AGAGE,CSIRO,UCI,SIO}_{CO2,CH4,N2O}` with `_xdate` and growth-rate `_gr` columns

Citation rule (from the licence file): cite the dataset DOI **and** the report component
(*IPCC, 2021: Summary for Policymakers … doi:10.1017/9781009157896.001*).
WGI SPM collection record: catalogue.ceda.ac.uk/uuid/ae4f1eb6fce24adcb92ddca1a7838a5c (SPM.1–SPM.10).
""",
    ),
    (
        "Step 4 · IPCC Data Catalogue — WGIII final data (panel a)",
        WORLD, "markdown",
        """
## Step 4 · WGIII *Data for Figure SPM.1* — IPCC Data Catalogue (MetadataWorks)

**Status: `AVAILABLE`\\* — official record exists; identical totals rebuilt from the open source workbook.**

| Item | Detail |
|---|---|
| Record | *Data for Figure SPM.1*, version 0.0.1, published 4 April 2022, authors Lamb et al. |
| DOI | **10.48490/vfxm-tm28** → resolves to `ipcc-browser.ipcc-data.org/browser/dataset?id=437` |
| Content | global net anthropogenic GHG emissions 1990–2019, Gt CO₂-eq (GWP100-AR6), by gas: CO₂-FFI, CO₂-LULUCF, CH₄, N₂O, F-gases |
| Format | CSV, "Data Downloads" section of the catalogue page (JavaScript application — browser only) |
| Source | Minx et al. (2021) ESSD, doi:10.5194/essd-13-5213-2021 (EDGAR v6 + bookkeeping models) |
| Related WGIII records | SPM.2 (regional emissions, id 441), SPM.5 (pathways), WGIII Ch.2 figure data |

**What this project does:** `scripts/build_wgiii_spm1_from_essd.py` downloads the Zenodo workbook (doi:10.5281/zenodo.6483002)
and writes `data/final/wgiii_spm1/global_ghg_emissions_by_gas_1970-2019.csv`
(1990: 38.3 · 2000: 42.2 · 2010: 52.6 · **2019: 59.1 Gt CO₂-eq**; shares 2019: CO₂-FFI 64 %, CO₂-LULUCF 11 %, CH₄ 18 %, N₂O 4.5 %, F-gases 2.3 %).

\\* TODO (optional): download the official CSV in a browser and store it next to the rebuilt file for a one-to-one check.
""",
    ),
    (
        "Step 4 · CIESIN / SEDAC — SYR final figure data (panels c, d)",
        "ciesin", "map",
        """
**Status: `PARTIAL` — records exist for (c) and (d); workbooks not yet fetched; (a), (b) `MISSING`.**

The Synthesis Report's figure data are catalogued in the IPCC Data Catalogue and hosted by
CIESIN / NASA SEDAC at Columbia University (DOI prefix 10.7927):

| Panel | Record | Version | DOI | Landing page | File |
|---|---|---|---|---|---|
| (c) | *IPCC AR6 Synthesis Report LR Figure 2.1 (c): Changes in global surface temperature* — catalogue id 8498 | 1.0.0, 2025-04-10 | 10.7927/nq55-cr83 | sedac.ciesin.columbia.edu/ddc/ar6-syr-lr-fig2-1c/ | Excel, ~15.5 KB |
| (d) | *IPCC AR6 Synthesis Report LR Figure 2.1 (d): Humans are responsible* — catalogue id 8493 | 1.0.0, 2025-04-09 | 10.7927/b38b-zp83 (search results disagree — verify) | sedac.ciesin.columbia.edu/ddc/ar6-syr-lr-fig2-1d/ | Excel |
| (a), (b) | no SYR-level record | — | — | — | use WGIII SPM.1 / WGI Fig 2.5 |

Other SYR records on the same host (for orientation): Figure 2.2(b), Cross-Section Box.2 Figure 1(a),(b) (scenario data from the AR6 Scenarios Database, IIASA).

**TODO** (browser needed; SEDAC refuses non-browser connections): download both workbooks, confirm the DOI and licence
on the landing pages, convert to CSV in `data/final/syr_fig2_1/`; the notebook's final cell then compares them with the WGI values.

CEDA counterpart: the *IPCC AR6 Synthesis Report (SYR) dataset collection* record (uuid 9177e927f0664da9bf1e25f57561d0d8) is created but **not yet published**.
""",
    ),
    # ------------------------------------------------------------- status map
    (
        "Data status at a glance",
        WORLD, "markdown",
        """
## Where Figure 2.1 stands today (checked 2026-10-13)

| Step | Archive | Panel (a) emissions | Panel (b) concentrations | Panel (c) temperature | Panel (d) attribution |
|---|---|---|---|---|---|
| 1 Report | ipcc.ch | `ONLINE` | `ONLINE` | `ONLINE` | `ONLINE` |
| 2 Input | DKRZ `IPCC-AR6_CMIP6` | – | – | `ONLINE` CMIP6 hist/ssp245, hist-nat | `ONLINE` CMIP6 DAMIP |
| 2 Input | originating institutions | `ONLINE` EDGAR, GCB, Zenodo workbook | `ONLINE` NOAA, SIO, CSIRO, AGAGE, UCI | `ONLINE` HadCRUT5, NOAA, Berkeley, Kadow, PAGES2k | `ONLINE` HadCRUT4.6 |
| 3 Intermediate | DKRZ `IPCC-DDC_AR6_Supplements` / CEDA / CSIC | `PARTIAL` none; see Zenodo | `PARTIAL` inside final file | `PARTIAL` inside final file | `PARTIAL` inside final file |
| 4 Final (WG) | CEDA / IPCC Data Catalogue | `AVAILABLE`* 10.48490/vfxm-tm28 | `AVAILABLE` 10.5285/c6f19b27… | `AVAILABLE` 10.5285/0b275905… | `AVAILABLE` 10.5285/c1eb6dad… |
| 4 Final (SYR) | CIESIN / SEDAC | `MISSING` | `MISSING` | `PARTIAL` 10.7927/nq55-cr83 | `PARTIAL` 10.7927/b38b-zp83 |

Legend: `AVAILABLE` bundled in this project · `ONLINE` published, link only · `PARTIAL` exists but incomplete or unverified · `MISSING` no record.
\\* rebuilt from the open Zenodo source.

**Service notes:** ipcc-data.org and catalogue.ceda.ac.uk returned intermittent 502/503 errors; SEDAC and ipcc-browser are browser-only.
Data files were retrieved through `dap.ceda.ac.uk` and the Zenodo API.
""",
    ),
    (
        "How to reuse the data",
        WORLD, "markdown",
        """
## How to go from any IPCC figure to its data

1. **Read the caption's traceability tag** (`{WGI SPM.1 … WGIII SPM.1}`) — it names the Working-Group figures the panel came from.
2. **Final data first.** WGI/WGII → CEDA (`10.5285/…`, index at github.com/IPCC-WG1/CEDA_IPCC_AR6_WGI_Figures_data);
   WGIII → IPCC Data Catalogue (`10.48490/…`); SYR → IPCC Data Catalogue hosted by CIESIN/SEDAC (`10.7927/…`).
3. **Open the README and licence shipped with the record**; CEDA files are BADC-CSV (metadata header, `data` … `end_data`).
4. **Need the processing chain?** Look for intermediate records (DKRZ `IPCC-DDC_AR6_Supplements`, CEDA intermediate table) and the code (github.com/IPCC-WG1, Zenodo).
5. **Need the raw inputs?** CMIP6 at DKRZ (`IPCC-AR6_CMIP6`, DOIs `10.26050/WDCC/AR6.*`); observations and inventories at the originating institutions.
6. **Cite twice** — dataset DOI *and* report component — and respect licences: data CC BY 4.0, figure images under the IPCC copyright policy (redraw from data).

**In this project:** `ar6_syr_fig2_1_data_story.ipynb` reproduces all four panels live in the browser from the Step-4 files;
`data/PROVENANCE.md` lists every record; `README.md` lists the open TODOs (SYR workbooks, DKRZ supplements list).
""",
    ),
]


def main() -> None:
    layers, sources, layer_tree, story_segments = {}, {}, [], []

    base_src, base_layer = uid(), uid()
    sources[base_src] = {
        "name": "OpenStreetMap.Mapnik",
        "type": "RasterSource",
        "parameters": {
            "attribution": "(C) OpenStreetMap contributors",
            "interpolate": False,
            "maxZoom": 19.0,
            "minZoom": 0.0,
            "provider": "OpenStreetMap",
            "url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            "urlParameters": {},
        },
    }
    layers[base_layer] = {
        "name": "OpenStreetMap.Mapnik Layer",
        "type": "RasterLayer",
        "visible": True,
        "parameters": {"opacity": 1.0, "source": base_src},
    }
    layer_tree.append(base_layer)

    for key, (name, lon, lat, colour) in PLACES.items():
        s, l = uid(), uid()
        x, y = merc(lon, lat)
        sources[s] = {
            "name": f"Marker – {name}",
            "type": "MarkerSource",
            "parameters": {"color": colour, "feature": {"coords": [x, y]}},
        }
        layers[l] = {
            "name": name,
            "type": "VectorLayer",
            "visible": True,
            "parameters": {"opacity": 1.0, "source": s, "symbologyState": {}},
        }
        layer_tree.append(l)

    for title, where, mode, md in SEGMENTS:
        if isinstance(where, str):
            _, lon, lat, _ = PLACES[where]
            zoom = 11.5
        else:
            lon, lat, zoom = where
        seg = uid()
        layers[seg] = {
            "name": title,
            "type": "StorySegmentLayer",
            "visible": True,
            "parameters": {
                "zoom": zoom,
                "extent": extent(lon, lat, zoom),
                "content": {
                    "contentMode": mode,
                    "title": title,
                    "markdown": md.strip("\n"),
                    "image": "",
                },
                "layerOverride": [],
                "transition": {"type": "smooth", "time": 2.0},
            },
        }
        layer_tree.append(seg)
        story_segments.append(seg)

    lon0, lat0, z0 = WORLD
    doc = {
        "schemaVersion": "0.6.0",
        "layerTree": layer_tree,
        "layers": layers,
        "sources": sources,
        "stories": {
            uid(): {
                "title": "IPCC AR6 SYR Figure 2.1 – the data journey (report → input → intermediate → final)",
                "storyType": "guided",
                "presentationBgColor": "#0b2545",
                "presentationTextColor": "#eef4ed",
                "showGradient": True,
                "storySegments": story_segments,
            }
        },
        "options": {
            "bearing": 0.0,
            "pitch": 0.0,
            "projection": "EPSG:3857",
            "longitude": lon0,
            "latitude": lat0,
            "zoom": z0,
            "extent": extent(lon0, lat0, z0),
        },
        "viewState": {},
        "metadata": {
            "description": "Story map of the data behind IPCC AR6 SYR Longer Report Figure 2.1, "
                           "structured as report → input → intermediate → final data with availability status",
            "generated_by": "scripts/build_storymap.py",
            "checked": "2026-10-13",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT} with {len(story_segments)} segments and {len(PLACES)} markers")


if __name__ == "__main__":
    main()
