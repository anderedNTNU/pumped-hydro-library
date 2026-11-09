---
bibkey: zisos2023mixing
title: "Mixing Renewable Energy with Pumped Hydropower Storage: Design Optimization under Uncertainty and Other Challenges"
authors: "Athanasios Zisos, Georgia-Konstantina Sakki, Andreas Efstratiadis"
year: 2023
venue: "Sustainability, 15(18), 13313"
peer_reviewed: true
methods: [heuristics-simulation, uncertainty-modelling]
review_sections: [reservoir-sizing-capacity, modelling-phs-plants, research-gap, phs-technology]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Hourly rule-based simulation + evolutionary annealing-simplex optimisation sizes the upper reservoir (and PV) of a 6 MW seawater PHS in an islanded wind/PV system (Sifnos, Greece); 100 Monte Carlo scenarios (wind, demand, power curve) give a distribution of optimal reservoir sizes (~315–330k m³, far below the 1.1M m³ 'autonomy' design). No market, no prices, no operational optimisation."
---

# Seawater PHS + renewables design under uncertainty (Zisos et al., 2023)

## Research question / purpose
Two aims (p. 3): (1) can a detailed hourly simulation–optimisation model of the water–energy fluxes reduce the investment cost of an already proposed hybrid renewable energy system (HRES) on the Greek island of Sifnos, by finding a **smaller upper reservoir** than the conventional "energy autonomy" sizing of [23] (Katsaprakakis & Voumvoulakis 2018)? (2) what is the impact of three sources of uncertainty on the design: wind velocity (natural, exogenous), electricity demand (anthropogenic, exogenous) and wind-to-power conversion (internal/endogenous, a probabilistic power curve)? A parallel aim is to discuss the technical challenges of using **seawater** (the sea is the lower reservoir): corrosion, marine fouling, groundwater salinisation (p. 3, Sec. 6).

## Setting
- **System:** non-interconnected island power system (Sifnos, Western Aegean; 74 km², 2755 permanent residents, ~100,000 summer tourists; current supply 9.0 MW oil plant, 1.20 MW wind, 0.20 MW PV; 2020 demand 17.3 GWh, hourly peak 5.4 MW in summer, p. 3). Proposed HRES: 4 wind turbines (2 × 2.3 MW Enercon E-70 E4 + 2 × 0.9 MW Enercon E-44 = 6.4 MW, spaced 400 m), PV park, and an **open-loop seawater PHS**: upper reservoir on a plateau at +320 m, sea as lower reservoir (pp. 3–6, Table 1). Pump 6.0 MW, turbine 6.0 MW (both fixed; p. 6). Penstock 910 m long, 1.0 m diameter (p. 6). The existing oil plant covers the remainder.
- **Markets:** none. The system serves island load; revenue is a fixed "energy profit" of 300 EUR/MWh and an "energy penalty" of 350 EUR/MWh (Table 2, p. 7; the penalty presumably applies to unmet demand, the paper does not spell it out — unverified), plus an empirical reliability penalty (Fig. 4, p. 8). No day-ahead, intraday or reserve market; energy market uncertainty listed as future work (p. 17).
- **Horizon and resolution:** hourly simulation over **20 years** (the economic life of the project, p. 6, p. 11).

