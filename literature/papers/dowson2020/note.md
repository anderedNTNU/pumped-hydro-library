---
bibkey: dowson2020
title: "The policy graph decomposition of multistage stochastic programming problems"
authors: "Oscar Dowson"
year: 2020
venue: "Networks 76(1), 3-23"
peer_reviewed: true
methods: [sddp-markov-chain, risk-averse-cvar, multistage-scenario-trees]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/dowson2020.pdf"
takeaway: "Introduces the policy graph (nodes = subproblems, arcs = Markov transitions) as a unifying notation for multistage stochastic programs; a Markovian policy graph is exactly MC-SDDP's structure; extends SDDP to cyclic (infinite-horizon, discounted) graphs and shows a 52-week finite-horizon model suffers end-of-horizon effects that an infinite-horizon cycle removes; implemented in SDDP.jl."
---

# The policy graph decomposition (Dowson, 2020)

_Version filed: author/archive manuscript from Optimization Online (2018/11, 29 pages), not the publisher's typeset version. **All page numbers below are manuscript (= PDF) pages**, printed in the header as "DOWSON n". Journal pages are 3-23; no exact mapping is possible (journal version is shorter). Cite sections when page precision matters._

_Tagging note: `sddp-markov-chain` because the "Markovian policy graph" (Sec. 3.1, pp. 9-10) is the formal structure of our MC-SDDP and the algorithm of Sec. 4 solves it. `risk-averse-cvar` for the nested coherent risk measures (Sec. 3.3, pp. 11-13). `multistage-scenario-trees` because the paper shows scenario trees are a special case of policy graphs (pp. 8-9). No review section: the only application is dairy farming._

## Research question / purpose
- Give practitioners a structured, unambiguous way to formulate multistage stochastic programs (the "policy graph"), whose nodes give a natural decomposition and whose arcs carry information flow through time (p. 1).
- Extend SDDP to solve a subset of policy-graph problems that includes discrete-time, convex, **infinite-horizon** problems with continuous states and controls (pp. 1-2).
- Demonstrate on an existing dairy-farm model (POWDer) that a finite-horizon formulation suffers from end-of-horizon effects that the infinite-horizon formulation removes (p. 1, Sec. 5).

## Setting
- **System:** generic; example is a pastoral dairy farm (New Zealand), not energy.
- **Markets:** n/a (the milk price is the Markov state in the example).
- **Horizon and resolution:** example has 52 weekly stages, either finite horizon or a cycle (end of week 52 = start of week 1) with discount factor 0.95 (pp. 23-24).

## Method
- **Model type:** convex (LP) multistage stochastic programming in stochastic-optimal-control language (stage, state, control, transition function, stage objective, decision rule), not scenario-tree/filtration language (p. 2, Sec. 2.1, pp. 2-3).
- **Building blocks** (Sec. 2.2, pp. 3-5):
  - *Node*: incoming/outgoing state, noise, controls, transition function, stage objective, decision rule (p. 3).
  - *Hazard-Decision* node: control chosen after observing the noise; *Decision-Hazard*: before (p. 4). A Decision-Hazard node can be rewritten as a deterministic node followed by a Hazard-Decision node with an expanded state (Fig. 3, pp. 4-5).
- **Policy graph** (Sec. 3, pp. 6-8): tuple (root node R, nodes N, edges E, transition matrix Phi). Two kinds of uncertainty: (i) stagewise-independent noise inside a node, (ii) Markovian transitions between nodes (p. 6). Linear policy graph = standard stage sequence (p. 7).
- **How uncertainty is represented:**
  - Stagewise-dependent processes are modelled by combining the two kinds: the node transition selects the distribution the noise is drawn from (Sec. 3.1, p. 9). Example: El Nino / La Nina years as Markov states with different rainfall distributions; avoids adding a binary state variable and gives **two decision rules per stage** (pp. 9-10).
  - **Markovian policy graph** definition: finite set of stages, each with a set of nodes; all nodes of stage t connect to nodes of at most one other stage; "the different nodes within a stage" are the **Markov states** of the stage (p. 10).
  - A scenario tree is a Markovian policy graph with deterministic nodes (Figs. 6-7, pp. 8-9); generality comes at the cost of many more nodes / decision rules (p. 8).
  - Alternative to Markov nodes: state-space expansion (Guigues 2014) (p. 9).
