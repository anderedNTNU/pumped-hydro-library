---
bibkey: kong2020overview
bibkey_provisional: true
title: "An overview on formulations and optimization methods for the unit-based short-term hydro scheduling problem"
authors: "Jiehong Kong, Hans Ivar Skjelbred, Olav Bjarte Fosso"
year: 2020
venue: "Electric Power Systems Research 178, 106027 (doi:10.1016/j.epsr.2019.106027)"
peer_reviewed: true
methods: [deterministic-lp-milp, hydro-production-function, dynamic-programming]
review_sections: [modelling-phs-plants, market-participation]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "literature/inbox/02_Driftsplanlegging_og_optimering/30_Kong_2020_Formulations_and_optimization_methods_for_unit_based_short_term_hydro_scheduling.pdf"
takeaway: "SINTEF/NTNU review of unit-based short-term hydro scheduling (exact methods, papers since 2000), organised by objective and constraint: head and losses, HPF/hill-chart modelling, unit limits, PHS pump modes, reserves, and coupling to long-term strategy via target volume or water value (price coupling preferred)."
---

# Unit-based short-term hydro scheduling: formulations and methods (Kong et al., 2020)

> **Page convention.** Article 106027, pp. 1–14 = PDF pages 1–14.

## Research question / purpose
Classify the mathematical-programming formulations and exact solution methods for the **unit-based** short-term hydro scheduling (STHS) problem (each turbine-generator unit modelled individually), published since 2000, by objectives and constraints rather than paper by paper (pp. 1, 3). Motivation: producers that sell in **both energy and capacity markets** need precise energy conversion and available capacity per unit (p. 1).

## Setting
- **System:** any hydro system; single plants and cascades; includes pumped-storage hydropower plants (PSHP) (pp. 7, 10).
- **Markets:** competitive markets (Scandinavia, Spain, Canada) with price-taking producers, and centralised systems (Brazil) with load targets (p. 3); reserves/ancillary services discussed (p. 10).
- **Horizon and resolution:** STHS = one day to one week (abstract, p. 1); deterministic (uncertainty excluded from scope, p. 3).

## Method
- **Model type:** review of exact methods (LP, NLP, MILP, MIQP, MINLP, DP, Lagrangian relaxation); heuristics explicitly excluded (p. 3).
- **Objectives (pp. 3–4):** maximise revenue (eq. 1); minimise start-up costs (eq. 2); minimise value of water used/spilled or maximise value of stored water (eqs. 3a–3b); others (max power for given flow, min discharge for given load, min losses). Typical competitive objective: revenue − start-up cost + end water value (eq. 4).
- **Constraints (pp. 4–10):** water balance with time delays and overflow (eqs. 5–7); storage and bypass limits (eqs. 8–9); gross head and flow-related head losses — penstock (quadratic), intake, tailrace (eqs. 10–11, Fig. 1); HPF p = G·η_gen(p)·η_turb(h, q)·h·q (eq. 12); unit power and head-dependent discharge limits, forbidden zones (eqs. 13–16); start-up logic (eqs. 17–18); power balance (eqs. 19–20); coupling to long/mid-term strategy (eqs. 21, 3b); environmental, ramping, PSHP and reserve constraints (p. 10).
- **Tables 1–2 (pp. 8–9):** 26 papers with problem type (ULD vs UC+ULD), formulation, solver, hydro system, country, objective, penstock structure, head variation, head losses and coupling type.
- **How uncertainty is represented:** out of scope (p. 3).
- **Key modelling insights:** see findings.

## Data / case
None (review).

