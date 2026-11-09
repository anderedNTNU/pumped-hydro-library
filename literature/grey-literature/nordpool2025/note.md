---
bibkey: nordpool2025
title: "Product Specifications -- Nordic/Baltic Market Areas"
authors: "Nord Pool AS"
year: 2025
venue: "Nord Pool Rulebook, Product Specifications (Nordic/Baltic), effective 'September 2025' (marked-up draft version)"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Superseded Sept-2025 (tracked-changes) version of Nord Pool's Nordic/Baltic product spec: 96 x 15-min DA delivery periods, GC 12:00 D-1, 0.1 MW lot, DA price limits -500/+4,000 EUR/MWh; replaced by the 28 May 2026 version (ph24_nordpool_specifications_2026)."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/120_Zotero_udatert_Product_Specifications_Nordic_Baltic_Market_Areas_september_2025.pdf
---

# Nord Pool Product Specifications, Nordic/Baltic (September 2025 version)

**Source:** Zotero copy (imported 28.10.2026) of the bib URL `.../product-specifications-nordic-and-baltic-september-2025.pdf`. `%PDF` OK, 10 pages. PDF metadata: created with Word for Microsoft 365 on **26 June 2025**, title "Report". Page numbers below are the printed page numbers, which equal the PDF page numbers.

**Important: this is a marked-up (tracked-changes) draft, not a clean rulebook text.** The extracted text contains deleted and inserted wording side by side, e.g. the footer "Effective from: 18 March[ ] September 2025" (no exact date filled in), "These This Product Specifications" (p. 3), "Minimum number of consecutiveduration of hours in Block Orders: 1 Delivery Periodhours" (p. 4), "2.22.3 Day-ahead Market Trading hoursGate Opening" (p. 5). Strike-through formatting is not visible in the text extraction, so for some fields it is impossible to tell from `source.txt` which value is the deleted one and which the new one (e.g. "Maximum amount of Block Orders within an Exclusive Group: 2964", p. 4, is probably "29" deleted and "64" inserted, or vice versa) (unverified). The examples refer to the day-ahead auction of 18 June 2025, which matches the originally planned 15-min MTU go-live of 11 June 2025 (see `ote2025mtu`), so this draft was probably prepared for that go-live and then re-dated to September 2025 after the postponement (unverified inference).

## Research question / purpose
n/a. Rulebook document specifying Nord Pool's physical-market products in the Nordic and Baltic areas: day-ahead (SDAC), intraday continuous (SIDC/IDCT) and intraday auctions (SIDC/IDA).

## Setting
- **System:** Nordic/Baltic bidding zones (NO, SE, FI, DK, LT, LV, EE; IDA granularity table lists NO1–NO5, SE1–SE4 etc., p. 10).
- **Markets:** day-ahead, intraday continuous, intraday auctions. Reserves are not covered.
- **Time:** all times CET; clock-change days have 23 or 25 hours (§1.2, p. 3).

## Method
n/a.

## Data / case: product parameters relevant for modelling PHS participation

**Day-ahead (§2.1, p. 4; §2.2–2.3, p. 5)**

| Parameter | Value in this version | Same in 28 May 2026 version? |
|---|---|---|
| Delivery periods | 24 h = **96 Delivery Periods** (15-min MTU) | yes |
| Gate closure | **12:00 CET on D-1** | yes |
| Gate opening | normally 60 days before D (§2.3, p. 5) | yes |
| Trade lot / tick | 0.1 MW / €0.01/MWh | yes |
| Order resolution | 15, 30, 60 min (`_QH`, `_HH`, `_PH`) | yes (2026 uses `_H` for 60 min, per `ph24_nordpool_specifications_2026` note) |
| Order types | "Hourly Curve Orders" (marked-up wording), block, exclusive groups, flexible | 2026: "Curve Orders" |
| Block orders | 900 MW limit; min. duration 1 Delivery Period; max 100 per portfolio | yes |
| Exclusive groups | **max 5 per portfolio** (2026: 10); blocks per group "2964" (garbled; 2026: 24) | changed |
| Price steps | max 200 per Delivery Period | yes |
| **Lower technical price limit** | **−500 €/MWh** (NOK/SEK −6,500; DKK −4,000) | **changed: −600 €/MWh in 2026** |
| Upper technical price limit | +4,000 €/MWh (NOK/SEK +52,000; DKK +32,000) | yes |
| Price thresholds | Baltic only: max +2,400, min −500 €/MWh; Nordic "–" | removed in 2026 |
| Settlement | D (owing to NP) / D+1 (owing from NP) (§1.3, p. 3) | yes |

