---
bibkey: rex2024hydropower
bibkey_provisional: true
title: "Hydropower investment decisions. The ProdRisk-Shop simulator: decision support tool for revenue calculations"
authors: "Stefan Rex, Birger Mo, Linn Emelie Schäffer, Siri Gulaker Mathisen"
year: 2024
venue: "HydroCen Report 45, Norwegian Research Centre for Hydropower Technology (NTNU/SINTEF), Trondheim, June 2024. ISBN 978-82-93602-46-0"
peer_reviewed: false
methods: [heuristics-simulation, deterministic-lp-milp, hydro-production-function]
review_sections: [market-participation, reservoir-sizing-capacity, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "SINTEF ProdRisk (SDDP cuts) + SHOP (weekly detailed MILP) revenue simulator for Norwegian hydro investment analysis; adds strategy re-optimisation (head effects) and reserve capacity markets; reserves only in the short-term model distort reservoir handling, and up-regulation reserves lower / down-regulation reserves raise water values."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/05_Investering_opprusting_og_okonomi/Rex2024.pdf
---

# ProdRisk-SHOP simulator for hydropower investment revenues (Rex et al., 2024)

HydroCen Report 45 (WP 3.3 "Optimal hydro design in the future power system"), quality-assured by Arild Helseth (SINTEF). NVA record: https://nva.sikt.no/registration/0198cc611293-cfebdaf1-c2ca-4b92-bf63-4e489ca5d77a. Cover abbreviates the last author as "Siri Mathisen".
**Page convention:** printed page = PDF page − 2 (PDF 10 = p. 8). 61 PDF pages; read in full.

## Research question / purpose
Document the ProdRisk-SHOP simulator, which computes production revenues of existing and future hydro systems for NPV-based investment analysis, and two new functionalities: (i) **re-optimisation** of the long-term strategy during the simulation (better head representation, denser cuts), and (ii) **reserve capacity markets** in the short-term model and in both models; a "snipping" method to cut computation time is mentioned (p. 3, 11, 55).

## Setting
- **System:** Norwegian cascades: artificial 2-reservoir test system (Module A 684 Mm³, Module B 104 Mm³, 100 % efficiency) (p. 19); **Røssåga** (4 modules, Røsvatn 2363 of 2600 Mm³; head variation ~10 % at Øvre Røssåga, 2.4 % at Fallfoss) (p. 23-24); **Røldal-Suldal (RSK)** and its eastern part (4 reservoirs, 2 plants, Holmevann 96 Mm³) (p. 29-30, 37, 43-44). No pumped storage is modelled in the case studies; PHS is named as an investment option of current interest (p. 8-9).
- **Markets:** spot (day-ahead) energy; reserve capacity markets: non-spinning "RR" and spinning "FRR" up-regulation (SHOP), and up/down non-spinning reserves in both models (p. 28, 42-43). No activation, no intraday.
- **Horizon and resolution:** ProdRisk planning horizon 2-5 years in weekly stages; SHOP weekly problems run week by week through all scenarios (52 × number of scenarios runs); price data 3-hourly (p. 12, 30).

## Method
- **Model type:** two-model chain imitating Norwegian practice (p. 12):
  - **ProdRisk:** SDDP-based long-term strategy under inflow and price uncertainty; strategy = Benders cuts per week (interpretable as water values); requires a convex model; final simulation can use some non-convex relations (PQ curve) (p. 12). End-of-horizon water values come from another tool (e.g. Vansimtap) (p. 12). Head handled via an assumed average head per week (cuts shared by all scenarios), which scales the PQ curve for the week and adds a precomputed "head value" term (p. 13-15).
  - **SHOP:** deterministic short-term MILP with detailed physics (unit efficiencies, start costs, losses, head) run week by week, using ProdRisk cuts as end-of-week water value (p. 12, 25).
- **How uncertainty is represented:** historical inflow years (e.g. 58 for Røssåga 1958-2015); spot prices from EMPS "Low Emission" scenario (HydroCen Report 5), 30 weather years, 3-hourly, rescaled to NO2 2022 mean; reserve prices = observed NO2 2022 series repeated every year (deterministic), so spot-reserve correlation is not modelled (p. 24, 30, 42-43). The internal stochastic model of ProdRisk is not described in this report (see Gjelsvik et al. 2010).
- **Re-optimisation (Sec. 3.2):** shorter parallel-mode ProdRisk runs started from SHOP's actual state, with original cuts as end values; frequency and horizon are tuning parameters; overlapping horizons avoid end-effect discontinuities (p. 16-19, 22).
- **Reserves:** capacity limited by min/max production and head; spinning condition needs binaries (p. 28); market volume limits as % of installed capacity (20 % RR, 10 % FRR in RSK; 20 % of max production for East RSK) (p. 30, 43). In ProdRisk (available from 2024): one up and one down market, same time resolution as spot, deterministic reserve prices, no activation (p. 42).
- **Cost of wear:** piecewise-linear discharge cost below best efficiency point (slopes 1 and 8 EUR/h/(m³/s)), requiring unit-commitment binaries (p. 34-35).

## Data / case
See Setting. Computation: test case SHOP simulation over 50 scenarios on 8 cores: 45 min (no reserves), 1:40 h (RR), 6:50 h (RR+FRR) (p. 34); full RSK SHOP time +~25 % per added market (p. 34); with reserves in both models the simulator time rises 38 % (up), 64 % (down), 102 % (both) (p. 53).

## Key findings
- (p. 9) Industry practice: investment analysis = revenue simulation (weekly to hourly) + separate static NPV with scenario prices; this may underestimate price uncertainty and so flexibility investments. Capacity and pumping upgrades add little energy but flexibility, so their revenue depends on price variability and short-term response → detailed short-term modelling matters for investment analysis.
- (p. 10) Summary of Kleiven et al. (2024 working paper): including hourly production flexibility can give **up to 20 % larger capacity installations**; value of optimally delaying investment falls as hourly price variability rises.
- (p. 21) Test case with variable head: re-optimisation adds ~4 MEUR (yearly) and ~6 MEUR (seasonal) over 50 years vs ~870 MEUR without; longer update horizons better (p. 22).
- (p. 24-26) Røssåga: ProdRisk 6740 vs SHOP 6280 MEUR sales revenue (7 % gap) from model differences; updates help SHOP only when reservoirs are not emptied every year.
- (p. 28-29) Test case with reserve price = factor × spot price: low factor → reserves sold from spare capacity without changing production; ~0.5 × spot → production pattern changes substantially; high → spill/bypass to maximise reserve sales.
- (p. 33-34, Table 1, RSK, reserves in SHOP only; row mapping reconstructed from garbled extraction) production ≈ 91.5 % / 90.9 %, spot revenue 89.5 % / 88.2 %, total revenue 114.3 % / 115.1 % of the no-reserve case (text: "total revenue ... increases by roughly 15 %", production "decreases by roughly 9 %").
- (p. 27, 33) With up-regulation reserves only in SHOP, simulated reservoir operation deviates clearly from ProdRisk: **the assumption that water values computed without reserves remain valid does not hold** for RSK (based on the extreme 2022 price year); "water values that do not account for reserve markets are presently used by many hydro producers in the Nordics" (p. 27).
- (p. 40) Scaling up intraday spot-price volatility (daily mean kept) **reduces reserve allocation**: flexibility is used for spot arbitrage instead; spinning condition and wear costs make reserves less attractive in volatile spot markets.
- (p. 41) Discharge cost curve cuts estimated wear costs by ~50 %.
- (p. 44-46) East RSK, reserves in SHOP only: up-regulation raises upstream (Holmevann) storage, down-regulation lowers it, symmetric up+down roughly cancel. With reserves also in ProdRisk, average filling moves back towards the no-reserve case; SHOP-only gives "a too strong incentive to hold back water" (p. 45).
- (p. 46-49) Up-regulation reserves remove most full-power hours and create a plateau at P_max − reserve; reserves add roughly 20 % revenue per reserve market, near-maximal because reserve prices were high and limits arbitrary (20 %) (p. 49).
- (p. 50) Including reserves in the strategy raises total income in all cases, most for down-regulation only (~1 % of total revenue).
- (p. 50-53, Figs. 42-45) **Up-regulation reserves systematically lower marginal water values; down-regulation reserves raise them** (confirming Helseth et al. 2017); relative water values between reservoirs barely change, which is why reservoir handling changes little.

## Strengths
- Directly from the developers of the Norwegian industry-standard tools; shows the strategy-simulation coupling and its inconsistencies concretely.
- Quantifies how reserve markets change water values and reservoir handling, with up vs down separation.
- Transparent about limitations (deterministic reserve prices, no activation, arbitrary market limits).

## Weaknesses / limitations
- Research report, not peer reviewed; contains editorial leftovers (p. 28 "Make clear if water values are computed with respect to reserve prices in cases below."; Fig. 15 caption "(Does axis cover EUR/MWh and EUR/MW?)", p. 31).
- Reserve prices deterministic and repeated from one extreme year (2022); no spot-reserve correlation; no activation (p. 30, 42-43).
- Few scenarios (20-30) in reserve cases; no PHS case; results "crucially depend on the price assumptions as well as the reserve market limits" (p. 49).
- Tables garbled in the PDF text layer (Table 1).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review: investment/sizing practice in Norway | Revenue simulation + static NPV; flexibility upgrades (capacity, pumping) depend on price variability | p. 9, Sec. 1.3 |
| Lit. review: sizing with hourly flexibility | Kleiven et al.: up to 20 % larger capacity when hourly flexibility included | p. 10, Sec. 1.4 |
| Lit. review: market participation (reserves and water values) | Up-reg lowers, down-reg raises water values; SHOP-only reserves distort reservoir handling | p. 27-28, 42-53, Sec. 4.1, 4.4 |
| Model: include reserves in the long-term (SDDP) problem | Water values without reserves invalid for RSK; income gain from reserves in strategy | p. 27, 33, 45, 50 |
| Model: reserve modelling simplifications | Capacity only, no activation, deterministic prices, market limit % of capacity | p. 30, 42-43 |
| Background: Norwegian tools | ProdRisk (SDDP, cuts), SHOP (MILP), EMPS prices, Vansimtap end values | p. 9-12 |
| Background: price volatility vs reserves | More intraday volatility → less reserve allocation | p. 40 |
| Model: head effects in SDDP | Average-head approximation in ProdRisk and its bias; re-optimisation benefit | p. 13-15, 21 |
| Research gap | Ancillary services value not covered; reserve-spot price relationship needs research | p. 55 |

## Useful quotes (with page numbers)
> "water values that do not account for reserve markets are presently used by many hydro producers in the Nordics." (p. 27)

## Follow-up references to check (backward snowballing)
- Helseth, Fodstad, Mo (2016), "Optimal medium-term hydropower scheduling considering energy and reserve capacity markets", IEEE TSTE 7(3), 934-942.
- Helseth, Mo, Fodstad (2017), "Water values in future power markets", IEEE PowerTech.
- Høgenvik, Mathisen, Helseth, Mo (2022), "A comprehensive simulator for hydropower investment decisions", PMAPS.
- Kleiven, Nadarajah, Fleten (2024), "Hierarchical planning for hydropower capacity upgrade", SSRN working paper; Kleiven (2022) NTNU PhD thesis.
- Mo & Høgenvik (2020), HydroCen Report 19 (basic simulator).
- Helseth et al. (2023), hydropower scheduling toolchains Brazil/Norway/USA, J. Water Resour. Plann. Manage.
- Gjelsvik, Mo, Haugstad (2010), bib `gjelsvik2010`.

