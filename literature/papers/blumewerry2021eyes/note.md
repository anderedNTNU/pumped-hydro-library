---
bibkey: blumewerry2021eyes
bibkey_provisional: true
title: "Eyes on the Price: Which Power Generation Technologies Set the Market Price?"
authors: "Eike Blume-Werry, Thomas Faber, Lion Hirth, Claus Huber, Martin Everts"
year: 2021
venue: "Economics of Energy & Environmental Policy 10(1), 1–14 (IAEE)"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [price-volatility, electricity-markets]
relevance: background
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/08_Blume-Werry_2021_Eyes_on_the_price_Which_power_generation_technologies_set_the_market_price.pdf
takeaway: "Green-X fundamental model of 20 interconnected European markets for 2020: hard coal and gas set the price in only ~40% of hours (with lignite, fossil plants still below two thirds), reservoirs and pumped hydro set it in about a quarter of hours (mostly mid/high-priced), and in the Nordics Norwegian reservoirs set the price in most hours via water values tied to the next thermal unit."
---

# Which technologies set the market price? (Blume-Werry et al., 2021)

_Journal pages 1–14 = PDF pages 1–14. Not in `references.bib`: provisional key (Better BibTeX may render the hyphenated surname differently, e.g. `blume-werry2021eyes`; check in Zotero). The PDF is the authors' copy hosted by Neon (see KILDEINFO), with journal layout and DOI 10.5547/2160-5890.10.1.eblu._

## Research question / purpose
Which generation technologies actually set the hourly day-ahead price in European markets, compared with the "conventional belief" that coal- or gas-fired plants are the marginal units in most hours (abstract, p. 1–2)? Also: how much is price setting in one country driven by foreign plants via interconnection (p. 2, 6–9)?

## Setting
- **System:** 20 interconnected European bidding zones/countries incl. Norway, Sweden, Finland, Denmark, Germany, NL, GB, Iberia, Italy, etc. (footnote 1, p. 2).
- **Markets:** day-ahead wholesale (hourly).
- **Horizon and resolution:** reference year 2020 (8,784 hours), modelled in spring 2018 with ICE forward fuel prices (p. 6, 10).

## Method
- **Model type:** Green-X, deterministic partial-equilibrium dispatch and investment model, total-cost minimisation; plant database of units > 10 MW; hourly merit-order dispatch with NTC-limited cross-border trade (TYNDP), copperplate within countries; price-inelastic exogenous demand (p. 5–6).
- **How uncertainty is represented:** none (deterministic) (p. 6).
- **Hydro treatment:** reservoirs and PHS are dispatched with **shadow prices reflecting the marginal cost of an alternative thermal plant**, manually adjusted until dispatch reproduces historic monthly reservoir levels (p. 4, 6). The authors note that "price setting" by hydro is thus somewhat misleading: the opportunity cost of water equals the expected future value of electricity (p. 4).
- **Analysis:** for each hour, identify the marginal (price-setting) technology and its country; aggregate over the year and by price tercile (p. 9–12).
- **Calibration:** back-tested against historic averages, spreads, peak/off-peak, flows (p. 6). The authors stress the results are "imperfect simulations", not observations (p. 6).

## Data / case
Green-X power plant database; ICE fuel forwards (spring 2018); historic load profiles; NTCs from ENTSO-E TYNDP (p. 5–6).