- **Cyclic policy graphs** (Sec. 3.2, p. 11): infinite horizon handled by a discount factor, represented as arc probabilities out of a stage summing to less than one (implicit zero-cost leaf node). Discount factor rho can be read as a 1 - rho probability that the system stops; rho = 1/(1+r) for interest rate r (p. 11).
- **Risk** (Sec. 3.3, pp. 11-13): finite sample spaces; Expectation, AV@R (= CVaR, Rockafellar-Uryasev) and Worst-case, all coherent; dual (risk-set) representation and "changed probability distribution" (pp. 12-13). Nested node-wise risk measures give time consistency (p. 14).
- **Standard form:** cost-to-go V_i(x, omega) = C_i + risk-adjusted cost-to-go of children, with probability of reaching (j, omega_j) = phi_ij * p_omega (p. 13); Hazard-Decision subproblem (3) and Decision-Hazard subproblem (4) (p. 14).
- **Solution method (Sec. 4, pp. 15-22):** SDDP extension.
  - Assumptions (A1)-(A7) (pp. 15-16): finite number of nodes; all nodes Hazard-Decision; finite noise sample space per node; LP subproblems; bounded feasible optimal control for every incoming state (relatively complete recourse); every sub-graph has positive probability of reaching a leaf (i.e., discount factor round a cycle < 1); states in a polytope.
  - Literature chronology of SDDP convergence results (pp. 16-17), including that **Gjelsvik et al. (1999) and Philpott & de Matos (2012) presented Markovian-policy-graph algorithms "although none provided convergence results"** (p. 16).
  - Cut formulation (5) with a copy constraint x-bar_i = x_i whose dual is the subgradient (the "fishing dual"), simpler than transforming duals of the transition constraints (pp. 17-18).
  - Cut calculation (Algorithm 2, p. 18) uses Philpott et al. (2013) Prop. 4: under a coherent risk measure, the risk-adjusted cut is the expectation of node subgradients under the changed distribution.
  - Forward pass (Algorithm 3, p. 19): sample child nodes by Phi, terminate with probability 1 - sum_j phi_ij at each node, plus a hard maximum depth tau.
  - Backward pass (Algorithm 4, p. 20) identical to standard SDDP; a node visited several times in a forward pass gets several cuts. No explicit cut sharing is needed because a policy graph is a "compressed scenario tree" whose nodes merge exactly when cuts could be shared (p. 19).
  - Lower bound = root-node value (p. 20). Upper bound only statistical (Monte Carlo, Algorithm 5, p. 21), and only for the expectation risk measure; no upper bound in the risk-averse case (p. 20). Termination "an open question"; the common rule (LB inside UB CI, Pereira-Pinto) has known subtleties (Homem-de-Mello et al. 2011) (pp. 20-21).
  - Convergence (Sec. 4.6, pp. 21-23): no general claim. The maximum depth tau truncates the cyclic graph into an **acyclic Markovian policy graph**, for which "finite convergence ... follows directly from existing proofs" (Philpott & Guan 2008; Girardeau et al. 2015; Guigues 2016) (p. 22). Truncation error epsilon <= rho^tau * 2M/(1-rho) for a one-node cycle (p. 22).
- **Key modelling choices and assumptions:** convexity, finite noise, discounting in cyclic graphs, relatively complete recourse.

## Data / case
- POWDer dairy model of Dowson et al. (2019): 52 weekly stages, 5 state variables (soil moisture, pasture cover, grass in storage, cows milking, milk produced), 2 stagewise-independent noises (evapotranspiration, rainfall), Markov states = forecast end-of-season milk price (pp. 23-24, Fig. 17 shows 5 price states $4-$8).
- Infinite-horizon run: rho = 0.95, maximum depth tau = 18,200 (350 cycles), 1000 iterations; bound epsilon <= $0.01/ha (p. 24).

