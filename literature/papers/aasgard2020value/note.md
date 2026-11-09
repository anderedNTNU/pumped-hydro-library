---
bibkey: aasgard2020value
bibkey_provisional: true
title: "The value of coordinated hydropower bidding in the Nordic day-ahead and balancing market"
authors: "Ellen Krohn Aasgård"
year: 2020
venue: "Energy Systems 13, 53–77 (2022; published online 12 May 2020)"
peer_reviewed: true
methods: [multistage-scenario-trees, uncertainty-modelling]
review_sections: [market-participation, electricity-markets, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/01_Aasgard_2020_The_value_of_coordinated_hydropower_bidding_in_the_Nordic_day_ahead_and_balancing_market.pdf
takeaway: "72-h multistage stochastic bidding model (inside SINTEF's SHOP framework) for a Norwegian (NO2) hydro plant in the day-ahead and mFRR balancing market; balancing participation adds 0.8–2.6% (sequential) or 1.4–2.9% (coordinated), and the value of coordination is larger under more uncertainty (1.7% vs 1.1%)."
---

# Value of coordinated bidding in day-ahead and balancing markets (Aasgård, 2020/2022)

_PDF page 1 = journal p. 53 (offset +52). Not in `references.bib` yet: provisional key; if Zotero stores the issue year 2022, Better BibTeX would generate `aasgard2022value` instead._

## Research question / purpose
How much does a Nordic hydropower producer gain by participating in the **balancing market (FRR-M / regulating power market)** in addition to the day-ahead market, and what is the extra value of **coordinating** bids across the two markets rather than bidding sequentially (abstract, p. 53; p. 54)? Main contribution: computing lower and upper bounds on these values (limited vs perfect information on the balancing market) for a realistic hydropower case, with a forecast-based scenario-generation method (p. 54).

## Setting
- **System:** example plant with two generating units below a single reservoir: 50 Mm³ storage, max discharge 150 m³/s (reservoir can be emptied in ~90 h), units 30 MW min / 50 MW max; described as very flexible (p. 70). No pumping.
- **Markets:** Nord Pool day-ahead (NO2) and the Norwegian balancing market for tertiary reserve (regulating power market, FRR-M) — energy activation with **premiums** over day-ahead and a stochastic **volume limit** (pp. 56, 59, 64). Day-ahead bids at noon the day before; balancing bids up to 45 min before the hour (p. 57). Intraday not modelled. Day-ahead turnover 394 TWh in 2017 (p. 59).
- **Horizon and resolution:** 72 hours, hourly; scenario tree with daily branching at hours 24 and 48 (pp. 57–58, 66). Test days: 46 instances in the first 33 weeks of 2018 (p. 70).

## Method
- **Model type:** multistage stochastic program in scenario formulation (eqs. 1–5, pp. 56–58), implemented within SHOP-type short-term scheduling (unit commitment, start/stop costs, detailed hydro constraints) (pp. 56–57). Market sales sum to production with penalised imbalances (3). Explicit non-anticipativity (4) and **market non-anticipativity** (5): day-ahead trades cannot depend on next-day price realisations (p. 58).
- **How uncertainty is represented:**
  - *Day-ahead price:* 24-hour panel model (Huisman et al. [14]): deterministic hour/weekday/season dummies + AR(1) between the same hour on consecutive days, estimated by SUR (R `systemfit`); strong cross-hour error correlations (pp. 59–63, Tables 1–3).
  - *Balancing market:* premiums (not prices), weakly correlated with day-ahead prices so modelled independently (p. 64). Event-driven, unevenly spaced time series (Croston-type moving-average arrival rate; balancing demand in 71% of hours, mean 1.23 h between events; α ≈ 0.01) plus AR(1)-type unevenly spaced models for volume (φ = 0.83, σ = 70.54) and premium (φ = 0.76, σ = 38.58) (pp. 64–65). An individual producer can take the whole market volume with a given probability (e.g. 1 in 10) (p. 65).
  - *Scenario trees:* forecast-based method of Kaut [9] combining point forecasts with historical forecast errors; training 2014–2016 (models), 2017 (forecast errors), test first 33 weeks of 2018 (pp. 65–66). Separate trees per market (base: 3 branches → 9 scenarios each), combined all-against-all into 81 scenarios (pp. 69–71).
  - Intraday uncertainty in the balancing market ignored: balancing prices and volumes are revealed with day-ahead clearing (daily branching), for tractability (p. 58).
- **Solution method:** direct solution of the deterministic equivalent (~15 s per run for 81 scenarios; >1 h for 256) (pp. 71, 75).
- **Key modelling choices and assumptions:**
  - Three strategies: day-ahead only; **sequential** (lock day-ahead from the day-ahead-only run, then optimise balancing); **coordinated** (joint) (pp. 69–70).
  - **Lower bound** (limited information): balancing trades fixed together with day-ahead trades, before balancing prices are known. **Upper bound** (perfect information): balancing trades decided knowing realised balancing prices/volumes (p. 70).
  - **End-of-horizon water value = average day-ahead price in the day's scenario tree**; initial reservoir reset to 50% each day (p. 71). The author notes water values should properly come from longer-term models (p. 71).

## Data / case
- Nord Pool ftp data for NO2 day-ahead and balancing prices and turnovers, EUR/NOK exchange rates (p. 66).
- Day-ahead model underpredicted 2018 prices (higher than normal), but used consistently across cases (p. 68).

## Key findings
- (p. 72, Fig. 9) Limited information: average gain sequential vs day-ahead-only **0.8%**, coordinated **1.4%**, coordinated vs sequential **1.7%**.
- (p. 73, Fig. 11) Perfect information: sequential **2.6%**, coordinated **2.9%**, coordination **1.1%**.
- (p. 74) Value of coordination higher with more uncertainty; results specific to this very flexible system.
- (p. 74) With a balancing market the producer shifts from storing towards producing, since it can get higher prices than the (day-ahead-based) water value; "opportunities in multiple markets should be reflected in longer-term models that calculate the value of water."
- (p. 75, Tables 4–5) Bounds move with tree size (4/9/16 branches per market) but the qualitative result holds.
- (p. 54) Very few Nordic hydropower companies use formal optimisation for trades beyond day-ahead; Boomsma et al. [2] found much larger gains (9.60–30.79% from balancing participation, 8.03–24.79% from coordination).

## Strengths
- Clear lower/upper-bound design for valuing an extra market under information assumptions.
- Realistic Nordic market timing and non-anticipativity structure.
- Dedicated statistical model for the intermittent, event-driven balancing market (premium + volume).
- Embedded in the industry-standard short-term model framework.

## Weaknesses / limitations
- Only 72 h; water value crudely set to average day-ahead price; reservoir reset daily, so no long-term or seasonal effect.
- Balancing uncertainty within the day ignored (daily branching).
- Balancing **energy** only; no reserve **capacity** products (FCR, aFRR, mFRR capacity).
- Single, very flexible plant; day-ahead model poor for 2018.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Research gap: multi-market value should enter long-term water values | Conclusion of case study | p. 74 |
| Lit review (market participation): value of balancing market for hydro | +0.8–2.6% sequential, +1.4–2.9% coordinated | pp. 72–74, Figs. 9, 11 |
| Lit review: sequential vs coordinated bidding | Definitions and value of coordination | pp. 54, 69–70 |
| Background (electricity markets): Nordic market sequence and gate closures | Day-ahead noon, balancing 45 min before; FRR-M balancing market | pp. 55, 57, 59 |
| Background: industry practice | Few companies optimise beyond day-ahead | p. 54 |
| Method: balancing market price/volume modelling | Unevenly spaced time series, premium vs price | pp. 64–65 |
| Method: forecast-based scenario trees | Kaut method, training/test split | pp. 65–69 |
| Comparison: Boomsma et al. larger gains | 9.60–30.79% | p. 54 |

## Useful quotes (with page numbers)
> "The results here indicates that opportunities in multiple markets should be reflected in longer-term models that calculate the value of water." (p. 74)

## Follow-up references to check (backward snowballing)
- [2] Boomsma, Juul, Fleten (2014), bidding in sequential markets: the Nordic case, EJOR 238(3).
- [13] Klæboe, Eriksrud, Fleten (2015), benchmarking forecasting models for balancing market prices, Energy Systems 6(1).
- [9] Kaut (2017), forecast-based scenario-tree generation, Optimization Online.
- [6] Faria & Fleten (2011), day-ahead bidding taking Elbas into account, CMS (in inbox).
- [8] Vardanyan (2016), bidding in sequential markets with risk, KTH thesis.
- [11] Skjelbred (2019), unit-based short-term hydro scheduling, NTNU thesis.

