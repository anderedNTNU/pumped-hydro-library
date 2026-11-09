---
bibkey: chancelier2026optimal
bibkey_provisional: true
title: "Optimal operation and valuation of electricity storage systems in intraday markets"
authors: "Jean-Philippe Chancelier, Michel De Lara, Tanguy Lindegaard, François Pacaud, Teemu Pennanen, Ari-Pekka Perkkiö"
year: 2026
venue: "Computational Management Science 23, article 16 (25 pp.)"
peer_reviewed: true
methods: [sddp-markov-chain, risk-averse-cvar, uncertainty-modelling]
review_sections: [reservoir-sizing-capacity, market-participation]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/114_Chancelier_2026_Optimal_operation_and_valuation_of_electricity_storage_systems_in_intraday_markets.pdf
takeaway: "Battery trading over 24 hourly intraday periods as a convex stochastic control problem with explicit cash account, solved by Markov-chain SDDP (SDDP.jl) after Gauss-Hermite quadrature discretisation of an AR(1) DA-ID spread; storage is valued by utility-indifference pricing, which rises with capacity, charging speed and price volatility and saturates for risk-averse agents."
---

# Storage operation and indifference valuation with Markov-chain SDDP (Chancelier et al., 2026)

_**Version and page mapping:** published open-access version (CC BY 4.0), Computational Management Science (2026) 23:16, received 19 April 2025, accepted 27 January 2026, published online 9 April 2026. Pages are "Page X of 25" = PDF page X._

## Research question / purpose
- Develop models and computational tools for the **optimal operation and valuation** of batteries and other storage under uncertain prices, where valuation reflects the owner's financial position, market views and risk preferences (pp. 1-2).
- Valuation via the **indifference pricing principle**: the maximum amount an agent would pay to rent the storage for [0, T] without lowering expected utility (pp. 5-6).

## Setting
- **System:** generic storage with capacity X̄e, max charge/discharge speeds, charging function c(u) with separate charge/discharge efficiencies (c+ = 0.95, c− = 1.05), proportional leakage l (set to 0) (pp. 5, 18).
- **Markets:** intraday (France), energy traded just before gate closure for each delivery period at best bid/ask; bid-ask spread δ (set to 1 EUR/MWh, not empirical) (pp. 4-5, 7-8, 18). Imbalance market discussed but not traded (p. 4).
- **Horizon and resolution:** one day, T = 24 hourly stages (p. 18); 15-min products from 30 Sept 2025 noted (p. 3).

## Method
- **Model type:** maximise E[v(terminal cash)] subject to cash and energy dynamics, storage and speed bounds (problem (3), p. 5). Exponential utility v(z) = (1/γ)(1 − e^(−γz)) with risk aversion γ (eq. 6, p. 6).
- **Indifference price:** for exponential utility, the price follows from a **single** solve of the storage problem: π = −(1/γ) ln(1 − γ φ(0, X̄e)) (Proposition 1, pp. 6-7).
- **Convex reformulation:** with linear bid/ask costs and piecewise-linear charging, the problem becomes linear by splitting purchases and sales (11a-11e, p. 10). The relaxation that allows simultaneous charging and discharging (12) is **exact** if s−/c− ≤ s+/c+ (bid price over discharge factor not above ask price over charge factor), and a feasible non-simultaneous solution can be constructed that is at least as good (Proposition 2, pp. 11-12). _Our note: with zero spread and negative prices this condition can fail, i.e. simultaneous charge/discharge could then be "profitable" in the LP; relevant to pump/turbine exclusivity in our LP._
- **How uncertainty is represented:** mid-price s_t = DA price s̄_t + ξ_t, with ξ an AR(1) process with Gaussian innovations, fitted on 8,760 hourly DA vs ID1 observations for France 2024 (eq. 8, pp. 8-9; Fig. 1). Zero intercept supported by a high p-value (p. 9; Table 1, slope estimate about 0.48 as extracted, **(unverified: table garbled in text extraction)**). The Markov process is discretised into a finite-state Markov chain by **conditional Gauss-Hermite quadrature** (Tauchen and Hussey 1991 style), with transition probabilities from density ratios (Sec. 4.2, pp. 15-16).
- **Solution method:** SDDP for Markov-chain problems (Infanger and Morton 1996; Philpott and de Matos 2012; Löhndorf and Shapiro 2019), via SDDP.jl; general decision-hazard-decision format (controls before and after observing the stage noise) supported in theory (Sec. 3-4, pp. 9-17).
- **Key modelling choices and assumptions:** explicit cash account (lending/borrowing) instead of discounting, giving the price in money at purchase time and avoiding the "asset-backed trading strategies" of Löhndorf and Wozabal (2021) (p. 3); small trader at best bid/ask (p. 7).

