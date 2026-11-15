---
bibkey: li2022solving
bibkey_provisional: true    # not in references.bib yet (Zotero was not running 2026-11-15); key follows the Better BibTeX pattern
title: "Solving stochastic hydro unit commitment using Benders decomposition and modified stochastic dual dynamic programming"
authors: "Zhuangzhuang Li, Ping Yang, Yi Yang, Guanpeng Lu, Yufeng Tang"
year: 2022
venue: "Frontiers in Energy Research 10, 955875 (doi:10.3389/fenrg.2022.955875)"
peer_reviewed: true
methods: [benders-decomposition, multistage-scenario-trees, hydro-production-function, uncertainty-modelling]
review_sections: [modelling-phs-plants, market-participation]
relevance: background
read_by: []
added: 2026-11-15
takeaway: "One-day, hourly unit commitment for a price-taking hydropower producer under price uncertainty: start-up and shutdown costs, minimum up and down times, forbidden zones and head effects, with the value of stored water entering as a piecewise-linear future revenue from a medium-term SDDP model; solved by Benders decomposition around a modified SDDP that builds cuts from lift-and-project relaxations."
---

# Stochastic hydro unit commitment with modified SDDP (Li et al., 2022)

_Open access (CC BY). Published version, 14 pages; page numbers below are the article's page numbers 01–14 (= PDF pages). Downloaded 2026-11-15 from frontiersin.org. Not an SDDP study of medium-term storage: SDDP is used inside a **one-day** problem._

## Research question / purpose
How should a price-taking hydropower producer commit its units over the next day when market prices are uncertain and the value of water left in the reservoir (the opportunity cost) is taken into account, and how can the resulting large mixed-integer stochastic problem be solved (abstract, p. 01; contributions, p. 03)?

## Setting
- **System:** Xiluodu (18 units, 12,600 MW, annual regulation) and Xiangjiaba (8 units, 6,000 MW) on the Yangtze (p. 09, Table 2); a second test on an eight-plant system of 3,084 MW from Conejo et al. 2002 (p. 12). No pumping.
- **Markets:** energy only (day-ahead price), price-taker (p. 01). No reserves.
- **Horizon and resolution:** 1 day, hourly steps (p. 10).

## Method
- **Model type:** multistage stochastic mixed-integer linear program (eqs. 1–25, pp. 04–06).
- **How uncertainty is represented:** market price as a scenario tree with three price nodes per period, assumed **stagewise independent** so that cuts can be shared; built from an ARMA forecast with Pearson type 3 forecast errors and Monte Carlo sampling (p. 07, p. 09, p. 10).
- **Solution method:** two layers. Benders decomposition: the master problem sets start-up and shutdown; the subproblem operates the plants. The subproblem is decomposed by period and solved by a "modified SDDP" in which lift-and-project cuts are added to the LP relaxation until it gives the mixed-integer solution, and the SDDP cut is taken from the duals of that relaxation (pp. 06–09).
- **Stopping:** the inner algorithm stops when the upper bound is within the 95 % confidence interval of the lower bound, as in Pereira and Pinto; 500 scenarios sampled in the forward iteration (pp. 10–11).
- **Key modelling choices and assumptions:** head-dependent generation (fore-bay level, tail-race level, penstock loss, net head, efficiency) linearised with the method of Guisández and Pérez-Díaz (p. 05); no end-volume requirement, the end volumes follow from the future revenue function (p. 09, p. 11).

## Model elements (eqs. 1–25, pp. 04–06)
- **Objective:** immediate revenue (price × output per unit and period) plus future revenue minus start-up and shutdown costs (eqs. 1–4).
- **Future revenue:** piecewise-linear function of the end-of-horizon reservoir volumes, given by slopes and intercepts (eq. 14, Table 3); the paper says it can be obtained from medium-term scheduling with SDDP (p. 05).
- **Constraints we do not have:** water travel time between plants (eq. 5); discharge per **unit** with an on/off binary (eqs. 7–8); fore-bay and tail-race levels, penstock loss and net head (eqs. 9–13); generation and efficiency as functions of discharge and head (eqs. 15–17); **forbidden operating zones** (eqs. 18–19); start-up and shutdown logic (eqs. 20–21); **minimum online and offline time** (eqs. 22–23); **maximum number of start-ups and shutdowns** (eqs. 24–25).
- **Parameters in the case (p. 09):** start-up cost 300 $ and shutdown cost 100 $ per event; minimum up and down time 4 h; at most two start-ups and shutdowns per unit; forbidden zone from 0 to 20 % of maximum output.

## Data / case
- Day-ahead prices of Sichuan Province for the error distribution (p. 09).
- CPLEX 12.9 from Python (p. 10).

## Key findings
- (p. 10, Table 5) Deterministic case: the method reproduces the direct CPLEX solution within 0.001 % and is 8.8 times faster.
- (p. 11, Table 6) Stochastic case: converges in 2,123 s with a final gap of 0.0093 %; classical Benders decomposition stops at a 3.16 % gap after one hour.
- (p. 11) Value of the stochastic solution: 2.3 % of total revenue.
- (p. 11, Fig. 9) With the future revenue function the plants stop discharging at the end volumes that maximise total revenue, without a fixed end volume.

## Strengths
- Shows how a medium-term water value (a piecewise-linear function of end volume) is used as the end condition of a short-term unit commitment model.
- Lists the unit-level constraints that a linear medium-term model leaves out.

## Weaknesses / limitations
- One-day horizon; prices stagewise independent; start-up cost values are assumed "for simplicity" (p. 09).
- The future revenue parameters are given, not computed in the paper.
- Parts of the text describe the method loosely; the equations in our text copy are partly garbled (use the PDF).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Limitation of our linear weekly model: unit commitment detail we omit | start-up cost, min up/down time, forbidden zones, head | pp. 04–06 |
| Background: water value as end condition of a short-term model | future revenue constraint (14) and Fig. 9 | pp. 05, 11 |
| Method: stopping when the upper bound is inside the 95 % confidence interval | inner algorithm | pp. 10–11 |
| Literature review 5.6: SDDP-type methods with integer variables | modified SDDP with lift-and-project cuts; comparison with SDDiP | pp. 03, 08 |

## Useful quotes (with page numbers)
> "none of the existing literature on HUC has taken the future revenue into account" (p. 02; the authors' own claim, not checked)

## Follow-up references to check (backward snowballing)
- Guisández & Pérez-Díaz (2021), MILP formulations for the hydro production function in unit-based short-term scheduling.
- Kelman, Barroso & Pereira (1998/2001), future revenue of hydro plants in a liberalised market with SDDP.