## Method
- **Model type:** simulation–optimisation for **design (investment)**. Inner model: hourly rule-based simulation (Fig. 3, p. 6): net power P_net = P_wind + P_solar − P_demand; if P_net > 0 and storage < S_max, pump seawater to the upper reservoir; if P_net < 0 and storage > dead volume, release through the turbine; otherwise unmet demand (covered by oil plant) or excess energy (spilled). Outer loop: **evolutionary annealing-simplex (EAS)** algorithm [45], a heuristic global optimiser combining simulated annealing with downhill simplex (p. 8). Coded from scratch in R/RStudio 4.2.2 (p. 7).
- **Design variables:** reservoir **active depth** (hence storage volume) and **number of PV modules** (PV capacity) (p. 4, p. 7). Pump/turbine power, wind capacity and head are fixed.
- **Objective:** "multi-objective" problem collapsed into financial terms: revenues from electricity production minus construction, purchase, installation and maintenance costs, all as equivalent annual cost with a 20-year depreciation period, plus a reliability penalty with logarithmic shape (Fig. 4: penalty grows to ~25 M EUR as reliability falls towards 50 %) (pp. 7–8). Reliability = frequency of demand satisfaction (p. 7). Discount rate not stated (unverified).
- **How uncertainty is represented:** Monte Carlo with **100 scenarios** (p. 11). Each scenario: one synthetic 20-year **hourly** series of wind velocity and of demand generated with the **anySim** R package (stationary/cyclostationary stochastic models reproducing marginal distributions and dependence of ~10 years of historical data) (p. 11), plus random power-curve shape parameters a ~ N(2.25, 0.0225), b ~ N(20, 0.016) chosen so mean deviation from the theoretical curve ≤ 15 % (p. 11), plus a soft cut-out between 25 and 30 m/s with random slope z ~ N(150, 225) (large) and N(45, 100) (small) (p. 11). Solar radiation is **not** stochastic (same data in all scenarios, p. 12). The design is **re-optimised separately in each scenario**, giving 100 equally probable optimal designs, not one design optimised against all scenarios (p. 11) — in stochastic-programming terms closer to a wait-and-see distribution than a here-and-now solution (our interpretation).
- **Post-processing:** marginal distributions fitted to optimal depth and mean annual profit (fitdistrplus, moment matching), then a **Gaussian copula** of the two (p. 13, Figs. 6–7).
- **Key modelling choices and assumptions (pp. 5–6):** trapezoidal reservoir (linear storage/area–elevation curves); intake 1.2 m above the reservoir bottom (dead volume for deposits); pump capacity 6.0 MW = max potential surplus (6.4 MW wind − 0.4 MW min hourly demand); turbine 6.0 MW, slightly above peak load 5.4 MW; **constant efficiencies** turbine 0.85, pump 0.80 (so round trip ≈ 0.68); no head effects in the power conversion (with ~3 m active depth vs 320 m head they would be negligible anyway); wake effect between turbines via eq. (1) with a = 0.10, k = 0.038 (p. 5); power curve eq. (2) (Sakki et al. [36]) with a = 2.25, b = 20 calibrated to manufacturer data (p. 5). Inputs also include precipitation and evaporation (Fig. 3).
- **Cost data (p. 7, Table 2):** excavation 6.00 EUR/m³; waterproofing membranes 1.50 EUR/m²; conveyance 25.0 EUR/m; wind 1,200,000 EUR/MW; solar 1,100,000 EUR/MW; pump/turbine cost C = C0·P^a·H^β (Aggidis et al. [44]) with C0 = 14,400 EUR, a = 0.56, β = −0.112, giving ~3.94 M EUR for 6 MW at 320 m gross head; maintenance 1 % of investment per year.

## Data / case
- Hourly wind velocity, solar radiation and power demand (basis for the synthetic data) published on Zenodo (doi 10.5281/zenodo.8100255) (p. 17). Historical record ~10 years, called "rather short" (p. 11).
- Wind turbine and PV data in Table 1 (p. 5): E-44 900 kW rated, cut-in 3.0 m/s, rated 16.5 m/s; E-70 E4 2300 kW, cut-in 2.5 m/s, rated 15.0 m/s; cut-out 34 m/s listed for both (text on p. 10 refers to a 25 m/s theoretical cut-off — inconsistent; Table 1 column alignment in the text extraction is also uncertain); PV module 1.94 m², 340 W, 17.5 % efficiency.

## Key findings
- (p. 4) The preliminary conventional design [23] sized the reservoir at **1,100,000 m³**, giving up to **16 consecutive days** of autonomy from full without recharging. The authors argue this worst-case "autonomy" approach oversizes the reservoir (p. 3).
- (p. 8, Table 3) **Deterministic benchmark optimum:** active depth 2.88 m (4.08 m total incl. 1.20 m), storage **315,195 m³**, PV 1.09 MW; reliability 94.76 % (oil plant runs ~5 % of the time); mean annual production wind+PV 24.98 GWh, PHS 4.69 GWh; mean annual profit 789,131 EUR; investment 15,526,518 EUR; annuity 1,814,222 EUR; payback 5.90 years; capacity factors PV 0.207, small WT 0.304, large WT 0.424, hydro station 0.108.
- (pp. 8–9) Optimal reservoir is **less than a third** of [23]'s, though the authors caution the two are not fully comparable (different assumptions). Low hydro capacity factor reflects its supporting role covering deficits at peak demand, not poor performance (p. 8).
- (p. 12, Table 4) **Monte Carlo (100 scenarios):** active depth mean 3.07 m (sd 0.76); storage mean **329,882 m³** (sd 53,370; listed 10/50/90 % quantiles 400,282 / 323,278 / 274,583 m³); PV mean 1.69 MW (sd 0.03); reliability 94.89 % (sd 1.50); mean annual net profit 640,234 EUR (sd 255,062; quantiles 959,029 / 669,924 / 315,269); investment 15,615,067 EUR; payback 6.35 years (sd 0.51); CF small WT 0.29, large WT 0.41, hydro 0.09; PV CF constant 0.21. Reservoir size and hence profit and reliability vary significantly, PV capacity hardly at all (p. 12).
- (p. 13) Across scenarios, optimal active depth and mean annual profit are **strongly negatively correlated (Pearson R = −0.75)**; a copula of the two lets a designer read a probabilistic profit range for a chosen reservoir size, or the range of sizes compatible with a profit target; a conservative design favours a large reservoir (upper quantile) (pp. 13–14).
- (p. 16) Even under uncertainty, the original 1.1 M m³ proposal lies far outside the 90 % range of optimal sizes; the smaller reservoir costs only a minor loss of reliability.
- (p. 14) Okinawa Yanbaru seawater PHS (first in the world, built 1987–1999) was dismantled in 2016 because demand growth was overestimated, so it became unprofitable. Ali & Jang [82] found seawater PHS cheaper in initial investment than batteries for an island HRES.
- (pp. 14–16) Seawater challenges: GRP/FRP pipes (friction factor 0.030, p. 15); marine fouling; corrosion types for stainless-steel pumps (crevice, erosion, cavitation, corrosion fatigue), PREN ≈ 40 per NORSOK M-001 (p. 15); centrifugal pumps, possibly in parallel with different flow rates; groundwater salinisation and the need for HDPE geomembranes and drainage (pp. 15–16).