## Key findings
- (p. 10) MC-SDDP structure formalised: Markov states are nodes within a stage; one decision rule (cut set) per node.
- (p. 16) Markovian-graph SDDP algorithms by Gjelsvik et al. (1999) and Philpott & de Matos (2012) had no convergence proofs; (p. 22) for acyclic Markovian graphs, finite convergence follows from existing proofs.
- (p. 17) Shapiro & Ding (2019, the precursor of `shapiro2020`) show computational and policy benefits of an infinite-horizon model for the Brazilian system.
- (p. 20-21) No deterministic upper bound; statistical UB valid only for risk-neutral problems; stopping is an open question.
- (p. 25) Finite-horizon POWDer imposed an end-of-year pasture-cover penalty (2,500 kg/ha) to let the same policy repeat each year; the infinite-horizon policy instead ends the season at minimum pasture cover, showing the constraint was sub-optimal.
- (p. 25) Finite-horizon value $5,782/ha/yr, discounted at 0.95 = $115,640/ha; infinite-horizon = $119,439/ha: +$3,799/ha (+3.3%), attributed to end-of-horizon effects.
- (pp. 25-26) Main benefit: no need to choose a terminal value function; main cost: computation grows with rho because discounting matters over longer horizons; the finite horizon "corresponds to setting rho = 0". Choice between finite and infinite horizon is application dependent (p. 26).
- (p. 26) Implemented in the open-source Julia package SDDP.jl.

## Strengths
- Clear, solver-agnostic notation that covers linear, Markovian, scenario-tree, random-stage-count and cyclic problems.
- Explicit link between Markov states and nodes, and between policy graph and cut sharing.
- Honest about what is and is not proved (no general convergence result, no risk-averse UB).
- Open-source implementation.

## Weaknesses / limitations
- Only one application instance; author explicitly draws no strong conclusions about computational performance or discount-factor choice (p. 23).
- Convergence argument only proved for the single-node cycle (p. 22).
- Assumes all nodes Hazard-Decision and finite noise.
- Manuscript version; journal pagination differs.

## Use it for... (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3.x: Markov representation / MC-SDDP definition | Markovian policy graph; Markov states = nodes within a stage; one decision rule per node | Sec. 3.1, pp. 9-10, Fig. 10 |
| Theory: two types of uncertainty (stagewise-independent noise vs Markov transitions) | Explicit distinction and how they combine into stagewise dependence | p. 6, Sec. 3.1 p. 9 |
| Theory: scenario tree vs SDDP decomposition | Scenario tree as a special policy graph; cost in tractability | pp. 8-9, Figs. 6-7 |
| Model: copy variable for incoming state, dual = cut slope | "Fishing dual" x-bar = x | pp. 17-18 |
| Model: end-of-horizon effect, horizon extension vs infinite horizon | Cyclic graph with discount factor; +3.3% value; no terminal value needed; finite horizon = rho 0 | Sec. 3.2 p. 11; Sec. 5.1 pp. 25-26 |
| Model: discount factor interpretation | rho as 1 - stopping probability; rho = 1/(1+r) | p. 11 |
| Method: convergence of our (acyclic) MC-SDDP | Unrolled acyclic Markovian graph -> finite convergence from Philpott & Guan, Girardeau et al., Guigues | Sec. 4.6, p. 22; also p. 16 |
| Method: stopping / bounds caveats | Only statistical UB, risk-neutral only; stopping an open question | Secs. 4.4-4.5, pp. 20-21 |
| Method: software | SDDP.jl implementation | p. 26 |
| Literature chronology of SDDP variants | Pereira-Pinto -> Philpott-Guan -> Girardeau -> Guigues -> Rebennack -> Nannicini -> Baucke -> Shapiro-Ding | pp. 16-17 |

## Useful quotes (with page numbers)
> "we refer to the different nodes within a stage as the Markov states of the stage." (p. 10)

> "the main benefit of the infinite-horizon model is that practitioners no longer have to derive reasonable estimates for the terminal value function" (pp. 25-26)

## Follow-up references to check (backward snowballing)
- Girardeau, Leclere & Philpott (2015), convergence for convex multistage programs (Math. Oper. Res. 40).
- Philpott, de Matos & Finardi (2013), coherent risk measures in SDDP, upper bounds (Oper. Res. 61).
- Homem-de-Mello, de Matos & Finardi (2011), sampling strategies and stopping criteria for SDDP (Energy Systems 2).
- Nannicini, Traversi & Calvo (2017), Benders squared for infinite horizon.
- Shapiro & Ding (2019) -> published as `shapiro2020`.
- Dowson & Kapelevich, SDDP.jl (INFORMS J. Computing 2021; Optimization Online 2017 cited here).
- Street et al. (2018), decision-hazard hydrothermal scheduling.

