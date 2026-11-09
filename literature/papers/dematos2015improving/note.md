---
bibkey: dematos2015improving
bibkey_provisional: true
title: "Improving the performance of stochastic dual dynamic programming"
authors: "Vitor L. de Matos, Andy B. Philpott, Erlon C. Finardi"
year: 2015
venue: "Journal of Computational and Applied Mathematics 290, 196-208 (volume/pages unverified; DOI 10.1016/j.cam.2015.04.048)"
peer_reviewed: true
methods: [sddp-time-series, sddp-markov-chain]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDDP_i_vannkraft/DeMatos2015.pdf"
takeaway: "Computational tuning of SDDP on a 120-stage Brazilian hydrothermal model: cut selection (Level-1 dominance best) cuts run time about 10x with negligible loss in bound or policy cost, and scenario incrementation (start with one forward scenario per pass, increase over iterations) gives the best policy; one-scenario passes win early, many-scenario passes win late."
---

# Improving the performance of SDDP (de Matos, Philpott & Finardi, 2015)

_Version filed: author manuscript from EPOC dated 6 January 2015 (29 pages). **Page numbers below are manuscript (= PDF) pages.** Journal version pagination differs (no mapping)._

_Tagging note: `sddp-time-series` is the closest available tag for this stagewise-independent SDDP study (monthly lognormal inflows, no PAR model; there is no plain "SDDP" tag). `sddp-markov-chain` is added only because the tuning techniques (cut selection, forward-pass scenario strategy) apply directly to our MC-SDDP implementation; the paper itself has no Markov chain._

## Research question / purpose
- Tune SDDP to build a near-optimal policy in the shortest computation time, by testing (i) how scenarios are visited in the forward pass (tree-traversing strategy) and (ii) which cuts are included in the stage LPs (cut selection) (pp. 2-3).
- Motivation: models must be solved frequently by the ISO and energy companies, so computation time must be modest (p. 3).

## Setting
- **System:** Brazilian power system, 158 hydro and 151 thermal plants; hydro aggregated into 4 energy-equivalent reservoirs (p. 17).
- **Markets:** none; cost minimisation.
- **Horizon and resolution:** 10 years, monthly, 120 stages (p. 17).

## Method
- **Model type:** multistage stochastic LP, RHS uncertainty, stagewise independent; last stage future cost 0 or a convex polyhedral function (pp. 3-4).
- **How uncertainty is represented:** inflows stagewise independent with a known lognormal distribution per calendar month (12 distributions per reservoir) (pp. 17-18). SAA: 20 equally likely Monte Carlo outcomes per stage -> 20^119 scenarios; forward scenarios and policy evaluation sampled within the SAA tree (p. 18).
- **Solution method:** SDDP (Sec. 2, pp. 3-8) with three tree-traversing strategies (Sec. 3):
  - *Traditional:* N scenarios per forward pass, N cuts per stage per backward pass (pp. 5-8).
  - *One scenario per pass* (Philpott & Guan 2008): forward + backward on one scenario at a time; performs well early (p. 9). Its UB estimator is unbiased but successive costs are not independent, so no CLT-based CI during the run; "in practice we typically run it for a pre-determined number of iterations" (pp. 9-10). Less advantageous under parallel processing (p. 10).
  - *Scenario incrementation* (cf. Shapiro et al. 2013): batches of N scenarios with k scenarios per pass, k increasing through the factors of N; admits a convergence test once k is large (pp. 10-11).
- **Cut selection (Sec. 4, pp. 12-17):** cuts are never deleted, only excluded from the LP; at the end all cuts define the policy (p. 12). Strategies: *Last-cuts* (keep the most recent H, e.g. 600 or 1000) (p. 13); *Level-H dominance*: keep cuts that are among the H highest at some previously visited trial point (Level 1 = highest at some point), with cheap incremental bookkeeping (pp. 14-15); *Dynamic cut selection (DCS)*: add the most violated stored cut iteratively and re-solve, warm-started with cuts used earlier in the iteration (pp. 15-17).
- **Stopping:** fixed number of iterations (10,000 cuts per stage); the standard test is included for completeness but judged less reliable (p. 6).
- **Key modelling choices and assumptions:** aggregated reservoirs, stagewise independence, Gurobi 4.61, 10 parallel processes (p. 18).

