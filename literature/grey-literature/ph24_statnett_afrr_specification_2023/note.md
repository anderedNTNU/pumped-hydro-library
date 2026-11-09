---
bibkey: ph24_statnett_afrr_specification_2023
title: "Appendix 1: Technical Product and Interface Specification for Delivery of Automatic Frequency Restoration Reserves (aFRR) to Statnett"
authors: "Statnett"
year: 2023
venue: "Statnett technical specification, Version June 2023 (rev. 4.0, 01-06-2023); PDF, 17 pp."
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Statnett aFRR technical spec: delta set-point added to the BSP schedule, 1 MW step, FAT 120 s preferred / 300 s max, 30 s max delay, accuracy rules; aFRR capacity 'shall not affect or be affected by' FCR, mFRR, day-ahead or XBID obligations; FCR and aFRR may come from the same asset."
---

# Statnett aFRR technical product and interface specification (Statnett, 2023)

**Source file:** `source.pdf` / `source.txt` (fetched 2026-11-04; bib URL works). English. Page numbers: only roman i–iii are printed; body cited by **section number**. Several broken cross-references in the source ("Feil! Fant ikke referansekilden.", TOC "2.7 … Feil! Bokmerke er ikke definert.") and the section numbers in the TOC differ slightly from the body (body: 2.1 Asset/production mix, 2.2 BSP schedules, 2.3 Parameters, 2.4 FAT, 2.5 Delay, 2.6 Set-point definition, 2.7 Accuracy, 2.8 Balancing capacity, 2.9 ACE mode, 2.10 Actual contribution, 2.11 Interplay FCR/aFRR, 2.12 Bidding limitations). Body numbering used below.

## Research question / purpose
Technical product parameters and SCADA/ICCP interface requirements that a BSP must meet to deliver aFRR to Statnett.

## Setting
- **System:** Norway; aFRR providing units (single asset or group; hydro, wind, solar, storage, consumption).
- **Markets:** aFRR capacity market (activation via Statnett set-point).
- **Horizon and resolution:** seconds to minutes (set-point every ≥ 4 s).

## Method
n/a.

## Data / case
n/a.

## Key findings
- (Definitions) aFRR purpose: release primary reserves and bring frequency back to 50.00 Hz. **Balancing capacity** = reserve volume the BSP has agreed to hold and for which it submits balancing-energy bids. **FAT** = time from TSO signal until assets reach new set-point; **delay time** = time until physical delivery starts.
- (Sec. 1.1) aFRR is a PI-controller function in Statnett's SCADA; must react slower than FCR (low-pass filter) to avoid interfering.
- (Sec. 2.1) A providing unit may mix assets (e.g. a 6-h block delivered 2 h from wind and 4 h from hydro); the TSO sees one set-point; **set-point always a multiple of 1 MW**.
- (Sec. 2.2) **Resulting production = BSP schedule + TSO request** (Figure 2).
- (Sec. 2.3, Table 1) **Step size 1 MW** (changed from 10 MW); **FAT 120 s preferred, 300 s max; delay ≤ 30 s; accuracy at FAT within 1 MW or 10 % of set-point change; sustained error ≤ 5 MW.**
- (Sec. 2.4) Max FAT 5 min, preferred ≤ 2 min; **deactivation time ≤ FAT**.
- (Sec. 2.6) Set-point is a **delta** relative to planned production. **"Available aFRR capacity shall not affect or be affected by other obligations such as FCR, mFRR, day-ahead or XBID."**
- (Sec. 2.8) Statnett can only regulate within purchased margins (result of the aFRR capacity market).
- (Sec. 2.9) ACE mode currently Constant Frequency; future Tie-Line Bias.
- (Sec. 2.10) Actual contribution = set-point + error = measured MW − planned production (incl. mFRR, period shift) − FCR adjustment.
- (Sec. 2.11) **The BSP may deliver both aFRR and FCR from the same asset at the same time**; when bidding aFRR it must compute FCR maximum capacity for a 0.5 Hz deviation [49.5–50.5 Hz] with current droop.
- (Sec. 2.12) An asset may belong to only one active aFRR providing unit; normally one substation (station group possible).
- (Sec. 3–4) Interface: ICCP, remote-control-permitted signal, communication timeout (hold contribution e.g. 900 s), two physical connections to E-NETT, redundant SCADA, **99 % availability** measured weekly; set-point increments 1 MW, rate ≤ every 4 s.

## Strengths
Primary technical source; explicit statement on independence from other obligations; clarifies how the set-point is superposed on the schedule (useful for modelling headroom).

## Weaknesses / limitations
- Dated June 2023 (pre-15-min ISP; before the 2 Dec 2025 BSP terms). Product parameters (1 MW, 5 min) still match current terms and the aFRR page.
- Broken cross-references; no printed page numbers.

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where (section) |
|---|---|---|
| Background/model: independence from other obligations | aFRR capacity shall not affect / be affected by FCR, mFRR, DA, XBID | Sec. 2.6 |
| Model: superposition on schedule | Production = BSP schedule + TSO delta set-point | Sec. 2.2, 2.6, 2.10 |
| Background 2.4: response time | FAT 120 s preferred / 300 s max; delay ≤ 30 s; deactivation ≤ FAT | Sec. 2.3 (Table 1), 2.4, 2.5 |
| Model: bid resolution | 1 MW step | Sec. 2.1, 2.3 |
| Model: FCR and aFRR on same unit | Allowed simultaneously; FCR max capacity at 0.5 Hz counted | Sec. 2.11 |
| Background: mixed-asset providing units | Hydro/wind combination example | Sec. 2.1 |

## Useful quotes (with page numbers)
> "Available aFRR capacity shall not affect or be affected by other obligations such as FCR, mFRR, day-ahead or XBID." (Sec. 2.6)

## Follow-up references to check (backward snowballing)
- Vedlegg til retningslinjer for fos § 8a and § 14 (footnotes, Sec. 2.10–2.11).

