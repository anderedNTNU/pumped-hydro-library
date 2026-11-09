---
bibkey: hunt2020global
bibkey_provisional: true
title: "Global resource potential of seasonal pumped hydropower storage for energy and water storage"
authors: "Hunt, Julian D.; Byers, Edward; Wada, Yoshihide; Parkinson, Simon; Gernaat, David E. H. J.; Langan, Simon; van Vuuren, Detlef P.; Riahi, Keywan"
year: 2020
venue: "Nature Communications 11, 947 (doi:10.1038/s41467-020-14555-y)"
peer_reviewed: true
methods: []
review_sections: [ldes-seasonal-storage, phs-technology, reservoir-sizing-capacity]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/03_Konfigurasjoner_og_potensial/Hunt2020Global.pdf
takeaway: "First global GIS assessment of seasonal pumped hydro storage (SPHS: off-river high-head reservoir beside a major river, 1 GW each): energy-storage capex 1.8–50 US$/MWh of storage capacity, 370–600 US$/kW, water 0.007–0.2 US$/m³; 17.3 PWh below 50 US$/MWh (≈ 79% of 2017 world electricity use); potential concentrated in mountain regions."
---

# Global potential of seasonal pumped hydro storage (Hunt et al., 2020)

_Article number 947; page numbers are the article's own pages 1–8 (= PDF pages). Supplementary Information (cost equations, Tables S1–S7) is not in this PDF._

## Research question / purpose
Give the first globally consistent estimate of the technical potential and cost of **seasonal pumped hydropower storage (SPHS)** for both energy and freshwater storage, using a new high-resolution plant-siting model (pp. 1–2). Motivation: growing seasonal mismatch between supply and demand with more wind, solar and hydro; most storage technologies "only fulfil short-term cycles (daily or shorter)" (p. 2).

## Setting
- **System:** global (56° S–60° N, limited by SRTM topography coverage, p. 5). **Note: this excludes most of Norway north of 60° N.** Concept: a high-head-variation storage reservoir built **parallel to a major river** (off-river), filled by pumping from the river in periods of low demand or high water availability and released when generation or water is needed (p. 2). Can increase output of downstream dams in cascade (p. 2).
- **Markets:** none; engineering cost and potential assessment.
- **Horizon and resolution:** static; grid 15 arc-seconds (≈ 450 m); results reported as the cheapest project per 1° cell (p. 2, p. 5). Hydrology monthly/annual from PCR-GLOBWB (6-arc-minute) (Fig. 3, p. 6).

## Method
- **Model type:** GIS siting and costing algorithm ("SPHS world potential model"), nine stages (Supplementary Table 4; Fig. 3, p. 6): find a river with Strahler order ≥ 7 within tunnel distance (tunnel length increased in 3 km steps up to 30 km per Fig. 3; the text says "within 130 km", p. 5, inconsistent); try dams of 50/100/150/200/250 m height along four axes, max dam length 7.2 km; build reservoir and level–area–volume curves; cap reservoir at 1,625 km² flooded area (Fig. 3); compare with water availability; estimate costs.
- **Water availability (pp. 5, Eqs. 1–3):** seasonal variation index SV and inter-annual variation index IV from monthly and annual flows; water available Q_A = Q·(SV·0.1 + (1+IV)·0.1) (Eq. 3, as extracted); reservoir volume capped at **11% of annual river flow**; average water available for storage = 7.7% of annual flow (p. 5). Reservoirs are operated to **regulate** (flatten) river flow; a river with constant flow gives zero storage need.
- **Costs (pp. 2, 5, 7):** components dam, tunnel, powerhouse excavation, pump-turbine, electro-technical equipment, land (land value 41,000 US$/ha, ≈ 5% of cost). Cost equations from **SWECO/NVE (2012) "Cost base for hydropower plants"** (ref. 34) and tunnel design from an NTNU MSc thesis on pumped storage at Otra (ref. 33). Every project has **fixed 1 GW generation/pumping capacity** (p. 2, p. 7).
- **Cost metrics (Eqs. 4–5, p. 7):** water storage cost = project cost / water storage (US$/m³); long-term energy storage cost = project cost / energy storage capacity (US$/MWh), with and without cascade gains downstream; short-term cost = generation-capacity cost / 1 GW (US$/kW, excluding dam and land). **These are capital costs per unit of storage capacity, not per MWh delivered.**
- **How uncertainty is represented:** none (deterministic; hydrology summarised by indices).

## Data / case
SRTM30 topography; GRIN river network (Strahler order); PCR-GLOBWB hydrology (pp. 5–6). Illustrative site in **Tibet** (Fig. 1b–d, p. 3): 18 km tunnel; energy storage cost 11.7 US$/MWh at 50 m dam (tunnel 45%, land 8%, dam 7% of cost) and lowest at 150 m dam (tunnel 30%, dam 36%, land 6%); higher dams raise cost because the reservoir exceeds the water that can be extracted (p. 2).

