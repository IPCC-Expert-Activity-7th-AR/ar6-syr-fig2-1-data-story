#!/usr/bin/env python3
"""Generate the JupyterGIS Story Map (storymap/ipcc_ar6_data_journey.jGIS).

Structure follows the IPCC data-management chain for SYR Figure 2.1:

  Step 1  The report and the figure           (IPCC, Geneva)
  Step 2  Input data        – DKRZ / CSIC + originating observatories & inventories
  Step 3  Intermediate data – CEDA chapter-level records, DKRZ Supplements, code
  Step 4  Final data        – CEDA (WGI), IPCC Data Catalogue (WGIII), CIESIN-SEDAC (SYR)
  Status  One-page availability dashboard and how to reuse

Readability rules used for every stop (the story panel is narrow):
  * one status badge on the first line:  🟢 AVAILABLE  🔵 ONLINE  🟡 PARTIAL  🔴 MISSING
  * tables have at most 2 columns, except the status matrix which uses
    emoji-only cells (4 narrow columns)
  * short bullets, no sentence longer than one line in a 40-character column
  * every stop ends with a "➡" hint to the next stop

The .jGIS format is the JSON document used by JupyterGIS (schemaVersion 0.6.0).
Coordinates are stored in EPSG:3857 (Web Mercator metres).
"""
import json
import math
import pathlib
import re
import uuid

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "storymap" / "ipcc_ar6_data_journey.jGIS"
CHECKED = "2026-10-13"

R = 6378137.0

AVAILABLE = "🟢 **AVAILABLE** – copy in this project, loaded live from the archive when online"
ONLINE = "🔵 **ONLINE** – published, link only (not re-hosted here)"
PARTIAL = "🟡 **PARTIAL** – exists but incomplete or not verifiable from here"
MISSING = "🔴 **MISSING** – no record exists"
LEGEND = "🟢 available · 🔵 online · 🟡 partial · 🔴 missing"

CEDA_DAP = "https://dap.ceda.ac.uk/badc/ar6_wg1/data"


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


# ------------------------------------------------------------- link helpers --
DOI_RE = re.compile(r"(?<![\w/\[(])(10\.\d{4,9}/[A-Za-z0-9._\-/]*[A-Za-z0-9])")
LINKED_DOI_RE = re.compile(r"\[(10\.\d{4,9}/[^\]]+)\]\((https?://doi\.org/[^)]+)\)")
URL_RE = re.compile(
    r"(?<![\w/\[(@])((?:www\.)?(?:github\.com|wdc-climate\.de|interactive-atlas\.ipcc\.ch|sedac\.ciesin\.columbia\.edu|"
    r"ipcc-browser\.ipcc-data\.org|ipcc-data\.org|catalogue\.ceda\.ac\.uk|dap\.ceda\.ac\.uk|gml\.noaa\.gov|scrippsco2\.ucsd\.edu|"
    r"agage\.mit\.edu|edgar\.jrc\.ec\.europa\.eu|redmine\.dkrz\.de|zenodo\.org|ipcc\.ch)(?:/[^\s)\]|`*,;]*[^\s)\]|`*,;.])?)")


def short_doi(d):
    """Shorten CEDA-style DOIs (32-hex uuid) for display: 10.5285/0b275905…"""
    m = re.fullmatch(r"(10\.5285/[0-9a-f]{8})[0-9a-f]{24}", d)
    return m.group(1) + "…" if m else d


def linkify(text):
    """Turn bare DOIs and known data-portal URLs into markdown links (outside code spans),
    and shorten the display text of existing long DOI links."""
    parts = text.split("`")
    for i in range(0, len(parts), 2):                      # even parts are outside code spans
        t = LINKED_DOI_RE.sub(lambda m: f"[{short_doi(m.group(1))}]({m.group(2)})", parts[i])
        t = DOI_RE.sub(lambda m: f"[{short_doi(m.group(1))}](https://doi.org/{m.group(1)})", t)
        t = URL_RE.sub(lambda m: f"[{m.group(1)}](https://{m.group(1)})", t)
        parts[i] = t
    return "`".join(parts)


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
    "ceda":   ("CEDA, Harwell – DDC: WGI final + intermediate + input figure data", -1.3140, 51.5740, "#c62828"),
    "ciesin": ("CIESIN / SEDAC, Palisades NY – DDC: SYR final figure data", -73.9120, 41.0040, "#c62828"),
}

