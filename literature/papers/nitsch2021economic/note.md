---
bibkey: nitsch2021economic
bibkey_provisional: true
title: "Economic evaluation of battery storage systems bidding on day-ahead and automatic frequency restoration reserves markets"
authors: "Felix Nitsch, Marc Deissenroth-Uhrig, Christoph Schimeczek, Valentin Bertsch"
year: 2021
venue: "Applied Energy, 298, 117267"
peer_reviewed: true
methods: [deterministic-lp-milp, heuristics-simulation]
review_sections: [market-participation, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Agent-based German market model (AMIRIS) with aFRR capacity bids from DA opportunity costs, plus a perfect-foresight MILP for a battery on DA + aFRR: aFRR gave 27-77 % of revenue historically (more for short-duration storage), but in a 2030 high-RE scenario revenue shifts almost entirely to the more volatile DA market."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/108_Nitsch_2021_Economic_evaluation_of_battery_storage_systems_bidding_on_day_ahead_and_automatic_frequenc.pdf"
---

# Battery storage on day-ahead and aFRR markets (Nitsch et al., 2021)

## Research question / purpose
What revenue can a privately owned battery storage system (BSS) earn on the day-ahead (DA) and aFRR markets, now and in a future high-renewables system, when both market prices are simulated fundamentally rather than taken as given (pp. 2–3)? Novelty: aFRR implemented in the agent-based model AMIRIS, combined "model-within-model" with an operator optimisation (p. 3).

## Setting
- **System:** Germany, single bidding zone, no grid (p. 6). Storage: a BSS with energy-to-power (E2P) ratio 1–10 h (p. 8).
- **Markets:** DA (hourly uniform-price clearing) and aFRR (capacity "power" prices and activation "energy" prices, positive and negative) (pp. 3–5). No intraday, FCR or mFRR (p. 9).
- **Horizon and resolution:** one year, 8760 hours. Back-test 2019; scenario 2030 with 60 % renewables (pp. 5–6). aFRR bidding simplified to hourly, although real German aFRR tenders were weekly/daily (p. 7).

## Method
- **Model type:** (1) AMIRIS agent-based market simulation: conventional plants bid marginal cost on DA; aFRR capacity bids are **opportunity costs relative to the forecast DA price** (eqs. 1–4, p. 3, following Müsgens, Ockenfels & Peek): positive capacity bid = p_forecast − c if in the money, otherwise the cost of running at minimum load; negative capacity bid = 0 if c ≤ p_forecast; positive energy bid = c, negative energy bid = 0. aFRR is cleared first, then DA bids are adjusted to remaining capacity (Fig. 1, p. 4). (2) BSS MILP (GAMS/CPLEX) maximising DA + aFRR capacity + aFRR energy revenue over the year with SOC bounds, power limit SOC_max/E2P on all flows, no simultaneous charge/discharge, 87 % charge and discharge efficiency, no degradation or self-discharge (eqs. 5–12, pp. 4–5).
- **How uncertainty is represented:** none in the operator model (**perfect foresight**, p. 4). aFRR demand fixed at 1.7 GW each direction from historic averages; activated energy from historic data (pp. 6, 9).
- **Key choices:** BSS is a price-taker and is paid like the most expensive accepted plant; results are an upper bound (p. 8, p. 9).

## Data / case
Plant park 2018 and 2030 (Tables 1–2), 2030 scenario from Lutz et al.; CO₂ 35 EUR/t in 2030 (pp. 5–6). Historic 2016 prices used as a third comparison (p. 8).

## Key findings
- (p. 7) Back-test 2019: simulated mean DA price 39.20 vs. historic 38.70 EUR/MWh, correlation 0.81; low prices overestimated because ramping/start-up costs are missing.
- (p. 7–8) 2030: mean DA price 63 EUR/MWh, std 12 EUR/MWh; positive aFRR capacity prices up to about 45 EUR/MW, highest variability in winter, lowest in summer; **negative aFRR capacity prices are 0 EUR/MW** because plants with marginal cost below the DA price can supply them at no opportunity cost.
- (p. 8) Varying aFRR demand 1.4–2.0 GW barely changed prices, because supply capacity is ample.
- (p. 9) In 2016/2019 the aFRR share of BSS revenue ranges from 77 % (E2P = 1) to 27 % (E2P = 10): short-duration storage earns more from reserves. In 2030 there is "hardly any significant revenue from the aFRR market"; DA revenue rises strongly due to higher price fluctuations.
- (p. 9) Smaller E2P gives higher revenue per unit of energy capacity; +1 percentage point round-trip efficiency gives about +2.5 % revenue.
- (p. 9) Outlook for BSS investors is challenging; additional markets or incentives may be needed.

## Strengths
- Explicit, simple formula for reserve-capacity bids as DA opportunity cost, the same economic logic as our capacity-vs-energy trade-off.
- Shows how the revenue split between energy and reserves depends on storage duration.

## Weaknesses / limitations
- Perfect foresight; hourly aFRR market instead of the real daily/weekly; aFRR prices are not well explained by theory (simulated 2019 revenue below historic 2016, p. 8); no strategic bidding or competition among flexibility providers (p. 9).
- Battery, not hydro; no long-term storage value; German market, not Nordic.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background: electricity markets, reserve pricing | aFRR capacity and energy bids derived from DA opportunity cost; negative aFRR capacity priced at 0 when units are in the money | p. 3, eqs. 1–4; p. 8 |
| Literature review: market participation of storage in DA + aFRR | Revenue split DA vs. aFRR, 27–77 % aFRR share depending on E2P; shift to DA in 2030 | p. 9, Sec. 3.2 |
| Literature review: storage duration vs. revenue source | Short E2P favours reserves and short-term price fluctuations | p. 9 |
| Discussion: price volatility increases arbitrage value | Higher DA price fluctuations in 2030 make DA the main revenue source | p. 9, p. 10 |

## Useful quotes (with page numbers)
> "we hardly see any significant revenues from the aFRR market in the scenario 2030" (p. 9)

## Follow-up references to check (backward snowballing)
- [36] Müsgens, Ockenfels & Peek: German balancing power market design and opportunity-cost bidding.
- [10] Braeuer et al. 2019: BSS with parallel revenue streams (FCR, intraday, DA, peak shaving).
- [70] Ela et al.: system services as a growing revenue share (contrasting view).
- [1] Hasche, Haiges & Schulz 2016: prequalified aFRR capacities, batteries in the reserve market.

