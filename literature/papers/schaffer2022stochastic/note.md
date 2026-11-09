---
bibkey: schaffer2022stochastic
bibkey_provisional: true
title: "A stochastic dynamic programming model for hydropower scheduling with state-dependent maximum discharge constraints"
authors: "Linn Emelie Schaffer, Arild Helseth, Magnus Korpås"
year: 2022
venue: "Renewable Energy 194, 571–581"
peer_reviewed: true
methods: [sdp, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: high
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/52_Schaffer_2022_Stochastic_dynamic_programming_hydropower_state_dependent_maximum_discharge_constraints.pdf"
takeaway: "NTNU/SINTEF medium-term SDP for a Norwegian two-reservoir cascade (price taker, weekly stages, 1 year) with a joint price–inflow Markov chain built by AR model → 10,000 samples → K-means → counted transitions; a state-dependent discharge rule makes water values nonconcave but costs <0.8% profit."
---

# SDP with state-dependent maximum discharge constraints (Schaffer, Helseth & Korpås, 2022)

> **Page convention.** Journal page = PDF page + 570 (PDF p. 1 = p. 571, PDF p. 11 = p. 581). Open access (CC BY).

## Research question / purpose
How can a state-dependent environmental constraint (maximum discharge that depends on reservoir volume, weekly inflow and whether the "low-inflow period" has ended) be represented accurately in medium-term hydropower scheduling, and how does it change water values, simulated operation and profit? SDDP cannot easily treat such nonconvexities, so the authors use SDP (pp. 572–573).

## Setting
- **System:** two upper reservoirs and plants of Bergsdalsvassdraget, Western Norway; about 55 MW generation and up to 360 Mm³ storage (p. 577, Fig. 3). Conventional cascade, no pumping.
- **Markets:** single energy price per sub-period (price-taker revenue). No reserves.
- **Horizon and resolution:** one year of weekly decision stages; each week has three price periods of 56 h (p. 577). Water values are computed for a "presumed stationary future system state" (p. 573).

## Method
- **Model type:** SDP with a discretised reservoir grid. Each stage–state decision problem is an LP (or MILP when the future-profit function is nonconcave) (pp. 573–576).
- **How uncertainty is represented:** discrete **Markov chain** over weekly average energy price and weekly total inflow, extended with a binary "environmental state". Construction procedure (p. 575, Sec. 2.3):
  1. historical or forecast inflow and price data as input;
  2. fit an autoregressive model with serial correlation in inflow and cross-correlation between inflow and price;
  3. sample 10,000 scenarios;
  4. K-means clustering per week gives the nodes (each node = one inflow value + one price value);
  5. transition probabilities = share of scenarios moving between nodes from one week to the next.
  The environmental state doubles the nodes in the relevant weeks; transitions are multiplied by the probability of inflow above/below a threshold (p. 575, Fig. 2).
- **Solution method:** backward recursion over all stages, reservoir states and stochastic states (Algorithm 1, p. 576). The expected future profit for two reservoirs is a 2-D piecewise-linear interpolation (triangle method) with SOS2 constraints, needed only if the function is nonconcave; a concavity check before each subproblem lets most problems be solved as LPs (pp. 574, 577). **End of horizon:** the algorithm iterates until water values in the last and first stage converge (cyclic, steady-state water values) (p. 575; p. 577).
- **Key modelling choices and assumptions:**
  - Risk-neutral price taker maximising profit (p. 573).
  - Production = Σ_d η_{h,d}·q_{h,d}: piecewise-linear efficiency per discharge segment, no head dependence (eq. 2, p. 574).
  - Small spillage penalty; soft penalty below 10% reservoir filling "to represent risk-aversion of the producer" (pp. 573–574, eq. 6).
  - Environmental rule (pp. 574–575, eqs. 16–19): no discharge (except minimum flow) once the restriction is active until the reservoir reaches a threshold; then storage must stay above it; for a later period storage may not decrease.

## Data / case
- 58 historical inflow years; prices from the EMPS model for a low-emission 2030 European dataset (p. 577).
- Reservoir grid: 20 equidistant points per reservoir → 400 storage combinations; 10 Markov nodes per stage (20 in weeks with the environmental state) (p. 577).
- Penalties: spillage 10⁻³ €/(m³/s); drawdown below 10% ≈ 150 and 580 €/Mm³ for lower and upper reservoirs (p. 577).
- Environmental rule for the lower reservoir: activation by above-average inflow from week 15 (at the latest week 19), active until week 32 or until 146 Mm³; no decrease weeks 33–35; minimum discharge 3 m³/s (p. 577).
- Julia/JuMP + CPLEX 12.10; one iteration without the rule: 208k subproblems in ≈ 440 s; with the rule: 224k in ≈ 1,860 s (≈ 40% MILP); convergence in 16–20 iterations with criterion 10⁻³ €/Mm³ (p. 578).
- Simulation: 1,000 scenarios randomly drawn from the sampled scenarios, weekly decision problem with SDP water values as end-of-week value (pp. 577–578).

## Key findings
- (p. 578) Without the rule, water values are non-increasing in storage, which "will always be the result from linear hydropower scheduling models where the expected future profit is a concave function". High at low storage (risk of emptying), zero when spilling.
- (p. 578, Fig. 4–5) With the rule, water values sometimes increase with storage: the expected future profit is nonconcave. The largest changes are in weeks 18–32 and propagate back to week 1.
- (p. 578) Upper-reservoir water values hardly change: it does not pay to release more from upstream to reach the threshold sooner (case-specific).
- (p. 578) In ≈ 85% of scenarios the threshold is reached before week 33; early activation by high inflow occurs in 50% of scenarios but has muted economic effect.
- (p. 580, Table 1) Annual profit falls by ≈ 72 k€ (0.77%); in weeks 19–35 profit falls by ≈ 17% (406 k€), but annual generation is almost unchanged (−0.11%). The loss comes from a lower realised price, not lower sales.
- (p. 580) SDP scales poorly with more reservoirs because of the state-space discretisation.

## Strengths
- Very transparent description of how a joint price–inflow Markov chain is built from data (AR model → sampling → K-means → counted transitions), directly comparable with our approach.
- Shows how a cyclic (first-stage = last-stage) water-value convergence handles the end-of-horizon problem.
- Out-of-sample-style evaluation by simulating the water-value policy on 1,000 scenarios.

## Weaknesses / limitations
- Small system (two reservoirs) by necessity of SDP; coarse uncertainty (10 nodes) and time resolution (3 × 56 h) by the authors' own choice (p. 577).
- No head effects, no reserves, no pumping. Prices come from a model (EMPS), not market data.
- Simulation scenarios are drawn from the same sampled set used to build the Markov chain, so it is not an independent out-of-sample test.
- Economic results are sensitive to price assumptions (p. 580).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method: building the price–inflow Markov chain (clustering + counted transitions) | 5-step procedure: AR model, 10,000 samples, K-means per week, transition counting | p. 575, Sec. 2.3 |
| Method: inflow–price correlation in hydro systems | "inflow and price tend to be negatively correlated in hydro-dominated systems" | p. 575, Sec. 2.3 |
| Model: end-of-horizon water value / steady state | Iterate until water values in last and first stage converge | p. 575, Sec. 2.4; p. 577 |
| Theory: water values non-increasing in storage under convexity; nonconvexity breaks this | Explanation and figures | p. 578, Sec. 3.2, Figs. 4–5 |
| Theory/Lit. review: SDP vs SDDP trade-off (nonconvexity vs dimensionality) | Discussion of SDDP, combined SDP/SDDP (Gjelsvik et al. 1999), SDP, SDDiP | pp. 572–573, Sec. 1; p. 580, Sec. 4 |
| Model: soft minimum-reservoir penalty for risk aversion | 10% filling penalty, values | pp. 573–574, eq. 6; p. 577 |
| Case-study design: Markov nodes (10), grid (20 points), 3 × 56 h price periods | Parameter choices and run times | pp. 577–578 |
| Evaluation: policy simulation on 1,000 scenarios | Simulation set-up | pp. 577–578, Sec. 3.3 |

## Useful quotes (with page numbers)
> "The transition probabilities are determined by counting the share of scenarios transitioning between the different nodes from one week to the next." (p. 575)

> "To account for end-of horizon effects, an iterative approach is used until the water values in the last and first stage converge." (p. 575)

## Follow-up references to check (backward snowballing)
- [10] Gjelsvik, Belsnes & Haugstad (1999), combined SDP/SDDP for medium-term scheduling under spot-price uncertainty, PSCC.
- [8] Helseth & de Melo (2020), scheduling toolchains in hydro-dominated systems, SINTEF report (hdl 11250/2672581).
- [17] Pereira-Bonvallet et al., hydrothermal scheduling with non-convex irrigation constraints (SDDP approximation).
- [20] Helseth, Mo & Hågenvik (2020), nonconvex environmental constraints via SDDiP, PMAPS.
- [18] Helseth, Fodstad, Askeland, Mo, Nilsen, Pérez-Díaz, Chazarra & Guisández (2017), "Assessing hydropower operational profitability considering energy and reserve markets", *IET Renew. Power Gener.* 11(13):1640–1647. SDP with reserves, and the water-value calculation that Schaffer follows (p. 577). **High priority for our market-participation section.**
- [31] Guisández et al. (2020), should environmental constraints be considered in LP-based water value calculators?, *IJEPES* 117.

