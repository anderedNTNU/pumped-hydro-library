---
bibkey: lohndorf2023
title: "The Value of Coordination in Multimarket Bidding of Grid Energy Storage"
authors: "Nils Löhndorf, David Wozabal"
year: 2023
venue: "Operations Research 71(1), 1-22"
peer_reviewed: true
methods: [multistage-scenario-trees, uncertainty-modelling, heuristics-simulation]
review_sections: [market-participation, modelling-phs-plants, reservoir-sizing-capacity, price-volatility]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/Innlimte_referanser_2026-10-29/lohndorf2023.pdf
takeaway: "35-stage stochastic program for day-ahead bidding plus hourly continuous intraday trading with price impact (German EPEX, 2017 days): coordination is worth 10.0-29.1% for a 1 GW / 8 GWh pumped-hydro plant, 8.3-8.5% for a 10 MW battery and only 1.0-1.6% for a 100 MW reservoir without pump; reoptimisation policy within 0.0-7.2% of an information-relaxation upper bound."
---

# Value of coordinating day-ahead and intraday bidding of storage (Löhndorf and Wozabal, 2023)

_Page mapping: journal page = PDF page − 2 (PDF pp. 1-2 are the VU repository and INFORMS cover pages; journal pp. 1-22 = PDF pp. 3-24). Published version of record. Published online 31 January 2022 (Klæboe et al. 2022 cite it as "Löhndorf and Wozabal (2022)")._

## Research question / purpose
- What is the value of a **coordinated** strategy, where day-ahead (DA) bids anticipate continuous intraday (ID) trading opportunities, compared with a **sequential** strategy that bids DA first and then reoptimises in ID, for different types of grid energy storage (pp. 1-2)?
- Methodological contributions (p. 3): (1) scenario trees that preserve the martingale property and do not grow exponentially, giving lower bounds; (2) a reoptimisation heuristic giving an implementable policy; (3) an information-relaxation upper bound with **optimal bilinear penalties**.

## Setting
- **System:** three stylised storage assets (p. 17): (i) **pumped-hydro storage 1,000 MW, 8,000 MWh** (8 h at full power), initial level 2,000 MWh, 75% round-trip efficiency; (ii) **battery 10 MW** that can be filled/emptied in one hour, 95% efficiency, empty at start; (iii) **seasonal hydro reservoir without pump**, 100 MW, large reservoir, continuous deterministic inflow equivalent to 50 MW.
- **Markets:** German EPEX SPOT day-ahead auction (price-taker, piecewise-constant bid functions with Z = 3 breakpoints, as Löhndorf et al. 2013) and continuous intraday market for hourly products (price-setter with temporary linear price impact) (pp. 7-8, 17). Reserves (ancillary services) mentioned but not modelled (p. 1).
- **Horizon and resolution:** one day; 35 stages: t = 0 DA bid (before 12:00), t = 1 DA clearing (12:45), t = 2..34 hourly intraday trading from 15:00 to 22:00 next day; each hourly product tradable for nine hours until the hour before delivery (pp. 8-9).
- Market facts (p. 7): EPEX total 567 TWh in 2018; German ID 82 TWh vs DA 485 TWh in 2018; ID trading for a given hour opens 15:00 the day before, continuous until 5 minutes before delivery.

