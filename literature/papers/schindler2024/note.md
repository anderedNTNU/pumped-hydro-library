---
bibkey: schindler2024
title: "A Planner-Trader Decomposition for Multimarket Hydro Scheduling"
authors: "Kilian Schindler, Napat Rujeerapaiboon, Daniel Kuhn, Wolfram Wiesemann"
year: 2024
venue: "Operations Research (published 2024; DOI 10.1287/opre.2023.2456)"
peer_reviewed: true
methods: [two-stage-stochastic, uncertainty-modelling, heuristics-simulation]
review_sections: [market-participation, modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/Innlimte_referanser_2026-10-29/schindler2024.pdf
takeaway: "Year-long hourly scheduling of a pumped-storage cascade selling in spot and secondary reserve (aFRR-type) markets with stochastic hourly activations, made tractable by a planner (daily reservoir targets, affine decision rules + SAA) / trader (daily LP) decomposition; on an Austrian cascade, adding reserves raises out-of-sample revenue by about 25% and the reserve-up market earns about 45% of revenue."
---

# Planner-trader decomposition for multimarket hydro (Schindler et al., 2024)

_**Version and page mapping:** the PDF is the authors' manuscript with appendix from Optimization Online (46 pages, own pagination = PDF pages), not the typeset Operations Research version. Page numbers below are **manuscript pages**; check against the published article before quoting. `references.bib` has no volume/pages for this entry. The first author died in 2020; the paper is posthumously dedicated to him (p. 29)._

## Research question / purpose
- Peak/off-peak spreads in Europe are eroding (German nuclear phase-out raising base prices, PV lowering peaks), so hydropower producers turn to **reserve markets** to recover profitability (pp. 1-3).
- Propose a tractable stochastic program for a fleet of interconnected (pumped-)hydro plants trading in **spot and reserve markets** over one year with hourly decisions and uncertain prices, inflows and **reserve activations** (pp. 3-4). Claimed as the first model with stochastic reserve activations at hourly granularity (p. 4).

## Setting
- **System:** arbitrary cascade topology (directed acyclic graph; each arc can carry a generator and a pump; dummy sink reservoir) (p. 8). Case: **Gasteiner Tal cascade, Salzburg, Austria** — Bockhartsee annual reservoir 18.5 Mm³, Nassfeld daily reservoir 0.23 Mm³, Remsach compensation reservoir 4,000 m³; Nassfeld **pumped-storage** plant between Bockhartsee and Nassfeld (generation 40,600 m³/h, 6.68 × 10⁻⁴ MWh/m³; pumping 28,500 m³/h, inverse efficiency 9.35 × 10⁻⁴ MWh/m³), Böckstein and Remsach plants downstream; up to 264,000 MWh/year (p. 24).
- **Markets:** spot (day-ahead) and **secondary reserve up and down** (capacity fee + activation price, pay-as-bid) in the Austrian Power Grid control area; intraday, primary and tertiary reserves and forwards excluded (pp. 4, 9). Reserve products in four-hour blocks for capacity, 15-min activation prices (pp. 24-25).
- **Horizon and resolution:** one year (D = 364 days), hourly (p. 25); planner daily, trader hourly within a day (p. 3).

## Method
- **Full model (C)** (pp. 7-12): maximise expected spot revenue + reserve capacity fees + activation payments; spot bids s_t, reserve-up/down bids u_t, v_t decided day-ahead; generation, pumping, spill hourly; energy delivery constraint s_t + (allocation × activation) u_t − (…) v_t = η g_t − ζ p_t, reservoir dynamics, bounds; **reserve commitments must be honoured robustly** under all activation sequences (non-compliance → penalties or exclusion) (pp. 11-12). This has **random recourse** (activations multiply bids in constraints) (p. 3).
- **Market approximations (pp. 9-10):** markets infinitely liquid; spot price revealed day-ahead and bids adapt to it (continuum of bids, price-taker); reserve allocation as **Bernoulli** variables with probabilities set by a single capacity-price bid; activation fraction of the hour as continuous random variables with mean set by a single energy-price bid; up + down activation ≤ 1; activations serially independent and independent of other uncertainties (justified in Appendix A via a two-state Markov model of 5-second activations; uncertainty coefficient shows near-independence between hours, pp. 33-34). Inflows known one day ahead (p. 10).
- **Planner-trader decomposition (Sec. 3, pp. 12-14):** exact bi-layer reformulation — planner (CP) chooses end-of-day reservoir levels over 365 stages; trader (CT) maximises expected daily profit given start and end levels (Props. 1-2).
- **Information restriction (Approximation 1, p. 15):** end-of-day levels fixed **one day in advance**. Then the 25-stage trader problem reduces to a **finite LP** (CTr) of size O(A·H) whose constraints cover the worst-case activation (two "scenarios": full up or full down activation) (Props. 3-5, Theorem 1, pp. 15-18). Valid inequality: down-reserve bids limited by spot bids plus pumping capacity (Prop. 4, pp. 16-17). Theorem 2 (p. 19): reduced problem (Cr) is a lower bound on (C) with fixed recourse.
- **Numerical solution (Sec. 5, pp. 20-23):** end-of-day levels as **affine decision rules** in (i) cumulative inflow of the day, (ii) cumulative inflow to date, (iii) average spot price of the day (Approximation 2, p. 21); two-stage problem solved by **sample average approximation** (Approximation 3, p. 21). **Water values** = shadow prices of the constraint linking start-of-day and previous end-of-day levels (eq. 5, pp. 20, 22). Daily trader problem (6) adds nominal (expected) activation flows and values nominal end-of-day water with those water values (p. 22); real-time operation via truncated problems after activations are observed (p. 23). Rolling horizon, re-solved daily, circular reuse of data to avoid end-of-horizon effects (pp. 23, 25).
- **Key modelling choices and assumptions:** risk-neutral; no on/off (integer) constraints, **no head effects**, no flow delays (p. 4); single bid per market tuned by two hyperparameters: target capacity-bid acceptance probability and target activation frequency (pp. 4, 25); capacity and activation bids constant over four-hour blocks (p. 25).

## Data / case
- Inflows: daily data 2002-2012, 1/24 per hour; 2002-2011 in-sample, 2012 out-of-sample (p. 24).
- Prices: APG Balancing Statistics 2020; out-of-sample = realised EXAA/EPEX spot, 4-h capacity fees and 15-min activation prices of 2020; in-sample generated from regression models with month, weekday and hour (block) dummies (pp. 24-25). Capacity fees hard to predict (p. 24).
- C++ / Gurobi 9.0.1, single core; planner problems < 2 min, trader problems fractions of a second (p. 25). Code and data on GitHub (p. 25).

## Key findings
- (Table 1, p. 25) Predicted activation frequencies are accurate (e.g. target 0.5 → 50.9%/51.8% actual), but capacity acceptance deviates from targets (target 1.0 → 70.7%/47.1%) because the fee regressions fit poorly.
- (Table 2, p. 26) Out-of-sample annual revenues 10.48-13.40 M EUR across hyperparameters; best (capacity target 1.0, activation target 0.5): **13,396.20 k EUR**, split 53.0% spot, 44.8% reserve-up, 2.2% reserve-down. Spot-only-like settings (capacity target 0.0): about 10.76 M EUR.
- (p. 26) Reserve-down appears negligible but enables pumping and later revenue; adding **either** reserve market to a spot-only model raises revenue by **20-25%**, the second reserve market adds only 0.1-5%.
- (pp. 26-27, Figs. 3-4) Model captures different time scales: annual reservoir changes slowly, daily and compensation reservoirs fast; **water values are seasonal**, highest before the depletion phase of the top reservoir.
- (p. 28, Fig. 5) Water-level predictions are close for a while but degrade further ahead; updated daily.
- (p. 29, Fig. 6) The stochastic spot+reserve strategy outperforms both the stochastic spot-only model and a deterministic expected-value model by **about 25%** in cumulative revenue; the deterministic model had to be restricted ad hoc and still fails to honour reserve commitments.
- (pp. 4-7) Literature summary with run times: Löhndorf et al. (2013) 4-40 h; Helseth et al. (2015) 42 h, (2016) 55-60 h, (2017) 24-40 h; Chazarra et al. (2018) 3-17 min per day; Klæboe et al. (2019) 2-7 h; SDP/SDDP models typically weekly stages with crude reserve representation (pp. 5-7).

## Strengths
- Year-long horizon with hourly reserve activations and pumping, solved in minutes.
- Exact decomposition results with clear statements of which approximations lose optimality.
- Realistic reserve mechanics (allocation risk, activation risk, robust honouring of commitments).
- Out-of-sample evaluation with real 2020 prices and a held-out inflow year; public code.
- Good review of multimarket hydro models (deterministic, scenario tree, SDP, SDDP) with run times (pp. 4-7).

## Weaknesses / limitations
- Spot bids adapt to the realised price (continuum of bids), activations serially independent, markets infinitely liquid.
- Affine decision rules on three features; perfect-information recourse within the SAA; conservative information restriction.
- No head effects, no integer unit constraints, no delays; only secondary reserve.
- Same price year (2020) used for in- and out-of-sample (in-sample from regressions), so out-of-sample is only partly independent (p. 25).
- Manuscript version in our folder.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section, manuscript) |
|---|---|---|
| Background 2.4/2.5: eroding peak/off-peak spreads push hydro to reserves | Nuclear phase-out, PV growth (Mayer 2014) | pp. 1-3 |
| Background 2.4: reserve types and activation times | Primary ~30 s, secondary ~5 min, tertiary manual 15 min | p. 2 |
| Background 2.2: PHS ~95% of global grid storage (DOE 2020) | Statement | p. 2 |
| Literature review 5.4: value of reserves for PHS cascade | +20-25% revenue from one reserve market; reserve-up ~45% of revenue; stochastic beats deterministic by ~25% | pp. 26, 29 |
| Literature review 5.3/5.4: survey of multimarket hydro models + run times | Deterministic, tree, SDP, SDDP studies | pp. 4-7 |
| Model: reserve commitments must be feasible under all activations | Model (C), Prop. 4 valid inequality | pp. 11-12, 16-17 |
| Model: reserve activations serially independent (justification) | Appendix A | pp. 33-34 |
| Model: water values as duals of reservoir linking constraint; seasonal water values | Eq. (5), Fig. 4 | pp. 20, 22, 27 |
| Method: rolling horizon, circular data reuse against end effects | Sec. 5-6 | pp. 23, 25 |
| Method: hyperparameter tuning of bid prices | Tables 1-2 | pp. 25-26 |
| Research gap: SDDP models coarse for reserves | Critique of weekly SDP/SDDP | pp. 6-7 |

