---
bibkey: abgottspon2015hydro
bibkey_provisional: true
title: "Hydro power planning: Multi-horizon modeling and its applications"
authors: "Hubert Abgottspon"
year: 2015
venue: "Doctoral thesis, ETH Zurich (Diss. ETH No. 22729), ISBN 978-3-906327-06-8"
peer_reviewed: false
methods: [sdp, sddp-markov-chain, multistage-scenario-trees, deterministic-lp-milp, risk-averse-cvar, heuristics-simulation, benders-decomposition]
review_sections: [modelling-phs-plants, market-participation, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "PhD thesis behind abgottspon2013/2014/2016: multi-horizon (daily/weekly interstage SDP/SDDP on storage reservoirs + hourly intrastage deterministic-equivalent MILP) for Swiss PHS self-scheduling with DA, secondary reserves, forwards and risk; also reviews SDP/SDDP, Markov-chain multi-cut SDDP and dualized SDDP for non-concave (reserve-induced) value functions."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/01_Produsentmodeller_og_tidsskalaer/AbgottsponThesis2015.pdf
---

# Multi-horizon modelling for hydro power planning, PhD thesis (Abgottspon, 2015)

DOI: 10.3929/ethz-a-010548986. Examiners: G. Andersson; co-examiners O. B. Fosso (NTNU) and G. Koeppel (p. ii). Industry partners EGL AG and BKW Energie AG (p. iii).
**Page convention:** printed thesis page = PDF page − 19 (PDF 20 = p. 1). All "p. X" below are printed pages. 181 PDF pages; read in full: summary, Ch. 1-2, 3 (SDP/SDDP), 4 (extended SDDP), 5 (risk), 6 (multi-horizon; all), 7 (non-concavity), 8 (delta hedging), 10 (closure), App. A; Ch. 9 (short-term bidding, agent-based SFC) skimmed.
**Research family:** chapters are built on `abgottspon2013stochastic` (Ch. 6.4.2), `abgottspon2014` (Ch. 6.3.2), `abgottspon2016multihorizon` (Ch. 6.2, 6.3.1), plus PMAPS 2012/2014, SEPOPE 2012, EEM 2013 papers (p. 3-4). Same results, not independent evidence.

## Research question / purpose
Provide a transparent, computationally efficient modelling framework for the **self-scheduling of a hydro GenCo** (price-taker, exogenous prices) with Swiss **pumped-storage** plants in liberalised markets, so that water values can include short-term (hourly) flexibility, ancillary services (secondary frequency control, SFC), risk and forward trading (p. 1-2). Main contribution: **multi-horizon modelling**; secondary: dualized SDDP with locally valid cuts and a measure of non-concavity, delta-hedging of SFC cash flows, short-term bidding tools (p. 2, p. v-vi).

## Setting
- **System:** two real Swiss PHS plants (App. A, p. 151-154):
  - **KWM (Kraftwerke Mattmark AG):** one seasonal reservoir (100 Mm³) + one balancing reservoir (0.1 Mm³, 1000× smaller, catches inflow); Francis turbines u1, u2 (37 MW each) and pumps p1, p2 (23 MW each) between them; Pelton turbines u3, u4 (92 MW each, SFC-prequalified, technical minimum ~10 %); full production 260 MW; glacier-fed, strongly seasonal inflows, optimisations preferably end in spring (p. 151-153).
  - **KWO (Kraftwerke Oberhasli AG):** "most complicated" Swiss plant; confidential BKW model with 10 reservoirs, 195 Mm³ (≈ a quarter of yearly inflow), 4 seasonal + 6 balancing; 12 turbines 1.125 GW, 8 pumps 424 MW; Francis pumps on/off only (one 60-100 % with frequency converter); MILP operating rules; three turbines deliver SFC (p. 153-154). Max 280 MW SFC (p. 12).
- **Markets:** hourly day-ahead (the "most important" for modelling, p. 10); Swiss SFC (secondary reserve) capacity market; generic intraday (Ch. 6.4.1); forward peak products (Ch. 6.4.2). Swiss SFC rules: weekly tender, symmetric blocks ≥ 5 MW in ±1 MW steps, quantity-price pairs, TSO picks at most one pair per bid, control demand ±400 MW, almost symmetric energy (p. 11-12).
- **Horizon and resolution:** MTHP: months to a few years, typically one year; daily or weekly interstages with hourly intrastage steps (p. 41, 77).

## Method
- **Model type:** multistage stochastic program written as DP recursions; multi-horizon decomposition (Ch. 6.2, p. 76-86):
  1. *Interstage (master) problem:* daily/weekly stages; **states = storage reservoirs only**; here-and-now decision = daily/weekly total release W_t (SDP version); output = water values/profit-to-go (p. 77).
  2. *Intrastage problem:* hourly; states = balancing reservoirs; DA bidding and production; possibly a multistage stochastic program on a scenario tree, solved as **deterministic equivalent** with CPLEX (p. 77-79). Fig. 6.1 (p. 78): (a) data revealed at once → deterministic intrastage; (b) revealed every 3 h → stochastic.
  - Balancing-reservoir fillings fixed at start/end of every intrastage problem (no inter-stage storage in small basins), justified by strong daily autocorrelation (p. 78-79).
  - SDP form (6.1, p. 79-81): Q_t(v) = max_W (1/N_t) Σ_j φ_j(W) + Q_{t+1}(v − W); W discretised adaptively. SDDP form (6.2, p. 81-82): no here-and-now W; end-of-stage storage may vary by sample j; storage balance explicit.
- **Solution methods (Ch. 3-4, 7):** SDP (discretised states/decisions; for KWM), SDDP/dualized SDDP (for KWO); Matlab + CPLEX 12.4 (p. 14).
  - SDDP review (p. 30-37): cuts as outer approximation of a concave profit-to-go; deterministic upper bound (maximisation), statistical lower bound with CLT confidence (eq. 3.15); cut selection by age or level-one dominance (p. 37); SDP beats SDDP for 1-2 states, SDDP not for > ~20 states (p. 35). Water values = slope of the active cut at a given filling (p. 44).
  - **Markov-chain / multi-cut SDDP (Sec. 4.2, p. 52-54):** stage-wise dependence handled by state augmentation (AR inflow, cuts shared, concave, slower convergence) or by a discrete Markov chain for prices with **cuts not shared across Markov states** (after Gjelsvik et al. 1999, ref. [76] = bib `gjelsvik1999`); value function need not be concave in the price state; cost grows with the number of Markov states, convergence rate not affected (p. 53-54, Example 4.1 with 2 price states and AR(1) inflow).
  - Non-concavity (Table 4.1, p. 55): multi-cut SDDP, concavification/reformulation, ordinary SDDP (slight), **dualized SDDP** via Lagrangian relaxation of state-transition constraints (moderate; Alg. 5, p. 56-59, ≥ 2× effort), SDP (not well-behaved).
  - Ch. 7: measure of non-concavity = relative gap between Lagrangian-relaxed and original objective (eq. 7.1, p. 120); KWO without SFC: small (Fig. 7.2a axis only up to 2 %; "doesn't show any considerable non-concavity" despite 9 binaries of 44 decisions, p. 120-121); **with SFC: ~10× larger**, dualized SDDP needed in at least half the stages (p. 121); forcing end fillings via terminal value amplifies non-concavity (p. 122). Locally valid cutting planes (p. 122-126).
- **How uncertainty is represented:** sampled data (SAA) with N_t samples per stage, stage-wise independent in the main algorithms (p. 25-26); data processes assumed given by the GenCo, not modelled in the thesis (p. 10); Monte Carlo evaluations sample from distributions estimated from data "because of lack of a sufficient amount of historical data" (p. 102).
- **Risk (Ch. 5, 6.2.3):** nested (dynamic) mean-AV@R (eq. 5.3-5.6), coherent and time-consistent (p. 66-67); risk-averse SDDP loses the lower bound → stop on stable upper bound or iteration count (p. 69). Multi-horizon variants: risk on the whole subtree or on intrastage scenarios only (eq. 6.3, p. 83-84).
- **Ancillary services in the multi-horizon model (Sec. 6.2.4, p. 84-86):** only capacity remuneration (energy delivery assumed symmetric, net zero); **bid capacity a multiple of 10 MW per qualified turbine; price fixed beforehand at a conservative 20 CHF/MWh** (p. 85); SFC quantity is "modeled as a wait-and-see decision within the intrastage subproblem" (p. 85); interstage length = tender period (weekly; expected to become ≤ daily) (p. 85-86); integer q and binary q_active with modified turbine limits (eq. 6.4) → MILP → non-concave value function → SDP or dualized SDDP (p. 86). SFC set point and minimum generation reduce flexibility (Fig. 2.1, p. 11-12).
- **Key modelling choices:** **head dependence neglected** and constant efficiencies ("reasonable for HPPs in the Alps with a relative high water head compared with its maximum variation", p. 9); forbidden zones for some turbines/pumps (p. 9); discounting omitted (p. 22); evaluation by operation simulation with sequential hourly MILPs using water values as opportunity costs (p. 87).

## Data / case
KWM and KWO (above); data partly confidential (p. 13). Hourly priced forward curve from the KWM operator; EEX Phelix German peak futures for forwards (p. 109). Hardware: 2× Xeon E5 2.2 GHz, 8 of 16 cores, shared server ("some results have to be taken with caution", p. 14).

## Key findings
- (p. 12) SFC value: KWO max 280 MW SFC × conservative 20 CHF/MW/h ≈ almost 50 M CHF/yr possible vs typical market turnover ~140 M CHF/yr.
- (p. 46-49, Tables 3.1-3.2) Coupled here-and-now stage problem as one LP is 60-100× faster than decomposing by discretised decisions; wait-and-see formulation over-optimistic; deterministic expected-value formulation can be infeasible (VSS infinite in toy example).
- (p. 89-90, Table 6.2, Fig. 6.3) Commercial hourly SDP tool for KWO (balancing reservoirs fixed at one point) needs HPC; multi-horizon gives > 80 % less overflow; hourly SDP cannot anticipate within-day patterns.
- (p. 93-96, Fig. 6.4, Table 6.3; KWO, deterministic data, convergence = gap < 5 %) multi-horizon 19 iterations / ~6 h; hourly SDDP 62 iterations / ~108 h and ~24× memory; daily SDDP 16 iterations / 22 min. Lower bound vs in-sample simulation profit [M€]: **multi-horizon 119 vs 116 (2.3 %)**, hourly SDDP 111 vs 99 (12 %), daily SDDP 96 vs 111 (13 %). First-stage water values similar across methods, higher for higher-elevation basins, lowest for the daily model (short-term flexibility not exploited) (p. 94).
- (p. 96-104, KWM, weekly interstage, SDP, with/without SFC; same experiment as `abgottspon2014`) four intrastage representations: (1) weekly peak/off-peak, (2) price-duration curves, (3) deterministic intrastage (week known), (4) stochastic intrastage (DA prices revealed daily, inflow weekly). Fig. 6.7: more short-term detail → higher water value; method 3 overvalues; methods 3 and 4 within 10 % for ~80 % of water values (p. 102). Table 6.4 (100 Monte Carlo scenarios, **M€**): expected profit 34.24/34.99, 29.13/30.44, 34.80/35.85, 33.40/**39.14**; AV@R10 % 32.66/33.27, 27.90/29.03, 33.27/33.47, 31.82/**36.28** (without/with SFC). Method 4 best only with SFC (+~10 %).
- (p. 103-104) Recommendation: stochastic intrastage needs good data-process modelling, so **deterministic intrastage subproblems are "a good compromise"**; even for a simple plant like KWM multi-horizon modelling is meaningful.
- (p. 105-107) Long-term valuation of KWM: daily interstage, DA bid as 24-h here-and-now, intraday wait-and-see in 4-h blocks (2⁶ = 64 ID scenarios per DA scenario); risk-neutral DA+ID without price response creates arbitrage → positions limited to about max generation; "results of the evaluation critically depends on these limits" (p. 106-107). Study (EPFL, Iliadis 2014): payback ~30 years, IRR 4-8 % depending on fuel/CO₂ prices (p. 107).
- (p. 107-115) Price-maker forward + DA trading with linear price response (quadratic objective), monthly receding-horizon bidding simulation from April 2009: forward trading 24 vs 20 M€ (+~20 %); small balancing basin limits turbine/pump deployment (p. 113-114).
- (p. 125-126, Table 7.1, KWM with SFC, 100 scenarios) mean profit: perfect information 53.04, SDP 44.70, dualized SDDP 43.54, SDDP with locally valid cuts 44.32 M€.
- (p. 129-130) Delta-hedging: if August SFC offers are not accepted, production ~30 MW lower → don't sell all expected production forward.
- (p. 135) For a price-taker, the marginal value of a turbine/pump = difference of upstream and downstream water values divided by its production function; fails for complex plants (KWO), so marginal cost curves are built by simulation (p. 135-136).
- (p. 144) Agent-based Swiss SFC market: strategic bidding beneficial in theory but unlikely in practice (oversupply of reserves).

## Strengths
- Systematic, practitioner-oriented treatment of how to couple seasonal water values with hourly operation, with explicit formulations for each alternative (Ch. 6) and clear trade-off table (Table 6.1, p. 88).
- Real plants with industry-validated models; explicit treatment of reserve-induced non-concavity.
- Good textbook-level review of SDP, SDDP, Markov-chain multi-cut SDDP, dualized SDDP and nested AV@R in hydro context (Ch. 3-5).

## Weaknesses / limitations
- KWO comparisons (Sec. 6.3.1) use **no inflow/price scenarios** (deterministic DDP) and **in-sample** single-run simulation (p. 93, 95); only KWM tests (Sec. 6.3.2, Ch. 7) are stochastic Monte Carlo, with distributions estimated from limited data (p. 102).
- Head effects neglected, constant efficiencies (p. 9); balancing reservoirs reset each stage (p. 79).
- SFC: capacity price fixed and known (20 CHF/MWh), only capacity payment, symmetric activation (p. 85).
- Data confidential, shared busy server for timings (p. 13-14). Not peer reviewed as a whole (chapters partly are).
- Numbers for the KWO comparison differ from the 2016 paper (see oddities below).

## Comparison with `abgottspon2014` (PSCC note) — what the thesis adds or corrects
| Item | `abgottspon2014` note | Thesis |
|---|---|---|
| Plant | "typical Swiss plant", no data | It is **KWM** (Sec. 6.3.2 uses KWM; Table 6.4 = Table II); data in App. A.1 (100 Mm³ / 0.1 Mm³; 2×37 MW Francis, 2×23 MW pumps, 2×92 MW Pelton, 260 MW) (p. 96, 151-153) |
| Units of Table II | "likely M€, unverified" | **Mio €** confirmed (Table 6.4, p. 103) |
| Head effects | "unverified" | Explicitly **neglected**, constant efficiencies (p. 9) |
| SFC quantity | all-or-nothing per turbine | Multi-horizon model: integer multiples of **10 MW** per qualified turbine + binary active (eq. 6.4, p. 85-86); methods 1-2: binary q ∈ {0,1} × q_max (eqs. 6.6-6.7, p. 97-99) |
| SFC price | "minimum one can expect to be accepted" | Estimated from historical data, conservative **20 CHF/MWh** (p. 85) |
| Timing of SFC decision | here-and-now first stage of intrastage | Thesis text says "wait-and-see decision within the intrastage subproblem" (p. 85), i.e. wait-and-see w.r.t. the interstage sample; whether it precedes the intrastage DA tree is not stated (unverified) |
| Why SDP not SDDP | non-concavity from reserves | Same, plus: KWM has one storage state so SDP is cheap; dualized SDDP used for KWO; non-concavity ~10× with SFC (p. 86-87, 121) |
| Recommendation | stochastic intrastage pays off with reserves | Adds: deterministic intrastage is a "good compromise" given data-modelling burden (p. 103-104) |
| Monte Carlo data | estimated distributions | Same: "lack of a sufficient amount of historical data", 100 scenarios (p. 102) |

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: Markov-chain SDDP (cuts per Markov state) | Multi-cut SDDP, non-concavity in price state, complexity | p. 52-54, Sec. 4.2, Example 4.1; p. 118 fn. 1 |
| Theory: SDDP bounds and water values | Upper/lower bound (max problem), CLT confidence bound, cut selection, water value = active cut slope | p. 30-37, 43-44 |
| Theory: here-and-now vs wait-and-see, EVPI/VSS | Toy example and Tables 3.1-3.2 | p. 44-49 |
| Model: weekly stages + hourly within-week subproblem | Multi-horizon framework; deterministic vs stochastic intrastage | p. 76-82, Fig. 6.1; p. 96-104 |
| Model limitation: within-week perfect foresight | Method 3 overvalues water; methods 3/4 within 10 % for ~80 % | p. 102, Fig. 6.7 |
| Model: reserves make SDDP non-convex unless continuous | SFC with integer/binary → MILP → non-concave; measure ~10× | p. 86, 118, 121 |
| Model: reserve modelling simplifications | Capacity-only, symmetric activation, fixed price 20 CHF/MWh, 10 MW blocks | p. 84-86 |
| Model: head effects neglected justification | High head relative to variation (Alps) | p. 9 |
| Model: PHS bidding from water values | Pump/turbine marginal value from water-value difference | p. 135 |
| Lit. review: modelling PHS plants | Hourly vs daily vs multi-horizon on KWO: 12 %/13 %/2.3 % deviation | p. 87-96, Table 6.3 |
| Lit. review: market participation (reserves) | SFC raises profit ~10 % with stochastic intrastage; SFC ~50 M CHF potential vs 140 M CHF turnover | p. 12, 103 |
| Lit. review: market participation (DA+ID arbitrage) | Need position limits when DA and ID both in a risk-neutral model | p. 106-107 |
| Background: PHS investment economics | KWM payback ~30 y, IRR 4-8 % (citing Iliadis 2014) | p. 107 |
| Method: risk | Nested mean-AV@R; no lower bound in risk-averse SDDP | p. 65-69 |
| Method: benchmarks | Perfect information 53.04 vs SDP 44.70 M€ | p. 126, Table 7.1 |
| Background: Swiss SFC market rules | Weekly tender, ≥5 MW symmetric blocks, ±400 MW | p. 11-12 |

## Useful quotes (with page numbers)
> "as a good compromise, one could also recommend deterministic subproblems" (p. 104)

## Follow-up references to check (backward snowballing)
- [76] Gjelsvik, Belsnes, Haugstad (1999), PSCC, Markov price model in SDDP (bib `gjelsvik1999`).
- [41] Gjelsvik, Mo, Haugstad (2010), Handbook of Power Systems I (bib `gjelsvik2010`).
- [75] Löhndorf, Wozabal, Minner (2013), Oper. Res. (bib `lohndorf2013`).
- [109] Kaut et al. (2013), multi-horizon stochastic programming, CMS (cf. bib `kaut2024`).
- [107] Pritchard, Philpott, Neame (2005), Math. Prog.
- [66] Fertig, Heggedal, Doorman, Apt (2014), optimal investment timing and capacity choice for PHS, Energy Systems 5(2), 285-306 (sizing literature).
- [121] Iliadis (2014), EPFL PhD thesis, PHS valuation in multiple markets, Swiss case.
- [74] Cerisola et al. (2012) / [78] Thome et al., SDDP with non-convexities.
- [73] Flach, Barroso, Pereira (2010), price-maker SDDP, IET GTD.
- [119] Baslis & Bakirtzis (2010), price-maker PHS yearly scheduling, EEM.

## Oddities
- KWO comparison numbers differ from `abgottspon2016multihorizon`: thesis uses a 5 % gap criterion (multi-horizon 6 h, hourly 108 h, daily 22 min) and deviations 2.3 % / 12 % / 13 % (Table 6.3, p. 95); the 2016 paper reports 0.5 % gaps after ~30 h / 2 h, ~5 % for hourly after > 4 days, and includes a fourth "daily intrastage" model. Likely different runs; cite the one matching the claim.
- The thesis lists the multi-horizon paper as "submitted to Energy Procedia, 2015" (p. 4).
