---
bibkey: ph24_mfrr_activation_guide
title: "BSP – Implementation Guide – mFRR energy activation market (15 min resolution and automated balancing)"
authors: "Nordic TSOs (Nordic Balancing Model)"
year: 2024
venue: "NBM implementation guide, Version 1.1.6, 9.9.2024; PDF, 57 pp."
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Nordic mFRR EAM guide (go-live 3 Dec 2024): 15-min MTU, BSP GCT QH-45 (QH-25 at MARI), scheduled activation orders at QH-7.5, FAT 12.5 min, marginal price per 15 min, complex/linked bids with duration and resting time; some Statnett values (10 MW min bid, 0.5 € price step) since superseded."
---

# Nordic mFRR energy activation market – BSP implementation guide (Nordic TSOs, 2024)

**Source file:** `source.pdf` / `source.txt` (fetched 2026-11-04; bib URL works). Cover: "Version: 1.1.6, Status: Published, Date: 9.9.2024". Printed page numbers = PDF page numbers. Later pages are CIM message specs.

## Research question / purpose
Interface and process description for BSPs in the Nordic **mFRR EAM** with 15-minute resolution and automated balancing (Activation Optimisation Function, AOF); go-live **3 December 2024** (p. 6).

## Setting
- **System:** Nordic TSOs (Energinet, Fingrid, Statnett, Svenska kraftnät).
- **Markets:** mFRR energy activation market; transition towards MARI.
- **Horizon and resolution:** 15-min MTU (quarter-hour, QH).

## Method
n/a (process/interface description). Bid selection by the Nordic AOF; fall-back algorithm may miss in-the-money bids (p. 11).

## Data / case
n/a.

## Key findings
- (p. 7) Definitions: BEGCT (BSP gate closure), direct activation (DA) = activation at any time between scheduled activation points; FAT; ISP.
- (pp. 9–10, Sec. 2.1, timeline table) BSP GCT: H-45 before go-live; **QH-45 from go-live of 15-min ISP/IDC**; **QH-25 latest when connecting to MARI**. AOF run, results, TSO verification; **activation orders sent at QH-7.5**.
- (p. 14, Sec. 3.3.1, product table: Today / Go-live mFRR EAM / MARI) Max/min price 10 000/−10 000 EUR/MWh (later ±15 000, then ±99 999); price granularity 0.01 (Statnett 0.5 at go-live, p. 27); **min bid size 1 or 10 MW at go-live (Statnett 10 MW, footnote 2), 1 MW at MARI**; max 9 999 MW; bid granularity 1 MW; activation granularity 1 MW (0.1 MW for pro-rata ties); **marginal price resolution 60 → 15 min**; **FAT 12.5 min** (Statnett and Svk from go-live; exemptions possible).
- (pp. 15–17, Sec. 3.3.2) Bid attributes: minimum offered volume, indivisible bids, exclusive groups, multipart bids, inclusive bids, conditional and technical linking across QHs, scheduled vs scheduled-and-direct activation, **maximum duration and resting time** (via technical linking), period shift, faster/slower activation.
- (pp. 17–18, Sec. 3.3.3) Validation rules for bids and complex/linked bids (e.g. a QH0 bid may link to ≤ 3 bids in each of QH-1 and QH-2).
- (p. 24, Sec. 3.5) Prices and volumes published on ENTSO-E Transparency and NUCS; activated bids report per BSP after each ISP.
- (p. 27, Sec. 4.3 Statnett) **Statnett: 0.5 EUR price granularity and 10 MW minimum bid at go-live**; national attributes: max duration, resting time, inclusive bids, locational info, period shift, faster activation, mFRR-D; 15-min cut-off for stale bid documents (p. 28).

## Strengths
Detailed description of activation timing and bid attributes (duration, resting time) — useful if mFRR activation is ever modelled.

## Weaknesses / limitations (outdated as of Nov 2026)
- **Statnett minimum bid 10 MW is superseded**: since 2 Dec 2025 the minimum is **1 MW** (`ph24_statnett_bsp_terms_2025`, Art. 62.7, p. 45; Art. 34.3a for CM).
- Statnett's 0.5 EUR price step may have been removed (BSP terms Art. 62.6a: increments of 0.01 EUR/MWh).
- Written before go-live; national terms take precedence (p. 12). A newer guide version may exist on nordicbalancingmodel.net (unverified).

## Use it for… (lookup guide)
| Use in our thesis | What the guide provides | Where (page/section) |
|---|---|---|
| Background 2.4: timing table (mFRR activation row) | GCT QH-45 with 15-min ISP; QH-25 at MARI | pp. 9–10, Sec. 2.1 |
| Background 2.4: 15-min MTU and pricing | Marginal price resolution 15 min; FAT 12.5 min | p. 14, Sec. 3.3.1 |
| Background 2.4: activation timing | Orders sent QH-7.5 | p. 10 |
| Model/future work: energy-limited bidding | Max duration, resting time, technical linking | pp. 15–17, Sec. 3.3.2 |
| Background: go-live of Nordic mFRR EAM | 3 December 2024 | p. 6 |

## Useful quotes (with page numbers)
> "The go-live date for mFRR energy activation market is December 3rd 2024." (p. 6)

## Follow-up references to check (backward snowballing)
- Nordic TSOs, "Memo – Process for activating products" (Ref [10], p. 8).
- "Implementation guide for mFRR EAM transition" (Statnett/Svk, p. 10).

