# IPCC AR6 SYR Figure 2.1 — a data story for notebook.link

[![Launch on Notebook.link](https://img.shields.io/badge/notebook.link-launch-2b6cb0)](https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/)

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
| `storymap/ipcc_ar6_data_journey.jGIS` | JupyterGIS **Story Map**: 11 guided stops at the observatories, inventories and DDC archives behind the figure | double-click (JupyterGIS editor) → **Preview Mode**, or right-click → **Open With → Specta** for full-screen presentation |
| `data/final/…` | Unmodified copies of the CEDA records for WGI Fig SPM.1, SPM.2, Fig 2.5 (+ README/licence), and a CSV rebuilt from the Zenodo source of WGIII Fig SPM.1 | read by the notebook |
| `data/input/README.md`, `data/intermediate/README.md` | Detailed provenance of the input tier (EDGAR, bookkeeping models, NOAA/SIO/CSIRO/AGAGE/UCI, HadCRUT5 …, CMIP6 at DKRZ) and the intermediate tier (DKRZ `IPCC-DDC_AR6_Supplements`, CEDA, code on GitHub/Zenodo) | documentation |
| `data/PROVENANCE.md` | One table of every record, version, DOI, host, licence, plus citation templates | documentation |
| `scripts/` | Reproducible builders: `build_wgiii_spm1_from_essd.py` (Zenodo → CSV), `build_notebook.py` (nbformat → ipynb), `build_storymap.py` (→ .jGIS) | run locally |
| `environment.yml`, `nblink-lock.json`, `jupyter-lite.json` | notebook.link environment (xeus-python, numpy, pandas, matplotlib, jupytergis-lite), pinned lock file, Specta defaults | read by notebook.link |

## Run it on notebook.link

### A. Zero-setup link (public repository)

Prefix the repository URL with `notebook.link/`:

```
https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/
```

notebook.link reads `environment.yml` + `nblink-lock.json` from the repository
root, solves the WebAssembly environment in the browser and opens JupyterLab.
Then:

1. In the file browser double-click `ar6_syr_fig2_1_data_story.ipynb` and run all cells
   (`Run ▸ Run All Cells`). First start downloads ~50 MB of WebAssembly packages; later visits are cached.
2. For the reading view: right-click the notebook → **Open With ▸ Specta**
   (layout *article*, code hidden; the notebook metadata already sets this).
3. For the Story Map: double-click `storymap/ipcc_ar6_data_journey.jGIS`, then switch on
   **Preview Mode** in the Story panel, or right-click → **Open With ▸ Specta** for the full-screen guided story.

To open a file directly, append its path:
`https://notebook.link/github/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/lab/tree/ar6_syr_fig2_1_data_story.ipynb`

A link without a git reference always follows the latest commit of the default branch.
Pin a tag or commit for a permanent snapshot, e.g.
`https://notebook.link/github.com/IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story/commit/<sha>/`.

### B. Publish a permanent, aliased link from the notebook.link dashboard

1. Sign in at https://notebook.link (free individual plan; GitHub sign-in works).
2. **Links → New Link → Repository**: provider *GitHub*, repository
   `IPCC-Expert-Activity-7th-AR/ar6-syr-fig2-1-data-story`, git reference (`main` or a tag),
   *Document path* `ar6_syr_fig2_1_data_story.ipynb`, interface style *Specta* (or *Lab*),
   alias e.g. `ipcc-ar6-fig2-1`, visibility *public* or *unlisted*.
3. The link becomes `https://notebook.link/@<your-user>/ipcc-ar6-fig2-1` — this is the equivalent of
   `https://notebook.link/@arjxn-py/nepal-flash-flood`.
4. Create a second link with *Document path* `storymap/ipcc_ar6_data_journey.jGIS` and interface
   style *Specta* for the story-map presentation.

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
