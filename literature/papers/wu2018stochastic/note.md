---
bibkey: wu2018stochastic
bibkey_provisional: true
title: "Stochastic dynamic programming for hydropower reservoir operations with multiple local optima"
authors: "Xinyu Wu, Chuntian Cheng, Jay R. Lund, Wenjing Niu, Shumin Miao"
year: 2018
venue: "Journal of Hydrology, 564, 712-722"
peer_reviewed: true
methods: [sdp, hydro-production-function]
review_sections: [modelling-phs-plants]
relevance: background
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDP_i_vannkraft/Wu2018.pdf"
takeaway: "Head-dependent energy and a cascade-wide firm-power constraint make the SDP stage problem non-concave with a non-convex feasible region, so several local optima exist per state; a two-stage 'coarse traversing + local search' algorithm finds better decisions with less than half the run time of dense traversing (Lancang cascade, China, monthly, 51 storage points)."
---

# SDP with multiple local optima (Wu et al., 2018)

## Research question / purpose
Multiple local optima limit the accuracy of SDP for **non-concave** reservoir operation models. The paper analyses where non-concavity and non-convexity come from in cascaded hydropower energy maximisation, and proposes a two-stage solution algorithm for each state's sub-problem: coarse traversing of the discretised decision space to find promising regions, then local search in each region (abstract, p. 712).

## Setting
- **System:** five cascaded reservoirs on the middle–lower Lancang (Mekong) River, Yunnan, China: 14,820 MW installed; Xiaowan (4200 MW, 98.77 × 10⁸ m³) and Nuozhadu (5850 MW, 113.35 × 10⁸ m³) dominate storage; the other three held near upper bounds (Table 1, p. 717). Conventional hydro, no pumping.
- **Markets:** none. Objective is energy, with a system-wide firm power Pf = 6800 MW (p. 717).
- **Horizon and resolution:** periodic infinite-horizon SDP, monthly periods, yearly cycle (p. 715). Inflows 1953–2008 (p. 717).

## Method
- **Model type:** discretised SDP (Eq. 14, p. 714), storage-only state (51 points per reservoir, p. 717). Decision: releases; feasible region [0, q̄] after penalising soft constraints (p. 715).
- **How uncertainty is represented:** discretised joint distribution of local inflows; 5 inflow intervals per main reservoir (correlated); smaller reservoirs assumed "frequency synchronous" with upstream ones (p. 717). Inflows independent between months (storage is the only state) (p. 714).
- **Solution method:** two-stage algorithm: (1) traverse L × L decision grid; (2) single-point or multi-point local search with step halving (8 halvings) (pp. 716–718; Figs. 4–6).
- **Key modelling choices:**
  - **Head effects:** p = k·q·{[z(s_t) + z(s_{t+1})]/2 − z_d} (Eq. 4, p. 713). With polynomial level–storage curves of degree ≥ 2, energy is non-concave in turbine flow (p. 714).
  - Total power constraint (Eq. 10) can make the feasible region non-convex even with linear level–storage curves (Eqs. 12–13, Fig. 1, p. 714).
  - Soft constraints as penalties: quadratic penalty (spread shortages) vs concave penalty with exponent < 1 (fewer shortage periods, approximates a chance constraint) plus an extreme minimum power Pe = 3000 MW (Eqs. 15–20, pp. 714–715).
  - Averaging piecewise functions over inflow scenarios adds non-concavity (Fig. 2, p. 715).
  - 4-coefficient bilinear interpolation of the future value function (p. 716).

## Data / case
- 1953–2008 monthly inflows; minimum releases 470, 500, 504 m³/s for Xiaowan, Nuozhadu, Jinghong (p. 717).
- Java implementation, results after 5 SDP iterations (p. 719).

## Key findings
- (p. 715, Fig. 3) With a quadratic firm-power penalty there are two local optima separated by a gap; with a concave penalty there are three, and the global optimum is easier to miss. Missed optima show up as "protrusions and sunken points" in rule surfaces.
- (p. 716) Errors in a stage decision propagate through the future value function in the backward recursion.
- (p. 719, Table 2) Traversing with 101 × 101 points takes ~30× more time and still does not reach the objective of single-point search with 11 × 11 initial points. Multi-point search with 21 × 21 takes ~50% and ~12% of the time of 51 × 51 and 101 × 101 traversing: "at least 50%" time saving.
- (p. 719) Traversing density matters more for the concave-penalty model (11 → 21 points: +3.5% quadratic, +31.3% concave).
- (p. 719) SDP rules give 0.5–0.9% more energy than a simple equal-ratio rule.
- (pp. 719–720) Multi-point search gives similar objective values but more reasonable rule surfaces.
- (p. 720) Practical limit ≈ 3 large reservoirs; can be combined with aggregation or SSDP for larger systems.

## Strengths
- Clear diagnosis of the sources of non-concavity in hydro scheduling: head-dependent power, cascade power constraints, scenario averaging.
- Quantified accuracy–time trade-off of decision discretisation.

## Weaknesses / limitations
- No market prices; energy maximisation with firm power.
- Inflow independence between months; penalty coefficients not optimised (p. 720).
- Computing times from different computers, so only approximate (p. 719).
- Only quasi-global; no optimality guarantee.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Assumption: constant head / convex stage problem | Head-dependent power (Eq. 4) makes energy non-concave; non-convex feasible region | pp. 713–714, Eqs. (4), (12)–(13), Fig. 1 |
| Theory: why concavity matters for DP/SDDP | Multiple local optima per state; error propagation in recursion | pp. 715–716, Fig. 3 |
| Lit review: SDP for cascades | Monthly SDP of a 5-reservoir cascade with firm power | pp. 714–717 |
| Soft constraints / reliability via penalties | Quadratic vs concave penalties, chance-constraint approximation | pp. 714–715, Eqs. (15)–(20) |
| Lit review: dimensionality limits | ~3 large reservoirs practical for SDP | p. 720 |

## Useful quotes (with page numbers)
> "The multi-optima problem of reservoir operations are often caused by non-concave objective functions and non-convex feasible region" (p. 720)

## Follow-up references to check (backward snowballing)
- Rougé & Tilmant (2016), WRR 52(5) — SDDP with multiple near-optimal solutions.
- Tejada-Guibert, Johnson & Stedinger (1993, 1995), WRR — multireservoir SDP and value of hydrologic information.
- Faber & Stedinger (2001), J. Hydrol. 249 — SSDP with ESP forecasts.
- Zhao et al. (2012) — monotonic storage–release relationship for concave DP.

