---
bibkey: sogl2017
title: "Commission Regulation (EU) 2017/1485 of 2 August 2017 establishing a guideline on electricity transmission system operation (SO GL)"
authors: "European Commission"
year: 2017
venue: "Official Journal of the European Union, L 220, 25.8.2017, pp. 1–120"
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "EU legal basis for FCR/FRR/RR: definitions, Nordic frequency-quality parameters (±100 mHz, 15 min time to restore), FCR full activation 30 s at ±500 mHz, aFRR activation delay ≤ 30 s, continuous FCR availability, LER rules, 5-yearly prequalification."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/Innlimte_referanser_2026-10-29/sogl2017.pdf
---

# System Operation Guideline, SO GL (European Commission, 2017)

**Source file:** `source.pdf` / `source.txt`, copied from the inbox. It is the **original OJ text (L 220, 25.8.2017, pp. 1–120)**, not the consolidated version, so later amendments are not included. **Provenance caveat:** per the inbox KILDEINFO, EUR-Lex showed a robot check, so the PDF was obtained from a third-party archive (Certifico). The text carries the OJ headers and page numbers (checked), but for the thesis the citation should point to the official EUR-Lex/OJ publication (CELEX 32017R1485). PDF page = OJ page number.

## Research question / purpose
Not research. EU regulation (network code) that sets harmonised rules for transmission system operation: operational security, operational planning and scheduling, and **load-frequency control and reserves** (Part IV). It defines the reserve categories FCR, FRR (automatic and manual) and RR, the frequency-quality parameters per synchronous area, and minimum technical, prequalification and provision requirements for reserve providers. Entry into force on the 20th day after publication (Art. 192, p. 112), i.e. September 2017.

## Setting
- **System:** all EU synchronous areas (CE, GB, IE/NI, Nordic, Baltic); Nordic-specific values in Annexes III and V.
- **Markets:** none directly (balancing markets are in EB GL 2017/2195); defines the reserve *products* that the markets procure.
- **Horizon and resolution:** n/a.

## Method
- **Model type / uncertainty / solution method / assumptions:** n/a (legal text).

## Data / case
n/a.

## Key findings (rules, with article and OJ page)
**Definitions (Art. 3(2), pp. 4–12)**
- (Art. 3(2)(6)–(8), p. 5) **FCR** = active power reserves available to contain system frequency after an imbalance; **FRR** = active power reserves available to restore frequency to nominal (and power balance to schedule for multi-LFC-area systems); **RR** = reserves to restore/support the required level of FRR.
- (Art. 3(2)(9)–(11), p. 5) Reserve provider, reserve providing unit, reserve providing group.
- (Art. 3(2)(95), p. 9) "Reserve capacity" = amount of FCR, FRR or RR that needs to be available to the TSO.
- (Art. 3(2)(99)–(101), p. 9) Automatic FRR; **automatic FRR activation delay** (setpoint → start of delivery); **automatic FRR full activation time** (setpoint → full activation/deactivation).
- (Art. 3(2)(111)–(112), p. 10) FCR full activation frequency deviation; **FCR full activation time** (reference incident → full FCR).
- (Art. 3(2)(143), p. 12) **Manual FRR full activation time** (setpoint change → full activation/deactivation of mFRR).
- (Art. 3(2)(146), p. 12) Prequalification = verifying compliance of a reserve providing unit/group with TSO requirements.
- (Art. 3(2)(155)–(157), p. 12) Standard frequency range, standard frequency deviation, steady-state frequency deviation.
- (Art. 3(2)(58), p. 7) Reference incident = maximum instantaneous power deviation considered in FCR dimensioning.

**System states and frequency quality**
- (Art. 18, p. 21) System states (normal/alert/emergency); alert state e.g. if reserve capacity is reduced by > 20 % for > 30 min, or frequency deviation persists beyond trigger times.
- (Art. 127, pp. 76–77) Nominal frequency 50 Hz; defaults in Annex III.
- (Annex III, Table 1–2, p. 116) **Nordic:** standard frequency range **±100 mHz**; maximum instantaneous deviation **1 000 mHz**; maximum steady-state deviation **500 mHz**; **time to restore frequency 15 minutes**; frequency restoration range ±100 mHz; alert state trigger time 5 min; target max **15 000 minutes per year** outside the standard range.

**Load-frequency control structure (Arts. 139–145, pp. 82–85)**
- (Art. 140, p. 82) Mandatory processes: frequency containment process (FCP) and frequency restoration process (FRP); RR process optional.
- (Art. 143, p. 84) FRP control target: regulate FRCE to zero within the time to restore frequency; **for CE and Nordic, progressively replace activated FCR by FRR**.
- (Art. 145, pp. 84–85) Each LFC area implements an **automatic FRP (aFRP)** — closed loop, FRCE in, aFRR setpoint out, PI controller — and a **manual FRP (mFRP)** operated through manual activation instructions.

