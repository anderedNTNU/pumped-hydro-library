---
bibkey: gimeno2015assessment
bibkey_provisional: true
title: "Assessment of the European potential for pumped hydropower energy storage based on two existing reservoirs"
authors: "Marcos Gimeno-Gutiérrez, Roberto Lacal-Arántegui"
year: 2015
venue: "Renewable Energy 75, 856-868 (2015), doi:10.1016/j.renene.2014.10.068"
peer_reviewed: true
methods: []
review_sections: [phs-technology, ldes-seasonal-storage, reservoir-sizing-capacity]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/gimeno2015assessment.pdf
takeaway: "JRC GIS screening of new PHS formed by linking two existing European reservoirs (head >= 150 m, <= 20 km apart): 54 TWh theoretical / 29 TWh realisable storage potential; Norway only 0.99 TWh theoretical / 0.75 TWh realisable because only 129 of ~886 Norwegian reservoirs were in the database, and Norwegian PHS is limited by pump/turbine capacity, not reservoir volume."
---

# European PHS potential from linking two existing reservoirs (Gimeno-Gutiérrez & Lacal-Arántegui, 2015)

_Renewable Energy 75 (2015) 856–868; journal page = PDF page + 855 (PDF 1 = p. 856)._

## Research question / purpose
First European-wide estimate of **energy storage potential for new PHS created by connecting two existing reservoirs** (topology T1, Table 2, p. 857) with sufficient head and short distance, using a GIS model developed by JRC and University College Cork and validated by a SETIS expert workshop (pp. 857–858). T1 chosen for its low environmental impact (no new dam) (p. 857).

## Setting
- **System:** existing reservoirs ≥ 100,000 m³ in most EU states plus Norway, Switzerland, Turkey, Balkans, Iceland (pp. 858–859).
- **Markets:** none (resource assessment).
- **Horizon and resolution:** static; scenarios for maximum distance 1, 2, 3, 5, 10, 20 km (Table 3, p. 858).

## Method
- **Model type:** GIS screening (ArcGIS) on a DEM (SRTM 90 m to 60°N; **GMTED2010 250 m for the Nordic countries**, lower accuracy, p. 860) and the EEA ECRINS dam/reservoir database (p. 860).
- **Criteria (Table 3, p. 858; Table 4, p. 861):** min head 150 m; min reservoir 100,000 m³; ≥ 500 m from inhabited sites; ≥ 200 m from transport infrastructure; ≥ 500 m from UNESCO sites; ≤ 20 km to transmission grid; not within Natura 2000.
- **Potentials:** theoretical (topography + reservoirs) and realisable (after social, infrastructure, environmental and grid filters) (p. 858). A "hit" = overlapping circles of radius half the max distance around two dams (p. 861).
- **Energy calculation:** limited by the **upper** reservoir volume (assumed ≤ lower), head and an **80 % round-trip efficiency** (pp. 861–862); no natural inflow, no other water users (p. 861–862). No installed power (MW) estimated (p. 867).
- **Validation:** vs. 23 existing PHS (Table 5, p. 862): Pearson 0.998 for storage MWh; storage hours of existing EU PHS mostly 3–8 h (Montezic 35 h, La Muela II 32 h).

## Data / case
ECRINS reservoirs; CORINE Land Cover 2006; Natura 2000; UNESCO; Platts grid (pp. 859–861). **Norway: only 129 reservoirs in ECRINS vs 905 (886 > 100,000 m³) according to NVE** (p. 860).

