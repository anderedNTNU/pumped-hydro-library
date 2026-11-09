---
bibkey: harby2025muligheter
bibkey_provisional: true
title: "Muligheter og utfordringer i Driva: Pumpekraft og miljøforbedringer"
authors: "Atle Harby, Markus Först (SINTEF Energi AS)"
year: 2025
venue: "SINTEF Energi AS, prosjektnotat 25.12.09, versjon 1.0, 27 Feb 2025, prosjektnr. 502004169, for Trønderenergi Kraft AS (open). Published as an attachment on https://www.tronderenergi.no/nedre-driva"
peer_reviewed: false
methods: [heuristics-simulation]
review_sections: [phs-technology, reservoir-sizing-capacity]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "SINTEF memo for TrønderEnergi's Nedre Driva project: purely hydrological sizing (1973–2024 daily flows, no prices) of a pump lifting water from the river Driva to Gjevilvatnet under minimum-flow rules; ~30 m³/s pump with 20/5 m³/s summer/winter minimum flow fills 68 Mm³ before 20 June in all years and allows ~365 Mm³/yr pumping; reversible unit could also release water for winter low flows."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/05_Investering_opprusting_og_okonomi/Tilleggsdokumenter/73_TronderEnergi_2025_Nedre_Driva_Mer_kraft_og_effekt_for_fremtiden_VEDLEGG_IKKE_SELVE_KILDEN.pdf
---

# Pumped storage and environmental flows in Driva (Harby & Först / SINTEF, 2025)

Norwegian-language SINTEF project note (21 pp.), prepared by Atle Harby, approved by Håkon Sundt, client contact Petter Hersleth (p. 1). The inbox labels it "VEDLEGG, IKKE SELVE KILDEN": it is an attachment to the TrønderEnergi web page "Nedre Driva: mer kraft og effekt for fremtiden" (inbox `73_TronderEnergi_2025_..._NETTSIDE.pdf`), which is the source originally collected. This note covers the SINTEF memo; project facts from the web page are marked "(web page)".
**Page convention:** printed page = PDF page ("x av 21"). Read in full.

## Research question / purpose
Preliminary assessment of (i) how much water can be pumped from Driva at Festa into Gjevilvatnet for different pump capacities and minimum-flow requirements, and (ii) whether releases from Gjevilvatnet (via a reversible pump-turbine or a valve) can improve low-flow habitat for salmon and trout (pp. 1, 3–5).

## Setting
- **System:** Driva kraftverk (in operation since 1973) with intake reservoir Gjevilvatnet (Oppdal); proposed pump from Driva at Festa up to Gjevilvatnet, extra water for Driva kraftverk or a new plant with outlet in Sunndalsfjorden, giving higher head and possibly more storage in Gjevilvatnet "so that a plant can be operated more flexibly" (p. 4). (Web page: Driva today 2 × 75 MW Francis, 565 m head, 600 GWh/yr; Gjevilvatnet 15 m regulation (645.8–660.8 masl); Nedre Driva would add a new underground station at Sunndalsøra with ~90 m more head (~660 m total), ~35 km headrace, combined 1100 GWh and 550 MW; 600 MW notified to NVE; owners TrønderEnergi 75 % / Istad Kraft 25 %.)
- **Markets:** none; electricity prices explicitly ignored (p. 5).
- **Horizon and resolution:** daily mean flows 1 Jan 1973 – 31 Dec 2024 at gauge Driva v/Grensehølen (p. 5).

## Method
- **Model type:** rule-based hydrological simulation (no optimisation): flow above the minimum-flow requirement is pumped up to pump capacity; if natural flow is below the requirement, water is released from Gjevilvatnet (p. 5).
- **Scenarios:** pump capacity 10–50 m³/s in 5 m³/s steps; minimum flow 20 or 30 m³/s in summer and 5 or 10 m³/s in winter at Grensehølen (≈ 20 % lower at Festa) (pp. 5, 7). Target: pump ≥ 68 Mm³ before 20 June each year (p. 7).
- **Habitat:** NINA mesohabitat mapping (Foldvik et al. 2023) evaluated with Li & Reynolds contagion, Shannon diversity and O'Neill dominance indices; judgmental extrapolation to ~5 m³/s (pp. 12–17).
- **Key assumptions:** no prices, no technical/operational pump limits (minimum pumpable flow, start/stop), fixed calendar dates for release periods (p. 5).

