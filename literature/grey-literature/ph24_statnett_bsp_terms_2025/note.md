---
bibkey: ph24_statnett_bsp_terms_2025
title: "Metode om vilkår for leverandør av balansetjenester og vilkår for balanseansvarlige (EB GL art. 18) — endring, godkjent 30. oktober 2025"
authors: "Statnett"
year: 2025
venue: "Statnett terms and conditions (approved by RME); PDF, 69 pp."
peer_reviewed: false
methods: []
review_sections: [electricity-markets]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Binding Norwegian rules for aFRR CM, mFRR CM, mFRR EAM and imbalance settlement: 60-min CM MTU, 15-min EAM MTU, D-7 to D-1 07:30 gate, 1 MW min bid, marginal pricing, FAT 5 / 12.5 min, CM-to-EAM bidding obligation."
---

# Statnett terms for BSPs and BRPs (Statnett, 2025)

**Source file:** `source.pdf` / `source.txt` (fetched 2026-11-04 from the bib URL, file name `ebgl-art-18---innforing-av-1mw-budstrorrelse.pdf`). Norwegian. Printed page numbers = PDF page numbers.
Cover title: "Forslag til endring i metode om vilkår for leverandør av balansetjenester og vilkår for balanseansvarlige i samsvar med artikkel 18 nr. 1 i kommisjonsforordning (EU) 2017/2195 …", "Godkjent 30. oktober 2025". Amends the version approved 27 May 2025 (Fortale (1), p. 8). Fully in force **2 December 2025** (Art. 2, p. 9). The change that motivated the revision (per the file name) is the introduction of a **1 MW minimum bid size**.

