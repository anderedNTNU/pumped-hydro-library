---
bibkey: ph24_statnett_reserve_overview
title: "Hvordan fungerer reservene?"
authors: "Statnett"
year: 2026
venue: "Statnett web page (statnett.no), published 26.08.2024, last updated 02.09.2026"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "One-page Statnett summary of FFR, FCR-N/D, aFRR and mFRR: purpose, symmetry, response times (FCR-N 63 %/60 s, 95 %/3 min; FCR-D 86 %/7.5 s, 100 %/30 s; aFRR 5 min; mFRR 2.5 + 10 min ramp), gate closures and how capacity vs activation is paid."
---

# How the reserves work (Statnett web page, 2026)

**Source file:** `source.txt` (text of `<main>`), raw HTML in `source.html`. Fetched 2026-11-04 from the bib URL (HTTP 200). Page dates: published 26.08.2024, **last updated 02.09.2026** (before the bib urldate 2026-10-20, so the snapshot should match what the authors saw). Norwegian. No page numbers; cited by section heading.

## Research question / purpose
Short product overview of the four Norwegian reserve categories for market participants; links to the reserve-market calculator.

## Setting
- **System:** Norway / Nordic synchronous area.
- **Markets:** FFR, FCR (FCR-N, FCR-D), aFRR (capacity market), mFRR (capacity + activation market).
- **Horizon and resolution:** n/a.

## Method
n/a (informational web page).

## Data / case
n/a.

## Key findings (by section)
**FFR**
- Purpose: slow the rate of frequency change. Two products: **FFR Profil** (armed daytime and all weekend in summer, min bid **1 MW**) and **FFR Flex** (armed on weekly order, min bid **5 MW**); procured once a year for the summer season. Activation options: full response in 0.7 s below 49.5 Hz, 1.0 s below 49.6 Hz, 1.3 s below 49.7 Hz. Delivery 5 or 30 s.

**FCR**
- Purpose: stop the frequency change and stabilise at a new level. **FCR-N** acts in the normal band **49.9–50.1 Hz**; it is a **symmetric product** ("må leveres til samme pris enten om frekvensen går opp eller ned"); linear response, activated automatically from **local frequency measurement**.
- **FCR-D**: outside the normal band at larger disturbances; **prices per direction (up/down)**; purchase of FCR-D "assessed year by year".
- **Response:** FCR-D **86 % within 7.5 s and 100 % at 30 s**; FCR-N **63 % within 60 s and 95 % within 3 min**.
- Both FCR markets are procured **daily**.

**aFRR**
- Purpose: bring frequency back towards 50 Hz. Activation currently distributed **pro rata** among providers. Physical response activated automatically by a **signal from Statnett** (deviation from planned production); ICCP link between SCADA systems required. **Fully activated within 5 min, preferably 2 min.**
- **Asymmetric** (separate prices up/down). Capacity market cleared the day before; **bid deadline 07:30 D-1**; bids per hour; one price per hour per bidding zone.
- "I dag er dette kun et kapasitetsmarked": activated volume compensated at the **regulating-power price in the direction of regulation (the imbalance price) in the relevant hour** ("i aktuell time"). With PICASSO, aFRR CM acceptance will instead create an obligation to bid into an aFRR activation market.

**mFRR**
- Purpose: maintain balance until a new market balance is reached. **Asymmetric.** Capacity-market winners must bid into the activation market; **capacity payment is independent of whether the activation bids are used**.
- Capacity market cleared the day before; **deadline 07:30 D-1**; hourly bids, one price per hour per bidding zone.
- **Activation market closes 45 min before the operating hour** ("driftstimen" — the page has not been updated to the 15-min MTU; per `ph24_statnett_bsp_terms_2025` Art. 61.3 it is 45 min before each 15-min MTU).
- Activation response: 2.5 min from order to start; then linear ramp over 10 min to full response; hold 5 min; ramp down 10 min unless re-ordered.

## Strengths
Compact, authoritative, covers all products in one place; good for a background table.

## Weaknesses / limitations
- Web page, wording simplified; some phrases lag the rules ("driftstimen", "aktuell time" after the 15-min ISP/MTU change).
- Response percentages are simplified time-domain statements; the formal FCR requirements are in `ph24_nordic_tsos_fcr_requirements_2025` (FCR-D: 86 % at 7.5 s is Requirement 2, p. 18; FCR-N is specified in frequency domain).
- Does not give FCR-D frequency bands or minimum bid sizes for FCR/aFRR/mFRR (those are on the product pages).

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where (section) |
|---|---|---|
| Background 2.4: FCR-N band and symmetry | 49.9–50.1 Hz, symmetric, local frequency, linear | "Primærreserver (FCR)" |
| Background 2.4: response table FCR-N/FCR-D | 63 %/60 s, 95 %/3 min; 86 %/7.5 s, 100 %/30 s | "Primærreserver (FCR)" |
| Background 2.4: aFRR activation and FAT | Automatic signal, pro rata, ≤ 5 min (pref. 2 min) | "Sekundærreserver (aFRR)" |
| Background 2.4: aFRR energy pricing today | Imbalance (regulating-power) price in direction of regulation | "Sekundærreserver (aFRR)" |
| Background 2.4: mFRR CM → EAM obligation, payment independent of activation | Stated explicitly | "Tertierreserver (mFRR)" |
| Background 2.4: mFRR activation profile | 2.5 min + 10 min ramp + 5 min hold + 10 min ramp down | "Tertierreserver (mFRR)" |
| Background 2.4: FFR products | Profil/Flex, min bid 1/5 MW, 0.7–1.3 s | "Raske frekvensreserver (FFR)" |
| Model: asymmetric capacity products | aFRR and mFRR: separate up/down prices | aFRR and mFRR sections |

## Useful quotes (with page numbers)
> "Betalingen i kapasitetsmarkedet er uavhengig av om bud i aktiveringsmarkedet blir kjøpt eller ikke." (section "Tertierreserver (mFRR)")

## Follow-up references to check (backward snowballing)
- Statnett "reservemarkedskalkulator" (linked; not fetched).
- Product pages: `statnett2026b`, `ph24_statnett_afrr`, `ph24_statnett_mfrr`, `statnett2026d`.

