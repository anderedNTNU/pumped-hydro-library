---
bibkey: sioshansi2009estimating
bibkey_provisional: false
title: "Estimating the value of electricity storage in PJM: Arbitrage and some welfare effects"
authors: "Ramteen Sioshansi, Paul Denholm, Thomas Jenkin, Jurgen Weiss"
year: 2009
venue: "Energy Economics 31(2), 269-277 (doi:10.1016/j.eneco.2008.10.005)"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [modelling-phs-plants, reservoir-sizing-capacity]
relevance: high
read_by: []
added: 2026-11-05
takeaway: "Price-taking storage (modelled on PHS: 80 % round trip, Bath County) in PJM 2002-2007 as a deterministic LP with perfect foresight, hourly, solved two weeks at a time with a 15-day horizon so stored energy keeps carry-over value; 8 h of storage captures ~85 % and 20 h ~95 % of arbitrage value, a two-week backcast rule captures >=85 %, and a 1 GW device loses ~10-20 % of value through its own price impact (QP)."
---

# Value of storage in PJM: arbitrage and welfare (Sioshansi et al., 2009)

_Journal version (Energy Economics). Page numbers are journal pages 269-277._

## Research question / purpose
Four questions (p. 269): (1) how storage efficiency and energy capacity (hours of storage) drive the arbitrage value of a small, price-taking device; (2) how close a realistic operator without foresight comes to the perfect-foresight value; (3) how fuel prices, fuel mix and transmission constraints make the value vary across years and locations; (4) how a large device that moves prices changes its own arbitrage value and creates consumer/producer welfare effects.

## Setting
- **System:** a generic storage device; the parameters are taken from pumped-hydro storage (80 % round trip, "at the upper range of actual storage devices currently available (such as the Bath County PHS plant in PJM, which has an 80.3% efficiency)", p. 270). Same input and output power (footnote 3, p. 270).
- **Markets:** energy arbitrage only, against hourly load-weighted average PJM marginal prices (p. 270). Ancillary services and capacity payments are explicitly left out (p. 277).
- **Horizon and resolution:** each year 2002-2007, hourly; optimised **two weeks at a time** with perfect foresight, using a **15-day planning horizon** so that energy left at the end of each two-week window has carry-over value (p. 270).

## Method
- **Model type:** "Because of the price-taking assumption, the model is a linear program" (GAMS/CPLEX, p. 270). For the large device (Sec. 5) a linear price-load relation per month turns it into a convex QP (GAMS/MINOS, p. 274).
- **How uncertainty is represented:** deterministic, perfect foresight. Uncertainty is tested only by a "backcasting" rule: optimise on the previous two weeks' prices and apply the dispatch to the current two weeks (pp. 271-272).
- **Key modelling choices and assumptions:** price-taker (small device); carry-over value handled by a one-day look-ahead beyond the two-week window instead of a terminal value; equal charge/discharge power; constant efficiency; no head or reserve modelling.

## Key findings
- (p. 270, Fig. 2) Arbitrage value for a 12-h device ranged from about $60/kW-yr (2002) to more than $110/kW-yr (2005).
- (p. 270, Figs. 3-4) More than 50 % of the value comes from the first 4 h of storage; **8 h captures about 85 % and 20 h about 95 %**; the marginal value of an extra hour falls roughly linearly to about 8 h.
- (p. 271, Fig. 5) Efficiency matters with a multiplier: raising a 20-h device from 70 % to 80 % efficiency increases arbitrage value by more than 30 %; 9-10 h captures 90 % of the value for all efficiencies examined.
- (p. 272, Fig. 6) The two-week backcasting rule without foresight captures about 85 % or more of the perfect-foresight value in every year, because daily and weekday/weekend patterns are predictable.
- (p. 273, Fig. 12) Location matters: with 16 h and 80 %, average PJM value $77/kW-yr in 2006, but up to $105/kW-yr at individual buses.
- (pp. 274-275, Fig. 15) A 1 GW, 12-h device that moves prices loses about 10 % of its price-taker value in recent years and more than 20 % in some earlier years, when PJM was smaller.
- (pp. 275-276, Tables 1-3) Consumer surplus gains exceed producer losses, so large storage gives net welfare gains that a merchant owner does not capture (p. 277).

## Strengths
- Transparent, widely cited formulation of the price-taker storage LP, with explicit reasoning for the LP structure, the horizon and the carry-over value.
- Quantifies three things we need: value against hours of storage, the gap between perfect foresight and an implementable rule, and the price-taker error for a large device.

## Weaknesses / limitations
- Arbitrage only; one aggregated price; no reserves, head, inflow or seasonal storage.
- Perfect foresight gives an upper bound; the backcasting rule is a crude lower bound.
- Equal charge and discharge power; no pump/turbine distinction.
- The 15-day look-ahead is a heuristic for the end-of-window value, not an optimised water value.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review, modelling: deterministic LP for price-taking storage | LP because of price-taking; two-week windows with 15-day horizon | p. 270, Sec. 2 |
| Model: end-of-week value / why a terminal value is needed | Without carry-over value the device empties at the end of each window | p. 270 |
| Lit. review, sizing: value against hours of storage | 4 h > 50 %, 8 h ≈ 85 %, 20 h ≈ 95 % of value | p. 270, Figs. 3-4 |
| Assumptions: perfect foresight = upper bound | Backcast rule captures ≥ 85 % | pp. 271-272, Fig. 6 |
| Assumptions / perspective: price-taker error for large plants | 1 GW device loses ~10-20 % of value | pp. 274-275, Fig. 15 |
| Background: efficiency of PHS | 65-85 % for modern PHS; Bath County 80.3 % | pp. 270-271 |

## Useful quotes (with page numbers)
> "Because of the price-taking assumption, the model is a linear program" (p. 270)

## Follow-up references to check (backward snowballing)
- Walawalkar, Apt & Mancini (2007), *Economics of electric energy storage for energy arbitrage and regulation in New York*, Energy Policy 35, 2558-2568 (energy + regulation, likely LP; unverified).
- Graves, Jenkin & Murphy (1999), *Opportunities for electricity storage in deregulating markets*, Electricity Journal 12, 46-56.
- Sioshansi, Denholm & Jenkin (2011), *A comparative analysis of the value of pure and hybrid electricity storage*, Energy Economics 33, 56-66.

