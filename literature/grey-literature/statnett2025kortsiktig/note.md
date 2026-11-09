---
bibkey: statnett2025kortsiktig
bibkey_provisional: true
title: "Kortsiktig markedsanalyse 2025–2030"
authors: "Statnett (Georg Devik, William Bjønness, Ida Naalsund, Rolf Korneliussen, Julie Gunnerød)"
year: 2025
venue: "Statnett report (slide format), September 2025"
peer_reviewed: false
methods: []
review_sections: [price-volatility, electricity-markets, ldes-seasonal-storage]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Statnett's 5-year outlook: more zero-price hours (about 1/4 of the year in DE/UK by 2030) and prices switching between 0 and 90-150 EUR/MWh; S-Norway avg falls to ~50 EUR/MWh; inflow varies 70-80 TWh dry vs wet; European batteries 120 GW x 3 h = 360 GWh (<5 % of Blåsjø); no Norwegian pumped storage before 2030."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/66_Statnett_2025b_Kortsiktig_markedsanalyse_2025_2030.pdf
---

# Kortsiktig markedsanalyse 2025–2030 (Statnett, 2025)

**Source:** `source.pdf` (51 slide pages, Norwegian), https://www.statnett.no/globalassets/for-aktorer-i-kraftsystemet/planer-og-analyser/kma/kortsiktig-markedsanalyse-2025---2030.pdf (KILDEINFO, fetched 28.10.2026). Dated 1 September 2025 (foreword, p. 2). Printed page numbers = PDF page numbers. Some figure glyphs are lost in the text extraction (e.g. "yskland" for Tyskland).

## Research question / purpose
Annual 5-year outlook of trends and uncertainties in the Nordic/European power system, incl. simulated prices, explicitly "not a detailed price forecast" (p. 2). This edition focuses extra on price differences between Norwegian bidding zones (p. 5).

## Setting
- **System:** Nordics, Baltics, Poland, DE, CZ, SK, AT, CH, IT, FR, BE, NL, UK, ES, PT (~90 % of European demand/production) (p. 5 footnote).
- **Markets:** wholesale (DA-type hourly prices); flow-based market coupling in the Nordics modelled. No reserve markets.
- **Horizon and resolution:** each year 2025–2030 simulated separately, hourly, over **29 historical weather years (1988–2016)** (p. 5, p. 50). Simulated 2025 is used as a normalised reference, not observed prices (p. 3 footnote, p. 5).

## Method
- **Model type:** Samnett (integrated market and grid model with detailed hydro and flow-based coupling, Nordics + Baltics) and BID3 (continental/UK market model, better on thermal, demand flexibility, batteries, H2); BID3 price series are inputs to Samnett; PSS/E for grid limits (p. 50).
- **Uncertainty:** 29 weather years; market scenarios Basis/Høypris/Lavpris; Norwegian demand/production scenarios Lav/Medium/Høy (p. 5). Each year is simulated independently, so inter-year inflow/reservoir links are not captured (p. 5).
- **Key assumptions:** the model cannot produce negative prices; 0 is the lowest price (p. 19 footnote). Basis 2030: 120 GW batteries with 3 h duration (p. 15, p. 24 footnote).

## Data / case: key numbers
| Item | Value | Page |
|---|---|---|
| Continental/UK avg price, Basis | ~90–100 €/MWh (2025 sim.) → ~60 €/MWh (2030) | p. 3, p. 19 |
| Lavpris / Høypris continental avg 2030 | 35–40 / just over 100 €/MWh | p. 3 |
| **Short-term price pattern** | prices "increasingly often switch between 0 and 90–150 €/MWh" with the weather | p. 19 |
| Zero-price hours DE and UK 2030 | about **¼ of the year** (doubling of zero-price hours in many countries over 5 years) | p. 19 |
| UK zero-price share summer / winter | 3 % → 23 % / 2 % → 19 % (2025 → 2030) | p. 21 |
| DE summer–winter avg price gap | 20 → just under 40 €/MWh (2025 → 2030) | p. 21 |
| Weather-driven spread in annual avg (DE/UK 2030) | > 30 €/MWh between weather years | p. 19 |
| European battery fleet, Basis 2030 | **120 GW** (tripling), avg 3 h → **360 GWh**, "< 5 % of the capacity in Blåsjø, Norway's largest hydro reservoir" | p. 15 |
| Batteries needed to remove almost all zero-price hours | ~600 × Basis energy (≈ 9,000 GW, 24 h) | p. 24 |
| **Pumped storage** | "little growth in flexibility from other technologies such as pumped storage and flexible H2 in the next five years. In Norway there are several pumped-storage plans but none is likely to be built before 2030" | p. 15 |
| S-Norway avg price, Medium/Basis | under 70 €/MWh (2025) → ~50 €/MWh (2030) (p. 4); 65–70 → 50–55 (p. 35) | p. 4, p. 35 |
| Mid-Norway / N-Norway 2030 | 40–45 / ~33–35 €/MWh | p. 4, p. 35 |
| Realistic range S- and Mid-Norway avg price 2030 | 30–70 €/MWh | p. 36 |
| **Inflow variability** | inflow to Norwegian hydro can differ by **70–80 TWh between a dry and a wet year** | p. 4 |
| Norwegian energy surplus (normal year) | ~17 TWh today → 5 TWh (Medium 2030); −9 TWh (Høy) | p. 4 |
| Planned hydro capacity increases | plans for up to **10 GW** more hydro capacity, doubtful any is ready by 2030 | p. 33 |
| Dry year (1996) in Høy 2030 | S-Norway deficit ~28 TWh, import 80 % of the time; prices up to industry curtailment levels (500–1000 €/MWh in the model) | p. 44 |

