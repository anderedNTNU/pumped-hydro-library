---
bibkey: bradbury2014economic
bibkey_provisional: true   # not yet in Zotero/references.bib; ask the group to add it
title: "Economic viability of energy storage systems based on price arbitrage potential in real-time U.S. electricity markets"
authors: "Kyle Bradbury, Lincoln Pratson, Dalia Patiño-Echeverri"
year: 2014
venue: "Applied Energy 114, 512-519 (doi:10.1016/j.apenergy.2013.10.010)"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [reservoir-sizing-capacity, price-volatility]
relevance: medium
read_by: []
added: 2026-11-05
takeaway: "Perfect-foresight LP over a full year (8760 h) of 2008 real-time prices in 7 US markets for 14 storage technologies, with the energy-to-power ratio chosen to maximise IRR: the optimal duration is set mainly by efficiency, self-discharge and the cost split between power and energy, not by price volatility (which raises IRR); PHS and CAES are optimal at roughly 5-10 h and already exceed 10 % IRR, and their IRR improves most by cutting power-capacity cost."
---

# Arbitrage-based viability and sizing of storage (Bradbury et al., 2014)

## Research question / purpose
Which energy and power capacities maximise the internal rate of return (IRR) of 14 storage technologies when they arbitrage real-time prices, and how much would power or energy capital costs have to fall to reach a 10 % IRR (abstract, p. 512; p. 513)? Previous studies fixed both capacities and so did not size storage optimally (p. 513).

## Setting
- **System:** generic storage with technology-specific round-trip efficiency, self-discharge, lifetime and costs; 14 technologies including pumped hydro (PHS), CAES, flywheels, capacitors and eight battery types (p. 513; Table A.1).
- **Markets:** real-time energy arbitrage only, 2008 LMPs at one node in each of NYISO, ERCOT, PJM, SPP, MISO, CAISO and ISO-NE (p. 515). Ancillary services, capacity and day-ahead markets are deliberately not modelled (p. 513).
- **Horizon and resolution:** one year, hourly (n = 8760) (p. 513).

## Method
- **Model type:** LP maximising annual arbitrage revenue, Eqs. (1)-(3) (p. 513): storage balance with self-discharge and round-trip efficiency on charging, power limits on charge and discharge, energy limit; E(0) = 0. Revenue feeds an IRR calculation, Eqs. (4)-(7), solved by Newton-Raphson (pp. 513-514).
- **Sizing:** power fixed at 1 MW, energy capacity varied to find the IRR-maximising hours of storage; costs scale linearly, so the result holds at any scale (Fig. 3 caption, p. 516).
- **How uncertainty is represented:** deterministic, perfect foresight of the year's prices.
- **Key modelling choices and assumptions:** price-taker; charge and discharge at the same maximum rate; linear capital cost C = E·cE + P·cP (Eq. 6, p. 514); no O&M except CAES fuel.

## Key findings
- (p. 515, Fig. 2) Revenue grows quickly from 0 to 5 h of storage and approaches an asymptote at about 15 h because of the daily price cycle; about half a day of storage captures most arbitrage revenue.
- (p. 515) Revenue depends on market volatility: Houston (most volatile) is the most profitable, Boston less than 60 % of it.
- (p. 512, abstract; p. 518) The profit-maximising duration is set mainly by technology characteristics (efficiency, self-discharge) and cost structure, not by price volatility, which instead raises IRR.
- (p. 516, Fig. 3) Optimal PHS duration is about 4.6-10 h (best and worst case averaged over the markets; the abstract states 7-8 h); PHS and CAES reach IRRs well above 10 % in every market except Boston under the best parameters (p. 515).
- (p. 517; p. 518) For PHS and CAES, power-capacity costs make up about 65-95 % of total cost, so cutting power cost raises IRR most; the reason the optimal PHS duration is longer is that reservoir (energy) capacity is cheap relative to turbines (p. 518).
- (p. 518) The authors note that perfect foresight and equal charge/discharge rates overestimate profitability, while linear cost scaling may underestimate it.

## Strengths
- Treats storage duration as a design variable and separates power cost from energy cost, the same distinction as in `blakers2021` and `horsleyWrobel2002`.
- Simple, fully stated LP; directly comparable across technologies and markets.

## Weaknesses / limitations
- Arbitrage in real-time markets only; no reserves, no inflow, no seasonal value; one year (2008, a high-price year) of data.
- Perfect foresight over a whole year; E(0) = 0 with no terminal condition.
- PHS is generic: one power rating for pumping and generation, constant efficiency, no head effects.
- Sizing only varies energy for fixed power, not pump and turbine power separately.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review, sizing: LP-based sizing of storage duration | IRR-maximising hours of storage for 14 technologies | pp. 513-516, Eqs. 1-7, Fig. 3 |
| Lit. review, sizing: power vs energy cost for PHS | Power cost 65-95 % of PHS total; reservoir capacity cheap | pp. 517-518, Fig. 4 |
| Lit. review, price volatility: volatility raises value but not optimal size | Houston vs Boston; size set by technology | pp. 512, 515, 518 |
| Assumptions: perfect foresight and equal charge/discharge rates overestimate profit | Authors' own caveat | p. 518 |

## Useful quotes (with page numbers)
> "the profit-maximizing size (i.e. hours of energy storage) of an ESS is primarily determined by its technological characteristics" (p. 512)

## Follow-up references to check (backward snowballing)
- Walawalkar, Apt & Mancini (2007), Energy Policy 35(4), 2558-2568 (arbitrage + regulation in New York; ref. [17]).
- Kazempour et al. (2009), *Electric energy storage systems in a market-based economy: comparison of emerging and traditional technologies*, Renewable Energy 34(12), 2630-2639 (ref. [18]).
- Yang & Jackson (2011), *Opportunities and barriers to pumped-hydro energy storage in the United States*, RSER 15(1), 839-844 (ref. [12]).