## Data / case
- 21 cases: 3 tree-traversing strategies x 7 cut-selection settings (600 cuts, 1000 cuts, Level 1-3, DCS, none) (Table 1, p. 18). 10,000 cuts per stage; each policy simulated on 5,000 SAA scenarios at 11 checkpoints (pp. 18-19).

## Key findings
- (pp. 19-20, Tables 2-3, Fig. 5) One scenario per pass: keeping only the last 600 cuts is fastest but gives the lowest LB and the costliest policy; Level 1 dominance gives essentially the same quality as no selection and is **11 times faster** (p. 20).
- (pp. 21-22, Tables 4-5, Fig. 6) Scenario incrementation: LB similar across selection strategies; last-cuts policies more expensive; Level 1 slightly quickest.
- (pp. 23-24, Tables 6-7, Fig. 7) Traditional traversal: Level 1 again best speed-quality trade-off.
- (p. 24) Traditional traversal is poor early: with no cuts in the first pass "all water is used in all 200 scenarios"; one-scenario-per-pass improves the Bellman approximation faster early (p. 24).
- (pp. 24-25, Tables 8-9) Late in the run, many scenarios per pass win: after 10,000 cuts traditional (LB 24.697) and incrementation (24.701) beat one-per-pass (24.634) (10^9 BRL).
- (p. 25) Without cut selection all three take about 12 h for 10,000 cuts, roughly ten times slower than with Level 1 dominance.
- (pp. 26-27, Tables 10-11) Best combination: start with one scenario per pass, increment scenarios, Level 1 dominance; cut selection does not significantly change LB or expected cost at termination but reduces time by an order of magnitude (p. 26).

## Strengths
- Systematic factorial comparison on a realistic large instance; policies evaluated by independent simulation (5,000 scenarios).
- Simple, cheap cut-selection rule (Level 1) that is easy to implement.

## Weaknesses / limitations
- Single test case; efficiency "will vary from problem to problem" (p. 18).
- Evaluation within the SAA tree, not the underlying distribution (p. 18).
- Stagewise independence only; no Markov states (in MC-SDDP the number of cut sets grows with states, so cut selection matters per (stage, state)).
- Journal metadata (volume/pages) not printed in the manuscript (unverified).

## Use it for... (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method: cut selection to speed up SDDP | Last-cuts, Level-H dominance, DCS; Level 1 ~10-11x faster with no quality loss | Sec. 4, pp. 12-17; results pp. 19-27 |
| Method: number of forward paths per iteration | One-per-pass vs traditional vs incrementation; early vs late behaviour | Sec. 3, pp. 8-11; p. 24 |
| Method: stopping by fixed iterations; no CI during one-per-pass runs | Rationale for pre-determined iteration count | p. 6, pp. 9-10 |
| Method: policy evaluation by independent simulation | 5,000 simulated scenarios at checkpoints | pp. 18-19 |
| Theory: SDDP description (forward/backward, LB/UB, 90% CI test) | Standard formulation | Sec. 2, pp. 3-8 |

## Useful quotes (with page numbers)
> "cut selection strategies do not have a significant impact on the policy in terms of lower bound and expected operation cost at the end of the iterative process, but they may reduce the computation time by an order of magnitude." (p. 26)

## Follow-up references to check (backward snowballing)
- Homem-de-Mello, de Matos & Finardi (2011), sampling strategies and stopping criteria for SDDP (Energy Systems 2).
- Shapiro, Tekaya, da Costa & Soares (2013), scenario incrementation and last-active-cuts selection (EJOR 224).
- de Matos & Finardi (2012), computational study of LTHS model (IJEPES 43).
- de Matos, Philpott, Finardi & Guan (2011), PSCC.

