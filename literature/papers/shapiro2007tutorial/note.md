---
bibkey: shapiro2007tutorial
bibkey_provisional: true
title: "A Tutorial on Stochastic Programming"
authors: "Alexander Shapiro, Andy Philpott"
year: 2007
venue: "Unpublished tutorial manuscript, dated 21 March 2007 (EPOC, epoc.org.nz/papers/ShapiroTutorialSP.pdf)"
peer_reviewed: false
methods: [two-stage-stochastic, multistage-scenario-trees, dynamic-programming, risk-averse-cvar, uncertainty-modelling]
review_sections: []
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Intuition-first tutorial built on the newsvendor/inventory model: two-stage recourse, scenario construction and the 3^d explosion, SAA and its O(N^-1/2) rate, statistical upper/lower bounds on the optimality gap, multistage DP vs scenario trees and the curse of dimensionality, and chance constraints → VaR → CVaR as the best convex conservative approximation."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Stokastisk_programmering/ShapiroPhilpott2007.pdf"
---

# A tutorial on stochastic programming (Shapiro and Philpott, 2007)

_Page mapping: 35 PDF pages; printed page numbers at the page foot equal PDF page numbers. Main text pp. 1-31 (Notes pp. 29-31), appendix pp. 31-33, references pp. 33-35._

_Bibkey note: not in `references.bib`; key generated Better BibTeX style ("A" skipped → "tutorial"). Not a journal article; if cited, use @unpublished/@misc with the EPOC URL._

_Tagging note: theory source. `dynamic-programming` because Sec. 3 derives DP equations for the multistage inventory model and discusses the curse of dimensionality. No SDDP content at all._

## Research question / purpose
- Introduce basic ideas of stochastic programming to practitioners and researchers, with emphasis on motivation and intuition rather than technical completeness (p. 1).
- Questions addressed: how to approximate a random variable by finitely many scenarios, how to solve the resulting problem, and how to judge the quality of the approximate solution (p. 6).

## Setting
- **System:** classical inventory (newsvendor) model throughout: order cost c, back-order penalty b, holding cost h; numerical instance c = 1, b = 1.5, h = 0.1, demand uniform on [0, 100] (pp. 2-5).
- **Markets:** none.
- **Horizon and resolution:** two-stage (Sec. 2) and T-period inventory (Sec. 3).

## Method
- **Model type:** tutorial.
- **Two-stage linear SP (pp. 7-8):** min c^T x + E[Q(x, ξ)], Q the optimal value of the second-stage LP (eqs. 2.1-2.2); deterministic equivalent with one copy of y per scenario (eq. 2.4).
- **How uncertainty is represented:** finite scenarios with probabilities (p. 8); expert scenarios (low/medium/high per component) give K = 3^d scenarios (p. 9); Monte Carlo sampling / SAA (eq. 2.7, p. 11); conditional-expectation discretisation gives a lower-bounding approximation by Jensen's inequality when G is convex in D (p. 6); multistage scenario trees by conditional sampling (p. 19).
- **Solution method:** LP on the deterministic equivalent; decomposition methods only pointed to in Notes (Benders/L-shaped, (augmented) Lagrangian, interior point, operator splitting, stochastic decomposition of Higle and Sen) (p. 31).
- **Solution quality (Sec. 2.3, pp. 13-16):** UB on g(x̂) from an independent sample with CLT confidence (eqs. 2.8-2.9); LB on the true optimum from M independent SAA replications using v ≥ E[v̂_N] and a t-quantile (eqs. 2.10-2.12); statistically valid gap bound with confidence at least 1 - 2α (eq. 2.13); worked example gives a 90% gap bound of 17.20 for x̂ = 40 (pp. 15-16).
- **Multistage (Sec. 3, pp. 16-19):** DP equations for the T-period inventory model with value functions V_t(y_t, d_[t-1]) (eqs. 3.3-3.6); under stagewise independence V_t depends only on y_t and the optimal policy is base-stock (p. 18); non-anticipativity and definition of a (feasible) policy (pp. 17-18).
- **Risk (Sec. 4, pp. 19-29):** worst-case constraint, chance constraint (eqs. 4.2-4.6), VaR (eq. 4.7), CVaR (eq. 4.14) as best convex conservative approximation (pp. 24-26), coherent risk measures (p. 27), mean-CVaR problem (eqs. 4.17-4.19) with almost the same complexity as the expected-value problem (p. 28), equivalence to a worst-case-probability (distributionally robust) problem (eqs. 4.23-4.24, p. 28), critique of variance/standard deviation (pp. 29).
- **Key modelling choices and assumptions:** relatively complete recourse; making any second-stage problem feasible with a penalised slack t (eq. 2.6, p. 10).

## Data / case
- Inventory model numbers only. Exact optimum for uniform demand: E[G(x, D)] = 75 - 0.5x + 0.008x², minimised at x̄ = 31.25 with v = 67.19 (pp. 5-6, 15).