## Research question / purpose
Not research: the legally binding Norwegian terms and conditions (EB GL art. 18) for balancing service providers (BSPs) and balance responsible parties (BRPs). Covers the aFRR capacity market (aFRR CM), the mFRR capacity market (mFRR CM), the mFRR disturbance-reserve markets (mFRR-D), the mFRR energy activation market (mFRR EAM), and imbalance settlement. **FCR and FFR are not covered** (they fall outside EB GL's definition of balancing capacity; Fortale (3), p. 8) — see `statnett2026c` for FCR.

## Setting
- **System:** Norwegian bidding zones NO1–NO5, Nordic synchronous area.
- **Markets:** aFRR CM, mFRR CM, mFRR-D CM/EAM, mFRR EAM, imbalance settlement (BRP part).
- **Horizon and resolution:** CM: daily auction, 60-min MTU. EAM: 15-min MTU. Imbalance settlement period (ISP): 15 min.

## Method
- **Model type:** n/a (regulatory text)
- **How uncertainty is represented:** n/a
- **Solution method:** n/a (market clearing described: price-order selection, marginal pricing)
- **Key modelling choices and assumptions:** n/a

## Data / case
n/a.

## Key findings (rules, with article and page)
**General (Part 2, ch. 1)**
- (Art. 3.1b, p. 9) "aktiveringstid" = time from the BSP receiving Statnett's order until the bid is activated. Deactivation time defined in Art. 3.1h (p. 10).
- (Art. 8, pp. 14–15) Station groups: same bidding zone, same BRP, no internal grid limits; consumption and production not in the same group; different production technologies not in the same group; **energy storage in its own station group** (may be combined with production or consumption after assessment).
- (Art. 10, p. 16) **MTU = 60 min for aFRR CM, mFRR CM and mFRR-D CM; MTU = 15 min for bidding and activation in mFRR EAM and mFRR-D EAM.**
- (Art. 11, p. 16) BSP is financially responsible for deviations from activated volume.
- (Art. 13, pp. 16–17) **Linked aFRR/mFRR capacity bids:** the same volume can be offered in both CMs as an exclusive group across markets; separate prices; **aFRR CM is cleared first**; if accepted in aFRR the linked mFRR bid drops out, otherwise it enters the mFRR clearing. Linked bids cannot be block bids.
- (Art. 14, p. 17) Cross-zonal FRR capacity exchange: max 10 % of cross-zonal capacity (up to 20 % if needed); aFRR gets CZC before mFRR.

**aFRR capacity market (ch. 2, pp. 19–26)**
- (Art. 17.1a, p. 19) **Full activation time 5 min** after order.
- (Art. 17.1c, p. 19) Accepted bids must be **fully available for activation for the whole agreed delivery period** (or obligation transferred, Art. 24).
- (Art. 18, pp. 19–20) **Gate opens D-7 00:00 CET; gate closes D-1 07:30 CET**; bids binding after GCT; results published by **09:00 CET** (note: the FRR implementation guide says aFRR results "no later than D-1 9:20 CET", see `ph24_nordic_tsos_frr_guide_2026` p. 9).
- (Art. 19, pp. 20–21) Bids per station group and bidding zone, **separate for up and down**, per MTU; **offered capacity may not be part of other obligations** (Art. 19.1e). Bid content: MW, price in EUR "per MWh" (as written), direction, MTU, divisibility, bid type (single, block, bid curve), location. **Minimum bid 1 MW, steps of 1 MW**; bids ≤ 50 MW may be indivisible; bids > 50 MW must be divisible. Block bids allowed for consecutive MTUs with same MW/direction/zone/price. Exclusive bid curves allowed. Total offered ≤ prequalified volume (may differ up/down).
- (Art. 20, pp. 21–22) One price per bidding zone, MTU and direction; **marginal pricing**; selection in price order in a **common Nordic optimisation**; bids behind congestion can be made unavailable without compensation; block bids do not set the price but can raise it (paradoxically accepted bids get at least their bid).
- (Art. 21, p. 22) Special purchases (grid reasons) and extra purchases after GCT are **pay-as-bid**.
- (Art. 27.2, p. 24) **Activated aFRR energy is priced at the mFRR balancing-energy price in the same direction** (Art. 67).
- (Art. 28, pp. 24–25) Capacity settled per MTU and direction; weekly settlement via eSett.
- (Art. 30, p. 25) Non-delivered aFRR capacity: payment cut at marginal CM price × **1**.

**mFRR capacity market (ch. 3, pp. 27–34)**
- (Art. 32.1a, p. 27) **Full activation time 12.5 min**.
- (Art. 32.1c–d, p. 27) Accepted CM volume must be **bid into mFRR EAM** with at least the same volume for the whole delivery period, available for **direct activation** except the last quarter-hour of the delivery period.
- (Art. 33, pp. 27–28) **D-7 00:00 CET to D-1 07:30 CET**; results by 09:00 CET.
- (Art. 34, pp. 28–29) Same bid rules as aFRR: separate up/down, per MTU, not in other obligations, **min 1 MW in 1 MW steps**, ≤ 50 MW may be indivisible, > 50 MW divisible; block bids, exclusive curves; can be linked to aFRR CM bids (Art. 13).
- (Art. 35, pp. 29–30) Bids may carry **duration and resting-time limits** (relevant for energy-limited assets) with group IDs so the clearing respects them.
- (Art. 36, p. 30) Marginal pricing, one price per zone/MTU/direction; selection "based on socio-economic calculations".
- (Art. 42, p. 33) CM-accepted volumes must be bid into EAM **by 21:30 D-1**; bids may still be updated until EAM GCT; EAM volume ≥ total CM obligation.
- (Art. 44, p. 34) Penalties: missing EAM bids → CM marginal price × **2**; bid cannot be activated when called → CM marginal price × **25**.

**mFRR energy activation market (ch. 5, pp. 43–52)**
- (Art. 59.1a–b, p. 43) Full activation **≤ 12.5 min** after order; acknowledge activation message within 2 min.
- (Art. 61, p. 44) **Gate opens after day-ahead results (normally ~13:00 D-1); preliminary deadline 21:30 D-1; GCT 45 min before each MTU**; binding after GCT.
- (Art. 62.3, p. 44) BSP must be able to deliver per its bids — **obligations from other markets may not limit the offered regulation volume.**
- (Art. 62.4–7, p. 45) Bid content (MW, EUR/MWh, direction, MTU, divisibility, location); availability flags for direct activation, period shift, faster activation. Price step 0.01 EUR/MWh; **up-bids must be priced above the day-ahead area price, down-bids below**; price limits ±10 000 EUR/MWh. **Minimum bid 1 MW, 1 MW steps**; divisible unless stated; minimum activation volume allowed.
- (Art. 62.9–11, p. 46) Complex bids (exclusive, sorted/multipart, inclusive groups), duration and resting-time constraints in whole MTUs, conditional and technical linking across consecutive MTUs.
- (Art. 63, p. 47) Price-order selection: common Nordic optimisation for scheduled activations, national for direct activations; out-of-merit activations possible; Statnett may suspend bids it deems not efficiently priced and use the volume at the day-ahead price.
- (Art. 64.1, p. 47) Activation steps of 0.1 MW.
- (Art. 65.1, p. 48) **Scheduled activation**: order sent 7.5 min before the quarter-hour shift, cyclic every 15 min; **ramp starts 5 min before the activation time and is linear until 5 min after**; FAT 12.5 min; deactivation mirrors activation if not renewed.
- (Art. 65.2, p. 48) **Direct activation**: start 2.5 min after order, 10 min linear ramp; ordered for current and following MTU.
- (Art. 66, p. 49) Period-shift activation (structural imbalances around MTU shifts; BSP chooses ramp profile), faster activation (if FAT < 12.5 min declared), early deactivation (1 min prep + 4 min).
- (Art. 67, pp. 49–50) **mFRR price in EUR/MWh, per direction and bidding zone, marginal pricing**; if no activation in a direction in an MTU, the mFRR price = day-ahead area price.
- (Art. 68, p. 50) 99 % weekly availability on heartbeat messages.
- (Art. 72, pp. 51–52) Activated bids settled at **best of mFRR price and bid price**; volume computed as a block per MTU using the ordinary ramp profile; faster activation gets +1 EUR/MWh on the bid price option.

**BRP part (Part 3, pp. 63–69)**
- (Art. 88.3, p. 63) BRPs must be in planned balance 15 min after intraday GCT.
- (Art. 92.3, p. 65) Trades reported ≤ 45 min before the ISP.
- (Art. 94, p. 65) **ISP = 15 min.**
- (Art. 97, p. 67) Imbalance price = mFRR up-price if dominant direction is up, mFRR down-price if down; otherwise "value of avoided activation" (Art. 98) plus incentive component (Art. 99).
- (Art. 100, p. 68) **Single price** for positive and negative imbalances.

## Strengths
- Primary, binding source; precise numbers for every product parameter we need (MTU, gate times, min bid, divisibility, pricing, FAT, penalties).
- Covers the interaction between aFRR CM and mFRR CM explicitly (Art. 13 exclusive linking).

## Weaknesses / limitations
- Norwegian only; long legal text.
- Does not cover FCR (see `statnett2026c`) or FFR.
- Will change again when the Nordic TSOs connect to MARI (mFRR) and PICASSO (aFRR): e.g. EAM GCT 45 → 25 min (see `ph24_statnett_mfrr`).
- Cover says "Forslag til endring …" although it is the approved version (approval date on cover).

## Use it for… (lookup guide)
| Use in our thesis | What the document provides | Where (article, page) |
|---|---|---|
| Background 2.4: timing table (aFRR/mFRR CM rows) | D-7 00:00 CET open, D-1 07:30 CET close, results by 09:00 CET | Art. 18 (pp. 19–20), Art. 33 (pp. 27–28) |
| Background 2.4: mFRR activation row | Opens after DA results (~13:00 D-1), preliminary deadline 21:30 D-1, GCT 45 min before each 15-min MTU | Art. 61 (p. 44), Art. 10.2 (p. 16) |
| Background 2.4: MTU of capacity markets | 60 min (aFRR CM, mFRR CM, mFRR-D CM) | Art. 10.1 (p. 16) |
| Model: min bid / bid resolution for FRR capacity | 1 MW, 1 MW steps; ≤ 50 MW may be indivisible, > 50 MW divisible | Art. 19.3 (pp. 20–21), Art. 34.3 (pp. 28–29) |
| Model: symmetric vs asymmetric | Separate bids and prices for up and down (aFRR, mFRR) | Art. 19.1c, 20.1, 34.1c, 36.1 |
| Model: pricing of reserve capacity | Marginal (pay-as-cleared), one price per zone/MTU/direction; special/extra purchases pay-as-bid | Art. 20–21 (pp. 21–22), Art. 36–37 (p. 30) |
| Model: capacity vs energy remuneration | Capacity paid per MTU irrespective of activation; mFRR energy at best of mFRR price and bid; aFRR energy at mFRR price in same direction | Art. 28, 27.2 (p. 24), Art. 72 (p. 51) |
| Model: deliverability constraint | Offered capacity cannot be in other obligations; other-market obligations may not limit EAM bids | Art. 19.1e (p. 20), 34.1e (p. 28), 62.3 (p. 44) |
| Model: mFRR CM → EAM obligation | CM volume must be bid into EAM, available for direct activation, by 21:30 D-1 | Art. 32.1c–d (p. 27), Art. 42 (p. 33) |
| Model: linked aFRR/mFRR capacity bids | Same MW offered in both CMs as exclusive group; aFRR cleared first | Art. 13 (pp. 16–17) |
| Model: response time | aFRR FAT 5 min; mFRR FAT 12.5 min; scheduled-activation ramp −5 to +5 min around QH shift; direct: start after 2.5 min, 10-min ramp | Art. 17.1a (p. 19), 32.1a (p. 27), 59.1a (p. 43), 65 (p. 48) |
| Model: penalties for non-delivery (risk of overcommitting) | aFRR ×1; mFRR missing EAM bid ×2; failed activation ×25 CM price | Art. 30 (p. 25), 44 (p. 34), 73 (p. 52) |
| Model: energy-limited bids | Duration and resting-time limits on mFRR CM/EAM bids | Art. 35 (pp. 29–30), 62.10 (p. 46) |
| Background: imbalance settlement | ISP 15 min, single imbalance price = mFRR price in dominant direction | Art. 94 (p. 65), 97 (p. 67), 100 (p. 68) |
| Background: storage in station groups | Storage in its own station group | Art. 8.2g (p. 15) |

## Useful quotes (with page numbers)
> "Tilbudt aFRR-kapasitet kan ikke inngå i andre forpliktelser." (Art. 19.1e, p. 20)

## Follow-up references to check (backward snowballing)
- Statnett, "Vilkår for FCR-markedet" (= `statnett2026c`).
- Nordic aFRR / mFRR Capacity Market rules and Market handbook FRR CM (linked from `ph24_statnett_mfrr`).
- EB GL (EU 2017/2195) art. 18.

