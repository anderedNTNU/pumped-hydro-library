---
bibkey: shapiro2011
title: "Analysis of stochastic dual dynamic programming method"
authors: "Alexander Shapiro"
year: 2011
venue: "European Journal of Operational Research 209(1), 63-72"
peer_reviewed: true
methods: [sddp-time-series, sddp-markov-chain, risk-averse-cvar, multistage-scenario-trees, benders-decomposition]
review_sections: []
relevance: high
read_by: []
added: 2026-11-04
takeaway: "SDDP analysed as an algorithm on a sample average approximation (SAA) of a stagewise-independent linear multistage problem: what the LB and the statistical UB really bound, why the Pereira-Pinto stopping rule is misleading, finite (but possibly impractical) convergence w.p.1, paired t-test policy comparison, and a mean-CVaR risk-averse SDDP at almost the same cost."
---

# Analysis of the SDDP method (Shapiro, 2011)

_Page mapping: PDF page n = journal page 62 + n (journal pp. 63-72)._

_Tagging note: `sddp-time-series` because the paper treats SDDP under stagewise independence and shows AR(1) dependence handled by state augmentation (p. 63). `sddp-markov-chain` is included only because its bound, stopping and policy-comparison results are what we apply to our MC-SDDP; the paper itself contains **no** Markov-chain treatment. `multistage-scenario-trees` because SDDP is analysed on a sampled SAA scenario tree (p. 66). `benders-decomposition` because the two-stage backward step is Kelley's cutting plane (p. 65)._

## Research question / purpose
- Analyse statistical properties and convergence of SDDP for linear multistage stochastic programs with stagewise-independent data, in a two-step framework: first sample an SAA problem from the true (possibly continuous) distribution, then solve the SAA with SDDP (p. 63, abstract and Sec. 1).
- Relate SDDP solutions and bounds of the SAA problem to the "true" problem (pp. 65-67).
- Extend SDDP to a risk-averse (mean-CVaR, nested) formulation and argue its complexity is almost the same as risk neutral (pp. 63-64, Sec. 4, pp. 68-71).

## Setting
- **System:** generic linear multistage stochastic program (1.1) (p. 63). No energy application, no data.
- **Markets:** n/a.
- **Horizon and resolution:** general T stages.

## Method
- **Model type:** linear multistage stochastic programming, nested formulation (1.1) with random data xi_t = (c_t, A_t, B_t, b_t), xi_1 deterministic (p. 63). Two-stage case first (Sec. 2), then multistage (Sec. 3).
- **How uncertainty is represented:**
  - Basic assumption: stagewise independence, xi_{t+1} independent of the history xi_[t] (p. 63).
  - Across-stage dependence "in some cases" handled by adding state variables: if only b_t is dependent and follows a first-order AR process b_t = Phi b_{t-1} + eps_t with independent errors, replacing x_t by (x_t, b_t) recovers stagewise independence (eq. 1.2, p. 63). Nonnegativity need not be enforced on b_t.
  - Earlier SDDP work assumed finitely many scenarios; Shapiro allows continuous distributions (e.g. normal or log-normal ARIMA errors) and samples from them (p. 63).
  - SAA: replace each P_t by an empirical distribution of N_t i.i.d. draws, each with prob 1/N_t; the SAA tree preserves stagewise independence and has prod_{t=2}^T N_t scenarios (p. 66, eq. 3.4).
- **Solution method:** SDDP applied to the SAA.
  - *Backward step (two-stage)* (p. 64, eqs. 2.6-2.9): solve the second stage for all N sample points at the trial x_k, average values and dual-based subgradients, add a supporting plane; lower bounds theta_k (eq. 2.8). This is Kelley's cutting plane method, finitely convergent for the two-stage SAA (p. 65).
  - *Forward step (two-stage)* (p. 65, eqs. 2.10-2.11): subsample M points from the SAA (with or without replacement), compute sample mean and variance of costs, normal-approximation CI.
  - *Multistage backward step* (pp. 66-67, eqs. 3.5-3.12): solve stage T for each of N_T realisations, average duals into a cut for stage T-1, move backwards. For t < T the resulting planes are only cutting planes (not necessarily supporting) of the true SAA cost-to-go, because they are computed from approximations (p. 67).
  - *Implementable policy* (p. 67, eq. 3.14): forward recursion using the current cut approximations; the policy is feasible for any realisation, so its expected cost (eq. 3.15) is an upper bound.
  - *Policy comparison* (p. 68, Remark 6, eq. 3.16): evaluate two policies on the same M sampled scenarios and apply a paired t-test to the differences.
  - *Risk-averse SDDP* (Sec. 4, pp. 68-71): chance constraint -> VaR (non-convex) -> CVaR conservative approximation (Rockafellar-Uryasev) (eqs. 4.1-4.6, pp. 68-69); mean-CVaR objective rho = (1-lambda)E + lambda CVaR_alpha, a coherent risk measure (eq. 4.7, p. 69); reformulated by adding an auxiliary first-stage variable u (VaR level) and a second-stage LP (eqs. 4.8-4.11); nested multistage version with stage parameters lambda_t, alpha_t (eqs. 4.12-4.16, p. 69); time-consistent (p. 70); DP equations with state augmented by u_t (eqs. 4.17-4.25, p. 70); SAA cuts and subgradient formula (eqs. 4.26-4.29, p. 70); forward step (eq. 4.30, p. 70); policy value requires conditional (nested) sampling with prod M_t LPs, impractical for many stages (pp. 70-71).