## Key findings
- (p. 4) Newsvendor solution is a quantile x̄ = F^{-1}(κ), κ = (b - c)/(b + h), which can be very different from the mean demand; sample quantiles are less sensitive than the sample mean to data perturbations.
- (p. 6) More scenarios generally give a better approximation of the objective, but not necessarily a better solution; conditional-expectation scenarios give a lower bound (Jensen).
- (p. 9) Typically only the first-stage solution has practical value because the true realisation will differ from the generated scenarios.
- (pp. 9-10) Scenario counts explode: 3 values for each of d = 25 independent components gives 3^25 ≈ 10^12 scenarios.
- (p. 10) Relatively complete recourse defined; infeasibility can be removed by a penalised slack.
- (p. 11) SAA is not an algorithm; the SAA problem still has to be solved.
- (p. 12) Monte Carlo sample averages converge at O_p(N^{-1/2}): one more digit of accuracy needs 100 times more samples. For d ≤ 2 use a grid; for d ≤ 10 quasi-Monte Carlo usually does better. SAA solves the true problem to about 1-2% with manageable samples if: sampling is possible, SAA problems are solvable, relatively complete recourse holds, and second-stage variability is not "too large".
- (p. 13) A tiny-probability infeasible scenario (e.g. p = 10^-6) makes the expected cost infinite yet is practically undetectable by sampling.
- (pp. 13-14) Out-of-sample estimate of a candidate solution's value can use a large independent sample because it only requires solving separate second-stage problems.
- (p. 17) Stagewise independence makes conditional expectations unconditional, so value functions depend only on the physical state; then the DP can be solved accurately by discretisation.
- (p. 18) Discretisation-based DP works with two, three or even four state variables but is out of the question with more than about 10: the curse of dimensionality.
- (p. 19) Multistage scenario trees have N_1 × ... × N_T paths; stochastic programming focuses on the first-stage decision rather than V_t for all states; multistage programs are tractable only in special cases.
- (pp. 21-22) Chance constraints can give non-convex feasible regions (bimodal demand example).
- (p. 26) CVaR is the best possible convex conservative approximation of a chance constraint (following Nemirovski and Shapiro).
- (p. 28) Mean-CVaR has almost the same computational complexity as the risk-neutral problem and is an LP for finite scenarios.
- (p. 29) Variance-based risk control is symmetric, can break convexity, and is not monotone (Example 9).
- (p. 31) Simple one-dimensional examples can mislead intuition in higher dimensions.

## Strengths
- Very clear intuition, small fully worked numbers; authors are central SDDP researchers.
- Statistical gap estimation procedure (UB from out-of-sample evaluation, LB from replicated SAA) is laid out step by step.
- Compact explanation of why CVaR (not variance or VaR) is the natural risk measure in SP.

## Weaknesses / limitations
- Not peer reviewed; 2007, so no SDDP, no Markov-chain uncertainty, no energy application.
- Two-stage focus; multistage treated only through the inventory DP.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3 (Stochastic Optimisation): why optimise expected value (Law of Large Numbers, repeated decisions) | Justification and caveat for one-off decisions | pp. 1-3 |
| Theory 3 (Two-Stage): recourse problem and deterministic equivalent | eqs. 2.1-2.4 | pp. 7-8, Sec. 2 |
| Theory 3: scenario explosion 3^d | Example with d = 25 | pp. 9-10, Sec. 2.1 |
| Theory 3 / Model (Initial Bounds and Feasibility): relatively complete recourse via penalised slack | eq. 2.6 | p. 10 |
| Theory 3: SAA, convergence rate O_p(N^-1/2), when it works | Sec. 2.2 | pp. 10-13 |
| Model (Evaluation on Unseen Weekly Data): CI on policy value from an independent sample | eqs. 2.8-2.9 | pp. 13-14, Sec. 2.3 |
| Theory 3 (Dynamic Programming / SDP): DP equations, stagewise independence reduces state, curse of dimensionality | Sec. 3 | pp. 16-19 |
| Theory 3: definition of policy and non-anticipativity | Sec. 3 | pp. 17-18 |
| Theory/extension: VaR, CVaR, coherent risk, mean-CVaR | Sec. 4 | pp. 22-29 |

## Useful quotes (with page numbers)
> "It is out of the question, however, to use such a discretization approach with more than, say, 10 variables." (p. 18)

## Follow-up references to check (backward snowballing)
- [15] Kleywegt, Shapiro, Homem-de-Mello. The sample average approximation method for stochastic discrete optimization. SIAM J. Optim. 12, 479-502 (listed as 2001 in the tutorial; usually cited as 2002).
- [17] Mak, Morton, Wood (1999). Monte Carlo bounding techniques for determining solution quality in stochastic programs. ORL 24, 47-56.
- [20] Nemirovski and Shapiro. Convex approximations of chance constrained programs. SIAM J. Optim. 17, 969-996 (2006 in the tutorial; Roald et al. cite it as 2007).
- [27] Rockafellar and Uryasev (2000). Optimization of conditional value-at-risk. J. Risk 2, 21-41.
- [2] Artzner, Delbaen, Eber, Heath. Coherent measures of risk.
- [11] Heitsch and Römisch (2003). Scenario reduction algorithms in stochastic programming. COAP 24; [25] Pflug (2001). Scenario tree generation by optimal discretization. Math. Programming B 89.
- [13] Higle and Sen (1996). Stochastic Decomposition (book, Kluwer). The inbox file `HigleSen1991.pdf` is presumably their 1991 paper, a different item.
- [32] Shapiro and Nemirovski. On complexity of stochastic programming problems (book chapter, Springer).