## Data / case
- France 2024 day-ahead and ID1 index (hourly); capacity 1 MWh, risk aversion γ = 0.03 for convergence tests, charging speed ρ = U/X̄e = 0.4 (and 1) (pp. 8, 19-20).

## Key findings
- (p. 17, Table 2) Time for 1,000 SDDP iterations grows roughly linearly with quadrature points: N = 1: 201 s, 2: 44 s, 4: 77 s, 8: 144 s, 16: 270 s, 32: 820 s, 64: 1,820 s (p. 19).
- (p. 19, Fig. 3) N = 1 (deterministic) converges in fewer than 10 iterations; for N ≥ 4 the SDDP bounds almost coincide.
- (pp. 19-22, Fig. 4) Out-of-sample evaluation on 10,000 paths from the **continuous** AR process, using the control of the **nearest Markov state**; out-of-sample values rise towards the SDDP bound with N, marginal gains above N = 8; in-sample (on the chain) values are also reported.
- (p. 22, Fig. 5) Higher risk aversion thins the left tail of terminal wealth; risk-averse agents cycle less; the effect is larger for faster batteries.
- (pp. 22-23, Fig. 6) Indifference price increases with capacity but **saturates for risk-averse agents** (they avoid large stored positions because of price risk).
- (p. 23, Fig. 7) Value increases with charging speed, more strongly for less risk-averse agents.
- (p. 23, Fig. 8) Higher price volatility raises the storage value for all risk-aversion levels.

## Strengths
- Rigorous convex-analysis foundation (existence, Markovian Bellman functions, optimality) for Markov-chain SDDP on storage problems (Theorems 3-5, pp. 14-15).
- Clear recipe for a **valuation** metric of storage capacity derived from an SDDP policy, with risk preferences.
- Quadrature-based Markov discretisation plus out-of-sample testing on the continuous process: a transparent way to choose the number of Markov states.

## Weaknesses / limitations
- Toy case: 1 MWh battery, one day, one market, stylised efficiencies and spread not estimated from data (p. 18).
- One-dimensional price noise; no reserves, no DA decision (DA price taken as given).
- No comparison with simple benchmarks or with perfect foresight.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method: Markov-chain SDDP theory (Bellman functions depend on current Markov state) | Theorems 3-5 | pp. 14-15, Sec. 4.1 |
| Method: discretising a continuous price process into a Markov chain | Conditional quadrature, transition probabilities | pp. 15-16, Sec. 4.2 |
| Method: choosing number of Markov states | Bounds vs N, runtime vs N, out-of-sample convergence | pp. 17-22, Table 2, Figs. 3-4 |
| Method: out-of-sample policy evaluation | Nearest-Markov-state rule on continuous scenarios | p. 20 |
| Model: simultaneous pump/turbine in LP | Prop. 2 exactness condition for relaxing charge/discharge complementarity | pp. 11-12 |
| Lit review: storage sizing / valuation | Value vs capacity, charging speed, volatility, risk aversion | pp. 22-23, Figs. 6-8 |
| Lit review / theory: risk-averse storage operation | Exponential utility, indifference pricing | pp. 5-7, Sec. 2.3 |
| Lit review: SDDP vs MPC / HJB for storage | Argument that SDDP handles state constraints and uncertainty | pp. 2-3 |

## Useful quotes (with page numbers)
> "the valuation of a storage increases with the storage capacity. With higher risk aversion, however, the valuations seem to saturate for larger capacities." (pp. 22-23)

## Follow-up references to check (backward snowballing)
- Löhndorf and Wozabal (2021), gas storage valuation in incomplete markets with SDDP, EJOR 288.
- Picarelli and Vargiolu (2021), optimal operation of pumped hydro storage with state constraints (continuous time).
- Mégel, Mathieu and Andersson (2015), SDDP to schedule storage providing multiple services, PowerTech.
- Martinez Parra et al. (2024), two-timescale decision-hazard-decision formulation for storage usage values, arXiv 2408.17113.
- Pennanen and Perkkiö (2026), dynamic programming and dimensionality in convex stochastic control, Optimization Letters 20.
- Roald et al. (2023), survey of power-system optimisation under uncertainty (we have `roald2023`).

