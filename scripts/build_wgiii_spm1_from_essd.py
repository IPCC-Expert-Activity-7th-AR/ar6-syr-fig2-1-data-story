#!/usr/bin/env python3
"""Build a small, notebook-friendly CSV of global GHG emissions by gas (1970-2019).

Source (input data for WGIII Figure SPM.1 / SYR Figure 2.1 panel a):
  Minx, J.C., Lamb, W.F., Andrew, R.M., et al. (2021/2022):
  "A comprehensive and synthetic dataset for global, regional and national
  greenhouse gas emissions by sector 1970-2018 with an extension to 2019",
  Earth System Science Data 13, 5213-5252, doi:10.5194/essd-13-5213-2021.
  Data: Zenodo, doi:10.5281/zenodo.6483002 (files essd_ghg_data_gwp100.xlsx,
  essd_lulucf_data.xlsx).  Emissions are in t CO2-eq using AR6 GWP100 values;
  CO2-LULUCF is the mean of three bookkeeping models (BLUE, H&N, OSCAR), the
  same convention used by WGIII.

The official WGIII "Data for Figure SPM.1" record is held in the IPCC Data
Catalogue (doi:10.48490/vfxm-tm28, MetadataWorks).  That site is
JavaScript-only and could not be downloaded programmatically, so this script
rebuilds equivalent global totals directly from the published source data.

Usage:
  python scripts/build_wgiii_spm1_from_essd.py [--cache DIR]

The two Zenodo workbooks (~14 MB) are downloaded into --cache (default
./.cache) if not already present.  Output:
  data/final/wgiii_spm1/global_ghg_emissions_by_gas_1970-2019.csv
"""
import argparse
import pathlib
import sys
import urllib.request

import pandas as pd

ZENODO = "https://zenodo.org/api/records/6483002/files/{}/content"
FILES = ["essd_ghg_data_gwp100.xlsx", "essd_lulucf_data.xlsx"]
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "data" / "final" / "wgiii_spm1" / "global_ghg_emissions_by_gas_1970-2019.csv"


def fetch(cache: pathlib.Path) -> None:
    cache.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        target = cache / name
        if target.exists():
            continue
        print(f"downloading {name} ...", file=sys.stderr)
        urllib.request.urlretrieve(ZENODO.format(name), target)


def build(cache: pathlib.Path) -> pd.DataFrame:
    ghg = pd.read_excel(cache / "essd_ghg_data_gwp100.xlsx", sheet_name="data")
    lulucf = pd.read_excel(cache / "essd_lulucf_data.xlsx", sheet_name="data")

    # Global totals by gas, t CO2-eq -> Gt CO2-eq
    g = ghg.groupby("year")[["CO2", "CH4", "N2O", "Fgas"]].sum() / 1e9
    g = g.rename(columns={"CO2": "CO2_FFI", "Fgas": "F_gases"})

    # CO2-LULUCF: sum of regional means of the three bookkeeping models
    lu = lulucf.groupby("year")[["blue", "houghton", "oscar", "mean"]].sum() / 1e9
    g["CO2_LULUCF"] = lu["mean"]
    g["CO2_LULUCF_BLUE"] = lu["blue"]
    g["CO2_LULUCF_HN"] = lu["houghton"]
    g["CO2_LULUCF_OSCAR"] = lu["oscar"]

    g = g.loc[1970:2019]
    g["GHG_total"] = g[["CO2_FFI", "CO2_LULUCF", "CH4", "N2O", "F_gases"]].sum(axis=1)
    g = g[["CO2_FFI", "CO2_LULUCF", "CH4", "N2O", "F_gases", "GHG_total",
           "CO2_LULUCF_BLUE", "CO2_LULUCF_HN", "CO2_LULUCF_OSCAR"]].round(4)
    g.index.name = "year"
    return g


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=str(HERE.parent / ".cache"))
    args = ap.parse_args()
    cache = pathlib.Path(args.cache)
    fetch(cache)
    df = build(cache)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# Global net anthropogenic GHG emissions by gas, Gt CO2-eq/yr (AR6 GWP100)\n"
        "# Rebuilt from Minx et al. (2021) ESSD dataset, Zenodo doi:10.5281/zenodo.6483002\n"
        "# CO2_LULUCF = mean of BLUE, Houghton & Nassikas, OSCAR bookkeeping models\n"
        "# Equivalent to the data behind IPCC AR6 WGIII Figure SPM.1 (doi:10.48490/vfxm-tm28)\n"
        "# and SYR Longer Report Figure 2.1 panel (a). Licence of source data: CC BY 4.0\n"
    )
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(header)
        df.to_csv(fh)
    print(f"wrote {OUT} ({len(df)} rows)")
    print(df.loc[[1990, 2000, 2010, 2019]].round(2).to_string())


if __name__ == "__main__":
    main()
