---
bibkey: hummelen2025exploring
bibkey_provisional: true
title: "Exploring European hydrogen demand variations under tactical uncertainty with seasonal hydrogen storage"
authors: "Sebastian Emil Hummelen, Erlend Hordvei, Marianne Petersen, Stian Backe, Hongyu Zhang, Pedro Crespo del Granado"
year: 2025
venue: "Energy Strategy Reviews, 61, 101818"
peer_reviewed: true
methods: [multistage-scenario-trees, uncertainty-modelling]
review_sections: [ldes-seasonal-storage]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "NTNU EMPIRE capacity-expansion model extended so storage levels carry across representative seasonal periods with a multi-stage tree (tactical uncertainty): seasonal hydrogen storage raises storage investment 5-14x, cuts total European system cost 1-5 % (abstract: up to 6 %) and displaces up to 600 TWh/yr of dispatchable generation after 2040; pumped hydro excluded as seasonal option due to limited potential."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/98_Hummelen_2025_Exploring_European_hydrogen_demand_variations_under_tactical_uncertainty_with_seasonal_hyd.pdf"
---

# Seasonal hydrogen storage with tactical uncertainty in EMPIRE (Hummelen et al., 2025)

## Research question / purpose
(1) How can seasonal storage be modelled in a stochastic multi-horizon capacity-expansion model so that "tactical" (medium-term, between-season) uncertainty is captured? (2) What does seasonal hydrogen storage do to European power and hydrogen investments under three hydrogen demand profiles (winter peak, constant, summer peak) (pp. 1–2)? Uncertainty levels follow a strategic/tactical/operational split (p. 1).

## Setting
- **System:** European power and hydrogen system, 20 nodes (countries/regions), EMPIRE model (pp. 3, 6).
- **Markets:** system cost minimisation, no market products; green-hydrogen rules (additionality, temporal/spatial correlation) enforced (p. 3).
- **Horizon and resolution:** investment periods of 3 years, 8 periods to 2048, rolling horizon of 3 periods; within each period 12 representative 336-hour operational windows (monthly partitions, 4032 hours), hourly (p. 6).

## Method
- **Model type:** multi-horizon stochastic LP; investments per period, hourly operations in scenarios (p. 3–4).
- **How uncertainty is represented:** scenarios by random sampling of historical time windows (demand, VRES availability) with a common starting hour to keep cross-correlation; equiprobable (p. 4). New: operations restructured as a **multi-stage tree** inside each investment period, with three stages and four equiprobable branches, branching before May and before September (p. 6, Fig. 1).
- **Solution method:** rolling-horizon decomposition over investment periods; subproblems ~10 h each, total ~64 h, 180 GB RAM (p. 6).
- **Key modelling choices:** storage level passed from the last hour of a parent node to the first hour of the child node; the net change over a representative period is scaled by a **seasonal scale factor** (365/12 days per month ÷ 14 days per window = 2.17) so the sampled period stands for its whole season; cyclic link from the last leaf back to the first node (pp. 4–5, eqs. 1–4). Without seasonal storage each period starts and ends at 50 % storage (p. 6). Batteries and pumped hydro are in EMPIRE but not considered as seasonal storage: batteries due to CAPEX and losses, "pumped hydro is limited by its comparatively small technical potential" (p. 6).

## Data / case
Costs aligned with Shirizadeh et al.; hydrogen storage potential per region (salt caverns, aquifers, depleted fields); discount rate 5 % (p. 6, Appendix B).

## Key findings
- (p. 8, Sec. 5.2) Seasonal storage lowers total system cost by 1–5 % (EUR 19–115 billion) across demand profiles, most when demand peaks in winter; generator investment falls by EUR 22–130 billion while storage investment rises by EUR 13–69 billion.
- (p. 8) Pipeline capacity reduced, e.g. 12 % Spain–France and 15 % total European pipeline capacity by 2045 in the winter-peak case.
- (p. 8) After 2042, seasonal storage replaces over 600 TWh/yr of dispatchable generation (winter-peak case), mainly with solar.
- (p. 10) Seasonal storage stabilises seasonal power prices; median prices fluctuate less over the year.
- (p. 11) Storage investment increases by factors of 5–14 with inter-seasonal transfer.
- (p. 11) Limitations: exogenous, stylised hydrogen demand; fixed technology trajectories; sampled historical weather; rolling horizon can be myopic.

## Strengths
- Clear discussion of the trade-off between seasonal coupling and keeping uncertainty: full-year scenarios give perfect foresight, independent representative periods block inter-seasonal storage (p. 2).
- Practical device (scale factor) for chaining short representative periods into seasonal storage dynamics.

## Weaknesses / limitations
- System planner perspective; no prices or market revenues for a storage owner.
- Only four branches per stage; scenario tree, not SDDP, and the scale factor assumes non-sampled hours behave like sampled ones (p. 5).
- Dismisses pumped hydro as seasonal storage on technical potential with one citation.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background: LDES and seasonal storage value | Seasonal storage cuts European system cost 1–5 %, replaces up to 600 TWh/yr dispatchable generation, stabilises seasonal prices | p. 8 (Sec. 5.2, 5.6), p. 10, p. 11 |
| Background: competing seasonal technologies | Hydrogen chosen as seasonal option; batteries excluded (CAPEX, losses) and PHS limited by technical potential | p. 6 (Sec. 5 intro) |
| Method discussion: perfect foresight vs. uncertainty when chaining periods with storage | Trade-off statement; multi-stage tree with seasonal branching; scale factor 2.17 | p. 2 (Sec. 2.2), pp. 4–5 (Sec. 3.6–3.7) |
| Literature review: related NTNU work | Links to Abgottspon & Andersson 2014 (stochastic tree for PHS medium-term) as the hydropower analogue | p. 2, Table 1 |

## Useful quotes (with page numbers)
> "pumped hydro is limited by its comparatively small technical potential" (p. 6)

## Follow-up references to check (backward snowballing)
- [16] Abgottspon & Andersson 2014 PSCC, medium-term PHS optimisation with stochastic intrastage subproblems — already in papers/ as `abgottspon2014`.
- [12] Kaut: linking seasonal storage across representative periods in multi-horizon models (HyOpt).
- [55] Source for limited technical potential of pumped hydro in Europe (unverified which study).
- [11] Strømholm & Rolfsen: multi-horizon MILP for hydrogen production and storage.