**Intraday continuous (§3, pp. 6–7):** opens when DA prices are published, normally 14:00 CET; 96 delivery periods; 0.1 MW lot; EUR only; limit, FOK, IOC, iceberg (min. clip 5 MW); products 1 hour, quarter hour, block; price limits ±9,999 €/MWh; linked basket ≤ 100 orders (FOK). **Gate closure 60 min before delivery in NO**, SE, DK; FI 0 min; FI–EE border 30 min (p. 6). Settlement D+2 / D+3.

**Intraday auctions (§4, pp. 9–10):** IDA1 (GC 15:00 D-1, delivery 00–24 next day), IDA2 (GC 22:00 D-1, 00–24 next day), IDA3 (GC 10:00 D, 12:00–24:00 same day = 48 periods); auction start 14:40 / 21:40 / 09:40, end 15:20 / 22:20 / 10:20 (the `-layout` table on p. 9 is scrambled, read with care). 15-min resolution in all Nordic/Baltic zones; 0.1 MW lot; ±9,999 €/MWh; block limit 900 MW; gate opening normally 60 days before D (§4.4, p. 10). Settlement D+1 / D+2.

**Pricing rule:** not stated; the document refers to the "Auction method" in the Day-ahead / Intraday Market Regulations (pp. 4, 9).

## Key findings
- (p. 4) DA: 96 × 15-min delivery periods, GC 12:00 CET D-1, 0.1 MW lot, price limits −500/+4,000 €/MWh.
- (p. 6) Continuous intraday: GC 60 min before delivery in Norway.
- (p. 9) IDA1–3 gate closures 15:00 D-1, 22:00 D-1, 10:00 D.

## Strengths
- Documents the product set at the time of the 15-min MTU go-live in SDAC (1 October 2025), which is the start of our 15-min price data.

## Weaknesses / limitations
- **Superseded** by the version effective 28 May 2026 (`ph24_nordpool_specifications_2026`), which the thesis already cites.
- A tracked-changes draft with no exact effective date ("18 March[ ] September 2025"); some numbers are garbled in the extraction. Not a citable "clean" rulebook.

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where |
|---|---|---|
| Data: price bounds for the historical sample Oct 2025–May 2026 | DA technical limits −500/+4,000 €/MWh (Nordic); Baltic thresholds +2,400/−500 | p. 4 |
| Background 2.4: 15-min DA MTU | 96 Delivery Periods; 15/30/60-min orders | pp. 4–5 |
| Background 2.4: intraday GC in Norway | 60 min before delivery | p. 6 §3.2 |
| Background 2.4: IDA timing | GC 15:00 / 22:00 / 10:00; IDA3 covers 12–24 on D | p. 9 §4.2 |
| Prefer instead | Current version effective 28 May 2026 | `ph24_nordpool_specifications_2026` |

## Useful quotes (with page numbers)
> "Gate Closure: 12:00 CET on D-1" (p. 4)

## Follow-up references to check (backward snowballing)
- Nord Pool Day-ahead and Intraday Market Regulations (auction method / pricing).
- Clean (non-marked-up) Nord Pool spec effective 1 October 2025, if one exists.