- **Key modelling choices and assumptions:** linearity; relatively complete recourse (second stage feasible for all x in X and almost every realisation) (p. 64; also p. 66); X nonempty and bounded (p. 64); finite cost-to-go functions; convex cost-to-go (p. 64, p. 66); piecewise-linear SAA cost-to-go (p. 66); assumption (A1) finite optimal values for all SAA scenarios (p. 68); basic optimal dual solutions in backward steps (p. 68); forward samples drawn independently from the SAA scenarios (p. 68).

## Data / case
- None. Purely theoretical/methodological; no numerical experiments.

## Key findings
- (p. 63) SDDP complexity of one forward/backward run is proportional to the *sum* of sampled points per stage, not their product; this holds *because of* stagewise independence (p. 64).
- (p. 63) Stagewise dependence of AR(1) type in the RHS can be removed by augmenting the state with b_t.
- (p. 64) Convex expected value function under the stated assumptions; lower bounds theta_k on the SAA optimal value from the cut approximation (eq. 2.8).
- (p. 65, Remark 1) The Pereira-Pinto stopping rule (stop when LB is inside the UB CI, citing their p. 368) gives no accuracy guarantee: higher variance or higher confidence makes it stop sooner; at high enough confidence it can stop at any iteration.
- (p. 65, Remark 2) Variance decomposition and a CI for the *true* expected value combining forward-sample and SAA-sample variance (eqs. 2.12-2.13).
- (p. 65, Remark 3) Expected SAA optimal value is below the true optimal value, so E[theta_k] is also a lower bound for the true problem; SAA optimal values converge at rate O_p(N^{-1/2}), so accuracy epsilon needs N = O(epsilon^{-2}).
- (p. 66) The cutting-plane (Kelley) method is not efficient for two-stage LPs; better methods exist but it is unclear how to extend them to multistage (footnote 5).
- (p. 66) The SAA tree has prod N_t scenarios; scenario-tree approaches to multistage problems are computationally intractable, but sample sizes N_t of order O(epsilon^{-2}) per stage suffice for an epsilon-accurate solution (citing Shapiro 2006 and Shapiro et al. 2009).
- (p. 67) theta_k is, on average, a lower bound for the true optimal value; the expected cost of the forward (implementable) policy over the true distribution is an upper bound for the true problem, over the SAA scenarios an upper bound for the SAA. UB at confidence about 1-alpha: theta-bar + z_alpha sigma-hat / sqrt(M).
- (p. 67, Remark 4) The forward-cost variance grows roughly proportionally to T; it is more meaningful to use the difference between the UB (theta-bar + z_alpha sigma/sqrt M) and the LB as an approximate bound on the optimality gap of the current policy.
- (pp. 67-68, Remark 5) Taking the minimum of k upper bounds requires a Bonferroni correction (confidence 1-alpha/k per bound).
- (p. 68, Remark 6) Two policies can be compared by a paired t-test on common sampled scenarios; pairing is advantageous because the two costs are positively correlated (footnote 7).
- (p. 68, Prop. 3.1) With subsampled, independently generated forward scenarios, (A1), and basic optimal duals, the forward policy is optimal for the SAA w.p.1 after a sufficiently large number of iterations (finite convergence). Without independence of forward samples there is no convergence guarantee "even for relatively small problems".
- (p. 69) Mean-CVaR is coherent; formulation (4.7) avoids the infeasibility that the CVaR constraint (4.6) can cause; lambda trades off average vs. risk.
- (p. 70) The nested risk-averse formulation is time consistent; backward-step complexity almost unchanged vs risk neutral (p. 71).
- (p. 71) Finite convergence proofs can be misleading: with astronomically many scenarios and cuts, convergence may take unrealistically long; Kelley's method has exponential worst case in dimension (Nesterov). It may be impossible to solve the SAA to optimality, yet SDDP can give a practically acceptable implementable policy.
- (p. 71) For large T, sample-based upper bounds are typically too loose to be practically useful; a more realistic stopping rule is to stop when the lower bounds stabilise (Hindsberger and Philpott), and possibly test via t-tests whether further iterations improve the policy. Stabilisation of LB does not mean optimality.
- (p. 71) Cut removal should be done with care because it can alter statistical properties of bounds.
- (p. 71) For risk-averse SDDP, upper bounds are not straightforward; compare expected values of risk-averse and risk-neutral policies with the t-test instead.

