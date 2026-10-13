# IPCC AR6 SYR Figure 2.1 — a data story for notebook.link

[![Launch on Notebook.link](https://img.shields.io/badge/notebook.link-JupyterLab-2b6cb0?logo=jupyter&logoColor=white)](https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/lab/)
[![Story Map](https://img.shields.io/badge/Story%20Map-open%20in%20Specta-0b7a3b?logo=openstreetmap&logoColor=white)](https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/specta/?path=storymap/ipcc_ar6_data_journey.jGIS)
[![Story Map editor](https://img.shields.io/badge/Story%20Map-JupyterGIS%20editor-0b7a3b?logo=openstreetmap&logoColor=white)](https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/lab/?path=storymap/ipcc_ar6_data_journey.jGIS)
[![Data story notebook](https://img.shields.io/badge/Data%20story-read%20in%20Specta-c2410c?logo=jupyter&logoColor=white)](https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/specta/?path=ar6_syr_fig2_1_data_story.ipynb)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Story%20Map%20(Specta)-444?logo=github)](https://ipcc-expert-activity-7th-ar.github.io/ar6-syr-fig2-1-data-story/specta/?path=storymap/ipcc_ar6_data_journey.jGIS)

An interactive, browser-only (JupyterLite / WebAssembly) story that starts from
**IPCC AR6 Synthesis Report, Longer Report Figure 2.1** — *the causal chain from
emissions to resulting warming* — and follows the IPCC's **input → intermediate
→ final** data model to show where every number in the figure comes from, which
Data Distribution Centre (DDC) partner archives it, and how to reuse it.

Audience: policy analysts and data practitioners. Language: English.

## What is in the project

| Path | What it is | How to open on notebook.link |
|---|---|---|
| `ar6_syr_fig2_1_data_story.ipynb` | The data story: narrative + live reproduction of the four panels from archived final data (pandas + matplotlib, runs in the browser) | double-click in the file browser, or right-click → **Open With → Specta** for the article view |
| `storymap/ipcc_ar6_data_journey.jGIS` | JupyterGIS **Story Map**: 20 guided stops organised as **Step 1 report → Step 2 input → Step 3 intermediate → Step 4 final data**, each with catalogue record, DOI, version, files, licence and an availability flag (`AVAILABLE` / `ONLINE` / `PARTIAL` / `MISSING`), ending with a status dashboard | double-click (JupyterGIS editor) → **Preview Mode**, or right-click → **Open With → Specta** for full-screen presentation |
| `data/final/…` | Unmodified copies of the CEDA records for WGI Fig SPM.1, SPM.2, Fig 2.5 (+ README/licence), and a CSV rebuilt from the Zenodo source of WGIII Fig SPM.1 | read by the notebook |
| `data/input/README.md`, `data/intermediate/README.md` | Detailed provenance of the input tier (EDGAR, bookkeeping models, NOAA/SIO/CSIRO/AGAGE/UCI, HadCRUT5 …, CMIP6 at DKRZ) and the intermediate tier (DKRZ `IPCC-DDC_AR6_Supplements`, CEDA, code on GitHub/Zenodo) | documentation |
| `data/PROVENANCE.md` | One table of every record, version, DOI, host, licence, plus citation templates | documentation |
| `scripts/` | Reproducible builders: `build_wgiii_spm1_from_essd.py` (Zenodo → CSV), `build_notebook.py` (nbformat → ipynb), `build_storymap.py` (→ .jGIS) | run locally |
| `environment.yml`, `nblink-lock.json`, `jupyter-lite.json` | notebook.link environment (xeus-python, numpy, pandas, matplotlib, jupytergis-lite), pinned lock file, Specta defaults | read by notebook.link |

## Run it on notebook.link

### A. Direct links (no account needed)

notebook.link resolves `https://notebook.link/github/{owner}/{repo}/[tree/{branch}/|commit/{sha}/]{app}/?path={file}`
where `{app}` is `lab` (JupyterLab), `notebooks`, `edit`, `tree`, `voici` or `specta` (presentation). The badges above use:

| What you want | Link |
|---|---|
| Story Map, full-screen guided presentation | `https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/specta/?path=storymap/ipcc_ar6_data_journey.jGIS` |
| Story Map in the JupyterGIS editor (layers, segments, Preview Mode) | `https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/lab/?path=storymap/ipcc_ar6_data_journey.jGIS` |
| Data-story notebook as an article (code hidden, charts computed live) | `https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/specta/?path=ar6_syr_fig2_1_data_story.ipynb` |
| Data-story notebook in JupyterLab | `https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/lab/?path=ar6_syr_fig2_1_data_story.ipynb` |
| Plain JupyterLab with the file browser | `https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/lab/` |

On first start notebook.link reads `environment.yml` + `nblink-lock.json` from the repository root and installs the WebAssembly
environment (xeus-python, pandas, matplotlib, **jupytergis-lite**, **specta**) — wait for the boot screen to finish; do not press
*Continue*, which would skip to a bare default environment without JupyterGIS and Specta. Later visits are cached.

Inside JupyterLab: the `.jGIS` file opens in the JupyterGIS map editor (left panel *Layers* / *Segments*, right panel *Story*
with the **Preview Mode** switch); right-click any file → **Open With ▸ Specta** gives the presentation view.
A link without a git reference follows the latest commit of `main`; pin a tag or commit for a permanent snapshot, e.g.
`…/ar6-syr-fig2-1-data-story/commit/<sha>/specta/?path=storymap/ipcc_ar6_data_journey.jGIS`.

### B. Short aliased link from the notebook.link dashboard (optional)

Sign in at https://notebook.link → **Links → New Link → Repository**: GitHub, repository
`IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story`, reference `main` or a tag, *Document path*
`storymap/ipcc_ar6_data_journey.jGIS`, interface style *Presentation* (Specta), alias e.g. `ipcc-ar6-fig2-1`.
The result is `https://notebook.link/@<user>/ipcc-ar6-fig2-1`, the same form as `@arjxn-py/nepal-flash-flood`.

### GitHub Pages mirror (self-hosted JupyterLite)

`.github/workflows/deploy.yml` builds the same content as a static JupyterLite site with the Specta app and publishes it to
GitHub Pages (Settings → Pages → Source: *GitHub Actions*; the workflow enables it on first run when allowed).
URLs: `https://ipcc-expert-activity-7th-ar.github.io/ar6-syr-fig2-1-data-story/specta/?path=storymap/ipcc_ar6_data_journey.jGIS`
and `…/lab/?path=ar6_syr_fig2_1_data_story.ipynb`.

### C. Edit collaboratively inside notebook.link (optional)

Create a **project** from the *Jupyter GIS Stack* environment, upload the repository content,
edit the story map with the JupyterGIS GUI (segment extents, images, layer overrides), take a
**public snapshot** and create a *Project Snapshot* link. Export the edited `.jGIS` back into
this repository to keep Git as the source of truth.

## Rebuild locally

```bash
pip install pandas matplotlib openpyxl nbformat nbclient ipykernel mambajs
python scripts/build_wgiii_spm1_from_essd.py        # downloads 2 Zenodo workbooks (~14 MB) to .cache/
python scripts/build_storymap.py                    # writes storymap/ipcc_ar6_data_journey.jGIS
python scripts/build_notebook.py --execute          # writes + executes the notebook
mambajs create-lock environment.yml nblink-lock.json   # refresh the lock after changing environment.yml
```

## Open items (need a browser / human check)

- [ ] Download the SYR-level Excel workbooks for panels (c) and (d) from CIESIN/SEDAC
      (doi:10.7927/nq55-cr83, doi:10.7927/b38b-zp83), confirm the DOI shown for (d), convert to CSV,
      place in `data/final/syr_fig2_1/` (instructions in that folder's README). The notebook's
      final comparison cell activates automatically.
- [ ] Browse the DKRZ *Find data* list for `IPCC-DDC_AR6_Supplements` and note any GMST/attribution entries.
- [ ] Optional: replace the OpenStreetMap basemap in the story map with a muted style, and add
      per-stop images (the `image` field of each segment is empty by design — IPCC figure images are
      under the IPCC copyright policy).
- [ ] Optional: tune segment extents/zoom in the JupyterGIS GUI and commit the edited `.jGIS`.

## Licences and citation

Data files are redistributed under their original licences (CEDA records and the Zenodo ESSD
dataset: CC BY 4.0). See `data/PROVENANCE.md` for full citations; IPCC data policy asks for
*both* the dataset DOI and the report component to be cited. Code in `scripts/` is MIT.
Figure *images* of the IPCC are not reproduced; all charts are redrawn from data.
