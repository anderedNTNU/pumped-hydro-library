---
bibkey: alic2023optimal
title: "Optimal price-based scheduling of a pumped-storage hydropower plant considering environmental constraints"
authors: "Asja Alic, Linn Emelie Schäffer, Marco Toffolon, Vincenzo Trovato"
year: 2023
venue: "Energy Systems (Springer), doi:10.1007/s12667-023-00614-y (online first)"
peer_reviewed: true
methods: [sdp, uncertainty-modelling, hydro-production-function, heuristics-simulation]
review_sections: [modelling-phs-plants, market-participation, reservoir-sizing-capacity, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Medium-term SDP (1 year, 52 weekly stages, 3-h sub-intervals) for a Norwegian cascade with a retrofitted 38 MW pump. Price and inflow form a joint 5-state-per-week Markov chain from K-means clustering, close to our uncertainty model. Adding the pump raises median revenue by only +2.35% (energy only, price-taker); a weekly resolution overestimates revenue when state-dependent environmental constraints bind."
---

# Price-based PHS scheduling with environmental constraints (Alic et al., 2023)

> **Page numbers:** the repo PDF is the online-first version, with no journal pagination. Page numbers below are **PDF pages 1–45**. Update them if the issue pagination is added to Zotero.

## Research question / purpose
How much does adding a **pumping unit** to an existing Norwegian cascade increase energy production and revenue? And how do three environmental constraints affect operation and revenue? The constraints are (i) minimum environmental flow (MEF), (ii) ramping limits on reservoir water levels, and (iii) a state-dependent constraint on maximum water abstraction (SCWA, through both turbines and pump) (abstract, p. 1; contributions, pp. 8–10).

A second question is methodological: is a **weekly-stage** medium-term model accurate when constraints depend on the state? The paper compares it with a forward simulation using **daily** stages (Sect. 4, pp. 23–26). It also tests how the granularity of the state discretisation affects accuracy and run time (Sect. 5.2.4, pp. 38–40). The model extends Schäffer, Helseth and Korpås (2022, Renewable Energy), an SDP with state-dependent discharge constraints for two conventional plants (p. 8).

## Setting
- **System:** a cascade of two plants, Rosskrepp–Kvinen in the Sira-Kvina watercourse, southern Norway (pp. 26–27).
  - **Upper plant (Rosskrepp, reservoir Rosskreppfjorden):** regulation volume 684.10 Mm³; Francis turbine 38 MW, 58 m³/s. It cannot pump today, so the study models a **hypothetical retrofit** to PSHP with 38 MW in both modes (pp. 27, 29).
  - **Lower plant (Kvinen, reservoir Øyarvatn):** regulation 104.10 Mm³; Francis turbine 80 MW, 90 m³/s. A conventional HPP (p. 27).
  - The pump in the upper station lifts water from Øyarvatn to Rosskreppfjorden (p. 14).
- **Markets:** the plant is a **price-taker** in a "competitive energy market" and sells energy at wholesale prices (p. 17). **No reserves or ancillary services**; these are listed as future work (p. 42). Day-ahead is not named explicitly. Prices are weekly averages from the Markov model, spread over 3-h sub-intervals with a fixed scaling profile λ_{t,k} that gives a "generic daily pattern" (p. 18).
- **Horizon and resolution:** 1 year with **T = 52 weekly stages**, each split into **K = 56 sub-intervals of 3 h** (p. 11; p. 29). There is a daily-stage variant (Z = 7 days, I = 8 three-hour sub-intervals) for the forward simulation only (pp. 25–26; p. 35).

## Method
- **Model type:**
  - Medium-term **stochastic dynamic programming (SDP)** computes water values (WVs), followed by a **forward simulation (FS)** over Ns = 100 scenarios (Fig. 1; pp. 10–11, 14, 29).
  - Each stage problem (the "Scheduling Algorithm", Eqs. 10–29) is an optimisation over the 56 sub-intervals. The expected future revenue α_{t+1} is a piecewise-linear interpolation over the discretised two-reservoir volume grid, using **SOS2** weighting variables (Eq. 10a, p. 18). The stage problem is therefore a MILP, or at least needs SOS2 branching (unverified whether the authors call it a MILP).
  - Solved in Julia 1.7.3 / JuMP / CPLEX (p. 30).
- **How uncertainty is represented:** a **discrete Markov chain** over joint (weekly inflow, weekly average price) states, following [20] (p. 12):
  - The input is several years of historical weekly inflows and weekly average prices for the same weeks.
  - The serial correlation of inflows between adjacent weeks and the inflow–price cross-correlation are estimated, and an **autoregressive model** generates **10,000 points per week**.
  - These are clustered with **K-means into L = 5 nodes** per week. Each node is a pair (inflow per reservoir, price), with the same price for both reservoirs.
  - **Transition probabilities** between weeks = share of sampled scenarios moving from node to node.
  - Data: inflows for 1981–2010 (30 years) from NVE. Prices from [34], "reflecting a potential 2030 power system in the Nordic scenario" (p. 29).
- **Solution method:**
  - **Backward SDP** over all discretised volume pairs (N = 25 points per reservoir, giving 625 pairs) and the 5 stochastic states (pp. 12, 29). WVs at T start at zero.
  - The algorithm iterates until the WVs at t = T and t = 0 differ by less than a tolerance (Eq. 2). The WVs from t = 0 become the next iteration's end values (Eq. 3), giving periodic yearly boundary conditions, i.e. an infinite-horizon formulation (p. 13). Tolerance is 10⁻³ (unit garbled in the extraction) (p. 29).
  - In the FS, each scenario is solved **deterministically week by week**: the week's inflow and price are known at the start of the stage, and decisions use the optimal WVs (pp. 11, 14).
- **Key modelling choices and assumptions:**
  - **Head effects neglected:** net head variations relative to the gross head are ignored, which the authors call common in medium-term models. Turbine power is piecewise linear in discharge with segment slopes (Eq. 15). Pump power vs pumped flow is a **concave piecewise-linear** curve with E segments (Eqs. 4–6, 17–18; Fig. 4; pp. 15–16, 20).
  - **Machine type:** grid connection and machine type are ignored. The flexible pump behaves more like a **fully-fed or doubly-fed (variable-speed)** machine than a fixed-speed pump, which gives an "upper bound" on flexibility (p. 14).
  - **Cavitation proxy:** pumping is banned for the whole week if the lower-reservoir volume at the end of the previous week is below a threshold (Eq. 7/19, p. 16; Check 1, Fig. 6).
  - **MEF** goes through its own bypass route b_{h,k}, with a slack variable (Eqs. 8, 20). **Ramping** is written as limits on volume change per 3-h step, converted from ±0.03 m water-level limits through 4 volume bands. Ramping can be violated at a penalty (Eqs. 9, 29; Table 3; pp. 17, 22–23, 29–30).
  - **SCWA** on the lower reservoir in weeks 23–38 (Eqs. 21–28; Check 2, Fig. 7; pp. 21–22): no turbine or pump abstraction while the volume is below V_lim = 87.44 Mm³ (84% of capacity). Once the threshold is reached, the reservoir must stay above it. These are **if-conditions evaluated on the start-of-stage state** before the stage problem is solved. This non-convex logic is why SDP is used instead of SDDP (p. 7).
  - Penalties: spillage C_S = 1 M[€]/m³/s; ramping slack C_C = 0.1 M[€]/Mm³. The currency symbol is lost in the text extraction (p. 29).
  - Water values are defined as the marginal or opportunity value of stored water (€/Mm³). They decrease with storage because of spill risk and increase at low storage because of the risk of emptying (pp. 11–12).

## Data / case
- **Four cases** (Table 2, p. 28; p. 29):
  - **BC:** today's system with SCWA (turbines only) and MEF, no pump.
  - **Case A:** BC plus a 38 MW pump, with SCWA extended to pumping.
  - **Case B:** BC plus ramping on the upper reservoir.
  - **Case C:** Case A plus ramping on the upper reservoir.
- **Environmental settings** (Table 1, p. 28):
  - V_lim = 87.44 Mm³ in weeks 23–38.
  - MEF 0.5 m³/s in weeks 25–38 and 0.2 m³/s in weeks 39–42.
  - Ramping ±0.03 m per 3 h (taken from HYMO alteration parameters [35]) (p. 29).
- **Computation:** 100 FS scenarios, the same in all cases. Run on an Intel i5 with 8 GB RAM. Run time grows with discretisation from 5×5 to 25×25 (Fig. 20, p. 40; the largest case is roughly 20+ h judging from the plot, unverified).
- **Not included:** investment costs (p. 30; p. 35).

## Key findings
- (pp. 30–31, Fig. 12) **Median annual energy production vs BC:**
  - Case A: **+9.34%**
  - Case B: **−0.08%**
  - Case C: **+6.74%**

  "Energy production" is **gross** turbine output and leaves out pumping load, so recirculated water counts again.
- (p. 31) **Pumping consumption:**
  - Case A: 0.044 TWh to pump 182.68 Mm³ on average.
  - Case C: 0.0297 TWh for 122.53 Mm³.
- (pp. 31–32, Fig. 13) **Median net annual revenue vs BC:**
  - Case A: **+2.35%**
  - Case B: **−1.01%**, because ramping shifts production from high-price to lower-price periods, consistent with Niu and Insley (2013).
  - Case C: **+0.47%**

  "The benefits arising from the use of a pumping system overcome the limitations imposed by the ramping constraints" (p. 32).
- (pp. 32–34, Fig. 14) Without ramping constraints, water-level changes above 0.05 m per 3 h are frequent: 5.25% of the time in BC and 11.11% in Case A (positive). Levels rise by more than 0.20 m and fall by up to −0.15 m in 3 h. With ramping, there are still some violations, caused by snowmelt inflow (the penalty is cheaper than spilling) and by coarse volume bands, since the band is chosen from the start-of-week volume. The fix proposed is more bands or the actual bathymetry (pp. 32–33).
- (p. 34) Cumulative volume variation is higher with a pump: 524.4 Mm³ in Case A vs 419.8 Mm³ in BC.
- (p. 35) The results cover operational revenue only. A full investment analysis would need machinery, civil works (tunnels, enlarged power station), permits and monitoring.
- (pp. 35–38, Fig. 15; Table 4) **Daily-stage FS vs weekly** (Case C):
  - **Week 23** (first week of SCWA): energy **−20.59%**, revenue **−24.21%**.
  - **Week 34** (SCWA long active): energy −8.06%, revenue −6.55%.

  "The weekly model might overestimate the total energy production and revenues", because the state is known less precisely when state-dependent constraints change the problem (p. 38). The daily variant **interpolates WVs linearly** between weekly boundaries (Eqs. 30–31, pp. 25–26).
- (pp. 38–40, Figs. 19–20) A finer volume discretisation improves interpolation accuracy (performance index, Eq. 33) at a rising computational cost.
- (p. 7) The authors note that SDDP is the most effective method for medium- and long-term hydropower scheduling (citing Hjelmeland et al. 2018, SDDiP), but choose SDP because of the non-convex state-dependent constraints. SDP suits "small systems involving a limited number of state variables".
- (pp. 6–7) Taxonomy: long-term models are 1–10 years and stochastic; medium-term models run from a few months to a year under inflow and price uncertainty; short-term models cover days to weeks and are deterministic.
- (p. 42) Future work: a full investment analysis; a **price-maker** setting; detailed electrical-machine technology (fixed vs variable speed); and **ancillary services or frequency-response revenue**.

## Strengths
- A real Norwegian system with realistic, regulator-imposed environmental constraints (SCWA, MEF), implemented carefully.
- **Joint price–inflow Markov chain built by K-means clustering of simulated weekly samples, with counted transitions.** Methodologically almost the same as our Markov-state construction, and a direct precedent for it.
- Weekly stages with intra-week sub-intervals is the same stage structure as ours. The paper is explicit about water values as marginal and opportunity cost.
- The weekly vs daily comparison measures the error caused by weekly state disclosure. This is useful for discussing the limitations of our weekly stages.
- Honest about scope: no investment costs, energy-only, price-taker.

## Weaknesses / limitations
- **SDP on a discretised grid** (2 reservoirs × 25 points) does not scale. Run time is hours, even for this small system (Fig. 20).
- **Only 5 Markov states per week**. Prices are weekly averages spread with a **fixed** intra-week profile, so intra-week price volatility (the main driver of PHS arbitrage) is not stochastic. This probably explains the small +2.35% revenue gain (our interpretation, not stated by the authors).
- One price dataset, a potential 2030 Nordic scenario from a research project. The price data are only loosely documented (refs [34], plus profile values "courtesy of NTNU", p. 18).
- **No reserve markets** and no intraday. Head effects and efficiency variation with head are neglected (constant gross head).
- **In-sample evaluation:** the FS uses scenarios with weekly inflow and price known at the start of each week. The paper does not state whether these scenarios come from the same Markov model or the same historical data, i.e. whether evaluation is out of sample (unverified). There is no explicit terminal or remaining water value in reported revenues; periodic boundary conditions are used instead.
- Pump capacity is fixed at 38 MW, equal to the turbine, with no sensitivity analysis on pump size, reservoir size or storage duration.
- "Energy production" counts gross turbine output, which inflates the energy gain from pumping (+9.34%) relative to the economic gain.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (PDF page/section) |
|---|---|---|
| Model: Markov-chain construction by clustering | AR model, 10,000 points per week, K-means into 5 nodes, transition probabilities by counting | p. 12, Sect. 2.2 |
| Model: weekly stages with intra-week resolution | T = 52, K = 56 three-hour sub-intervals | pp. 11, 29 |
| Model: weekly price to intra-week profile | Weekly average price × scaling factor λ_{t,k} | p. 18 |
| Model: water value definition | Marginal or opportunity value of stored water; shape vs storage level | pp. 11–12 |
| Model: pump and turbine curves, head neglected | Concave piecewise-linear pump power; constant gross head; variable-speed-like flexibility | pp. 14–16, Sect. 3.1 |
| Model: end-of-horizon handling | Periodic yearly boundary (WV at T = WV at 0), iterated to convergence | p. 13, Eqs. 2–3 |
| Model: price-taker assumption | "price-taker agent operating in a competitive energy market" | p. 17 |
| Method: why SDP vs SDDP | SDDP called most effective for medium- and long-term scheduling; SDP chosen for non-convex state-dependent constraints; SDP limited to few states | p. 7, Sect. 1.1 |
| Theory/background: long-, medium-, short-term scheduling taxonomy | 1–10 years; months to 1 year; days to weeks (deterministic) | pp. 6–7 |
| Lit. review (modelling PHS): Norwegian PHS retrofit, environmental constraints | MEF, ramping, SCWA formulations; Rosskrepp–Kvinen case | pp. 16–22, 26–29 |
| Lit. review (market participation): energy-only, no reserves | Price-taker energy arbitrage; ancillary services as future work | pp. 17, 42 |
| Lit. review (sizing/capacity): value of adding pump capacity | Median revenue +2.35% (A), +0.47% (C); no investment analysis | pp. 30–32, 35 |
| Discussion/limitations: weekly resolution bias | Daily-stage FS gives −24.21% revenue (week 23), −6.55% (week 34); weekly model may overestimate | pp. 35–38, Sect. 5.2.3 |
| Discussion: computational burden of grid SDP | Run time grows with N² discretisation; hours on an i5 | pp. 38–40, Fig. 20 |
| Background (PHS tech): round-trip efficiency up to about 80% | Cites Pitorac et al. (2020) [6]; secondary source | p. 5 |
| Background (environment): PHS effects on reservoirs | Level fluctuations, stratification, ice cover | pp. 5–6 |

## Useful quotes (with page numbers)
> "the hydropower system is assumed to be a price-taker agent operating in a competitive energy market" (p. 17)

> "the results confirm that the weekly model might overestimate the total energy production and revenues from the hydropower system." (p. 38)

> "this paper only evaluates potential operational benefits without carrying out a full investment analysis" (p. 30)

## Follow-up references to check (backward snowballing)
- [20] Schäffer, Helseth, Korpås (2022), "A stochastic dynamic programming model for hydropower scheduling with state-dependent maximum discharge constraints", *Renewable Energy* 194: the base model and full Markov-chain description.
- [21] Hjelmeland, Zou, Helseth, Ahmed (2018), "Nonconvex medium-term hydropower scheduling by SDDiP", *IEEE Trans. Sustain. Energy*: SDDiP for non-convexities.
- [23] Helseth et al. (2017), *IET RPG*, "Assessing hydropower operational profitability considering energy and reserve markets" (check whether this is `helseth2017` in our bib).
- [24] Pérez-Díaz et al. (2020), medium-term scheduling with price-maker aFRR participation, *EPSR*: reserves in an SDP framework.
- [29] Helseth, Mo, Hagenvik, Schäffer (2022), "Hydropower scheduling with state-dependent discharge constraints: an SDDP approach", *JWRPM*.
- [6] Pitorac, Vereide, Lia (2020), "Technical review of existing Norwegian pumped storage plants", *Energies*: background for PHS technology and Norway.
- [14] Schäffer et al. (2020), EEM review on modelling environmental constraints.

