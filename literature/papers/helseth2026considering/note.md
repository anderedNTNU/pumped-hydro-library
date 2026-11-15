---
bibkey: helseth2026considering
bibkey_provisional: false   # in references.bib since 2026-11-15 (added through Zotero, key pinned)
title: "Considering short-term variability in long-term hydropower scheduling by multi-stage Benders decomposition and residual demand functions"
authors: "Arild Helseth, Birger Mo"
year: 2026
venue: "Energy Systems, online first 3 August 2026 (doi:10.1007/s12667-026-00825-z)"
peer_reviewed: true
methods: [sddp-time-series, benders-decomposition, uncertainty-modelling]
review_sections: [price-volatility, modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-15
takeaway: "Long-term SDDP model (weekly stages, 3 years, Northern and Central Europe 2050) in which the weekly hydro production is decided before the hourly wind and solar outcome is known; the within-week dispatch is approximated by cost cuts built in the forward pass. With 2-hour instead of 24-hour resolution the median and the spread of the water values rise, so short-term variability changes the value of stored water."
---

# Short-term variability inside long-term SDDP (Helseth & Mo, 2026)

_Open access (CC BY), published online first; 24 pages, no volume or journal page numbers yet. Page numbers below are **PDF pages**. Downloaded 2026-11-15 from link.springer.com. System model, no pumping._

## Research question / purpose
Long-term hydropower scheduling models use coarse time steps and assume that everything within a stage is known. How can short-term variability and uncertainty in wind and solar power be included in such a model at acceptable computing time, and what does it do to the water values (abstract, p. 1; contributions, p. 4)?

## Setting
- **System:** Northern and Central Europe in a 2050 scenario, 61 price areas, 17 of them with a detailed hydropower system represented through an aggregated reservoir and feasibility cuts (pp. 12–13, 15–16).
- **Markets:** none; minimisation of the expected cost of thermal generation and rationing; prices are duals of the hourly power balances (p. 5, p. 19).
- **Horizon and resolution:** 3 years, weekly stages; 24-, 4- or 2-hour steps within the week (cases T24, T4, T2) (p. 16).

## Method
- **Model type:** multistage stochastic linear program; each weekly problem is itself two-stage: the week's total hydro production is chosen first, the hourly dispatch follows for each wind scenario (eq. 1, pp. 6–7).
- **How uncertainty is represented:** weekly inflow by a first-order vector autoregressive model, inflow is a state variable (pp. 13–14); hourly wind and solar by a few scenarios per week, the same set in every node, assumed uncorrelated with inflow and between weeks (p. 5, p. 7). Thirty weather years lie behind both models (p. 16).
- **Solution method:** SDDP, described as a sampling-based variant of multi-stage Benders decomposition (p. 12). The within-week dispatch problem is replaced by "cost cuts" that are added gradually in the forward iterations, one solve per visit, and shared among the nodes of a stage (pp. 8–11).
- **Settings in the case (p. 17):** 40 sampled inflow scenarios per forward iteration, 10 backward openings, 5 wind scenarios, at most 300 iterations, cost cuts built in the first 80. A final simulation on 40 pre-defined scenarios (p. 19).
- **Key modelling choices and assumptions:**
  - The reservoir is assumed to stay within its limits during the week, so there is **no reservoir balance per time step** (p. 6).
  - Hydro production of the week can be distributed freely over the time steps, which "may overestimate the flexibility of hydropower"; ramping constraints could be added in the dispatch problem (p. 15).

## Model elements (eqs. 1 and 6, pp. 6–7, 14)
- **Sets:** thermal units, time steps within the stage, scenario-tree nodes or stages, hydro subsystems, wind scenarios, cut sets (future cost, cost and feasibility cuts).
- **Parameters:** marginal cost of thermal units; **cost of rationing**; demand per step; maximum hydro, thermal and wind output per step; maximum reservoir volume in energy units; inflow model parameters; scenario probabilities.
- **Variables:** thermal generation, hydro production per step, wind production, rationing, reservoir volume, total hydro production of the stage, spillage, future expected cost, dispatch cost.
- **Constraints:** storage balance per stage in energy (volume + production + spillage = previous volume + inflow); the hourly hydro productions sum to the stage total; hourly power balance; capacity bounds; feasibility cuts that keep the aggregated hydro system within what the detailed system can do; cuts.

## Data / case
- Scenario and system data described in their ref. [26]; open-source model and example code (p. 10, p. 22).

## Key findings
- (p. 19, Fig. 9) Finer time resolution gives more frequent high prices (above 50 €/MWh) and zero prices in South-East Norway.
- (p. 21, Figs. 10–11) The median and the range of the water values increase with finer time resolution, in weeks 15 and 35 alike.
- (p. 22) Conclusion: the variance of water values depends on the time resolution, so long-term models of such systems need a fine time resolution.
- (pp. 17–18, Fig. 7) Building only one cost cut per stage and forward pass converges slowly in a deterministic test (about 2000 iterations), but in SDDP several scenarios share the cuts.

## Strengths
- Addresses the assumption that the whole week is known when the weekly decision is made, which our weekly model also makes.
- Shows with one model how time resolution changes water values.
- Open access and open code.

## Weaknesses / limitations
- System model with aggregated hydropower; no owner perspective, no reserves, no pumping.
- Wind uncertainty by five scenarios; no correlation between weeks or with inflow.
- A fixed number of iterations instead of a convergence test in the large case (p. 17).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Limitation of our model: the whole week is known when decisions are made | statement that stage-wise known uncertainty is reasonable for inflow but less so for wind and solar | p. 3 |
| Model: one water balance per week, free distribution within the week | assumption and its caveat | pp. 6, 15 |
| RQ3 / results: short-term variability raises the level and spread of water values | Figs. 10–12 | pp. 19–21 |
| Theory: SDDP as a sampling-based variant of multi-stage Benders decomposition | statement | p. 12 |
| Literature review 5.6: long-term models with fine time resolution | review of recent work | pp. 3–4 |

## Useful quotes (with page numbers)
> "may overestimate the flexibility of hydropower" (p. 15, on distributing the weekly production freely over time steps)

## Follow-up references to check (backward snowballing)
- Their [16]–[18]: analytical and decomposed representations of the short-term dispatch inside SDDP (residual demand / intrastage cost functions).
- Kaut, Midthun, Werner et al. (2014), multi-horizon stochastic programming (their [11]).
