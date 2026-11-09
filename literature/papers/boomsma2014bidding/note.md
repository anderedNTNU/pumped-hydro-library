---
bibkey: boomsma2014bidding
bibkey_provisional: true
title: "Bidding in sequential electricity markets: The Nordic case"
authors: "Trine Krogh Boomsma, Nina Juul, Stein-Erik Fleten"
year: 2014
venue: "European Journal of Operational Research 238(3), 797-809 (2014) (volume/pages unverified). PDF filed here = author manuscript, 36 pages"
peer_reviewed: true
methods: [multistage-scenario-trees, uncertainty-modelling]
review_sections: [market-participation, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/11_Web_search_2026-11-04/boomsma2014bidding.pdf
takeaway: "26-stage stochastic program for coordinated day-ahead (Elspot) and hour-ahead balancing-market bidding by a Nordic hydro producer: under a two-price imbalance system coordination raises daily profit by 8-25 % (price-taker, 2010) or 2-5 % with price response; under a one-price system the gain is provably zero."
---

# Bidding in sequential Nordic spot and balancing markets (Boomsma, Juul & Fleten, 2014)

_The PDF is the **author manuscript** (36 pages, own numbering, figures and tables at the end); page numbers below are manuscript pages, not EJOR pages. Journal volume/pages (EJOR 238(3), 797–809) are from memory and **unverified**. Inbox key `boomsma2014bidding` has no DOI in the PDF._

## Research question / purpose
For a producer trading in the Nordic **day-ahead spot market** and the **hour-ahead balancing (regulating power) market**, (i) can higher risk exposure in the balancing market (risk of not being dispatched) explain observed hesitation to bid there? (ii) is it profitable to hold back spot capacity to offer up-regulation, or to sell more in spot to offer down-regulation? (iii) what is the gain from coordinated vs separate bidding, and can it be bounded without solving the coordination problem? (pp. 2–3).

## Setting
- **System:** generic participant; case: Norwegian hydropower plant with two serially connected reservoirs, both with inflow, real data for storage/discharge capacities, efficiency and inflow (p. 23).
- **Markets:** Elspot day-ahead (hourly price-volume curves, piecewise-linear in Nordic rules) and the common Nordic balancing market (up/down regulation bids hour-ahead, price = last activated bid) (pp. 5–6). Imbalance settlement under **one-price** or **two-price** systems (p. 6, 12). No reserve **capacity** market; balancing here is energy activation.
- **Horizon and resolution:** one operating day, 24 hourly intervals; **26 stages**: stage 1 spot bidding, stages 2–25 balancing bids, stages 3–26 operation and imbalance settlement (p. 7).

## Method
- **Model type:** multistage stochastic MILP/LP (deterministic equivalent on a scenario tree, nodal formulation) (pp. 7–14); convex QP when price response is included (p. 14).
- **Bidding:** fixed price points (10 per hour, equiprobable spot-price intervals), volume decisions; supply/demand curves monotone; step-wise or piecewise-linear acceptance; price-taker so acceptance is known a priori (pp. 8–9, 22). Up-regulation accepted only if bid price ≤ balancing price **and** system up-regulated (balancing price > spot) → "risk of not being dispatched" (p. 11). Min spot bid 0.1 MWh; balancing bids 10–50 MWh (p. 22).
- **Imbalances:** z⁻ − z⁺ = spot + balancing commitments − production (eq. 9, p. 12); one-price: settled at balancing price; two-price: max/min of spot and balancing price (p. 12).
- **Price response (Sect. 4.5, p. 14):** linear inverse demand in both markets; empirical parameters (0.0027, 0.0057, 0.15 €/MWh per MWh) weak, so ×10 in results (p. 22).
- **Hydro operation (Sect. 4.6.1, p. 15):** serial reservoirs, storage balance, bounds, constant efficiency, **terminal value = constant water values** (piecewise-linear concave water-value function, 45 €/MWh at 50 % filling); deterministic inflow (p. 15, 23). Initial storage 50 %, minimum 10 % (p. 23).
- **How uncertainty is represented:** spot price SARIMA(2,1,0)×(1,0,1)₂₄; balancing price ARMAX(1,0,0) with spot price as exogenous regressor (captures cross-correlation); de-trended/de-seasonalised with hourly, daily, monthly dummies, hourly differencing (p. 16–17). Fit: R² 0.79 (spot), 0.50 (balancing); RMSE 4.12 and 17.86 €/MWh (p. 17). Data 2009–2010 from Energinet.dk (p. 17).
- **Scenario generation:** stage-wise alternating sampling and **k-medoids** clustering (Euclidean): 500 spot paths → 10; then for each hour 500 balancing values per node → 10, then keep largest clusters with factor l = 1.18 so the tree has 500 scenarios (pp. 18–19). Moments preserved reasonably (Table 6, p. 34): spot mean 71.99→72.27, sd 24.14→21.22, autocorrelation 0.888→0.877; balancing autocorrelation 0.430→0.641; cross-correlation 0.721→0.824.
- **Bounds (Sect. 6, pp. 20–22):** Prop. 1: spot-only and sequential (separate) bidding give lower bounds LB1 ≤ LB2 ≤ coordinated; Prop. 2: with fixed prices, spot-only bidding under a **one-price** system is an upper bound; Corollary 1: under one-price, coordinated = spot-only (no gain from balancing market).
- **Solver:** GAMS; <1 minute on a laptop (p. 23).

## Data / case
Nordic spot and balancing prices 2009–2010 (Energinet.dk); one weekday mid-month in each month of 2010; Norwegian two-reservoir hydro plant (pp. 22–23).

## Key findings
- (p. 22, Corollary 1; p. 25) Under a **one-price** imbalance system, a price-taker gains nothing from the balancing market: the market design gives no incentive to relieve imbalances.
- (Table 7, p. 35; pp. 24–25) Under **two-price**, price-taker: **gain from coordinated bidding 8.03 % (Dec) to 24.73 % (Mar)** of daily profit, 9–20 % in most months; UB−LB1 gap 9.6–30.8 %. Up-regulation volumes small (0.5–9 %), down-regulation large (29–37 %), because average balancing prices were below spot prices in 2010.
- (p. 23–24) Raising balancing prices by 5/10/20 % (Dec 2010) shifts volumes to up-regulation (19/66/85 %); gains 4.23/4.75/9.81 %. Gain grows with the **difference** between average balancing and spot prices, not with the level (p. 25).
- (p. 24) "Value of waiting": deferring decisions to an hour ahead allows adapting to prices; partly offset by the risk of not being dispatched (risk-adjusted up-regulation price 32.40 vs spot 72.27 €/MWh in Dec 2010). The cost of non-dispatch risk is "largely offset by the value of waiting"; hesitation in practice may stem from transaction/learning costs.
- (p. 25) Coordination changes spot bidding curves: large spot volumes in some hours to enable down-regulation later (Fig. 6).
- (p. 25) UB−LB1 is a good indicator of the coordination gain; with only 50 % of capacity available for balancing, gain 5.89 % vs bounds 9.60/8.41 % (p. 26).
- (Table 8, p. 36; p. 26) With (amplified) price response, coordination gain falls to **1.99–5.31 %**; still zero under one-price.
- (p. 25, 27) Coordinated bidding likely to become more important as renewables raise the value of balancing.

## Strengths
- Explicit sequential information structure (day-ahead, then hour-by-hour) in a true multistage model.
- Analytical bounds tell practitioners when coordination is worthwhile without solving the full model.
- Scenario generation that tracks auto- and cross-correlation, with reported moment preservation.

## Weaknesses / limitations
- One-day horizon; hydro represented with constant water values (no long-term link); deterministic inflow.
- Balancing **energy** only; no reserve **capacity** products (FCR/aFRR/mFRR capacity), which are now central.
- 2010 data, pre-15-minute settlement and pre-single-price reform (the Nordic imbalance pricing has since changed; our remark, not in paper).
- Risk-neutral; simple price models (no jumps/regimes).
- Manuscript version: table numbering in the text (Tables 1–4) differs from the appended tables (Tables 5–8).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review 5.4: value of coordinating DA and balancing | Coordination gain 8–25 % (price-taker), 2–5 % with price response | Tables 7–8, pp. 35–36; pp. 24–26 |
| Lit. review 5.4: when coordination does not pay | Zero gain under one-price imbalance settlement | Cor. 1, p. 22 |
| Lit. review 5.4: gain depends on price spread between markets | Gains grow with |balancing − spot| average difference | p. 25 |
| Background 2.4: Nordic balancing market mechanics | Up/down regulation, marginal pricing, one- vs two-price settlement | pp. 5–6 |
| Method: multistage information structure | 26-stage tree; non-anticipativity per market clearing | pp. 7–8, 11–12 |
| Method: scenario generation with clustering | Stage-wise sampling + k-medoids; moment preservation table | pp. 18–19; Table 6 p. 34 |
| Method: price models | SARIMA for spot, ARMAX for balancing with spot regressor | pp. 16–17, Table 5 p. 34 |

## Useful quotes (with page numbers)
> "our model results show that the cost of this additional risk is largely offset by the value of waiting." (p. 24)

## Follow-up references to check (backward snowballing)
- [8] Fleten & Kristoffersen (2007), EJOR: stochastic programming for bidding of a Nordic hydro producer.
- [7] Faria & Fleten (2011), CMS: day-ahead bidding considering Elbas.
- [35] coordinated spot/balancing bidding with smooth curves (cited as only prior example).
- [37] bidding in three sequential short-term markets.
- [24] Klæboe, Eriksrud & Fleten (2013), Energy Systems: balancing price forecasting benchmarks.
- [28] Lu, Chow & Desrochers (2004), IEEE TPWRS: pumped-storage bidding strategies.

