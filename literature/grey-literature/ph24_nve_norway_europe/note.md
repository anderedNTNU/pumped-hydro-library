---
bibkey: ph24_nve_norway_europe
title: "Norway and the European power market"
authors: "NVE-RME (Norwegian Energy Regulatory Authority)"
year: 2016
venue: "nve.no web page, published 28.01.2016 (content partly from 2015)"
peer_reviewed: false
methods: []
review_sections: [electricity-markets, price-volatility]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "NVE-RME overview: five Norwegian bidding zones reflecting congestion, European DA coupling via Euphemia, Nord Pool and EPEX SPOT both active, water value as alternative value, flatter intraday but strong seasonal price profile in Norway. Published 2016, so partly outdated."
---

# Norway and the European power market (NVE-RME web page)

**Fetched:** 2026-11-04 from https://www.nve.no/norwegian-energy-regulatory-authority/wholesale-market/norway-and-the-european-power-market/ (HTTP 200). `source.txt` / `source.html`. The HTML shows **"Publisert 28.01.2016"**; there is no later update date. Locations are given by heading.

## Research question / purpose
n/a. Regulator's overview of key figures, gains from cross-border trade, bidding zones and DA market coupling.

## Setting
- **System:** Norway and its interconnections; the Nordic synchronous area.
- **Markets:** day-ahead (coupled), intraday, balancing (mFRR common merit order).

## Method
n/a.

## Data / case
**Intro bullets** (2015-era data):
- Production about 130 TWh in a normal year, varying with inflow.
- **96 % hydro** (Statkraft gives 88 % for 2024 in `statkraft_hydropower`).
- "hydropower storage possibility is **85 TWh**".
- 2015 net export 14.8 TWh; 5-year average 11.3 TWh; net import 7.6 TWh in 2011.
- In 2015 Nord Pool area consumption was 402 TWh, of which 374 TWh (93 %) was traded in DA.

**§ Trading power between countries:**
- Norway's flexible hydro vs Danish wind vs Swedish and Finnish thermal. Export during snowmelt and high precipitation. Import when Denmark is windy, "possible for the Norwegian hydropower producers to **save water in the hydro reservoirs for later, when the water has a higher value**".
- Interconnections raise welfare but have distributional effects: more export capacity raises the exporting zone's price.
- **Water values:** "the water value is the alternative value, if used in a later point in time instead".
- **Price profile:** prices in adjacent countries "often fluctuate more within a day than in Norway where we typically have a flatter load curve". There are "relatively large price variations between seasons, with **low Norwegian prices during the Summer**". Denmark has small seasonal differences, so Norway normally exports more in summer.

**Further text (no headings):**
- NO, SE, FI and DK2 share one synchronous area. The Nordic TSOs run a **common Nordic merit order list for mFRR** and a common System Operation Agreement.
- **"Two power exchanges operate in both the day-ahead and intraday market in Norway, these are Nord Pool and EPEX SPOT."**
- **Five bidding zones (NO1–NO5)** reflecting structural congestion. No constraints are given to the market within zones. TSOs set cross-zonal capacities daily. DA capacity is physically firm. Different zones can have different prices.
- Prices give short-run (next-day planning) and long-run (maintenance, investment) signals. Price differences indicate the value of grid expansion.

**§ The European Day-Ahead market coupling:**
- Market-based dispatch since 1971 (Samkjøringen). Coupled via **PCR / EUPHEMIA**, which maximises social welfare under cross-zonal constraints.
- DAM gate closure 12:00, "12–36 hours before physical delivery". "**Prices and flow are calculated at an hourly basis**" (outdated; 15-min MTU now). Publication usually 12:42 CET.
- Intraday cross-zonal trading possible. "a common trading platform for intraday (**XBID**) is currently being developed" (**outdated**: XBID/SIDC went live in 2018, unverified date).
- Cross-border NTC table (as on the page): NO–SE 3,695 MW; NO–DK Skagerrak 1–4 1,700 MW ("100 MW reserved for aFRR most of the time"); NorNed 700 MW; NordLink 1,400 MW; NSL 1,400 MW, all "in operation". NordLink and NSL entered operation in 2020–2021, so the table has been updated since 2016, although the text says otherwise (unverified).

## Key findings
- Norway has five bidding zones whose prices can diverge because of transmission constraints. Norwegian prices are flat within the day but seasonal (low in summer).
- Water value is the opportunity (alternative) value of using water later.

## Strengths
- An official regulator source for market structure. A neat lay definition of water value and of the Norwegian price pattern.

## Weaknesses / limitations
- **Outdated:** published 2016, with 2015 statistics, hourly DA, "XBID being developed" and PCR terminology. Several facts have changed: the 15-min MTU, SIDC live, flow-based capacity calculation in the Nordics since 2024 (unverified date).

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where |
|---|---|---|
| Background 2.4: Norway's bidding zones | Five zones NO1–NO5 reflecting congestion; prices can differ; no intra-zonal constraints | Text after "§ Trading power…" |
| Background 2.4: exchanges in Norway | Nord Pool **and** EPEX SPOT operate DA and ID | same |
| Background 2.4: DA coupling | Euphemia, social-welfare maximisation, GC 12:00 (12–36 h before delivery) | § European Day-Ahead market coupling |
| Theory 3.x: water value intuition | "alternative value, if used at a later point in time" | § Trading power between countries |
| Background 2.5: Norwegian price pattern | Flat within the day; large seasonal variation; low summer prices | § Trading power between countries |
| Background 2.4: balancing | Common Nordic mFRR merit order list | text after § Trading power |
| Background: storage size | 85 TWh hydro storage; 96 % hydro (old) | intro bullets |
| Background: interconnectors | NTC table | end of page |

## Useful quotes (with page numbers)
> "the water value is the alternative value, if used in a later point in time instead" (§ Trading power between countries)

## Follow-up references to check (backward snowballing)
- A current NVE-RME or Statnett page on Nordic flow-based market coupling and the 15-min MTU (to replace the outdated parts).
- NVE energy statistics for current hydro share and reservoir capacity.