## Useful quotes (with page numbers)
> "significant revenues can be earned on the reserve markets if the stochastic reserve activations are modeled faithfully" (p. 4)

## Follow-up references to check (backward snowballing)
- Helseth, Fodstad, Mo (2016). Optimal medium-term hydropower scheduling considering energy and reserve capacity markets. IEEE TSTE 7(3).
- Helseth et al. (2015). Co-optimizing sales of energy and capacity in a hydropower scheduling model. PowerTech.
- Chazarra et al. (2016, 2018). Stochastic weekly scheduling / economic viability of PHS in secondary regulation.
- Schillinger, Weigt, Barry, Schumann (2017). Hydropower operation in a changing environment: a Swiss case study. Proc. 14th EEM. (Yearly LP with weekly bidding subproblems for spot, intraday and all three reserve types, p. 5.)
- Fodstad, Aarlott, Midthun (2018). Value-creation potential from multi-market trading for a hydropower producer. Energies 11(1).
- Abgottspon, Andersson (2012). Approach of integrating ancillary services into a medium-term hydro optimization.
- Gauvin, Delage, Gendreau (2017, 2018). Decision rule approximations for reservoir management.

## Added 2026-11-05: simultaneous pumping and generation
- The model has **no constraint** against pumping and generating on the same arc in the same hour (continuous flows, no binaries, pp. 11–12).
- **Lemma 2 (appendix, PDF p. 42):** adding the complementarity condition g_t·p_t = 0 does not lower the optimal value of the reduced trader problem, which includes reserve bids. Proof idea: reduce both flows by the same water amount, spill the difference, and the net energy and all market decisions stay unchanged. This relies on the pump using more energy per m³ than the generator produces, and on unlimited spill.
- **Use for Q-004:** a formal argument that an LP need not forbid simultaneous operation, because an optimal solution without it always exists. The argument holds only if spill is free and unlimited, and it does not cover separate waterways where the pump and turbine sit on different arcs.

