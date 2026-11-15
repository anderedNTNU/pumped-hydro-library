---
bibkey: downward2020stochastic
bibkey_provisional: false   # in references.bib since 2026-11-15 (added through Zotero, key pinned)
title: "Stochastic dual dynamic programming with stagewise-dependent objective uncertainty"
authors: "Anthony Downward, Oscar Dowson, Regan Baucke"
year: 2020
venue: "Operations Research Letters 48(1), 33–39 (doi:10.1016/j.orl.2019.11.002); filed copy is the Optimization Online preprint of 11 July 2018"
peer_reviewed: true
methods: [sddp-time-series, sddp-markov-chain, uncertainty-modelling]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-15
takeaway: "Shows that a price process in the objective makes the value function a saddle function (convex in the reservoir state, concave in the price state), so ordinary cuts fail, and gives an SDDP algorithm with saddle cuts that keeps an autoregressive price as a continuous state; demonstrated on a hydro-bidding cascade. Names the Markov-chain discretisation as the usual alternative and notes that it needs cuts for every Markov state."
---

# SDDP with a price process in the objective (Downward et al., 2020)

_Our copy is the **Optimization Online preprint** (dated 11 July 2018, 15 pages, title with "stagewise dependent"); the article appeared in Operations Research Letters 48(1), pp. 33–39, which is not open access. Page numbers below are **preprint pages**; check the published version before quoting. Downloaded 2026-11-15 from optimization-online.org (entry 2018/02/6454)._

## Research question / purpose
How can SDDP handle a stochastic process with stagewise dependence in the **objective coefficients** (for example an autoregressive spot price) without discretising it into a Markov chain (abstract, p. 1; pp. 1–2)?

## Setting
- **System:** hydro-bidding example from Wahid (2017): two reservoirs in a cascade, each with a turbine; extended to five reservoirs (pp. 11–12). No pumping.
- **Markets:** energy sold at the spot price; a cost of spillage as a penalty for exceeding operating limits (p. 12).
- **Horizon and resolution:** 12 stages (p. 11). An illustration, not a case study.

## Method
- **Problem class:** multistage stochastic linear programs with stagewise-independent noise that drives a state `y` (the price) through a linear recursion; the stage cost is bilinear in the price state and the decisions (p. 3).
- **Why ordinary SDDP fails:** dependent noise is usually handled by adding state variables. For right-hand-side noise the value function stays convex. For objective noise the value function becomes **concave in the price state and convex in the other states**, a saddle function, so cutting planes are not valid bounds (p. 2; Lemmas 1–2, pp. 3–5).
- **The usual workaround:** model the dependent process as a Markov chain with discrete states (Gjelsvik 1999, Philpott and de Matos 2012, Rebennack 2016). The paper states that this "can become computationally expensive since cuts must be added for all of the discretized Markov states", and that a multi-dimensional process needs prohibitively many states; SDDP variants interpolate between the value functions of Markov states (Gjelsvik 2010, Wahid 2017) (p. 2).
- **Proposed method:** lower bounds for a saddle function built from sampled points (Sec. 3, pp. 5–6, after Baucke et al. 2018); an SDDP-style algorithm in which **every realisation of the next stage's noise is solved in the backward pass** to build an expected cut (p. 8); almost sure convergence in finitely many iterations (Theorem 2, p. 11). No upper bound function is computed, so there is no deterministic convergence test (p. 7).
- **Implementation:** in SDDP.jl ("objective states"); practical points such as bounding the multipliers in early iterations are left out of the paper (p. 14).

## Model elements (example, pp. 11–12)
- **State:** water in each reservoir at the start of the stage; the price state (lag 1, or lags 1 and 2).
- **Decisions:** flow through each turbine and spill.
- **Constraints:** linear reservoir transition; minimum and maximum flow limits.
- **Objective:** spot price times generation, minus a spillage penalty.
- **Price process:** autoregressive of lag 1, half of the previous price plus half of a time-dependent level plus a noise term with ten equally likely values (p. 12); a lag-2 version for the larger example (p. 12).

## Data / case
- Two-reservoir model solved for 2000 iterations; the lower bound converges to the value found by stochastic dynamic programming, −24,855 $ (p. 12, Fig. 1).
- Five-reservoir model with two price lags (seven state dimensions): 5000 iterations, then a Monte Carlo simulation with 1000 replications, about 2000 seconds (p. 13).

## Key findings
- (p. 12) The saddle-cut algorithm reproduces the SDP solution on the small example.
- (p. 13) With seven state dimensions SDP is no longer practical, the new algorithm is.
- (p. 13, Fig. 2) In a low-price path more energy is kept in storage because the price is expected to revert upwards; in a high-price path more is generated early.
- (p. 14) Autoregressive and ARMA price processes can be modelled inside SDDP; before this they could only be approximated with Markov chains or binary expansion.

## Strengths
- States precisely why price uncertainty is harder than inflow uncertainty in SDDP, which is the reason our model uses a Markov chain.
- Available in open software.

## Weaknesses / limitations
- Small illustrative example; no comparison of solution quality or run time against a Markov-chain model.
- Requires the price state to evolve independently of the decisions and of the other states (p. 14).
- Only a lower bound (for minimisation); convergence is judged from the bound.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method / theory: why price is put in a Markov chain rather than treated as a continuous state | saddle-function argument | p. 2; Lemmas 1–2, pp. 3–5 |
| Method: cuts are needed for every Markov state in Markov-chain SDDP | statement with references | p. 2 |
| Literature review 5.6: alternatives to the Markov chain for price uncertainty | saddle cuts / objective states | pp. 5–8, 14 |
| Limitation of our choice: few Markov states for a two-dimensional process (price and inflow) | remark on multi-dimensional processes | p. 2 |

## Useful quotes (with page numbers)
> "cuts must be added for all of the discretized Markov states" (p. 2)

## Follow-up references to check (backward snowballing)
- Wahid (2017), PhD thesis, River optimization: short-term hydro-bidding under uncertainty (open on HAL).
- Baucke, Downward & Zakeri (2018), deterministic algorithm for multistage stochastic minimax dynamic programmes.
- Rebennack (2016), combining sampling-based and scenario-based nested Benders decomposition, Mathematical Programming 156.
