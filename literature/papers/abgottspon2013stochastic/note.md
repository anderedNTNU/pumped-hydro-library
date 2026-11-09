---
bibkey: abgottspon2013stochastic
title: "Stochastic scheduling for a price-maker hydro producer considering forward trading"
authors: "Hubert Abgottspon, Göran Andersson"
year: 2013
venue: "2013 IEEE Grenoble Conference (IEEE PowerTech 2013), pp. 1–6"
peer_reviewed: true
methods: [sdp, heuristics-simulation]
review_sections: [market-participation, modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "SDP with hourly quadratic recourse for a price-maker Swiss PHS plant (240 MW gen / 46 MW pump / ~200 GWh) trading day-ahead and peak forwards; forward trading raises simulated annual profit ~20% (24 vs 20 M€)."
---

# Price-maker PHS scheduling with forward trading (Abgottspon & Andersson, 2013)

> **Page convention.** IEEE proceedings pages 1–6 = PDF pages 1–6.

## Research question / purpose
Propose a tractable model for the bidding problem of a **price-maker** pumped-storage hydro producer with seasonal inflows, over a one-year horizon, choosing between own production/pumping, the **day-ahead** (pool) market and **forward contracts**, under stochastic inflows; and show how the results (water values and optimal forward bids) can be used as **decision support** (p. 1). Price influence is modelled by a **linear price–quantity dependency** instead of a market-clearing/game model, which keeps the problem tractable (p. 1).

Stated contributions (pp. 1–2): (i) a price-maker formulation of the bidding problem, considering day-ahead and forward markets, easily applicable to hydro self-scheduling; (ii) a one-year simulation of the bidding process in a realistic setting.

## Setting
- **System:** realistic Swiss Alpine PHS plant, two hydraulic stages (p. 3): stage 1 = large upper basin (seasonal storage) and much smaller lower basin, with **two turbines and two pumps** between them; stage 2 = two turbines discharging from the smaller basin. Both basins receive inflows from precipitation and glaciers. **Installed generation 240 MW, pumping 46 MW, total storage ≈ 200 GWh (≈ 100 million m³)** (p. 3).
- **Markets:** hourly **day-ahead** (pool) market and **forward contracts** (OTC, based on standard power futures with financial settlement); peak products used since the plant mostly runs in peak hours; **EEX Phelix German peak futures** prices as forward bid prices (pp. 3–4). Ancillary-services market mentioned as available (p. 3) but **not modelled**. Producer is a **price-maker**: both pool and forward prices depend linearly on traded amount (Fig. 3, p. 3; p. 4).
- **Horizon and resolution:** 1 year, start 1 April 2009 (p. 4). **Stage length varies with available forward products**: daily stages for the first month, then weekly and monthly stages (p. 3; Fig. 1, p. 2); **hourly** intrastage recourse steps (p. 3).

## Method
- **Model type:** risk-neutral multistage stochastic program solved by **SDP** (eq. 1, p. 2): profit-to-go Φ_{t,x} = max ½yᵀHy + yᵀc_t + E_ξ[Q_{t,x,ξ} + Φ_{t+1,x}], with y = forward bid (MW), quadratic because forward prices are linear in quantity. Recourse Q_{t,x,ξ} is a **deterministic QP** (eq. 2, p. 3) with hourly production, pool and basin variables, technical and financial equality constraints (deliver contracted energy) and time-varying bounds (e.g. maintenance).
- **Decision structure (p. 2):** forward contracts are **here-and-now** at the start of each stage, without knowledge of inflows (forward prices known); within the stage, hourly **wait-and-see** decisions with perfect information: production decisions (technical constraints) and pool decisions (meet forward obligations, bid production in DA). Production/pumping are **not in the objective**: the model chooses between generating from stored water or buying energy in the DA market (p. 2).
- **How uncertainty is represented:** random data ξ = **water inflows** (Table I, p. 3; p. 2), estimated from historical data, in both basins (p. 3). DA prices are taken from an **hourly price forward curve (HPFC)** built by the industry partner, arbitrage-free to futures (p. 4), with linear price impact. Note: the abstract says "stochastic prices" (p. 1) and the simulation step 1 says "stochastic spot prices (out of HPFC)" (p. 5), but the model description treats only inflows as random — how price stochasticity enters is **not specified** (unverified).
- **Solution method:** discretise basin filling (state, upper seasonal basin only) and discharge amount → recursive shortest-path problem (Fig. 2, p. 3); for each filling find the optimal discharge and forward amount; "embarrassingly parallel" (p. 4). Water values = derivative of profit-to-go w.r.t. basin filling (p. 3–4). Forward simulation applies the optimal decisions from a starting filling to get expected basin levels and the forward bids at those levels (p. 3).
- **Key modelling choices and assumptions:**
  - Only the seasonal basin is the SDP state; the small lower basin is a state only inside the hourly recourse (p. 3).
  - Linear price dependency estimated "by experience or historical data", held **constant over all stages** (p. 4); without price dependency there would be little incentive to trade forwards (p. 4).
  - **End-of-horizon water has no value**; optimisation starts with empty basins on 1 April (Alpine seasonality: high inflows late spring/summer, none in winter) (p. 4).
  - Forward amount discretised into **11 values** (p. 5).
  - Risk neutral; financial and operational risk not considered explicitly (footnote 2, p. 6).
  - Head effects / efficiency curves: not described in the model; the simulation heuristic must handle "correct efficiencies" (p. 4) (unverified whether head dependence is modelled).
- **Simulation of the bidding process (pp. 4–5, Fig. 7):** monthly receding horizon from 1 April 2009 for one year: (1) SDP gives water values and optimal forward bids for all discretised fillings; (2) first forward simulation (expected prices and inflows, no stochasticity) gives expected basin levels and the bids there; (3) second forward simulation with **actual historical spot prices and inflows** mimics operation for one month, giving realised basin level, remaining positions and profit. Hourly dispatch by heuristic: turbines fully on if water value < DA price, pumps fully on if water value > price, subject to technical limits (p. 4).

## Data / case
Swiss PHS plant above; EEX Phelix peak futures; HPFC from the industry partner (Axpo AG is project partner, p. 1); historical inflows and spot prices from 2009–2010. MATLAB R2012a + CPLEX 12.4; one optimisation run ≤ 4 min on a quad-core 2.3 GHz i7, 8 GB RAM; without exploiting the DP structure "it can easily take hours" (p. 4). Whole one-year simulation: 35 min (p. 5).

## Key findings
- (p. 4, Fig. 4) Profit-to-go strictly increasing over time and **concave in basin filling** within a stage; water values from the first stage can be compared directly with DA prices.
- (p. 5, Fig. 5) Example week: 100 MW peak forwards sold; full deployment of turbines/pumps often impossible because the small 2nd-stage basin limits both stages; on day 5 the forward obligation is not met from production and cheap energy is bought back in the DA market.
- (p. 5, Fig. 6) Optimal forward bids are sales (long producer hedging); positions shift to short as settlement approaches (Fig. 9, p. 6).
- (p. 6, Fig. 8) Upper basin used up to ~80% of capacity; acts as seasonal storage. Profit higher in summer than winter (non-storable inflows).
- (p. 6) **Total simulated profit 24 M€ with forward trading vs 20 M€ without → about 20% increase**; historical revenues were 20–30 M€, so the simulation is realistic.

## Strengths
- Real plant data (capacities, storage) and real market products (EEX peak futures, HPFC).
- Clear here-and-now (forward) vs wait-and-see (hourly DA + dispatch) separation.
- Shows a full monthly receding-horizon simulation with historical data, i.e. a policy evaluation, not just an optimisation result.
- Tractable price-maker representation (linear price impact → QP).

## Weaknesses / limitations
- Price uncertainty is not clearly modelled (inflows are the only random data in the formulation); the abstract's "stochastic prices" is not backed by a described price model.
- Linear price impact constant over time; estimated "by experience".
- Zero end-of-horizon water value; risk neutral.
- Only one simulated year (2009/10); 11-point forward discretisation.
- Some internal inconsistency: Fig. 6 caption says no bids are bought, while p. 6 says forwards were bought at the beginning (negative early profit, long positions in Fig. 9).
- No reserves, no head effects described, no configuration variation.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review 5.4: market participation beyond DA | DA + forward trading for a price-maker PHS; forward trading +~20% profit (24 vs 20 M€) | p. 1 (aims), p. 6 (result) |
| Lit. review 5.3: SDP for PHS with hourly recourse | Multistage SP solved by SDP with discretised basin; QP recourse; here-and-now vs wait-and-see | pp. 2–3, Sec. II, eqs. 1–2, Figs. 1–2 |
| Lit. review 5.5: example plant with fixed capacities | 240 MW generation, 46 MW pumping, ~200 GWh / 100 Mm³, two-stage Alpine PHS | p. 3, Sec. III |
| Model / theory: water values as opportunity cost, derivative of profit-to-go | Definition and use for comparison with DA price | p. 1, pp. 3–4 |
| Method: benchmark dispatch heuristic | Water value vs DA price rule; full turbine/pump deployment subject to limits | p. 4 (Sec. IV-A) |
| Method: rolling-horizon policy evaluation on historical data | Monthly receding horizon, two forward simulations, historical prices and inflows | p. 5, Fig. 7 |
| Model assumption contrast: end-of-horizon value | Residual water given no value, start at empty basin | p. 4 |
| Perspective (price-taker vs price-maker) | Example of price-maker modelling with linear price impact instead of market clearing | p. 1, p. 4, Fig. 3 |

## Useful quotes (with page numbers)
> "By nature hydro producers are in long position" (p. 1)

> "trading in the Forward market results to an increase of profit of about 20%" (p. 6)

## Follow-up references to check (backward snowballing)
- [9], [10] Baslis & Bakirtzis (2010, 2011), price-maker PHS mid-term stochastic scheduling with residual demand curves, IEEE TPWRS 26(4).
- [11] Flach, Barroso & Pereira (2010), long-term allocation of hydro for a price-maker, SDDP, IET GTD 4(2).
- [5] Conejo, Garcia-Bertrand & Carrion (2008), forward trading for an electricity producer.
- [7] Fleten et al. (2011), bidding hydropower generation integrating short- and long-term scheduling, PSCC.
- [8] Barquín & García-González (2000), water value in competitive markets: DP and game theory.
- [1] Abgottspon, Bucher & Andersson (2012), SDP for unified short- and medium-term planning, PMAPS.
- [4] Labadie (2004) — already in bib as `labadie2004`.

