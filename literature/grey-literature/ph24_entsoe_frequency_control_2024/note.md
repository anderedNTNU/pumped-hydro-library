---
bibkey: ph24_entsoe_frequency_control_2024
title: "Overview of Frequency Control in the Nordic Power System"
authors: "Nordic Analysis Group (ENTSO-E)"
year: 2024
venue: "ENTSO-E report, version 2.1, 7 May 2024; PDF, 30 pp."
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Nordic TSOs' technical overview of FCR-N, FCR-D, FFR, aFRR and mFRR: purposes, activation bands and times, dimensioning (600 MW FCR-N, 300–400 MW aFRR, Statnett ~39 % shares), national procurement designs, and NBM changes (15-min ISP, PICASSO/MARI); Figure 1 (p. 6) shows the reserve activation sequence."
---

# Overview of Frequency Control in the Nordic Power System (Nordic Analysis Group / ENTSO-E, 2024)

**Source file:** `source.pdf` / `source.txt` (fetched 2026-11-04; bib URL works). Printed page numbers = PDF page numbers. Revision index (p. 27): v1.0 2021-08-26 … v2.1 2024-04-19 ("Updated outdated information").

## Research question / purpose
Technical overview of frequency control in the Nordic synchronous area for stakeholders: system states, reserve products, dimensioning, procurement per TSO, emergency measures, operation, future changes.

## Setting
- **System:** Nordic synchronous area (Energinet DK2, Fingrid, Statnett, Svenska kraftnät).
- **Markets:** FCR-N, FCR-D, FFR, aFRR (CM), mFRR (EAM + national CMs); DA/ID context.
- **Horizon and resolution:** status as of spring 2024 (60-min ISP; 15-min ISP announced).

## Method
n/a (descriptive report).

## Data / case
Reserve shares 2024 (Tables 1–3).

## Key findings
- (p. 5) Frequency depends on power imbalance, kinetic energy (inertia) and reserves; **more production than consumption → frequency increases, and vice versa**. Containment process (FCR) vs restoration process (FRR restores 50 Hz and releases FCR). FFR: very fast stepwise response in low-inertia situations.
- (p. 6) **Figure 1: example of a frequency disturbance and illustration of the different reserve activations** (FCR-N not included because a large disturbance is illustrated).
- (p. 7) Standard frequency range 50 Hz ± 100 mHz; transient ±1000 mHz up to 60 s, then within ±500 mHz; target ≤ 15 000 min/yr outside standard range (Nordic aim 10 000); reserves restored 15 min after a disturbance.
- (p. 9) Day-ahead gate closure 12:00 CET, results 12:45 CET; trading periods 1 h "will in the near future change to 15 minutes".
- (p. 10) **FCR-N**: linear in 49.9–50.1 Hz, **symmetric**, ~**63 % within 60 s and 95 % within 3 min**. **FCR-D** up/down separate, linear 49.5–49.9 / 50.1–50.5 Hz, **86 % within 7.5 s**, energy after 7.5 s ≥ 3.2 s × steady-state power; static FCR-D variant. **FFR** (since 2020): up only, thresholds 49.5/49.6/49.7 Hz, full activation **0.7–1.3 s**, support duration 30 s or 5 s.
- (p. 11) **aFRR**: up and down, control signal **every 10 s**, activated continuously, **max FAT 5 min**. **mFRR**: up and down, **FAT 15 min** (2024 value), only manual product; mFRR EAM (Nordic) + national mFRR CMs.
- (pp. 12–14) Dimensioning: **FCR-N 600 MW** Nordic (±1 % of 60 GW); 2024 FCR shares: **Statnett 39.10 %** (Table 1); FCR-D covers reference incident (e.g. Oskarshamn 3, NordLink); FFR keeps nadir > 49.0 Hz, 300 MW assumption, Statnett 117 MW (Table 2); **aFRR Nordic min 300 MW, max 400 MW**, procured almost every hour, set quarterly; Statnett 46 %/43 % up/down = 138/129 MW (Table 3); mFRR dimensioned on national reference incident and increasingly on stochastic imbalances.
- (p. 15) Statnett FCR: D-2 and D-1 markets, **marginal pricing**, hourly bids per bidding zone; congestion-driven extra purchases pay-as-bid; base delivery (grunnleveranse).
- (p. 16) FCR-D same design as FCR-N (Statnett). Statnett FFR: seasonal Profil/Flex, marginal pricing, activation costs reimbursed.
- (p. 17) **aFRR CM: common Nordic, daily, hourly bids, opens D-7, closes D-1 07:30; marginal pricing; procured capacity obliged to deliver aFRR energy**; PICASSO in future.
- (pp. 17–18) mFRR EAM: opens 14 days before, **GCT 45 min before the operational hour** (2024), Nordic merit order, marginal pricing set after the hour; separate up/down bids. Statnett: national mFRR CM daily (GCT 07:30 D-1, results 08:10) plus a **seasonal winter CM**; EAM preliminary GCT 21:30 D-1.
- (pp. 24–25) NBM: ISP 60 → 15 min, PICASSO (aFRR) and MARI (mFRR), automated AOF, ACE-based balancing per bidding zone, lower bid sizes possible. Updated FCR requirements in force Sept 2023, transition to Sept 2028.

## Strengths
Single authoritative Nordic overview with physical explanation and numbers; good figure for the activation sequence.

## Weaknesses / limitations (outdated as of Nov 2026)
- mFRR FAT 15 min → now **12.5 min** (`ph24_statnett_bsp_terms_2025` Art. 59).
- 60-min ISP/MTU → **15-min ISP** and 15-min mFRR EAM MTU now in force.
- mFRR EAM GCT "45 min before the operational hour" → now 45 min before each quarter-hour.
- Statnett min mFRR bid sizes have since fallen to 1 MW.
- Technical rather than market-economic; no PHS-specific content.

## Use it for… (lookup guide)
| Use in our thesis | What the report provides | Where (page/section) |
|---|---|---|
| Background 2.4: Figure (frequency response and reserve activation) | Figure 1, example disturbance with FFR/FCR-D/aFRR/mFRR activations | p. 6, Sec. 1 |
| Background 2.4: direction of frequency change | Surplus production → frequency rises, and vice versa | p. 5 |
| Background 2.4: product definitions, bands, times | FCR-N, FCR-D, FFR, aFRR, mFRR | pp. 10–11, Sec. 2 |
| Background 2.4: market size | FCR-N 600 MW; aFRR 300–400 MW; Statnett shares | pp. 12–14, Tables 1–3 |
| Background 2.4: procurement designs per TSO | FCR D-2/D-1 marginal, aFRR CM, mFRR EAM/CM | pp. 15–18, Sec. 4 |
| Background 2.4: frequency quality limits | ±100 mHz; 15 000 min/yr target | p. 7, Sec. 1.2 |
| Background / discussion: NBM changes | 15-min ISP, PICASSO/MARI, AOF | pp. 24–25, Sec. 7.1 |

## Useful quotes (with page numbers)
> "FCR-N is a symmetrical product, which means that the FCR providing entity has to be able to both decrease and increase its power production or consumption" (p. 10)

## Follow-up references to check (backward snowballing)
- SO GL (EU 2017/1485), EB GL (EU 2017/2195), Nordic SOA Annex LFCR (refs [1]–[3], p. 29).
- Nordic FCR technical requirements (Sept 2023) → `ph24_nordic_tsos_fcr_requirements_2025`.

