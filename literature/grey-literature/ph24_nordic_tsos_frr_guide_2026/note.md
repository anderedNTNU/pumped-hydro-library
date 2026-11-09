---
bibkey: ph24_nordic_tsos_frr_guide_2026
title: "Nordic FRR balancing capacity market / Nordic MMS / BSP implementation guide"
authors: "Nordic TSOs (Nordic Balancing Model)"
year: 2026
venue: "NBM implementation guide, Version 1.4, 08.10.2026; PDF, 45 pp."
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Nordic aFRR/mFRR capacity market via Nordic MMS: gate D-7 00:00 to D-1 07:30 CET, hourly MTU, integer MW bids 0–999, price 0–9 999 €/MW/h, pay-as-cleared per zone/MTU/direction, exclusive aFRR–mFRR linking (aFRR cleared first), CZC reservation optimised against day-ahead value."
---

# Nordic FRR balancing capacity market – BSP implementation guide (Nordic TSOs, 2026)

**Source file:** `source.pdf` / `source.txt` (fetched 2026-11-04; bib URL works). Cover: Version 1.4, 08.10.2026. Printed page numbers = PDF page numbers. Pages 22–45 are mostly XML/CIM message specifications.

## Research question / purpose
Technical and functional guide for BSPs integrating with **Nordic MMS** for the common Nordic aFRR and mFRR capacity markets: reserve-requirement publication, bid submission, market results.

## Setting
- **System:** Nordic market area (DK1, DK2, FI, NO1–NO5, SE1–SE4; p. 23).
- **Markets:** aFRR CM and mFRR CM (FCR capacity also supported by Nordic MMS but out of scope, p. 5).
- **Horizon and resolution:** daily auctions; hourly (PT60M) bids and reserve requirements.

## Method
- **Clearing:** optimisation maximising socio-economic benefit, weighing reserve-procurement savings from exchange against the cost of reserving cross-zonal capacity (CZC) from the day-ahead market (p. 5).

## Data / case
n/a.

## Key findings
- (p. 5, Sec. 1.1) Capacity procured **before the day-ahead market**, considering geographic distribution and network constraints; CZC reservation methodology for FRR.
- (p. 5, Sec. 1.3) aFRR CM / mFRR CM: BSPs commit to offer the allocated amount as balancing-energy bids in the respective activation market.
- (pp. 8–9, Sec. 2.1–2.3) **Gate opening D-7 00:00 CET; gate closure D-1 07:30 CET; results: mFRR no later than D-1 08:10 CET, aFRR no later than D-1 09:20 CET**; TSOs can extend or reopen the bidding gate. (Note: BSP terms Art. 18.5 say aFRR results by 09:00 CET — minor discrepancy between documents.)
- (p. 15, Sec. 3.2) Reserve requirements published as daily data in **hourly resolution** per bidding zone / macro area; macro-area min/max acts as localisation constraint.
- (p. 16, Sec. 3.3.1) Bids per bidding zone; **Statnett requires locational information for both aFRR and mFRR.**
- (p. 16, Sec. 3.3.2–3.3.3) **Bid quantity integer 0–999 MW**, may vary per hour, ≤ portfolio max; **bid price 0–9 999 €/MW/h**, two decimals, same for all positions in a time series.
- (p. 16, Sec. 3.3.4) Block bids: equal quantities over consecutive MTUs; all-or-nothing; not in exclusive groups.
- (pp. 16–17, Sec. 3.3.5) Divisible bids accepted between minimum quantity and offered quantity; minimum quantity ≤ 50 MW. Indivisible bids ≤ 50 MW. **Explicit "indivisible" flag only for delivery days before 27.10.2026 (p. 17) / 25.11.2026 (p. 18)**; afterwards indivisibility via minimum quantity (inconsistent dates within the guide).
- (p. 17) **Exclusive linking within a market and between aFRR and mFRR; aFRR CM cleared before mFRR CM.** Rule change from delivery date 15.10.2026: if the linked aFRR bid is selected, divisible linked mFRR bids are offered with quantity reduced by the accepted aFRR quantity (previously: excluded entirely). Order may exceptionally be reversed.
- (p. 18, Sec. 3.3.6) Technical linking with resting time and maximum activation duration allowed for **mFRR only**, not aFRR.
- (p. 20, Sec. 3.4) **Settlement is pay-as-cleared**: clearing prices per bidding zone, MTU and regulation direction.

## Strengths
Current (Oct 2026), precise market-clearing rules, explicit about aFRR/mFRR interaction in the capacity auction.

## Weaknesses / limitations
- Implementation-oriented; market rules proper are in national terms (`ph24_statnett_bsp_terms_2025`) and Nordic CM rules (Ref [1]–[2], p. 7).
- Internal date inconsistency for removal of indivisible flag (27.10.2026 vs 25.11.2026).

## Use it for… (lookup guide)
| Use in our thesis | What the guide provides | Where (page/section) |
|---|---|---|
| Background 2.4: timing table (aFRR/mFRR CM rows) | GOT D-7 00:00 CET; GCT D-1 07:30 CET; results 08:10 (mFRR) / 09:20 (aFRR) CET | pp. 8–9, Sec. 2.3 |
| Background 2.4: capacity procured before DA | Stated | p. 5, Sec. 1.1 |
| Model: MTU and bid resolution | Hourly (PT60M); integer MW | p. 15, 16 |
| Model: price units/limits | 0–9 999 €/MW/h | p. 16, Sec. 3.3.3 |
| Model: pricing rule | Pay-as-cleared per zone/MTU/direction | p. 20, Sec. 3.4 |
| Model: aFRR–mFRR interaction | Exclusive linking, aFRR cleared first | p. 17 |
| Model: energy-limited mFRR bids | Resting time, max duration (mFRR only) | p. 18, Sec. 3.3.6 |
| Background: CZC reservation vs DA | Optimisation weighs savings vs DA cost | p. 5 |

## Useful quotes (with page numbers)
> "Settlement of accepted bids uses the pay-as-cleared methodology" (p. 20)

## Follow-up references to check (backward snowballing)
- The Nordic aFRR Capacity Market rules; The Nordic mFRR Capacity Market rules (Refs [1]–[2], p. 7).