## Strengths
- The standard reference for what SDDP bounds mean statistically and for the critique of the original stopping rule.
- Separates two error sources cleanly: SAA sampling error (true vs sampled problem) and SDDP optimisation error (policy vs SAA optimum).
- Gives a practical policy-comparison method (paired t-test on common random numbers), directly usable for benchmark evaluation.
- Early, influential risk-averse (nested mean-CVaR) SDDP formulation, with explicit DP equations and cut formulas.

## Weaknesses / limitations
- Stagewise independence is assumed throughout; dependence only via state augmentation for linear AR in the RHS. No Markov-chain (finite-state) dependence, so the convergence result does not directly cover MC-SDDP (later work such as Philpott and de Matos 2012 or Löhndorf et al. covers that; not checked here).
- Convergence proof only for the finite SAA, finite cuts and independent sampling; no rate.
- No numerical experiments.
- Risk-averse upper bounds left essentially unresolved.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: stagewise independence assumption and why it matters for SDDP complexity | Definition; complexity proportional to sum, not product, only under stagewise independence | p. 63 (Sec. 1); p. 64; p. 71 (Sec. 5) |
| Theory: handling dependence by state augmentation (AR) | AR(1) RHS b_t = Phi b_{t-1} + eps_t, state (x_t, b_t) | p. 63 (eq. 1.2) |
| Theory: convexity, relatively complete recourse | Assumptions for cut validity | p. 64 (Sec. 2); p. 66 (Sec. 3) |
| Theory: SAA and sampled scenario trees | SAA construction, prod N_t scenarios, O(epsilon^-2) sample size | pp. 64-66 (eqs. 2.4-2.5, 3.4) |
| Theory: SDDP backward step and cuts in multistage | DP equations, cut formulas, supporting vs cutting planes | pp. 66-67 (eqs. 3.1-3.12) |
| Theory: lower bound / upper bound and statistical gap | LB theta_k; UB = expected policy cost (eq. 3.15); CI and UB theta-bar + z sigma/sqrt M | pp. 64-67 |
| Theory: critique of Pereira-Pinto stopping criterion | Remarks 1 and 4 | p. 65; p. 67 |
| Theory/Method: stopping rule based on LB stabilisation | Practical recommendation | p. 71 (Sec. 5) |
| Theory: convergence of SDDP | Prop. 3.1, finite convergence w.p.1 on SAA, conditions; caveat that it can be impractically slow | p. 68 (Sec. 3.1); p. 71 |
| Method/Results: comparing our policy to benchmarks | Paired t-test on common sampled scenarios | p. 68 (Remark 6, eq. 3.16, footnote 7) |
| Method: SAA vs true problem (in-sample vs out-of-sample) | Policy feasible for any realisation; expected cost over true distribution bounds true problem | p. 67 |
| Theory/Extension: risk-averse SDDP with CVaR | Mean-CVaR nested formulation, DP equations, cut subgradients, time consistency | pp. 68-70 (Sec. 4) |
| Theory: cut selection caveat | Removing cuts can affect bound statistics | p. 71 |

## Useful quotes (with page numbers)
> "it could be impossible to solve the SAA problem to optimality" (p. 71)

Other key statements, paraphrased (not quoted): the Pereira-Pinto stopping criterion gives no guarantee of accuracy (p. 65); for large T sample-based upper bounds are too loose to be useful, so stop when lower bounds stabilise (p. 71); complexity of one backward step is proportional to the sum of sample sizes (p. 71).

## Follow-up references to check (backward snowballing)
- Pereira and Pinto (1991), Math. Programming 52 (in repo: `pereira1991`).
- Philpott, A.B. and Guan, Z. (2008). On the convergence of stochastic dual dynamic programming and related methods. Operations Research Letters 36, 450-455.
- Linowsky, K. and Philpott, A.B. (2005). On the convergence of sampling based decomposition algorithms for multistage stochastic programs. JOTA 125, 349-366.
- Chen, Z.L. and Powell, W.B. (1999). Convergent cutting plane and partial-sampling algorithm for multistage stochastic linear programs with recourse. JOTA 102.
- Donohue, C.J. and Birge, J.R. (2006). The abridged nested decomposition method. Algorithmic Operations Research 1.
- Hindsberger, M. and Philpott, A.B. (2002). Stopping criteria in sampling strategies for multistage SLP-problems (conference presentation).
- Shapiro, A., Dentcheva, D. and Ruszczyński, A. (2009). Lectures on Stochastic Programming: Modeling and Theory. SIAM.
- Rockafellar, R.T. and Uryasev, S. (2000). Optimization of conditional value-at-risk. Journal of Risk 2.
- Kelley, J.E. (1960). The cutting-plane method for solving convex programs. SIAM J. 8.
- Shapiro, A. (2006). On complexity of multistage stochastic programs. ORL 34.

