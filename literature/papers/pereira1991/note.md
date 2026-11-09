---
bibkey: pereira1991
title: "Multi-stage stochastic optimization applied to energy planning"
authors: "M. V. F. Pereira, L. M. V. G. Pinto"
year: 1991
venue: "Mathematical Programming 52, 359-375"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, benders-decomposition, sdp, dynamic-programming]
review_sections: [modelling-phs-plants]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Original SDDP paper: approximates SDP expected-cost-to-go functions by piecewise-linear Benders cuts from stage duals, with forward Monte Carlo simulation, backward cut generation and LB/UB convergence test; 39-reservoir Brazilian hydrothermal case."
---

# SDDP: multi-stage stochastic optimization for energy planning (Pereira and Pinto, 1991)

_Page mapping: PDF page n = journal page 358 + n (journal pp. 359-375)._

_Tagging note: the paper is the parent of both SDDP families. It is tagged `sddp-markov-chain` because it is the base algorithm of our MC-SDDP, and `sddp-time-series` because its hydro formulation puts lagged inflows ("hydrologic trend") in the state (p. 370). The algorithm itself, as presented, assumes stagewise-independent right-hand sides (p. 367), and the case study uses independent inflows (p. 372). Neither a Markov chain nor a PAR model is implemented._

## Research question / purpose
- Present a method for multistage stochastic (linear) optimisation that avoids the state discretisation and "curse of dimensionality" of stochastic dynamic programming (SDP), by approximating the expected-cost-to-go functions with piecewise-linear functions built from LP duals (Benders cuts) (p. 359).
- Name the method stochastic dual dynamic programming (SDDP) and illustrate it on optimal stochastic scheduling of a 39-reservoir hydrothermal system (p. 359, Sec. 5, pp. 369-374).
- Described by the authors as a "technical note" (p. 359); it is an algorithm paper with a short case study, no convergence proof.

## Setting
- **System:** hydrothermal generating system; case study of 39 hydro plants (22 with reservoirs, 17 run-of-river) from the southern-southeastern Brazilian power pool, plus one aggregate thermal unit (p. 372). Not pumped storage.
- **Markets:** none. Centralised cost minimisation: thermal fuel cost plus penalty for load curtailment (deficit modelled as dummy thermal plants) to meet demand (pp. 369, 371).
- **Horizon and resolution:** 10 stages in the case study (p. 372). Units are MW-month and the hydrologic trend is "lateral inflow in the previous month" (p. 372), so stages appear to be monthly (stage length not stated explicitly; (unverified)). No intra-stage time resolution.

## Method
- **Model type:** multistage stochastic linear program, written as an SDP recursion (28a-d) with discount factor beta, state transition = water balance, bounds on storage and outflows (pp. 370-372).
- **How uncertainty is represented:** right-hand-side vectors b_t (inflows) are independent random variables across stages, each discretised into m scenarios with probabilities p_tj (p. 367). General formulation conditions the inflow distribution on the state, and the state may include previous inflows, x_t = [v_t, a_{t-1}, a_{t-2}, ...] (p. 370, eq. 29). Case study: independent inflows, 2 realisations per stage, first-stage inflow known, so 2^9 = 512 inflow sequences (p. 372).
- **Solution method:**
  - *Deterministic two-stage DDP (Sec. 2, pp. 359-365).* Future cost function alpha_1(x_1) = min c_2 x_2 s.t. A_2 x_2 >= b_2 - E_1 x_1 (eq. 4, p. 360). By LP duality it equals max over the dual vertices pi^i of pi^i (b_2 - E_1 x_1), so it is piecewise linear in x_1 (eqs. 5-7, pp. 361-362, Fig. 3). Solving the second stage at trial points gives multipliers that are vertices of the dual polyhedron and hence supporting hyperplanes; a subset of them gives a lower approximation (eqs. 8-9, p. 363). Lower bound from the approximate first-stage problem (eq. 12, p. 363), upper bound from evaluating the second stage at the first-stage solution (eq. 13, p. 364). Trial points = previous optimal first-stage solution, i.e. cuts are built near "interesting" points (p. 364). Two-stage algorithm steps (a)-(f) (p. 364).
  - *Equivalence:* the two-stage DDP is a Benders decomposition with LP master and subproblem; multistage and stochastic extensions are extensions of Benders (citing Birge 1980, Wets 1988) (p. 365).
  - *Multistage deterministic DDP* (p. 365): forward simulation t = 2..T with current approximations (eq. 15), upper bound as sum of stage costs (eq. 16), backward recursion t = T..2 solving stage problems at the forward trial states (eq. 17), multipliers give a new supporting hyperplane for stage t-1 (step g).
  - *SDDP (Sec. 3, pp. 366-368).* Two-stage stochastic problem with m second-stage subproblems (eqs. 18-19); expected future cost = probability-weighted sum (eq. 20, p. 366). Backward recursion: for each stage, each trial state and each scenario b_tj solve the stage LP (eq. 22), take the expected multiplier pi-bar = sum_j p_tj pi_tj and add one cut for the expected future cost function of stage t-1 (p. 367). Forward pass: a full enumeration of scenario combinations grows exponentially, so a Monte Carlo forward simulation over a sample of n scenarios generates trial states (eq. 23, pp. 367-368).
  - *Bounds and stopping (p. 368):* lower bound from the first-stage problem; upper bound estimated as first-stage cost plus mean of n simulated total costs (eqs. 24-25); standard deviation of the estimator (eq. 26); 95% CI [z-bar - 2 sigma, z-bar + 2 sigma] (eq. 27); stop when the lower bound lies inside this interval.
  - *Extensions (pp. 368-369):* iterate forward/backward over a subset of stages without returning to stage 1; parallel forward samples and backward subproblems, possibly asynchronous (conjecture); nonlinear case possible, with global optimality only under convexity.
