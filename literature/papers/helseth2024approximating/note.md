---
bibkey: helseth2024approximating
bibkey_provisional: false
title: "Approximating hydropower systems by feasibility spaces in stochastic dual dynamic programming"
authors: "Arild Helseth"
year: 2024
venue: "Electric Power Systems Research 234, 110615 (PSCC 2024 special issue)"
peer_reviewed: true
methods: [sddp-time-series, benders-decomposition, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "SINTEF: aggregated (one equivalent reservoir per price area) SDDP for the Norwegian system, constrained by low-dimensional feasibility cuts (end storage, weekly sum energy, ramping, reserve) precomputed from the detailed hydro system; on 30 historical years the feasibility-cut strategy cut total cost 7.2% on average vs. plain aggregation, at 2.7x computation time."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/100_Helseth_2024_Approximating_hydropower_systems_by_feasibility_spaces_in_stochastic_dual_dynamic_programm.pdf
---

# Feasibility spaces for aggregated hydropower in SDDP (Helseth, 2024)

_Open access (CC BY). Article number 110615; PDF pages 1–7 carry no journal page numbers, so "p. X" below = PDF/article page X. Not in `references.bib` yet: key is provisional and must be added to Zotero._

## Research question / purpose
How to represent a large, detailed hydropower system inside a long-term SDDP scheduling model without exploding the state space. Aggregated "equivalent reservoir" (ER) models are fast but ignore local constraints (reservoirs, flows, generation limits) and can lead to sub-optimal use of hydro (p. 1). The paper extends Helseth & Mo (2023, IEEE TSTE) by (i) drastically reducing the dimensionality of the feasibility cuts and (ii) demonstrating the method on the Norwegian power system (p. 2).

## Setting
- **System:** Norwegian power system (9 price areas, ~2030 expansions included, isolated from Europe); >35 GW hydro, 92 TWh storage, 152 TWh/yr average inflow; 9.5 GW thermal, 7.0 GW wind (p. 4, Table 1, Fig. 3). Conventional hydro cascades, aggregated per area; no pumped storage modelled specifically.
- **Markets:** system cost minimisation (not a price-taker). A system reserve capacity requirement is included, covered by hydro only, constant over the week, symmetric up/down, freely exchangeable between areas (p. 3).
- **Horizon and resolution:** 3 years, weekly stages, 42 four-hour time steps per week (p. 4).

## Method
- **Model type:** multistage stochastic LP; stage problem (3) is a multi-area LP with energy-storage balances per area, area energy balances with exchange, thermal generation, price-elastic/inelastic demand, curtailment, reserve requirement, ramping limits, Benders cuts and feasibility cuts (p. 2–3).
- **How uncertainty is represented:** inflow only; first-order vector autoregressive model for normalised weekly energy inflow per area, residuals fitted to a three-parameter lognormal (Maceira & Bezerra 1997) (p. 2–3). Wind and demand could be added to the AR model "in principle" (p. 2). Normalised inflow of previous stage is a state variable alongside storage.
- **Solution method:** SDDP (Julia/JuMP, CPLEX 20.1, 7 parallel workers); 70 forward scenarios, 7 sampled white-noise terms per stage in the backward pass, max 80 iterations (p. 4–5).
- **Feasibility spaces:** spatial decomposition. Master = aggregated area problem; subproblem (4) = detailed LP of the area's hydro system that minimises slack on "requirements" from the master (p. 3). Three steps: (1) disaggregate initial energy storage and inflow to physical reservoirs by a fixed, time-dependent mapping (state-dependent mapping would break convexity); (2) impose requirements: end storage, weekly *sum* energy production, maximum ramping rate, reserve capacity; (3) if infeasible, the duals of (4c) give a feasibility cut (3m) (p. 3). Using the weekly sum energy rather than per-time-step energy (as in Helseth & Mo 2023) makes cut dimension independent of the number of time steps (p. 3–4). Ramping requirement tested once per day (p. 4).
- **Cut generation:** computed before SDDP: each stage/state variable discretised into 5 values between extremes, (4) solved for each combination; redundant cuts removed; 50–130 feasibility cuts per area and stage (p. 4–5).
- **Key assumptions:** hydro operating cost neglected in subproblems; no grid bottlenecks within an area; end-of-horizon water valued against a common reference value (p. 3, 5).

## Data / case
126 inflow series, 30 years (1961–1990), weekly (p. 4). Detailed simulation uses the 30 historical years arranged in 30 overlapping 3-year sequences (1961–63, 1962–64, ...) (p. 5). Data not shareable (p. 6).

## Key findings
- (p. 5) Aggregate simulation (2000 sampled scenarios): Feas case has higher cost and significantly higher simulated prices than Base, because hydro is more constrained; price spikes around weeks 20 and 70 (start of snow melt).
- (p. 5, Figs. 5–6) Feasibility cuts reduce use of maximum generation capacity and limit ramping in areas 6 and 7.
- (p. 5) Detailed simulation on historical data: total cost lower in 21 of 30 sequences and 7.2% lower on average with the Feas strategy; prices more stable, lower spikes (weeks 18 and 70).
- (p. 5) Individual reservoirs (e.g. Svartisen, area 8) generally handled more realistically, but "many examples" of poor reservoir handling remain in Feas.
- (p. 5–6) Computation: 10.7 h (Base) vs 27.6 h (Feas), factor 2.7; earlier higher-dimensional cuts in Helseth & Mo (2023) gave factor 8.7. Stage LP with feasibility cuts ≈ 10k variables / 4k constraints (25% feasibility cuts) vs 350k / 158k with detailed hydro.
- (p. 6) Finer discretisation of cut generation did not improve quality much; coarser discretisation compromised quality.

## Strengths
- Clear, compact formulation; quantifies the cost of aggregation via out-of-sample detailed simulation on historical inflows.
- Shows how ramping and reserve capacity can be passed through a low-dimensional interface.
- Honest about remaining poor reservoir handling.

## Weaknesses / limitations
- Inflow-only uncertainty; prices are endogenous (system cost minimisation), not exogenous price-taker prices.
- Fixed disaggregation mapping does not capture true variability in the detailed system (p. 5).
- Norway isolated from Europe; reserves very simplified (symmetric, weekly constant, no bottlenecks).
- No cut management; single-author conference-extended paper.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review: aggregation vs. detail in SDDP hydro models | ER models fast but miss local constraints; feasibility cuts as remedy | p. 1–2, Sec. 1 |
| Theory/method: weekly stages with intra-week time steps in SDDP | 42 × 4 h steps per week, 3-year horizon, 156 stages | p. 4, Sec. 4.1 |
| Method: reserve capacity in an SDDP stage problem | Reserve requirement (3g)–(3i) with symmetric, weekly-constant reserve | p. 3, Sec. 2.2 |
| Method: inflow VAR(1) with lognormal residuals as state | Eq. (3c)–(3d) | p. 2–3 |
| Evaluation design: out-of-sample simulation on historical sequences | 30 overlapping 3-year sequences, end-water valued at common reference | p. 5, Sec. 4.3 |
| Computation-time figures for SDDP on large hydro systems | 10.7 h vs 27.6 h; problem sizes | p. 5–6, Sec. 4.4 |
| Background: Norwegian hydro system size | >35 GW, 92 TWh storage, 152 TWh/yr inflow | p. 4 |

## Useful quotes (with page numbers)
> "local constraints on reservoirs, flows and generations seen in the detailed system are difficult to account for in aggregated models" (p. 1)

## Follow-up references to check (backward snowballing)
- Helseth & Mo (2023), "Hydropower aggregation by spatial decomposition – An SDDP approach", IEEE TSTE 14(1) 381–392 (the base method).
- Ploussard et al. (2022), hydro-economics trade-off surfaces, Applied Energy 324.
- Rosemberg et al. (2021), cost of network simplifications, IEEE TSTE 13(1).
- Maceira & Bezerra (1997), stochastic streamflow model.
- Helseth et al. (2023) toolchains paper (filed as `helseth2023hydropower`).