**FCR (Title 5, Arts. 153–156, pp. 90–95)**
- (Art. 153, pp. 90–91) FCR dimensioned at least annually; must cover at least the reference incident (Nordic: largest single unit/HVDC/line loss, separately up and down); Nordic may use a probabilistic dimensioning with ≤ once in 20 years insufficiency; initial FCR obligations shared by net generation + consumption.
- (Art. 154(1)–(2), p. 91) FCR must meet Annex V; TSOs of a synchronous area may add **common additional properties** (basis for `nordictsos2022` and the Nordic technical requirements). FCR activated by a proportional governor or monotonic piecewise-linear characteristic (Art. 154(6)).
- (Annex V, p. 117) **Nordic FCR:** frequency measurement accuracy 10 mHz; insensitivity + dead band ≤ 10 mHz; **FCR full activation time 30 s if frequency is outside the standard range; full activation frequency deviation ±500 mHz** (these apply to FCR-D in practice, see `nordictsos2022` p. 5).
- (Art. 155, pp. 92–93) Prequalification: TSO confirms completeness within 8 weeks, decides within 3 months; **re-assessment at least every 5 years** or when equipment/requirements change.
- (Art. 156(4), p. 93) **"An FCR provider shall guarantee the continuous availability of FCR" during the obligation period** (except forced outage).
- (Art. 156(6), pp. 93–94) Loss of one unit: **share per FCR providing unit ≤ 5 % of the FCR required for the Nordic synchronous area** (origin of Statnett's 70 MW cap, see `statnett2026c`).
- (Art. 156(7)–(13), pp. 94–95) Energy reservoirs: unlimited reservoir → activate as long as the deviation persists; **limited energy reservoir (LER)** → continuously available in normal state; in alert state full activation for 15–30 min; recovery within 2 h after alert state (Nordic/CE).

**FRR (Title 6, Arts. 157–159, pp. 95–98)**
- (Art. 157(2), pp. 95–96) FRR dimensioned per LFC block from ≥ 1 year of historical imbalance records, probabilistic; positive and negative FRR **determined separately**, each ≥ the dimensioning incident and covering LFC-block imbalances **≥ 99 % of the time**; aFRR and mFRR full activation times ≤ time to restore frequency (15 min Nordic).
- (Art. 158(1), pp. 96–97) FRR minimum technical requirements: one reserve connecting TSO; activate per setpoint; **automatic FRR activation delay ≤ 30 s**; full automatic/manual FRR capacity within the respective full activation time; real-time monitoring of scheduled and actual output; ramping-rate requirements of the LFC block.
- (Art. 159, pp. 97–98) FRR prequalification analogous to FCR (8 weeks / 3 months; valid for whole LFC block; re-assessed at least every 5 years).

## Strengths
- Primary EU legal source; gives the authoritative definitions of FCR/FRR/RR and full activation times used in all TSO documents.
- Nordic parameter values tabulated (Annex III, Annex V).

## Weaknesses / limitations
- Original 2017 text; not consolidated. Product parameters actually used in Norway (aFRR 5 min, mFRR 12.5 min FAT, FCR-N 63 %/60 s, FCR-D 86 %/7.5 s) are set in national/Nordic documents, not here.
- Copy obtained from a third-party archive (see provenance caveat).
- Does not cover market design (bidding, pricing, MTU): that is EB GL 2017/2195 and Statnett's terms (`ph24_statnett_bsp_terms_2025`).

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where (article, OJ page) |
|---|---|---|
| Background 2.4: definitions of FCR, FRR, RR | Legal definitions | Art. 3(2)(6)–(8), p. 5 |
| Background 2.4: aFRR vs mFRR as processes | aFRP closed-loop PI controller; mFRP via manual instructions | Art. 145(1),(4),(5), pp. 84–85 |
| Background 2.4: FRR replaces FCR | FRP progressively replaces activated FCR (Nordic) | Art. 143(1)(b), p. 84 |
| Background 2.4: Nordic frequency quality | ±100 mHz standard range; 15 min time to restore; 15 000 min/yr target | Annex III, p. 116 |
| Background 2.4: FCR full activation | 30 s, ±500 mHz (Nordic) | Annex V, p. 117 |
| Background/model: aFRR activation delay | ≤ 30 s | Art. 158(1)(d), pp. 96–97 |
| Background: full activation time definitions | aFRR FAT, mFRR FAT | Art. 3(2)(101), p. 9; Art. 3(2)(143), p. 12 |
| Model: reserve must stay available | FCR continuous availability; FRR full capacity within FAT | Art. 156(4), p. 93; Art. 158(1)(f)–(g), p. 97 |
| Background: up/down reserves separately dimensioned | Positive/negative FRR ≥ dimensioning incident, ≥ 99 % of imbalances | Art. 157(2)(e)–(i), pp. 95–96 |
| Background: unit cap | ≤ 5 % of Nordic FCR per providing unit | Art. 156(6)(a), p. 93 |
| Background: limited energy reservoirs | Continuous availability; 15–30 min in alert state; 2 h recovery | Art. 156(8)–(13), pp. 94–95 |
| Background: prequalification | 8 weeks / 3 months; re-assessment ≥ every 5 years | Art. 155, pp. 92–93; Art. 159, pp. 97–98 |

## Useful quotes (with page numbers)
> "An FCR provider shall guarantee the continuous availability of FCR, with the exception of a forced outage…" (Art. 156(4), p. 93)

## Follow-up references to check (backward snowballing)
- Commission Regulation (EU) 2017/2195 (EB GL), electricity balancing: market rules (bidding, pricing, settlement).
- Commission Regulation (EU) 2016/631 (RfG), Art. 15(2)(d): frequency-sensitive-mode ranges.
- Nordic synchronous area operational agreement (SAOA) and methodologies under Art. 118 (e.g. `nordictsos2022`).