## Key findings
- (p. 863, Table 6; p. 864, Table 8; Table 10, p. 865) Europe: theoretical **54.31 TWh** at 20 km (8,268 sites), 8.00 TWh at 10 km, 0.83 TWh at 5 km, 0.004 TWh at 1 km; realisable **28.63 TWh** at 20 km (3,229 sites), 1.32 TWh at 10 km.
- (p. 863, Table 7) Turkey dominates at 20 km (36.8 TWh theoretical, 19.6 TWh realisable).
- (p. 867) EU: 11.4 TWh theoretical, ~4 TWh realisable at 20 km.
- (p. 856, 865) Theoretical potential ≈ 3.5 × and realisable ≈ 2 × existing PHS storage in 14 countries (Eurelectric 2.5 TWh in 16 countries, p. 863).
- **Norway (Table 11, p. 866; Tables 7 and 9):** theoretical 991 GWh (20 km), 332 (10 km), 33 (5 km), 5.2 (3 km); realisable **747 GWh (20 km), 212 (10 km), 17 (5 km), 5.2 (3 km)**. Norway keeps most of its potential through the filters (p. 865).
- (p. 863) Norway's low potential is "surprising" given Europe's largest hydro capacity (30 GW); causes: reservoir **data gap** and **large distances between reservoirs**.
- (p. 865–866) Existing Norwegian PHS storage reported at **11 TWh** (Harby, different methodology); in Norway "pumping is not used on a daily or weekly cycle but for seasonal pumping between very large reservoirs"; pumping/generation is **limited by pump and turbine capacity, not reservoir size**; example: pumping into Blåsjø (7,000 GWh) (p. 866).
- (p. 866) Counting existing + realisable, most potential lies in Norway, Spain, Switzerland, France and the UK.
- (p. 867) For Norway, the challenge is "not the lack of storage volume but the total costs and the business model for developing pumped storage hydro, and in particular for increasing turbine capacity."
- (p. 862) Storage-to-power ratio: for PHS < 10 GWh, storage and installed capacity correlate (Pearson 0.91), not for larger plants; large reservoirs + low power → slow level changes and long-term storage; small reservoirs + high power → short-term balancing.

## Strengths
- Transparent, reproducible criteria; country-level tables for six distance scenarios.
- Explicit about data gaps (Norway) and conservative biases.

## Weaknesses / limitations
- Norway badly under-represented (129 of ~886 reservoirs); coarse DEM above 60°N → Norwegian figures are a lower bound.
- Energy only (no MW, no cost/economic potential); ignores inflow, other users, lower-reservoir limits and level-change rates (p. 867).
- Upper-reservoir-limited assumption fails where the lower reservoir is smaller (e.g. Bleiloch) — and Aurland III's lower reservoir (10 Mm³) is far smaller than its upper (448 Mm³; `pitorac2020technical`).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.1 LDES: European PHS potential | 54 TWh theoretical, 29 TWh realisable (20 km) | Abstract p. 856; Tables 6, 8, 10 pp. 863–865 |
| Background 2.2/2.3: Norwegian PHS is seasonal and power-limited | Seasonal pumping between very large reservoirs; limited by pump/turbine capacity; Blåsjø 7,000 GWh; existing 11 TWh | pp. 865–866 |
| Background: Norway new-PHS potential (T1) | 0.99 TWh theoretical / 0.75 TWh realisable (20 km), data-gap caveat | Table 11 p. 866; p. 860, 863 |
| Lit. review 5.5 sizing: storage vs power design | Storage hours of existing PHS 3–35 h; storage–power correlation <10 GWh; long- vs short-term services | Table 5 p. 862; p. 862 |
| Background: Norway barrier is turbine capacity and business model | Quote p. 867 | p. 867 |
| Background: EU hydro/PHS statistics 2011 | 335 TWh hydro, 29 TWh PHS output from 38 TWh pumping; 42.6 GW PHS in EU | Table 1, p. 857 |

## Useful quotes (with page numbers)
> "in Norway pumping is not used on a daily or weekly cycle but for seasonal pumping between very large reservoirs" (pp. 865–866)

## Follow-up references to check (backward snowballing)
- [12] Lacal-Arántegui, Fitzgerald & Leahy (2011), JRC: PHS potential from single dams.
- [11] Fitzgerald et al. (2012), Energy 41: GIS model for converting hydro schemes to PHS.
- [9] SETIS expert workshop on PHS potential (2012).
- [20] Eurelectric (2011), Hydro in Europe: powering renewables.
- [17] Harby (SINTEF), personal communication on Norwegian PHS storage.

