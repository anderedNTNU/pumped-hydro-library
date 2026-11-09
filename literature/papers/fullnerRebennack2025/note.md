---
bibkey: fullnerRebennack2025
title: "Stochastic Dual Dynamic Programming and Its Variants: A Review"
authors: "Füllner, Christian; Rebennack, Steffen"
year: 2025
venue: "SIAM Review 67(3), 415–539"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, benders-decomposition, multistage-scenario-trees, sdp, risk-averse-cvar, uncertainty-modelling, adp-reinforcement-learning]
review_sections: [modelling-phs-plants, market-participation]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Tutorial review of SDDP: assumptions, cuts, bounds, stopping, convergence and complexity, plus all major variants. Sec. 14.4 (pp. 495–500) is the reference for Markov-chain SDDP: one cut set per Markov state, no cut sharing between states. Explains why prices in the objective require a Markov chain rather than state expansion."
---

# SDDP and its variants: a review (Füllner & Rebennack, 2025)

> **Page numbers:** journal p. = PDF page + 414 (PDF p. 1 = journal p. 415). Text pp. 415–527, references pp. 528–539. The article is open access under CC BY 4.0.
> **Notation:** the review uses cost **minimisation**. In our profit-maximisation model, "lower bound" and "upper bound" swap roles (cuts give an upper approximation of expected profit-to-go).

## Research question / purpose
A tutorial-style review of SDDP (abstract, p. 415). It (i) introduces standard SDDP with a precise list of the assumptions it needs (Assumptions 1–9, pp. 422–425), (ii) analyses convergence and complexity and compares SDDP with SDP and nested Benders decomposition (NBD) (secs. 4–5, pp. 438–444), (iii) covers sampling, stopping criteria and exact upper bounds (secs. 6–8, pp. 444–455), (iv) surveys applications and software (secs. 9–10, pp. 455–461), and (v) reviews extensions that relax each assumption one at a time: continuous uncertainty, risk aversion, unknown distributions, stagewise dependence (including Markov chains), convex and nonconvex/mixed-integer problems, infeasibility, non-block-diagonal structure, infinite and random horizons (secs. 11–20, pp. 461–514). It ends with performance improvements (sec. 21, pp. 514–526) and open research questions (sec. 22, pp. 526–527). Table 1 (p. 421) maps the four parts.

## Setting
- **System:** generic multistage stochastic linear program (MSLP). Applications section 9.1 covers hydrothermal systems: Brazil, Central/South America, Norway, New Zealand (p. 457). PHS is not discussed specifically. Other storage (gas storage, microgrid storage) is mentioned on p. 459, and grid-level storage (batteries, EVs) on p. 460.
- **Markets:** mostly central-planner cost minimisation (p. 455). Market-driven settings with spot-price uncertainty in the objective (p. 459). Strategic (price-maker) bidding (p. 460). Continuous intraday trading [213] (p. 460). Reserve energy and ancillary services in short-term SDDP models [139, 223] (p. 459). Norwegian hydro scheduling with balancing-market / reserve-capacity bids [107, 108] = Helseth et al. (p. 498).
- **Horizon and resolution:** planning hierarchy of short-term dispatch (a few days or weeks), mid-term operational planning (1–2 years) and long-term operational planning (3–5 years) (p. 457). Typical LTOP: 5 years, monthly, 60 stages (pp. 457–458).

## Method
- **Model type:** MSLP over a finite horizon $T$. Stage constraints $T_{t-1}x_{t-1}+W_t x_t=h_t$ (eq. 2.2, p. 424). Dynamic programming equations (DPE) (2.4)–(2.6) with value function $Q_t(x_{t-1},\xi_t)$ and expected value function $\mathcal Q_t(x_t)$, also called "cost-to-go function", "future cost function" or "recourse function" (p. 427).
- **Standard assumptions (pp. 422–425):** (1) finite, deterministic horizon; (2) **stagewise independence**; (3) known distribution; (4) exogenous uncertainty (no decision dependence); (5) finite randomness (finite support, $q_t$ realisations); (6) linearity; (7) only consecutive stages coupled (block-diagonal structure, Fig. 3 p. 426); (8) risk-neutral objective; (9) relatively complete recourse and bounded reachable set.
- **How uncertainty is represented:** standard SDDP uses a recombining scenario tree (scenario lattice) with $|\mathcal S|=\prod_t q_t$ scenarios (p. 423, Fig. 1). The extensions cover AR/PAR/SPAR processes via state expansion (secs. 14.1–14.3), Markov chains (sec. 14.4), hybrid NBD/SDDP (14.5), saddle cuts for objective states (14.6), dual SDDP (14.7), conditional cuts (14.8), SAA for continuous distributions (sec. 11) and distributionally robust or hidden-Markov models (sec. 13).
- **Solution method:** forward pass (simulate the current policy on $|\mathcal K|$ sampled scenarios to get trial points) and backward pass (solve the stage subproblems for all $q_t$ realisations at the trial points and build an expected cut from the dual multipliers) (Alg. 3.1, p. 432; pp. 430–435). Cut gradient $\beta=-\pi^\top T_{t-1}$ from LP duals (p. 434, eq. 3.7 p. 435). Lower bound from the first-stage problem (3.8). Statistical upper bound from the forward-pass sample mean (3.9) (p. 435).
- **Key modelling choices and assumptions:** the value functions are piecewise linear and convex in the state (Thm. 2.8, Cor. 2.9, p. 429). Local (non-state) variables should be kept out of the state vector because complexity grows exponentially in the state dimension (Remark 2.6, p. 428). Cut approximations need an initial valid bound (Remark 3.2, p. 431).

