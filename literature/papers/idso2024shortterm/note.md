---
bibkey: idso2024shortterm
bibkey_provisional: true
title: "The Short-Term Price Elasticity, Temperature Elasticity, and Wind Speed Elasticity of Electricity: A Case Study from Norway"
authors: "Johannes Idsø, Jon Gunnar Nesse, Øyvind Heimset Larsen"
year: 2024
venue: "Sustainability 16(8), 3321 (MDPI)"
peer_reviewed: true
methods: []
review_sections: [price-volatility, electricity-markets]
relevance: background
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/24_Idso_2024_Short_term_price_temperature_and_wind_speed_elasticity_of_electricity_Norway.pdf
takeaway: "Daily log-linear regression for southern Norway 2013–2023: after the 2021 NordLink/NSL cables, southern Norwegian prices rose from ~263 to ~1197 NOK/MWh and their std from 116 to 928 NOK/MWh while northern Norway decoupled; demand is almost price-inelastic (−0.087 overall, n.s. when cold and P > 1500 NOK/MWh) and driven by temperature (elasticity ≈ −0.7 above 0 °C, −0.2 below)."
---

# Short-term price, temperature and wind elasticity of Norwegian demand (Idsø, Nesse & Larsen, 2024)

_Article 3321; the PDF's "X of 21" equals PDF page X, used as page numbers below. Not in `references.bib`: provisional key (Better BibTeX may produce `idso2024short` or `idso2024shortterm` depending on hyphen handling; check in Zotero). The authors' "°F to allow logarithms" and some inconsistencies (see Weaknesses) suggest reading results cautiously._

## Research question / purpose
How did electricity consumption in southern Norway respond to the very large and sustained price increase from autumn 2020 onwards, and what are the short-term price, temperature and wind-speed elasticities of demand; are they constant across price and temperature levels (p. 1–2, 11–12)?

## Setting
- **System:** southern Norway (average of NO1, NO2, NO5) vs northern Norway (NO3, NO4) (p. 9).
- **Markets:** Nord Pool day-ahead spot price (consumer support schemes ignored in the regression, discussed in Sect. 3.3) (p. 12, 18).
- **Horizon and resolution:** daily data 2013 – Nov 2023 (3970 days) (p. 17).

## Method
- **Model type:** econometric. Cobb–Douglas demand C = A·P^b1·T^b2·V^b3 → log-linear OLS (eq. 1–2, p. 12–13) in Stata; temperature in °F to allow logs; no seasonal dummies by design ("Consumption in January is high not because the name of the month is January, but because it is cold", p. 12).
- Sub-sample regressions by price (> / < 1500 NOK/MWh) and temperature (> / < 0 °C) quadrants (p. 14–15, Fig. 16) and by temperature bands (Table 2, p. 15).
- Standardised-variable regression to rank explanatory power (eq. 5, p. 16–17).
- Diagnostics: VIF ≈ 1, Breusch–Pagan p = 0.24, non-normal residuals justified by CLT (p. 17–18).
- Sine-curve-with-trend consumption model as a simple forecast (eq. 3, p. 13).
- **How uncertainty is represented:** n/a.

## Data / case
Nord Pool prices and consumption; MET Norway temperature and wind (p. 13, 20).

