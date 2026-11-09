---
bibkey: hjelmeland2019phd
title: "Medium-Term Hydropower Scheduling: In a Multi-Market Setting"
authors: "Martin N. Hjelmeland"
year: 2019
venue: "PhD thesis, Department of Electric Power Engineering, NTNU (Doctoral theses at NTNU 2019:130)"
peer_reviewed: false
methods: [sddp-markov-chain, sddp-time-series, hydro-production-function, uncertainty-modelling, benders-decomposition, heuristics-simulation]
review_sections: [market-participation, electricity-markets, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "NTNU PhD (7 papers) on Nordic medium-term hydro scheduling with day-ahead + reserve capacity sales: convex SDDP (Markov-chain price, VAR1 inflow) overestimates reserve-capacity income by ~30% (up to ~40%) vs a nonconvex simulator; SDDiP with strengthened Benders cuts handles min-generation, nonconcave generation function and variable head at high computational cost."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/Innlimte_referanser_2026-10-29/hjelmeland2019phd.pdf
---

# Medium-term hydropower scheduling in a multi-market setting (Hjelmeland, 2019)

Article-based PhD (NTNU 2019:130), supervisors Korpås, Helseth, Doorman; part of SINTEF project "Integrating Balancing Markets in Hydropower Scheduling Methods" (p. iii). 162 PDF pages: a 69-page synthesis (ch. 1–4) plus the seven papers in Appendix A.
**Page convention:** printed page = PDF page − 17 throughout (PDF 18 = p. 1; the appended papers keep the thesis pagination, e.g. Article I = pp. 81–86 = PDF 98–103). Read in full: abstract, ch. 1–4; Articles I and II skimmed for case details. Articles VI and VII have their own notes: `hjelmeland2019tste` and `hjelmeland2019energies`.

## Research question / purpose
Analyse and develop methods for medium-term hydropower scheduling (MTHS) for a Nordic price-taking producer that sells energy day-ahead **and** reserve capacity (rotating reserves), building on SDDP (p. 4). Two strands: (i) how well the existing convex SDDP model (SINTEF ProdRisk prototype) performs when reserve capacity is added (Articles I–II); (ii) nonconvex MTHS via SDDiP, strengthened Benders cuts, nonconcave generation functions and variable head (Articles V–VII). Side studies on an inertia market (III) and wind providing reserves (IV).

## Setting
- **System:** conventional (no pumping) Norwegian reservoir hydropower. Main test system: three reservoirs (Reservoir 3 has 2 % of storage but 25 % of inflow; Reservoirs 2 and 3 feed the same station) (p. 47, Fig. 3.1). Article I: a system "under construction in south-west of Norway", stations of 13.8 MW and 400 MW (p. 84). Article IV: a constructed Nordic-like system with wind.
- **Markets:** Elspot day-ahead energy; reserve capacity (primary FCR-N weekly/daily market in Articles I/II/VII; up/down secondary reserves in IV); inertia market in III. Market background (Elspot, Elbas, FCR-N/D, FRR-A, FRR-M, RKOM, RPO) in ch. 2 (pp. 9–23).
- **Horizon and resolution:** MTHS weekly stages, multi-year horizon; Articles I/II use **21 time periods per weekly stage (three per day)**, chosen to match the weekly FCR-N market periods (p. 48).

## Method
- **Model type:** multistage stochastic LP (strategy model = SDDP) evaluated by a more detailed **simulator model** (MILP stagewise problems with minimum generation, binary start-up costs, binary hydraulic coupling, nonconcave generation function) using the SDDP cuts (pp. 48, Fig. 3.2). Later SDDiP (binary state expansion, copy constraints, Benders / Lagrangian / strengthened Benders / integer-optimality cuts) (pp. 34–42).
- **How uncertainty is represented:** inflow normalised and modelled as a **VAR(1)** process, Eq. (2.19)–(2.20) (p. 44); energy price as a **discrete Markov chain** with transition probabilities ρij(t), Eq. (2.21), built following Mo et al. 2001 (p. 44, Fig. 2.24). Correlation between inflow and price is only indirect (price series from an EMPS run that accounts for inflow, not in the noise term) (p. 45). Article I: 7 price nodes, 50 forward scenarios (p. 85). Article VII: inflow, energy price and reserve-capacity price via Downward et al.'s objective-uncertainty method (pp. 45, 59). Reserve prices from historical FCR data 2013–2014 (Articles I/II).
- **Solution method:** SDDP with Benders cuts; cut relaxation via dual simplex (Algorithm 2, p. 34–36); SDDiP; McCormick envelopes for bilinear price × generation (Article VI, p. 58).
- **Key modelling choices and assumptions:** risk-neutral price taker, exogenous prices (p. 27); end-of-horizon EFP from LTHS or zero with long horizon (p. 33, fn 5); generation function concave and discharge-only in LP MTHS, head-dependent nonconcave in VII (p. 54–55, 59); reserve-capacity constraint c_t ≤ c_max/(P_min + c_max)·p_t to limit reserves at low output (Eq. 3.1, p. 49).

## Data / case
Weekly inflow history (70 years in Article II, p. 90), day-ahead prices from EMPS, FCR-N prices from historical 2013–2014 data (pp. 84, 90). Generation-function data from online measurements at two Norwegian stations (Article V, p. 55). Market statistics for 2017 (Nord Pool 512 TWh; NO2 Elspot turnover ≈ 13 bn NOK) (p. 11).

## Key findings
- (p. 49, 67, 82) The LP SDDP strategy model **overestimates income from reserve capacity by ~30 %** (29.2 % in Article I) relative to the simulator, because without a firm minimum-generation limit it runs stations at very low output to sell reserves when energy prices are low (e.g. 10 MW output to sell 10 MW PFR although the technical minimum was 50 MW) (pp. 49, 84). Overall profit was only 0.93 % lower (pp. 82, 85).
- (p. 49) Adding the low-output reserve constraint (3.1) to the simulator widened the reserve-income gap to ~40 % (Article II; p. 88 abstract).
- (p. 49–50, Fig. 3.3) The LP model dispatches simultaneously from two reservoirs with different heads feeding one station, which is physically impossible; the simulator switches between them.
- (p. 50) Marginal cost of reserve capacity differs strongly by reservoir size / installed capacity: small reservoir + small station has high marginal cost during spring flood (running at max to avoid spill); large reservoir has strongly negative marginal cost (wants to store water for winter).
- (p. 50) Selling energy + reserve capacity raised overall simulated profit by **2.56 %** vs energy only, a theoretical upper bound given exogenous reserve prices and thin reserve-market liquidity.
- (p. 16–17) FCR-N prices in NO2 correlate with inflow: high in spring flood (flexible plants stop to save water, so rotating reserves are scarce). "This aspect illustrates a core issue of this dissertation; how to optimally allocate the resource between the markets."
- (p. 53–54, 66) With wind penetration > 20 % the cost of upward reserves rises sharply; wind can provide downward reserves cheaply.
- (p. 57, 67) A concave generation function gives ~2 % higher objective and, with a summer minimum-discharge constraint, **14.1 % higher expected generation** than the measured nonconcave function (Article V).
- (p. 58–60) SDDiP converges on nonconvex MTHS only with Lagrangian cuts (≈50 MILPs per cut vs 1 LP for Benders); strengthened Benders cuts give a much tighter bound at manageable cost, yet a ~36 % bound gap remained after 50 iterations with full price uncertainty (p. 60). Benders cuts gave higher water values and higher reservoir levels (more spill risk) (p. 60, Fig. 3.10).
- (p. 21–23, 68) Elspot dominates turnover: NO2 Elspot ≈ 1.46 bn NOK vs ~100 MNOK in primary + secondary reserves (2017) (p. 68); still, reserve revenues are expected to grow with European integration (p. 4, 23).
- (p. 62–63) Notes that Helseth et al. extended the Markov chain to include a weekly primary reserve market and found the problem becomes computationally very demanding as the chain dimension grows; this motivated other methods.

## Strengths
- Clear, honest benchmarking of the operational SDDP approach against a more detailed simulator using identical scenarios.
- Good compact overview of the Nordic market sequence and reserve products as of 2018 (Table 2.3, p. 22) and of the LTHS/MTHS/STHS hierarchy (pp. 23–28).
- Directly relevant methods (Markov-chain price, weekly stages with intra-week periods, water values from cuts).

## Weaknesses / limitations
- Conventional hydro only; no pumping.
- Market description dated (pre-15-min MTU, pre-Nordic aFRR capacity market, pre-mFRR EAM); RKOM and FRR-A specs are 2018 status.
- Reserve prices exogenous and historical; no activation energy; risk-neutral.
- Small number of case systems; SDDiP results not converged on the full problems.
- Some internal slips in the synthesis: conclusions credit the generation-function methods to "Article VI" (p. 66) and the McCormick price modelling to "Article V" (p. 59); both should be the other article.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Limitation: LP model overestimates reserve revenue | 29.2 % (Art. I), ~40 % (Art. II) overestimate; cause: no min-generation | pp. 48–49, 67; Art. I pp. 82, 84–85; Art. II p. 88 |
| Model: reserve capacity vs generation constraint | c_t ≤ c_max/(P_min+c_max)·p_t | p. 49, Eq. (3.1) |
| Model: intra-week resolution choice | 21 periods per weekly stage aligned with FCR-N periods | p. 48 |
| Theory: SDDP stagewise independence, Markov-chain price, VAR(1) inflow | Formal description | pp. 32–34, 42–45, Eq. (2.19)–(2.21) |
| Theory: hydropower scheduling hierarchy (LTHS/MTHS/STHS), water value definition | Concise overview | pp. 23–28, Fig. 2.14–2.15; definition p. xii |
| Theory: SDDP bounds (max problem: master gives upper bound, forward sim gives statistical lower bound) | Algorithm 1 | pp. 33–35 |
| Background 2.4: Nordic reserves FCR-N/D, FRR-A, FRR-M, RPO; market timeline | Products, activation times, gate closures (2018 status) | pp. 15–22, Table 2.3 |
| Background: reserve prices correlate with inflow/spring flood | FCR-N NO2 price patterns | pp. 16–17, Figs. 2.8–2.9 |
| Lit review market-participation: energy+reserves adds ~2.6 % profit | Upper-bound estimate | p. 50 |
| Lit review: production function convexification overstates generation | +2 % objective, +14.1 % generation with min discharge | p. 57 |
| Lit review / gap: reserve revenues small today but expected to grow | Turnover comparison NO2 2017 | pp. 22–23, 68 |

## Useful quotes (with page numbers)
> "A MTHS model based on SDDP will overestimate the hydropower system's opportunity to sell reserve capacity." (p. 67)

> "This aspect illustrates a core issue of this dissertation; how to optimally allocate the resource between the markets." (p. 17)

## Follow-up references to check (backward snowballing)
- [37] Helseth, Fodstad, Mo (2016), Optimal medium-term hydropower scheduling considering energy and reserve capacity markets, IEEE TSTE (= `helseth2016`, already in our library).
- [9] Helseth et al. (2017), Assessing hydropower operational profitability considering energy and reserve markets, IET RPG (= `helseth2017iet`, in our library) — states the importance of reserve markets when refurbishing plants (p. 63).
- [94] Helseth, Mo, Fodstad (2017), Water values in future power markets, PowerTech.
- [41] Abgottspon (2015), PhD ETH, multi-horizon modelling (cf. `abgottspon2016multihorizon`).
- [42] Aasgård et al. (2018), Hydropower bidding in a multi-market setting, Energy Systems.
- [80] Downward, Dowson, Baucke (2018/2020), SDDP with stagewise-dependent objective uncertainty.
- [78] Mo, Gjelsvik, Grundt, Kåresen (2001), price modelling with Markov chain (cf. `mo2001`).
- [46] Gjerden et al. (2015), Hydrothermal scheduling in Norway using SDDP; a large-scale case study (DOR figure).
- [87] Cerisola, Latorre, Ramos (2012), SDDP applied to nonconvex hydrothermal models.

