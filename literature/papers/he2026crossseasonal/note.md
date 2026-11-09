---
bibkey: he2026crossseasonal
bibkey_provisional: true
title: "Cross-Seasonal Optimal Dispatch of a Wind–Photovoltaic Hybrid Pumped-Storage Multi-Energy Complementary System"
authors: "He, Pan; Li, Wenwu; Chu, Zhao"
year: 2026
venue: "Processes 14(17), 2774 (MDPI) (doi:10.3390/pr14172774)"
peer_reviewed: true
methods: [heuristics-simulation, uncertainty-modelling]
review_sections: [ldes-seasonal-storage, modelling-phs-plants]
relevance: background
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/02_Sesonglagring_og_systemmodeller/He2026.pdf
takeaway: "Chinese two-reservoir cascade with 149 MW reversible units added to an annual-regulation reservoir (hybrid PHS, 848 MW): deterministic one-year dispatch minimising residual-load variance, solved by a progressive-optimality heuristic (VPPOA); imposed seasonal storage rate-of-change constraints give 848.8 GWh wet→dry transfer and raise dry-season reliability 93.2%→100% vs daily regulation."
---

# Cross-seasonal dispatch of a hybrid pumped-storage cascade (He et al., 2026)

_Article-numbered paper; page numbers are the article's own pages 1–29 (= PDF pages). Received 31 July 2026, published 29 August 2026._

## Research question / purpose
Existing work on **hybrid pumped-storage stations** (reversible pump-turbines installed between existing cascade reservoirs, i.e. pump-back retrofits of conventional hydro) focuses on short-term peak shaving; the cross-seasonal water-reallocation potential is under-explored (pp. 1, 3). The paper builds a medium-to-long-term cross-seasonal dispatch model, proposes a solution heuristic (VPPOA), and compares three operating modes (pp. 1, 4).

## Setting
- **System:** an unnamed Chinese river basin: Station A (upper, **annual-regulation** reservoir, total storage 2,338 Mm³, regulating storage 1,120 Mm³, normal pool 355 m, dead level 330 m, 500 MW conventional + **149 MW reversible** units) and Station B (lower, daily regulation, 36.78 Mm³, 265/260 m) (Table 3, p. 13). Hybrid station total after expansion 848 MW (p. 12; how 848 relates to 500 + 149 is not explained). Wind 221 MW and PV 774 MW sized by a planned ratio 0.46:0.12:0.42 (p. 12).
- **Markets:** none. Objective is system-technical (residual-load variance), not cost or profit.
- **Horizon and resolution:** one year (2014, a relatively wet year; ECMWF meteorological data) (p. 13). The period length is **not stated explicitly** (typical-day figures suggest sub-daily, possibly hourly, resolution; unverified).

## Method
- **Model type:** deterministic dispatch: minimise variance of residual load R_t = load − wind − PV − hydro generation + pumping (Eqs. 1–3, p. 4). Water balance for both reservoirs with pumping from lower to upper (Eqs. 4–5); storage bounds varying by season (flood-control level in flood season); release and output bounds; pumping power P = ρgHQ/(1000 η_p) (Eq. 18, p. 6); mutual exclusivity of pumping and generating (Eq. 19).
- **Seasonal constraint (Eq. 8, p. 5):** storage must **increase** by at least a minimum per period in the flood season (May–Sept), **decrease** by at least a minimum in the dry season (Dec–Feb), and stay within ±δ in transition seasons (Mar–Apr, Oct–Nov). The seasonal pattern is thus **imposed**, not optimised.
- **Operating modes (pp. 13–14):** (1) no hybrid storage; (2) hybrid daily regulation: water pumped within a day is released the same day, using scheme 1's long-term level trajectory as boundary; (3) hybrid seasonal regulation: long-term level boundary from the seasonal constraint.
- **How uncertainty is represented:** scenario analysis only (Sec. 2.2, pp. 7–9): Latin Hypercube Sampling from empirical CDFs of wind, PV and load, reduced by **K-means** to 5 representative scenarios with probabilities = cluster shares (Eqs. 26–30); 3 typical hydrological years (wet, normal, dry) by ranking annual inflow (Eq. 31); 15 combinations, of which 6 are analysed (Table 2, p. 9). Each scenario solved deterministically and independently (p. 9). Authors admit "probabilistic uncertainty of future inflow and renewable generation is not explicitly modeled" (p. 26).
- **Solution method:** **VPPOA**, a variant of the progressive optimality algorithm (POA): multiple initial reservoir trajectories, sliding windows with variable phase lengths [1,2,3,2,1], 10 heuristic candidate pump/generate strategies per window, feasibility pre-check against the seasonal constraint, final refinement (Fig. 1 and Steps 1–7, pp. 10–12). MATLAB R2023b, max 200 iterations, tolerance 10⁻⁴ (p. 24).
- **Key modelling choices and assumptions:** head appears in the pumping equation but no head-dependent production function is given for generation (unverified); constant pumping efficiency; no costs, prices or end-of-horizon value (year-end level ≈ start level, p. 19).

