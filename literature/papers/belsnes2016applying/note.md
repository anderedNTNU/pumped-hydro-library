---
bibkey: belsnes2016applying
bibkey_provisional: true
title: "Applying successive linear programming for stochastic short-term hydropower optimization"
authors: "Michael M. Belsnes, Ove Wolfgang, Turid Follestad, Ellen K. Aasgård"
year: 2016
venue: "Electric Power Systems Research 130, pp. 167–180 (doi:10.1016/j.epsr.2015.08.020)"
peer_reviewed: true
methods: [multistage-scenario-trees, hydro-production-function, deterministic-lp-milp, uncertainty-modelling]
review_sections: [modelling-phs-plants, market-participation]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "literature/inbox/02_Driftsplanlegging_og_optimering/07_Belsnes_2016_Applying_successive_linear_programming_for_stochastic_short_term_hydropower_optimization.pdf"
takeaway: "SINTEF's SHARM: stochastic successive LP on price/inflow scenario trees for 1-week hourly scheduling; a first-order head-of-water term in the LP gains ~1.5% and lands within 0.02% of the NLP; stochastic beats re-run deterministic by 0.01–8.9%, mainly via avoided spill."
---

# Stochastic successive LP for short-term hydro scheduling (SHARM) (Belsnes et al., 2016)

> **Page convention.** Journal pp. 167–180 = PDF pages 1–14 (journal page = PDF page + 166).

## Research question / purpose
Can the successive linear programming (SLP) method that SINTEF's deterministic SHOP model uses to handle non-linear, state-dependent hydro (turbine efficiency depending on head) be extended to a **stochastic** setting (price and inflow scenario trees), and can such a model reproduce the significant gains from stochastic short-term scheduling reported in the literature on real Norwegian data (p. 169)? Also: how to quantify the benefit of a stochastic model over the industry practice of re-running a deterministic one (pp. 174–175).

## Setting
- **System:** conventional reservoir hydro (no pumping) in Norway. GAMS test: two coupled stations, upper reservoir 10× the lower (300 vs 30 units) (p. 171). Case A/B: real system with 6 reservoirs and 6 plants (p. 175, Fig. 12). Case C: one reservoir, one plant, nominal discharge ≈ 20 m³/s (p. 178).
- **Markets:** only the **day-ahead spot market** is modelled; spot price is the only stochastic price (p. 169). Intraday (Elbas) and the regulating-power market are described as context (pp. 167–168, Fig. 2) but not modelled; primary/secondary reserves explicitly not included (p. 174).
- **Horizon and resolution:** hourly time resolution, typical planning period 1–2 weeks (p. 170); case studies use a 1-week (7-day) horizon (pp. 174, 178).

## Method
- **Model type:** stochastic MILP/LP written as a **deterministic equivalent on a scenario tree** (p. 169). Objective = expected income from production plus value of stored water at the end of the horizon (eq. 1, p. 170).
- **How uncertainty is represented:** scenario trees for price and inflow, generated from multi-dimensional scenarios with the Heitsch–Römisch / Dupačová tree-construction and reduction algorithms (refs 17–19, p. 169). Inflow scenarios from unadjusted HBV ensemble forecasts (51 members, equal probability) (pp. 169, 176); price scenarios from a market-analysis company (SKM Market Predictor, 60 scenarios, equal probability) (p. 177). **Branching every 24 h** to reflect daily day-ahead clearing (pp. 169, 177). Price and inflow are assumed **uncorrelated** and are made stochastic **one at a time** in the case studies (pp. 169, 172).
- **Solution method:** iterative SLP. Base LP (eqs. 1–6, p. 170): water use split into "up to best point" and "above best point" segments with two efficiencies (two-step efficiency curve to avoid non-convexity); end-of-horizon water value as a **decreasing step-wise function** (eq. 5); total water valued as efficiency-weighted sum over reservoirs (eq. 6). Between iterations efficiencies are updated from the previous reservoir level (eqs. 7–8, linear in level, assuming **flat-bottom, straight-wall reservoirs**, p. 170). A small penalty on deviations from the previous iteration's reservoir level (eqs. 9–10) removes **flip-flop** between solutions (pp. 170–171). A **head-of-water term** (eq. 11, derived in Appendix A, p. 180) is added to the objective: a first-order approximation of the extra production that a higher reservoir level would give via higher efficiency, which vanishes at convergence (p. 171).
- **SHARM prototype (pp. 172–174):** C++ implementation; incremental model building (each LP is built around the previous solution, like warm-starting, and shifts linearisation points so the result approaches a quadratic solution, Fig. 7, p. 173); unit commitment (UC) by MIP in the first part of the tree and a heuristic further out; 3 iterations in UC mode + 3 iterations with locked UC give a converged solution (p. 173); minimum generation (30–40% of nominal to avoid cavitation, p. 173) handled with a "two mode" approach without binaries (p. 172); start-up costs included; no hydraulic connections, time delays or reserves (pp. 173–174).
- **Evaluation method (Section 5, pp. 174–175):** the deterministic strategy (point-wise probability-weighted mean forecast) is evaluated **on the same scenario tree** step by step: at each branching point deterministic sub-problems are solved with earlier decisions fixed (Figs. 9–11). This mimics daily re-planning, but by construction the stochastic model can never come out worse (p. 174, Fig. 9). The authors list the biases both ways (shrinking branching factor favours deterministic; same scenarios for optimisation and evaluation favour stochastic) and name rolling-horizon evaluation as the better alternative (p. 175, p. 179).
- **Key modelling choices and assumptions:** head effect via efficiency as a linear function of reservoir level; two efficiency segments; end-value step function; scenario tree with daily branching; risk-neutral expected value.