## Added 2026-11-05: reduced trader LP (CTr) and what it would mean for our weekly model
_The Greek symbols are lost in the text extraction; this is our reading of pp. 11–17. Verify against the PDF before citing details._
- **(C), p. 12:** energy delivery s_t + (allocated × activated) u_t − (allocated × activated) v_t = η g_t − ζ p_t; reservoir w_t = w_{t−1} + inflow + M(g − p + z); flow and level bounds.
- **(CTr), p. 17:** a deterministic LP.
  - Flows are scheduled so that spot plus **fully activated up-reserve** is delivered: s_t + u_t = η g_t − ζ p_t, the worst case for the water.
  - Down-reserve is limited by the valid inequality s_t − v_t ≥ −Σ ζ p̄ (Prop. 4): down-regulation at most equals the scheduled output plus maximum pumping.
  - Expected prices (acceptance probability × fee, plus expected activation payment) sit in the objective.
- **Mapping to our model:**
  - Replace the per-unit allocation (r^{G±}, r^{P±}), the readiness rule, the eligibility sets and the τ-margins with plant-level c^↑_t, c^↓_t.
  - The water balance includes full up-activation, and down-reserve is bounded by output (+ pumping headroom).
- **Trade-off:**
  - **Gains:** simpler, a peer-reviewed formulation, guaranteed deliverability, and Lemma 2 for simultaneous operation.
  - **Losses:** no distinction between products (FCR spinning/symmetric vs aFRR/mFRR) or between units. Full activation every hour is very conservative. The pump term in down-headroom must be dropped for fixed-speed Aurland 3.