## Data / case
None (a review). The only worked example is the illustrative three-stage LP, Example 3.4 (pp. 436–437; Figs. 5–6). Its multicut continuation is Example 21.2 (pp. 520–521), and its risk-averse version is Fig. 12 (p. 477).

## Key findings
**Mechanics, bounds and convergence**
- (p. 419) SDDP can be viewed as an ADP method and as a sampling-based variant of NBD. NBD is reasonable only up to about four or five time steps. SDDP "comes with the additional prerequisite that the data process is stagewise-independent".
- (p. 435, Lemma 3.3) Cuts are valid, tight at the trial point for the current approximation, and finite in number when built from dual basic solutions. (p. 436) After finitely many steps the polyhedral $\mathcal Q_t$ is represented exactly.
- (pp. 435, 437–438) Standard SDDP gives a valid lower bound (minimisation) but only a **statistical** upper bound. In practice $|\mathcal K|$ is often 1, so the forward-pass estimate is not meaningful. The policy is therefore assessed afterwards by forward simulation with e.g. 1,000 or 10,000 paths, either in-sample or **out-of-sample** (with the true distribution) (p. 438). Remark 3.5 calls this model validation versus model test.
- (pp. 437, 438 Fig. 6) In the example, lower bounds stabilise quickly while the upper-bound estimates oscillate around $v^*$.
- (p. 439, Thm. 4.1) Under Assumptions 1–9 with independent random forward sampling, SDDP converges with probability 1 to an optimal policy in finitely many iterations. The lower bounds converge, but the sample trajectories and sample averages need not. (p. 440) The argument that every scenario is sampled infinitely often "is … almost never applicable to SDDP in practice".
- (p. 440) The number of LPs per iteration is $1+|\mathcal K|\sum_{t\ge2}q_t$, linear in $T$, $|\mathcal K|$ and $q_t$.
- (p. 441, Thm. 4.2) With random sampling, the expected number of iterations is **exponential in $T$ and in the state dimension $n_t$**, and polynomial in $q_t$, $1/\varepsilon$, the Lipschitz constant $L$ and the state-space diameter $D$. Deterministic sampling makes it polynomial or linear in $T$, but the state-dimension dependence cannot be removed.
- (pp. 443–444, Table 3) SDDP needs no state or action discretisation, unlike SDP, but needs stagewise independence (SDP and SDDP: "Markovian uncertainty is possible as well"). It "does not manage to leave the respective worst-case complexity classes" of SDP and NBD (p. 444). It performs well for continuous actions, a medium number of stages and a moderate state dimension (p. 444).
- (p. 443, Remark 5.1) **Cut sharing**: under stagewise independence there is one $\mathcal Q_t$ per stage, so cuts built on one sampled path are valid for all scenarios. The authors note that the term "is sometimes considered to be misleading".

**Stopping criteria (sec. 7, pp. 448–450)**
- (pp. 448–449) Pereira and Pinto's original criterion stops when the lower bound lies inside the confidence interval of the upper-bound estimate, with $\alpha=0.05$ ($z=1.96$).
- (p. 449) Shapiro's critique: this criterion rewards high variance, high confidence levels and small samples, and favours premature stopping. Shapiro instead stops when the **upper end of the CI minus the lower bound** is small.
- (p. 449) Pooling forward-pass values from earlier iterations destroys independence, so the CI is no longer valid [53].
- (pp. 449–450) The hypothesis-test variant controls type I and type II errors (tested with $\delta=0.1$, $\gamma=0.05$ [112]). It remains a heuristic.
- (p. 450) In practice SDDP is stopped after a fixed number of iterations or cuts, after a time limit, or when the lower bound stalls. None of these guarantees optimality. Deterministic stopping needs exact upper bounds (sec. 8).
- (p. 450) "optimally stopping SDDP remains an open challenge".

