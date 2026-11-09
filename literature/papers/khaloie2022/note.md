---
bibkey: khaloie2022
title: "Offering and bidding for a wind producer paired with battery and CAES units considering battery degradation"
authors: "Hooman Khaloie, Amjad Anvari-Moghaddam, Javier Contreras, Jean-François Toubeau, Pierluigi Siano, François Vallée"
year: 2022
venue: "International Journal of Electrical Power and Energy Systems 136, 107685"
peer_reviewed: true
methods: [multistage-scenario-trees, risk-averse-cvar, uncertainty-modelling, deterministic-lp-milp]
review_sections: [market-participation]
relevance: background
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/Innlimte_referanser_2026-10-29/khaloie2022.pdf
takeaway: "Three-stage stochastic MILP with CVaR for a 50 MW wind farm + 50 MW battery + CAES offering/bidding in sequential DA, intraday and balancing markets (Iberian data, 24 h, 3,600 scenarios): coordinated operation adds 13% expected profit over disjoint operation, 22% with demand-response purchases; battery degradation costs are small; no reserves."
---

# Wind + battery + CAES offering and bidding in DA and intraday markets (Khaloie et al., 2022)

_**Version and page mapping:** published Elsevier version (from ORBi UMONS repository). Article number 107685; the PDF's own page numbers 1-11 = PDF pages 1-11, used below._

## Research question / purpose
- Derive optimal DA offering (selling) and bidding (purchasing) curves plus intraday trades for a hybrid power generation system (HPGS) of a wind farm, a battery (BES) and a CAES unit, under price and wind uncertainty, with CVaR risk control and battery degradation cost (p. 1, pp. 3-4).
- Novelties claimed (p. 3): joint wind-CAES-BES operation in sequential markets; derivation of both offering and bidding curves in DA; CAES operating modes (charging, discharging, simple-cycle) as first-stage (non-scenario-dependent) decisions; intraday demand-response exchange (IDREX); degradation cost.

## Setting
- **System:** 50 MW wind farm; BES 50 MW charge/discharge, 5 blocks × 50 MWh (so 250 MWh, unverified reading of Table 1), efficiencies 95%/80% (charging/discharging assignment as extracted, unverified); CAES 100 MW compression, 150 MW expansion, storage 20 × 150 MWh (as extracted), heat rate 4.07 MBtu/MWh in discharging, 10.83 MBtu/MWh in simple-cycle (gas-turbine-only) mode, energy ratio 0.95 (unverified: Table 1 is garbled in the text layer; check the PDF) (Table 1, p. 7; parameters p. 6).
- **Markets:** DA, intraday and balancing (imbalance settlement with price ratios); IDREX demand-response purchases; bilateral DR contracts (pp. 3-6). No reserve capacity markets; providing balancing reserves is listed as future work (p. 10).
- **Horizon and resolution:** 24 hourly periods (pp. 6-8).

## Method
- **Model type:** three-stage stochastic MILP (p. 3): stage 1 = operating status of BES and CAES and DA offering/bidding curves (here-and-now); stage 2 = intraday trades and DR procurement after DA prices; stage 3 = balancing deviations after wind and all prices are known. Objective = expected profit + β·CVaR (eq. 1, p. 4; CVaR constraints 2-4, p. 4). Non-decreasing offer curves and decreasing bid curves enforced, plus non-anticipativity (eqs. 38-43, pp. 5-6). Intraday buy/sell volumes capped as a share of capacity (eqs. 34-35, p. 5). Battery degradation via piecewise-linear cycle-depth cost (Xu et al. 2018 model, 20 blocks) (pp. 6, 9).
- **How uncertainty is represented:** normal distributions for DA, ID and balancing prices, Rayleigh for wind speed; 5,000 roulette-wheel scenarios per source reduced by Kantorovich distance to 10 DA × 6 ID × 6 balancing × 10 wind = **3,600** scenarios (pp. 3, 6).
- **Solution method:** GAMS/CPLEX; 56,385 continuous, 120 binary variables, 73,034 equations, 5.9 s (Table 7, p. 10).
- **Key modelling choices and assumptions:** price-taker; charging power excluded from the HPGS's scheduled delivery (criticism of Jirsaraie et al. 2019) (pp. 3, 5); risk parameter β, confidence α = 0.95, gas 4.6 EUR/MBtu (p. 6).