## Key findings
- (p. 3, p. 19) More zero- and sometimes negative-price hours are the dominant trend in all scenarios; with high gas costs this gives **high short-term price variation**.
- (p. 15, p. 24) Batteries provide most new flexibility, but their energy is small; storing over weeks and months is "still far too expensive" for batteries (p. 15). More price variation raises battery revenue from spot, intraday, capacity and balancing markets (p. 24).
- (p. 35, p. 37) Norwegian prices stay below continental prices because hydro producers must lower their bids to sell the summer/wet-year surplus when neighbours have zero prices; low summer prices abroad lower the expected value of water that cannot be stored until winter.
- (p. 36) Scarcer water in NO5 → higher water values and higher prices in NO5 than elsewhere in S-Norway when demand grows.
- (p. 45) In winter peak hours Norwegian prices are set by peaking plants abroad, not by Norwegian water values, when hydro capacity cannot cover both domestic demand and full export; **more installed hydro capacity would counter this**.
- (p. 33) Little batteries in Norway: much hydro and less wind/solar give flatter prices and lower battery profitability.

## Strengths
- Recent (Sept 2025), detailed, Norway-specific; explicit about weather-year uncertainty and the price formation role of water values.

## Weaknesses / limitations
- Simulated prices floor at 0 (no negative prices), so variation is understated (p. 19).
- Years simulated independently; no multi-year reservoir dynamics (p. 5).
- Not a forecast; scenario ranges are wide.

## Use it for… (lookup guide)
| Use in our thesis | What the source provides | Where |
|---|---|---|
| Background 2.1 (LDES): batteries are short-duration | 120 GW × 3 h = 360 GWh, < 5 % of Blåsjø; week/month storage too expensive for batteries | p. 15 |
| Background 2.2/2.3: PHS plans in Norway, none before 2030 | Quote on pumpekraft | p. 15 |
| Background 2.5: price volatility / zero prices | prices switch between 0 and 90–150 €/MWh; zero prices ~¼ of the year DE/UK 2030 | p. 19 |
| Background 2.5: seasonal price pattern increasing | DE summer–winter gap 20 → ~40 €/MWh; UK zero-price shares | p. 21 |
| Background 2.5: Norwegian price levels by zone | S-Norway ~50 €/MWh 2030; ranges 30–70 | pp. 4, 35–36 |
| Model / data: inflow uncertainty | 70–80 TWh dry–wet difference | p. 4 |
| Background: water values set Norwegian prices; peak hours set abroad | | p. 37, p. 45 |
| Background: hydro capacity expansion plans | up to 10 GW planned, doubtful by 2030 | p. 33 |
| Method comparison: weather-year scenario approach | 29 weather years 1988–2016, ~250,000 hourly states per year | p. 50 |

## Useful quotes (with page numbers)
> "I Norge er det flere pumpekraftplaner men ingen av disse ligger an til å bli bygget før 2030." (p. 15)

## Follow-up references to check (backward snowballing)
- Statnett Langsiktig markedsanalyse (LMA) 2024/2025 for the 2050 view.
- ENTSO-E adequacy analyses referenced on p. 25.
- EMBER (2025), cited p. 8 for European emissions (= `rosslowe2025european`).

