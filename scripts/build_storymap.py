#!/usr/bin/env python3
"""Generate the JupyterGIS Story Map (storymap/ipcc_ar6_data_journey.jGIS).

The story follows the data behind IPCC AR6 SYR Figure 2.1 around the world:
observatories that produce the input data, the IPCC Data Distribution Centre
partners (DKRZ, CSIC, CEDA, CIESIN) that archive input/intermediate/final
data, and the IPCC Secretariat where the figure is published.

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
    mpp = 2 * math.pi * R / 256 / 2 ** zoom  # metres per pixel in EPSG:3857
    dx, dy = w_px / 2 * mpp, h_px / 2 * mpp
    return [x - dx, y - dy, x + dx, y + dy]


def uid():
    return str(uuid.uuid4())


# ---------------------------------------------------------------- places ----
# (name, lon, lat, marker colour, role)
PLACES = [
    ("IPCC Secretariat, Geneva", 6.1400, 46.2220, "#1f4e79", "final-figure"),
    ("Mauna Loa Observatory (NOAA GML)", -155.5763, 19.5362, "#2e7d32", "input"),
    ("Cape Grim Baseline Station (CSIRO / AGAGE)", 144.6900, -40.6830, "#2e7d32", "input"),
    ("Met Office Hadley Centre, Exeter (HadCRUT)", -3.4740, 50.7270, "#2e7d32", "input"),
    ("JRC Ispra (EDGAR emissions database)", 8.6280, 45.8100, "#2e7d32", "input"),
    ("DKRZ, Hamburg (IPCC DDC: CMIP6 input + intermediate data)", 9.9800, 53.5680, "#b26a00", "ddc"),
    ("CSIC-IFCA, Santander (IPCC DDC: Interactive Atlas)", -3.8040, 43.4710, "#b26a00", "ddc"),
    ("CEDA, Harwell (IPCC DDC: WGI final figure data)", -1.3140, 51.5740, "#c62828", "ddc"),
    ("CIESIN / SEDAC, Palisades NY (IPCC DDC: SYR final figure data)", -73.9120, 41.0040, "#c62828", "ddc"),
]

SEGMENTS = [
    # (title, place index or None, zoom, markdown, image)
    (
        "The data journey behind one IPCC figure",
        None,
        1.4,
        (
            "## From emissions to warming: where does Figure 2.1 come from?\n\n"
            "IPCC AR6 Synthesis Report, Longer Report **Figure 2.1** shows the causal chain from "
            "greenhouse-gas emissions (a), to atmospheric concentrations (b), to observed warming (c), "
            "to the human contribution to that warming (d).\n\n"
            "The IPCC manages the data behind every figure in three tiers:\n\n"
            "* **Input data** – observations and model output used by authors\n"
            "* **Intermediate data** – processed products created during the assessment\n"
            "* **Final data** – the numbers plotted in the published figure\n\n"
            "This story visits the places where each tier is produced and archived. "
            "Use the arrows to move between stops. The companion notebook reproduces all four panels "
            "from the archived final data."
        ),
        "",
    ),
    (
        "Stop 1 · IPCC Secretariat, Geneva — the published figure",
        0,
        12,
        (
            "**Final figure.** Figure 2.1 was approved with the Synthesis Report in March 2023 and is "
            "published at [ipcc.ch](https://www.ipcc.ch/report/ar6/syr/figures/figure-2-1).\n\n"
            "Its caption traces each panel back to the Working Group reports: "
            "**WGIII Figure SPM.1** (panel a), **WGI Section 2.1 / Figure 2.5** (panel b), "
            "**WGI Figure SPM.1** (panel c) and **WGI Figure SPM.2** (panel d).\n\n"
            "Following those references is the key to finding the data."
        ),
        "",
    ),
    (
        "Stop 2 · Mauna Loa — measuring CO₂ (input data, panel b)",
        1,
        11,
        (
            "**Input data.** The CO₂ curve in panel (b) starts in 1958 with the continuous record from "
            "Mauna Loa, Hawaii, run by NOAA's Global Monitoring Laboratory and the Scripps Institution of "
            "Oceanography.\n\n"
            "WGI Chapter 2 combined global means from **NOAA GML, SIO, CSIRO, AGAGE and UCI** networks. "
            "These observational inputs are not held by the IPCC DDC; they are cited to the originating "
            "networks and listed in the WGI Annex III and the FAIR data table for Figure 2.5."
        ),
        "",
    ),
    (
        "Stop 3 · Cape Grim — CH₄ and N₂O (input data, panel b)",
        2,
        11,
        (
            "**Input data.** Cape Grim, Tasmania, is a Southern-Hemisphere baseline station of CSIRO and "
            "the AGAGE network. Its flask and in-situ records are part of the CH₄ (1983–2019) and "
            "N₂O (1978–2019) global means plotted in panel (b).\n\n"
            "The archived final data for WGI Figure 2.5 (CEDA, doi:10.5285/c6f19b27f8e74e98968c17c8e1f74c60) "
            "keeps the network-by-network series (NOAA, AGAGE, CSIRO, UCI, SIO) so the provenance stays visible."
        ),
        "",
    ),
    (
        "Stop 4 · Exeter — the global temperature record (input data, panels c & d)",
        3,
        12,
        (
            "**Input data.** The observed warming in panels (c) and (d) rests on blended land–ocean "
            "temperature datasets. WGI Chapter 2 assessed **HadCRUT5** (Met Office Hadley Centre / UEA), "
            "**NOAAGlobalTemp-Interim**, **Berkeley Earth** and **Kadow et al. (2020)**; "
            "the WGI SPM.2 attribution used **HadCRUT4.6**.\n\n"
            "Pre-industrial context comes from the **PAGES 2k** multi-proxy reconstruction (1–2000 CE) and "
            "a mid-Holocene (~6500 yr BP) assessment."
        ),
        "",
    ),
    (
        "Stop 5 · Ispra — emissions inventories (input data, panel a)",
        4,
        12,
        (
            "**Input data.** Panel (a) is built from the **EDGAR v6** inventory of the EU Joint Research "
            "Centre (fossil CO₂, CH₄, N₂O, F-gases), combined with CO₂ from land-use change as the mean "
            "of three bookkeeping models (**BLUE, Houghton & Nassikas, OSCAR**) from the Global Carbon Budget.\n\n"
            "WGIII Chapter 2 authors (MCC Berlin) harmonised these into the ESSD dataset of "
            "Minx et al. (2021), archived on Zenodo (doi:10.5281/zenodo.6483002)."
        ),
        "",
    ),
    (
        "Stop 6 · DKRZ Hamburg — CMIP6 input & intermediate data",
        5,
        12,
        (
            "**IPCC DDC — input & intermediate.** The German Climate Computing Centre hosts two DDC "
            "collections:\n\n"
            "* **IPCC-AR6_CMIP6** – the ~65,000 CMIP6 datasets (historical, ssp245, hist-nat, hist-GHG, "
            "hist-aer …) used by WGI, each with a DOI `10.26050/WDCC/AR6.*`. The model lines in WGI SPM.1 "
            "and the attribution bars in SPM.2 / SYR 2.1(d) are computed from these.\n"
            "* **IPCC-DDC_AR6_Supplements** – intermediate datasets created by IPCC authors "
            "(e.g. assessed GSAT projections, sea-level projections).\n\n"
            "No intermediate record exists specifically for Figure 2.1; the processing chain is "
            "documented in the WGI code repositories (github.com/IPCC-WG1)."
        ),
        "",
    ),
    (
        "Stop 7 · Santander — CSIC and the Interactive Atlas",
        6,
        12,
        (
            "**IPCC DDC — input & intermediate.** CSIC-IFCA hosts the WGI **Interactive Atlas** and the "
            "regional intermediate data behind it. Together with DKRZ it is the DDC's long-term archive for "
            "input and intermediate datasets.\n\n"
            "Figure 2.1 is a global figure, so the Atlas is not one of its sources, but it is where regional "
            "versions of the same observational and CMIP6 inputs can be explored."
        ),
        "",
    ),
    (
        "Stop 8 · CEDA Harwell — WGI final figure data",
        7,
        12,
        (
            "**IPCC DDC — final data (WGI).** The Centre for Environmental Data Analysis archives the numbers "
            "plotted in WGI figures, under **CC BY 4.0**:\n\n"
            "* Figure SPM.1 – doi:10.5285/0b2759059ad6474098e40dad73e0a8ec (panel c)\n"
            "* Figure SPM.2 – doi:10.5285/c1eb6dad1598427f8f9f3eae346ece2f (panel d)\n"
            "* Figure 2.5 – doi:10.5285/c6f19b27f8e74e98968c17c8e1f74c60 (panel b)\n\n"
            "Each record carries a README, a licence file and a citation that must be used together "
            "with the report citation. These CSV files are bundled in this project and plotted in the notebook."
        ),
        "",
    ),
    (
        "Stop 9 · Palisades NY — SYR final figure data",
        8,
        12,
        (
            "**IPCC DDC — final data (SYR).** For the Synthesis Report the final data are published through "
            "the IPCC Data Catalogue and hosted by **CIESIN / NASA SEDAC** at Columbia University:\n\n"
            "* SYR LR Figure 2.1 (c) – doi:10.7927/nq55-cr83\n"
            "* SYR LR Figure 2.1 (d) – doi:10.7927/b38b-zp83\n\n"
            "Panels (a) and (b) have no SYR-level record yet; their data are the WGIII and WGI records "
            "visited earlier. The CEDA record for the SYR collection exists but is not yet published."
        ),
        "",
    ),
    (
        "Using the data",
        None,
        1.4,
        (
            "## How to reuse Figure 2.1 data\n\n"
            "1. **Start from the figure caption** – the `{WGI SPM.1 …}` references name the source figures.\n"
            "2. **Look up the final data** – WGI/WGII at CEDA (`10.5285/…`), WGIII at the IPCC Data Catalogue "
            "(`10.48490/…`), SYR at CIESIN/SEDAC (`10.7927/…`).\n"
            "3. **Trace inputs** – CMIP6 at DKRZ (`10.26050/WDCC/AR6.*`), observations at the originating networks.\n"
            "4. **Cite twice** – the dataset DOI *and* the report chapter.\n\n"
            "Open the notebook `ar6_syr_fig2_1_data_story.ipynb` in this project to reproduce the four panels "
            "from the archived data."
        ),
        "",
    ),
]


def main() -> None:
    layers, sources, layer_tree, story_segments = {}, {}, [], []

    # Basemap
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

    # Markers
    for name, lon, lat, colour, _role in PLACES:
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

    # Story segments
    for title, idx, zoom, md, image in SEGMENTS:
        if idx is None:
            lon, lat = 10.0, 30.0
            content_mode = "markdown"
        else:
            _, lon, lat, _, _ = PLACES[idx]
            content_mode = "map"
        seg = uid()
        layers[seg] = {
            "name": title,
            "type": "StorySegmentLayer",
            "visible": True,
            "parameters": {
                "zoom": zoom,
                "extent": extent(lon, lat, zoom),
                "content": {
                    "contentMode": content_mode,
                    "title": title,
                    "markdown": md,
                    "image": image,
                },
                "layerOverride": [],
                "transition": {"type": "smooth", "time": 2.0},
            },
        }
        layer_tree.append(seg)
        story_segments.append(seg)

    lon0, lat0 = 10.0, 30.0
    doc = {
        "schemaVersion": "0.6.0",
        "layerTree": layer_tree,
        "layers": layers,
        "sources": sources,
        "stories": {
            uid(): {
                "title": "IPCC AR6 SYR Figure 2.1 – the data journey",
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
            "zoom": 1.4,
            "extent": extent(lon0, lat0, 1.4),
        },
        "viewState": {},
        "metadata": {
            "description": "Story map of the data behind IPCC AR6 SYR Longer Report Figure 2.1",
            "generated_by": "scripts/build_storymap.py",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT} with {len(story_segments)} segments and {len(PLACES)} markers")


if __name__ == "__main__":
    main()