**Exact upper bounds (sec. 8, pp. 450–455):** inner approximations (convex combinations of value-function points, Lipschitz regularisation; Philpott & de Matos) are costly and loose for many stages. The authors suggest computing them only every few hundred iterations (p. 452). Dual SDDP gives deterministic bounds but each iteration is much more expensive (p. 455).

**Applications (sec. 9, pp. 455–461)**
- (p. 455) Power system optimisation is "by far the dominating application field", with roots in the Brazilian hydrothermal system.
- (p. 457) LTOP balances using water now (no fuel cost) against storing it for drier periods under uncertain inflow. Inflow realisations per stage: typically 20–100. $T=60$ gives about $10^{78}$–$10^{120}$ scenarios. Each forward pass samples 1 or 100–200 scenarios.
- (pp. 457–458) Inflows are modelled with PAR, SPAR or GPAR (log-normal) models. A multiplicative error destroys convexity, so it must be linearised.
- (p. 458) Large systems are aggregated into energy-equivalent reservoirs (EERs) because of the state-dimension complexity.
- (pp. 458–459) **End-of-horizon effect:** the optimal policy empties the reservoirs at the end. The common fix is to add 60 more stages (120 in total) [211], or to use infinite or random horizons (secs. 19–20).
- (p. 459) MTOP: in market-driven systems, **spot prices are uncertain in the objective**. This is stagewise-dependent uncertainty in the objective. For Norway, "a combined SDP/SDDP approach is commonly used" [86, 87, 88, 107, 108].
- (p. 459) The **water head effect** is often ignored in LTOP but matters in MTOP. Production times discharge is nonconvex, so it needs the nonconvex extensions of sec. 16 [38, 110, 170].
- (p. 459) Short-term SDDP models can include reserve energy and ancillary services [139, 223].
- (p. 460) Price-maker bidding gives sawtooth, nonconvex revenue functions (saddle cuts, step functions). SDDP is also applied to continuous intraday trading [213], to investment planning (SDDiP, or SDDP inside a Benders loop with binary first-stage investment [184]), and to the value of water [231] (= Tilmant et al. 2008).
- (p. 461) Software: PSR SDDP (commercial). SDDP.jl is the most comprehensive open-source package: Markov chain SDDP, objective and belief states, cut selection, parallelism, SDDiP, risk and DRO. It requires a finite stochastic process. msppy integrates SAA.

**Continuous uncertainty and policy assessment (sec. 11, pp. 461–467)**
- (p. 463, P.11.4) A policy from the discretised (SAA) problem is feasible for the true process. Its simulated cost under the true process is a valid bound (an upper bound in minimisation).
- (p. 464) The SDDP bounds measure **in-sample** performance only. To judge the policy for the true problem, it must be evaluated **out of sample**. This also allows comparison of policies from different discretisations [52].
- (pp. 464–466) The de Matos–Morton–Finardi procedure gives an upper-bound estimator from $M_u$ i.i.d. out-of-sample paths (11.6–11.7), a lower-bound estimator from several SAA replications (11.8), and a one-sided CI for the optimality gap (p. 466). With one SAA, CIs are overly optimistic if SDDP has not converged (p. 466).
- (pp. 466–467) LHS and RQMC reduce bias and variance compared with plain Monte Carlo, especially for small branch sizes.

**Risk aversion (sec. 12, pp. 467–485)**
- (p. 468) AVaR = CVaR definition (12.5). The usual objective is the convex combination $(1-\lambda)\mathbb E+\lambda\,\mathrm{AVaR}_\alpha$ (12.7).
- (p. 469) Coherence. (p. 470) Multiperiod forms: end-of-horizon, nested, stagewise. (p. 471) Time consistency. AVaR alone is not strictly monotone. The mixture with $\lambda<1$ ensures time consistency (p. 471).
- (p. 474) Nested conditional risk measures are "by far the most frequently chosen" approach. They add a VaR state variable $u_t$ (Shapiro) or extra constraints (Philpott & de Matos) (pp. 474–475), or use a change of probability measure (pp. 475–476). Overview in Table 5 (p. 477).
- (pp. 478–482) In risk-averse SDDP **upper bounds are hard** (no tower property). The options are importance-sampling estimators (Kozmík & Morton), inner approximations, change-of-measure, fixing the iteration count from a risk-neutral run [167], lower-bound stabilisation, and benefit factors [32].
- (pp. 482–483) Entropic risk is conditionally consistent but hard to parametrise. (pp. 483–484) E-AVaR keeps the risk-neutral DPE structure. (pp. 484–485) Biobjective SDDP.

