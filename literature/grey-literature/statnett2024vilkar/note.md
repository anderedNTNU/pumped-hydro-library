---
bibkey: statnett2024vilkar
bibkey_provisional: true
title: "Vilkår for aktiveringsmarkedet for mFRR (regulerkraftmarkedet), gjeldende fra og med 01.01.2024"
authors: "Statnett"
year: 2024
venue: "Statnett market terms, appendix to guidelines for fos § 11; Dok. Id 2023/3187-6; PDF, 13 pp. (historical/superseded)"
peer_reviewed: false
methods: []
review_sections: [electricity-markets, price-volatility]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "SUPERSEDED pre-2025 Norwegian mFRR activation-market rules: 15-min max activation time, quarter-hour volumes but one price per hour, mFRR price set after the hour by the marginal activated bid, 10 MW minimum bid (5–9 MW allowed in NO1/NO3), GCT 45 min before the hour; documents the regime behind historical hourly mFRR prices."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/03_Reservemarkeder_og_vilkar/64_Statnett_2024b_Vilkar_for_aktiveringsmarkedet_for_mFRR_fra_01_01_2024.pdf
---

# Statnett mFRR activation-market terms from 1 Jan 2024 (Statnett, 2024) — historical

**Source file:** `source.pdf` / `source.txt` (copied from the inbox; original in Statnett's "retningslinjer – historikk" archive, URL in the inbox KILDEINFO `64_Statnett_2024b_KILDEINFO.md`). Norwegian. **Printed page = PDF page − 1.**

**Why filed although superseded:** the current rules (`ph24_statnett_bsp_terms_2025`, Ch. 5; `ph24_mfrr_activation_guide`) describe the automated **15-minute** Nordic mFRR EAM. This document is the only filed source for the **previous hourly-priced regime**, which generated the historical mFRR (regulerkraft) prices in any pre-2025 price data. The companion 2024 terms for the aFRR and mFRR capacity markets were *not* filed: their content is essentially carried over into the current BSP terms.

## Research question / purpose
Binding terms for offers, acceptance, activation and pricing in the Norwegian mFRR activation market (formerly "regulerkraftmarkedet", RKM), valid from 1 January 2024 (version 18; change log p. 3). Appendix to the guidelines for fos § 11 (p. 5).

## Setting
- **System:** Norway, all bidding zones; bids in a common Nordic list (p. 9).
- **Markets:** mFRR energy activation market (manual activation by phone/electronic order).
- **Horizon and resolution:** quarter-hour volumes, **hourly price** (p. 6).

## Method
- **Model type / uncertainty / solution method / assumptions:** n/a (regulatory text).

## Data / case
n/a.

## Key findings (rules, section and printed page)
- (Sec. 4, p. 5) Participation requires a balance agreement with Statnett (or via a BRP); new regulation objects approved by Statnett (answer within 3 months); re-qualification at most every 5 years.
- (Sec. 5, p. 6) **mFRR activation time maximum 15 minutes.** Quantity and price on a **quarter-hour basis (15 min)**, but **"mFRR-pris vil settes per time"** (one mFRR price per hour).
- (Sec. 6.1, p. 6) Preliminary bids for next day by **21:30**; new bids/corrections at the latest **45 minutes before each operating hour**.
- (Sec. 6.3, p. 7) Must be able to fully activate within 15 min of the order; **obligations from other markets shall not limit the ability to deliver the offered mFRR volume**. Quantity may vary per quarter-hour, but **price must be the same through the hour**. Prices in EUR/MWh in steps of **0.5 EUR/MWh**; up-bids at least the nearest 0.5 EUR above the day-ahead area price, down-bids at most the nearest 0.5 EUR below; price limits **±10 000 EUR/MWh**. Max duration and resting time may be specified in whole quarter-hours.
- (Sec. 6.4, pp. 7–8) **Minimum bid normally 10 MW**; in **NO1 and NO3** one additional bid of 5–9 MW per station group allowed; bids < 10 MW otherwise not used in ordinary balancing (except under fos § 12 orders, min 1 MW).
- (Sec. 7.1, p. 8) Bids normally used in price order; Statnett may skip bids for system reasons without compensation, and may suspend bids and use the volume at the day-ahead price if pricing is not socio-economically efficient (fos § 11).
- (Sec. 7.2, pp. 8–9) Activation messages sent continuously as needed; **activation applies for the rest of the hour** unless otherwise stated; start and stop can be at any minute.
- (Sec. 7.3, pp. 9–10) **Pricing:** common Nordic list; mFRR price equal across zones without congestion. Up-regulation price = **most expensive activated balancing bid**, down-regulation price = **cheapest activated**; **set per bidding zone after the hour has ended**. Up-price ≥ and down-price ≤ day-ahead area price; if no regulation in a direction, mFRR price = day-ahead area price; a **dominating direction** per hour is determined from net regulated volume. Special regulations (out of merit for system reasons) paid as bid.
- (Sec. 7.4, p. 10) mFRR prices published one hour after the operating hour, on ENTSO-E Transparency Platform.
- (Sec. 8, pp. 10–11) Disputes on registered activations possible if timing deviates > 5 min/hour/bid or energy > 5 MWh/hour/bid.

## Comparison with current rules (`ph24_statnett_bsp_terms_2025`, from 2 Dec 2025)
| Parameter | 2024 terms (this source) | Current terms |
|---|---|---|
| Activation / FAT | max 15 min (Sec. 5) | FAT 12.5 min (Art. 59.1a) |
| MTU / pricing period | quarter-hour volumes, **hourly price** (Sec. 5) | **15-min MTU** for bids and prices (Art. 10.2, 67) |
| Gate closure | 45 min before operating hour (Sec. 6.1) | 45 min before each 15-min MTU (Art. 61) |
| Minimum bid | **10 MW** (5–9 MW in NO1/NO3) (Sec. 6.4) | **1 MW**, 1 MW steps (Art. 62) |
| Price step | 0.5 EUR/MWh | 0.01 EUR/MWh |
| Activation | manual, rest of hour | scheduled (cyclic every 15 min) and direct activation, defined ramps (Art. 65) |
| Price limits | ±10 000 EUR/MWh | ±10 000 EUR/MWh |

## Strengths
- Primary, binding source for the market design that produced historical Norwegian hourly mFRR prices.

## Weaknesses / limitations
- Superseded; must not be cited for current rules. The exact go-live date of the 15-min Nordic mFRR EAM is not in this document (check `ph24_mfrr_activation_guide` / `ph24_statnett_mfrr`).
- Norwegian only.

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where (printed page) |
|---|---|---|
| Data/case: historical mFRR prices | Hourly mFRR price set after the hour by marginal activated bid, per zone | Sec. 5 (p. 6); Sec. 7.3 (pp. 9–10) |
| Data/case: structural break in mFRR data | Old vs new rules (table above) | Sec. 5, 6.1, 6.4 |
| Background 2.4 (history): RKM → mFRR EAM | Name change, previous rules | p. 4 (Ordliste), change log p. 3 |
| Background: dominating direction / day-ahead price fallback | Rules a)–b) | Sec. 7.3 (p. 9) |
| Background: other obligations may not limit EAM bids (unchanged principle) | Deliverability rule | Sec. 6.3 (p. 7) |

## Useful quotes (with page numbers)
> "mFRR-pris vil settes per time." (Sec. 5, p. 6)

## Follow-up references to check (backward snowballing)
- Superseded companion documents (not filed): "Vilkår for kapasitetsmarkedet for aFRR" (2024, Dok. Id 2023/3187-6) and "Vilkår for kapasitetsmarkedet for mFRR" (11.02.2024).
- Forskrift om systemansvaret (fos) §§ 11–12.