## Key findings
- (p. 1) Most STHS literature is **plant-based** (units aggregated into one equivalent unit), which shrinks the problem; capacity markets make unit-level modelling more important.
- (p. 5) Head variation from volume change is negligible for **large reservoirs** over a short horizon; must be considered for medium/small reservoirs with daily or hourly regulation; some large-scale models assume fixed head for tractability. Using the **average of start and end volume** for the water level is common.
- (p. 6) Turbine efficiency can be as low as 60% at minimum discharge and ~95% at best point; generator efficiency typically > 95% and increasing with output.
- (p. 7) Quadratic HPF in release and volume (common in plant-based models) can be very inaccurate with multiple units; piecewise-linear 2-D (fixed head) or 3-D (head-sensitive) tables are the conventional alternative; Diniz & Maceira (2008) cited for convex-hull breakpoints.
- (pp. 7–8, 10) **Coupling to long/mid-term:** load coupling, volume coupling (target end volume), or price coupling (end water value in the objective); a constant energy conversion factor is acceptable for large reservoirs but causes errors for small ones (p. 10); water value as a concave piecewise-linear function of volumes ("cuts") from a long/mid-term model (p. 10); a free end volume with water values gave higher profit than a target volume, so **price coupling is "more accurate and comprehensive"** (p. 10).
- (p. 10) **PSHP:** analogous to pure generation plus a pump-status binary and exclusivity constraints (no simultaneous pumping and generating); fixed-speed pumps have fixed flow/power for a given head; head variation usually neglected in pumping mode; variable-speed pumps face the same challenges as generators; hydraulic short-circuit (some units pump, others generate) gives spinning-reserve flexibility.
- (p. 10) **Reserves:** first modelled as "production + reserve ≤ max production" on plant or system level; nowadays more detailed constraints on response time, types and market rules are needed.
- (p. 11) MILP is the workhorse; piecewise linearisation can cause deviations or infeasibility; dynamic breakpoints help.
- (p. 12) Conclusion: even detailed models simplify heavily (static water level, fixed or flow-only efficiency, constant penstock losses, independent penstocks), which does not match real operation; a quantitative comparison of the effect of such simplifications is needed.

## Strengths
- Systematic, constraint-by-constraint classification; Nordic authors (SINTEF, SHOP background); explicit on coupling to long-term water values and on PSHP and reserves.

## Weaknesses / limitations
- Deterministic scope only; heuristics excluded; mostly short-term, unit-level detail that our weekly/long-term model does not need.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Limitations: continuous power, no UC/min load (`06_mathematical_model.tex:64–67`, `:104–105`) | Unit-based detail (min/max limits, forbidden zones, start-ups) needed when selling capacity | pp. 1, 7, 12 |
| Limitation: constant head/efficiency (`06_mathematical_model.tex:69`) | Head variation negligible for large reservoirs short-term; efficiency ranges 60–95% | pp. 5–6 |
| Lit review: modelling approaches (`04_literature_review.tex:44`) | Classification of objectives/constraints; Tables 1–2 | pp. 3–10, Tables 1–2 (pp. 8–9) |
| Model: end-of-horizon water value / coupling | Load, volume, price coupling; price coupling preferred; cuts from long-term model | pp. 7–8, 10 |
| PHS modelling | Pump binary, no simultaneous pump/generate, fixed vs variable speed, hydraulic short-circuit | p. 10 |
| Market participation: reserves in scheduling models | Simple "p + r ≤ Pmax" vs detailed reserve constraints | p. 10 |
| Theory: HPF formula | Eq. (12) with net head eq. (11) | pp. 5–6 |

## Useful quotes (with page numbers)
> "a price coupling signal is expected to be more accurate and comprehensive than a volume coupling signal." (p. 10)

## Follow-up references to check (backward snowballing)
- Borghetti et al. (2008), MILP STHS with head-dependent reservoir and pumped storage (ref. 18).
- Chang et al. (2001), MILP STHS with pumped storage (ref. 2).
- Skjelbred et al. (ref. 40), SHOP-type MILP with shared penstocks.
- Diaz et al. (ref. 33), free end volume with water values vs target volume.
- Ref. 77: review of trends and challenges in scheduling models for PSHPs.

