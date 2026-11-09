---
bibkey: kloess2014bulk
bibkey_provisional: true   # not yet in Zotero/references.bib; ask the group to add it
title: "Bulk electricity storage technologies for load-leveling operation – An economic assessment for the Austrian and German power market"
authors: "Maximilian Kloess, Karl Zach"
year: 2014
venue: "International Journal of Electrical Power & Energy Systems 59, 111-122 (doi:10.1016/j.ijepes.2014.02.002)"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [reservoir-sizing-capacity, price-volatility, market-participation]
relevance: medium
read_by: []
added: 2026-11-05
takeaway: "Investor-perspective, perfect-foresight linear optimisation (GAMS) of yearly peak/off-peak arbitrage on EXAA day-ahead prices 2007-2011 for PHS (85 % cycle efficiency), AA-CAES, H2 and CH4 storage: the economically optimal PHS is a day storage with 7-8 h of energy per unit of power, PHS revenues fell sharply after 2009 (PV shaving midday peaks is named as the main driver) and even PHS dropped below capital costs; reserves are left out."
---

# Bulk storage for load levelling in Austria-Germany (Kloess and Zach, 2014)

## Research question / purpose
How do four bulk storage technologies (PHS, adiabatic CAES, hydrogen and methane storage) perform economically in load-levelling (price arbitrage) operation in the German-Austrian day-ahead market, and how did their revenues develop over 2007-2011 with growing wind and PV (abstract, p. 111; p. 112)?

## Setting
- **System:** one generic storage plant per technology, investor perspective ("plants are operated to maximize their own profit", p. 114). PHS: 92 % charging and 92 % discharging efficiency (85 % cycle), 500 €/kW + 30 €/kWh investment, 25-year depreciation (Table 2, p. 114; p. 112).
- **Markets:** EXAA day-ahead prices (almost perfectly correlated with EEX), years 2007-2011 (p. 115). Control reserve is **not** included because its revenue potential could not be estimated generally (p. 116); intraday is discussed but not modelled (p. 116).
- **Horizon and resolution:** one year at a time, hourly; weekly operation plots shown for 300 MW / 2100 MWh plants (Figs. 9-10, pp. 117-118).

## Method
- **Model type:** "linear optimization model implemented in GAMS" maximising yearly revenue from peak/off-peak arbitrage minus grid fees (Eq. 7, p. 115), with a state-of-charge balance with separate charge and discharge efficiencies (Eq. 8) and bounds on charge, discharge and stored energy (Eqs. 9-11, p. 115).
- **How uncertainty is represented:** deterministic, perfect foresight of the year's prices, which "generat[es] the maximum achievable annual profit" (p. 115).
- **Key modelling choices and assumptions:** price-taker (the effect of a new plant on prices is neglected, though it is acknowledged that added storage levels prices, p. 115); same maximum power for charging and discharging; constant efficiencies; capital cost with a power and an energy component (Eq. 1, p. 112).

## Key findings
- (p. 116, Fig. 7) With 2009 prices, revenues of all technologies fall below their capital costs; PHS comes closest. The optimal PHS layout has a storage-capacity-to-power ratio of 7-8, i.e. a day storage (AA-CAES 4-5).
- (p. 116, Fig. 8) Revenues are highly sensitive to market conditions: between 2009 and 2011 PHS revenues dropped by about 60 %, AA-CAES about 70 %, H2 and CH4 more than 80 %. Low-efficiency technologies are more sensitive.
- (pp. 117-118, Figs. 9-10) PHS cycles daily in both summer and winter weeks; H2 and CH4 run weekly cycles because their low efficiency cannot exploit daily spreads.
- (p. 118, Figs. 12-14) In seasonal operation all technologies charge in spring/summer and discharge in autumn/winter; a new PHS would not be sized for seasonal storage on economic grounds.
- (p. 119) Daily cycles are the most important source of storage revenue.
- (p. 120) PV growth (4 to 16 GW over 2007-2011) lowering midday peaks is named as a likely main driver of falling storage revenues.
- (p. 116; p. 121) Reserve provision might improve the economics of flexible plants like PHS, but it is left to future research.

## Strengths
- European, investor-perspective LP with explicit power and energy cost components; multi-year comparison shows how sensitive arbitrage value is to the price pattern.
- Explicitly compares day storage and seasonal storage for PHS.

## Weaknesses / limitations
- Energy arbitrage only, one year at a time with perfect foresight; no reserves, no inflow, no head effects.
- Generic PHS without natural inflow, so seasonal operation only reflects price spreads.
- Equal power for pumping and generating; simultaneous charging and discharging is not discussed.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review, sizing: optimal PHS duration for arbitrage | Ratio 7-8 (day storage) | p. 116, Fig. 7; p. 119 |
| Lit. review, modelling: deterministic LP for PHS arbitrage | Linear optimisation in GAMS, Eqs. 7-11 | p. 115 |
| Background / price volatility: arbitrage value sensitive to price pattern, PV shaving peaks | Revenue drop 2009-2011; PV as driver | pp. 116-117, 120 |
| Lit. review, markets: reserves excluded but expected to matter | Reason for excluding control reserve | p. 116 |
| Background: PHS cost components | 500 €/kW + 30 €/kWh (favourable site) | p. 112 |

## Useful quotes (with page numbers)
> "the optimal way to operate a PHS plant is as a day-storage" (p. 116)

## Follow-up references to check (backward snowballing)
- Steffen (2012), *Prospects for pumped-hydro storage in Germany*, Energy Policy 45, 420-429 (ref. [16]).
- Hildemann, Ulbig & Andersson (2011), *Electricity grid in-feed from renewable sources: a risk for pumped-storage hydro plants?*, EEM 2011 (ref. [14]).
- Deane, Ó Gallachóir & McKeogh (2010), *Techno-economic review of existing and new pumped hydro energy storage plant*, RSER 14(4), 1293-1302 (ref. [15]).
- Gatzen (2008), *The economics of power storage: theory and empirical analysis for Central Europe* (ref. [13]).