**Stagewise dependence and Markov chains (sec. 14, pp. 490–503)**
- (p. 490) Demand, fuel prices, **electricity prices and inflows** are often correlated over time, so stagewise independence is often inappropriate.
- (pp. 490–492) **State expansion (TS-SDDP):** add $\xi_{t-1}$ (the AR history) as a state variable. By **Thm. 14.3 (p. 491)** the expected value function is jointly convex only if the dependent uncertainty enters the **right-hand side** $h_t$. It is **concave in objective coefficients $c_t$**, i.e. a saddle function. So an AR price model in the objective cannot be handled by plain state expansion. The state dimension grows, and more so for higher lags (p. 492).
- (pp. 492–495) Infanger–Morton scenario-adaptable cut formulas share cuts across histories for linear AR in the RHS (Table 6, p. 494). They mitigate the state-expansion cost only partly.
- (p. 495) For a hydrothermal problem, SDDP solutions are more sensitive to the initial **information state** than to the initial resource state [215].
- (pp. 495–497, sec. 14.4.1) **Markov chain modelling:** $L$ Markov states, transition probabilities $\omega_{\ell\ell'}$. The chain is assumed time-homogeneous only for simplicity, "even though this is not required" (p. 495). The expected value function $\mathcal Q_{t\ell}$ is indexed by the **previous** Markov state and weights the successor states by $\omega_{\ell\ell'}$ (eq. 14.12, p. 496). DPE (14.13).
- (p. 496) Cuts cannot be shared between Markov states, so separate expected value functions must be stored for each state. In return, each one stays convex.
- (pp. 496–497) The process can be represented as a Markovian policy graph [60] (SDDP.jl).
- (p. 497, sec. 14.4.2) Forward pass: sample the Markov state first, then $\xi$ conditionally [168]. Historical inflow–price pairs can be used instead. If a drawn price is not a Markov state, use the closest state [86] or interpolate between the hyperplanes of neighbouring states [88, 237].
- (p. 497) Backward pass: loop over $t$, trial point $k$, Markov state $\ell$ and realisation $j(\ell)$. Cut coefficients are weighted by $\omega_{\ell\ell'}$ (eq. 14.15). Multicut and risk-averse formulas are in [168].
- (p. 497) Challenges: the Markov property may not hold, useful state values and transition probabilities must be defined [88, 150], and cuts are shared only within states. The number of states "should be rather small to preserve computational tractability".
- (p. 498, sec. 14.4.3) Use cases: (a) nonlinear processes approximated by a Markov chain; (b) regime switching; (c) **hybrid SDP/SDDP**, where RHS inflow uncertainty is sampled (cut sharing) and objective price uncertainty is a Markov chain (no sharing across price states). This goes back to Gjelsvik et al. for the Norwegian system [86, 88, 89] and is used for hydrothermal scheduling with balancing-market bids [107, 108], risk management [115, 123, 149] and fuel contracts [39]. Price and inflow are usually assumed independent in that setting.
- (pp. 498–499) (d) **MC-SDDP** proper: the data process itself is approximated by a discrete Markov chain (lattice quantisation [31, 136]). The Markov states enter the subproblems directly and describe the uncertainty completely. MC-SDDP is also called ADDP [137, 138]; state expansion is called TS-SDDP.
- (p. 499) MC-SDDP effort grows **linearly in the number of Markov states** [208]. It needs no linearity and allows dependence in all of $c_t, T_{t-1}, W_t, h_t$. State expansion may be favourable for a moderate state dimension (one value function per stage).
- (p. 499) Main drawback: for a continuous true process, MC-SDDP "policy and lower bounds obtained are not necessarily valid for the true problem" [136]. Löhndorf & Shapiro nevertheless report tighter bounds and better policies, even on the true process. They conjecture this is because state expansion adds state variables that the policy does not control, which leads to poorer exploration (pp. 499–500).
- (p. 500) Hybrid NBD/SDDP: the "complicating" uncertainty becomes a scenario tree. Markov approaches allow dependence between processes. With one realisation per Markov state, the number of LPs per iteration equals standard SDDP.
- (pp. 500–502) Saddle cuts for AR price "objective states" (Downward et al. [59]) need a Lipschitz bound $\nu$. If it is too small the cuts are invalid; if too large they are weak.
- (p. 502) Dual SDDP for objective uncertainty. (pp. 502–503) Conditional cuts (van Ackooij & Warin) are not guaranteed valid.

**Nonconvexity, feasibility, horizon (secs. 15–20)**
- (pp. 503–506) Convex SDDP: Lagrangian cuts, almost-sure asymptotic convergence.
- (pp. 506–510) Mixed-integer or nonconvex problems (e.g. head effects, unit commitment): convex relaxation (simulate with the true nonconvex model afterwards, p. 506), Lagrangian cuts, MIDAS step functions, SDDiP (binary states, exact), SLDP, nonconvex Lipschitz cuts, scaled cuts.
- (pp. 510–512) Infeasibility: feasibility cuts (rarely used, since they do not prevent infeasibility in simulation, p. 511), penalisation via slack variables (e.g. load shedding; penalty choice can distort value functions, p. 512), Lipschitz regularisation.
- (p. 512) Infinite horizon with discount factor $\delta<1$. (p. 513) B2. **Periodic SDDP** [210]: a 60-month problem reduced to 13 stages. It also mitigates the end-of-horizon effect. Cyclic policy graphs [60]. (pp. 513–514) A random horizon becomes a two-state Markov chain.

**Performance (sec. 21, pp. 514–526)**
- (p. 514) Ávila et al. report lower bounds stalling at about a 22% gap for large state spaces.
- (pp. 515–516) Cut selection: level-1 dominance about 10 times faster with no significant loss in policy quality [53]; limited-memory level 1 is better [8].
- (p. 516) $|\mathcal K|=1$ forward samples, scenario incrementation. ReSa, AND (pp. 516–517). CUPPS, DOASA (p. 517). Inexact cuts (pp. 517–519).
- (p. 520) **Multicut SDDP** keeps one cut set per realisation and takes the expectation in the objective. It has the same convergence properties, fewer iterations but larger LPs, and is best when $q_t$ is moderate.
- (pp. 521–522) Experience replay / batch learning. (pp. 522–524) Regularisation (quadratic, level bundle, nonconvex MCP, Chebyshev centres). (pp. 524–526) Parallelisation by scenario or by node. (p. 526) Aggregation of realisations into clusters gives valid coarse cuts by Jensen's inequality (when $W_t, c_t$ are deterministic).

**Outlook (pp. 526–527):** open problems are stopping, upper bounds in risk-averse SDDP, DRO, nonconvex extensions, regularisation, reinforcement-learning techniques and decision-dependent uncertainty.

## Strengths
- The most complete and recent single reference on SDDP, with explicit assumptions and a pointer to the section that relaxes each one. Very useful for justifying each modelling assumption.
- Clear, citable statements on the bounds (statistical versus deterministic), stopping and in-sample versus out-of-sample assessment.
- The Markov-chain section explicitly contrasts MC-SDDP with TS-SDDP and hybrid SDP/SDDP, with the Norwegian price-plus-inflow lineage (Gjelsvik, Helseth).
- Open access (CC BY 4.0) and recent (accepted 2024, published 2025).

## Weaknesses / limitations
- No numerical comparisons of its own. The performance claims are second-hand from the cited studies.
- Hydro applications are surveyed briefly and from a central-planner perspective. There is nothing specific on pumped storage, price-taker merchant storage, reserve co-optimisation or storage sizing.
- No guidance on *how* to build the Markov chain (clustering, number of states, estimating transitions). It only says this must be done and that the number of states should be small (p. 497), and points to lattice quantisation [31, 136] (p. 499).
- Water values are not discussed explicitly as cut slopes. The review only derives the cut gradient from LP duals (p. 434). Reading the cut slope as the marginal water value is our interpretation.
- Typo in Outlook item 7 (p. 527): it says "stagewise-dependent" where "decision-dependent" is meant (cf. Assumption 4, p. 422).
- Some extracted text lines are missing from `paper.txt` page breaks, but the content was recoverable.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: what SDDP is, origin (Pereira & Pinto 1991), Brazil | Intro, history, hydrothermal motivation | pp. 418–420, sec. 1 |
| Theory: SDDP as ADP / sampling variant of NBD | Two research streams (SDP and stochastic programming) | p. 419; sec. 5, pp. 441–444 |
| Theory: curse of dimensionality of SDP; SDDP avoids state discretisation | SDP needs discretised state, action and noise spaces; SDDP uses cuts at trial points | pp. 419, 429, 441–442; Table 3 p. 444 |
| Theory: "breaking the curse of dimensionality" is overstated | SDDP does not leave the worst-case complexity classes | pp. 420, 444 |
| Theory: list of SDDP assumptions (stagewise independence, finite randomness, linearity, risk neutrality, relatively complete recourse) | Assumptions 1–9 | pp. 422–425, sec. 2 |
| Theory: recombining scenario tree / lattice, number of scenarios $\prod q_t$ | Definition and Fig. 1 | p. 423 |
| Theory: Bellman equation, (expected) value function, cost-to-go / future cost function terminology | DPE (2.4)–(2.6) | p. 427, sec. 2.4 |
| Theory: value functions are piecewise linear and convex in the state (so cuts work) | Thm. 2.8, Cor. 2.9–2.10 (Lipschitz) | p. 429 |
| Model: only end-of-week volume as state; hourly decisions local | Remark 2.6: keep local variables out of the state, since complexity is exponential in state dimension | p. 428 |
| Model: epigraph LP formulation of the subproblem with cuts ($\theta$ / $\alpha$ variable) | Eq. (2.12) | p. 430 |
| Theory / Model: forward and backward pass | Sec. 3, Alg. 3.1, Fig. 4 | pp. 430–435 |
| Model: initial bound on future value before cuts ($\alpha\le\overline M$) | Remark 3.2, three initialisation strategies | p. 431 |
| Theory: cut intercept and gradient; expected cut over realisations | Eqs. (3.2)–(3.5) | pp. 433–434 |
| Theory / Model: cut slope from LP duals (basis for water values as cut slopes; interpretation is ours) | $\beta=-\pi^\top T_{t-1}$; finitely many dual extreme points | p. 434, eq. (3.7) p. 435 |
| Theory: cuts valid, tight and finite | Lemma 3.3 | pp. 435–436 |
| Theory 3.6: SDDP bounds (deterministic first-stage bound, statistical simulated bound) | Sec. 3.4, eqs. (3.8)–(3.9) | p. 435 |
| Theory: illustrative example of bounds converging | Example 3.4, Fig. 6 (lower bounds stabilise, estimates oscillate) | pp. 436–438 |
| Method: policy assessment by large forward simulation, in-sample vs out-of-sample | Sec. 3.7, e.g. 1,000 or 10,000 paths; Remark 3.5 validation vs test | pp. 437–438 |
| Method: out-of-sample evaluation needed because SDDP bounds are in-sample only | Sec. 11.2 | p. 464 |
| Method: confidence intervals for policy value and optimality gap | de Matos–Morton–Finardi estimators (11.6)–(11.8), CIs | pp. 465–466 |
| Theory: convergence of SDDP (almost-sure finite) | Thm. 4.1 and the caveat on sampling every scenario | pp. 438–440 |
| Theory: complexity, exponential in $T$ and state dimension | Thm. 4.2 | pp. 440–441 |
| Theory: LPs per iteration grow linearly in $T$, $|\mathcal K|$, $q_t$ | Cost per iteration | p. 440 |
| Theory: comparison SDDP vs SDP vs NBD vs deterministic equivalent | Table 3 | p. 444 |
| Theory: cut sharing under stagewise independence | Remark 5.1 | p. 443 |
| Method: benchmark "stagewise-independent uncertainty" | Assumption 2 and its role; cut sharing; why dependence matters | pp. 422, 443, 490 |
| Method: forward sampling choices ($|\mathcal K|$, MC, LHS, QMC, importance sampling) | Sec. 6; sec. 21.1.2 | pp. 444–448; p. 516 |
| Method: stopping criterion (bound minus confidence limit, iteration cap) | Pereira–Pinto CI rule and its flaws; Shapiro's conservative rule; practical rules | pp. 448–450, sec. 7 |
| Method: repeated stopping checks / pooling iterations break CI validity | Pooling destroys independence; no test guarantees bounded premature-stopping probability | pp. 449–450 |
| Method: "optimal stopping is open" caveat | Sec. 7 conclusion, Outlook item 1 | pp. 450, 526–527 |
| Theory: deterministic upper bounds (inner approximation, dual SDDP) | Sec. 8 | pp. 450–455 |
| Literature review: SDDP dominant in power and hydro scheduling | Sec. 9.1 | pp. 455–457 |
| Background / lit review: planning hierarchy (short, medium, long term) | Time scales | p. 457 |
| Lit review: SDDP for Norway | Røtting & Gjelsvik [194], Gjelsvik et al. [87] | p. 457 |
| Lit review: typical LTOP size (monthly, 60 stages, 20–100 inflow realisations) | Numbers | pp. 457–458 |
| Model / uncertainty: inflow PAR/SPAR/GPAR models, why log-normal breaks convexity | Inflow modelling | pp. 457–458 |
| Model: end-of-horizon effect and extended horizon | Add 60 stages (120 in total) [211]; periodic SDDP; infinite horizon with discount | pp. 458–459; p. 512–513 (secs. 19) |
| Model: discount factor | Infinite-horizon problems need $\delta<1$ | p. 512 |
| Lit review: price uncertainty in market-driven hydro scheduling; Norwegian SDP/SDDP | MTOP paragraph | p. 459; p. 498 |
| Lit review: reserve / balancing markets with SDDP (Helseth et al. = `helseth2016`) | Cited as applications of hybrid SDP/SDDP | pp. 459, 498 |
| Model assumption: no head effects (linear) and why | Head effect makes the problem nonconvex; needs sec. 16 methods (SDDiP [110] = `hjelmeland2019tste`) | p. 459; pp. 506–510 |
| Lit review: price-maker bidding is nonconvex (justifies price-taker assumption) | Sawtooth revenue functions | p. 460 |
| Lit review: intraday trading with SDDP | [213] | p. 460 |
| Lit review: investment / sizing with SDDP (binary first stage + SDDP) | Investment planning paragraph | p. 460 |
| Lit review: storage other than hydro (gas, microgrids, batteries) | Different storage systems | pp. 459–460 |
| Theory: water values via SDDP (Tilmant et al. 2008 = `tilmant2008`) | Listed as an SDDP use | p. 460 |
| Method / software: SDDP.jl features (Markov chain, policy graph, objective states) | Sec. 10 | p. 461 |
| Theory: SAA for continuous distributions; policy from discretised model is feasible for the true process | Sec. 11.1, P.11.1–P.11.5 | pp. 462–464 |
| Theory: risk measures (VaR, CVaR/AVaR, $\mathbb E$–AVaR mix, coherence) | Sec. 12.1 | pp. 467–470 |
| Theory: nested vs end-of-horizon risk, time consistency | Secs. 12.1.2–12.1.3, Fig. 11 | pp. 470–472 |
| Extension / future work: risk-averse SDDP formulations | Table 5; DPE reformulations | pp. 473–477 |
| Future work: upper bounds and stopping in risk-averse SDDP are hard | Sec. 12.3.3 | pp. 478–482 |
| Future work: distributionally robust SDDP | Sec. 13.1 | pp. 485–489 |
| Theory: stagewise dependence of prices and inflow is common | Sec. 14 intro | p. 490 |
| Theory: TS-SDDP / state expansion with AR | Sec. 14.1, eqs. (14.1)–(14.3) | pp. 490–492 |
| **Model choice: why Markov chain and not AR for prices** | Thm. 14.3: convexity only for RHS dependence; concave in objective coefficients (saddle) | p. 491; p. 495; p. 500 |
| Theory: state expansion increases dimension (worse with lags) | Sec. 14.1 end | p. 492 |
| Theory: Infanger–Morton cut sharing with AR | Sec. 14.2, Table 6 | pp. 492–495 |
| Theory: SDDP solutions sensitive to information state | [215] | p. 495 |
| **Theory 03_theory "Markov Representation": MC-SDDP modelling** | Markov states, transition probabilities, conditional expected value function (14.12), DPE (14.13), Fig. 13 | pp. 495–497, sec. 14.4.1 |
| **Model: one cut set per Markov state, no sharing between states** | Separate expected value functions per state | p. 496; p. 497 |
| Model: time-inhomogeneous (week-dependent) transition matrix is allowed | "even though this is not required" | p. 495 |
| Method: forward-pass sampling of Markov state, then realisation | Sec. 14.4.2 | p. 497 |
| **Method: mapping unseen data to a Markov state (nearest state, or interpolation)** | Closest state [86]; interpolation between neighbouring hyperplanes [88, 237] | p. 497 |
| **Model: backward pass over all Markov states; transition-weighted cuts** | Loop over $t,k,\ell,j(\ell)$; eq. (14.15) | p. 497 |
| Model: our multicut-over-states form vs aggregated cut | Multicut SDDP; multicut Markov formulas in [168] | p. 520; p. 497 |
| **Method: keep the number of Markov states small; states and transitions must be chosen** | Challenges of MC-SDDP | p. 497 |
| Lit review: hybrid SDP/SDDP (Gjelsvik, Norwegian system, balancing markets, risk) | Use case (c) | p. 498 |
| Theory: MC-SDDP vs TS-SDDP (definitions, cost, when to prefer which) | Use case (d) | pp. 498–500 |
| Theory: MC-SDDP effort linear in number of states | [208] | p. 499 |
| **Method caveat: training bounds not valid for the true process; need out-of-sample test** | [136]; Löhndorf & Shapiro find better policies anyway | p. 499–500 |
| Theory: Markov chain built by lattice quantisation | [31, 136] | p. 499 |
| Theory: hybrid NBD/SDDP | Sec. 14.5 | p. 500 |
| Theory: objective states and saddle cuts (alternative for AR prices) | Sec. 14.6 | pp. 500–502 |
| Theory: hidden Markov / belief states | Sec. 13.2 | pp. 489–490 |
| Model: guaranteeing feasibility (relatively complete recourse; idle/spill solution; slack penalties) | Assumption 9; sec. 17 | p. 425; pp. 510–512 |
| Future work: integer variables (unit commitment, start-ups), nonconvex efficiency | Sec. 16 (SDDiP, Lagrangian cuts, MIDAS) | pp. 506–510 |
| Method: convex relaxation in training, true model in simulation | Convexification paragraph | p. 506 |
| Method: computational speed-ups (cut selection, multicut, parallelisation) | Sec. 21 | pp. 514–526 |
| Method: aggregating realisations into clusters gives valid coarse cuts | Sec. 21.4 | p. 526 |
| Discussion / future work: open SDDP problems | Outlook | pp. 526–527 |

## Useful quotes (with page numbers)
> "the number of Markov states should be rather small to preserve computational tractability." (p. 497)

> "cuts cannot be shared between Markov states, but only within them" (p. 497)

> "the policy and lower bounds obtained are not necessarily valid for the true problem" (p. 499, on MC-SDDP)

> "optimally stopping SDDP remains an open challenge." (p. 450)

> "By far the dominating application field of SDDP is power system optimization" (p. 455)

## Follow-up references to check (backward snowballing)
Keys in brackets are existing keys in `references.bib`.
- [136] Löhndorf & Shapiro 2019, *Modeling time-dependent randomness in SDDP*, EJOR. MC-SDDP vs TS-SDDP [`lohndorf2019`].
- [138] Löhndorf, Wozabal & Minner 2013, ADDP for hydro storage trading, Oper. Res. [`lohndorf2013`].
- [86] Gjelsvik, Belsnes & Haugstad 1999: SDP/SDDP under spot-price uncertainty, closest-state mapping [`gjelsvik1999`].
- [88] Gjelsvik, Mo & Haugstad 2010, Handbook of Power Systems I, pp. 33–55 [`gjelsvik2010`].
- [150] Mo, Gjelsvik, Grundt & Kåresen 2001: price modelling for the Markov states [`mo2001`].
- [107] Helseth, Fodstad & Mo 2016: energy and reserve capacity markets [`helseth2016`]. [108] Helseth et al. 2015, PowerTech: co-optimising energy and capacity sales.
- [110] Hjelmeland, Zou, Helseth & Ahmed 2019: nonconvex MTHS by SDDiP [`hjelmeland2019tste`].
- [106] Helseth & Braaten 2015: parallel SDDP for hydropower, Energies.
- [167] Philpott & de Matos 2012 [`philpott2012`]. [168] Philpott, de Matos & Finardi 2013: coherent risk with Markov-chain SDDP, multicut formulas.
- [171] Philpott & Guan 2008: convergence [`philpott2008`]. [205] Shapiro 2011 [`shapiro2011`]. [211] Shapiro et al. 2013: risk-neutral and risk-averse SDDP, 120-stage horizon.
- [210] Shapiro & Ding 2020: periodic SDDP, end-of-horizon [`shapiro2020`].
- [60] Dowson 2020: policy graph [`dowson2020`]. [61] Dowson & Kapelevich: SDDP.jl.
- [52] de Matos, Morton & Finardi 2017: assessing policy quality. [112] Homem-de-Mello et al. 2011: sampling and stopping.
- [6] Ávila, Papavasiliou & Löhndorf 2024: batch learning SDDP, parallelisation.
- [215] Soares, Street & Valladão 2017: solution variability.
- [231] Tilmant, Pinte & Goor 2008: marginal water values [`tilmant2008`].
- [213] Shinde et al. 2022: SDDP for continuous intraday trading.
- [194] Røtting & Gjelsvik 1992: SDDP for Norwegian seasonal scheduling.

