---
bibkey: faria2011day
bibkey_provisional: true
title: "Day-ahead market bidding for a Nordic hydropower producer: taking the Elbas market into account"
authors: "Eduardo Faria, Stein-Erik Fleten"
year: 2011
venue: "Computational Management Science 8(1-2), 75-101"
peer_reviewed: true
methods: [two-stage-stochastic, deterministic-lp-milp, uncertainty-modelling, hydro-production-function]
review_sections: [market-participation, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/17_Faria_2011_Day_ahead_market_bidding_for_a_Nordic_hydropower_producer_Taking_the_Elbas_market_into_account.pdf
takeaway: "Two-stage stochastic MILP for day-ahead bidding of a price-taking Norwegian cascade (Otra, 719 MW) with an Elbas intraday recourse, ARMA-GARCH price scenarios: anticipating Elbas changes profit by at most 0.12% (0.65% in a high-volatility case), so day-ahead bidding can be modelled without intraday trading."
---

# Day-ahead bidding with Elbas (Faria and Fleten, 2011)

_Page mapping: journal page = PDF page + 74 (journal pp. 75-101). DOI 10.1007/s10287-009-0108-5 (from the PDF; no KILDEINFO file was found next to this PDF in the inbox). Published online 2009, volume year 2011._

## Research question / purpose
- Develop a model to support day-ahead (Elspot) bidding of a **price-taking** hydropower producer in Nord Pool that accounts for the possibility of trading in the intraday market **Elbas**, and measure the value of doing so (pp. 75, 77-78).
- The balancing (regulating) market is excluded: with Elbas available its volume for the producer is "very low" (p. 77).

## Setting
- **System:** three hydropower plants in the upper **Otra cascade** (Holen12, Holen3 upstream of Brokke), Agder Energi, 719 MW in seven units; three reservoirs, two upstream plants share the same downstream reservoir; time delays from upper to lower reservoir (pp. 82-85, Fig. 3). Conventional hydro, **no pumping**. Price area NO1 (p. 91).
- **Markets:** Elspot day-ahead (hourly bids and **block bids**, six 4-hour blocks used instead of all 276 possible blocks) and Elbas continuous intraday (one aggregated trading opportunity per hour, volume limit 5, 10 or 20% of installed capacity) (pp. 79, 82, 86). No reserves.
- **Horizon and resolution:** next day, 24 hourly periods (p. 79).
- Market facts given (useful background): Elspot 2007 turnover EUR 9.1 bn, 291 TWh, > 65% of Nordic consumption (p. 76); Elbas 2007 only 1.6 TWh vs regulating market about 13 TWh (p. 82); spot prices published at about 14:00, production plans to TSO before 19:00 (p. 77); regulating bids executable within 15 min (p. 77); Elbas trading from 14:00 up to one hour before delivery, Norway joining Elbas in Q1 2009 (p. 81).

## Method
- **Model type:** two-stage stochastic **mixed-integer linear program** solved as a deterministic equivalent in Xpress-MP (eq. 22, p. 89; p. 78).
  - *First stage:* hourly and block bid volumes x_it, x_ib for fixed price points p_i (fixed in advance to avoid bilinear terms, following Fleten and Pettersen 2005; equidistant within the range of price scenarios) (pp. 79, 90).
  - *Recourse:* dispatched volumes by linear interpolation of the bid curve (eqs. 2-3, 23) and block acceptance by mean price (eqs. 5, 24) (pp. 79-81, 90); Elbas trades z_t (positive or negative), production with unit commitment and start-up costs (eqs. 7-8), discharge/storage limits, water balance with delays (eqs. 15-16), concave piecewise-linear **production-discharge curves** per unit (eqs. 18-19), energy balance y_t + Σ y_b + z_t = Σ w_it (eq. 20) (pp. 82-86).
  - **Unbiased bidding:** expected Elbas trade must be zero in every hour, Σ_s Σ_e π_s π_e z_t^{s,e} = 0 (eq. 21, p. 88), because system operators require Elspot bids to be unbiased and do not want Elbas to become the de facto spot market (p. 88, footnote 5).
- **How uncertainty is represented:** only prices; inflow deterministic for the 24-h horizon (p. 86). Spot price scenarios from an **ARMA-GARCH** model on log-returns of hourly NO1 prices (lags up to 504 h, GARCH terms up to lag 25) (eqs. 25-31, Table 1, pp. 90-93). Elbas prices from an **ARMAX-GARCH** model with Swedish spot as explanatory variable (hour-specific coefficients), conditioned on each spot scenario (eqs. 32-35, Table 2, pp. 93-95). Correlation spot vs average Elbas price 0.80 (levels) and 0.54 (returns) (p. 87, footnote 6 p. 92). Scenario sets 20, 40 or 60 spot scenarios × 10 Elbas scenarios (200-600 second-stage scenarios), crude Monte Carlo (pp. 93, 95).
- **Key modelling choices and assumptions:** price-taker; net head assumed to vary only with discharge (small reservoir variation in the case), so head effects partly ignored (p. 85); **end-of-horizon water value** as concave piecewise-linear functions V_j of stored water, "available from more long-term models", to avoid emptying reservoirs (eqs. 9-10, pp. 83-84); the model tends to operate at intersections of the piecewise curves, so curves must be specified carefully (p. 85). Elbas collapsed into one trading opportunity per hour (two-stage approximation of a multistage process) (p. 86).

## Data / case
- Nord Pool hourly spot NO1, Sweden spot and Elbas prices, 1 January to 30 November 2007 (pp. 91, 94). Plant data from Agder Energi (p. 95).
- Problem sizes (Table 3, p. 96): 20/40/60 spot scenarios give 136k/272k/408k continuous and 33.6k/67.2k/100.8k binary variables; solved in 87/191/349 s on a 1.6 GHz laptop with 2 GB RAM.
- Value of considering Elbas = (profit with Elbas-aware bids − profit with bids computed ignoring Elbas but Elbas allowed in recourse) / latter (p. 98).

## Key findings
- (p. 95, Fig. 11) The generator offers its full 719 MW at any spot price above 29 EUR/MWh in the example hours.
- (p. 96, Table 4 p. 97) In-sample stability: objective deviates at most 1% (20 scen.), 0.6% (40) and 0.3% (60) from the mean of five replications.
- (p. 98, Figs. 12-13) With Elbas, the bid curve occasionally offers less volume at a given price: the producer saves some energy for possible Elbas trading.
- (p. 99, Table 5) Value of considering Elbas is very low, never above 0.12% (limits 5/10/20%: 0.02-0.03%, 0.05-0.06%, 0.07-0.12%).
- (p. 99, Table 6) With initial conditions from a higher-volatility period: higher but still low, never above 0.65%.
- (p. 100) Conclusion: for a price-taking medium-sized producer, Elbas does not significantly affect profit; "the day-ahead bidding problem can be modeled without Elbas trading".

## Strengths
- Detailed short-term hydro model (cascade, unit commitment, start-up costs, PQ curves, delays, block bids).
- Clean definition of the "value of considering" a later market, which later coordination studies reuse (`klaeboe2022day`, `lohndorf2023`).
- Realistic market rules: unbiased-bid constraint, Elbas liquidity limits.

## Weaknesses / limitations
- 2007 data from before Norway joined Elbas; Elbas model fitted on Swedish data and transferred to NO1 (pp. 87, 94).
- Fixed, arbitrary Elbas volume limit (criticised by Klæboe et al. 2022, p. 689); the model cannot reserve capacity for intraday at the time of day-ahead bidding (criticised by Löhndorf and Wozabal 2023, p. 2).
- Single day, deterministic inflow, no reserves, no pumping, no long-term coupling except via exogenous water values.
- Results for one medium-sized producer; the authors expect different results for thermal producers (p. 100).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model: justify omitting intraday market | Value of considering Elbas ≤ 0.12% (≤ 0.65% high volatility) | pp. 98-100, Tables 5-6 |
| Literature review 5.4: day-ahead + intraday for Nordic hydro | Two-stage stochastic MILP, Elbas recourse | pp. 78, 86-90 |
| Model: end-of-horizon water value from long-term model | Concave piecewise-linear V_j (eqs. 9-10) | pp. 83-84 |
| Model: bidding curves with fixed price points | Eqs. (2)-(5), (23)-(24) | pp. 79-81, 90 |
| Model: unbiased day-ahead bids / expected imbalance zero | Eq. (21), TSO requirement | p. 88 |
| Background 2.4: Nordic market timing and volumes (2007) | Elspot 291 TWh (> 65%), Elbas 1.6 TWh, regulating 13 TWh; gate times | pp. 76-77, 81-82 |
| Uncertainty modelling: ARMA-GARCH price scenarios | Model, parameter tables, validation steps | pp. 90-95 |
| Model: head effects only through discharge | Assumption and justification | p. 85 |

## Useful quotes (with page numbers)
> "the day-ahead bidding problem can be modeled without Elbas trading" (p. 100)

## Follow-up references to check (backward snowballing)
- Fleten, Kristoffersen (2007). Stochastic programming for optimizing bidding strategies of a Nordic hydropower producer. EJOR 181, 916-928.
- Fleten, Kristoffersen (2008). Short-term hydropower production planning by stochastic programming. Comput. Oper. Res. 35, 2656-2671.
- Fleten, Pettersen (2005). Constructing bidding curves for a price-taking retailer in the Norwegian electricity market. IEEE TPWRS 20(2).
- Olsson, Söder (2008). Modeling real-time balancing power market prices using combined SARIMA and Markov processes. IEEE TPWRS 23(2).
- Kristoffersen, Fleten (2009/2010). The development of stochastic programming models for planning short-term power generation and bidding (review).

