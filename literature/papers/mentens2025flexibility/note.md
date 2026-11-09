---
bibkey: mentens2025flexibility
bibkey_provisional: true
title: "Flexibility in short-term electricity markets for renewable integration and uncertainty mitigation: A comprehensive review"
authors: "Lander Mentens, Herbert Peremans, Johan Springael, Philippe Nimmegeers"
year: 2025
venue: "Smart Energy 18, 100183 (Elsevier)"
peer_reviewed: true
methods: []
review_sections: [electricity-markets, price-volatility]
relevance: background
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/35_Mentens_2025_Flexibility_in_short_term_electricity_markets_for_renewable_penetration.pdf
takeaway: "Narrative review of European (CWE-focused) day-ahead, intraday and balancing market design (SDAC/EUPHEMIA, 15-min MTU from June 2025, SIDC and the June 2024 pan-European intraday auctions, PICASSO/MARI, price limits, imbalance pricing) and of flexibility in time, space and demand response, including storage; useful as an up-to-date reference on market timing and rules, not on Nordic hydro."
---

# Flexibility in European short-term electricity markets (Mentens et al., 2025)

_Article 100183, 14 pages; page numbers below are PDF pages 1–14 (the journal uses article numbering, no separate page range). Not in `references.bib`: provisional key. The inbox file name says "renewable penetration"; the actual title says "renewable integration and uncertainty mitigation" (KILDEINFO notes this)._

## Research question / purpose
How can the design of short-term electricity markets (DA, ID, balancing) be improved to integrate RES by maximising flexibility (p. 2)? Contributions: (1) explain short-term market dynamics, (2) propose design improvements to increase flexibility, (3) use flexibility to mitigate uncertainty (p. 2). Flexibility is split into **time** (storage, granularity), **space** (interconnection, coupling, nodal pricing) and **price signals / demand response** (p. 2).

## Setting
- **System:** European markets with focus on Central Western Europe (CWE); Nordic mentioned only for gate times and intraday auctions.
- **Markets:** forwards/futures, day-ahead, intraday (continuous and auctions), balancing (FCR, aFRR, mFRR; imbalance settlement).
- **Horizon and resolution:** n/a (review).

## Method
- **Model type:** narrative literature and regulatory review; Table 1 classifies ~25 reviewed works by flexibility dimension, market and scope (p. 4).
- **How uncertainty is represented:** n/a.

## Data / case
None (review of literature, regulation and exchange documentation).

## Key findings
- (p. 1–2) Four sequential markets: forwards/futures → DA → ID → balancing; TSO responsible after ID gate closure; BSP procurement vs BRP settlement.
- (p. 4–5) Forward/futures products are coarse (base/peak, year → month → day), re-profiled toward delivery; short-term markets "add shape" (Figs. 1–2).
- (p. 5) **DA (SDAC):** 28 markets, blind auction, gate closure mostly 12:00 D-1, EUPHEMIA uniform-price clearing; **15-min MTU in SDAC from 11 June 2025** (delivery 12 June) (p. 5, 8).
- (p. 6) DA orders: linear (up to 256 price/quantity pairs), block, smart/large blocks representing non-convexities; CWE DA price limits **−500 / +4000 €/MWh**; price caps relate to "missing money"; negative prices explained by inflexible plants and subsidised RES.
- (p. 6) **ID:** continuous trading opens 15:00 D-1 (**14:00 in the Nordics**), lead time 60 to 15 min; pay-as-bid, price–time priority; limits ±9999 €/MWh. **Pan-European intraday auctions from 13 June 2024**: IDA1 15:00 D-1, IDA2 22:00 D-1, IDA3 10:00 D (CET), in CWE, Nordic and Polish zones.
- (p. 6) **Balancing:** FCR full activation within 30 s; **aFRR within 7.5 min; mFRR within 15 min**; single vs dual imbalance pricing (France dual; BE, DE, NL single) (p. 7).
- (p. 7) Net regulation volume as share of consumption has declined, attributed to better forecasts, profiling, ID liquidity, coupling.
- (p. 8) Europe procures reserves separately and before DA; capacity in reserves cannot be offered in DA, so reserve prices embed **opportunity cost of DA participation**; co-optimisation of energy and reserves (as in Australia/US) proposed.
- (p. 8) Smart orders incl. loop blocks and storage/arbitrage orders that carry storage level, efficiency and charge/discharge rates.
- (p. 9) PICASSO (aFRR, operational since 2022) and MARI (mFRR, operational 2022); harmonised balancing energy bid limits **±10,000 €/MWh until July 2026, then ±15,000 €/MWh**.
- (p. 9–10) Storage and demand response: arbitrage, price smoothing; reserve market participation "often yields higher revenues than energy markets" for these resources (citing [16]); ID price volatility closer to delivery raises profit potential.
- (p. 11) Future research: integrated models of flexibility provision, market design and **price volatility** across all three markets.

