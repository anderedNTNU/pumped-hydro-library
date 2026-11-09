---
bibkey: seifert2025
title: "Coordinated Trading Strategies for Battery Storage in Reserve and Spot Markets"
authors: "Paul E. Seifert, Emil Kraft, Steffen J. Bakker, Stein-Erik Fleten"
year: 2025
venue: "arXiv preprint arXiv:2406.08390v4 (20 Feb 2025)"
peer_reviewed: false
methods: [sddp-markov-chain, uncertainty-modelling]
review_sections: [market-participation, modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/103_Seifert_2024_Coordinated_Trading_Strategies_for_Battery_Storage_in_Reserve_and_Spot_Markets.pdf
takeaway: "NTNU/KIT Markov-chain SDDP (SDDP.jl) bidding model for a 10 MW/10 MWh battery coordinating FCR capacity, day-ahead and intraday in Germany 2022 at 4-hour resolution: FCR-only dominates (no coordination value at real prices), but with FCR prices halved coordination adds up to 12.5%; model resolution drives the result."
---

# Coordinated battery trading in FCR, day-ahead and intraday with Markov-chain SDDP (Seifert et al., 2025)

_**Version and page mapping:** arXiv v4 (20 Feb 2025), 28 PDF pages. PDF p. 1 is an unnumbered "Highlights" page; the manuscript's own page numbers start at 1 on PDF p. 2, so **printed page = PDF page − 1**. Page numbers below are printed manuscript pages. Inbox file name says 2024 (v1 was June 2024); the bib entry `seifert2025` points to v4, which is this file. Not (yet) peer reviewed as far as this PDF shows._

## Research question / purpose
- "Is the use of SDDP adequate to depict the storage operator's problem for coordinated bidding in three markets under given computational and technical limitations while following the German market schedule?" (p. 2).
- Three contributions (p. 5): (1) a multistage stochastic bidding model adding a balancing (reserve capacity) market to DA and ID, solved with SDDP; (2) econometric price models that separate fundamentals from stochastic residuals, calibrated on the 2022 crisis year; (3) evaluation of battery economics with multiple revenue streams and the value of coordination.

## Setting
- **System:** grid battery, 10 MW / 10 MWh (1-hour), Germany (p. 13). No efficiency losses (p. 12). Price-taker (discussed p. 20).
- **Markets:** FCR (symmetric capacity product, 4-hour blocks, pay-as-cleared, capacity payment only, activation energy ignored), DA auction, ID market modelled as a DA-dependent spread (pp. 7, 13).
- **Horizon and resolution:** three-day planning horizon (p. 4); each day split into six 4-hour blocks f = 1..6, a stage is t = (d, f), so 18 stages (pp. 7, 14). FCR bids at (d−1, f = 3), cleared at (d−1, f = 4); DA bid at (d−1, f = 4), clearing deferred to (d, f = 1) for Markov-chain bookkeeping reasons (footnote 2, p. 7); ID bid one block ahead (p. 7). No FCR/DA bidding on the last day, to avoid end-of-horizon distortions (p. 7).

## Method
- **Model type:** multistage stochastic LP with bid curves on discrete price levels (Heaviside market clearing, eq. 2; monotone bid curves, eq. 3, following Fleten and Pettersen 2005, Löhndorf et al. 2013, Wozabal and Rameseder 2020) (p. 11). Objective: FCR revenue at FCR clearing, DA revenue at DA clearing, ID revenue every block, minus slack penalty (eq. 1, p. 11).
- **State variables:** SoC, bid quantities per market/price level/block, cached committed quantities for FCR because clearing and delivery are offset in time (eqs. 8-9, p. 12); 73 state variables in total (p. 13).
- **Storage constraints:** SoC balance (eq. 10a); SoC must leave room for symmetric FCR reservation in both directions, FCR ≤ SoC ≤ Q − FCR (eq. 10b, p. 12); start and end SoC fixed to Q_INIT (eq. 10c), slack variables with penalty 3,000 EUR/MWh to keep SDDP feasible (pp. 12, 15; Appendix A.3 pp. 25-26). FCR bids limited to half the rated power as a conservative assumption (p. 12). ID bids limited by storage room left after DA and FCR commitments (eqs. 4-7, pp. 10-12; validity checked in Appendix A.4, p. 26).
- **How uncertainty is represented:** a three-dimensional Markov chain over DA, ID and FCR prices (Fig. 4, p. 9).
  - DA and FCR prices regressed by OLS on residual load, TTF gas, CO2 price (and residual-load quantiles, time-of-day dummies for FCR); stochastic residuals kept (pp. 7-9). DA model adj. R² 84.8% (2022) and 84.9% (2021), strong autocorrelation (Durbin-Watson 0.154) (p. 8). FCR R² 36% (2022), over 53% (2021), no significant autocorrelation; FCR-DA price correlation −0.024, so FCR treated as independent of DA (pp. 8-9).
  - Multivariate k-means on residual vectors of **three consecutive days** (121 historic combinations from 363 days); elbow plots give **5 DA clusters and 3 FCR clusters** (p. 9). ID price = DA cluster + cluster-dependent spread with three levels: mean, 15th and 85th percentile of the ID deviation distribution (p. 10). ID deviations are non-normal with long tails (p. 9).
  - Transition probabilities from counted cluster transitions in history; forecasted fundamentals added back to get the price levels for the trading period (p. 10).
- **Solution method:** SDDP.jl (Dowson and Kapelevich 2021) in Julia; 1,081 price-level combinations, about 4 billion price paths implied; about 45 min and 18,000 iterations on an Apple M1 Pro; stopping rule if the upper bound improves less than 0.1 over 3,000 iterations after 5,000 initial iterations (p. 13).
- **Key modelling choices and assumptions:** 4-hour resolution as lowest common denominator of the three markets (p. 7); prices averaged within blocks; no degradation; FCR activation energy neglected (p. 13; limitation p. 20).

## Data / case
- German market data 2022 (EPEX Spot, regelleistung.net), energy-crisis year with high and volatile prices (p. 13; Figs. A.16-A.17, pp. 25-26). Policy simulated on fundamentals for 05.07.2022-08.07.2022 (p. 14); first day contains only ID actions and is omitted from result tables (p. 13).

## Key findings
- (p. 14, Fig. 6) Tight optimality gap after about 6,000 iterations; no storage violations from 12,000 iterations on; mean simulated revenue of three days converges to an upper bound of **10,415 EUR**.
- (p. 15, Table 2) Two-day revenue, 10,000 in-sample simulations: **FCR only 7,384.1 EUR** (best), ID only 2,705.9, DA only 2,986.8, FCR+DA 7,168.5, ID+FCR 6,467.1, ID+DA 2,958.6, all three 7,008.8. FCR dominates; combinations do not beat FCR-only (the model finds near-optimal mixes and never reaches the corner solution).
- (pp. 15-16) Adding ID mostly fails to add value at 4-hour resolution, but ID participation reduces SoC violations and penalties. ID widens both tails of the revenue distribution (Fig. 9, p. 16).
- (p. 17) About **39.6% (direction metric) / 39.5% (feasibility metric)** of combined DA+ID volume is inter-market arbitrage.
- (p. 17, Table 3) With FCR prices **halved**, multi-market policies beat single-market ones: FCR+DA 4,220.7 EUR vs FCR-only 3,689.9 EUR, i.e. **+530.8 EUR or 12.5%**; all three markets +5.7% over the best single market.
- (p. 19) Resolution dilemma: 4-hour blocks underestimate spot arbitrage, while capacity reservation is cycling-independent; power/energy ratio would shift the balance (a 10 MW/20 MWh battery would earn the same FCR revenue but more spot revenue); suggested as future sensitivity.
- (p. 19) In line with Kongelf et al. (2019), no significant coordination value in expectation; contrary to Löhndorf and Wozabal, no profit from ID volatility. FCR market (about 600 MW in Germany) will saturate, so revenue stacking becomes necessary.
- (p. 19) SDDP samples only a tiny share of Markov price paths (at most 5,107,075, 0.000124%); about 5% gap to the FCR-only solution accepted.
- (p. 20) Slack variables can create large negative simulated revenues; fixed imbalance penalty may be too conservative.

## Strengths
- Closest methodological sibling to our work: **Markov-chain SDDP (SDDP.jl), Markov states from k-means clustering of multi-day residual vectors, counted transition probabilities**, with a reserve-capacity market alongside DA. Same institution (NTNU IØT, Fleten).
- Explicit treatment of market timing (bid vs clearing vs delivery) inside SDDP stages, and of SoC headroom for symmetric reserve capacity.
- Honest discussion of resolution, SDDP sampling and slack-penalty limitations.

## Weaknesses / limitations
- 4-hour resolution and averaged prices make spot arbitrage look weak; headline result (FCR dominates) is resolution-dependent (p. 19).
- Three-day horizon with fixed start/end SoC: no water-value/end-of-horizon valuation; not transferable to seasonal storage as is.
- No efficiency losses, no degradation, no FCR activation energy; in-sample evaluation only (Tables 2-3 are "in-sample simulations").
- Coordination value only appears after an artificial 50% FCR price cut.
- Preprint; one simulated period in the tables.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method: Markov-chain SDDP for storage bidding (precedent) | SDDP.jl, Markov chain on DA/ID/FCR prices, 18 stages | pp. 5-13, Sec. 3-4 |
| Method: building Markov states by clustering | Multivariate k-means on 3-day residual vectors, elbow plots, 5 DA / 3 FCR clusters, counted transitions | p. 9-10, Sec. 3.3; App. A.1 |
| Method: price model = fundamentals + stochastic residual | OLS on residual load, TTF, CO2; R² values | pp. 7-9, Sec. 3.2 |
| Model: reserve headroom in storage | SoC bounds tightened by symmetric FCR reservation | p. 12, eq. (10b) |
| Model: handling bid/clearing/delivery offsets in SDDP stages | Caching committed quantities as state variables | p. 12, eqs. (8)-(9); footnote 2 p. 7 |
| Model: feasibility slacks in SDDP and penalty choice | 3,000 EUR/MWh penalty, tested 10k and 100k | p. 12; App. A.3 pp. 25-26 |
| Lit review: market participation, reserve vs energy | FCR-only dominates at 4 h resolution; coordination up to 12.5% with halved FCR prices | pp. 15-17, Tables 2-3 |
| Lit review: value of coordination is contested | Summary of Boomsma, Kongelf, Löhndorf and Wozabal, Heredia, Wozabal and Rameseder | pp. 3-4, 19 |
| Lit review: SDDP as de facto standard in hydro | Statement with refs (Pereira and Pinto, Rotting and Gjelsvik, Rougé and Tilmant) | p. 3 |
| Discussion: resolution and power/energy ratio | 4 h blocks underestimate spot revenue; 0.5C battery comparison | p. 19 |
| Discussion: SDDP sampling / near-optimal policies | Only 0.000124% of paths visited, ~5% gap | p. 19 |

## Useful quotes (with page numbers)
> "SDDP has evolved into the de-facto standard solution technique in complex hydropower reservoir management." (p. 3)

## Follow-up references to check (backward snowballing)
- Boomsma, Juul and Fleten (2014), bidding in sequential Nordic markets, EJOR 238 (not in our library).
- Kongelf et al. (2019), portfolio size and gains from coordinated bidding, Norwegian hydropower, Energy Systems 10 (not in our library).
- Löhndorf and Wozabal, value of coordination in multimarket bidding of grid storage (we have it as `lohndorf2023`).
- Finnah, Gönsch and Ziel (2022), PHS in German DA + ID auctions (filed as `finnah2022integrated`).
- Heredia, Cuadrado and Corchero (2018), wind + battery in spot and secondary reserve markets, Comput. Oper. Res. 96.
- Kraft, Russo, Keles and Bertsch (2022), stochastic optimisation of trading in sequential markets, EJOR.
- Klæboe, Eriksrud and Fleten (2015), benchmarking balancing-price forecasting models, Energy Systems 6.
- Ottesen, Tomasgard and Fleten (2018), multi-market bidding for flexibility aggregators, Energy 149.

