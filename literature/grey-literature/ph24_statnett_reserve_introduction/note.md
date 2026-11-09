---
bibkey: ph24_statnett_reserve_introduction
title: "Hva er reservemarkedene?"
authors: "Statnett"
year: 2026
venue: "Statnett web page (statnett.no), published 06.01.2023, last updated 18.03.2026"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Statnett intro: imbalances from forecast errors and faults are handled by Statnett as system operator through four reserve types (FFR, FCR, aFRR, mFRR) activated in sequence; Nordic sharing of reserve volumes; NBM brings Nordic aFRR/mFRR capacity markets and PICASSO/MARI."
---

# What are the reserve markets? (Statnett web page, 2026)

**Source file:** `source.txt` (text of `<main>`), raw HTML `source.html`. Fetched 2026-11-04 from the bib URL (HTTP 200). Last updated **18.03.2026**. Norwegian; cited by section heading.

## Research question / purpose
Introductory page for newcomers: why reserves exist, the four reserve types, the activation sequence, Statnett's role, upcoming changes (NBM).

## Setting
- **System:** Norway; Nordic synchronous area (Norway, Sweden, Finland, Eastern Denmark/Zealand).
- **Markets:** reserve markets in general; mentions spot, intraday and long-term contracts for context.
- **Horizon and resolution:** n/a.

## Method
n/a.

## Data / case
n/a.

## Key findings (by section)
- (Lead) There will always be deviations between production and consumption → imbalances handled by **Statnett as system operator ("systemansvarlig")**; the main tool is the reserve markets.
- (Hva er reserver?) The system must always be in balance to keep **50 Hz**; if production ≠ consumption the frequency changes (direction not stated here). Planning: financial/long-term contracts months/years ahead; spot, intraday and reserve-market clearing the day before and towards operation. Actors should trade themselves into balance; remaining imbalances handled in real time with reserves.
- (Reservemarkedene …) Statnett buys products in reserve markets; actors are **paid to adjust consumption or production** when needed. Imbalances from **forecast deviations or structural deviations** between plans and actual consumption; example: more/less wind than forecast, covered by hydro. **Faults** (e.g. line outage in bad weather) can change frequency a lot and fast → larger reserve volumes needed.
- (Hvilke typer reserver finnes?) **Four types in Norway: FFR, FCR, aFRR, mFRR**, activated at different times.
- (Hva skjer …) Sequence: FFR slows the frequency change → FCR stops it and stabilises at a new level → aFRR brings frequency back to the normal band → mFRR maintains balance until a new market balance.
- (Statnett sin rolle) Statnett coordinates operation; common synchronous area; reserve volumes allocated in a **common Nordic agreement**; geographic distribution requirements. Links to the ENTSO-E Nordic frequency-control report (= `ph24_entsoe_frequency_control_2024`).
- (Endringer fremover) Work on updated technical requirements; **Nordic Balancing Model (NBM)**: common Nordic capacity markets for aFRR and mFRR and connection to **PICASSO and MARI**.

## Strengths
Plain-language overview; good for the opening of the reserves subsection.

## Weaknesses / limitations
- No numbers; does not state the direction of frequency change (production < consumption → falling) explicitly; no PHS-specific content.
- The term used is "systemansvarlig" (system operator); TSO status is implied, not stated.

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where (section) |
|---|---|---|
| Background 2.4: why reserves are needed | Imbalances from forecast errors and faults; reserves handle residual imbalance | "Hva er reserver?", "Reservemarkedene håndterer …" |
| Background 2.4: Statnett's role | System operator, coordinates operation, Nordic agreement on reserve volumes | "Hva er Statnett sin rolle?" |
| Background 2.4: activation sequence FFR→FCR→aFRR→mFRR | Ordered description | "Hva skjer når ubalansen oppstår …" |
| Background 2.4: upcoming changes | NBM, Nordic CMs, PICASSO/MARI | "Endringer fremover" |

## Useful quotes (with page numbers)
> "I Norge bruker vi fire forskjellige typer reserver og alle fire aktiveres på ulike tidspunkt for å skape en jevn balansering" (section "Hvilke typer reserver finnes?")

## Follow-up references to check (backward snowballing)
- `ph24_entsoe_frequency_control_2024` (linked).
- "Nordic TSOs – Batteries in the Nordic reserve markets, April 2025" (linked PDF; possibly relevant for storage participation).