## Method
- **Stylised two-period model (Sec. 2, pp. 3-7):** unit storage, price-taker DA, linear price impact λ in ID, expected ID price = DA price. Proposition 1 (p. 4): with DA market orders it is **never optimal to allocate all capacity to DA**, and for small enough price impact it is optimal to trade only ID. Proposition 2 (pp. 5-6): holds even with DA bidding functions if ID margins exceed DA margins (eq. 7), which is true for jointly normal prices when ID variances exceed DA variances. Intuition: ID prices are observed before trading and are more volatile; larger storage behaves like larger λ and makes ID relatively less attractive (p. 5). Value of coordination is driven by liquidity cost, price volatility and information gain (p. 7).
- **Multistage stochastic program (Sec. 3, pp. 7-9):** positions y_t per hourly product, projected storage levels s_t; DA volumes via Heaviside sum of bid quantities (eq. 11); forward-looking storage balance ensuring every position is backed by a feasible schedule (eq. 12, Löhndorf and Wozabal 2021), giving relatively complete recourse; immediate reward DA revenue (eq. 13) and ID revenue with linear price impact (eq. 14), so a convex QP. **Fixed storage level at start and end of the day** to isolate coordination from seasonal value; authors note that in practice short-term planning must be integrated with long-term planning "by using water values", which "can be derived from long-term models such as Löhndorf et al. (2013)" (pp. 7-8). Head effects on power capacity and efficiency ignored (p. 7).
- **How uncertainty is represented (Sec. 4, pp. 9-11):** DA prices = regression with weekly piecewise-linear trend and weekday dummies per hour (eq. 15; MAE EUR 5.56), residuals used as empirical distribution (Oct 2015 - Sep 2018). ID prices of each hourly product as **arithmetic random walk without drift** starting at the realised DA price (eq. 16); ADF test does not reject a unit root in 77% of series; innovations = centred empirical residuals (eq. 17), separate summer/winter distributions; martingale assumption supported by data (Fig. 2a). Price impact: linear regressions of price on cumulative volume per hour and product from tick data, slope modelled log-linearly in time-to-maturity (eq. 18); negligible within six hours of delivery, about 1.47 EUR/MWh for the 12:00 product traded 21 h ahead (p. 11). ID data Nov 2015 - Sep 2017.
- **Solution method (Sec. 5, pp. 11-16):**
  - *Scenario tree lower bound:* conditional-mean discretisation gives a lower bound for concave rewards by Jensen (Prop. 3, pp. 12-13). Algorithm 1 builds the tree stage by stage with **k-means** on samples from each parent's partition (Wasserstein-2 / Voronoi argument, eqs. 22-24, pp. 13-14), splitting the node with the largest internal variation until L_t nodes; sample means corrected to keep the martingale property (Remark 1, p. 14). Terminal nodes L_T = 10,000 (default), node count growing linearly with stage (eq. 37, p. 17).
  - *Reoptimisation heuristic (RH):* first-stage from the tree, later stages solved by a deterministic receding-horizon QP with expected prices (eqs. 26-27, p. 14) — implementable policy.
  - *Sequential benchmark:* two-stage problem ignoring ID for the DA bid, then greedy ID reoptimisation (eqs. 28-29, pp. 14-15); pure ID strategy by setting DA bids to zero (Remark 2, p. 15).
  - *Information relaxation upper bound (IR):* perfect-information problem with penalty; optimal bilinear penalty found by dualisation into a single convex stochastic program with expectation constraints (Prop. 4, pp. 15-16), solvable by SAA because innovations are centred and stagewise independent.