## Key findings
- (p. 1, abstract) Coal- and gas-fired plants set the price in only about **40 %** of all hours across the countries studied. The body (p. 9, 12) gives gas ≈ one third of hours and coal + lignite together > a quarter (lignite larger than hard coal), with all three fossil technologies below two thirds; the 40 % therefore appears to exclude lignite (consistent reading, but check Fig. 5 before quoting).
- (p. 9) **Reservoirs and pumped hydro set the price for about a quarter of all hours**; nuclear just under 10 %; renewables incl. run-of-river a similar share. > 90 % of hours are set by reservoirs/PHS, nuclear, gas, coal, lignite.
- (p. 9–10) In Norway, Sweden and Finland, Norwegian reservoirs and Finnish/Swedish nuclear share the price-setting hours; similar patterns across the three.
- (p. 10) Lowest-priced tercile: nuclear ≈ a quarter of hours, lignite ≈ a fifth, gas also ≈ a fifth (dominant in GB, Iberia, Italy).
- (p. 11) Medium tercile: gas, reservoirs/PHS, and lignite+coal each ≈ one third; in the Nordics, **Norwegian reservoirs set the price for the great majority of hours**.
- (p. 11–12) Highest tercile: gas ≈ two fifths, coal ≈ one fifth; reservoir share slightly lower than in the medium tercile, including in the Nordics.
- (p. 12) Nordic prices even in the highest tercile mostly not significantly above coal marginal cost. Norwegian reservoirs set the price, but their water values reflect the next dispatchable plant, which can be **German coal or lignite** — so German off-peak generation influences Nordic prices indirectly.
- (p. 6–9) High interconnectivity: ~75 % of Dutch hours are set by foreign plants (abstract, Fig. 2); Germany also strongly linked; GB and Iberia little affected.
- (p. 13) Conclusion: hydro-storage and PHS set the price in most hours in Northern Europe; national policies spill over through price setting.

## Strengths
- Explicit hour-by-hour attribution of the marginal technology across 20 coupled markets.
- Clear statement of how hydro "price setting" really works (water values linked to thermal alternatives), relevant to Nordic price formation.

## Weaknesses / limitations
- Model results for a forecast year (2020 modelled in 2018), not observed market data; deterministic; inelastic demand; no intra-country grid.
- Hydro dispatch via manually tuned shadow prices to match historic monthly levels — simplistic for hydro-dominated systems.
- Pre-dates the 2021–2023 gas price crisis, when gas-driven price setting in Europe and price coupling to the Nordics changed considerably (our inference).
- Figures are bar charts with few exact numbers in the text; shares must be read from Figs. 5–8.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.4: merit order and marginal pricing | Definition of price setting by marginal unit; residual load concept | Sect. 1–2, p. 1–4 |
| Background 2.5: Nordic price formation via water values | Reservoirs set Nordic prices in most hours; water values reflect next thermal unit (German coal/lignite) | p. 4, 6, 11–12 |
| Background 2.5: hydro/PHS as price setters in Europe | ≈ a quarter of hours, mainly mid/high-priced | p. 9, 12–13 |
| Background 2.4: market coupling and cross-border price setting | 75 % foreign price setting in NL; large-country dominance | p. 6–9, Figs. 2–4 |
| Background 2.5: negative prices and low-price hours | Link to renewables, inflexibility | p. 3 |
| Background: water value as opportunity cost | Opportunity cost of water = expected future value of electricity | p. 4, 6 |

## Useful quotes (with page numbers)
> "Reservoirs and hydro-storage plants have effectively very low marginal costs and are, however, often the marginal unit to satisfy demand." (p. 4)

> "During most hours in the Nordics, Norwegian reservoirs set the price as per the modelling results." (p. 12)

## Follow-up references to check (backward snowballing)
- Germeshausen & Wölfing (2020), Energy Policy 142: how marginal is lignite? price-setting technologies.
- Hirth (2018), Energy Journal 39(1): factor decomposition of the drop in European power prices.
- Ferkingstad, Løland & Wilhelmsen (2011), Energy Economics 33(3): causal modelling of Nordic/German electricity and fuel prices.
- Faria & Fleten (2011), CMS 8: day-ahead bidding for a Nordic hydropower producer with Elbas (in our library as `faria2011day`).
- Botterud & Auer (2020), EEEP: gas–electricity price correlation Europe vs US.
- Keles et al. (2020), Energy Economics: cross-border effects on Swiss prices.

