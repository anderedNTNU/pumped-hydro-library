---
bibkey: finnah2021
title: "Optimizing trading decisions of wind power plants with hybrid energy storage systems using backwards approximate dynamic programming"
authors: "Benedikt Finnah, Jochen Gönsch"
year: 2021
venue: "International Journal of Production Economics 238, 108155"
peer_reviewed: true
methods: [adp-reinforcement-learning, uncertainty-modelling, heuristics-simulation]
review_sections: [ldes-seasonal-storage, market-participation]
relevance: background
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/Innlimte_referanser_2026-10-29/finnah2021.pdf
takeaway: "Wind farm (20 MW) with a short-term battery (20 MWh, 20%/day self-discharge) and a long-term hydrogen store (300 MWh) trading hourly on the German continuous intraday market over a year, solved by backwards ADP with OCBA sampling; combining short- and long-term storage beats a single doubled storage by 4-5 pp, and joint operation beats separate operation by over 21 pp."
---

# Wind + battery + hydrogen trading with backwards ADP (Finnah and Gönsch, 2021)

_**Version and page mapping:** the PDF is the authors' manuscript (SSRN, October 2020, "to appear in IJPE"; 31 pages, own pagination = PDF pages). The published article has an article number (108155), not page numbers. Page numbers below are **manuscript pages**._

## Research question / purpose
- Decision problem of a profit-maximising producer with stochastic wind generation who sells on the **continuous intraday market** and owns a **hybrid energy storage system**: a battery (short-term, high efficiency, high self-discharge) and a **hydrogen-based energy storage (HES)** (long-term, low round-trip efficiency, near-zero self-discharge, hydrogen can also be sold) (pp. 1-2).
- Contributions (p. 3): (1) model the problem as a dynamic program solved by **backwards ADP (BADP)**; (2) compare l1/l2 norms, weighted regression and an **optimal computing budget allocation (OCBA)** for fitting value function approximations; (3) managerial insights on synergies of short- and long-term storage and joint vs separate operation.

## Setting
- **System:** 20 MW wind farm (four 5 MW turbines, Hamburg wind data), grid connection 25 MW; NaS battery 20 MWh, 5 MW in/out, 0.75 charge and discharge efficiency, self-discharge 20%/day; HES with 5 MW electrolyser (efficiency 0.8) and 5 MW fuel cell (0.6), 300 MWh hydrogen tank, zero self-discharge (pp. 16, 26).
- **Markets:** German continuous intraday market only, hourly products traded right before gate closure (30 min) at the volume-weighted average price; hydrogen sold at a known constant price (30 EUR/MWh); imbalances penalised (pp. 5-7, 17). Price-taker.
- **Horizon and resolution:** one year, **T = 8760 hourly stages**; discount factor 1.05^(−1/8760) (5%/year) (p. 16).

## Method
- **Model type:** finite-horizon Markov decision process (Bellman eq. 16, p. 12) with decisions: electricity to trade for next hour, hydrogen to sell, share of excess energy to battery (p. 9); a fixed priority rule for covering deficits (wind → battery → fuel cell → balancing) (Assumption 7, p. 7).
- **How uncertainty is represented:** intraday price as an **Ornstein-Uhlenbeck (mean-reverting AR(1)) process** with mean depending on hour, weekday, month (splines) and trend, fitted to German intraday prices 2014-2018 (eq. 26, pp. 16-17); wind speed from month-hour Weibull distributions with interpolated parameters and a cubic power curve (eq. 27, p. 17). Price assumed Markov (Assumption 4, p. 6).
- **Solution method:** BADP on **post-decision states** (battery level, hydrogen level, commitment, price) (eq. 18, p. 12); value function approximated by a quadratic polynomial with 20 coefficients (eq. 20, p. 13); backwards in time, sample M post-decision states per period (Sobol sequence), evaluate each N times by solving the one-period problem with the next period's VFA, regress (Algorithm 1, p. 13). Variants: l1/l2 regression, weighted regression, OCBA allocating more evaluations to high-variance states (pp. 14-15). Budget M·N = 5000 evaluations per period (p. 18). Benchmark: tuned safety-stock heuristic (p. 18). Forward ADP not implemented (argued to perform badly here, p. 18).
- **Key modelling choices and assumptions:** price-taker; perfect one-hour-ahead production forecast (Assumption 5); risk-neutral (discounting as mild risk adjustment); penalties from the 2006 German balancing-group regime (no pay for overproduction, double price for shortage) for policy learning; evaluation with average reBAP 38.40 EUR/MWh for setting comparisons (pp. 17-18); terminal value zero (eq. 17, p. 12).

