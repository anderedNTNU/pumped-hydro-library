---
bibkey: ph24_nordpool_day_ahead
title: "Day-ahead market"
authors: "Nord Pool"
year:
venue: "nordpoolgroup.com web page (undated; footer '© Nord Pool 2020')"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Nord Pool's day-ahead explainer: closed auction for next-day delivery, social-welfare matching via SDAC/Euphemia under TSO network constraints, capacities published 10:00, GC 12:00 CET, prices about 12:45. Text still says 'hourly' (outdated since the 15-min MTU)."
---

# Day-ahead market (Nord Pool web page)

**Fetched:** 2026-11-04 from https://www.nordpoolgroup.com/en/the-power-market/Day-ahead-market/ (HTTP 200). `source.txt` / `source.html`. Undated; the footer says "© Nord Pool 2020". The site's news teasers include "Transition to 15-minute Market Time Unit (MTU)". Locations are given as ¶ = paragraph of the main text.

## Research question / purpose
n/a. Nord Pool's introductory page on its day-ahead market.

## Setting
- **System:** Nord Pool day-ahead in 15 countries and 21 bidding zones.
- **Markets:** day-ahead (SDAC).

## Method
n/a.

## Data / case
- ¶1: customers "sell or buy energy for the next 24 hours in a closed auction". Orders are matched "to maximize social welfare while taking network constraints provided by transmission system operators into consideration".
- ¶2: 15 countries, 21 bidding zones, > 300 buyers and sellers, > 2,000 orders per day, about 500 TWh per year.
- ¶3: "sets bidding zone prices for each hour" (**outdated**: the MTU has been 15 min since the SDAC go-live on 1 Oct 2025, unverified date; the current product specification has 96 delivery periods, `ph24_nordpool_specifications_2026` p. 4).
- ¶4: a range of order types. The DA result is "the baseline for planning the next 24-hour period", with later changes in the intraday market.
- ¶5: **10:00 CET** available capacities on interconnectors and in the grid are published. **Bids until 12:00 CET** for delivery the next day.
- ¶6: orders are matched in **SDAC** using the common algorithm **Euphemia**. "The single price for each hour and each bidding zone is set where the curves for sell price and buy price meet, taking into account network constraints", i.e. **uniform (marginal) pricing**. Again "each hour" is outdated.
- ¶7: prices are announced at **12:45 CET or later**, then individual results. "The physical obligation to deliver/consume" follows, as Nord Pool nominates the trades to imbalance settlement.
- The page does not mention NEMO status.

## Key findings
- Day-ahead is a closed, uniform-price auction with gate closure at 12:00 CET D-1. Its result is a physical delivery obligation.

## Strengths
- Plain-language description of the auction mechanics and timing from the operator.

## Weaknesses / limitations
- Undated and partly outdated ("each hour", "hourly clearing prices"). Use the product specifications for the MTU and order-resolution facts.

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where |
|---|---|---|
| Background 2.4: DA auction principle | Closed auction, social-welfare maximisation, TSO network constraints | ¶1 |
| Background 2.4: DA timeline | Capacities 10:00; GC 12:00 CET; prices about 12:45 CET | ¶5, ¶7 |
| Background 2.4 / model: pricing rule | Single (marginal) price per MTU and bidding zone via Euphemia/SDAC | ¶6 |
| Background 2.4: physical obligation | Trades nominated to imbalance settlement | ¶7 |
| Background 2.4: market size | 15 countries, 21 zones, about 500 TWh/yr | ¶2 |

## Useful quotes (with page numbers)
> "Orders are matched to maximize social welfare while taking network constraints provided by transmission system operators into consideration." (¶1)

## Follow-up references to check (backward snowballing)
- Nord Pool / SDAC announcement of the 15-min MTU go-live (for the exact date).
- A source for Nord Pool's NEMO designation in Norway (e.g. NVE-RME or ACER NEMO list).

