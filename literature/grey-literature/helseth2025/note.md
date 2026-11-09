---
bibkey: helseth2025
title: "The ReSDDP Model – Principles and Algorithm"
authors: "Arild Helseth"
year: 2025
venue: "SINTEF Energy Research, Project Report 2025:00598 (Unrestricted), RES100 project, project no. 502003757; hdl.handle.net/11250/3210524"
peer_reviewed: false
methods: [sddp-time-series, benders-decomposition, two-stage-stochastic, uncertainty-modelling, hydro-production-function]
review_sections: [modelling-phs-plants, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Documentation of SINTEF's open-source Julia/JuMP long-term SDDP model ReSDDP: weekly stages with intra-week time steps, VAR(1) inflow, hydro subsystems constrained by precomputed feasibility cuts (storage, energy, ramping, reserve), and a residual-demand cost function built from two-stage 'cost cuts' over hourly dispatch with short-term VRES scenarios; test system shows finer intra-week resolution (1 h vs 3 h/8 h) slightly raises water values in critical storage zones."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/80_Helseth_2025_The_ReSDDP_Model_Principles_and_Algorithm.pdf
---

# The ReSDDP model: principles and algorithm (Helseth, SINTEF report 2025)

_Grey literature (SINTEF project report, not peer reviewed). 49-page PDF; page numbers below are the report's own "X of 48" footer numbers = PDF page − 1 (cover and blank page unnumbered). Code: gitlab.sintef.no/energy/res100/resddp; reads EMPS (v10) data (p. 5)._

## Research question / purpose
Document the principles of ReSDDP, an open-source long-term hydro scheduling model whose main goal is to compute expected marginal water values in large hydro systems within renewable-dominated power systems, representing both long-term (inflow) and short-term (VRES) uncertainty while keeping computation tractable through spatial decomposition (p. 5–6).

## Setting
- **System:** multi-area hydrothermal system (Nordic/Northern Europe in RES100; test system with 4 price areas, 3 with hydro, 8.47 TWh hydro, 8.73 TWh wind, 3.56 TWh solar, 17.58 TWh demand) (p. 38, Table 6.1). Hydro aggregated into subsystems (≥1 per price area) (p. 12).
- **Markets:** system least-cost dispatch (fundamental model), endogenous prices; reserve capacity requirement optional (symmetric, weekly constant) (p. 17).
- **Horizon and resolution:** multi-year; weekly decision stages, intra-week time steps (test: 156 weeks; T1/T3/T8 = 1-, 3-, 8-hour steps) (p. 7, 38–39).

## Method
- **Model type:** multistage stochastic LP (eq. 2.1, p. 7), relatively complete recourse via slacks (p. 8).
- **How uncertainty is represented:** weekly inflow via VAR(1) on normalised energy inflow per subsystem (eq. 2.6, p. 9), state variables = storage + previous inflow; short-term VRES uncertainty revealed *within* the stage via a second-stage dispatch problem solved for several VRES scenarios, not as SDDP states (wind/solar autocorrelation across weeks assumed muted; wind and inflow assumed uncorrelated) (p. 32–33).
- **Solution method:** SDDP with forward sampling and backward recursion; lower bound from first stage, upper bound from average simulated cost; convergence check if lower bound lies in [UB ± 1.96σ], or stabilisation of the lower bound (eqs. 2.3–2.5, p. 8). In practice visual inspection after a fixed number of iterations (p. 36).
- **Three cut types (p. 34–36):**
  1. *FCF (Benders) cuts* in the backward pass, accumulated.
  2. *Feasibility cuts* (Ch. 3): derived from the dual of a detailed hydro LP (3.17) that minimises slack on subsystem targets — end storage, weekly sum energy, ramping capability, reserve capacity — given disaggregated initial storage and inflow (fixed distribution factors by expected inflow share, eq. 3.16) (p. 12–20). Computed beforehand by enumeration; per subsystem; assumption that hydro operating cost is negligible (p. 12, 21). Ramping requirement: detailed system must ramp up and down twice per day (morning/evening) (p. 17).
  3. *Cost cuts* (Ch. 4): residual demand cost function (RDCF) for hydro — the cost of the rest of the hourly dispatch as a convex function of weekly hydro energy per subsystem (and optionally ramping and reserve), obtained as two-stage Benders cuts in the forward pass (eqs. 4.1–4.2, 4.7–4.8) (p. 22–26). Optimum where marginal RDCF equals the future water value — "operate along a constant water value" as in EMPS (eqs. 4.4–4.6, p. 24).
- **Pumped storage:** in the feasibility check, pumping energy is subtracted from the energy target (3.17e), allowing pumping for seasonal (higher end volume) and short-term (ramping) benefit (Sec. 3.4.3, p. 20). Not tested numerically (listed as further work, p. 21).
- **Production function:** concave piecewise-linear PQ curves per module (3.17j–k), conversion to energy by best efficiency to sea (p. 9, 18–19).
- **Key assumptions:** hydro can be optimised at coarse (weekly) resolution within the stage because large storages rarely hit bounds intra-week (intra-stage reservoir balances ignored in CostApprox) (p. 22, 31, 33); hydro decisions made before knowing VRES outcomes (p. 32–33); convex residual problem (p. 33).

## Data / case
- Ch. 4 toy examples: 1 reservoir, 20 thermal units, 8 stages, binary inflow tree (255 nodes); CostApprox converges to the extensive-form optimum 429.3125 in 11 iterations (p. 27–29). With 168 hourly steps per stage: CostApprox-1 57 s vs Standard 194 s (p. 31).
- Ch. 6: 4-area test system, 50 weather years (hourly wind/solar, weekly inflow), 40 forward scenarios, 5 VRES scenarios, 7 backward openings, max 50 iterations, CPLEX 20.1, i9-13900K, 21 threads (p. 38–39). Dataset public on SINTEF GitLab.

## Key findings
- (p. 39) Operating cost increases with finer intra-week time resolution; lower bound stabilises while upper bound fluctuates (sampling); 400 forward samples reduce UB variability but are too slow for a desktop (p. 40).
- (p. 40–41, Table 6.2) Total run times 128 min (T1), 61 min (T3), 56 min (T8); in ReSDDP the forward pass (cost cuts) dominates, unlike standard SDDP.
- (p. 41) Simulated prices hardly differ between T1 and T3 strategies.
- (p. 42–43, Fig. 6.6) Water values decrease with storage; near rationing price (400 €/MWh) at low storage in weeks 1 and 10; low near full reservoir (spill risk); in critical zones water values are higher with finer time resolution.
- (p. 44) Feasibility cuts (42, 40, 35 per subsystem; 3-h resolution, 5-point discretisation, no reserves) add ~30% run time and constrain operation of subsystems 2–3, raising prices.
- (p. 31) Ignoring intra-stage reservoir balances overestimates storage capability for small reservoirs (test with capacity 20: Standard costs more and spills).

## Strengths
- Transparent, open-source, with public test data; clear separation of hydro detail, residual market and water values.
- Explicit treatment of intra-week resolution effects on water values — directly relevant to the question of how hourly flexibility feeds long-term values.
- Includes a (conceptual) pumped-storage and reserve treatment.

## Weaknesses / limitations
- Grey literature; small test system; results described as indicative, "not ... a detailed analysis" (p. 38).
- Inflow-only stochastic process across stages; prices endogenous; no Markov-chain price states.
- Pumped storage and reserves only sketched; ramping requirement heuristic; convergence assessed visually.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: SDDP bounds and statistical stopping criterion (LB in UB ± 1.96σ) | Eqs. (2.3)–(2.5) | p. 8, Sec. 2.2.1 |
| Method: weekly stages with intra-week time steps; hazard-decision within week | Problem formulation | p. 7, Sec. 2.1 |
| Method: effect of intra-week resolution on water values | T1/T3/T8 comparison | p. 39–43, Ch. 6 |
| Method: water values from cuts (fix storage, binding cut slope) | Two extraction techniques | p. 42–43, Sec. 6.5 |
| Method: short-term uncertainty as second-stage within week, not SDDP state | Assumptions | p. 32–33, Sec. 4.5 |
| Model: PHS within aggregated SDDP (pumping subtracts from energy target) | Sec. 3.4.3 | p. 20 |
| Model: reserve capacity in weekly SDDP stage (symmetric, constant over week) | Eqs. (3.14)–(3.15) | p. 17 |
| Lit. review: SINTEF model landscape (EMPS, ProdRisk, ReSDDP) | Ch. 1, Sec. 2.6 | p. 5, 11 |
| Computation: forward vs backward time, cut management | Sec. 5.2, 6.3 | p. 35–36, 40–41 |

## Useful quotes (with page numbers)
> "water values in the most critical zones ... are higher with finer time resolution" (p. 43)

## Follow-up references to check (backward snowballing)
- Helseth & Mo (2025), "Considering short-term variability and uncertainty in long-term hydropower scheduling", TechRxiv 10.36227/techrxiv.173747756.68315820 (Northern Europe 2050 application).
- Helseth & Mo (2023), hydropower aggregation by spatial decomposition, IEEE TSTE.
- Júnior, Dias & Diniz (2024), two-stage Benders + SDDP with intra-stage cost functions, IEEE TSTE.
- Gjerden et al. (2015), large-scale SDDP case study for Norway, PowerTech.
- de Matos, Philpott & Finardi (2015), improving SDDP performance (cut selection).
- Homem-de-Mello et al. (2011), sampling strategies and stopping criteria for SDDP.

