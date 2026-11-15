---
bibkey: helseth2020nonconvex
bibkey_provisional: true    # not in references.bib yet (Zotero was not running 2026-11-15); key follows the Better BibTeX pattern
title: "Nonconvex Environmental Constraints in Hydropower Scheduling"
authors: "Arild Helseth, Birger Mo, Hans Olaf Hågenvik"
year: 2020
venue: "2020 International Conference on Probabilistic Methods Applied to Power Systems (PMAPS), pp. 1–6 (doi:10.1109/PMAPS47429.2020.9183590)"
peer_reviewed: true
methods: [sddp-time-series, benders-decomposition, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-15
takeaway: "SDDiP (binary expansion of reservoir volume; Benders, strengthened Benders and Lagrangian cuts) for a price-taking Norwegian three-reservoir watercourse with a reservoir-level-dependent maximum discharge; exact treatment raises expected profit by 0.16 % at average prices compared with the linear relaxation, and strengthened Benders cuts capture most of the gain at about five times the run time."
---

# Nonconvex environmental constraints with SDDiP (Helseth et al., 2020)

_Our copy is the **accepted version** from the Norwegian research archive (NVA), 6 pages, with the IEEE copyright notice; page numbers below are the pages of that file. Downloaded 2026-11-15 from hdl.handle.net/11250/2689703. Conference paper._

## Research question / purpose
How can a nonconvex, state-dependent environmental constraint (maximum discharge that depends on the reservoir level) be represented exactly in medium- and long-term hydropower scheduling, and how much does the exact treatment improve on the linear approximation that ordinary SDDP needs (abstract, p. 1; contributions, pp. 1–2)?

## Setting
- **System:** Norwegian watercourse with 3 reservoirs and plants, 202 MW (p. 4, Fig. 1). No pumping.
- **Markets:** energy only, price-taker, single price zone; price is a **deterministic** exogenous series in this work (p. 2).
- **Horizon and resolution:** 1 year, weekly decision stages; the paper states that the time discretisation is coarse (pp. 4–5).

## Method
- **Model type:** multistage stochastic program whose weekly problem is an LP (eq. 3) extended to a MIP by the environmental constraint (eq. 5) (pp. 2–3).
- **How uncertainty is represented:** inflow only; an inflow model fitted to one series of 80 historical years with normal errors; 50 inflow scenarios re-sampled in each forward iteration, 6 error terms per stage in the backward iteration (p. 5).
- **Solution method:** stochastic dual dynamic integer programming (Zou et al.): binary expansion of the reservoir volumes (eq. 6; a 200 Mm3 reservoir at 0.01 Mm3 precision needs 15 binaries), local copies of the state (eq. 7), and three cut families: Benders (LP relaxation, the same as ordinary SDDP on the relaxed problem), strengthened Benders and Lagrangian (pp. 3–4). Bounds: lower bound from the S forward scenarios with a confidence term, upper bound from the first-stage problem (algorithm, p. 4).
- **Key modelling choices and assumptions:** concave generation by discharge segments, said to suit Norwegian stations with small relative head variation (p. 3); end-of-horizon value by a set of cuts obtained by calibration, which could come from a long-term model (p. 4); maximum 30 iterations (p. 5).

## Model elements (weekly problem, eqs. 3–5, pp. 2–3)
- **Sets:** reservoirs H with upstream sets; discharge segments K_h; cuts C; binaries N_h for the volume expansion.
- **Parameters:** weekly price; inflow; efficiency per discharge segment; **time-dependent lower and upper bounds on reservoir volume, discharge and bypass** (3f–3h); threshold volume V^lim for the state-dependent constraint.
- **Variables:** energy sold, end volume, discharge (total and per segment), overflow (spill), bypass, future expected profit, binary for the threshold.
- **Constraints:** water balance with upstream discharge, overflow and bypass (3b); discharge as the sum of segments (3c); generation from segments (3d); cuts (3e); bounds (3f–3h); **state-dependent maximum discharge**: if the average weekly volume is below the threshold, discharge is held at its minimum (4–5).
- The paper names two further environmental constraint types that keep the problem convex: minimum flows and maximum ramping rates on releases (p. 1, p. 3).

## Data / case
- Environmental constraint on reservoir 2: no discharge in weeks 18–35 if the volume is below 140 Mm3 (p. 4).
- Three price scenarios from weekly average Nord Pool system prices: 2006 (high), the 2005–2018 average, 2015 (low) (p. 5).
- Final simulation on a fixed, separately sampled set of 1000 inflow scenarios (p. 5).
- Julia, JuMP, CPLEX 12.9 (p. 5).

## Key findings
- (p. 5, Table I) Expected profit in M€, Benders / strengthened Benders / Lagrangian: 65.73 / 65.91 / 65.96 (high price), 56.74 / 56.81 / 56.83 (average), 34.59 / 34.62 / 34.63 (low). At average prices the gain is 0.09 M€ or 0.16 %.
- (p. 5) The gain is largest at high summer prices, where it pays to keep water for summer production.
- (p. 5) Run time 2–3 hours with Benders cuts, about five times more with strengthened Benders cuts, more again with Lagrangian cuts.
- (p. 5, Fig. 2) With Lagrangian cuts the gap is still open after 30 iterations.
- (p. 6) The authors expect that stochastic price, a finer time resolution and a longer horizon would change the results.

## Strengths
- Compact weekly formulation with time-dependent bounds and one exactly modelled environmental constraint.
- Separate out-of-sample style evaluation (1000 fixed scenarios).

## Weaknesses / limitations
- Deterministic price, coarse time resolution, one-year horizon (stated by the authors, p. 6).
- Small case; no reserve markets, no pumping.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model: time-dependent bounds on volume, discharge and bypass as convex environmental constraints | eqs. (3f)–(3h) and text | pp. 2–3 |
| Model: which environmental constraints stay linear (minimum flow, ramping) and which do not (state-dependent discharge) | discussion | pp. 1, 3 |
| Method: SDDP is the state of the art for Nordic medium-term scheduling | statement | p. 1 |
| Method: final simulation on 1000 separately sampled scenarios | case description | p. 5 |
| Limitation: linear SDDP cannot represent state-dependent constraints exactly | comparison of cut types | pp. 4–5 |

## Useful quotes (with page numbers)
> "these constraints fit well into algorithms relying on a convex model formulation, such as SDDP" (p. 1, on minimum flows and maximum ramping rates)

## Follow-up references to check (backward snowballing)
- Guisández (2016), PhD thesis on long-term reservoir operation with minimum flows and maximum ramping rates (their [12]).
- Pérez-Díaz & Wilhelmi (2010), economic impact of environmental constraints on short-term operation (their [9]).