## Strengths
- One of few papers that puts **storage volume** directly into the optimisation as a design variable, rather than evaluating fixed configurations.
- Rich uncertainty treatment for an islanded system: high-resolution (hourly) synthetic wind and demand that reproduce dependence structure, plus internal (power-curve) uncertainty.
- Transparent cost data and plant parameters (Tables 1–2, p. 6), usable as a cross-check.
- Copula-based presentation of the size–profit trade-off is a clear decision-support idea.

## Weaknesses / limitations
- **Operation is a greedy rule** (pump all surplus, generate all deficit): no intertemporal optimisation, no water values, no prices. Storage value comes only from reducing unmet demand.
- Design re-optimised per scenario: the result is a distribution of scenario-optimal designs, not a single design that is robust or optimal in expectation, and no design is tested out of sample on other scenarios.
- Heuristic optimiser (EAS), no optimality guarantee; only two design variables; pump and turbine fixed at 6 MW, so the pump/turbine/reservoir combination is not explored.
- Constant efficiencies, no head effects; no inflow (seawater, sea as lower reservoir); solar not stochastic; discount rate not reported (unverified).
- Internal inconsistencies: Fig. 6 caption (normal fitted to profit, log-normal to depth) contradicts the text (normal to depth, log-normal to profit) (p. 13); Table 4 "10 %" quantile of depth (3.96 m) is larger than the "90 %" quantile (2.36 m), so the quantile convention is unclear; mean PV capacity 1.69 MW under Monte Carlo vs 1.09 MW in the benchmark is not discussed; cut-out 34 m/s in Table 1 vs 25 m/s in the text.
- Islanded, small (MW-scale) system; not transferable to a price-taking plant in a liberalised market without major changes.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review (reservoir sizing): storage size as a decision variable | Reservoir active depth + PV capacity optimised; pump/turbine fixed at 6 MW | p. 4 (Sec. 3.1), p. 7 (Sec. 3.3), p. 8 (Sec. 3.4) |
| Lit review (reservoir sizing): conventional autonomy sizing oversizes | 1.1 M m³ / 16 days autonomy vs optimised 315,195 m³ | p. 3, p. 4, p. 8, p. 16 |
| Lit review (reservoir sizing): size–profit trade-off under uncertainty | R = −0.75 between optimal depth and mean annual profit; copula as decision support | p. 13–14 (Sec. 5.3, Figs. 6–7) |
| Lit review (modelling PHS): rule-based simulation of PHS operation | Hourly flowchart: pump surplus, generate deficit, storage bounds | p. 6 (Sec. 3.2, Fig. 3) |
| Lit review (uncertainty): Monte Carlo with synthetic hourly series | 100 scenarios, anySim, 20-year hourly wind and demand; probabilistic power curve | p. 11 (Sec. 5.1) |
| Comparison table row | Perspective, method, uncertainty, markets (none), horizon, resolution | Secs. 3–5, pp. 4–13 |
| Background (PHS technology): open vs closed loop definition | Open loop: upper reservoir connected to natural water body as lower; closed loop: no external hydrological connection | p. 2 |
| Background (PHS technology): seawater PHS, Okinawa | First seawater PHS 1987–1999, dismantled 2016 | p. 14 (Sec. 6) |
| Background (PHS technology): PHS share of storage | >95 % of global cumulative storage capacity (citing [16]) | p. 2 |
| Parameter cross-check: efficiencies, PHS cost function | Turbine 0.85, pump 0.80; C = C0·P^a·H^β, C0 = 14,400 EUR, a = 0.56, β = −0.112 | p. 6, p. 7 (eq. 3) |

## Useful quotes (with page numbers)
> "the optimized reservoir size equaled less than a third of the one suggested" (p. 9)

## Follow-up references to check (backward snowballing)
- [23] Katsaprakakis & Voumvoulakis (2018), hybrid power plant towards 100 % autonomy for Sifnos, Energy 161 (original conventional sizing).
- [31] Sakki et al. (2022), stochastic simulation–optimisation framework for renewable energy systems under uncertainty, RSER 168 (the framework applied here).
- [27] Kapsali, Anagnostopoulos & Kaldellis (2012), wind-powered PHS for remote islands, sensitivity analysis, Applied Energy 99.
- [11] Kaldellis, Zafirakis & Kavadias (2009), techno-economic comparison of storage for island networks, RSER 13.
- [95] Das et al. (2021), review of PHS for renewable and hybrid systems, Energy Storage 3.
- [97] Ruiz et al. (2022), low-head seawater PHS review, RSER 160.

