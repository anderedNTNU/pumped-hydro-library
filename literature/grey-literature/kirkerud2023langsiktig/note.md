---
bibkey: kirkerud2023langsiktig
bibkey_provisional: true
title: "Langsiktig kraftmarkedsanalyse 2023: Energiomstillingen – en balansegang"
authors: "Jon Gustav Kirkerud, Magnus Buvik, Ingrid Holm, Dag Spilde, Maria Sørbye, Ellen Skaansar, Hege Kvandal, Henriette Birkelund, Hanna Skulstad, Lars Petrusson, Kyrre Fjær, Céline Darras (NVE)"
year: 2023
venue: "NVE Rapport nr. 25/2023 (ISBN 978-82-410-2285-2), November 2023"
peer_reviewed: false
methods: []
review_sections: [price-volatility, ldes-seasonal-storage, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "NVE's LA23 long-term market outlook to 2040: Norwegian price ~80 øre/kWh (2030) then ~50 (2040); flexibility from batteries (max 8 h) short-term and H2/district heat long-term; hydro adapts by shifting water between seasons and earns above-average prices; prices vary more year-to-year, week-to-week and within the day."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/Tilleggsdokumenter/46_NVE_2024b_Utviklingen_i_kraftmarkedet_mot_2050_VEDLEGG_IKKE_SELVE_KILDEN.pdf
---

# Langsiktig kraftmarkedsanalyse 2023 (Kirkerud et al., NVE, 2023)

**Source:** `source.pdf` (88 pages, Norwegian). The inbox labels it as a "VEDLEGG" (attachment) to NVE 2024b; KILDEINFO gives its URL as https://publikasjoner.nve.no/rapport/2023/rapport2023_25.pdf. It is the base report that `nve2024utviklingen` extends to 2050. **Page numbers below are PDF pages.** The printed page numbers drift (printed = PDF up to about p. 26, printed = PDF − 1 later; e.g. section 4.2 "p. 52" in the contents is PDF p. 53). Bibkey uses the project leader/first author; if the group prefers a corporate key, `nve2023langsiktig` is the alternative (provisional either way).

## Research question / purpose
NVE's projection of the European, Nordic and Norwegian power system and prices to 2040 under adopted policy (model years 2030, 2035, 2040), used in NVE's licensing cost–benefit analyses (PDF pp. 2, 4).

## Setting
- **System:** 19 European countries (~2/3 of European supply), detailed Nordics (PDF p. 82).
- **Markets:** spot/wholesale; capacity mechanisms and reserves discussed qualitatively.
- **Horizon and resolution:** model years 2030/2035/2040; hourly simulation; **30 weather scenarios (1991–2020)** (PDF p. 82).

## Method
- **Model type:** TIMES (Norwegian energy-system demand projection), **TheMA** (deterministic European market model; only wind and solar vary between weather scenarios) and **Samnett** (stochastic Nordic market model with more detailed hydro, grid limits, flow-based coupling; varies inflow and temperature-dependent demand as well) (PDF p. 82).
- **Uncertainty:** 30 weather years; high/low fuel and CO2 price paths; identical gas, coal and CO2 prices across weather scenarios (PDF p. 82).
- **Key modelling limitations stated by NVE:** no negative prices (floor 0) so price variation is probably underestimated (PDF p. 65, p. 76); regulated hydro is **more flexible than reality** (no start-stop costs, ramping limits or water travel time) which biases captured prices for hydro upward (PDF p. 76); no unplanned outages (PDF p. 82).

## Data / case: key numbers
| Item | Value | PDF page |
|---|---|---|
| Norwegian avg price | ~80 øre/kWh (2030), ~50 øre/kWh (2040), 2022-NOK | p. 7 |
| Price collapse example | **−500 €/MWh** in NL 13–16 h on 2 July 2023, "the minimum price on the exchange" | p. 53 |
| Zero-price hours (< 0.5 øre/kWh) observed to 24 Sept 2023 | 3–5 % of the time in DE, NL and NO | p. 57 |
| DE residual load negative in 2040 | ~35 % of the time; max surplus ~180 GW (≈150 GW after flexible demand) | p. 56 |
| Cost of capacity reserves (capacity mechanisms) in EU | ~5.2 bn € in 2022, doubling from 2020 | p. 55 |
| Batteries in modelled non-Nordic countries, 2040 | **107 GW / 489 GWh** | p. 25 |
| Short-term flexibility in Europe 2040 | ~230 GW; longest battery duration **8 h** at full power | p. 58 |
| Long-term flexibility (H2, district heat) 2040 | 144 GW; H2 cut-out prices 0–36 €/MWh; electric boilers 0–15 €/MWh | p. 59–60 |
| Electrolysis capacity 2040 (non-Nordic modelled countries) | 109 GW | p. 24 |
| Norwegian hydro production increase to 2040 | ~8 TWh: +4 known projects, +2 capacity upgrades/turbine renewals, +3 higher inflow, −1 licence revisions | p. 47 |
| Weather effect | 2010 weather scenario gives ~20 øre/kWh above average price in 2030 | p. 63 |
| Gas marginal cost | 90–150 øre/kWh (2030, 2040) | p. 66 |
| SW-Norway duration curves | 2030: price within gas-cost band ~40 % of time (avg year), ~80 % (dry 2010); 2040 wet year: near H2 cut-out prices > 70 % of time | p. 67 |
| Norwegian peak-load balance | +2 GW (2022) → +0.2 GW (2030) → −0.7 GW (2040); modelled peak 24.7 / 27.6 / 30.3 GW | pp. 76–77 |

## Key findings
- (PDF p. 6, p. 22) A system with more variable renewables needs both short-term flexibility (batteries, demand response) and flexibility over longer periods (H2 production, power-to-heat). Batteries are cost-limited by storage capacity, so they mainly shift energy within short periods (PDF p. 24, p. 58).
- (PDF p. 57) "Store prisvariasjoner er en indikator på lite fleksibilitet ... men de er også en driver for å framskaffe mer fleksibilitet"; NVE expects future volatility to stay higher than today because flexibility is costly.
- (PDF p. 59) Flexible H2 and district-heat producers increasingly **set the price** via their cut-out prices; batteries dampen short-term variation but rarely set the price.
- (PDF p. 63–65) Year-to-year price variation increases to 2040 as weather-dependent technologies set prices more often. Within-week variation (std) rises in summer to 2030; hour-to-hour variation rises with more variable generation, especially in summer.
- (PDF p. 65) With more cheap winter production by 2040, **hydro producers save more water to spring and summer**, moving production to the best-paid periods: an explicit seasonal-storage reallocation effect.
- (PDF p. 47) Higher price variation makes **investment in more capacity in existing hydro plants** more attractive; this adds power but little energy. How much is built depends on price level, price volatility, acceptance and predictable framework conditions.
- (PDF p. 74) Regulated hydro obtains an **above-average captured price**; wind and solar below average (cannibalisation).

## Strengths
- Comprehensive, official, with explicit flexibility assumptions and a clear statement of model limitations relevant to hydro modelling.

## Weaknesses / limitations
- Pumped storage is not modelled or discussed (only "gross production and consumption for pumping" excluded from the summary tables, PDF p. 81).
- Weather-scenario approach with identical fuel prices understates price variation (PDF p. 63, p. 82).
- Projections from autumn 2023; partly superseded by `nve2024utviklingen` (2050 extension) and later NVE/Statnett analyses.

## Use it for… (lookup guide)
| Use in our thesis | What the source provides | Where (PDF p.) |
|---|---|---|
| Background 2.5: volatility rising at year, week and hour scales | | pp. 63–65 |
| Background 2.5: negative/zero prices already observed | −500 €/MWh in NL on 2 July 2023; 3–5 % zero-price hours (2023) | pp. 53, 57 |
| Background 2.1 (LDES): need for long-duration flexibility; batteries limited to ≤ 8 h | | pp. 22, 24, 58–59 |
| Background 2.1: battery fleet assumption | 107 GW / 489 GWh in 2040 | p. 25 |
| Background 2.3 / discussion: hydro shifts water between seasons as prices change | | p. 65 |
| Background 2.3: capacity upgrades driven by price variation | | p. 47 |
| Discussion: system models overstate hydro flexibility | no start-stop, ramping, travel time | p. 76 |
| Background 2.5: Norwegian price level outlook | ~80 øre/kWh 2030, ~50 øre/kWh 2040 | p. 7 |
| Method comparison: weather-year scenarios, 30 years 1991–2020 | | p. 82 |
| Background: tight peak-load balance in Norway | +2 → +0.2 → −0.7 GW | pp. 76–77 |

## Useful quotes (with page numbers)
> "Samtidig er regulerbar vannkraft i våre modeller mer fleksibel enn i virkeligheten." (PDF p. 76)

## Follow-up references to check (backward snowballing)
- NVE (2022) Norsk og nordisk effektbalanse fram mot 2030 (PDF p. 76).
- European Commission, Security of EU electricity supply 2023 (PDF p. 55).
- NVE LA21 (previous edition).