- **Key modelling choices and assumptions:**
  - State = reservoir storage plus hydrologic trend (previous inflows) (p. 370, eq. 29). Decisions = turbined outflow q_t and spillage s_t (p. 370, eq. 30).
  - Immediate cost = thermal cost to complement hydro, with deficits as dummy thermal plants; multi-subsystem energy balance with interchanges and capacities (eq. 31, p. 371).
  - Production coefficient rho_i is in reality a function of initial volume, end volume, outflow and spillage, i.e. head-dependent (eq. 32), but it is **assumed constant** in the derivations (p. 371). The authors note the true objective is nonlinear because of outflow times head and nonseparable because hydro energy is valued through expected fuel savings (pp. 369-370).
  - Water balance v_{t+1} = v_t + a_t + M(q_t + s_t), with M the plant incidence matrix (eq. 33, p. 371); storage upper bounds (eq. 34, p. 371); turbine upper bounds and minimum total outflow (eqs. 35-36, p. 372).
  - Discount factor beta in the recursion (p. 370). No explicit end-of-horizon value is described (the recursion has no terminal value term; (unverified) beyond what eq. 28 shows).

## Data / case
- 39 hydro plants (22 reservoirs, 17 run-of-river), southern-southeastern Brazil; data in Pereira and Pinto (1985) (p. 372).
- Initial storage 50% of capacity; aggregate thermal unit 10,000 MW; thermal cost $1/MW-month; curtailment cost $10/MW-month; demand 29,300 MW-month per stage; 10 stages (p. 372).
- Inflows independent, 2 realisations per stage, first stage known: 512 sequences (p. 372).
- Each stage subproblem: 102 variables, 40 constraints (excluding bounds and cuts) (p. 372). Full deterministic equivalent: 522,240 variables and 204,800 constraints; 1,023 distinct subproblems after removing duplicates (104,346 variables / 40,920 constraints) (p. 373).
- Stage LPs solved with a network-flow basis-partitioning algorithm (Kennington and Helgason 1984), exploiting that water balance, storage and outflow bounds form a network; power balance and cuts are side constraints (p. 373).
- Forward sample of 50 inflow sequences per iteration (p. 373).

## Key findings
- (p. 359) Future cost functions of SDP can be approximated by piecewise-linear functions from stage-problem duals; no state discretisation is needed, so the curse of dimensionality is avoided; suitable for parallel processing.
- (p. 361) DP needs discretised states; with 10 state components at 4 values each there are over a million states; SDP is typically limited to 3-4 state variables.
- (pp. 362-363) The future cost function of an LP is exactly piecewise linear (max over dual vertices); cuts from dual multipliers at trial points are supporting hyperplanes, and a subset of them gives a lower bound.
- (pp. 363-364) Lower bound from approximate first-stage problem, upper bound from evaluating the true second stage at the first-stage solution; the gap measures predicted vs. actual future cost.
- (p. 365) Attractive features: no discretisation, bounds at every iteration, warm start (successive problems differ by one constraint). Two-stage DDP equals Benders decomposition.
- (p. 367) Backward step uses the probability-weighted average of scenario multipliers to form one cut for the expected future cost function.
- (pp. 367-368) Forward pass uses Monte Carlo sampling because enumerating all scenario combinations grows exponentially with stages.
- (p. 368) Upper bound is a Monte Carlo estimate; its standard deviation defines a 95% CI; stopping rule: lower bound inside the CI. (This rule is later criticised by Shapiro 2011, pp. 65, 67.)
- (p. 369) Convergence to the global optimum in the nonlinear case only under convexity.
- (p. 372) Curse of dimensionality illustration: state = [storage, previous-month inflow] per reservoir, 20 intervals each, gives 20^(2n) states: 400 for 1 reservoir, 160 thousand for 2, 64 million for 3, 25 billion for 4, 10 trillion for 5.
- (pp. 373-374) Case converged in five iterations (one iteration = one forward simulation + one backward recursion); Fig. 5 shows LB/UB, Fig. 6 shows the gap against the standard deviation of the UB estimate; 37 CPU minutes on a VAX 11/780 (about 1.5 minutes on an IBM 3090).