## Data / case
- Iberian market (ESIOS) prices and meteoblue wind speeds, 1 Jan - 30 Jun 2018 (p. 6). Three DR resources with 4 MW each, price-quantity offers by valley/off-peak/peak (Table 2, p. 7). Bilateral DR prices 45, 50, 55 EUR/MWh (p. 6).

## Key findings
- (p. 7, Tables 3-4) Expected profit (β = 0): disjoint operation (Case 1) 33,382 EUR; coordinated (Case 2) 37,729 EUR (**+13.02%**, CVaR +8.39%); coordinated with DR (Case 3) 40,763 EUR (**+22.11%**, CVaR +23.00%).
- (p. 7) Raising β from 0 to 1 in Case 3 cuts expected profit only 0.28% while raising CVaR 20.75%.
- (p. 7, Table 5) Adding CAES to the wind-BES pair raises expected profit 7.38% (β = 0) and 7.69% (β = 2).
- (p. 8) BES does daily arbitrage (charges hour 5, discharges hour 21); CAES mostly runs in simple-cycle mode with very low charging in the 24-h horizon.
- (p. 9) Coordination accepts higher imbalance costs for higher total profit; DR purchases reduce imbalance cost.
- (p. 9, Table 6) Degradation cost reduces expected profit by only 62.5 EUR (Case 1) and 67.2 EUR (Case 3); coordinated operation uses deeper cycles. With degradation, BES shifts from DA to intraday offers (pp. 9-10).

## Strengths
- Explicit multi-stage information structure for sequential DA → ID → balancing decisions, with bid/offer curve derivation and CVaR.
- Quantifies the value of coordinating several assets across markets.

## Weaknesses / limitations
- 24-hour horizon, no end-of-horizon storage value: a CAES with 3,000 MWh is effectively not used as storage (mostly simple-cycle), so long-duration value cannot appear.
- Prices from independent normal distributions; no reserves; Iberian data from six months; in-sample evaluation.
- Some parameter table values are ambiguous in the PDF text layer.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review: multi-market bidding of storage portfolios | Coordinated vs disjoint: +13% / +22% expected profit | p. 7, Sec. 3.1.1, Tables 3-4 |
| Lit review: short-horizon models miss long-duration value | CAES mostly in simple-cycle mode over 24 h | p. 8, Sec. 3.1.2 |
| Method: three-stage stochastic DA/ID/balancing structure | Stage definitions and non-anticipativity | p. 3, Sec. 2.1; pp. 5-6 eqs. (38)-(43) |
| Method: CVaR in storage bidding | Profit-CVaR trade-off (0.28% profit for +20.75% CVaR) | p. 4 eqs. (1)-(4); p. 7 |
| Model: battery degradation cost | Piecewise-linear cycle-depth cost, small effect | p. 6 Sec. 2.3; p. 9 Table 6 |

## Useful quotes (with page numbers)
> "providing balancing reserves in addition to balancing energy could be another perspective for future research directions." (p. 10)

## Follow-up references to check (backward snowballing)
- Khatami, Oikonomou and Parvania (2019/2020), look-ahead CAES participation in DA and real-time markets (ref. [18]).
- Jirsaraie et al. (2019), risk-constrained bidding of wind + CAES aggregators (ref. [20]).
- Conejo, Carrión and Morales (2010), Decision making under uncertainty in electricity markets (ref. [32]) — standard textbook for scenario-based bidding and CVaR.
- Xu et al. (2018), cycle aging cost of batteries in electricity markets (ref. [36]).

