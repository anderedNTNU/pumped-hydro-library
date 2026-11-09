---
bibkey: nordictsos2021technical
bibkey_provisional: true
title: "Technical Requirements for Fast Frequency Reserve Provision in the Nordic Synchronous Area – External document, Version 1.1"
authors: "Nordic TSOs (published on ENTSO-E template; distributed by Statnett)"
year: 2021
venue: "Nordic TSOs technical requirements, 11 January 2021; 17 pp."
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Formal Nordic FFR requirements: activation at 49.7/49.6/49.5 Hz with full activation within 1.3/1.0/0.7 s; long (≥ 30 s) or short (≥ 5 s) support duration; ready for a new activation within 15 min; ≤ 50 MW behind a single point of failure."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/03_Reservemarkeder_og_vilkar/Tilleggsdokumenter/68_Statnett_2025d_Raske_frekvensreserver_FFR_VEDLEGG_IKKE_SELVE_KILDEN.pdf
---

# Technical requirements for FFR, v1.1 (Nordic TSOs, 2021)

**Source file:** `source.pdf` / `source.txt` (copied from the inbox). The inbox marks it as an **attachment, not the cited source**: it is the PDF linked from Statnett's FFR page (`statnett2026d`), original URL `https://www.statnett.no/globalassets/for-aktorer-i-kraftsystemet/marked/reservemarkeder/ffr/technical-requirements-for-ffr-v1.1.pdf` (see `68_Statnett_2025d_KILDEINFO.md`). Printed page = PDF page. No author is printed beyond the ENTSO-E template footer; the Nordic TSOs are the issuing parties (inferred from title and context).

## Research question / purpose
Specify the formal technical requirements for Fast Frequency Reserve (FFR) providing entities, the prequalification process, compliance tests and real-time telemetry/data logging (Summary, p. 3).

## Setting
- **System:** Nordic synchronous area.
- **Markets:** FFR (procured nationally; Statnett's market is described in `statnett2026d`).
- **Horizon and resolution:** n/a (second-scale response).

## Method
- **Model type / uncertainty / solution method / assumptions:** n/a (technical requirements).

## Data / case
n/a.

## Key findings
- (p. 3; Table 1, p. 6) Three equivalent activation alternatives, chosen by the provider: **A: 49.7 Hz, full activation ≤ 1.30 s; B: 49.6 Hz, ≤ 1.00 s; C: 49.5 Hz, ≤ 0.70 s.**
- (p. 3; Sec. 2.3, p. 8) **Support duration:** long ≥ 30 s (no limit on deactivation rate) or short ≥ 5 s (deactivation ≤ 20 % of prequalified capacity per second).
- (Sec. 2, p. 6) FFR quantified in MW, positive = more infeed or load reduction; **max 50 MW of FFR behind a single point of failure**.
- (Sec. 2.2, p. 7) Maximum overdelivery 20 % (TSO may allow up to 35 %).
- (Sec. 2.4–2.5, p. 9) Recovery ≤ 25 % of prequalified capacity; for short duration not before 15 s after the end of support; **ready for a new activation within 15 minutes**; full cycle < 15 min (p. 8).
- (Sec. 2.6, pp. 9–10) Maintained FFR capacity for a generator = min(P_max − P_setpoint − C_other, C_prequal), where C_other is other ancillary-service capacity already allocated (e.g. FCR-D): FFR headroom competes with other reserves.
- (Sec. 1.3, p. 5) Application data for generation units: rated MVA, inertia constant H, converter type, governor; for storage: rated MW, MWh, upper/lower energy limits.
- (Sec. 1.1–1.2, p. 4) Prequalification: 8 weeks completeness / 3 months decision (as SO GL); reassessment at least every 5 years.

## Strengths
- Primary technical source for the "~1 second" FFR response that the thesis attributes to `statnett2026d`.

## Weaknesses / limitations
- Version 1.1 of January 2021; a later version may exist (unverified). FFR is out of our model scope.

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where |
|---|---|---|
| Background 2.4: FFR response time | 49.7/49.6/49.5 Hz → 1.3/1.0/0.7 s | p. 3; Table 1, p. 6 |
| Background 2.4: FFR duration | ≥ 30 s (long) or ≥ 5 s (short); ready again within 15 min | p. 3; pp. 8–9 |
| Model analogy: reserve headroom | Maintained capacity = P_max − P_setpoint − other reserves | Sec. 2.6, pp. 9–10 |
| Background: unit limit | ≤ 50 MW behind a single point of failure | Sec. 2, p. 6 |

## Useful quotes (with page numbers)
> "1.0 s maximum full activation time for the activation level 49.6 Hz" (p. 3)

## Follow-up references to check (backward snowballing)
- Statnett FFR market terms ("Vilkår for FFR-marked", 2026) — referenced from `statnett2026d`.