## Strengths
- Clear, didactic derivation from two-stage deterministic LP to multistage stochastic case; the geometric argument (future cost = max over dual vertices) is the cleanest textbook source for why cuts are valid lower approximations.
- Gives the full algorithmic skeleton still used today: forward Monte Carlo pass, backward cut pass with probability-weighted duals, deterministic LB and statistical UB.
- Explicit hydro formulation (state, decisions, water balance, bounds), and an explicit statement of the curse of dimensionality with numbers.
- Notes parallelisation and the network structure of hydro stage problems.

## Weaknesses / limitations
- No convergence proof; convergence is only demonstrated empirically on one small case (5 iterations).
- Stopping criterion (LB inside UB confidence interval) is statistically weak; Shapiro (2011, p. 65 Remark 1, p. 67 Remark 4) shows it can stop arbitrarily early if the confidence level is raised.
- Uncertainty limited to independent RHS (inflows) in the algorithm (p. 367); serial correlation only mentioned through the state definition (p. 370), not implemented. No price uncertainty, no Markov chain.
- Constant production coefficient (no head effects) (p. 371); no pumping, no markets, cost-minimising central planner.
- Minor typos in the paper: on p. 364 the stopping sentence is inverted ("If this difference is greater than a given tolerance, the problem is solved"); on p. 373 the upper bound is referred to as "equation (20)" whereas it is eq. (16)/(24).

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: DP future cost function / backward recursion | Two-stage DP, immediate vs future cost, future cost as function of state; SDP recursion t = T..1 | pp. 360-361 (eqs. 3-4); p. 370 (eq. 28) |
| Theory: curse of dimensionality | 4^10 example; SDP limited to 3-4 state variables; 20^(2n) table for reservoirs | p. 361; p. 372 (Sec. 5.8) |
| Theory: why cuts are valid (future cost is piecewise linear, max over dual vertices) | LP duality argument, Fig. 3 | pp. 361-363 (eqs. 5-9) |
| Theory: cuts are lower approximations; LB and UB | Approximate future cost is a lower bound; LB eq. 12, UB eq. 13 | pp. 363-364 |
| Theory: Benders decomposition link | Two-stage DDP = Benders with LP master and subproblem | p. 365 |
| Theory: multistage forward/backward passes | Deterministic multistage DDP steps (a)-(g) | p. 365 |
| Theory: SDDP backward pass with expected cuts | Per-scenario solve, probability-weighted multiplier, one cut per trial state | pp. 366-367 (eqs. 18-22) |
| Theory: SDDP forward Monte Carlo pass | Sampling instead of enumerating scenario combinations | pp. 367-368 (eq. 23) |
| Theory: statistical upper bound and stopping rule (original) | UB estimate, std, 95% CI, LB-in-CI rule | p. 368 (eqs. 24-27) |
| Theory: parallelisation | Independent forward samples and backward subproblems | p. 369 (Sec. 4.2) |
| Theory: convexity needed for global optimality | Nonlinear extension only under convexity | p. 369 (Sec. 4.3) |
| Model: state variables (storage + hydrologic trend) | x_t = [v_t, a_{t-1}, ...] | p. 370 (Sec. 5.3, eq. 29) |
| Model: water balance with spillage | v_{t+1} = v_t + a_t + M(q_t + s_t) | p. 371 (eq. 33) |
| Model: constant production coefficient assumption / head effects | rho depends on volumes and outflow but assumed constant | p. 371 (eq. 32); pp. 369-370 |
| Model: storage and outflow bounds | Eqs. 34-36 | pp. 371-372 |
| Background/Theory: hydro scheduling trade-off (deplete vs. spill) | Verbal description of the intertemporal trade-off in reservoir operation | p. 369 (Sec. 5.1) |
| Literature review (modelling-phs-plants): origin of SDDP for hydro scheduling | 39-reservoir Brazilian case, 10 stages, 5 iterations | pp. 372-374 |

## Useful quotes (with page numbers)
> "No state discretization is necessary" (p. 359, abstract)

Other key statements, paraphrased (not quoted): approximate future cost from a subset of hyperplanes is a lower bound (p. 363); two-stage DDP is equivalent to Benders decomposition with LP master and subproblem (p. 365); stop when the lower bound is inside the UB confidence interval (p. 368).

## Follow-up references to check (backward snowballing)
- Pereira, M.V.F. and Pinto, L.M.V.G. (1985). Stochastic optimization of a multireservoir hydroelectric system: a decomposition approach. Water Resources Research 21(6). (System data and earlier decomposition approach.)
- Benders, J.F. (1962). Partitioning procedures for solving mixed-variables programming problems. Numerische Mathematik 4, 238-252. (In repo: `benders1962`.)
- Birge, J.R. (1980). Solution methods for stochastic dynamic linear programs. Stanford SOL Report 80/29. (Nested decomposition.)
- Wets, R.J.-B. (1988). Large scale linear programming techniques. In Ermoliev and Wets (eds.), Numerical Methods for Stochastic Optimization.
- Gal, S. (1989). Parameter iteration dynamic programming. Management Science. (Polynomial approximation of future cost.)
- Kennington, J.L. and Helgason, R.V. (1984). Algorithms for Network Programming. Wiley.

