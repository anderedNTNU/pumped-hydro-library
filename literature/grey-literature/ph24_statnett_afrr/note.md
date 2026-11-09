---
bibkey: ph24_statnett_afrr
title: "Sekundærreserver – aFRR"
authors: "Statnett"
year: 2026
venue: "Statnett web page (statnett.no), published 10.12.2018, last updated 17.09.2026"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Statnett aFRR product page: automatic pro-rata activation by Statnett signal, FAT ≤ 5 min (pref. 2 min), min bid 1 MW, common Nordic aFRR capacity market since 7 Dec 2022 cleared D-1, no activation market until PICASSO."
---

# Secondary reserves – aFRR (Statnett web page, 2026)

**Source file:** `source.txt` (text of `<main>`), raw HTML `source.html`. Fetched 2026-11-04 from the bib URL (HTTP 200). Page last updated **17.09.2026** (before urldate 2026-10-20). Norwegian; cited by section heading.

## Research question / purpose
Product page for aFRR (automatic Frequency Restoration Reserve) for market participants: what it is, technical specs, today's market, future PICASSO connection, how to become a provider.

## Setting
- **System:** Norway / Nordic synchronous area.
- **Markets:** Nordic aFRR capacity market (aFRR CM); planned aFRR energy activation market via PICASSO.
- **Horizon and resolution:** daily D-1 clearing (hourly bids, per other sources).

## Method
n/a.

## Data / case
n/a. Lists qualified aFRR BSPs (Eviny, Hafslund Kraft, Hydro Energi, Lyse Produksjon, Sira-Kvina, Skagerak, Statkraft, Å Energi) — all hydropower producers.

## Key findings (by section)
- (Intro) aFRR is activated **automatically by Statnett** to bring frequency back to **50.00 Hz**, thereby **releasing the activated FCR**; also called LFC. Activation is handled in Statnett's control-centre system; automation activates aFRR **evenly among all providers in the Nordics (pro rata)** via a control signal to the BSP's control system.
- Today mainly production units deliver aFRR, but consumption or storage meeting the requirements can too.
- (Tekniske spesifikasjoner) **FAT max 5 min after the TSO signal; Statnett prefers ≤ 2 min. Minimum bid size 1 MW.** Communication via closed network / ICCP to Statnett SCADA (not over internet/ECP).
- (Dagens marked) aFRR introduced in the Nordics in 2013; TSOs historically prioritised morning/evening hours and hour shifts. **Common Nordic aFRR capacity market launched 7 December 2022**; need dimensioned per bidding zone; **Statnett is Market Operator; cleared every day before the operating day (D-1).** Finland joined with limitations from 25 Dec 2022. Procured volumes published quarterly ("Market information aFRR procurement", Q1–Q4 2026 PDFs listed).
- (Utvikling) aFRR CM developed further in the NBM programme; EB GL requires a common European capacity algorithm (COBRA).
- (PICASSO) Nordic TSOs **plan** to introduce an aFRR activation market via PICASSO: TSOs compute aFRR need per bidding zone; activation in **price order instead of pro rata**; BSPs may submit activation bids whether or not they took part in the capacity market.
- (Vil du levere aFRR?) Prequalification includes tests of communication and response time.

## Strengths
Authoritative, current product description; states min bid and FAT explicitly.

## Weaknesses / limitations
- Does not itself give gate times or energy pricing (see `ph24_statnett_reserve_overview` and `ph24_statnett_bsp_terms_2025`).
- "Planned" PICASSO connection: date not given; the energy-remuneration rule will change at go-live.

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where (section) |
|---|---|---|
| Background 2.4: aFRR purpose | Restore 50 Hz, release FCR | Intro paragraph |
| Background 2.4: activation mechanism | Automatic Statnett signal, pro rata | Intro paragraph |
| Background 2.4: response table aFRR | FAT ≤ 5 min (pref. 2 min); min bid 1 MW | "Tekniske spesifikasjoner" |
| Background 2.4: market design | Common Nordic aFRR CM since 7.12.2022, D-1 clearing, Statnett MO | "Dagens marked" |
| Background / future work: PICASSO | Planned activation market, price-order activation | "PICASSO" |
| Context: aFRR providers in Norway | Hydro producers only | "Vil du levere aFRR?" |

## Useful quotes (with page numbers)
> "Full aktiveringstid (FAT) for aFRR er i dag maksimalt 5 minutter etter sendt signal fra TSO … Minste budstørrelse er på 1MW." (section "Tekniske spesifikasjoner")

## Follow-up references to check (backward snowballing)
- "Implementasjonsguide aFRR CM", "aFRR Market Handbook" (linked).
- Market information aFRR procurement Q1–Q4 2026 (volumes; possibly useful for data).
- `ph24_statnett_afrr_specification_2023` (technical spec).