## Data / case
Mean flow at Grensehølen 32 m³/s; winter lows Dec–Mar with mean weekly minimum 4.4 m³/s, 5-percentile 4.8 m³/s, measurements < 2 m³/s; spring flood May–July up to 680 m³/s (pp. 4–7, Table 1).

## Key findings
- (p. 7) To pump 68 Mm³ before 20 June on average: 15 m³/s pump suffices with 5 m³/s winter minimum flow; 35 m³/s needed with 10 m³/s winter minimum flow.
- (p. 8, Table 2) With 40 m³/s and M30-5 the 68 Mm³ target is met in all 52 years; with M20-5 a **30 m³/s** pump meets it in all years.
- (pp. 9, Tables 3–5) Mean natural flow 968 Mm³/yr; annual pumped volume grows with pump size with diminishing returns (e.g. M30-5: 165 → 403 Mm³/yr for 10 → 50 m³/s; M20-5: 184 → 462 Mm³/yr).
- (p. 1, 19) Recommended preliminary combination: minimum flow 5 m³/s winter (1 Oct–30 Apr) and 20 m³/s rest of the year, pump ~30 m³/s, about **365 Mm³ pumped in an average year**.
- (p. 8) Earlier snowmelt since 2017 has raised winter/spring flows, possibly a climate-change effect.
- (pp. 16–19) Habitat quality in Driva is good at summer flows ~20 m³/s; holding winter flow at ≈ 5 m³/s via releases could stabilise winter conditions and improve salmon winter survival; pumping winter surplus removes small winter floods (likely positive).
- (p. 20) Further work: low-flow habitat mapping, detailed pumping/release calculations including technical and economic limits, fish studies, climate change, effects on Gjevilvatnet (ice, temperature, erosion).

## Strengths
- Concrete, current (2025) Norwegian pumped-storage/pump project with real long hydrological series; shows how environmental flow rules constrain pump sizing.

## Weaknesses / limitations
- No prices, no economics, no plant operation: pump size is set only by hydrology and environmental constraints.
- Habitat effects at low flow are judgmental extrapolations, not measurements (pp. 16–18).
- Not the source originally collected (the web page is); a consultancy memo, not peer reviewed.
- Small inconsistencies: winter period given as 1 Oct–31 May (p. 5) but 1 Oct–30 Apr (pp. 1, 7); gauge Grensehølen numbered 129.20.0 (p. 4) and 109.20.0 (p. 5).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.3: other Norwegian PHS/pump projects (besides Aurland 3) | Nedre Driva: pump Driva→Gjevilvatnet, new station (web page: 550–600 MW, ~660 m head) | pp. 3–4; web page |
| Lit review sizing: hydrology/environment-driven pump dimensioning | 10–50 m³/s sweep, 68 Mm³ fill target, ~30 m³/s recommended | pp. 5, 7–9, 19 |
| Discussion/limitations: environmental minimum flows constrain pumping | Minimum-flow scenarios, pumped volumes | pp. 7–9, Tables 2–5 |
| Background: reversible unit can also deliver environmental releases | Release through PHS or valve | pp. 4, 8, 19 |

## Useful quotes (with page numbers)
> "Det er ikke tatt hensyn til strømpriser og dermed når det blir lønnsomt å pumpe vannet." (p. 5)

## Follow-up references to check (backward snowballing)
- Foldvik, Sundt-Hansen, Hindar & Solem (2023), NINA Rapport 2352 (habitat mapping of Driva).
- Forseth & Harby (2013), Håndbok for miljødesign av regulerte laksevassdrag, NINA Temahefte 52.
- TrønderEnergi web page "Nedre Driva" (the originally collected source, `..._NETTSIDE.pdf` in the inbox): could be filed separately as grey literature if the thesis cites the project.

