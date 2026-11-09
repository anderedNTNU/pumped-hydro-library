---
bibkey: shapiro2020
title: "Periodical multistage stochastic programs"
authors: "Alexander Shapiro, Lingquan Ding"
year: 2020
venue: "SIAM Journal on Optimization 30(3), 2083-2102"
peer_reviewed: true
methods: [sddp-time-series, risk-averse-cvar, sddp-markov-chain]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/shapiro2020.pdf"
takeaway: "For problems with periodic data (e.g. seasonal inflows), an infinite-horizon discounted problem can be written as periodical Bellman equations over one period (contraction, unique convex solution) and solved by a periodical SDDP; on the Brazilian system a 13-stage periodical model replaces a 120-stage model (60 + 60 extension months), gives similar bounds, and avoids the end-of-horizon effect that remains in the 120-stage model when the discount factor is 0.9906."
---

# Periodical multistage stochastic programs (Shapiro & Ding, 2020)

_Version filed: author manuscript from Optimization Online (2019/09, 25 PDF pages). **Page numbers below are PDF pages** (the printed manuscript number is PDF page minus 1 from PDF p. 2 on). Journal pages are 2083-2102; no exact mapping is possible. Cite sections when page precision matters._

_Tagging note: `sddp-time-series` because the main development assumes stagewise independence and the case uses a periodic AR(1) inflow model (PDF p. 13). `risk-averse-cvar` for the law-invariant coherent risk measure framework and the mean-AV@R experiment (PDF pp. 3-5, 18). `sddp-markov-chain` only for Sec. 7 (PDF p. 23), which writes the periodical Bellman equations for a stationary homogeneous Markov chain as future work, without an algorithm or experiments._

## Research question / purpose
- Show that when a multistage stochastic program has periodical behaviour (period m), the number of stages can be drastically reduced by a periodical analogue of the discounted infinite-horizon Bellman equations from MDP and stochastic optimal control (abstract, PDF pp. 1-2).
- Describe an SDDP variant for these periodical equations and test it on the Brazilian interconnected power system (PDF p. 2).

## Setting
- **System:** Brazilian interconnected power system, 4 regions with aggregated (energy-equivalent) reservoirs, thermal plants, inter-regional exchange and a transshipment node, deficit accounts to ensure complete recourse (PDF pp. 13-14).
- **Markets:** none; system cost minimisation.
- **Horizon and resolution:** originally 60 monthly stages plus 60 stages added "to deal with the so-called end-of-horizon effect" (T = 120); periodical model with m = 12 needs only 13 stages (deterministic first stage + 12) (PDF p. 14).

## Method
- **Model type:** risk-averse multistage stochastic program in nested form with discount factor gamma in (0,1), linear dynamics B_t x_{t-1} + A_t x_t = b_t, possibly T = infinity (eq. 2.1, PDF p. 3).
- **Risk:** conditional counterparts of a law-invariant coherent risk measure; risk neutral when rho = E (PDF p. 3). For bounded stage costs the nested risk of the infinite discounted sum exists (Cauchy argument, eq. 2.3-2.4, PDF p. 4).
- **How uncertainty is represented:** stagewise independent data process (PDF p. 4); periodical assumptions (A1)-(A5): xi_t and xi_{t+m} have the same distribution; data functions periodic with period m; coherent law-invariant risk measure; bounded costs; relatively complete recourse (PDF p. 5). Case study inflows: periodic first-order AR process with multiplicative errors, period 12 (PDF p. 13).
- **Periodical Bellman (Wald-Bellman, WB) equations** (3.1)-(3.2): value functions V_2..V_{m+1} with V_{m+2} replaced by V_2 (PDF p. 5).
- **Theory:** the operator T is a contraction in the max-sup norm with modulus gamma (Prop. 3.1); Theorem 3.1: unique solution, value iteration converges, convex value functions under convexity (PDF pp. 6-7). Optimal policy from the minimisers (3.6) (PDF p. 7). m = 1 stationary case (Remark 3.1, PDF p. 7).
- **Statistical inference (Sec. 4):** error bound ||V - V-hat|| <= (1-gamma)^-1 ||T(V) - T-hat(V)|| (eq. 4.2, PDF p. 8); SAA consistency w.p. 1; sample size per stage O((epsilon - delta)^-2), total scenarios N^m (PDF pp. 8-9).
- **Solution method (Sec. 5):** cutting-plane / SDDP-type algorithm (Algorithm 1, PDF p. 12): forward step over T >= m+1 stages using the periodic cut sets; **trial points** taken from one randomly chosen m-stage cycle of the forward trajectory (PDF p. 11); backward step from stage m+1 to 2, and the stage-2 cut is also added to stage m+1 (because V_{m+2} = V_2) (PDF p. 11). Local copy variables z_t simplify duals (PDF p. 11). Convergence proofs left to future research; they argue that finite-convergence proofs "do not guarantee convergence to an arbitrary small precision for larger problems" when the number of scenarios is astronomically large (PDF p. 11).
- **Policy evaluation (5.1.2):** forward simulation over a finite T approximates the infinite-horizon policy value with truncation error bounded by gamma^T kappa/(1-gamma) (eq. 5.4, PDF pp. 10, 13); CI for discretised and for "true" (continuous) problem; gap = (upper CI end - LB)/LB (PDF p. 13). For general coherent risk measures no randomised upper bound is available (PDF p. 10).
- **Software:** MSPPy (Python), Gurobi 8.1.0; SAA with N_t = 100 per stage; 300 iterations with 10 parallel processes (about 3000 effective iterations) (PDF pp. 13-15).
- **Key modelling choices and assumptions:** discounting essential (gamma < 1); stagewise independence (Markov case only sketched); convexity; complete recourse via deficit variables.

