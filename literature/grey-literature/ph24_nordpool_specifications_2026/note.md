---
bibkey: ph24_nordpool_specifications_2026
title: "Product Specifications (Nordic/Baltic Market Areas)"
authors: "Nord Pool AS"
year: 2026
venue: "Nord Pool Rulebook, B.3.1 Product Specifications, effective from 28 May 2026"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "The binding product rules for Nord Pool's Nordic/Baltic day-ahead (GC 12:00 D-1, 96 x 15-min periods, 15/30/60-min orders, 0.1 MW lot, -600/+4000 EUR) and intraday continuous (opens 14:00 D-1, GC 60 min in NO) and IDA1-3 (GC 15:00, 22:00, 10:00) markets."
---

# Nord Pool Product Specifications, Nordic/Baltic (effective 28 May 2026)

**Fetched:** 2026-11-04 from the bib URL, `%PDF` OK, 9 pages, `source.pdf` / `source.txt` (`pdftotext -layout`).
**Caution:** the `-layout` extraction **misaligns the table in §4.2 (p. 8)**: it prints the IDA start times (14:40/21:40/09:40) on the "Gate Closure" row. The `-raw` extraction and the PDF give the correct reading below. Page numbers are the document's printed page numbers, which equal the PDF page numbers.

## Research question / purpose
n/a. A rulebook document that specifies the physical-market products Nord Pool operates in the Nordic and Baltic areas: day-ahead (SDAC), intraday continuous (SIDC/IDCT) and intraday auctions (SIDC/IDA).

## Setting
- **System:** Nordic/Baltic bidding zones (NO1–NO5, SE1–SE4, FI, DK1–DK2, EE, LV, LT).
- **Markets:** day-ahead, intraday continuous, intraday auctions. Reserves are not covered.
- **Time:** all times CET (§1.2). Clock-change days have 23 or 25 hours (§1.2).

## Method
n/a.

## Data / case: product parameters relevant for modelling PHS participation

**Day-ahead market** (§2, pp. 4–5):

| Parameter | Value |
|---|---|
| Quotation | Continuous order submission until gate closure, then an auction (Day-ahead Market Regulations) |
| Trading hours / MTU | 24 h = **96 Delivery Periods** (15-min MTU) |
| **Gate closure** | **12:00 CET on D-1** |
| **Gate opening** | **normally 60 days before the delivery day** (§2.3) |
| **Trade lot (bid resolution)** | **0.1 MW** |
| Tick size | €0.01/MWh (NOK/SEK/DKK 0.01) |
| Currency | EUR, NOK, SEK or DKK orders; prices calculated in EUR |
| Order types | Curve, block, exclusive groups, flexible orders (part of exclusive groups) |
| **Order resolution** | **15, 30 or 60 min** (product codes `_QH`, `_HH`, `_H`) |
| Block orders | Volume limit 900 MW; minimum duration 1 delivery period; max 100 per portfolio; max 10 exclusive groups with ≤ 24 blocks each; linked blocks 7 levels, ≤ 6 per level, ≤ 13 in total; spread blocks max 3 pairs |
| Price steps | ≤ 200 per delivery period |
| **Technical price limits** | **−600 to +4,000 €/MWh** (NOK/SEK −7,800/+52,000; DKK −4,800/+32,000) |
| Cash settlement | D (owing to NP) / D+1 (owing from NP) (§1.3) |

**Intraday continuous (SIDC/IDCT)** (§3, pp. 6–7):

| Parameter | Value |
|---|---|
| Matching | Continuous, automatic when matching orders exist |
| **Trading opens** | after day-ahead prices are published, **normally 14:00 CET on D-1**; 96 delivery periods |
| Trade lot / tick | 0.1 MW / €0.01/MWh; EUR only |
| Order types | Limit, Fill-or-Kill, Immediate-or-Cancel, Iceberg (min. clip 5 MW); linked baskets ≤ 100 orders (FOK) |
| **Products** | **1 hour, quarter-hour, block orders** |
| Price limits | **−9,999 to +9,999 €/MWh** |
| **Gate closure (minutes before delivery)** | **NO 60**, SE 60, DK 60, FI 0, EE/LV/LT 30 |
| Cash settlement | D+2 / D+3 |

