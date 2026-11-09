---
bibkey: esett2026
title: "Nordic Imbalance Settlement Handbook: Instructions and Rules for Market Participants, Version 5.4"
authors: "eSett Oy"
year: 2026
venue: "eSett handbook, dated 1 June 2026, status 'For contractual basis'; 145 pp."
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Nordic imbalance and balancing-service settlement by eSett: 15-min ISP, single imbalance price = mFRR price in the dominating direction (Norway/Sweden), day-ahead price (VoAA + IC) when no activation; capacity and activated reserves invoiced weekly via eSett; storage > 1 MW metered as separate production and consumption."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/03_Reservemarkeder_og_vilkar/Innlimte_referanser_2026-10-29/esett2026.pdf
---

# Nordic Imbalance Settlement Handbook v5.4 (eSett, 2026)

**Source file:** `source.pdf` / `source.txt` (copied from the inbox; fetched 29.10.2026 from `https://www.esett.com/app/uploads/2026/06/NBS-Handbook-v5.4.pdf`, landing page `https://www.esett.com/handbook/`). **Printed page number = PDF page − 1** (cover unnumbered). Page numbers below are printed numbers.

## Research question / purpose
Not research. The contractual rulebook for the Nordic Imbalance Settlement (NBS): how eSett (owned by Energinet, Fingrid, Statnett, Svenska kraftnät) settles BRP imbalances and BSP balancing services in Denmark, Finland, Norway and Sweden, including reporting, pricing, invoicing and collateral (pp. 8–11). Procurement of balancing services is explicitly outside its scope (Sec. 1.2, p. 9).

## Setting
- **System:** Nordic market balance areas (MBA = bidding zone), incl. NO1–NO5.
- **Markets:** imbalance settlement (BRP), balancing-service settlement (BSP: FCR, aFRR, mFRR capacity and energy), reconciliation (Sweden).
- **Horizon and resolution:** **15-minute imbalance settlement period (ISP)** (Terminology, p. 2).

## Method
- **Model type / uncertainty / solution method / assumptions:** n/a (rulebook).

## Data / case
n/a.

## Key findings
- (p. 2, Terminology) **ISP = 15 minutes.** Imbalance = allocated (physical) volume − final (traded) position, incl. imbalance adjustment, per ISP.
- (p. 10, Sec. 1.4) The settlement follows Title V of EB GL (Regulation (EU) 2017/2195).
- (p. 14, Ch. 2) **Single imbalance** model: each BRP is financially liable for its imbalance; in balancing-service settlement, **balancing capacity and balancing energy are financially compensated between TSOs and BSPs**, and BSP regulation imbalances (activated vs delivered) are calculated.
- (pp. 44–46, Sec. 4.6) **Energy storages:** registered with two metering points (consumption = charging, production = discharging); **netting of consumption and production within an ISP not permitted** unless national rules allow; production plan required in Norway if storage ≥ 1 MW. Norway (Table 9, p. 45): storage > 1 MW → separate production and consumption metering points, PT15M resolution, type "Energy Storage (B25)". The examples are batteries; whether a large PHS plant is registered as "Energy Storage" or as production + consumption is not stated (unverified).
- (p. 56, Table 11) BRPs report bilateral trades up to 45 min before the ISP in Sweden and Norway.
- (p. 57, Table 12) BSPs report delivered reserves by 10:00 D+2, updates by 12:00 D+13.
- (p. 67, Sec. 5.4.6.1) TSOs report activated reserves per regulation object (and, for Statnett, Energinet, Svk, **contracted reserve volumes and amounts**) to eSett the day after delivery. The **15-min mFRR EAM uses the MARI standard product**; ramping before and after the activation ISP is included in energy volumes, while activation amounts are paid for the activation ISP(s) at its price (Figure 19: scheduled activation affects three ISPs, direct activation four).
- (p. 68, Sec. 5.4.6.4) **Norway:** Statnett reports a **production ramp** derived from production plans, assuming the ramp starts 5 min before and ends 5 min after the ISP shift, aligned with mFRR ramping.
- (p. 70, Ch. 6) Preliminary settlement daily from D+2; **final settlement 13 days after delivery**.
- (p. 73, Sec. 6.3) All reserve **capacity is purchased from the BSP**; activated **up** energy is purchased from the BSP, activated **down** energy is sold to the BSP; regulation imbalance = activated − delivered.
- (p. 79, Table 21) Imbalance-price inputs: mFRR up/down energy prices, volume-weighted aFRR up/down prices, dominating direction, VoAA + IC.
- (p. 80, Table 22; Sec. 7.1.1) **Norway and Sweden: single price** — in up-regulation ISPs both positive and negative imbalances are priced at the **mFRR up-regulation price**, in down-regulation ISPs at the **mFRR down-regulation price**. Denmark and Finland use the higher/lower of mFRR and volume-weighted aFRR (Finland: volume-weighted when mFRR activated).
- (p. 81, Sec. 7.1.4) With no activation (or equal up and down), imbalance price = **VoAA + IC = day-ahead price** (VoAA = average of lowest up-bid and highest down-bid; IC adjusts it to the day-ahead price).
- (pp. 82–83, Sec. 7.4) Fees: volume fee (EUR/MWh on production and consumption), imbalance fee, weekly fee; set nationally.
- (p. 87, Sec. 8.1, Figure 24) BSP invoice rows: sold activated reserves, purchased activated reserves, **purchased contracted reserves (MW)**, per type. Invoicing is weekly (Ch. 8).
- (p. 125, Sec. 11.2.5) Production plans are no longer used in the imbalance calculation; a Production Plan KPI monitors plan quality per BRP/MBA.
- (pp. 133–135, Change log) v4.x–5.x: 15-min ISP and 15-min metering now reported in Norway and Sweden; pricing updated for PICASSO (aFRR) participation; mFRR EAM launch; Denmark moved to the Finnish pricing model (listed under the 2025 versions; exact version unverified because of table layout).

