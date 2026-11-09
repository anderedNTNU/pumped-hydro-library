---
bibkey: statnett2026b
title: "Primærreserver – FCR"
authors: "Statnett"
year: 2026
venue: "Statnett web page (statnett.no), published 09.11.2018, last updated 18.05.2026"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Statnett FCR product page: FCR-N 49.9–50.1 Hz, FCR-D up 49.9–49.5 Hz / down 50.1–50.5 Hz; D-2 auction before and D-1 after day-ahead; 2026: ~230 MW FCR-N per hour, FCR-D up all year in D-1, FCR-D down not bought; min bid 0.1 MW; bids indivisible."
---

# Primary reserves – FCR (Statnett web page, 2026)

**Source file:** `source.txt` (text of `<main>`), raw HTML `source.html`. Fetched 2026-11-04 from the bib URL (HTTP 200). Last updated **18.05.2026**. Norwegian; cited by section heading.

## Research question / purpose
Product page for FCR (Frequency Containment Reserves): physics, FCR-N/FCR-D, the Norwegian FCR market, technical requirements/prequalification, Q&A.

## Setting
- **System:** Norway.
- **Markets:** FCR-N and FCR-D in D-2 and D-1 auctions; mandatory "grunnleveranse".
- **Horizon and resolution:** daily auctions, hourly MTU (per `statnett2026c`).

## Method
n/a.

## Data / case
2026 volumes: FCR-N need ~230 MW every hour all year.

## Key findings (by section)
- (Intro) FCR is activated **automatically from measured frequency**; divided into **FCR-N** (normal operation) and **FCR-D** (disturbance).
- **FCR-N** active in **49.9–50.1 Hz**, limits deviations from normal structural imbalances. **FCR-D up** for under-frequency, active **49.9–49.5 Hz**; **FCR-D down** for over-frequency, active **50.1–50.5 Hz**. FCR stays active until aFRR and mFRR restore balance.
- (FCR-markedet) Market consists of a **D-2 and a D-1 auction**; providers choose one or both. **D-2 runs before the day-ahead market ("elspot"), D-1 after it, to cover "restbehov"**; the split was agreed with producers to avoid large re-planning after day-ahead clearing.
- Units > 10 MVA not awarded in the FCR market must run with max 12 % droop (mandatory base delivery, paid at a fixed rate).
- (Vil du levere FCR?) **Statnett buys FCR-N in D-2 and D-1; need ~230 MW every hour in 2026. In 2026 FCR-D up is bought in the D-1 auction all year**; amount depends on prequalified capacity. **"For øyeblikket kjøpes ikke FCR-D ned i Norge."**
- (Tekniske krav) Nordic technical requirements approved by Nordic regulators 3 April 2023, in force in Norway since 1 Jan 2024; transition period Q1 2024 to March 2028 for re-prequalification.
- (Q&A) **Min bid 0.1 MW from 1 July 2024.** D-2 deadline **17:30**, D-1 deadline **18:00**. (Older Q&A text: FCR-D up only May–Sept 2025, planned continuous from Jan 2026 — consistent with main text.) **FCR bids are indivisible.** Sampling 1 Hz. Meter per bidding zone required.
- (Q&A, LER) Limited-energy-reservoir units must reserve **134 % power and 1 h energy for FCR-N**, and **20 % opposite-direction power and 20 min energy for FCR-D**. (A PHS with large reservoirs is not normally LER, but useful contrast.)
- (Q&A) Non-delivery settlement example with D-2 and D-1 obligations (cheapest obligation covered first).

## Strengths
Current procurement status (what is actually bought), clear frequency bands, auction sequencing relative to day-ahead.

## Weaknesses / limitations
- Q&A contains stale lines (2025 schedule).
- Response-time numbers not given (see `ph24_statnett_reserve_overview`).

## Use it for… (lookup guide)
| Use in our thesis | What the page provides | Where (section) |
|---|---|---|
| Background 2.4: FCR-N/FCR-D frequency bands | 49.9–50.1; 49.9–49.5; 50.1–50.5 Hz | Intro paragraphs |
| Background 2.4: what Statnett buys | FCR-N (D-2, D-1); FCR-D up (D-1, all year 2026); FCR-D down not bought | "Vil du levere FCR?" |
| Background 2.4: sequencing vs day-ahead | D-2 before spot, D-1 after spot for residual need | "FCR-markedet" |
| Background 2.4: deadlines, min bid | 17:30 (D-2), 18:00 (D-1); 0.1 MW; indivisible bids | Q&A |
| Context: FCR-N volume | ~230 MW per hour in 2026 | "Vil du levere FCR?" |
| Model (if FCR added): LER reservation | 134 % power + 1 h energy (FCR-N); 20 % + 20 min (FCR-D) | Q&A on LER |

## Useful quotes (with page numbers)
> "For øyeblikket kjøpes ikke FCR-D ned i Norge." (section "Vil du levere FCR?")

## Follow-up references to check (backward snowballing)
- Norsk støttedokument for FCR-kravene (v2024-01-05).
- Nordic FCR balancing capacity market – implementation guide for BSP (ver 260130) — suggests FCR is moving to Nordic MMS.