**Intraday auctions (SIDC/IDA)** (§4, pp. 8–9):

| | IDA1 | IDA2 | IDA3 |
|---|---|---|---|
| Name | 15:00 auction | 22:00 auction | 10:00 auction |
| Auction start | 14:40 | 21:40 | 09:40 |
| **Gate closure** | **15:00 (D-1)** | **22:00 (D-1)** | **10:00 (D)** |
| Auction end | 15:20 | 22:20 | 10:20 |
| **Delivery** | 00:00–24:00 next day (96 periods) | 00:00–24:00 next day (96 periods) | **12:00–24:00 same day (48 periods)** |

- Countries: EE, FI, LT, LV, DK, NO, SE. **Order resolution 15 min** in all Nordic/Baltic zones. Trade lot 0.1 MW. Curve, block, exclusive and flexible orders. Block limit 900 MW. Price limits −9,999/+9,999 €/MWh. Gate opening normally 60 days before D (§4.4). Cash settlement D+1 / D+2.
- **Pricing:** the document refers to the "Auction method" in the Market Regulations and doesn't state the rule. Day-ahead and IDA are uniform-price (marginal) auctions under SDAC/SIDC; continuous intraday is pay-as-bid, first come first served (see `ph24_nordpool_intraday`) (unverified from this document).

## Key findings
- (p. 4) Day-ahead: GC 12:00 D-1; 96 × 15-min delivery periods; orders at 15/30/60 min; 0.1 MW lot; −600/+4,000 €/MWh.
- (p. 6) Intraday continuous opens normally 14:00 D-1. Gate closure 60 min before delivery in NO. Hourly, quarter-hour and block products.
- (p. 8) IDA1/2/3 gate closures 15:00 D-1, 22:00 D-1 and 10:00 D. IDA3 covers 12:00–24:00 of D.

## Strengths
- The binding, current rule document, effective 28 May 2026, which matches the period of our thesis.

## Weaknesses / limitations
- Covers only Nord Pool's platform. EPEX SPOT also operates in Norway (`ph24_nve_norway_europe`). The pricing rule is not stated here. The `-layout` text of the §4.2 table is misaligned.

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where |
|---|---|---|
| Background 2.4: DA gate closure / opening | 12:00 CET D-1; normally 60 days before D | p. 4 §2.1; p. 5 §2.3 |
| Background 2.4 / model: DA MTU and order resolution | 96 × 15-min periods; 15/30/60-min orders | p. 4 §2.1; p. 5 §2.2 |
| Model: bid size and resolution | 0.1 MW trade lot; €0.01/MWh tick | p. 4 (DA); p. 6 (IDCT); p. 8 (IDA) |
| Model: price bounds | DA −600/+4,000 €/MWh; ID ±9,999 €/MWh | p. 4; p. 6; p. 8 |
| Model: block orders (e.g. pump blocks) | 900 MW limit; ≥ 1 delivery period; linked/exclusive groups | p. 4 |
| Background 2.4: continuous intraday | Opens about 14:00 D-1; GC 60 min before delivery in NO; hour, quarter-hour, block products | p. 6 §3.1–3.2 |
| Background 2.4: intraday auctions | IDA1/2/3 GC 15:00/22:00/10:00; delivery windows; 15-min resolution | p. 8 §4.2; p. 9 |
| Background 2.4: time convention | All times CET; clock-change days | p. 3 §1.2 |

## Useful quotes (with page numbers)
> "Gate Closure: 12:00 CET on D-1" (p. 4)

## Follow-up references to check (backward snowballing)
- Nord Pool Day-ahead Market Regulations and Intraday Market Regulations (pricing and matching rules).
- EPEX SPOT Nordic product specifications, for completeness.