WORLD = (10.0, 30.0, 1.4)   # lon, lat, zoom for full-screen markdown segments
EUROPE = (4.0, 49.5, 4.2)


def record(rows):
    """2-column fact table."""
    out = ["| | |", "|---|---|"]
    for k, v in rows:
        out.append(f"| **{k}** | {v} |")
    return "\n".join(out)


STATUS_MATRIX = f"""
| Tier → panel | (a) emissions | (b) concentr. | (c) temperature | (d) attribution |
|---|:-:|:-:|:-:|:-:|
| **1** Report (ipcc.ch) | 🔵 | 🔵 | 🔵 | 🔵 |
| **2** Input · DDC at DKRZ (CMIP6) | – | – | 🔵 | 🔵 |
| **2** Input · originating institutions | 🔵 | 🔵 | 🟢 | 🔵 |
| **3** Intermediate · chapter records at CEDA | 🟡 | 🟢 | 🟢 | 🟢 |
| **4** Final · Working Group record | 🟢 | 🟢 | 🟢 | 🟢 |
| **4** Final · SYR record (SEDAC) | 🔴 | 🔴 | 🟡 | 🟡 |

{LEGEND} · checked {CHECKED}
"""

# ---------------------------------------------------------------- segments --
# (title, place-key or (lon,lat,zoom) tuple, contentMode, markdown)
SEGMENTS = [
    # ------------------------------------------------------------------ intro
    (
        "The data behind IPCC AR6 SYR Figure 2.1",
        WORLD, "markdown",
        f"""
## One IPCC figure, four data tiers

**IPCC AR6 Synthesis Report · Longer Report · Figure 2.1**
*The causal chain from emissions to resulting warming.*

This story walks the figure back to its data, in the order the IPCC Data Distribution Centre (DDC) organises it:

| Step | Question |
|---|---|
| **1 · Report** | What does the figure show, and which Working-Group figures is it built from? |
| **2 · Input data** | Which observations, inventories and simulations did authors start from? |
| **3 · Intermediate data** | What was computed along the way, and where is it archived? |
| **4 · Final data** | Which numbers are plotted, and can I download them today? |

Each stop shows one status badge:

* {AVAILABLE}
* {ONLINE}
* {PARTIAL}
* {MISSING}

➡ **Next** – Step 1: the figure itself.
""",
    ),
    # ----------------------------------------------------------------- step 1
    (
        "Step 1 · The report: Figure 2.1 and its four panels",
        "ipcc", "map",
        f"""
{ONLINE}

**Climate Change 2023: Synthesis Report** – approved 19 March 2023, Geneva.
doi:10.59327/IPCC/AR6-9789291691647 · [figure page](https://www.ipcc.ch/report/ar6/syr/figures/figure-2-1)

The caption's traceability tag names the sources:
`{{WGI SPM A.2.2, WGI Figure SPM.1, WGI Figure SPM.2, WGI TS2.2, WGI 2.1; WGIII Figure SPM.1, WGIII A.III.II.2.5.1}}`

| Panel | Built from |
|---|---|
| **(a)** GHG emissions 1990–2019 by gas | WGIII Figure SPM.1 |
| **(b)** CO₂ · CH₄ · N₂O concentrations, annual, panel heights ∝ warming effect | WGI Section 2.1 (Figures 2.4, 2.5) + SPM.2(c) |
| **(c)** Global surface temperature vs 1850–1900, with the warmest period of the last 100 000 yr | WGI Figure SPM.1 |
| **(d)** Warming 1850–1900 → 2010–2019 by driver | WGI Figure SPM.2 |

The SYR re-publishes Working-Group data, so Steps 2–4 follow the WGI and WGIII records.

➡ **Next** – how the IPCC organises its data.
""",
    ),
    (
        "Step 1 · How the IPCC organises data",
        WORLD, "markdown",
        f"""
## Three tiers, five archives

| Tier | What it is → where it lives (AR6) |
|---|---|
| **Input data** | observations, inventories, model runs the authors started from → CMIP6 subset at **DKRZ**; observations stay with the producing networks |
| **Intermediate data** | products authors created while processing inputs → **DKRZ** `IPCC-DDC_AR6_Supplements`, **CSIC** Atlas, chapter-level records at **CEDA** |
| **Final data** | the numbers plotted in a published figure → WGI/WGII **CEDA** · WGIII **IPCC Data Catalogue** · SYR **CIESIN / SEDAC** |

DOI prefixes: DKRZ `10.26050/WDCC/AR6.*` · CEDA `10.5285/*` · IPCC Data Catalogue `10.48490/*` · SEDAC `10.7927/*`

### Status of Figure 2.1 today
{STATUS_MATRIX}

➡ **Next** – Step 2: the input data.
""",
    ),
    # ----------------------------------------------------------------- step 2
    (
        "Step 2 · Input data – overview",
        EUROPE, "markdown",
        f"""
## Step 2 · What the authors started from

The DDC re-hosts **model** input (DKRZ). **Observational** input is cited to the producing institution, not copied.
One exception helps us here: CEDA publishes an *Input data for Figure 2.11* record – the four temperature datasets behind panel (c).

| Panel | Input datasets |
|---|---|
| **(a)** | 🔵 EDGAR v6.0 (JRC) · CO₂-LULUCF from BLUE, Houghton & Nassikas, OSCAR · harmonised in Minx et al. 2021 (Zenodo) |
| **(b)** | 🔵 NOAA GML, Scripps, CSIRO, AGAGE, UCI network means · ice cores (Law Dome, WAIS, EDML) for pre-1958 |
| **(c)** | 🟢 HadCRUT5, NOAAGlobalTemp, Berkeley Earth, Kadow 2020 (CEDA input record) · 🔵 PAGES 2k · CMIP6 at DKRZ |
| **(d)** | 🔵 HadCRUT4.6 · CMIP6 DAMIP hist-GHG / hist-aer / hist-nat at DKRZ |

Detailed source tables: `data/input/README.md`.

➡ **Next** – the DDC input archive at DKRZ, then six places where inputs are made.
""",
    ),
    (
        "Step 2 · DKRZ Hamburg – the CMIP6 input archive",
        "dkrz", "map",
        f"""
{ONLINE}

{record([
    ("Archive", "World Data Center for Climate (WDCC), project `IPCC-AR6_CMIP6`"),
    ("Content", "CMIP6 subset used by WGI authors: **65 118 datasets**, ~120 models"),
    ("Granularity", "one entry per model × experiment, e.g. doi:10.26050/WDCC/AR6.C6CMCASFGO"),
    ("Used in Fig 2.1", "panel (c) model envelopes (historical + ssp245, hist-nat) · panel (d) attribution runs (hist-GHG, hist-aer, hist-nat)"),
    ("Licence", "CC BY 4.0"),
    ("Link", "[wdc-climate.de → IPCC-AR6_CMIP6](https://www.wdc-climate.de/ui/project?acronym=IPCC-AR6_CMIP6)"),
])}

➡ **Next** – CSIC-IFCA, the second DDC input/intermediate node.
""",
    ),
    (
        "Step 2 · CSIC-IFCA Santander – Atlas inputs",
        "csic", "map",
        f"""
{ONLINE}

* Hosts the WGI **Interactive Atlas** and, with DKRZ, the DDC long-term archive for input and intermediate data.
* Same observational and CMIP6 inputs, aggregated **regionally**.
* Figure 2.1 is global, so no Atlas product feeds it directly.
* Useful for regional versions of panels (c) and (d).

[interactive-atlas.ipcc.ch](https://interactive-atlas.ipcc.ch)

➡ **Next** – Mauna Loa, where the CO₂ record starts.
""",
    ),
    (
        "Step 2 · Mauna Loa – CO₂ since 1958 (panel b)",
        "mlo", "map",
        f"""
{ONLINE}

{record([
    ("Networks", "NOAA Global Monitoring Laboratory · Scripps Institution of Oceanography"),
    ("In the CEDA Fig 2.5 file", "columns `NOAA_CO2`, `SIO_CO2`, `CSIRO_CO2` (1958 / 1979 – 2019)"),
    ("2019 global mean", "≈ 410 ppm"),
    ("Before 1958", "ice-core composite from WGI Fig 2.4 (Law Dome, WAIS Divide, EDML)"),
    ("Links", "[gml.noaa.gov/ccgg/trends](https://gml.noaa.gov/ccgg/trends/) · [scrippsco2.ucsd.edu](https://scrippsco2.ucsd.edu/)"),
])}

➡ **Next** – Cape Grim for CH₄ and N₂O.
""",
    ),
    (
        "Step 2 · Cape Grim – CH₄ and N₂O (panel b)",
        "cgo", "map",
        f"""
{ONLINE}

{record([
    ("Station", "CSIRO / Bureau of Meteorology baseline station, member of **AGAGE**"),
    ("In the CEDA Fig 2.5 file", "`AGAGE_CH4` (1987–), `AGAGE_N2O` (1979–), `CSIRO_CH4`, `CSIRO_N2O` (1992–), `UCI_CH4` (1978–)"),
    ("2019 global means", "CH₄ ≈ 1867 ppb · N₂O ≈ 332 ppb"),
    ("Links", "[csiro.au/greenhouse-gases](https://www.csiro.au/greenhouse-gases) · [agage.mit.edu](https://agage.mit.edu/)"),
])}

➡ **Next** – Exeter and the surface-temperature record.
""",
    ),
    (
        "Step 2 · Exeter – the surface temperature record (panels c, d)",
        "exeter", "map",
        f"""
{AVAILABLE}

**HadCRUT5** (Met Office Hadley Centre / UEA) is one of four datasets averaged into the AR6 assessed global temperature.
CEDA publishes that four-dataset table as an *input data* record:

{record([
    ("Record", "WGI Ch.2 – *Input data for Figure 2.11* (v20220428)"),
    ("DOI", "10.5285/033cd690801741c9bc745b8da55faef4"),
    ("File", "`Figure_2_11c-lower_panel.csv` – HadCRUT, NOAA, Berkeley, Kadow 1850–2020 + decadal means"),
    ("Also in record", "HadCRUT trend and significance grids 1900–1980 / 1981–2020"),
    ("In project", "`data/input/wgi_ch2_fig2_11_input/`"),
])}

Other inputs cited here: **HadCRUT4.6** (basis of panel d, 1.06 °C) and the **PAGES 2k** reconstruction (1–2000 CE).

➡ **Next** – Ispra and the emissions inventory.
""",
    ),
    (
        "Step 2 · Ispra – EDGAR emissions inventory (panel a)",
        "ispra", "map",
        f"""
{ONLINE}

{record([
    ("Inventory", "**EDGAR v6.0** – EU Joint Research Centre"),
    ("Covers", "fossil CO₂, CH₄, N₂O, F-gases · country × sector × year"),
    ("Plus", "CO₂-LULUCF = mean of BLUE, Houghton & Nassikas 2017, OSCAR (Global Carbon Budget)"),
    ("Metric", "GWP100 from WGI Ch.7 Table 7.15 → CO₂-equivalent"),
    ("Link", "[edgar.jrc.ec.europa.eu](https://edgar.jrc.ec.europa.eu/)"),
])}

➡ **Next** – Berlin, where the inventory became the WGIII dataset.
""",
    ),
    (
        "Step 2 · Berlin – the harmonised emissions workbook (panel a)",
        "mcc", "map",
        f"""
{ONLINE}

{record([
    ("Paper", "Minx, Lamb, Andrew et al. (2021) ESSD 13, 5213–5252 · doi:10.5194/essd-13-5213-2021"),
    ("Data", "Zenodo **doi:10.5281/zenodo.6483002** · `essd_ghg_data_gwp100.xlsx` (196 639 rows) · `essd_lulucf_data.xlsx`"),
    ("Code", "github.com/mcc-apsis/AR6-Emissions-trends-and-drivers (R)"),
    ("In project", "global totals by gas rebuilt by `scripts/build_wgiii_spm1_from_essd.py` → **59.1 Gt CO₂-eq in 2019**, +54 % vs 1990"),
    ("Licence", "CC BY 4.0"),
])}

➡ **Next** – Step 3: the intermediate data.
""",
    ),
    # ----------------------------------------------------------------- step 3
    (
        "Step 3 · Intermediate data – overview",
        EUROPE, "markdown",
        f"""
## Step 3 · What was computed along the way

No record is labelled "intermediate data for SYR Figure 2.1". The processing chain is visible instead in
**chapter-level WGI records at CEDA**, now bundled here and loadable live from `dap.ceda.ac.uk`:

| Panel | Chapter-level record (CEDA, CC BY 4.0) |
|---|---|
| **(a)** | 🟡 none in the DDC – the Zenodo workbook is the processed table |
| **(b)** | 🟢 WGI Fig 2.4 – ice-core CO₂ / CH₄ / N₂O 0–2000 CE, 10.5285/60eeb3cce51a457cb5ee1c577a0c8674 · per-network means inside the Fig 2.5 file |
| **(c)** | 🟢 WGI Fig 2.11 – AR6 four-dataset mean 1850–2020, PAGES 2k, land/ocean, 10.5285/f3515388768344bfb2be0521f82388be |
| **(d)** | 🟢 WGI Fig 3.8 – lines of evidence per driver, 10.5285/bf3d0b8a8c0d4ae19cfd994b6fef4a5c · Fig 7.6 ERF 1750–2019, 10.5285/0dd364e74c254b64bb5fddb5dceed364 · Fig 7.8 attributed warming by agent, 10.5285/5ef11ad195844a59b83393870a5860e1 |

Other intermediate archives: DKRZ `IPCC-DDC_AR6_Supplements`, CSIC Atlas, figure code on github.com/IPCC-WG1.

➡ **Next** – DKRZ Supplements, then CEDA.
""",
    ),
    (
        "Step 3 · DKRZ Hamburg – IPCC-DDC_AR6_Supplements",
        "dkrz", "map",
        f"""
{PARTIAL}

{record([
    ("Project", "`IPCC-DDC_AR6_Supplements` – intermediate datasets with DDC quality assurance"),
    ("Examples", "assessed GSAT projections (doi:10.26050/WDCC/AR6.IPCC-DDC_AR6_Sup_GSATPr) · sea-level projection distributions"),
    ("Figure 2.1 entry", "none found; SPM.1 / SPM.2 ensemble statistics were archived with the *final* data at CEDA"),
    ("Open item", "the *Find data* list is JavaScript-only; browse it manually and note GMST / attribution entries"),
    ("Link", "[wdc-climate.de → IPCC-DDC_AR6_Supplements](https://www.wdc-climate.de/ui/project?acronym=IPCC-DDC_AR6_Supplements)"),
])}

➡ **Next** – CEDA, where the chapter-level chain is published.
""",
    ),
    (
        "Step 3 · CEDA Harwell – the chapter-level chain",
        "ceda", "map",
        f"""
{AVAILABLE}

Four CEDA records show how inputs became the SPM numbers:

{record([
    ("Fig 2.4 (v20221219)", "ice cores → pre-1958 part of panel (b) · `fig2_4b_data_v2.csv`"),
    ("Fig 2.11 (v20220510)", "four datasets → AR6 mean → panel (c) · `Figure2_11_panel_a.csv`"),
    ("Fig 3.8 (v20220613)", "Ribes, Haustein, Gillett, Ch.7 estimates + 13 CMIP6 models → panel (d) · `drivers_observed_warming.csv`"),
    ("Fig 7.6 → 7.8 (v20220721)", "ERF by agent → emulator → warming by agent → SPM.2(c) and panel (b) heights"),
])}

Catalogue state (checked {CHECKED}): all four **citable**, DOIs resolve, CC BY 4.0.
Archive: [dap.ceda.ac.uk/badc/ar6_wg1/data]({CEDA_DAP}/) – CORS enabled, so the notebook reads the files directly in the browser.

➡ **Next** – Step 4: the final data.
""",
    ),
    # ----------------------------------------------------------------- step 4
    (
        "Step 4 · Final data – overview",
        EUROPE, "markdown",
        f"""
## Step 4 · The numbers plotted in Figure 2.1

| Panel | Working-Group record (final data) |
|---|---|
| **(a)** | 🟢 WGIII *Data for Figure SPM.1* · 10.48490/vfxm-tm28 · IPCC Data Catalogue · rebuilt here from the Zenodo source |
| **(b)** | 🟢 WGI Ch.2 *Data for Figure 2.5* v20221116 · 10.5285/c6f19b27f8e74e98968c17c8e1f74c60 · CEDA |
| **(c)** | 🟢 WGI *Data for Figure SPM.1* v20221116 · 10.5285/0b2759059ad6474098e40dad73e0a8ec · CEDA |
| **(d)** | 🟢 WGI *Data for Figure SPM.2* v20210809 · 10.5285/c1eb6dad1598427f8f9f3eae346ece2f · CEDA |

| Panel | SYR-level record (CIESIN / SEDAC) |
|---|---|
| **(a)**, **(b)** | 🔴 no SYR record |
| **(c)** | 🟡 *SYR LR Figure 2.1 (c)* · 10.7927/nq55-cr83 · Excel, browser-only |
| **(d)** | 🟡 *SYR LR Figure 2.1 (d)* · 10.7927/b38b-zp83 (verify) · Excel, browser-only |

CEDA's *IPCC AR6 Synthesis Report (SYR)* collection record exists but is still **not published** ({CHECKED}).

➡ **Next** – CEDA, the IPCC Data Catalogue, CIESIN.
""",
    ),
    (
        "Step 4 · CEDA Harwell – WGI final data (panels b, c, d)",
        "ceda", "map",
        f"""
{AVAILABLE}

{record([
    ("SPM.1 v20221116", "panel (c) · `SPM1_1850-2020_obs.csv`, `SPM1_1-2000_recon.csv`, `spm1_6500_recon.csv`, `gmst_changes_model_and_obs.csv` · doi 10.5285/0b2759059ad6474098e40dad73e0a8ec"),
    ("SPM.2 v20210809", "panel (d) · `SPM2a.csv` (observed 1.06 [0.88–1.21] °C), `SPM2b.csv` (human 1.07 [0.8–1.3]), `SPM2c_data.csv` (CO₂ 0.79, CH₄ 0.51, N₂O 0.09 °C) · doi 10.5285/c1eb6dad1598427f8f9f3eae346ece2f"),
    ("Ch.2 Fig 2.5 v20221116", "panel (b) · `Data_Figure_2.5.csv` – 30 columns, 5 networks · doi 10.5285/c6f19b27f8e74e98968c17c8e1f74c60"),
    ("Format", "BADC-CSV: metadata header → `data` → rows → `end_data`"),
    ("Licence", "CC BY 4.0 · cite dataset DOI **and** report component"),
    ("Checked", f"{CHECKED}: catalogue reachable, bundled copies identical to the archive"),
])}

➡ **Next** – the WGIII record for panel (a).
""",
    ),
    (
        "Step 4 · IPCC Data Catalogue – WGIII final data (panel a)",
        WORLD, "markdown",
        f"""
## Step 4 · WGIII *Data for Figure SPM.1*

{AVAILABLE} (rebuilt from the open source workbook)

{record([
    ("Record", "*Data for Figure SPM.1*, version 0.0.1, 4 April 2022, Lamb et al."),
    ("DOI", "10.48490/vfxm-tm28 → ipcc-browser.ipcc-data.org/browser/dataset?id=437"),
    ("Content", "global net anthropogenic GHG emissions 1990–2019, Gt CO₂-eq (GWP100), by gas"),
    ("Access", "CSV in the *Data Downloads* section – JavaScript application, browser only"),
    ("Source", "Minx et al. (2021) ESSD · Zenodo 10.5281/zenodo.6483002"),
    ("In project", "`data/final/wgiii_spm1/global_ghg_emissions_by_gas_1970-2019.csv` – 1990: 38.3 · 2010: 52.6 · **2019: 59.1 Gt**"),
])}

Open item: download the official CSV in a browser and store it next to the rebuilt file for a one-to-one check.

➡ **Next** – CIESIN / SEDAC, the SYR host.
""",
    ),
    (
        "Step 4 · CIESIN / SEDAC – SYR final data (panels c, d)",
        "ciesin", "map",
        f"""
{PARTIAL}

SYR figure data are catalogued in the IPCC Data Catalogue and hosted by CIESIN / NASA SEDAC (Columbia University).

{record([
    ("Panel (c)", "*SYR LR Figure 2.1 (c): Changes in global surface temperature* · id 8498 · v1.0.0 (2025-04-10) · doi 10.7927/nq55-cr83 · Excel ~15 KB"),
    ("Panel (d)", "*SYR LR Figure 2.1 (d): Humans are responsible* · id 8493 · v1.0.0 (2025-04-09) · doi 10.7927/b38b-zp83 – verify on landing page"),
    ("Panels (a), (b)", "🔴 no SYR-level record – use WGIII SPM.1 / WGI Fig 2.5"),
    ("Access", "sedac.ciesin.columbia.edu/ddc/ar6-syr-lr-fig2-1c/ · sedac.ciesin.columbia.edu/ddc/ar6-syr-lr-fig2-1d/ – browser only"),
    ("Open item", "download both workbooks, confirm DOI and licence, save as CSV in `data/final/syr_fig2_1/`"),
])}

➡ **Next** – the status dashboard.
""",
    ),
    # ------------------------------------------------------------- status map
    (
        "Data status at a glance",
        WORLD, "markdown",
        f"""
## Where Figure 2.1 stands today
{STATUS_MATRIX}

### What changed on {CHECKED}
* CEDA catalogue reachable again → every CEDA DOI verified (all **citable**, all resolve).
* Four chapter-level CEDA records added → tier 3 is 🟢 for panels (b), (c), (d).
* CEDA *Input data for Figure 2.11* added → the four observational datasets behind panel (c).
* Notebook now loads CEDA files **live** (CORS enabled), falling back to the bundled copies.

### Still open
* SYR workbooks (c), (d) at SEDAC – browser only.
* DKRZ Supplements list – JavaScript only.
* CEDA SYR collection record – not yet published.

➡ **Next** – how to do this for any IPCC figure.
""",
    ),
    (
        "How to reuse the data",
        WORLD, "markdown",
        """
## From any IPCC figure to its data

1. **Read the caption's traceability tag** – it names the source figures.
2. **Final data first** – WGI/WGII → CEDA `10.5285/…` · WGIII → IPCC Data Catalogue `10.48490/…` · SYR → SEDAC `10.7927/…`.
3. **Open the README and licence** shipped with the record (CEDA: BADC-CSV).
4. **Need the chain?** Look for chapter-level and *input data* records at CEDA, DKRZ Supplements, and code on github.com/IPCC-WG1.
5. **Need raw inputs?** CMIP6 at DKRZ; observations and inventories at the producing institutions.
6. **Cite twice** – dataset DOI *and* report component. Redraw figures from data (images are IPCC copyright).

**In this project**
* `ar6_syr_fig2_1_data_story.ipynb` – reproduces the four panels live in the browser.
* `data/PROVENANCE.md` – every record, version, DOI, licence.
* `README.md` – open items.
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
                    "markdown": linkify(md.strip("\n")),
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
                "presentationTextColor": "#f5f7fa",
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
            "checked": CHECKED,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT} with {len(story_segments)} segments and {len(PLACES)} markers")


if __name__ == "__main__":
    main()
