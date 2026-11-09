---
bibkey: hjelmeland2016case
bibkey_provisional: true
title: "A case study on medium-term hydropower scheduling with sales of capacity"
authors: "Martin N. Hjelmeland, Arild Helseth, Magnus Korpås"
year: 2016
venue: "Energy Procedia 87, 124–131 (5th International Workshop on Hydro Scheduling in Competitive Electricity Markets) (doi:10.1016/j.egypro.2015.12.341)"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, deterministic-lp-milp, heuristics-simulation, hydro-production-function]
review_sections: [market-participation, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Article II of hjelmeland2019phd: on the Lysebotn system (NO2), a linear SDP/SDDP strategy model with day-ahead + weekly FCR-N sales is re-simulated with a MIP simulator (unit commitment, minimum production, one reservoir at a time, nonconvex PQ); capacity profit falls ~40 % (25.09 → 15.06 MNOK) while total profit falls only 1.26 %; reserves raise total profit by 3.31 % (strategy) / 2.56 % (simulator); the LP overstates available reserve especially when spill risk forces full production."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/hjelmeland2016case.pdf
---

# Case study: SDDP strategy vs MIP simulator with FCR-N sales, Lysebotn (Hjelmeland, Helseth & Korpås, 2016)

_Page convention: journal p. = PDF page + 123 (PDF 1 = p. 124). Reprinted as **Article II** in `hjelmeland2019phd`, thesis pp. 87–95 (p. 87 = cover sheet; journal p. X = thesis p. X − 36). The thesis synthesis summarises it on p. 49 (Eq. 3.1) and p. 50; see `literature/papers/hjelmeland2019phd/note.md`. Tables 1–2 are garbled in the text extraction; the numbers below were reconstructed and cross-checked (every Table 2 percentage reproduces from the Table 1 values, and total profit = energy + capacity + terminal value for all four columns)._

## Research question / purpose
Assess the value of providing primary reserves (FCR-N, "PFR") for a hydropower producer and "how decisive accurate modelling is for sale of capacity" (abstract, p. 124). Novelty: to "analyze and quantify the impacts detailed modelling imposes when including capacity sales", since long- and medium-term strategies are traditionally found with linear models whose drawbacks should be estimated (p. 125). Also notes that the co-optimisation in `helseth2015cooptimizing` [5] "is a simplification of the original market with sequential allocation" (p. 125).

## Setting
- **System:** the **Lysebotn** system in south-western Norway (Lyse AS data), with the new Lysebotn-2 station under construction, so input values are expectations (pp. 125–126). Reservoirs Nilsebuvatn (upper), Lyngsvatn (large regulating reservoir, long horizon) and Strandvatn (lower); Lyngsvatn and Breiava aggregated. Nilsebuvatn and Strandvatn act as short-term storages with rapid filling and emptying (p. 127, Fig. 2). Stations 13.8 MW and 400 MW (from `hjelmeland2016combined`, p. 3). No pumping.
- **Markets:** day-ahead + weekly PFR (FCR-N) market with 6 weekly bidding intervals (p. 126). Exogenous prices, price taker (p. 125).
- **Horizon and resolution:** two-year simulation, weekly stochastic stages, **21 time-blocks per week**, each belonging to one of the 6 weekly PFR intervals (p. 126). Results reported for the first 78 weeks starting from week 5, because the model was not connected to a long-term model and the end-of-horizon value was hard to calibrate (p. 127).

## Method
- **Model type:** same framework as `hjelmeland2016combined` (master-thesis formulation [6]) (pp. 125–126):
  - *Strategy Model*: hybrid SDP/SDDP LP with start-up costs and restrictions on capacity available for sale. **Improved in this paper with "a tighter bound on the minimum production level when supplying spinning reserve"** (pp. 125–126). In addition, a **constraint on outflow for Lyngsvatn and Strandvatn** because station Lyngsvatn-2 can operate from only one reservoir at a time (p. 127).
  - *Simulator Model*: same physical system and time resolution, MIP one-stage problem with more detail on start-up cost, hydraulic connection, power–discharge function and minimum production; binary unit commitment ("rigid unit commitment") (pp. 126–127). Uses the exact same inflow and price samples as the Strategy Model, so "the only difference in modelling is the one-stage dispatch problem" (p. 126).
  - *Reserve formulation*: symmetric spinning capacity; outputs "Marginal Cost of Capacity Spinning (MCCS)" and "Marginal Cost of Capacity Up (MCCU)", the simulated marginal profit change from moving the station set-point up or down, which arise because capacity must be symmetric (p. 129, Fig. 5). The exact form of the tightened minimum-production bound is not written in this paper; the thesis gives it as c_t ≤ c_max/(P_min + c_max)·p_t (`hjelmeland2019phd`, p. 49, Eq. 3.1).
- **How uncertainty is represented:** inflow AR(1), statistics from **70 years** of weekly inflow (p. 126); day-ahead price as a Markov chain with **7 price nodes**, prices from an EMPS simulation started at the beginning of 2013; PFR prices deterministic historical 2013–2014 from Statnett (p. 126).
- **Solution method:** SDDP forward sampling + backward cuts; **50 scenarios**, **8 backward inflow samples** (p. 127).
- **Cases:** "single" (day-ahead only) and "dual" (day-ahead + PFR), each run with both models (p. 127).

## Data / case
Table 1 (p. 130), MNOK and GWh, over the 78 reported weeks:

| | Single, Strategy | Single, Simulator | Dual, Strategy | Dual, Simulator |
|---|---|---|---|---|
| Objective value | 1 418.90 | 1 410.74 | 1 447.64 | 1 436.01 |
| Total generation (GWh) | 3 002.78 | 2 960.31 | 3 060.01 | 3 014.06 |
| Energy profit | 1 212.52 | 1 195.55 | 1 251.97 | 1 232.87 |
| Capacity profit | – | – | 25.09 | 15.06 |
| Terminal value | 207.75 | 217.09 | 190.22 | 200.83 |
| Total profit | 1 420.27 | 1 412.64 | 1 467.28 | 1 448.76 |
| CPU time | 7 h 37 min | 33 min | 10 h 37 min | 39 min |

(The column assignment was reconstructed from the garbled extraction using the percentages in Table 2 and the text on pp. 129–130; treat individual cells as "verified by consistency", not read directly.)

## Key findings
- (p. 124, abstract; p. 131) "the expected profit from sales of capacity was reduced by 40 % when comparing results from the Simulator with the Strategy Model" (Table 2: −39.98 %, 25.09 → 15.06 MNOK). **Note:** the text on p. 130 says "a total capacity profit reduction of 52%, c.f. Table 2", which matches no number in Table 2 and looks like an error; use 40 %.
- (p. 130) Total profit Simulator vs Strategy: **−0.54 %** (single) and **−1.26 %** (dual). Dual vs single: **+3.31 %** (Strategy) and **+2.56 %** (Simulator). Capacity profit is small in absolute terms (≈1.7 % of total profit in the Strategy Model, ≈1.0 % in the Simulator; computed from Table 1).
- (p. 130, Table 2) Simulator vs Strategy: generation −1.41 % / −1.50 %, energy profit −1.40 % / −1.53 % (single / dual); terminal water value higher in the Simulator. Dual vs single: terminal value −8.44 % (Strategy) / −7.49 % (Simulator), i.e. selling reserves leaves less water at the end. (The sentence on p. 129–130 that the dual case "tended to store more terminal water" seems to contradict this; unverified.)
- (pp. 127–128, Figs. 3–4) Reservoir percentiles hardly differ between models, but the Simulator shows jagged Strandvatn filling (rigid schedule) and lower production, so higher reservoir levels "as the gain from providing capacity reserves has been reduced due to the tightened system description" (p. 128).
- (p. 128, Fig. 4) Weeks 60–80: the Strategy Model ran Lyngsvatn-2 at its best point from Lyngsvatn and used the remaining capacity from Strandvatn, selling energy from both reservoirs while still providing PFR, with modest start-up costs. The Simulator must switch between reservoirs and respect minimum production, so it produces at high output for short periods, leaving "less capacity reserves available and increased start-up costs".
- (pp. 128–129, Fig. 5) Simulated marginal costs of providing capacity (MCCS, MCCU) are much higher in the Simulator. Nilsebuvatn (high inflow, small installed capacity) would gain much from extra capacity; when Strandvatn and Lyngsvatn could no longer deliver enough capacity, Nilsebuvatn's MCCS spikes.
- (p. 129, Figs. 6–7) Around weeks 20 and 70 (spring/summer) both markets give high income in the Strategy Model, but in the Simulator production was set to maximum to avoid spill and almost no capacity was sold.
- (p. 129, Fig. 8) Duration curves: with reserves, the Strategy Model shifts output from ~350 MW to ~170 MW and below; the Simulator shifts from ~400 MW to ~150 MW (good efficiency point). Low outputs around 40 MW in the Strategy Model nearly vanish in the Simulator; the effect is "modest as the tightened constraint on the spinning reserve at minimum production level has performed well".
- (pp. 130–131) Conclusion: the Strategy Model "overestimated the amount of available capacity reserves. This was especially evident in periods where prices where beneficial but risk of spillage resulted in maximum production and sales of energy only." Findings "may be case specific, considering that coupling between reservoirs strongly influenced the results" (p. 130). The profit-to-go function is not the true one for the Simulator; PFR volumes and the use of historical PFR prices are limitations (p. 131).

## Strengths
- Full two-model, two-market comparison with absolute numbers (Table 1), so both the value of reserves and the modelling error can be quoted.
- Explains *where* the LP error comes from: hydraulic coupling (one reservoir at a time), minimum production, and spill-driven full-load periods.
- Introduces simulated marginal cost of capacity (MCCS/MCCU) as a diagnostic.
- Real system with industry data (Lyse AS).

## Weaknesses / limitations
- Single case; authors stress case specificity (p. 130).
- Only 50 scenarios; cuts not re-generated for the Simulator; no out-of-sample test.
- Deterministic historical reserve prices; unlimited reserve volumes; price taker.
- No end-of-horizon coupling to a long-term model (only 78 of 104 weeks reported).
- Text errors: "52 %" vs 40 % for capacity-profit reduction (p. 130); unclear statement about terminal water (pp. 129–130); figure axes hard to read.
- No head effects; no pumping (Lysebotn is conventional).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Limitation: LP SDDP overestimates reserve revenue | Capacity profit −40 % (25.09 → 15.06 MNOK), total profit −1.26 % | p. 124 abstract; p. 130 Tables 1–2; p. 131 |
| Limitation: where the error comes from | Spill-risk periods at full load; one-reservoir-at-a-time; minimum production | pp. 128–129, 130–131, Figs. 4, 6–7 |
| Lit review (market participation): value of adding reserves | Total profit +3.31 % (LP) / +2.56 % (MIP) vs energy only | p. 130 |
| Model: tightened minimum-output reserve bound | Introduced in Strategy Model; formula in thesis Eq. 3.1 | pp. 125–126; `hjelmeland2019phd` p. 49 |
| Model: reserve sales reduce terminal water | Terminal value −8.44 % / −7.49 % dual vs single | p. 130, Table 2 |
| Method: evaluation with same scenarios, different one-stage problem | Strategy/Simulator design | p. 126, Fig. 1 |
| Method/diagnostic: marginal cost of capacity (MCCS/MCCU) | Definition and seasonal pattern by reservoir | pp. 128–129, Fig. 5 |
| Lit review: reserves shift output to part load | Duration curves single vs dual, LP vs MIP | p. 129, Fig. 8 |
| Data choices: AR(1) inflow from 70 years; EMPS prices; historical PFR prices | Case set-up | p. 126 |

## Useful quotes (with page numbers)
> "It showed that the Strategy Model overestimated the amount of available capacity reserves." (p. 130)

## Follow-up references to check (backward snowballing)
- [6] Hjelmeland (2015), Long-term scheduling of hydro power system in multiple markets, NTNU master thesis (full model formulation).
- [1] Morales, Conejo, Pérez-Ruiz (2009), economic valuation of reserves with high wind, IEEE TPWRS.
- [2] Zhou & Botterud (2014), dynamic scheduling of operating reserves in co-optimised markets with wind, IEEE TPWRS.
- [10] Pinto, Borges, Maceira (2013), parallel SDDP, IEEE TPWRS.
- [5] = `helseth2015cooptimizing`.

