---
bibkey: abgottspon2016multihorizon
bibkey_provisional: false
title: "Multi-horizon modeling in hydro power planning"
authors: "Hubert Abgottspon, Göran Andersson"
year: 2016
venue: "Energy Procedia 87, 2-10 (5th International Workshop on Hydro Scheduling in Competitive Electricity Markets)"
peer_reviewed: true
methods: [sddp-time-series, deterministic-lp-milp, multistage-scenario-trees]
review_sections: [modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Multi-horizon model for a 10-reservoir Swiss PHS (KWO): daily interstage SDDP with only the 4 storage reservoirs as states + hourly intrastage MILP for the 6 balancing reservoirs; vs hourly, daily and daily-intrastage alternatives it closes the gap to 0.5 % and has the smallest bound-vs-simulation error (2-3 %), but the case is deterministic (DDP) and in-sample."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/01_Produsentmodeller_og_tidsskalaer/Abgottspon2016.pdf
---

# Multi-horizon modelling in hydro power planning (Abgottspon & Andersson, 2016)

DOI: 10.1016/j.egypro.2015.12.351 (ETH Research Collection copy with cover sheet, ethz-b-000117060). Open access CC BY-NC-ND.
**Page mapping:** PDF p. 1 is the ETH cover sheet; journal p. 2 = PDF p. 2, ..., journal p. 10 = PDF p. 10 (so journal page = PDF page).
**Family:** same author and framework as `abgottspon2014` (PSCC 2014), `abgottspon2013stochastic` and the PhD thesis `abgottspon2015hydro` (Ch. 3.2 and 3.5 there contain an extended version of this comparison). Treat as one research line, not independent replications.

## Research question / purpose
Propose "multi-horizon modelling" for medium-term hydro planning (MTHP) of plants with two reservoir types: large **storage** reservoirs (seasonal) and very small **balancing** reservoirs (hours), and evaluate it against three traditional modelling alternatives with respect to computational complexity and modelling accuracy (p. 2-3). Claimed original idea: exploiting the physical difference between reservoir types in the decomposition (p. 3).

## Setting
- **System:** Kraftwerke Oberhasli AG (KWO), Switzerland: 10 reservoirs, of which 4 storage reservoirs (15-94 Mm³, typically emptied once a year) and 6 balancing reservoirs (0.02-0.08 Mm³, emptied within hours); aggregated 12 turbines (1.125 GW) and 8 pumps (424 MW) (p. 5, Fig. 2 p. 6).
- **Markets:** hourly day-ahead spot market; market position m = generation − pumping, can be bounded as crude risk control (p. 5). No reserves in this paper.
- **Horizon and resolution:** 1 year; daily interstage stages; hourly intrastage steps τ = 1..24 (p. 3-5, p. 8).

## Method
- **Model type (eq. 1, p. 4-5):** recursive DP: Q_t(v_stor,t−1) = (1/N_t) Σ_j max { Σ_τ E[c(τ)m(τ)] + Q_{t+1}(v_stor,t^j) }. Interstage problem: daily stages, **only storage reservoirs as states**, output = water values/profit-to-go. Intrastage problem: hourly, balancing reservoirs as (intrastage) states, DA bidding and production; possibly a multistage stochastic program on a scenario tree (Fig. 1, p. 4) solved as its deterministic equivalent by CPLEX (p. 4).
  - Balancing-reservoir water balance holds per hour (1a); storage-reservoir balance only aggregated over the day (1b); the end-of-day storage filling must be the same for all intrastage scenarios s ∈ S_j (here-and-now), so Q_{t+1} is evaluated once (p. 5).
  - **Balancing-reservoir fillings at the start and end of each intrastage problem are fixed beforehand**: water cannot be carried from one day to the next in balancing basins. Justified by strong daily autocorrelation of operation in Switzerland (demand-driven prices, temperature-driven inflows) (p. 4).
- **Alternatives compared (Sec. 4, p. 5-8):**
  1. *Hourly model* (eq. 2): hourly SDDP stages; only storage reservoirs as states; balancing reservoirs kept at constant filling (cannot store). Stage-wise independent hourly stages cannot anticipate e.g. evening price peaks (p. 6-7). Hourly SDDP with balancing reservoirs as states "will be troublesome" because their fillings are volatile → poor convergence; SDP suffers curse of dimensionality (p. 6).
  2. *Daily model*: same as (2) with daily steps, daily-average production/market decisions (p. 7).
  3. *Daily intrastage model* (eq. 3): daily interstage with **all** reservoirs (incl. balancing) as states, hourly intrastage; allows only deterministic intrastage problems because each intrastage scenario would need its own Q_{t+1} (p. 7-8, footnote 2).
- **Solution method:** **dualized SDDP** because intrastage decisions include integers (forbidden pumping zones and other operating rules) and value functions are non-concave (p. 3, p. 5); cut selection by level-one dominance and cut maturity (p. 8). Matlab + CPLEX 12.4, 8 cores (p. 8).
- **How uncertainty is represented:** framework allows interstage samples N_t and stochastic intrastage trees, but **in the case study all runs are without different inflow/price scenarios**, so strictly it is DDP (p. 8). The intrastage problem is deterministic (Fig. 1a) (p. 5).
- **Evaluation:** "operation simulation" from sequential hourly MILPs using each model's water values as opportunity costs; **one run, in-sample** (same data as the optimisation) to measure how well each approach approximates the original problem (p. 9). Footnote 3: higher simulation profit could also reflect overfitting (p. 9).

## Data / case
KWO plant as above. Prices/inflow data source not described in this paper (see thesis `abgottspon2015hydro` Ch. 3.5 for an extended case).

## Key findings
- (p. 8-9, Fig. 3a) **Optimisation gap:** multi-horizon stabilises at 0.5 % after ~30 h; hourly model needs > 4 days and stalls at ~5 %, with high memory use for hourly cut sets; daily model reaches 0.5 % in 2 h (~50 iterations); daily intrastage reaches 7 % in 0.5 h but stays ~6 % after two days, "which confirms the difficulties in finding optimal balancing reservoir fillings" (p. 9).
- (p. 9, Fig. 3b) **Accuracy (lower bound vs simulation profit):** daily model **undervalues** performance by > 10 % (plant is flexible; value lies in hourly market opportunities); hourly model **overvalues** by > 10% ("unnecessary detailed optimization of a poor model"); daily intrastage 4-6 % (undervalues, due to the high gap); **multi-horizon only 2-3 %** (slight overvaluation, possibly due to deterministic intrastage).
- (p. 9) All simulations had little spillage; profit differences come from different timing of water use.
- (p. 10) Conclusion: multi-horizon models solved with SDDP are realistic, avoid aggregation and are almost as cheap as aggregated models; "possibly solvable in less than a day".

## Strengths
- Clear taxonomy of four ways to combine long-term storage with short-term (hourly) detail, with formulations for each (eqs. 1-3).
- Shows explicitly that putting small, volatile reservoirs into the SDDP state vector hurts convergence (p. 6, 8-9).
- Separates "optimisation gap" from "model accuracy" (bound vs. simulated profit), a useful evaluation idea.

## Weaknesses / limitations
- **No stochasticity in the reported comparison** (DDP), and the simulation is a single in-sample run (p. 8-9): it is not an empirical validation of stochastic SDDP or of out-of-sample policy quality.
- Balancing reservoirs reset each day (no inter-day storage in small basins) (p. 4).
- No reserves; no head effects discussed; data not described.
- Short conference paper; extended analysis is in the PhD thesis.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review: modelling PHS plants (time-scale coupling) | Multi-horizon decomposition, inter- vs. intrastage, storage vs. balancing reservoirs | p. 2-5, Sec. 1-3, Fig. 1 |
| Model: why weekly stages + hourly sub-periods, not hourly SDDP stages | Hourly SDDP: > 4 days, 5 % gap, overvalues >10 %, cannot anticipate intraday price pattern | p. 6-7 (Sec. 4.1), p. 9 |
| Model: why not aggregate to daily/weekly averages | Daily model undervalues performance > 10 % | p. 7 (Sec. 4.2), p. 9 |
| Model: which reservoirs are SDDP states | Small volatile reservoirs as states → gap stuck ~6 % | p. 7-8 (Sec. 4.3), p. 9 |
| Method: evaluation (bound vs simulated profit) | Lower bound vs. operation simulation as accuracy metric; overfitting caveat | p. 8-9, footnote 3 |
| Theory: nonconvexity in SDDP | Dualized SDDP for integer intrastage decisions; cut selection | p. 5, p. 8 |
| Research gap | Deterministic, in-sample, no reserves, no sizing | p. 8-9 |

## Useful quotes (with page numbers)
> "a smaller difference between the simulation profit and the lower bound indicates a better model accuracy." (p. 9)

## Follow-up references to check (backward snowballing)
- [1] Kaut, Midthun, Werner, Tomasgard, Hellemo, Fodstad (2013), "Multi-horizon stochastic programming", Computational Management Science.
- [2] Löhndorf, Wozabal, Minner (2013), ADDP for hydro storage trading, Oper. Res. (bib `lohndorf2013`).
- [3] Pritchard, Philpott, Neame (2005), hydroelectric reservoir optimisation in a pool market, Math. Prog.
- [11] Abgottspon, Njálsson, Bucher, Andersson (2014), risk-averse medium-term hydro optimisation with spinning reserves, PMAPS.
- [13] Cerisola, Latorre, Ramos (2012), SDDP for nonconvex hydrothermal models, EJOR.
- [15] Homem-de-Mello, de Matos, Finardi (2011), sampling and stopping criteria for SDDP, Energy Systems.

