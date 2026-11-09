---
bibkey: ph24_statnett_mfrr
title: "Tertiærreserver – mFRR"
authors: "Statnett"
year: 2026
venue: "Statnett web page (statnett.no), published 31.10.2018, last updated 13.02.2026"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Statnett mFRR product page: separate capacity market (daily, hourly, national in Norway) and Nordic energy activation market (15-min, merit order, marginal pricing); min bid 1 MW, FAT ≤ 12.5 min; GCT to change 45 → 25 min at MARI."
---

# Tertiary reserves – mFRR (Statnett web page, 2026)

**Source file:** `source.txt` (text of `<main>`), raw HTML `source.html`. Fetched 2026-11-04 from the bib URL (HTTP 200). Last updated **13.02.2026**. Norwegian; cited by section heading.

## Research question / purpose
Product page for mFRR (manual Frequency Restoration Reserve): role, capacity market (mFRR CM), energy activation market (mFRR EAM), pricing, MARI.

## Setting
- **System:** Norway, per price area; Nordic EAM.
- **Markets:** mFRR CM and mFRR EAM; mentions mFRR-D (disturbance reserve).
- **Horizon and resolution:** CM daily with hourly resolution; EAM orders every quarter-hour.

## Method
n/a.

## Data / case
n/a.

## Key findings (by section)
- (Intro) mFRR is activated to keep balance between production, consumption and transmission in each price area; **it releases the activated aFRR** so that aFRR is available for new imbalances; also used to relieve grid overloads. **Two markets: a capacity market and an activation market.**
- mFRR is "the slowest and most energy-rich reserve": **each bid ≥ 1 MW, activation time ≤ 12.5 min, ordered every quarter-hour.** Balancing process is automatic (algorithms analyse need and order activations); operators can intervene. Outsourcing of activation handling allowed. Prequalification covers both CM and EAM.
- (Kapasitetsmarkedet) mFRR CM: providers are **paid to guarantee participation in the activation market**; both up and down secured; production and consumption can bid (power-intensive industry typical for fast demand changes). **Cleared daily with hourly resolution on a common Nordic platform; in Norway currently a national capacity market**, while Sweden, Denmark and Finland have a common one. Volume covers expected normal imbalances and large incidents, considering transfer capacity.
- (Aktiveringsmarkedet) mFRR EAM is a **common Nordic balancing market**; bids with price; sorted in a common Nordic list; cheapest first; each price area keeps its own balance but can get support from neighbours if transfer capacity is available. Statnett orders every quarter-hour, plus extra orders when needed.
- (Marginalprising) Bids selected in price order; **for each MTU the price is set by the most expensive accepted bid and all accepted bids get that price**; congestion → area price differences. **"Alle reservemarkedene har marginalprising."** Out-of-merit bids (skipped for bid properties) do not set the price and get the best of marginal price and bid price.
- (MARI) Nordic EAM uses the same algorithm as MARI; Nordic TSOs will connect jointly. For providers: no big technical changes, but **gate closure changes from 45 to 25 min before the operating quarter-hour**; direct activations will then be done in MARI.
- Links: "Market handbook FRR CM" (PDF); expired mFRR EAM terms (01.01.2024–03.03.2025).

## Strengths
Current, explicit on the CM/EAM split, min bid, FAT and pricing principle.

## Weaknesses / limitations
- No gate times for the CM (see `ph24_statnett_bsp_terms_2025` Art. 33 or the overview page).
- MARI connection date not given → GCT 45 min will become outdated.

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where (section) |
|---|---|---|
| Background 2.4: role of mFRR | Releases aFRR, keeps price-area balance, congestion relief | Intro |
| Background 2.4: two markets | Capacity market + activation market | Intro, "Kapasitetsmarkedet", "Aktiveringsmarkedet" |
| Background 2.4: response table mFRR | Min bid 1 MW, activation ≤ 12.5 min, ordered every quarter-hour | Intro (2nd paragraph) |
| Background 2.4: pricing | Marginal pricing per MTU; all reserve markets marginal | "Marginalprising" |
| Background 2.4: Norwegian mFRR CM is national | Norway national CM; SE/DK/FI common | "Kapasitetsmarkedet" |
| Discussion / future changes | GCT 45 → 25 min before operating quarter-hour at MARI | "MARI" |

## Useful quotes (with page numbers)
> "For mFRR er det to markeder, et kapasitetsmarked og et aktiveringsmarked." (intro)

## Follow-up references to check (backward snowballing)
- Market handbook FRR CM (linked PDF).
- mFRR-D page (disturbance reserve).