## Key findings
- (p. 2) > 5.1 million potential projects; best per 1° cell: 1,457 water-storage projects below 0.2 US$/m³ and 1,092 energy-storage projects below 50 US$/MWh.
- (pp. 1–2) **Costs:** water 0.007–0.2 US$/m³; energy storage 4.6–50 US$/MWh without cascade, **1.8–50 US$/MWh with cascade**; power capacity **370–600 US$/kW** (excluding dam and land; stepwise with tunnel length from 3 km in 3 km steps).
- (pp. 1–2) **Potential:** 17,325 TWh (17.3 PWh) of energy storage below 50 US$/MWh including cascade, ≈ **79% of world electricity consumption in 2017**.
- (p. 2) Comparison: natural-gas storage at 1 US$/mcf and 50% efficiency ≈ 6.8 US$/MWh, i.e. more expensive than SPHS in mountain regions with cascade (gas plant cost excluded).
- (p. 2) Background facts: global PHS ≈ 165 GW (≈ 25 GW mixed with conventional reservoir hydro); PHS often seen as daily/weekly up to monthly storage but can operate over **annual and pluri-annual cycles**.
- (pp. 2–3) Mean reservoir level variation 151.7 m (energy projects) / 141 m (water); land use 1.2–20 km²/TWh vs ≈ 150 km²/TWh for Brazilian conventional hydro storage.
- (p. 3) Potential concentrated in the lower Himalayas, Andes, **Alps**, Rocky Mountains, northern Middle East, Ethiopian and Brazilian highlands, Central America, East Asia, Papua New Guinea and Russian ranges.
- (p. 3) Example of service stacking: one project provides water storage 0.1 US$/m³, long-term energy storage 30 US$/MWh and short-term storage 600 US$/kW; complementary services cut cost.
- (pp. 4–5) Energy and water storage needs are **complementary in high-latitude countries** (summer melt, low summer demand, high winter demand) and in tropical hydro regions; not complementary in tropical regions without hydro where summer is the peak (air conditioning) — there SPHS should not be considered.
- (p. 5) Only technical potential; population, land use, biodiversity and transmission not included.

## Strengths
- Global, spatially explicit, uses Norwegian (NVE/SWECO) cost base.
- Separates energy-capacity cost (US$/MWh) from power cost (US$/kW), matching the LDES design-space framing.
- Clear statement that PHS can run annual and multi-year cycles; links storage to water management.

## Weaknesses / limitations
- Technical potential only; no operation, prices or revenue; "energy storage cost" is capex per MWh of capacity and must not be compared with LCOS or arbitrage profit.
- Fixed 1 GW per project; one project per 1° cell; latitude cap 60° N leaves out much of Norway.
- Supplementary Information needed for formulas and cost assumptions; Eq. 3 garbled in extraction.
- Inconsistencies (my checks): tunnel search distance "within 130 km" (p. 5) vs up to 30 km (Fig. 3 and p. 5 stage list); abstract water cost unit printed as "US$ m-1" in the extraction, elsewhere US$/m³.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.1: definition of seasonal PHS | Off-river high-head reservoir beside a major river, pumped in low-demand/high-flow periods | p. 2 |
| Background 2.1: PHS can store over annual/multi-year cycles | Statement plus ref. 14 | p. 2 |
| Background 2.1: why seasonal storage at high latitudes | Complementarity of water and energy storage needs (summer melt, winter demand) | pp. 4–5 |
| Background 2.2: PHS global capacity | ≈ 165 GW, 25 GW mixed plants | p. 2 |
| Background 2.1/2.2: SPHS cost per kWh and per kW | 1.8–50 US$/MWh, 370–600 US$/kW, 0.007–0.2 US$/m³ | pp. 1–2, Fig. 2 |
| Background 2.1: global potential | 17.3 PWh < 50 US$/MWh, ≈ 79% of 2017 world electricity | pp. 1–2 |
| Lit. review 5.5: energy vs power capacity costs; dam height trade-off | Cost curve vs dam height (Tibet example); tunnel/dam shares | p. 2, Fig. 1 p. 3 |
| Discussion: land use advantage of high-head variation | 1.2–20 km²/TWh vs 150 km²/TWh | p. 3 |

## Useful quotes (with page numbers)
> "the technology can also operate over annual and pluri-annual cycles" (p. 2)

## Follow-up references to check (backward snowballing)
- [14] Hunt et al. (2014), combining pumped storage in a yearly storage cycle with dams in cascade in Brazil, Energy 78.
- [15] Hunt et al. (2018), SPHS vs conventional reservoir dams, water–energy–land nexus, Energy Convers. Manage. 166.
- [22] Lu, Stocks, Blakers & Anderson (2018), GIS algorithms for pumped hydro sites, Appl. Energy 222 (closed-loop global atlas; relates to `blakers2021`).
- [25] Gimeno-Gutiérrez & Lacal-Arántegui (2015), European PHS potential from two existing reservoirs, Renew. Energy 75 — **Europe/Norway relevant**.
- [34] SWECO Norge / NVE (2012), Cost base for hydropower plants — Norwegian cost data (grey literature).
- [33] Rognlien (2012), Pumped storage development in Øvre Otra, NTNU MSc thesis.

