---
bibkey: deane2013derivation
bibkey_provisional: true
title: "Derivation of Intertemporal Targets for Large Pumped Hydro Energy Storage With Stochastic Optimization"
authors: "J. P. Deane, E. J. McKeogh, B. P. Ó Gallachóir"
year: 2013
venue: "IEEE Transactions on Power Systems, 28(3), 2147–2155 (doi:10.1109/TPWRS.2012.2236111)"
peer_reviewed: true
methods: [two-stage-stochastic, deterministic-lp-milp, heuristics-simulation]
review_sections: [modelling-phs-plants, ldes-seasonal-storage, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Medium_term_pumpekraft/Deane2013.pdf"
takeaway: "TSO-perspective PLEXOS study (Ireland 2035, 500 MW/10 GWh closed-loop PHS): end-of-week storage targets from a one-year two-stage stochastic run over 7 historical wind years, then daily targets with wind-forecast scenarios and 6-day look-ahead; cuts system cost vs a weekly refill rule (+0.19 % vs +0.38 % above perfect foresight, ~3.3 M€/yr)."
---

# Intertemporal storage targets for large PHS under wind uncertainty (Deane et al., 2013)

Journal page = PDF page + 2146 (article runs pp. 2147–2155). Tables I–VI are images and did not extract; values below are from the running text.

## Research question / purpose
How should a system operator formulate **end-of-day and end-of-week reservoir targets for a large (long-duration) closed-loop pumped hydro energy storage (PHES)** plant in a wind-dominated power system, given wind forecast uncertainty (abstract, p. 2147)? The paper argues that both common operating modes fail for large PHES: a **fixed cycle** (refill each day/week) ignores wind at the end of the cycle and under-uses storage; a **free cycle** based on short (1–2 day) optimisations lets a large reservoir empty in the first steps because it never reaches its bounds within the horizon (pp. 2147–2148). Large storages therefore need long optimisation horizons (week, month, year), which raises the question of how to handle uncertainty over those horizons (p. 2148).

## Setting
- **System:** test system for the Irish All-Island system in 2035: ~42 TWh demand, 7.4 GW peak; one **500 MW PHES with 10 GWh storage** (≈ 20 h at full power, our calculation), modelled as 2 × 250 MW units with 40 MW minimum stable generation, no simultaneous pump/generate; instantaneous wind penetration capped at 70 %; interconnector to GB (p. 2148).
- **Markets:** none; **cost-minimising TSO perspective**, explicitly not a market participant view (p. 2147). Spinning and replacement reserve modelled: each PHES unit can provide up to 100 MW spinning reserve when generating and the full 250 MW when pumping (p. 2148).
- **Horizon and resolution:** one-year horizon in all runs; step 1 at 6-hour intervals, step 2 at 2-hour intervals (daily optimisations with 6-day look-ahead), final evaluation hourly over 365 daily runs (pp. 2149–2150, Table II).

## Method
- **Model type:** unit-commitment and economic dispatch MILP in **PLEXOS** (fuel, start, no-load costs; min up/down; ramps; reserves; water balance) (p. 2148, Appendix pp. 2152–2154). Solved with Xpress MIP at 0.2 % relative gap; longest stochastic run 27 h (p. 2150).
- **How uncertainty is represented:** wind is the only stochastic variable (demand deterministic, acknowledged limitation, p. 2148). **Two-stage stochastic programming** with non-anticipativity imposed **only on PHES storage end volumes** (soft constraint with high penalty), so all scenarios share the same end-of-day/week levels while intraday operation can adapt (p. 2149; eq. 13).
- **Two-step methodology (p. 2149, Fig. 1):**
  1. *Weekly targets:* one-year optimisation over **7 equiprobable scenarios = historical wind years 2001–2007** (hourly profiles), 6-h intervals; yields one unique storage trajectory, from which end-of-week levels are extracted (Fig. 2, p. 2150). An annual look-ahead is needed because "without this annual look ahead, the system would empty prematurely for large reservoirs" (pp. 2149–2150).
  2. *Daily targets:* rolling daily optimisations with 6-day look-ahead and 3 synthetic 7-day wind forecast scenarios (ARMA forecast errors tuned to EirGrid forecasts), forced to hit the weekly targets; only the first day is kept (pp. 2150, Figs. 3–4).
- **Benchmark:** **weekly Refill Method**: reservoir returned to full at the end of each week (common practice for weekly balancing), daily targets as the average of deterministic runs per forecast (p. 2150).
- **Evaluation:** both target sets enforced in a deterministic hourly one-year simulation with realised 2008 wind, compared with a perfect-foresight run (p. 2150).

## Data / case
- Irish 2008 regional wind capacity factors scaled to 2035 capacity; historical wind 2001–2007; generation portfolio from Pöyry (2010) (p. 2148).
- Total annual system cost ~2 billion € (p. 2151).

## Key findings
- (p. 2151) Stochastic targets reduce total system cost relative to Refill; savings about **3.3 M€ per year** out of ~2 bn€, small in % but material.
- (p. 2151) Reason: better coordination of storage and interconnector imports; the PHES has a higher capacity factor and wind curtailment falls compared with Refill.
- (p. 2151) With fixed (day-ahead scheduled) interconnector flows, savings are larger; the stochastic method uses more CCGT and less OCGT.
- (p. 2151–2152, Figs. 5–6) Refill forces the reservoir to recycle each week, preventing pumping in early-week high wind and generation later; a "poor operational strategy" in wind-dominated systems, suitable for thermal systems.
- (p. 2152, Table VI) Sensitivity over all 7 wind years used to build forecasts: stochastic method on average **0.19 %** above perfect foresight cost vs **0.38 %** for Refill (flexible interconnector).

## Strengths
- Clear statement of why large/long-duration storage needs long horizons and end-of-horizon guidance, and why short free-cycle optimisations fail.
- Simple, implementable target-derivation approach in a commercial tool with full UC detail.
- Honest about limitations (deterministic demand, ARMA forecast errors may exaggerate variability).

## Weaknesses / limitations
- System-cost (TSO) view, not profit; no market prices or reserve markets as revenue.
- Storage targets rather than water values: targets are fixed volumes, not marginal values, so the policy cannot adapt to a different realised state beyond the soft penalty.
- Only 7 wind scenarios; demand, fuel prices and outages deterministic; closed loop with no inflow.
- Key numerical tables are images in this copy.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review (modelling PHS): fixed vs free cycle operation; large storage needs long horizons | Argument against both for large PHES | pp. 2147–2148 (Sec. II) |
| Lit review (research gap): short horizons empty large reservoirs prematurely | Annual look-ahead needed | pp. 2148–2150 |
| Method/benchmark: weekly refill heuristic | Refill Method definition and its cost penalty | p. 2150; p. 2151–2152; Table VI |
| Method: non-anticipativity only on storage end volumes (two-stage) | Soft NAC with penalty | p. 2149; Appendix eq. 13 |
| Method: rolling horizon with look-ahead | Daily optimisation with 6-day look-ahead, keep first day | p. 2149, p. 2150 (Fig. 4) |
| Background (LDES): large PHES (500 MW, 10 GWh) in high-wind systems | Test system | p. 2148 |
| Background (PHS technology): pumping-mode reserve contribution | Each unit up to 250 MW spinning reserve when pumping | p. 2148 |

## Useful quotes (with page numbers)
> "Without this annual look ahead, the system would empty prematurely for large reservoirs." (pp. 2149–2150)

## Follow-up references to check (backward snowballing)
- [2] Deane, Ó Gallachóir, McKeogh (2010) Techno-economic review of existing and new PHES plant, RSER 14.
- [19] Baslis & Bakirtzis (2011) mid-term stochastic scheduling of a price-maker hydro producer with pumped storage (in inbox as Baslis2011).
- [20] Tuohy & O'Malley (2009) impact of pumped storage on power systems with increasing wind penetration (free-cycle water values).
- [29] Meibom et al. (2011) stochastic optimisation model for high wind penetration in Ireland (WILMAR).

