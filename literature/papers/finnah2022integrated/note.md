---
bibkey: finnah2022integrated
bibkey_provisional: true
title: "Integrated day-ahead and intraday self-schedule bidding for energy storage systems using approximate dynamic programming"
authors: "Benedikt Finnah, Jochen Gönsch, Florian Ziel"
year: 2022
venue: "European Journal of Operational Research 301, 726-746"
peer_reviewed: true
methods: [adp-reinforcement-learning, uncertainty-modelling, deterministic-lp-milp]
review_sections: [market-participation, modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/04_Kraftmarkeder_priser_og_energisystem/104_Finnah_2022_Integrated_day_ahead_and_intraday_self_schedule_bidding_for_energy_storage_systems_using_a.pdf
takeaway: "A 10 MW / 100 MWh pumped-hydro storage trading self-schedule bids in the German hourly DA and quarter-hourly ID auctions over 30 days, solved by backwards ADP with an 842-dimensional price-history state: integrated DA+ID bidding beats sequential bidding by 8 pp and DA-only earns 40% of integrated; ADDP (SDDP-type with clustered lattice) reaches only 83% of a 7-day expectation model."
---

# PHS in German day-ahead and intraday auctions with backwards ADP (Finnah, Gönsch and Ziel, 2022)

_**Version and page mapping:** published open-access EJOR version (CC BY). Journal page = PDF page + 725 (journal pp. 726-746 = PDF pp. 1-21). Not to be confused with `finnah2021` (Finnah and Gönsch 2021, IJPE, wind + battery + hydrogen), which is a different paper. Seifert et al. (2025) cite this paper as reference [11]._

## Research question / purpose
- How should the owner of a fast-ramping energy storage, concretely a **pumped hydro storage (PHS)**, place self-schedule bids in both German auction markets (hourly day-ahead, quarter-hourly intraday auction), anticipating the second market when bidding in the first, when the price forecast is high-dimensional (p. 726)?
- Contributions (p. 728): (1) dynamic program whose state contains all Markovian features of a high-dimensional price forecast (several hundred dimensions), solved by backwards ADP (BADP); (2) comparison with approximate dual dynamic programming (ADDP, Löhndorf et al. 2013) and a receding-horizon expectation model; (3) evidence that integrated trading beats sequential trading.

## Setting
- **System:** generic storage, numerical study a PHS with capacity 100 MWh, pump and turbine working range 5-10 MW each, efficiency 0.9 each way, start-up cost 15 EUR per start, ramping time 2 min, grid fees 5 EUR/MWh on pumped energy (p. 735). No inflow, no head effects.
- **Markets:** German EPEX day-ahead auction (60-min products, bids until noon, results ~40 min later) and intraday auction (15-min products, closes 15:00) (pp. 726-727). Balancing prices are linear in ID prices and penalise deviations caused by ramping (Assumption 4, p. 727; eqs. 21-22, p. 731). Balancing/reserve markets, continuous ID, derivatives and OTC excluded (Assumption 1, p. 727; discussion pp. 739-740).
- **Horizon and resolution:** T = 30 days, two decision stages per day (DA then ID), hourly DA and quarter-hourly ID decisions (pp. 729, 735).

## Method
- **Model type:** MILP stage problems (binary pump/turbine on-off, minimum power, no simultaneous pump and turbine, linear ramping, start-up costs; eqs. 9-18, 23-24, pp. 730-731) inside a dynamic program with alternating DA and ID stages (eqs. 27-30, p. 731).
- **How uncertainty is represented:** lasso-estimated linear autoregressive price models (Ziel 2016): each of the 24 DA prices depends on the previous 168 DA prices plus weekday dummies; each of the 96 ID prices depends on last week's DA and ID prices plus same-day DA prices; Gaussian noise with full correlation matrices (eqs. 1-5, pp. 729-730; Assumption 6, p. 728). The DA-stage state therefore has **842 continuous variables** (storage level, last trade, 840 lagged prices) (p. 730).
- **Solution method:** a policy model merges the DA and ID stages into one expectation-based stage per day (Fig. 3, eqs. 31-35, pp. 731-732); the ID decision is then re-optimised after DA prices are known (p. 732). BADP fills a lookup table backwards over a discretised storage level (11 points) and last trade (3 points) and N = 50 sampled price histories; the next-stage expected value is a **regression-weighted combination of sample paths** instead of transition probabilities (Algorithm 1, p. 733), with a box-constrained, influence-weighted variant BADP-w (eqs. 36-39, Algorithm 2, p. 734).
- **Benchmarks (pp. 736-737):** ADDP (SDDP variant with Markovian lattice from k-means on 1,000 sampled histories, N = 50 clusters, counted transitions, K = 10 iterations); EM-7 (7-day expectation model, receding horizon); perfect foresight upper bound.
- **Key modelling choices and assumptions:** self-schedule (price-taking) bids, justified in Appendix A (pp. 740-742); expectation model within each day shown to match a two-stage SAA (Appendix B, pp. 742-743); start- and end-of-horizon effects ignored because the storage cycles within half a day (p. 735).

## Data / case
- EPEX Spot 2018-2020; four seasonal settings, each with 365 training days and 30 test days (Table 1, p. 735). Forecast MAE/RMSE per season in Table 2 (p. 736): DA MAE 5.07-7.26 EUR/MWh, ID MAE 3.22-4.90 EUR/MWh. 20 repetitions of the whole estimate-solve-evaluate chain to get confidence bands (p. 735). Matlab, intlinprog, Ryzen 5 PC (p. 736).

## Key findings
- (p. 737, Table 3) Relative profit vs EM-7 = 100%: BADP 99.70%, **BADP-w 101.44%**, BADP-w re-optimised 101.47%, **ADDP 82.80%** (and the slowest, 5,172 s learning), perfect foresight 185.70%. Least-squares Monte Carlo variant 94.31% (p. 737).
- (p. 737) The 1.44 pp gain in contribution margin could raise IRR of a storage project substantially, because storage IRRs are low (0.2%-9.1% cited).
- (pp. 737-738, Fig. 6) Operation shows strong daily and weekly cycles: charged at weekends and after midnight, discharged on weekdays during the day.
- (p. 738, Figs. 7-8) The dynamic program needs at least seven days of price history in the state to beat EM-7; a simple expectation model with a good forecast is better than an ADP with a poor one (pp. 738-740).
- (p. 740, Table 4) Relative to integrated DA+ID (100%): DA only **39.75%**, ID only **97.51%**, DA+ID sequential **91.98%**, integrated without expected-spread arbitrage 99.88%. Integrated beats sequential by about 8 pp and ID-only by 2.5 pp; sequential is worse than ID-only because DA commitments give a bad starting point (p. 739). Almost no DA-ID arbitrage, suggesting efficient auction markets (p. 739).
- (p. 742, Appendix A) With realistic, highly correlated DA forecast errors (up to 0.98 between consecutive hours), price-volume bids give no significant gain over self-schedule bids; with uncorrelated noise they would win by over 130 pp. Authors note this may differ for hydropower with large reservoirs and inflow (p. 727).
- (p. 740) Future work: infinite-horizon formulation, ramping-time effects, and a small buffer battery for PHS to enable instant ramping.

## Strengths
- One of the few stochastic bidding papers that explicitly models a PHS with binary pump/turbine modes, minimum power, ramping and start-up costs in two sequential markets.
- Careful benchmarking with confidence bands over 20 estimation runs; shows an SDDP-type method (ADDP with clustered lattice) can lose badly to simple baselines when the price process is high-dimensional and the lattice is coarse.
- Quantifies integrated vs sequential vs single-market trading.

## Weaknesses / limitations
- Small, short-duration PHS (10 MW / 100 MWh, 10 h) with no inflow and no head effects; 30-day horizon with no terminal water value.
- No reserve or balancing-capacity markets (excluded because German rules changed 2018-2020, p. 740).
- Risk-neutral; ADDP implementation uses only K = 10 iterations and no cut selection, so the ADDP comparison may understate SDDP-type methods (authors acknowledge, p. 737).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review: PHS in sequential DA + ID markets | PHS 10 MW/100 MWh, integrated vs sequential vs single-market | pp. 739-740, Sec. 6.5, Table 4 |
| Lit review: value of coordination | Integrated +8 pp over sequential; DA-only 39.75% | p. 739, Table 4 p. 740 |
| Model: PHS technical constraints (MILP) | Min power, mode exclusivity, ramping, start-up cost, grid fee | pp. 730-731, eqs. (9)-(18), (20)-(24) |
| Method: benchmark design | EM-7 receding-horizon expectation model, perfect foresight bound, 20-run confidence bands | pp. 735-737, Sec. 6.1-6.2 |
| Method: limits of clustered Markov lattices | ADDP with 50 k-means clusters reaches 82.8% of EM-7 | pp. 736-737, Table 3 |
| Method: self-schedule vs price-volume bids | Price-volume bids give no gain with correlated forecast errors | p. 727 (Assumption 2); App. A pp. 740-742 |
| Background: German DA and ID auction rules | Gate closures, 60-min vs 15-min products | pp. 726-727, Sec. 1.1 |
| Lit review: survey of storage trading methods | Löhndorf 2013, Boomsma 2014, Brijs 2019 (perfect foresight overestimates coordination value), Khatami 2020 (CAES) | pp. 728-729, Sec. 2 |

## Useful quotes (with page numbers)
> "Thus, if we are not willing to handle the large state variable in the dynamic program, the much simpler benchmark approach would be the better choice." (p. 738)

## Follow-up references to check (backward snowballing)
- Boomsma, Juul and Fleten (2014), EJOR: Nordic DA + balancing bidding for a hydro producer (not in our library).
- Brijs, Geth, De Jonghe and Belmans (2019): storage in both German auctions + balancing under perfect foresight.
- Wozabal and Rameseder (2020), EJOR: VPP bidding in Spanish DA + ID with ADDP.
- Khatami, Oikonomou and Parvania (2020): CAES in DA and real-time markets with ramps.
- Viehmann (2017): overview of German short-term markets.
- Ziel (2016): high-dimensional autoregressive DA price model.