## Data / case
- Brazilian 4-region hydrothermal model of Shapiro et al. (2013); monthly; discount factor 0.9906 (= 12% annual rate, as used in the original project) and an "algorithmic" 0.8 (PDF p. 14).

## Key findings
- (PDF p. 14) With gamma = 0.9906 the truncation-error coefficient gamma^T/(1-gamma) at T = 120 is about 34, so the 120-stage model's cost-to-go at stage 120 "may be far from zero and the end-of-horizon effect may still be significant"; with gamma = 0.8 it is about 1.2e-11 and the 120-stage model is effectively the infinite-horizon one.
- (PDF p. 14, Table 1) Risk neutral, gamma = 0.8: periodical and classical SDDP converge similarly; after 300 iterations LB 7.39 vs 7.37 ($m), gap 7.84% vs 10.3%; the periodical model solves a problem about ten times smaller per iteration (PDF p. 15).
- (PDF p. 15, Fig. 2) Stored energy stabilises quickly and is slightly more cyclical with the periodical model.
- (PDF p. 16, Figs. 3-4) gamma = 0.9906: classical SDDP stage costs decay faster in later stages because it "tends to use up all available stored energy" near the horizon end (end-of-horizon effect); the first ~10 stages agree, so rolling-horizon use of the first stages behaves similarly.
- (PDF p. 17) Mean-AV@R (lambda = 0.2, alpha = 0.1): both stabilise after 300 iterations; with gamma = 0.9906 the classical model suffers more from end-of-horizon effects than in the risk-neutral case; periodical solutions more cyclical and regular.
- (PDF pp. 20-21, Table 2) Binary thermal-security constraints (SDDiP with strengthened Benders cuts) become tractable with 13 stages; gap 5.67% after 300 iterations (gamma 0.8).
- (PDF p. 22) Conclusion: periodical SDDP gives similar and sometimes more reasonable solutions at much lower cost; for gamma close to 1 policy evaluation and upper bounds are expensive; the user may choose longer periods (m = 24 or 60) and still reduce effort and handle end-of-horizon effects.
- (PDF p. 23) Markov extension: for a stationary homogeneous Markov chain, a value function V_i is needed for every state i (eq. 7.2) - left as future research.

## Strengths
- Rigorous contraction / fixed-point foundation for infinite-horizon periodic SDDP.
- Quantifies the end-of-horizon truncation error and shows it can be large for realistic discount factors.
- Direct numerical comparison with a classical long-horizon model on a real hydro-dominated system.

## Weaknesses / limitations
- No convergence proof for the periodical SDDP (PDF p. 11).
- Markov-chain case only sketched; no experiments with Markov states (PDF p. 23).
- The gamma = 0.8 experiments have no economic meaning (stated by the authors, PDF p. 14).
- Requires strict periodicity of the data (stationary seasonal pattern).
- Manuscript version; journal pages differ.

## Use it for... (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model: horizon extension / end-of-horizon effect | 60 + 60 months to deal with end-of-horizon effect; stored energy run down near horizon end; truncation error coefficient | PDF pp. 14, 16 (Sec. 6, 6.2) |
| Model: terminal value 0 and truncation error bound | |sum_{t>T} gamma^{t-1} f_t| <= gamma^T kappa/(1-gamma) | eq. 5.4, PDF p. 10; eq. 2.3, PDF p. 4 |
| Discussion / future work: infinite-horizon (periodical) SDDP as alternative | Periodical WB equations, contraction, periodical SDDP algorithm | Secs. 3, 5, PDF pp. 5-12 |
| Theory: Markov-chain Bellman equations with one value function per state | Eq. 7.2 | Sec. 7, PDF p. 23 |
| Method: policy evaluation, CI and gap definitions | Forward simulation, CI for discretised and true problem, gap formula | Sec. 5.1.2, PDF p. 13 |
| Theory: SAA sample complexity | O((eps-delta)^-2) per stage, N^m scenarios | Sec. 4, PDF pp. 8-9 |
| Method: practical caveat on convergence proofs | Proofs give no practical precision guarantee with astronomically many scenarios | PDF p. 11 |

## Useful quotes (with page numbers)
> "the classical SDDP tends to use up all available stored energy and thus reduces the stage costs" (PDF p. 16)

## Follow-up references to check (backward snowballing)
- Shapiro, Tekaya, da Costa & Soares (2013), risk-neutral and risk-averse SDDP on the Brazilian system (EJOR 224).
- Ding, Ahmed & Shapiro (2019), MSPPy Python package.
- Warrington, Beuchat & Lygeros (2019), generalized DDP for infinite horizon.
- Baucke (2018), infinite-horizon Markov DP algorithm.
- Zou, Ahmed & Sun (2019), SDDiP.
- Bertsekas & Shreve (1978), contraction arguments.