## Strengths
- The authoritative operational description of how imbalances and reserves are settled and priced in the Nordics; current (June 2026).

## Weaknesses / limitations
- Long operational/IT handbook; most chapters (structure, metering, collateral, messaging) irrelevant for us.
- Binding Norwegian pricing rules are in Statnett's EB GL art. 18 terms (`ph24_statnett_bsp_terms_2025`, Arts. 94–100), which the thesis already cites; this handbook confirms them.
- Storage rules are written with batteries in mind.

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where (printed page) |
|---|---|---|
| Background 2.4: imbalance settlement period | 15-min ISP | p. 2 (Terminology) |
| Background 2.4: single imbalance price, Norway | mFRR up price in up-ISPs, mFRR down price in down-ISPs | p. 80, Table 22; Sec. 7.1.1 |
| Background 2.4: price when no balancing | VoAA + IC = day-ahead price | p. 81, Sec. 7.1.4 |
| Background 2.4: capacity vs energy payments | Capacity purchased from BSP; activated up purchased, down sold; invoice rows | p. 73, Sec. 6.3; p. 87, Fig. 24 |
| Background 2.4: mFRR ramping and settlement | MARI product; ramp spans 3 (scheduled) or 4 (direct) ISPs; paid at activation ISP | p. 67, Sec. 5.4.6.1, Fig. 19 |
| Background: Norwegian production ramp | Ramp ±5 min around ISP shift, aligned with mFRR | p. 68, Sec. 5.4.6.4 |
| Background: storage metering | Separate production/consumption, no netting in ISP, PT15M in Norway > 1 MW | pp. 44–46, Sec. 4.6, Table 9 |
| Background: role of eSett | Owned by four Nordic TSOs; settles BRPs and BSPs | pp. 8–11, 14 |

## Useful quotes (with page numbers)
> "In up-regulation ISPs, the price of negative and positive imbalances is the mFRR energy up-regulation price." (Sec. 7.1.1, p. 80)

## Follow-up references to check (backward snowballing)
- Commission Regulation (EU) 2017/2195 (EB GL), Title V (imbalance settlement).
- Statnett, "Metode om vilkår for leverandør av balansetjenester …" (= `ph24_statnett_bsp_terms_2025`).