## Data / case
GAMS test: inflow 0 or 4 with probability 0.5 per period (2 in the first), generator capacities 3 and 6 water units, efficiency 1 up to 80% of capacity and 20% lower above, spot price 2, end water value 10 steps declining linearly from 2.24 to 0.8 (p. 171). Case data from Norwegian producers in the SHARM industry tests (Agder Energi, TrønderEnergi named in acknowledgments, p. 179). Hardware: Intel Core 3 GHz, 8 GB RAM (p. 176).

## Key findings
- (p. 172, Fig. 6) Head-of-water optimisation improves the objective by **up to 1.5%**, most when reservoirs are about **half full** (largest flexibility); the iterative linear approach is on average only **0.02%** below the non-linear model.
- (p. 171, Fig. 5) Without a penalty the SLP flip-flops; with it, convergence in 6 iterations.
- (p. 174) Run time: Case A stochastic 165.75 s (16-scenario, 7-day tree) vs SHOP deterministic 10.23 s; Case C 20.41 s vs 1.64 s. A prior study found that reducing the tree by up to 22% changes the optimal value by ≤ 0.02%.
- (p. 176, Table 3) **Case A (inflow uncertainty, high reservoirs):** stochastic +0.39% objective; deterministic spills 60% more (34 vs 14 Mm³) because it saves water for later prices without seeing spill risk.
- (p. 177, Table 4) **Case B (price uncertainty, 40% initial level):** total objective only +0.01% (dominated by end value), but sales revenue +2.71% and obtained average price 25.00 vs 24.95 €/MWh (+0.19%).
- (p. 178, Table 5) **Case C (inflexible single reservoir, 80% initial, high inflows):** stochastic +8.9%; spill cut ~90% (0.09 vs 0.7 Mm³).
- (p. 169) Literature gains from stochastic short-term models: 0–16% (De Ladurantaye et al. 2007) and 1.3% (Honve et al. 2012).
- (p. 179) In their cases inflow uncertainty matters more than price, but this is "not a general result"; prices are expected to become more volatile with more intermittent renewables, raising the value of modelling uncertain prices.
- (p. 167) Context: day-ahead market had 84% market share in the Nordics in 2013; Elspot 349 TWh vs Elbas 4.2 TWh.

## Strengths
- Clean derivation of a head-of-water term that keeps the model linear (eq. 11, App. A) and a test against the true NLP.
- Real industry cases; honest discussion of the bias of the chosen evaluation method.
- Shows where stochastic value comes from (spill avoidance, price-hour allocation).

## Weaknesses / limitations
- Short-term only (1 week); end-of-horizon value is an exogenous step/linear function, not computed consistently.
- Price and inflow never stochastic together; assumed uncorrelated.
- Evaluation on the in-sample tree favours the stochastic model; no out-of-sample or rolling evaluation.
- No formal convergence proof for SLP (p. 172, p. 179); no reserves, no pumping.
- Equal-probability ensemble/price scenarios acknowledged as questionable (pp. 176–177).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model assumptions: constant head/efficiency (`06_mathematical_model.tex:69`) | Size of the head-of-water effect in an LP: up to 1.5%, largest at half-full reservoirs; LP with first-order term within 0.02% of NLP | p. 172, Fig. 6; p. 179 |
| Model: linear head correction (if extended) | First-order head-of-water term eq. (11) and efficiency-update eqs. (7)–(8); derivation | pp. 170–171; App. A p. 180 |
| Theory/method: SLP for non-linear hydro; SHOP used by most large Scandinavian producers | SLP description, flip-flop and penalty fix | p. 168; pp. 170–171, 173 |
| Literature review: modelling of hydro plants (short-term, stochastic) | Scenario-tree stochastic STHS with daily branching, HBV ensembles, price scenarios | pp. 169, 176–177 |
| Literature review: market participation | DA only; intraday/regulating market described; reserves explicitly not modelled; future work on sequential markets | pp. 167–168, 174, 179 |
| Method: evaluation of stochastic vs deterministic policies | Step-by-step evaluation on the scenario tree; discussion of its biases; rolling horizon preferred | pp. 174–175, 179 |
| Background: Nordic DA dominance | 84% market share 2013; Elspot 349 TWh vs Elbas 4.2 TWh | p. 167 |
| Discussion: where stochastic value comes from | Spill reduction 60%/90%; +2.71% revenue under price uncertainty | pp. 176–178, Tables 3–5 |
| Background: price volatility | Expectation of more volatile Nordic prices with renewables and new cables | pp. 168, 179 |

## Useful quotes (with page numbers)
> "the applied head-of-water optimization improves the model solution." (p. 172)

> "It is difficult to determine which of price and inflow is more important to consider as a stochastic parameter." (p. 179)

## Follow-up references to check (backward snowballing)
- Fosso & Belsnes (2004), SHOP short-term hydro scheduling in a liberalized system (ref. 7).
- De Ladurantaye, Gendreau & Potvin (2007), strategic bidding for price-taker hydro (ref. 13) — 0–16% stochastic gain.
- Fleten & Kristoffersen (2008), short-term hydropower production planning by stochastic programming (ref. 11).
- Follestad, Wolfgang & Belsnes (2011), effect of scenario-tree approximations (ref. 15).
- Heitsch & Römisch (2003), scenario reduction (ref. 17).