## Strengths
- Recent (2025) and fairly complete overview of EU short-term market rules and timelines, including 2024–2026 reforms.
- Explicit link between reserve-before-DA sequencing and opportunity-cost pricing, which matters for a storage plant choosing between energy and reserves.

## Weaknesses / limitations
- CWE-centred; Nordic-specific rules (e.g. Nordic aFRR/mFRR capacity markets, Nordic balancing model) are barely covered.
- Narrative review without systematic search protocol or quantitative synthesis; many claims rely on single references.
- Hydro and long-duration storage get little attention; price volatility is discussed qualitatively.
- Some numbers (activation times, price limits) are given without dates of validity; verify against ENTSO-E/Nord Pool documents before citing in the thesis.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.4: market sequence forwards → DA → ID → balancing | Description and Fig. 3 timeline | p. 1–2, 4–5, Fig. 3 p. 7 |
| Background 2.4: DA design (SDAC, EUPHEMIA, gate 12:00 D-1, 15-min MTU from 11 June 2025, price limits) | Rules and dates | Sect. 2.1, p. 5–6; Sect. 3.1.1, p. 7–8 |
| Background 2.4: ID market (continuous, IDAs from 13 June 2024, Nordic opening 14:00) | Rules and times | Sect. 2.2, p. 6; Sect. 3.1.2, p. 8 |
| Background 2.4: reserves FCR/aFRR/mFRR activation times; imbalance pricing | 30 s / 7.5 min / 15 min; single vs dual pricing | Sect. 2.3, p. 6–7 |
| Background 2.4: reserve procurement before DA → opportunity cost; co-optimisation | Argument and references | Sect. 3.1.3, p. 8 |
| Background 2.4: European balancing platforms PICASSO and MARI | Status and bid limits | Sect. 3.2.3, p. 9 |
| Lit. review 5.4 market participation: storage earns more in reserves | Statement citing [16] | Sect. 3.3, p. 10 |
| Background 2.5: drivers of short-term price volatility (RES, negative prices) | Qualitative discussion | p. 1–2, 6, 9 |

## Useful quotes (with page numbers)
> "capacity allocated to the reserve capacity market cannot be offered in the DA market, leading to suboptimal price formation" (p. 8)

> "Studies show that reserve market participation often yields higher revenues than energy markets for these resources" (p. 10)

## Follow-up references to check (backward snowballing)
- Brijs, De Jonghe, Hobbs & Belmans (2017), Applied Energy 195: short-term market design in CWE and power system flexibility (ref. [3]).
- Brijs, Geth, De Jonghe & Belmans (2019), J. Energy Storage 25: storage arbitrage opportunities in CWE short-term markets (ref. [15]).
- Newbery et al. (2018): market design for high-RES systems (ref. [4]).
- Scharff & Amelin (2016), Energy Policy 88: trading behaviour on the continuous intraday market Elbas (Nordic) (ref. [28]).
- Zalzar et al. (2020): cross-border ID integration with hydro storage (ref. [29]).
- Poplavskaya et al. (2021): EU balancing market rules (ref. [30]).
- Mays (2021): suppressed volatility in clearing and underinvestment in flexibility (ref. [38]).
- Mimica et al. (2022), EPSR 204: storage and demand response in a robust joint energy-reserve market (ref. [16]); source of the "higher revenues in reserves" claim, check before citing.