## Key findings
- (p. 1, 11–12) Southern Norway average price NOK 263/MWh in 2013–2019/2020 → NOK 1192/MWh in 2020/2021–2023 (abstract and p. 11–12 use slightly different period labels); peak NOK 7820/MWh (≈ EUR 780) on 30 Aug 2022 (p. 9).
- (p. 10, Table 1) 2013–2020: south 262.7 (std 116.1), north 269.3 (std 112.4) NOK/MWh, std of the south–north difference 33.9. 2020–2023: south ≈ 1196.7 (std 928.1), north ≈ 356.1 (std 353.6), difference ≈ 841.0 (std 881.2) (values re-assembled from a garbled table extraction; verify against the PDF).
- (p. 10) Before the two 1400 MW cables (NordLink to Germany, April 2021; North Sea Link to England, Oct 2021), north–south prices were almost equal; afterwards southern Norway experienced "price contagion" while northern Norway was shielded by limited north–south transmission.
- (p. 14) Full-sample elasticities: price −0.087, wind speed +0.022, temperature −0.603, R² = 0.86.
- (p. 15, Fig. 16) Quadrants: low price & warm P −0.006 / T −0.769; high price & warm P −0.07 / T −0.64; low price & cold P −0.013 / T −0.230; high price & cold P n.s. / T −0.204.
- (p. 15, Table 2) Temperature elasticity −0.73 (T > 5 °C), −0.55 (−2 to 5 °C), −0.19 (T < −2 °C); possible explanations wood-burning and heat-pump COP (p. 15–16).
- (p. 17) Standardised: 1 std in price → −2,359 MWh/day; in temperature → −51,104 MWh/day; i.e. temperature dominates.
- (p. 3–4, Fig. 2) Norwegian reservoir storage cycles from a spring minimum (before snowmelt) to an autumn maximum; producers must keep enough water for winter.
- (p. 4) Nord Pool: reservoir producers' supply bids are driven by opportunity cost of water rather than production cost.
- (p. 2–3) 2023: 89.2 % hydro, 9.1 % wind, 1.7 % thermal; average hydropower cost ≈ NOK 117.7/MWh (≈ EUR 10/MWh).

## Strengths
- Recent Norwegian data spanning the 2021–2023 price crisis; clear descriptive evidence on the step change in level and volatility of southern Norwegian prices and the north–south decoupling.
- Simple, transparent regressions.

## Weaknesses / limitations
- Simple OLS on daily data; no treatment of price endogeneity (price and demand jointly determined), no autocorrelation correction or time-series model; consumer support scheme (90 % above NOK 730/MWh from Dec 2021) weakens the link between spot price and price paid (p. 18), which biases the price elasticity toward zero.
- Labelling inconsistency: text says b2 is the wind elasticity and b3 the temperature elasticity, opposite to eq. 1 (p. 13).
- Temperature in °F to avoid log of negatives is ad hoc.
- Table 1 period labels overlap (2013–2020 vs 2020–2023) and the abstract cites 2021–2023.
- MDPI Sustainability; primarily descriptive.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.5: Norwegian price level and volatility after 2021 | Mean and std of prices south vs north, 2013–2020 vs 2020–2023 | Table 1, p. 10; Figs. 10–12 |
| Background 2.5: interconnector-driven price contagion | NordLink (Apr 2021) and NSL (Oct 2021), 1400 MW each; north shielded | p. 7, 10 |
| Background 2.5: peak price | NOK 7820/MWh on 30 Aug 2022 in southern Norway | p. 9 |
| Background 2.4: price-inelastic short-run demand | Price elasticity −0.087; n.s. at high price & cold | p. 14–15 |
| Background: seasonal reservoir cycle in Norway | Spring minimum, autumn maximum; reservoir energy 2013–2023 | p. 3–4, Fig. 2 |
| Background 2.4: Nord Pool day-ahead mechanics; water value in bids | Prices for the next 24 h announced at 1 p.m. the day before; opportunity cost drives reservoir bids | p. 4 |
| Background 2.2: Norwegian production mix | 89.2 % hydro, 9.1 % wind (2023); 1761 plants | p. 2–3 |

## Useful quotes (with page numbers)
> "price elasticity is low even when the price is very high. It is the temperature that controls the consumption." (p. 1, abstract)

> "northern Norway was shielded from price contagion due to small cable capacity between northern Norway and southern Norway." (p. 10)

## Follow-up references to check (backward snowballing)
- Statistics Norway electricity statistics (ref. [12]) for production mix figures.
- Statnett on price areas (ref. [25]).
- NVE report 36/2020 on electrification and the power system (ref. [3]).
- Few academic follow-ups; better sources for Nordic price dynamics are needed elsewhere.

