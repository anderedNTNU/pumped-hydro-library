---
bibkey: helseth2016
title: "Optimal Medium-Term Hydropower Scheduling Considering Energy and Reserve Capacity Markets"
authors: "Arild Helseth, Marte Fodstad, Birger Mo"
year: 2016
venue: "IEEE Transactions on Sustainable Energy, 7(3), 934–942"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, uncertainty-modelling]
review_sections: [market-participation, modelling-phs-plants, electricity-markets, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/22_Helseth_2016_Optimal_medium_term_hydropower_scheduling_considering_energy_and_reserve_capacity_markets.pdf
takeaway: "Hybrid SDP/SDDP (price Markov chain + AR(1) inflow in SDDP) for a price-taking Norwegian watercourse selling day-ahead energy and week-ahead symmetric spinning reserve capacity; joint energy×capacity price nodes (3×3) built by clustering EMPS scenarios; reserve sales raise expected profit, change reservoir trajectories and (here) lower water values."
---

# Medium-term hydro scheduling with energy and reserve capacity markets (Helseth et al., 2016)

_PDF page 1 = journal p. 934. Tables I and II are images in the PDF and could not be extracted to text; their contents (market time sequence, profit numbers per case) are **not** reproduced here (unverified)._

## Research question / purpose
How should a profit-maximising, price-taking, risk-neutral hydropower producer schedule a multi-reservoir system over the medium term when it can sell **both energy (day-ahead/spot) and reserve capacity** in separate, sequentially cleared markets, and how do schedules and water values change compared with an energy-only market (abstract, p. 934)? Contributions over the authors' 2015 PowerTech paper [19] (p. 935):
1. stochastic (not deterministic) reserve-capacity prices, with serial and cross correlation to energy prices;
2. capacity sold **the week before** operation, under uncertain energy prices and inflows (sequential, Nordic-style decision order, not co-optimisation);
3. capacity sales enter as **state variables** in the decomposition and in the Benders cuts;
4. linear constraints that discourage reserve delivery below minimum output and that ensure enough water behind the turbines for committed up-regulation.

## Setting
- **System:** Norwegian watercourse with 7 reservoirs and 7 power stations, total 986 MW (p. 939, Fig. 3). Stations 4 and 5 have minimum output 70 MW and 50 MW. Station 5: 330 MW installed, 50 MW minimum, max reserve 33 MW (p. 941). No pumping mentioned.
- **Markets:** day-ahead energy + reserve capacity (symmetric, spinning). Section II (p. 936) describes Norwegian reserve markets as of 2015: FCR-N (49.90–50.10 Hz, droop for generators > 10 MVA; weekly and daily primary reserve markets since 2008), secondary reserves (arrangement from 2008, FRR-A from 2013), FRR-M with the RKOM option market (since 2000, up-regulation only, option payment). Reserve capacity "is generally traded the week before actual operation and before the decisions on energy trade" (p. 936). Case blocks mimic the weekly primary reserve market and the secondary reserve market (p. 939).
- **Horizon and resolution:** 2 years, weekly decision stages; each week 21 time steps; capacity sold in 6 blocks (weekday night/day/evening, weekend night/day/evening) (p. 939). Typical medium-term horizon 1–3 years (p. 936).

## Method
- **Model type:** multistage stochastic LP (eq. 1, p. 936), decomposed into weekly LPs (eqs. 2–12, p. 938). Objective (2): capacity revenue for next week's blocks + energy revenue for this week's time steps − cost of artificial water + future expected profit α_{p,t+1} for price node p.
- **How uncertainty is represented:**
  - *Prices:* weekly average energy price and weekly average reserve-capacity price as a **discrete Markov chain**. Per stage, scenarios of each price are clustered separately into N_E energy and N_C capacity clusters; a price node is a pair (energy cluster, capacity cluster); transition probability i→j = (#scenarios in both i and j)/(#scenarios in i) (p. 937, Fig. 1, method of Mo et al. 2001 [24]). Up to N_E·N_C nodes and (N_E·N_C)² transitions per week. Hourly/block prices from scaling weekly averages by pre-defined profiles (p. 938).
  - *Inflow:* weekly inflow per reservoir from a lag-1 autoregressive model, sampled in forward and backward passes; inflow is a state variable (enters the cut RHS) (pp. 936, 939).
  - Prices assumed **independent of inflow**; the hybrid method requires SDP-part and SDDP-part processes to be independent. Authors: for a single watercourse within a price zone it is hard to find significant weekly correlation between local inflow and spot price (p. 937).
- **Solution method:** hybrid SDP/SDDP (Gjelsvik et al. 1999 [13]): SDDP cuts per price node and week, price state handled as in DP because a price state would violate SDDP convexity (pp. 935, 937). Forward pass: sample inflows (AR(1)) and prices (Markov transitions), solve weekly LPs, pass state; gives lower bound. Backward pass: cuts from duals of water balance (14) and capacity obligation (15); averaged over inflow samples; upper bound from first-week problem (p. 939, eq. 16).
- **Key modelling choices and assumptions:**
  - State Z_{t+1} = [end-of-week volumes v_K, capacity sold for next week c_{b,t+1}, inflow I, energy price, capacity price] (p. 938).
  - Capacity obligation c_{b,t} is for the whole watercourse (5); allocation r_kh per station (6)–(7).
  - **Spinning** requirement (6): r_kh ≤ (1/β_h)·generation; β_h = max(P_min/R_max, 1) (13). Example: P_min 50 MW, R_max 33 MW → β = 50/33, so full reserve only when the station runs ≥ 50 MW (p. 938). Linear stand-in for binary unit commitment, which would break SDDP convexity.
  - Capacity: r + e/Δ ≤ P_max (7). **Water-for-reserve** constraint (8): v − η_S·r ≥ V_min, enough water to deliver up-regulation at the lowest efficiency for the entire period; authors note this is conservative for primary/secondary reserves (p. 938).
  - Piecewise-linear concave discharge–generation with segments in decreasing energy equivalent (4); no head dependence; no start-up costs (could be added as in [11]); no time delays (pp. 938, 940).
  - Artificial water at high cost (10⁶ €/Mm³) for complete recourse (pp. 938–939).
  - Reserves assumed symmetric and spinning; can be relaxed by separate up/down variables and dropping (6) (p. 939).
  - End-of-horizon value: a set of cuts from a few initial model runs, same for all cases; alternative is a longer horizon (p. 940).
  - Max 10% of each station's installed capacity can be committed to reserves (p. 939).

## Data / case
- Price scenarios: 80 scenarios from the EMPS fundamental model run on the Nordic system with 80 historical inflow years and reserve-capacity constraints per price zone (p. 940).
- Markov model: 9 price nodes per stage (3 energy × 3 capacity clusters). Because 80 scenarios are few for 9 nodes, transition probabilities were slightly adjusted to make the matrix ergodic (Nandalal & Bogardi, ch. 3.3) (p. 940).
- AR(1) inflow fitted to one inflow series of 80 historical years, normal errors (p. 940).
- SDDP settings: 200 forward scenarios per iteration, 12 discrete inflow error terms per stage in the backward pass (same samples for every price node), max 60 iterations; C++ with Gurobi 6.0 dual simplex; Intel i7, 32 GB; 55–60 h per run (p. 940). 400 forward scenarios gave slightly faster upper-bound stabilisation but similar results (p. 940).
- Cases (p. 940): A energy-only (c_b upper bound = 0); B energy + capacity without water constraint (8); C with (8). Final forward simulation with 1000 scenarios, profits adjusted for end-minus-start reservoir differences.

## Key findings
- (p. 940) Expected total profit increases when capacity can be sold (B, C > A); C slightly lower than B because of the volume constraint (8), which mainly affects small reservoirs 4 and 5 (impact underestimated since no time delays). Exact numbers in Table II (image, unverified).
- (p. 940) "A significant part of the profit from capacity sales" is obtained without changing the generation schedule, because stations have best efficiency below maximum and leave headroom up and down. Still, schedules for A vs B–C differ significantly, so constraints (6)/(7) bind often.
- (p. 940) Results are sensitive to energy and capacity prices but also to system characteristics such as efficiency curves and reservoir volumes.
- (p. 941, Fig. 5) With reserves (case C), reservoir 7 follows a slightly higher trajectory until the spring flood (~week 20), then water is used more aggressively to keep downstream generators spinning in the low-load season, giving lower levels in autumn/early winter. Same pattern in other large reservoirs.
- (p. 941, Fig. 6) Station 5 runs much of the time at 297 MW and at 50 MW (its minimum) in case C; the formulation (6) encourages running at 50 MW rather than 33 MW to deliver spinning reserves.
- (p. 941, Fig. 7) Water values = coefficients of the binding cut. In this case water values are generally **lower** with reserves (B, C) than energy-only, because capacity is withheld for up-regulation in periods where case A would run at maximum; with other prices they could be higher (extra water use from spinning).
- (p. 941–942) Conclusion: reserve capacity can be added as an extension of an energy-only medium-term model; its impact on water values can give better end-value settings for short-term tools. Linearisation error may significantly affect expected profits and operation, more so with spinning-reserve sales; future work should validate against a model with integer variables (p. 942).
- (p. 934) SDDP "seems to be the state-of-the-art method" for long- and medium-term scheduling in hydro-dominated regions.

## Strengths
- Treats both energy and reserve-capacity prices as correlated stochastic processes inside one Markov chain, built by clustering scenario samples, close to our approach.
- Represents the Nordic decision order (capacity the week before energy) explicitly, with capacity sales as state variables in the cuts.
- Simple, reusable linear constraints for spinning requirement and water availability for reserves.
- Large real watercourse; clear algorithm description; convergence discussion.

## Weaknesses / limitations
- Fully linear: no unit commitment, no head effects; authors flag linearisation error as possibly significant with reserves (p. 942). (helseth2017iet later quantifies it.)
- Only 80 price scenarios for 9 nodes, ergodicity patch needed; prices from a fundamental model, not market data.
- Prices assumed independent of inflow (justified only qualitatively).
- No out-of-sample test; evaluation by in-sample forward simulation of 1000 scenarios from the same model.
- Symmetric reserves, single generic capacity product; no reserve activation energy; no intraday.
- Long runtime (55–60 h), no parallelisation.
- Conventional (no pumping) watercourse.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review (market participation): energy + reserves in SDDP | Hybrid SDP/SDDP with stochastic energy and reserve-capacity prices; profit up with reserves | pp. 934–935, 940–942 |
| Lit review: SDDP is state of the art for hydro scheduling | "SDDP seems to be the state-of-the-art method…" | p. 934, Sec. I |
| Method: Markov chain from clustered scenarios | Separate clustering per stage, price node = (energy, capacity) cluster pair, count-based transitions | p. 937, Sec. III-B, Fig. 1 |
| Method: ergodicity fix for sparse transition matrices | Adjusted transitions when few scenarios per node | p. 940 |
| Method: why price is a Markov state, not an SDDP state | Price state violates convexity; handled by DP over nodes | p. 937 |
| Model: reserve constraints | Spinning (6) with β (13), capacity (7), water-for-reserve (8), reserve cap (11)–(12) | p. 938, Sec. III-D |
| Model: reserves sold week ahead as state variable | Capacity obligation in cuts (9), duals from (15) | pp. 937–939 |
| Background (electricity markets): Norwegian reserve markets ~2015 | FCR-N, FRR-A, FRR-M/RKOM; capacity traded week before energy | p. 936, Sec. II (dated) |
| Model: end-of-horizon value | Cuts from initial runs, or longer horizon | p. 940 |
| Results discussion: reserves and water values/trajectories | Higher before spring flood, lower in autumn; water values lower in this case | p. 941, Figs. 5–7 |
| Limitations: linearisation error with reserves | Warns error is larger with spinning reserves | p. 942 |

## Useful quotes (with page numbers)
> "Currently, SDDP seems to be the state-of-the-art method for solving the long- and medium-term scheduling problem in regions where hydropower is the dominant technology" (p. 934)

> "reserve capacity is generally traded the week before actual operation and before the decisions on energy trade" (p. 936)

> "the linearization error may significantly impact expected profits and system operation for certain systems" (p. 942)

## Follow-up references to check (backward snowballing)
- [13] Gjelsvik, Belsnes, Haugstad (1999), hybrid SDP/SDDP under spot price uncertainty, PSCC.
- [24] Mo, Gjelsvik, Grundt, Kåresen (2001), price modelling for hydro in liberalised markets, PowerTech (Markov-chain construction).
- [19] Helseth, Mo, Fodstad (2015), co-optimising energy and capacity sales, PowerTech.
- [18] Abgottspon & Andersson (2014), PHS with stochastic intrastage subproblems (we have `abgottspon2014`).
- [26] Nandalal & Bogardi (2007), DP-based reservoir operation (ergodicity).
- [20] Read (2010), co-optimisation of energy and ancillary services.