- **Key modelling choices and assumptions:** risk-neutral; martingale prices (no systematic DA-ID spread, required to avoid speculation and by the regulator's balanced-schedule rule) (p. 7); temporary price impact only (Gatheral and Schied 2013); storage limits independent of content (no head effects); in-kind losses (pp. 7, 9).

## Data / case
- Days simulated: 21 June (summer) and 21 December (winter) 2017; average day-night spread EUR 16.10 vs 35.34 (pp. 17, 20).
- FICO Xpress barrier, 16-core Xeon 6130, 256 GB; L_T = 10,000 takes about 90 min, 30,000 about 6 h, 100,000 exceeds memory (p. 17). Out-of-sample evaluation with n = 10,000 simulated paths (p. 18); bounds estimated on 5,000 scenarios (p. 18).

## Key findings
- (Table 1, p. 18) Tree lower bounds increase with terminal nodes (e.g. PHS summer 37,279 → 42,131 EUR from 100 to 30,000 nodes).
- (Table 2, p. 18) Lower/upper bounds, EUR: PHS summer SP 41,965, RH 65,182, IR 70,241, PI 127,638; PHS winter 142,153 / 171,039 / 175,894 / 281,052; battery summer 334 / 598 / 597 / 1,792; battery winter 467 / 873 / 870 / 2,687; reservoir summer 48,791 / 50,327 / 50,482 / 58,714; reservoir winter 68,717 / 70,298 / 70,400 / 83,334 (row assignment reconstructed from garbled extraction; consistent with the gaps quoted in the text). IR-RH gap 0.0% (battery) to 7.2% (PHS); IR is 14.0-67.6% tighter than perfect information; tree (SP) underestimates RH by 3.0% (reservoir) to 35.6% (PHS) (p. 18).
- (Table 3, pp. 18-19; totals reconstructed, they match Table 2 RH values) Average profit, intraday-only / sequential / coordinated, EUR: PHS summer 38,372 / 50,476 / 65,182; PHS winter 94,829 / 155,544 / 171,039; battery summer 513 / 551 / 598; battery winter 783 / 806 / 873; reservoir summer 35,681 / 49,554 / 50,327; reservoir winter 49,976 / 69,595 / 70,298.
- (p. 18) **PHS gains 10.0-29.1%** from coordination over sequential; intraday-only loses 41-45% vs coordinated. Coordinated PHS accepts lower, even negative, DA profit (e.g. about −22,800 EUR in summer) offset by higher ID profit (p. 18; Table 3).
- (p. 18) **Battery gains 8.3-8.5%**; intraday-only loses only 10.3-14.2%, so small storage may skip DA entirely.
- (pp. 19-20) **Reservoir without pump hardly benefits** (our calculation from Table 3: about 1.0-1.6%); makes most profit DA; "focusing on day-ahead price volatility as in Löhndorf et al. (2013) therefore seems sufficient" for large inflexible storages (p. 20).
- (p. 20, Fig. 6) Coordinated DA bids are not bang-bang and do not use full power capacity; they match final ID positions better. Coordinated ID trading splits trades over hours considering price impact and increases volume close to delivery (Fig. 7).
- (p. 20) Storage value higher in winter than summer because of the larger day-night spread.
- (pp. 20-21) Conclusion: value of coordination driven by **storage flexibility and price impact**; large flexible PHS benefits most; owners of inflexible reservoirs lose little by not trading ID. Future work: non-martingale prices (Ito and Reguant 2016), portfolio-level bidding, continuous-time order book.

## Strengths
- Combines theory (stylised propositions), realistic multistage model, and rigorous lower and upper bounds with small gaps.
- Directly compares PHS, battery and a no-pump reservoir under the same market model: a clean asset-type comparison.
- Empirical price model of DA and ID with price impact estimated from order book data.
- Out-of-sample evaluation with many paths; bounds quantify policy quality.

## Weaknesses / limitations
- One-day horizon with fixed start and end storage level: no seasonal/water value interaction, so the reservoir case is artificial (must release inflow within the day).
- Only two days of 2017 German data; no reserves; risk-neutral; martingale assumption.
- Head effects ignored; stylised asset parameters, not a real plant.
- Table layout in the text extraction is scrambled; numbers above reconstructed (sums verified).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Literature review 5.4: day-ahead + intraday coordination for storage | Value 10.0-29.1% PHS, 8.3-8.5% battery, ~1-1.6% reservoir | pp. 18-20, Tables 2-3 |
| Model / limitations: why intraday is omitted (and what is lost) | Reservoir case: DA sufficient; PHS case: large loss | pp. 3, 19-21 |
| Literature review 5.5: asset type / storage duration matters for market value | PHS 1 GW/8 GWh vs battery 10 MW/1 h vs reservoir 100 MW | p. 17, Table 3 |
| Theory: never optimal to put all capacity in DA (stylised) | Props. 1-2 | pp. 4-6 |
| Background 2.4: German DA vs ID volumes, ID timing | 485 vs 82 TWh (2018); ID 15:00 to 5 min before delivery | p. 7 |
| Background 2.5: ID prices more volatile than DA, martingale DA-ID | Fig. 2, random walk, ADF 77% | pp. 5, 10-11 |
| Method: integrating short-term with long-term via water values | Statement referencing Löhndorf et al. 2013 | p. 8 |
| Method: lower/upper bounds for policy evaluation (information relaxation) | Prop. 3 (tree LB), Prop. 4 (bilinear penalty UB) | pp. 12-16 |
| Uncertainty modelling: scenario tree by k-means / Wasserstein | Algorithm 1, eqs. (22)-(24) | pp. 13-14 |
| Model: storage efficiency and head effects ignored (assumption) | Assumptions | p. 7 |

## Useful quotes (with page numbers)
> "coordinated bidding is most valuable for flexible storage assets with high price impact, like pumped-hydro storage" (p. 1)

## Follow-up references to check (backward snowballing)
- Boomsma, Juul, Fleten (2014). Bidding in sequential electricity markets: the Nordic case. EJOR 238(3).
- Kongelf et al. (2019). Portfolio size's effects on gains from coordinated bidding. Energy Systems 10(3).
- Wozabal, Rameseder (2020). Optimal bidding of a virtual power plant on the Spanish day-ahead and intraday market. EJOR 280(2).
- Bertrand, Papavasiliou (2019). Adaptive trading in continuous intraday electricity markets for a storage unit. IEEE TPWRS.
- Löhndorf, Wozabal (2021). Gas storage valuation in incomplete markets. EJOR 288(1).
- Densing (2013). Dispatch planning using newsvendor dual problems and occupation times: application to hydropower. EJOR 228(2).
- Brown, Smith, Sun (2010). Information relaxations and duality in stochastic dynamic programs. OR 58(4).

