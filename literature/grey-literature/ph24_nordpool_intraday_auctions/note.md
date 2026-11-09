---
bibkey: ph24_nordpool_intraday_auctions
title: "About the SIDC Intraday Auctions (IDAs)"
authors: "Nord Pool"
year: 2026
venue: "Nord Pool Support (knowledge-base article 8000111575), modified 17 April 2026"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "SIDC intraday auctions, live since 13 June 2024, three a day: IDA1 GC 15:00 and IDA2 GC 22:00 (delivery 00-24 next day), IDA3 GC 10:00 (delivery 12-24 same day), 15-min MTU in all Nordic zones; curve, block and exclusive-group orders."
---

# About the SIDC Intraday Auctions (Nord Pool Support article)

**Fetched:** 2026-11-04 from https://support.nordpoolgroup.com/support/solutions/articles/8000111575-about-the-sidc-intraday-auctions-idas- (HTTP 200). `source.txt` / `source.html`. The article shows "Modified on: Fri, 17 Apr, 2026 at 8:04 AM". Locations are given by heading.

## Research question / purpose
n/a. Support article for traders on the pan-European SIDC intraday auctions.

## Setting
- **System:** Nordic/Baltic and CORE bidding zones on the Nord Pool platform.
- **Markets:** intraday auctions (IDA).

## Method
n/a.

## Data / case
- Intro: "live in production since **13 June 2024** and are run **three times a day**".
- **§ Timing in Production:**
  - IDA1: GCT **15:00 CET**, delivery 00:00–24:00 the following day
  - IDA2: GCT **22:00 CET**, delivery 00:00–24:00 the following day
  - IDA3: GCT **10:00 CET**, delivery **12:00–24:00 the same day**
- "The auctions offer products with resolution of **15 min MTU** in all bidding zone[s]". The table lists DK1, DK2, FI, SE1–SE4, **NO1–NO5**, BE, NL, FR, the German TSO zones (TBW, AMP, TTG, 50Hz), AT, EE, LT, LV, PL.
- **§ Available Products** (described for the test auctions): curve orders (one per area per portfolio), block orders (normal, profile, linked) and exclusive group orders. It refers to the Product Specifications for the latest rules.
- Test environment: test IDAs have gate closures 10 min (Nordic/Baltic) or 20 min (CORE) after production. Production auctions are listed as "manually executed (only for exceptional cases…)" in the test table.
- Pricing: not stated. IDAs are uniform-price auctions coupled through SIDC (unverified from this page).

## Key findings
- Three daily IDAs (15:00, 22:00, 10:00 CET) with 15-min MTU in the Norwegian zones, live since 13 June 2024.

## Strengths
- Short, current, with explicit gate closures and delivery windows.

## Weaknesses / limitations
- A support article, not a rule document. The binding version is `ph24_nordpool_specifications_2026` §4. No pricing rule.

## Use it for… (lookup guide)
| Use in our thesis | What the article provides | Where |
|---|---|---|
| Background 2.4: IDA timing | GC 15:00 / 22:00 / 10:00 CET; delivery windows | § Timing in Production |
| Background 2.4: IDA start date | Live since 13 June 2024 | Intro |
| Background 2.4: resolution | 15-min MTU incl. NO1–NO5 | § Timing in Production (table) |
| Background 2.4: order types | Curve, block (normal/profile/linked), exclusive groups | § Available Products |

## Useful quotes (with page numbers)
> "The SIDC Intraday Auctions have been live in production since 13 June 2024 and are run three times a day." (intro)

## Follow-up references to check (backward snowballing)
- ENTSO-E / SIDC documentation on the IDA methodology (ACER Decision 01/2019, unverified).

