---
bibkey: nve2024utviklingen
bibkey_provisional: true
title: "Utviklingen i kraftmarkedet mot 2050: En utvidelse av Langsiktig kraftmarkedsanalyse 2023"
authors: "NVE (Norges vassdrags- og energidirektorat)"
year: 2024
venue: "NVE report (slide-format), October 2024"
peer_reviewed: false
methods: []
review_sections: [price-volatility, ldes-seasonal-storage, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "NVE extends its 2023 long-term market analysis to 2050: Norwegian average price falls to 42 øre/kWh (2022-NOK), flexibility mostly from demand (H2, ~400 GW batteries, 80 % <=3 h), hydro capacity +1.8 GW 2040-50, hourly prices in NO2 2050 mostly 29-59 EUR/MWh vs 27-94 in DE."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/46_NVE_2024b_Utviklingen_i_kraftmarkedet_mot_2050.pdf
---

# Utviklingen i kraftmarkedet mot 2050 (NVE, 2024)

**Source:** `source.pdf` (35 slide pages, Norwegian), from https://publikasjoner.nve.no/diverse/2024/utviklingen-i-kraftmarkedet-mot-2050.pdf; landing page https://www.nve.no/energi/analyser-og-statistikk/langsiktig-kraftmarkedsanalyse/utviklingen-i-kraftmarkedet-mot-2050/ (KILDEINFO, fetched 28.10.2026). Printed page numbers = PDF page numbers. No personal authors are named. The base report it extends, LA23, is filed separately as `kirkerud2023langsiktig` (it was the inbox "VEDLEGG").

## Research question / purpose
How the European, Nordic and Norwegian power system and prices may develop from 2040 to 2050 under adopted policy. The model years 2030/2035/2040 from LA23 are unchanged; only a 2050 dataset is added (p. 2). The 2050 reference path is a trend extrapolation for Europe (same MW/TWh growth 2040–50 as 2030–40) and a more judgemental path for the Nordics (p. 3).

## Setting
- **System:** 19 modelled European countries (~2/3 of European supply) with Norway/Nordics in detail (p. 9 footnote).
- **Markets:** wholesale spot only; no reserve markets.
- **Horizon and resolution:** model years 2030, 2035, 2040, 2050; hourly prices simulated over **30 weather scenarios** (p. 29).

## Method
- **Model type:** fundamental market models (as in LA23: TheMA for Europe, Samnett for the Nordics; see `kirkerud2023langsiktig`).
- **Uncertainty:** 30 historical weather years; high/low fuel-and-CO2 bands (p. 8, p. 29); sensitivities on demand growth and offshore wind (pp. 17, 30).
- **Key assumptions on flexibility:** most new flexibility is demand-side: flexible H2 electrolysis (575 TWh in 2050, of which < 150 TWh inflexible with 150 €/MWh cut-out price; rest with lower, stepped cut-out prices) (p. 25); batteries ~400 GW in 2050 (p. 10, p. 26), **80 % with up to 3 h duration and 20 % with 8 h** (p. 32); flexible electric boilers in district heating, cut-out 15 €/MWh, < 40 TWh (p. 26). Gas plant (50 % efficiency) marginal cost 107 €/MWh in 2050 (p. 8).

## Data / case: key numbers
| Item | Value | Page |
|---|---|---|
| Solar + wind share of European production | 58 % (2040) → 65 % (2050) | p. 5 |
| Emission-free share of production in modelled countries, 2050 | 87 % | p. 7, p. 10 |
| Continental average price (trading partners) | ~60 €/MWh (2040) → ~55 €/MWh (2050) | p. 23 |
| Prices at/above gas marginal cost in 2050 | about 25 % of the time | p. 23 |
| DE prices near zero **without** flexible demand and batteries, 2050 | 45 % of the time | p. 24 |
| Prices at or below flexibility cut-out prices | about 50 % of the time | p. 25 |
| Norwegian average price | 49 øre/kWh (2040) → **42 øre/kWh (2050)**, 2022-NOK; ~15 øre below trading partners | p. 6, p. 28 |
| Norwegian energy surplus 2050 | ~8 TWh (Nordics ~60 TWh) | p. 6 |
| Norwegian production / consumption 2050 | 215 TWh / ~207 TWh | p. 18, p. 21 |
| Norwegian hydro production | 137 (2022), 142 (2030), 145 (2040), 146 TWh (2050) (table) | p. 20 |
| Hydro capacity increase 2040–2050 | **+1.8 GW** from capacity upgrades, "an important source of flexibility" | p. 20 |
| Hourly price spread 2050 (50 % interval) | **NO2 29–59 €/MWh; DE 27–94 €/MWh**; price variation measured as coefficient of variation (std/mean of hourly prices) | p. 31 |
| High-demand scenario | Norway −13 TWh balance → price +17 øre/kWh | p. 30 |
| Import share on NSL and NordLink | ~30 % (2030) → 35 % (2050) of the time | p. 33 |

## Key findings
- (p. 5, p. 24) A system dominated by non-dispatchable generation depends on many kinds of flexibility; NVE assumes it comes mainly from demand. Without it, zero-price hours explode (45 % in DE 2050).
- (p. 25) In hours with high renewable output the **willingness to pay of flexible consumers (H2 cut-out prices) sets the price**; cut-out levels show as plateaus in the duration curve.
- (p. 26) Battery costs keep falling; rising hour-to-hour volatility makes short-term storage profitable; batteries already active, especially intraday.
- (p. 28, p. 31) Between 2040 and 2050 price variation **falls** in both DE and NO2 because flexibility grows faster than variable generation.
- (p. 32) By 2050 prices are lowest at midday on average over the whole year; highest prices shift to evening/night.
- (p. 34) Norwegian trade follows the seasonal inflow pattern (net export summer/autumn, import in winter and before snowmelt); hydro's ability to store water lets it save water for periods with higher value; short-term flows are increasingly driven by continental solar and wind.
- (p. 5) In the short and medium term, **capacity (effekt) upgrades in hydropower plants** and demand flexibility can help balance the system.

## Strengths
- Official Norwegian regulator projection to 2050; explicit numbers for battery durations, flexibility cut-out prices and price distributions in NO2.

## Weaknesses / limitations
- Trend extrapolation for Europe 2040–2050; NVE stresses large uncertainty (p. 3).
- **Pumped storage is not discussed at all** (no occurrence of "pumpekraft" in the report). Hydro flexibility is represented by capacity upgrades only.
- Price variation in 2050 falls by assumption of large demand-side flexibility; the models cannot produce negative prices (stated in LA23, see `kirkerud2023langsiktig`).
- Slide format: figures not reproducible from the text.

## Use it for… (lookup guide)
| Use in our thesis | What the source provides | Where |
|---|---|---|
| Background 2.5: future price level in Norway | 42 øre/kWh in 2050 (2022-NOK), down from 49 in 2040 | p. 6, p. 28–29 |
| Background 2.5: price variation in NO2 vs DE | 50 % of hourly prices 29–59 vs 27–94 €/MWh in 2050; CV as metric | p. 31 |
| Background 2.5: zero prices without flexibility | 45 % zero-price hours in DE 2050 without batteries/flexible demand | p. 24 |
| Background 2.1 (LDES): competing flexibility is short-duration | ~400 GW batteries, 80 % ≤ 3 h, 20 % 8 h | p. 26, p. 32 |
| Background 2.1: flexible H2 sets prices in surplus hours | cut-out prices; 575 TWh H2 consumption 2050 | p. 25 |
| Background 2.3: hydro capacity upgrades as Norwegian flexibility | +1.8 GW 2040–2050 | p. 20; p. 5 |
| Background 2.5: daily price shape changes (midday lowest) | | p. 32 |
| Background: seasonal trade pattern follows inflow | | p. 34 |
| Method: weather-year scenarios as uncertainty representation | 30 weather scenarios | p. 29 |

## Useful quotes (with page numbers)
> "I timer med høy fornybarproduksjon vil betalingsvilligheten til det fleksible forbruket bestemme prisen." (p. 25)

## Follow-up references to check (backward snowballing)
- NVE Langsiktig kraftmarkedsanalyse 2023 (filed: `kirkerud2023langsiktig`).
- IEA (June 2024) on the lack of investment in dispatchable capacity (p. 24).
- "Hovedtall" data file for LA23 extended to 2050 (p. 35).

