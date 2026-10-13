# SYR Longer Report Figure 2.1 – final data (IPCC Data Catalogue / CIESIN-SEDAC)

The Synthesis Report's final figure data are published through the IPCC Data
Catalogue (https://ipcc-browser.ipcc-data.org, operated by MetadataWorks) and
hosted by CIESIN / NASA SEDAC at Columbia University (DOI prefix 10.7927).

| Panel | Catalogue record | DOI | Landing page | File |
|---|---|---|---|---|
| (a) emissions | none at SYR level | – | – | use `../wgiii_spm1/` (WGIII Figure SPM.1) |
| (b) concentrations | none at SYR level | – | – | use `../wgi_ch2_fig2_5/` (WGI Figure 2.5) |
| (c) observed temperature | dataset 8498, v1.0.0, 2025-04-10 | 10.7927/nq55-cr83 | https://sedac.ciesin.columbia.edu/ddc/ar6-syr-lr-fig2-1c/ | Excel workbook (~15.5 KB) |
| (d) attributed warming | dataset 8493, v1.0.0, 2025-04-09 | 10.7927/b38b-zp83 (verify) | https://sedac.ciesin.columbia.edu/ddc/ar6-syr-lr-fig2-1d/ | Excel workbook |

## TODO – needs completion by a human with a browser

- [ ] Open the two SEDAC landing pages, confirm the DOI shown for panel (d)
      (search engines showed inconsistent DOIs), note the licence statement.
- [ ] Download the two Excel workbooks and save them here as
      `syr_lr_fig2_1c.xlsx` and `syr_lr_fig2_1d.xlsx`
      (the SEDAC servers refused non-browser connections on 2026-10-13).
- [ ] Export each workbook to CSV (`syr_lr_fig2_1c.csv`, `syr_lr_fig2_1d.csv`)
      so the WebAssembly kernel can read it without `openpyxl`.
- [ ] Un-comment the "SYR final data" cell in the notebook to compare the SYR
      workbook values with the WGI SPM.1 / SPM.2 values.

Until then the notebook reproduces panels (c) and (d) from the WGI SPM.1 and
SPM.2 final data archived at CEDA, which are the sources cited in the SYR caption.

Note: the CEDA catalogue also has a record for an "IPCC AR6 Synthesis Report
(SYR)" dataset collection (uuid 9177e927f0664da9bf1e25f57561d0d8) but it was
marked "not yet published" when checked.