## Data / case
2014 inflow and ECMWF weather data; wet season has high inflow but weak wind/PV, dry season the reverse (Fig. 3, p. 13). Data "included in this article" (p. 27), but no time series are tabulated.

## Key findings
- (p. 17, Table 4; abstract p. 1) Seasonal vs none vs daily: curtailment 82.74 vs 1,682.26 vs 335.93 GWh; residual-load variance 2,861.05 vs 12,589.28 vs 3,870.07 MW² (−77.3% vs none, −26.1% vs daily); wind–PV accommodation 96.6% vs 40.3% vs 87.4%; wet-season curtailment rate 3.9% vs 38.8% vs 13.4%; dry-season supply reliability 100% vs 86.4% vs 93.2%; **cross-seasonal energy transfer 848.8 GWh** (seasonal mode only).
- (p. 19) Seasonal mode: upper-reservoir level rises to ≈ 355 m in the flood season; cumulative net stored energy peaks at **518 GWh**; year-end level ≈ start level (closed annual cycle).
- (pp. 19–20) Typical days: flood-season midday pumping up to 450 MW with hydro reduced to 620 MW; dry-season hydro raised from 120 MW (no storage) to 350 MW.
- (pp. 20–21, Table 5) Wet → dry year: seasonal-mode variance 2,861 → 3,905 MW², accommodation 96.6 → 93.7%, reliability 100 → 97.3%; the seasonal mode is best in all year types.
- (p. 22, Table 6) Six uncertainty scenarios: variance 2,877–9,300 MW²; dry-season reliability down to 75.01% in the combined adverse scenario.
- (p. 25, Table 8) VPPOA beats GA, PSO and POA: variance 2,861 vs 6,551 / 4,876 / 3,581 MW² (−56.3 / −41.3 / −20.1%); 34.6 s.
- (p. 26) Future work: nested long-/short-term scheduling and stochastic or robust optimisation.

## Strengths
- Directly contrasts daily vs seasonal use of the same pump-turbine capacity, isolating the value of cross-seasonal storage.
- Hybrid (open-loop, cascade) PHS between existing reservoirs is close to the Norwegian pump-back configuration.
- Quantifies seasonal energy shifted (848.8 GWh, peak stored 518 GWh).

## Weaknesses / limitations
- Seasonal behaviour is **forced by constraints** (Eq. 8), so the "value of seasonal regulation" partly reflects the imposed rule, not an optimal policy.
- Deterministic, perfect foresight per scenario; scenarios are not used in a stochastic programme; heuristic solver without optimality bounds.
- Objective (residual-load variance) has no economic meaning for an owner; no prices, costs or markets.
- Time resolution not stated; Station A's 848 MW vs 500 + 149 MW unexplained; MDPI review time < 1 month.
- Internal inconsistencies (my checks): flowchart says 10 initial trajectories, text says 5 (pp. 10–11); scenario S1 (2,877.45 MW²) and Table 7 (1×: 2,877.45) differ from the base 2,861.05; the "Dry-Year" scenario S4 shows 100% reliability and only +1.0% variance, whereas the dry hydrological year in Table 5 lowers reliability (Table 2 column alignment is garbled in extraction, so the scenario labels may differ; unverified); text says no-storage accommodation "decrease[s] from 40.3% to 41.9%" (p. 21), which is an increase. Annual curtailment of 59.7% (1 − 40.3%) in the no-storage case vs a wet-season curtailment rate of 38.8% is hard to reconcile with dry-season supply shortfalls.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.1: seasonal storage value (wet→dry shift) | 848.8 GWh shifted, dry-season reliability 93.2→100% vs daily regulation | p. 1, p. 17 Table 4, p. 19 |
| Background 2.2: hybrid PHS / pump-back between cascade reservoirs | Definition and configuration | p. 1, p. 2, p. 12 Table 3 |
| Lit. review 5.3: seasonal PHS operating models | Deterministic variance-minimisation with seasonal storage constraints; POA-type heuristic | pp. 4–6, 10–12 |
| Lit. review 5.6: gap — deterministic, imposed seasonality | Authors' limitation statement and call for stochastic methods | p. 26 |
| Method discussion: scenario reduction by K-means | LHS + K-means with cluster-share probabilities | pp. 7–9, Eqs. 26–30 |

## Useful quotes (with page numbers)
> "probabilistic uncertainty of future inflow and renewable generation is not explicitly modeled" (p. 26)

## Follow-up references to check (backward snowballing)
- [31] Han, He, Yuan, **Hunt** et al. (2026), Evaluating the performance of seasonal pumped hydro storage coordinated operation with cascade hydropower integrating VRE, Renewable Energy 256, 124023 — source of the seasonal storage constraint (Eq. 8); English-language and likely more useful than this paper.
- [14] Li, Huang & Guo (2012), mid-long term reservoir operation for hybrid pumped storage plants, Electr. Power Autom. Equip. 32 (in Chinese).
- [16] Cheng, Li, Cheng & Guo (2013), operation rules for cascade hydro with hybrid pumped storage, J. Hydraul. Eng. 44 (in Chinese).
- [21] Zhang, Luo, Lu & Wang (2025), long-term complementary generation of wind–PV–hybrid storage (in Chinese).

