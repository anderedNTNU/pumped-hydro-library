---
bibkey: liu2025analytical
bibkey_provisional: true
title: "Analytical dispatch strategies for pumped storage hydro: A conditional dynamic programming approach to discontinuous multi-period optimization problems"
authors: "Jian Liu, Jianwen Zhang, Zaiwu Gong, Donald C. Wunsch II, Rui Bo"
year: 2025
venue: "Applied Energy, 383, 125255"
peer_reviewed: true
methods: [dynamic-programming]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Deterministic-price DP for a price-taking PHS (upper reservoir only) with non-zero minimum pump/turbine power: optimal policy is a set of SOC reference points (4 for PHS-only, 5 with wind); in a MISO two-week case raising minimum load from 0 to 100 % of 2100 MW cuts arbitrage profit by only ~0.2-0.4 %."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/Liu2025.pdf"
---

# Analytical DP dispatch of PHS with minimum operating levels (Liu et al., 2025)

PDF note: the inbox PDF has a one-page Scholars' Mine (Missouri S&T) cover sheet; the journal article starts on PDF page 2 (= article p. 1). Page numbers below are the article's printed page numbers. Article pp. 1–23 are the main text; appendices (proofs, Appendix B case details, Appendix C extra figures) and references follow.

## Research question / purpose
Analytical studies of storage arbitrage by DP usually set the minimum charging/discharging power to zero so that reward and value functions stay continuous. PHS units cannot run at near-zero flow (mechanical limits, wear, low efficiency at part load, p. 2). The paper asks (p. 3): (1) how do non-zero minimum pumping/generating limits, which make the reward and value functions discontinuous, change dispatch strategy and profit; (2) how does that strategy differ from the zero-lower-bound one?

## Setting
- **System:** a single PHS with a finite upper reservoir and an **effectively unlimited lower reservoir** (lake/river, e.g. Ludington PSH, Michigan) (p. 6). Scenario 2 adds a co-owned wind farm (p. 3).
- **Markets:** day-ahead energy arbitrage only, price-taker; no reserves (p. 6). Capacity markets/reserves named as future work (pp. 22–23).
- **Horizon and resolution:** synthetic 3-period example (Sec. 5); real case: 336 hourly periods (two weeks), MISO prices for 1–14 Oct, 6–19 Nov and 4–17 Dec 2023 (pp. 20–21).

## Method
- **Model type:** finite-horizon "Markov" DP with state S(t) = (E_t, P_t) (SOC and price) and binary unit-commitment variables U^p, U^g (no simultaneous pumping and generating), minimum and maximum pump/turbine energy per period, SOC bounds, pumping/generating/transmission efficiencies and self-discharge (eqs. 1–4, pp. 6–7).
- **How uncertainty is represented:** effectively **none**: "we assume that all forecasted electricity prices are known in advance", which makes the control problem deterministic (p. 7). Wind is also taken as known per period in the examples.
- **Solution method:** introduce auxiliary decision variables y_t that shift the discontinuous action set (−Q̄g…−Q_g, 0, Q_p…Q̄p) into a continuous range, solve the Bellman recursion on the auxiliary problem, map back ("conditional DP", pp. 7–8; Propositions 1–4). Result: threshold (reference-point) policy on SOC.
- **Key modelling choices:** linear reward (price × energy minus constant operating cost c), constant efficiencies (no head effects), **zero terminal value V_{T+1} = 0** (p. 7, p. 21), "slow storage" (cannot be filled/emptied in one period) as the general case (p. 6).

## Data / case
Real case (p. 21): E_max = 22 000 MWh, E_min = 2000 MWh, Q̄p = Q̄g = 2100 MW (≈9.5 h to fill/empty, approximating Ludington), c = 1 $/MWh, pump and turbine efficiency 0.8 each, no self-discharge, transmission efficiency 1, initial SOC 2000 MWh. Minimum power varied at 0 %, 30 %, 50 %, 80 %, 100 % of 2100 MW.

## Key findings
- (pp. 3, 22) PHS-only: four SOC reference points split the SOC range into five regions: buy to the first reference point, pump the minimum amount, idle, generate the minimum amount, sell down to the fourth reference point. With wind: five reference points, six regions.
- (p. 20) With a linear reward, merchants usually charge at either maximum power or the remaining free storage, and discharge at either maximum power or remaining energy; minimum-load limits only bite when free storage or stored energy is below the minimum.
- (p. 21, Table 1) Profit for PHS-only falls only slightly as minimum load rises, e.g. about 3.975 M$ (0 %) to 3.966 M$ (100 %) in the first price set, a reduction of roughly 0.2 % (row alignment in the extracted table is slightly garbled; values from the three periods are 3.97 M, 1.38 M and 1.16 M$). Number of full cycles also falls (Table 2), except at 100 % where all actions are full charge/discharge.
- (p. 22, Table 3) Same pattern with wind: 15.341 M$ → 15.331 M$.
- (p. 22) Zero-lower-bound models are a special case of theirs.

## Strengths
- Gives clear policy structure (threshold rules) and intuition for storage arbitrage with minimum operating levels.
- Explicitly motivates why PHS differs from batteries in minimum-load behaviour (p. 2).

## Weaknesses / limitations
- Deterministic prices (perfect foresight), so not comparable with stochastic water-value methods; "expected" profit is nominal.
- Zero end-of-horizon value of stored water over two weeks, which forces the reservoir toward empty at the end; unlimited lower reservoir; no head effects; no reserves; no start-up costs.
- The authors describe the profit effect of minimum limits as significant, but their own Tables 1 and 3 show effects well below 1 %.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model limitations: minimum operating levels omitted (06_mathematical_model) | Quantified effect of minimum pump/turbine power 0–100 % of rated on two-week arbitrage profit: ~0.2-0.4 % | p. 21 Table 1, p. 22 Table 3 |
| Background / PHS technology: why PHS has minimum flow limits | Mechanical limits, wear, low part-load efficiency | p. 2 |
| Literature review: modelling PHS plants (DP, perfect foresight) | Example of deterministic DP arbitrage with zero terminal value, unlimited lower reservoir | pp. 6–7, Sec. 3 |
| Literature review: comparison | Short review of PHS dispatch papers using DP/SDP/SDDP (e.g. Alvarez 2019 SDDP; Karhinen & Huuki 2019 DP; Toufani 2022 SDP) | p. 5, Sec. 2.2 |

## Useful quotes (with page numbers)
> "we assume that all forecasted electricity prices are known in advance" (p. 7)

## Follow-up references to check (backward snowballing)
- [40] Karhinen & Huuki (2019): PHS operation at different wind penetration levels using DP.
- [61] Toufani et al. (2022): converting a conventional cascade to pumped storage, SDP.
- [60] Alvarez et al. (2019): long-term PHS dispatch with SDDP.
- [51] Topalović et al. (2024): PHS vs. lithium batteries for price arbitrage.
- [64] Baldick et al. (2023): basic PSH scheduling model, mutual exclusivity and SOC limits.

