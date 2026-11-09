---
bibkey: statnett2025systemutviklingsplan
bibkey_provisional: true
title: "Systemutviklingsplan 2025: Elektrifisering for en ny tid"
authors: "Statnett SF"
year: 2025
venue: "Statnett system development plan (public report), 2025"
peer_reviewed: false
methods: []
review_sections: [electricity-markets, phs-technology]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Statnett's 2025 grid/system plan: flow-based DA coupling (Oct 2024), automated balancing per bidding zone (Mar 2025), 15-min ID trading (Mar 2025) and 15-min DA (30 Sept 2025), MARI/PICASSO connection planned 2027/2028, mFRR activation min bid to fall to 1 MW; regulable hydro and producers adding capacity/pumps are central flexibility."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/70_Statnett_2025f_Systemutviklingsplan_2025_Elektrifisering_for_en_ny_tid.pdf
---

# Systemutviklingsplan 2025 (Statnett, 2025)

**Source:** `source.pdf` (53 pages, Norwegian), https://www.statnett.no/globalassets/for-aktorer-i-kraftsystemet/planer-og-analyser/sup/systemutviklingsplan-2025.pdf (KILDEINFO, fetched 28.10.2026). Printed page numbers = PDF page numbers (footer "Statnett Systemutviklingsplan 2025 NN"). Read in depth: summary (pp. 2–9), ch. 1.3 market and system-operation solutions (pp. 17–22), ch. 5 production/flexibility (pp. 45–50); grid-project chapters 2–4 skimmed.

## Research question / purpose
Statnett's plan for developing the Norwegian transmission grid, market solutions and system operation in the coming years, under the strategy "Elektrifisering for en ny tid": increase utilisation of the existing system, build faster, increase robustness (pp. 2–3).

## Setting
- **System:** Norwegian transmission system (14,000+ km, 230 substations, p. 4) within the Nordic synchronous area.
- **Markets:** DA, ID, balancing/reserve markets (FCR, aFRR, mFRR), connection/tariffs.
- **Horizon:** ~2025–2050 (target 420 kV grid allows doubling of consumption and production towards 2050, p. 5).

## Method
n/a (planning document).

## Data / case: market-design facts with dates (relevant for modelling PHS market participation)
| Fact | Value | Where |
|---|---|---|
| Flow-based market coupling in Nordic DA | introduced **October 2024** | p. 18 |
| Flow-based for intraday auctions | planned **2027** | p. 18 |
| Automated balancing and congestion management (new Nordic balancing model, balancing per bidding zone) | introduced **March 2025** | p. 19 |
| **15-min trading in intraday market** | introduced **March 2025** | p. 21 |
| **15-min trading in day-ahead market** | in operation **30 September 2025** | p. 21 |
| Intraday auctions (IDAs) | introduced **June 2024** | p. 21 |
| mFRR activation basis | imbalance per bidding zone; aFRR activated from Nordic frequency | p. 20 |
| Connection to MARI (mFRR) and PICASSO (aFRR) | planned **2027/2028** | p. 20 |
| Nordic aFRR capacity market | established "in recent years"; Norwegian mFRR capacity market changed so capacity is bought closer to operation | p. 20 |
| **mFRR minimum bid size** | to be reduced to **1 MW** in the mFRR activation market, as part of the aggregation plan towards 2028/2029 | p. 20 |
| mFRR-D | separate procurement for actors that cannot meet mFRR requirements; used at faults, not normal balancing | p. 19 |
| Reserve needs and prices | needs have risen (per-zone balancing, less spare grid capacity after flow-based, larger HVDC dimensioning faults); reserve prices up due to high power prices and large price variation, **especially mFRR** | p. 20 |
| Imbalance prices | at times very high and variable (reserve situation, limited inter-zonal capacity) | p. 19 |
| Reserved grid capacity | ~7,700 MW new consumption, ~7,300 MW new production (Q3 2025) | p. 4, p. 14 |

## Key findings
- (p. 48) "Regulerbar vannkraft er svært verdifull fordi kraften kan spares til når den trengs mest. Dette blir enda viktigere i fremtiden." Statnett is in dialogue with several hydro producers who **consider increasing capacity and/or installing pumps** in their plants. Large upgrade plans in Agder, Rogaland and Telemark (NO2); grid needs covered by renewal of the Sauda–Lyse–Flesaker 300 kV grid.
- (p. 8) Capacity (effekt) expansions in existing hydro plants are important for the power balance and of high value for the system.
- (p. 15) Statnett is clarifying how to handle large combined connection cases, "for example hydropower with pumping possibilities".
- (p. 50) Hydro and large industry will be central flexibility providers; others include batteries, small hydro, **pumped storage**, solar and wind producers. More zero/negative-price hours raise the profitability of flexibility and storage.
- (p. 21) Quarter-hour settlement reduces imbalances caused by continuous demand changes vs step changes in production at settlement-period boundaries.

## Strengths
- Authoritative, recent TSO statement of market-design changes with dates, many of which define the market environment in our thesis (2025–2026).

## Weaknesses / limitations
- Planning document; dates for future steps (MARI/PICASSO 2027/2028, 1 MW mFRR bids) may slip.
- No quantitative reserve-product parameters (activation times, volumes); use the Statnett/Nordic TSO product documents for those (`ph24_statnett_*`, `ph24_nordic_tsos_*`).

## Use it for… (lookup guide)
| Use in our thesis | What the source provides | Where |
|---|---|---|
| Background 2.4: market reforms timeline | flow-based Oct 2024; IDAs Jun 2024; automated balancing Mar 2025; 15-min ID Mar 2025; 15-min DA 30 Sept 2025 | pp. 18–21 |
| Background 2.4: reserves, future platforms | MARI/PICASSO 2027/2028; mFRR per bidding zone; aFRR from Nordic frequency | p. 20 |
| Background 2.4 / model: mFRR minimum bid size | to be lowered to 1 MW (plan to 2028/2029) | p. 20 |
| Background 2.4: reserve costs rising, esp. mFRR | | p. 20 |
| Background 2.2/2.3: Norwegian producers considering pumps / capacity upgrades | | p. 48, p. 8 |
| Background 2.3: PHS listed as a flexibility source | | p. 50 |
| Background 2.4: imbalance prices high/volatile | | p. 19 |

## Useful quotes (with page numbers)
> "Statnett er i dialog med flere vannkraftprodusenter som vurdere å øke effekten og/eller installere pumper i sine kraftverk." (p. 48)

## Follow-up references to check (backward snowballing)
- Statnett, Kraftmarkedsåret 2024 (p. 17).
- Statnett, plan for aggregering i reservemarkedene (p. 20).
- Statnett, Analyse av transportkanaler 2025; Nettfornyelse og effekt i NO2 (p. 48–49).
- Statnett, Kortsiktig markedsanalyse 2025–2030 (filed: `statnett2025kortsiktig`).

