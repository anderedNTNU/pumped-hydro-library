---
bibkey: nve2026hydrologiske
bibkey_provisional: true
title: "Hydrologiske data til kraftsituasjonsrapporten"
authors: "NVE (contact: Maria Sidelnikova)"
year: 2026
venue: "nve.no web page / data tool, published 11.11.2021, last updated 03.06.2026"
peer_reviewed: false
methods: [uncertainty-modelling]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "NVE weekly hydrological data per Norwegian price area (precipitation energy, usable inflow, snow, hydrological balance vs 20-year mean) in net energy terms (GWh), from HBV models driven by MET Norway grids; since 2015 usable inflow is back-calculated from production and reservoir change; NLOD/CC BY licence; series revised on 3 June 2026."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/06_Hydrologi_statistikk_og_data/45_NVE_2024a_Hydrologiske_data_til_kraftsituasjonsrapporten_NETTSIDE.pdf
---

# Hydrological data for the power situation report (NVE, 2026)

**Source file:** `source.pdf` / `source.txt` (2-page snapshot made 28.10.2026). URL: https://www.nve.no/energi/analyser-og-statistikk/hydrologiske-data-til-kraftsituasjonsrapporten/. In Norwegian. The inbox file name says "NVE_2024a" (version used in the 2025 project report); the snapshot shows last update 03.06.2026, hence the key year 2026.

## Research question / purpose
Documents NVE's weekly hydrological series per price area, as published in the weekly power situation report (kraftsituasjonsrapporten).

## Setting
Norway, price areas NO1–NO5; weekly resolution.

## Method
- **Model type:** HBV rainfall–runoff models (snow, soil moisture, groundwater) driven by nationwide precipitation and temperature grids from MET Norway (new grid from 15 Dec 2021), calibrated to observed inflow or runoff. Water is converted to energy via energy equivalents (p. 1–2).
- **Exception:** **usable inflow (nyttbart tilsig) from 2015 onward is computed from production plus change in reservoir energy**, not from HBV. Historical max, min and mean still come from HBV (p. 2).

## Data / case
- **Definitions (p. 1):** *precipitation energy* = energy in the week's precipitation over the catchments minus evaporation (can be negative); *usable inflow* = energy in the water flowing to reservoirs and plants during the week; *hydrological balance* = deviation from the historical mean of reservoir filling plus snow, soil water and groundwater. **Reference period: the last 20 years.**
- **Net values (p. 1):** only water usable for production is counted; flood spill and minimum-flow releases are subtracted (reservoir filling is gross). Values refer to today's production system (p. 2).
- **Revision (p. 1):** from 3 June 2026, HBV-based figures for 2024 to April 2026 were adjusted (updated temperature and precipitation); production-based inflow is unaffected.
- **Licence (p. 2):** NLOD (compatible with CC BY 3.0 NO).

## Key findings
- See definitions above; the page is a data-documentation source.

## Strengths
The official, citable description of the most likely inflow data source for a Norwegian case (weekly, per price area, energy units).

## Weaknesses / limitations
Aggregated per price area in energy units (GWh), not plant-level m³/s. Methodological break in 2015 (HBV-based vs production-based inflow). Retroactive revisions (June 2026) mean that downloaded series depend on the download date.

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where |
|---|---|---|
| Data: source and definition of weekly inflow | Usable inflow definition, net values, per price area | p. 1 |
| Data: how inflow is estimated | HBV + MET grids; production-based from 2015 | p. 1–2 |
| Data: reference "normal" | Last 20 years | p. 1 |
| Data: licence/reproducibility | NLOD; revision on 3 June 2026 | p. 1–2 |

## Useful quotes (with page numbers)
> "Nyttbart tilsig viser mengden energi i vannet som renner til vannmagasiner og kraftverk i løpet av uka." (p. 1)

## Follow-up references to check (backward snowballing)
- NVE HBV model page (inbox item 43, not filed); Bergström (1976) HBV model; NVE magasinstatistikk.