## Data / case
- German continuous intraday VWAP 2014-2018 (EPEX), wind 2012-2016 Hamburg-Billbrook scaled to 100 m (p. 17). Matlab, standard PC; learning a policy about 5.5 h (p. 19). Evaluation: 1,000 simulation runs on the same out-of-sample scenarios from the calibrated processes; 99% CI below 0.5% of mean (p. 19).
- Validation on a discretised 100-period variant: l2-OCBA within 1.2 pp of exact discretised backward recursion and about 500 times faster (exact > 60 h) (Appendix B, pp. 26-27).

## Key findings
- (p. 19, Fig. 3) Weighted regression beats unweighted; OCBA improves further; l2 beats l1; l2-OCBA(250,20) best and used thereafter.
- (pp. 20-21) Strong weekly and seasonal patterns: weekend prices 16% lower, 12% less sold, 44% more bought; hydrogen production peaks in the first four months (low prices), reconversion peaks at year end (high prices); hydrogen stored for multiple weeks; tank empty at year end.
- (p. 22, Fig. 8) Of 100 MWh produced, 53.1% goes directly to the grid; about 20% to the electrolyser, 27.9% to the battery; **18.3% of production is lost**, mostly to storage efficiencies.
- (Table 1, pp. 22-23) Profit relative to base: without hydrogen sales 98.09%; **only battery (doubled) 95.76%; only HES (doubled) 96.40%** — combining short- and long-term storage is beneficial (4-5 pp); independent optimisation/operation of wind and storage 78.65% (over 21 pp loss, driven by grid fees and conservative selling).
- (p. 23) Conclusion: almost one fifth of energy never reaches the grid; considerable synergy between short- and long-term storage; integrated optimisation essential. Future work: multi-hour-ahead trading, limit orders.

## Strengths
- Year-long hourly horizon with a long-term storage that exploits seasonal price differences, solved with a scalable ADP method.
- Explicit list and discussion of modelling assumptions (pp. 6-7).
- Careful algorithm comparison and validation against an exact discretised solution.
- Clear illustration of long-duration (hydrogen) vs short-duration (battery) storage roles.

## Weaknesses / limitations
- Not hydro; intraday only (no day-ahead or reserves); price-taker with constant hydrogen price.
- Price model is a simple OU process; perfect one-hour production forecast.
- Penalty regime from 2006 used for learning, different regime for evaluation.
- Evaluation in-model (simulated from calibrated processes), not on historical paths.
- Manuscript version.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section, manuscript) |
|---|---|---|
| Background 2.1: long- vs short-duration storage roles | Battery daily cycling vs hydrogen seasonal shifting; 4-5 pp synergy | pp. 2, 21-23, Table 1 |
| Background 2.1: self-discharge and efficiencies of battery/hydrogen | NaS up to 20%/day; HES round trip 35-65%; battery 70-85% | pp. 2, 16 |
| Literature review 5.3/methods: ADP for storage trading over a year | BADP, post-decision VFA, OCBA | pp. 12-15 |
| Theory: why DP scales linearly in stages vs multistage SP exponentially | Statement | pp. 2, 8 |
| Method: long horizon to reduce end-of-horizon effects | Statement | p. 8 |
| Literature review: ADDP of Löhndorf et al. (2013) needs discrete exogenous states | Review statement | p. 5 |

## Useful quotes (with page numbers)
> "almost one fifth of energy produced never reaches the grid but is lost due to the efficiencies" (p. 23)

## Follow-up references to check (backward snowballing)
- Weitzel, Glock (2018). Energy management for stationary electric energy storage systems: a systematic literature review. EJOR 264(2). (Review of storage operation models.)
- Jiang, Pham, Powell, Salas, Scott (2014). A comparison of approximate dynamic programming techniques on benchmark energy storage problems: does anything work? IEEE ADPRL. (Forward ADP needs monotonicity/concavity, p. 18.)
- Gönsch, Hassler (2016). Sell or store? An ADP approach to marketing renewable energy. OR Spectrum 38(3), 633-660.
- Durante, Nascimento, Powell (2020). Backward approximate dynamic programming with hidden semi-Markov stochastic models in energy storage optimization.
- Löhndorf, Minner (2010). Optimal day-ahead trading and storage of renewable energies: an ADP approach. Energy Systems 1.

