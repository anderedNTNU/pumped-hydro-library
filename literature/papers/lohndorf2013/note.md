---
bibkey: lohndorf2013
title: "Optimizing trading decisions for hydro storage systems using approximate dual dynamic programming"
authors: "Nils Löhndorf, David Wozabal, Stefan Minner"
year: 2013
venue: "Operations Research 61(4), 810-823"
peer_reviewed: true
methods: [sddp-markov-chain, two-stage-stochastic, adp-reinforcement-learning, uncertainty-modelling, benders-decomposition]
review_sections: [modelling-phs-plants, market-participation, reservoir-sizing-capacity, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/101_Lohndorf_2013_Optimizing_Trading_Decisions_for_Hydro_Storage_Systems_Using_Approximate_Dual_Dynamic_Prog.pdf
takeaway: "The original Markov-chain SDDP ('ADDP') for a price-taking pumped-hydro owner: daily stages over a year, hourly day-ahead bidding curves as an intrastage two-stage stochastic MIQP, prices and inflows on a k-means Markov lattice with counted transitions; value of the stochastic policy over a rolling deterministic benchmark grows with power capacity relative to reservoir size (+0.7% small vs +8.5% large capacity)."
---

# ADDP for hydro storage trading (Löhndorf, Wozabal and Minner, 2013)

_**Version and page mapping:** the PDF in this folder is the authors' **preprint** (32 pages, own pagination "1-32", empty "History" field), not the typeset Operations Research article (journal pp. 810-823). All page numbers below are **preprint pages (= PDF pages)**. They cannot be mapped reliably to journal pages; before quoting page numbers in the thesis, check them against the published version. Text extraction drops most Greek letters; reconstructed symbols are flagged._

_Terminology: the paper calls its method **approximate dual dynamic programming (ADDP)**. Löhndorf and Shapiro (2019) later call the same idea MC-SDDP (see `lohndorf2019`)._

## Research question / purpose
- How to optimise day-ahead bidding and hourly operation of a system of hydro storage plants (with pumping) that trades in a wholesale market, while accounting for **long-term** storage value under uncertain prices and inflows (pp. 1-4).
- Two challenges (p. 2): day-ahead prices, intraday prices, the long-run price level and inflows are all uncertain; multi-reservoir systems need coordinated releases.
- Positioning (p. 3): two-stage bidding models (Fleten and Kristoffersen 2007 etc.) do not anticipate future storage states; scenario-tree multistage models handle only few stages; SDDP handles many stages but needs stagewise independence and convexity; "the only SDDP formulation that also considers price uncertainty" (Gjelsvik et al. 2010) uses only weekly price averages, which "underrates the short-term value of storage" (p. 3).
- Contribution: decompose into an **intrastage** (daily, hourly bidding + operation, stochastic MIQP) and an **interstage** problem (MDP over days on a Markov lattice), and solve the latter with ADDP (SDDP + ADP ideas), with a convergence proof and error bound (pp. 4-5).

## Setting
- **System:** network of hydro storage plants with convergent topology; each reservoir one turbine and possibly a pump (p. 6). Case: an Austrian Alpine system with an **upper (j = 1) and lower (j = 2) reservoir**, both fed by glacier rivers, pumping from lower to upper; releases from the lower reservoir feed a downstream cascade of small plants (p. 24). Table 1 (p. 25): j = 1 max content 84,941 thousand m³ (initial 34,333), j = 2 83,000 thousand m³ (initial 37,000); max pumping 600 MW, min pumping 20 MW; max generating 592 MW, min 15 MW (j = 1); pump efficiency 4.23 and turbine efficiency 3.17 MW per 1000 m³ for j = 1 (implied round trip about 75%, our calculation). Capacity upgrade in 2011 increased pump and turbine capacity at the upper reservoir "by a factor of five"; another upgrade of the same size planned for 2016 (p. 24). (Plant identity not named in the paper; the numbers resemble Kaprun, unverified.)
- **Markets:** EEX (Germany/Austria). Day-ahead (price-taker, piecewise-linear hourly bid curves), intraday/hour-ahead used to close positions (price-setter with linear price response), balancing market deliberately not used (pp. 2, 6). No reserves; reserves and futures named as future work (p. 30).
- **Horizon and resolution:** one year, **T = 365 daily stages**, hourly decisions (24 h) within each stage (pp. 5, 7, 26).

## Method
- **Model type:** finite-horizon MDP with decision epoch one day (eq. 1, p. 7), reformulated with a **post-decision value function** V̄_t(S_t, R_t) so that the expectation over state transitions sits outside the maximisation (eq. 2, pp. 7-8, following Powell 2007). The intrastage problem for given state is a **two-stage stochastic mixed-integer quadratic program** (eq. 13, pp. 11-12):
  - *First stage, day-ahead bidding* (pp. 8-10): for each hour h, I price-volume pairs; price points fixed in advance and only volumes decided (following Fleten and Kristoffersen 2007) to avoid non-convexity; realised volume by linear interpolation (eq. 3); monotonicity (eq. 4). Breakpoints placed so each segment gets about the same number of price scenarios (eq. 5); requires K ≥ 2I + 2 scenarios to preserve non-anticipativity (p. 10).
  - *Second stage, unit commitment* (pp. 10-11): reservoir balance with topology matrix A (eq. 6), position closing x^d + x^b = Σ_j (η⁺ d − η⁻ c) (eq. 7), reservoir bounds (eq. 8), turbine/pump min-max with binaries (eqs. 9-10).
  - *Objective* (pp. 11-12): day-ahead revenue + intraday revenue with linear price response (p − γ x^b) x^b + future value v_s; future value as min over hyperplanes a_n(S_t) + Σ_j b_nj(S_t) r_j,24 (eqs. 11-12), "following Pereira and Pinto (1991)".
- **How uncertainty is represented (Sec. 4, pp. 19-24):**
  - Separation into an **interday** Markov process of environmental variables S_t = (weekday, temperature, wind, solar, inflow, gas price) (eq. 28, p. 20) and **intraday** hourly prices conditional on S_t. Since day-ahead prices for all 24 hours realise simultaneously, day-ahead price vectors are treated as intrastage randomness without serial correlation in residuals (p. 4).
  - Gas price as GBM, discretised per day by minimising Kantorovich distance (≤ 0.5, cap 30 states/day), transitions from the GBM conditional distributions (p. 21).
  - Other state variables = deterministic trend + residual Markov chain (eq. 29). Trends: trigonometric regressions for temperature (R² 80.09%), wind (R² 9.46%), solar (R² 71.67%); inflow trend per day of year by Nadaraya-Watson regression on 18 years of daily data (R² 73.65%), inflow residual multiplicative (eqs. 30-32, pp. 21-22). Seven reservoirs' inflows aggregated into one state variable because pairwise correlations are about 0.8 (p. 20).
  - **Markov chain construction (p. 22):** fix number of states M, apply **k-means** to the detrended residual vectors, estimate transition probabilities **by counting transitions between clusters** in the sample (eq. 33). M = 30; smallest cluster 14 observations, largest 143. Only first-order lag captured "to ensure parsimony" (p. 22). Gas lattice and residual chain combined as a product lattice assuming independence (p. 22).
  - Hourly day-ahead prices: 48 linear regression models (24 hours × working day/weekend) on state variables, demand and day length, with second-order interactions; stepwise BIC selection; R² 65.81%; no log transform because of negative prices (pp. 22-23). Intraday price response: regression of intraday − day-ahead on demand, slope 0.0011, used as γ (p. 23; symbol reconstructed).
  - Simulation: start from the steady-state distribution of the chain, location-scale t-distributed residuals (heavy tails), day-ahead price scenarios by **Latin hypercube sampling** (eq. 34, pp. 23-24).
- **Solution method (Sec. 3, pp. 12-19):**
  - *Relaxed problem* (Def. 1, p. 12): LP relaxation of (13) with γ = 0. Proposition 1 (pp. 12-13): its value and post-decision value function are **concave in reservoir levels** (RHS argument, backward induction). Proposition 2 (pp. 13-14): with γ = 0 the relaxed problem is the sample average of K separate LPs (all trading moves to intraday, bids drop out). Its value is an **upper bound** on the true value (p. 14).
  - Cuts: hyperplane slopes from the duals of the reservoir balance (eq. 15), weighted over successor states with the transition probabilities (eq. 16, p. 15) — one set of cuts per Markov state.
  - *ADDP algorithm* (Fig. 2, p. 16): forward pass samples a state path from the lattice and one price scenario per stage, solves the relaxed LP and stores the end-of-day reservoir state; backward pass loops over **all** Markov states at each stage and stored reservoir states, computes cuts and updates the post-decision function of every predecessor state. A cut is added only if it improves the approximation by more than ε (eq. 18, p. 16).
  - Convergence (pp. 16-19): standard SDDP proofs need stagewise independence and RHS randomness (p. 17); ADDP still converges a.s. because the backward pass solves for all scenarios and cuts are not shared across states. Proposition 3: ε = 0 converges in finitely many steps to the optimal policy of the relaxed problem; with ε > 0 the policy is at most (T − 1)ε worse (p. 17; symbol reconstructed).
  - The cuts learned on the relaxed problem are then used inside the **original MIQP** (with bidding, binaries, price response) to make decisions (p. 14).
- **Key modelling choices and assumptions:** price-taker day-ahead, price-setter intraday, expected intraday price = day-ahead price, so no incentive to withhold capacity from day-ahead (p. 6); **head effects ignored** (constant conversion factors) (p. 6); no flow delays (p. 6); inflow deterministic given the state and constant within a day (pp. 6, 10); discount factor 1.0 (p. 26); **terminal value V̄_T chosen to "sufficiently penalize" reservoir content below the initial level** (p. 26); I = 3 breakpoints (four segments), K = 20 price scenarios per state (p. 26).

## Data / case
- EEX hourly day-ahead and intraday prices 2009-2011; wind/solar forecasts of the four German TSOs; population-weighted temperature index (Austria + Germany); gas prices NetConnect Germany; inflow data from the Austrian generating company, 18 years of daily data (pp. 20, 22).
- Problem size: T = 365, |S| = 282,211 states, 44,765,192 transition probabilities; an equivalent scenario tree would need 4.3 × 10^1234 terminal nodes (p. 26).
- Six configurations (Table 2, p. 25): Default (592 MW turbine / 600 MW pump), Small Capacity (112/120 MW, pre-2011), Large Capacity (1072/1080 MW, after planned 2016 upgrade), Reservoir Chain (7 reservoirs), 50% Min Capacity, Epsilon Zero (ε = 0; default ε = 10⁴).
- Java, Google OR-Tools + Sulum LP solver for the relaxation, Xpress for the MIQP; Amazon EC2 8-core instances; multithreading with linear speed-up (pp. 25-26).
- Evaluation (p. 26): 25 ADDP iterations; expected first-stage profit vs mean simulated profit from 1000 one-year simulations of the **non-relaxed** MIQP; benchmark = **rolling-horizon deterministic LP** using point forecasts of prices and inflows.

## Key findings
- (Table 3, p. 27; row assignment reconstructed from garbled extraction and checked against the RH gaps quoted on p. 28) Expected / simulated / rolling-horizon profit (€ M): Default 164.3 / 162.4 / 154.8 (13 iterations, 6.9 h); Small Capacity 134.0 / 132.2 / 131.3 (11 it.); Large Capacity 188.3 / 188.2 / 173.5 (17 it., 11.9 h); Reservoir Chain 229.2 / 229.2 / 219.3 (17 it., 38.8 h); 50% Min Capacity 164.7 / 163.4 / 154.5; Epsilon Zero 164.3 / 162.6 / 154.2. Hyperplane counts 1.5-3.5 million.
- (p. 27) Convergence is driven by storage **power capacity** and number of units; more reservoirs raise CPU time but hardly the number of iterations or hyperplanes. Problems needing more hyperplanes are those where the policy reaches many different reservoir states, i.e. large power capacity.
- (p. 28) Gap between rolling-horizon and optimal policy: **+0.7% for the small-capacity system, +8.5% for the large-capacity system**: "a flexible storage system that possesses the ability to quickly change the reservoir content benefits more from a stochastic solution".
- (p. 28) Gap between expected (relaxed) and simulated profit ≤ 1.2%, even with 50% minimum capacity, so the LP relaxation for cut generation costs little. ε = 10⁴ needs 3.7 × 10⁸ LPs vs 4.9 × 10⁸ for ε = 0 (about 12% less time), but the gap only closes with ε = 0.
- (pp. 28-29) Ratio of power capacity to reservoir size: ignoring inflows, the upper reservoir empties in 134 days at 112 MW but 14 days at 1,073 MW. Small system pumps 5.0% of the time in winter and 20.0% in summer; large system pumps 30.0% regardless of season; higher variability of reservoir content raises the value of the stochastic solution (Fig. 4).
- (pp. 29-30) Conclusion: lattice approximation gives a good fit; algorithm near-optimal despite the relaxation; computational complexity and value of the stochastic solution depend on the **ratio of reservoir size to installed power capacity**. Future work: reserve market and futures (p. 30).

## Strengths
- First paper (to our knowledge) to combine a **Markov-chain lattice for prices and inflows with SDDP-type cuts** for a price-taking hydro owner with pumping; full recipe from econometric model to lattice to algorithm.
- Hourly bidding inside daily stages over a full year, so short-term price variation and seasonal storage are handled together.
- Clear statement of why SDDP needs modifications when prices (objective coefficients) are random, and why per-state cuts fix it.
- Rigorous: concavity proof, convergence, explicit ε error bound; honest about the relaxation (upper bound) and measures its cost.
- Evaluates the policy by simulating the real (MIQP) problem and benchmarks against a rolling deterministic plan; compares plant capacities, i.e. a configuration comparison.

## Weaknesses / limitations
- Head effects, flow delays and reserves ignored; inflow deterministic within a day.
- Lattice is trained on simulated data from a fitted econometric model; the evaluation is in-model (same simulator), not on held-out historical data.
- The relaxed problem lets all trading move to intraday (γ = 0), so cuts come from a model without bidding; the quality of this approximation is shown only for this case.
- Terminal value is an ad hoc penalty below the initial level; no discussion of its sensitivity.
- Very large state space (282k states), long run times (4.6-38.8 h); M = 30 chosen without reported sensitivity.
- Preprint in our folder; table rows in the extraction are scrambled (reconstructed above).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section, preprint) |
|---|---|---|
| Literature review 5.3: MC-SDDP applied to a PHS owner | ADDP, Austrian upper/lower reservoir with pumping, EEX | pp. 4-5, 24-25 |
| Theory: why SDDP needs modification for price uncertainty | SDDP needs stagewise independence + RHS randomness; Gjelsvik et al. 2010 only weekly price averages | pp. 3, 17 |
| Theory: per-state cuts, transition-weighted expected future value | Eqs. (15)-(16), Fig. 2 | pp. 14-16 |
| Theory: convergence with Markov-chain uncertainty | Prop. 3, finite convergence, (T−1)ε bound | pp. 16-19 |
| Theory: concavity of value function in reservoir levels | Prop. 1 | pp. 12-13 |
| Model: Markov chain by k-means + counted transitions | Eq. (33), M = 30 clusters, 14-143 obs per cluster | p. 22 |
| Model: post-decision value function formulation | Eq. (2) | pp. 7-8 |
| Model: end-of-horizon treatment | Terminal value penalises content below initial level | p. 26 |
| Model: head effects ignored / constant conversion | Assumption | p. 6 |
| Model: price-taker day-ahead, intraday price response | Assumptions; γ = 0.0011 | pp. 6, 23 |
| Model: day-ahead bidding curves with fixed price points | Eqs. (3)-(5), K ≥ 2I+2 | pp. 8-10 |
| Uncertainty modelling: fundamental drivers of prices, inflow trend | Eqs. (28)-(32), regressions and R² | pp. 19-23 |
| Method: benchmark design (rolling deterministic plan) | RH benchmark, 1000 simulations | p. 26 |
| Literature review 5.5: value of stochastic policy vs capacity / storage duration | +0.7% small vs +8.5% large capacity; 134 vs 14 days to empty | pp. 28-29 |
| Background 2.2: PHS in Europe | 45 GW PHS of 260 GW hydro; €26 bn investment in 27 GW new PHS (Zuber 2011) | p. 2 |
| Research gap: reserves not modelled | Future work | p. 30 |

## Useful quotes (with page numbers)
> "a flexible storage system that possesses the ability to quickly change the reservoir content benefits more from a stochastic solution" (p. 28, preprint)

Paraphrased: the value of the stochastic solution depends on the ratio of reservoir size to installed power capacity (p. 30).

## Follow-up references to check (backward snowballing)
- Gjelskvik (Gjelsvik), Mo, Haugstad (2010). Long- and medium-term operations planning ... based on SDDP. Handbook of Power Systems I. (SDDP with weekly price averages; EMPS/ProdRisk lineage.)
- Löhndorf, Minner (2010). Optimal day-ahead trading and storage of renewable energies: an ADP approach. Energy Systems 1, 61-77.
- Pritchard, Philpott, Neame (2005). Hydroelectric reservoir optimization in a pool market. Math. Programming 103(3). (Intrastage/interstage decomposition.)
- Fleten, Kristoffersen (2007). Stochastic programming for optimizing bidding strategies of a Nordic hydropower producer. EJOR 181(2).
- Philpott, Guan (2008). On the convergence of SDDP and related methods. ORL 36(4).

