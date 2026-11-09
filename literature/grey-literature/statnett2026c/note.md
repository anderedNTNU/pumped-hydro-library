---
bibkey: statnett2026c
title: "Vilkår for FCR-markedet (cover: Forslag til vilkår for marked for FCR), gjeldende fra 28.04.2026"
authors: "Statnett"
year: 2026
venue: "Statnett market terms, appendix to guidelines for fos § 9; PDF, 17 pp."
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Binding Norwegian FCR market terms: D-2 (00:00–17:30 CET) and D-1 (00:00–18:00 CET) auctions, 60-min MTU, min bid 0.1 MW, max 70 MW per unit, marginal pricing, FCR-N energy at mFRR price, FCR-D energy at 0 EUR/MWh."
---

# Statnett FCR market terms (Statnett, 2026)

**Source file:** `source.pdf` / `source.txt` (fetched 2026-11-04; bib URL works). Norwegian. Printed page numbers = PDF page numbers. Cover: "Forslag til vilkår for marked for FCR — Gjeldende fra 28.04.2026".

## Research question / purpose
Binding terms for bidding, acceptance, reporting and settlement of Frequency Containment Reserves (FCR-N, FCR-D up, FCR-D down) in Norway. Appendix to the guidelines for the system-operation regulation (fos § 9), approved by RME (Art. 1, p. 3).

## Setting
- **System:** Norway, all bidding zones.
- **Markets:** FCR capacity market (D-2 and D-1 auctions) and settlement of FCR activation energy.
- **Horizon and resolution:** daily auctions, **MTU 60 min** (Art. 8, p. 8).

## Method
- **Model type / uncertainty / solution method / assumptions:** n/a (regulatory text).

## Data / case
n/a.

## Key findings (rules)
- (Art. 2.1l, p. 3) "marginalpris" = all accepted bids of the same product get the same price, set by the last accepted bid; (2.1p, p. 4) "pay-as-bid" defined.
- (Art. 5, pp. 5–6) Qualification: trading licence (RME), eSett agreement, Ediel, Fifty user, BRP agreement; units prequalified per SO GL art. 155 and the Nordic technical requirements (`ph24_nordic_tsos_fcr_requirements_2025`).
- (Art. 7.2g, p. 7) Energy storage in its own station group.
- (Art. 8, p. 8) **MTU = 60 minutes.**
- (Art. 10.1, p. 8) Units with mandatory "grunnleveranse" may participate without new prequalification until 27.03.2028 (Statnett can still require it in the D-2 FCR-N and D-1 FCR-D auctions).
- (Art. 10.7, p. 9) **Committed FCR must be reserved in the planning phase; intraday/bilateral trading, mFRR bids, mFRR-D bids and aFRR bids shall not affect the ability to deliver committed FCR.**
- (Art. 10.8, p. 9) If ramping rules (fos § 8b) conflict with FCR delivery, deliver as well as possible; obligation deemed fulfilled.
- (Art. 11, pp. 9–10) **D-2 auction: opens D-2 00:00 CET, closes D-2 17:30 CET, results by 18:30 CET. D-1 auction: opens D-1 00:00 CET, closes D-1 18:00 CET, results by 19:00 CET.** Bids binding after GCT.
- (Art. 12, pp. 10–11) Bids per station group and bidding zone, **separate for FCR-N, FCR-D up, FCR-D down**, per MTU; offered capacity may not be in other obligations (12.1e). Content: MW, **EUR/MW**, direction, MTU, location. **Min bid 0.1 MW; max 70 MW per unit (SO GL art. 156.6); a unit delivering FCR-N and FCR-D at the same time max 100 MW up and 100 MW down.** Price two decimals, 0.01–9 999 EUR/MW. No bids from units at gate-opening limit ("slagbegrenser").
- (Art. 13, pp. 11–12) One price per bidding zone and MTU, separately per auction and product; **marginal pricing**; bids selected in price order in a Norwegian optimisation (some cheaper bids may be skipped to minimise total cost); bids behind congestions can be made unavailable without compensation.
- (Art. 14, p. 12) Special purchases (grid) and extra purchases after GCT (up to one hour before the operating hour) are **pay-as-bid**.
- (Art. 17, pp. 13–14) Obligations can be transferred bilaterally within a bidding zone (notify ≥ 1 h before operating hour).
- (Art. 19, pp. 15–16) Capacity settled per MTU on the obligation, weekly via eSett; reported plans compared with obligations.
- (Art. 20, p. 16) **Activated FCR-N energy (MWh) settled at the mFRR balancing-energy price (EUR/MWh) in the direction of regulation (via BSP-terms Art. 67); activated FCR-D up and down energy priced at 0 EUR/MWh.**
- (unnumbered "Avregning av FCR-kapasitet som ikke er levert", p. 16; Art. 21 per TOC) Non-delivered capacity: payment cut at clearing price × 1; with D-2 and D-1 obligations in the same MTU, delivered capacity is allocated first to the cheapest obligation.

## Strengths
Primary, binding source; exact deadlines, bid limits and pricing rules for FCR.

## Weaknesses / limitations
- Norwegian; cover says "Forslag" (proposal) although it is the version in force from 28.04.2026.
- Does not contain the response-time requirements (63 % / 60 s etc.); those are in `ph24_statnett_reserve_overview` and the Nordic technical requirements.
- Does not say which products are actually procured (FCR-D down not bought at present: see `statnett2026b`).
- Article numbering in body skips the heading of Art. 21 (formatting error in source).

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where (article, page) |
|---|---|---|
| Background 2.4: timing table (FCR D-2, FCR D-1) | D-2: 00:00–17:30 CET; D-1: 00:00–18:00 CET; results 18:30 / 19:00 CET | Art. 11 (pp. 9–10) |
| Background 2.4: MTU | 60 min | Art. 8 (p. 8) |
| Background 2.4: min bid FCR | 0.1 MW; max 70 MW per unit; 100 MW combined FCR-N+FCR-D | Art. 12.3 (pp. 10–11) |
| Background 2.4: activation-energy settlement | FCR-N at mFRR balancing price in direction; FCR-D at 0 EUR/MWh | Art. 20 (p. 16) |
| Background/model: earlier commitments restrict later trading | FCR must be reserved in planning; intraday, mFRR, aFRR must not affect it | Art. 10.7 (p. 9); Art. 12.1e (p. 10) |
| Background: pricing | Marginal pricing per zone/MTU/product; special and extra purchases pay-as-bid | Art. 2.1l, 13.2 (p. 11), 14 (p. 12) |
| Background: symmetric vs directional | Separate bids for FCR-N, FCR-D up, FCR-D down | Art. 12.1c (p. 10) |

## Useful quotes (with page numbers)
> "Det aktiverte volumet FCR-D oppregulering i MWh og FCR-D nedregulering i MWh prises til 0 EUR/MWh." (Art. 20.2, p. 16)

## Follow-up references to check (backward snowballing)
- "Metode om vilkår for leverandør av FCR og vilkår for balanseansvarlige" (referred to in Art. 2.2b and Art. 20.1; the Art. 67 reference is to the mFRR price rule).
- Nordic technical requirements for FCR (= `ph24_nordic_tsos_fcr_requirements_2025`).

