---
bibkey: birgeLouveaux2011
title: "Introduction to Stochastic Programming"
authors: "John R. Birge, François Louveaux"
year: 2011
venue: "Springer Series in Operations Research and Financial Engineering, Springer, New York (2nd ed.), DOI 10.1007/978-1-4614-0237-4"
peer_reviewed: false        # graduate textbook (editorially reviewed, not journal peer review)
methods: [two-stage-stochastic, multistage-scenario-trees, benders-decomposition, sdp, risk-averse-cvar, uncertainty-modelling, adp-reinforcement-learning]
review_sections: []
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Standard SP textbook: two-stage recourse, multistage programs/scenario trees, EVPI/VSS (Ch. 4), L-shaped Benders (Ch. 5), nested decomposition (Ch. 6) and SDDP/AND sampling with UB confidence interval (Sec. 10.4, pp. 432-435); our theory-chapter source for SP concepts."
---

# Introduction to Stochastic Programming, 2nd ed. (Birge and Louveaux, 2011)

_Page mapping (printed page = PDF page - offset). The PDF omits blank pages, so the offset changes per chapter:
Ch. 1-2 (pp. 3-101): -26 · Ch. 3 (pp. 103-161): -25 · Ch. 4 (pp. 163-180): -24 · Ch. 5 (pp. 181-264): -22 · Ch. 6 (pp. 265-288): -21 · Ch. 7 (pp. 289-338): -20 · Ch. 8 (pp. 341-388): -19 · Ch. 9 (pp. 389-416): -18 · Ch. 10 (pp. 417-448): -17 · back matter: -17 to -15.
E.g. printed p. 55 = PDF 81, p. 103 = PDF 128, p. 163 = PDF 187, p. 266 = PDF 287, p. 433 = PDF 450. All page numbers below are printed book pages._

_Reading scope: TOC; Ch. 1 Sec. 1.1-1.3 and 1.6 (pp. 3-32, 48-49); Ch. 2 Sec. 2.1-2.7, 2.9-2.10 (pp. 55-93); Ch. 3 Sec. 3.1a-f and 3.4 (pp. 103-121, 149-155); all of Ch. 4 (pp. 163-172); Ch. 5 Sec. 5.1 (pp. 181-202); Ch. 6 Sec. 6.1 and 6.3 (pp. 265-276, 282-284); Ch. 10 Sec. 10.1-10.5 intro (pp. 417-439); intros of Ch. 8 and 9 and Sec. 9.1 (pp. 341, 389-391). Not read: Sec. 2.8, 3.2-3.3, 3.5, 5.2-5.9, 6.2, 6.4, Ch. 7, most of Ch. 8-9._

_Tagging note: the book describes SDDP (Pereira and Pinto 1991) only under **stagewise independence** (p. 433), so it is not tagged `sddp-markov-chain` or `sddp-time-series`; but Sec. 10.4 is still a citable textbook description of the SDDP forward/backward pass and bounds. The DP recursion of multistage programs (p. 150-151) justifies `sdp`; Sec. 2.9 CVaR justifies `risk-averse-cvar`; Sec. 10.3 scenario generation justifies `uncertainty-modelling`; Sec. 10.5 justifies `adp-reinforcement-learning`. No review-section tag fits: the book has no PHS or market-specific content (it only mentions pumped storage once, p. 417)._

## Research question / purpose
Textbook for a first graduate course: how to build uncertainty into optimization models, what difference recognising uncertainty makes to decisions, and which models are solvable and how (Preface, p. vii). Organised in four parts: Models (Ch. 1-2), Basic properties (Ch. 3-4), Solution methods (Ch. 5-7), Approximation and sampling (Ch. 8-10).

## Setting
- **System:** generic; worked examples are a farmer's land allocation (Sec. 1.1), college-savings financial planning on a scenario tree (Sec. 1.2), multistage **power-plant capacity expansion** with a load-duration curve (Sec. 1.3, pp. 28-35), facility location (Sec. 2.4), a three-month air-conditioner production/storage problem (Sec. 6.1, p. 270). No hydro model. Pumped storage is named once as the archetype of inter-period linkage (p. 417).
- **Markets:** none (no electricity-market content).
- **Horizon and resolution:** generic two-stage and H-stage programs; explicit discussion that stages are not periods (pp. 58, 65).

## Method
- **Model type:** two-stage stochastic LP with fixed recourse, min c'x + E[Q(x, xi)] (pp. 10, 59-60, 103-104); multistage stochastic LP with recourse in nested-expectation form (p. 150, eq. 3.4.1); deterministic equivalent / extensive form (pp. 8, 60, 182); explicit nonanticipativity (split-variable) form (pp. 25-26, 118-119).
- **How uncertainty is represented:** random vector xi on a probability space; discrete (finite scenarios with probabilities) or continuous distributions (pp. 55-57). Scenario trees for multistage problems (pp. 22, 152). Serial independence is assumed for the sampling algorithms (p. 427, p. 433); dependence handled by adding past realizations to the state (p. 151) or, in Grinold [1976], by finite-state **Markov transition probabilities p_ij** between stage outcomes (p. 155).
- **Solution method:** L-shaped method = Benders decomposition of the extensive form with optimality and feasibility cuts (Van Slyke and Wets 1969), finite convergence for finite xi (pp. 182-198); multicut L-shaped (pp. 198-200); nested L-shaped/Benders decomposition for multistage (pp. 266-275, "also appears in Pereira and Pinto [1985]", p. 266); SDDP and abridged nested decomposition (AND) with sampled forward passes and backward cut generation (pp. 432-435); SAA and sampled cuts (pp. 390-391); ADP with basis functions (pp. 436-438).
- **Key modelling choices and assumptions:** fixed recourse matrix W (p. 104); complete / relatively complete recourse, often enforced by penalty variables (pp. 113, 193, 423); recourse function Q(x) piecewise-linear convex for finite xi (Thm. 2, p. 107) and Q_{t+1}(x_t) convex/polyhedral in multistage (Thm. 32, p. 151); risk neutrality = expected value objective (p. 7), risk aversion via piecewise-linear utility, downside-risk constraints, VaR, CVaR, robust min-max (pp. 66-68, 84-86); end-of-horizon handled by annuities/salvage values (p. 31, Sec. 10.2) or terminal penalties (p. 426, Ex. 4).

## Data / case
Small illustrative numerical examples only (farmer: EVPI = $7,016, VSS = $1,150, pp. 9, 164-165; financial planning: RP = -1.514, EV = -3.788, VSS = 2.274, p. 24; air-conditioner nested-decomposition example, pp. 270-275). No real data set.

## Key findings
- (p. 7) Maximising expected profit corresponds to a risk-neutral decision maker; risk aversion discussed in Ch. 2.
- (pp. 8-9) Extensive form: first-stage decisions (planting) before the realisation, second-stage (sales/purchases) per scenario; the stochastic solution hedges and is never optimal for any single scenario.
- (pp. 9-10) EVPI = value of knowing the future (perfect information); VSS = gain from using the stochastic model instead of the expected-value solution; VSS is the more practically relevant one when no extra information can be bought. VSS can exceed EVPI.
- (p. 21) Decisions are **nonanticipative**: at each stage only past returns are observed; first-period decisions must be the same for all outcomes.
- (p. 22) On a scenario tree one decision vector per node; stage-t decisions are indexed by the history (s1, ..., s_{t-1}).
- (pp. 25-27) Scenario-based formulation with explicit nonanticipativity constraints; the tree "grows quite bushy" with horizon H; scenario counts become extremely large.
- (p. 31) Charging annuities on cumulative capacity instead of full investment cost simplifies end-of-horizon effects (salvage-value approach, Sec. 10.2).
- (p. 32) Decisions at t depend on realizations up to t but not on future ones; if decisions did not depend on xi the problem collapses to a deterministic one with expected coefficients.
- (pp. 55-56) Uncertain parameters are modelled as random variables; when Omega is a few "states of the world or scenarios", all random elements jointly depend on these finitely many scenarios (typical in strategic models).
- (pp. 57-58) Recourse programs: some decisions taken after uncertainty is disclosed; first stage = decisions before the random experiment, second stage = after; the stages are defined by before/after the experiment and **may contain sequences of decisions and events** (farming example: planting over the whole spring).
- (pp. 59-60) Classical two-stage fixed-recourse LP (Dantzig 1955, Beale 1955); second-stage value function Q(x, xi), expected Q(x), deterministic equivalent program (DEP); if Q is known the SP is an ordinary NLP.
- (p. 65) **Stages versus periods**: a 36-month plan can be a two-stage model; a multistage model is needed only if the firm can revise decisions (here: three stages with re-opening after a year).
- (p. 66) Frequently recurring short-term uncertainty (daily/weekly) -> expected value closely matches realised yearly revenue, so risk neutrality is reasonable; (p. 67) for one-shot/long-term scenarios the expectation is a poor representation of risk aversion.
- (p. 68) Expected downside-risk constraint E[u] <= l with u >= g - q'y, linear in the extensive form.
- (pp. 84-86) VaR, coherent risk measures (Artzner et al. 1999), CVaR as an LP (Rockafellar and Uryasev 2000), CVaR constraints, robust two-stage min-max.
- (pp. 89-90) DP / MDP literature emphasises low-dimensional state/action spaces and **Markovian structure**; backward recursion becomes cumbersome for large state spaces but underlies SP computation (Ch. 6); SP generally does not impose the Markov assumptions needed for stationary DP solutions.
- (p. 104) Recourse function Q(x) measures the expected future effect of first-stage decision x; first-stage decisions take these effects into account.
- (p. 105) The inherent difficulty of SP is the computational burden of computing Q(x) for all x.
- (p. 107, Thm. 2) For finite discrete xi, Q(x) is piecewise linear and convex; used by the L-shaped method.
- (pp. 113, 193) Complete recourse (pos W = R^m2) and relatively complete recourse (K1 subset of K2) avoid feasibility cuts; complete recourse is often added to a model so no outcome is infeasible.
- (pp. 118-119) Nonanticipativity constraints E(x) - x = 0 force almost all x(omega) to be equal; the split-variable form nearly decomposes by scenario.
- (pp. 149-151) Multistage SLP with recourse (4.1); decisions depend on the history up to t; DP-type backward recursion Q_t(x_{t-1}, xi_t) = min c_t x_t + Q_{t+1}(x_t), with Q_{t+1}(x_t) = E[Q_{t+1}(x_t, xi_{t+1})]; x_t is the state; **other state information on past realizations must be included if xi_t is not independent of the past** (p. 151).
- (p. 151, Thm. 32) K_t and Q_{t+1}(x_t) are convex, and polyhedral for finite supports (basis for cutting-plane methods).
- (p. 152) Finite realizations -> scenarios on a tree; each stage-t scenario has a single ancestor and possibly several descendants; deterministic equivalent is an "arborescent" LP that becomes extremely large as the number of stages grows even with few realizations per stage.
- (pp. 153-155) Block-separable recourse: aggregate decisions (w) vs detailed decisions (y) that do not affect future constraints; then multistage collapses to a two-stage-like problem.
- (p. 155) Grinold [1976]: xi_t in a finite set with transition probabilities p_ij = P{xi_{t+1} = j | xi_t = i}, MDP view of SP; yields separability of future decisions from previous outcomes.
- (pp. 163-164) EVPI = maximum amount one would pay for perfect information; wait-and-see WS = E[min_x z(x, xi)] (each scenario solved separately, first stage included); here-and-now = recourse problem RP; EVPI = RP - WS (minimisation).
- (p. 165) Expected value problem EV, expected result of the EV solution EEV = E[z(x_bar(xi_bar), xi)], VSS = EEV - RP = cost of ignoring uncertainty.
- (p. 166, Prop. 1) WS <= RP <= EEV (minimisation); Prop. 2: EV <= WS for fixed q and W (Jensen).
- (pp. 167-171) 0 <= EVPI, VSS <= EEV - EV; EVPI = 0 with VSS > 0 and vice versa are possible; no general rule links variance to EVPI/VSS.
- (pp. 182-187) L-shaped algorithm: master with feasibility cuts and optimality cuts theta >= e - E x; cut coefficients are probability-weighted second-stage duals (eqs. 1.6-1.7); stop when theta >= e - E x.
- (pp. 189-190, 197) Optimality cuts are supporting hyperplanes of Q(x) (subgradient inequality from LP duality); finite convergence because there are finitely many dual bases (Thm. 2, p. 198).
- (pp. 198-200) Multicut version: one cut per realization; fewer major iterations, larger master; rule of thumb: useful when K is not much larger than m1.
- (pp. 265-266) Multistage SPs are PSPACE-hard; approximation families: value-function approximation (outer/inner linearization), relaxation, policy restriction, aggregation/scenario reduction, Monte Carlo.
- (pp. 266-269) Nested L-shaped/Benders decomposition: cuts on Q_{t+1}(x_t) in each node subproblem NLDS(t,k); "fast-forward-fast-back" sequencing generally most efficient; Thm. 1 finite convergence for finite supports and bounded x.
- (p. 269) In the multistage case cuts need not be true supports (may lie strictly below the function) when subproblems carry approximate future functions.
- (p. 270) Example with storage between months; "no salvage value" assumed to resolve the end-of-horizon problem.
- (p. 417) Inter-period linkage example: power stored by pumping water into a hydro reservoir when demand is low, so decisions in one period depend on previous ones; number of periods causes exponential growth in problem size.
- (pp. 422-426) Aggregation bounds for many or infinite periods, with penalty variables for feasibility and a discount factor.
- (pp. 426-429) Scenario generation: moment matching (adjusted random samples, Kouwenberg 2001; Høyland and Wallace 2001), scenario reduction in distribution metrics (Dupačová, Gröwe-Kuska, Römisch 2003; Pflug 2001), EVPI-based tree adaptation (Dempster 2006); with serial independence the same samples can be used on every branch (p. 427).
- (p. 431) SAA convergence for multistage problems (Shapiro 2003).
- (pp. 432-435) SDDP (Pereira and Pinto 1991) and AND (Donohue and Birge 2006) under serial independence: sampled forward pass gives an upper-bound estimate with sample mean and standard deviation (eqs. 4.1-4.3) and confidence interval; backward pass builds cuts (lower bound); finite convergence with resampling (Philpott and Guan 2008); accuracy depends on the number of sampled scenarios.
- (p. 436, Ex. 2) Infinite-horizon stationary version with discount factor, solved by sampling-based outer linearization (Birge and Zhao 2007).
- (pp. 436-438) ADP: value function as weighted basis functions fitted by regression on sampled paths; linear ADP gives a lower-bound estimate, forward simulation an upper-bound estimate.

## Strengths
- Authoritative, widely cited textbook; precise definitions (recourse, DEP, WS, RP, EEV, EVPI, VSS) with numerical examples.
- Covers the whole chain from modelling to decomposition algorithms, with convergence proofs (L-shaped p. 198; nested p. 268).
- Explicit discussion of stages vs periods (p. 65) and risk neutrality vs risk aversion (pp. 66-67), both directly relevant to our modelling justification.
- Gives a compact SDDP description with upper-bound confidence interval (pp. 433-435) that can complement Pereira and Pinto (1991).

## Weaknesses / limitations
- SDDP section is brief and assumes stagewise independence; no Markov-chain SDDP, no PAR inflow model, no cut sharing with dependence.
- No hydropower, electricity-market or price-modelling content beyond the capacity-expansion example and a one-line mention of pumped storage (p. 417).
- Minimisation conventions throughout (lower bound from cuts, upper bound from simulation); signs must be flipped for our profit-maximisation formulation.
- Textbook, not peer reviewed in the journal sense; 2nd edition reorganised chapters relative to the 1997 1st edition, so page numbers differ between editions.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3.3: uncertain parameters as random variables | probability space, discrete/continuous distributions, expectation | pp. 55-57, Sec. 2.1 |
| Theory 3.3: finite scenarios with probabilities | Omega as a few states of the world/scenarios; discrete distribution f(xi_k); scenario index s with p = 1/3 in farmer example | p. 56; pp. 7-8; p. 106 |
| Theory 3.3: risk-neutral expected-profit objective | expected profit = risk neutral | p. 7 |
| Model justification: risk neutrality for a frequently operating plant | short-term recurring (daily/weekly) uncertainty -> expectation close to realised yearly revenue; one-shot scenarios need risk aversion | pp. 66-67, Sec. 2.5 |
| Theory/extension: risk aversion, CVaR | downside risk (p. 68), VaR, coherent risk measures, CVaR LP and CVaR constraint, robust min-max | pp. 68, 84-86, Sec. 2.9 |
| Theory 3.3: two-stage recourse, first/second stage | decisions before/after the random experiment; two-stage fixed-recourse LP; DEP | pp. 57-60, Sec. 2.3-2.4; pp. 103-104 |
| Theory 3.3: term "here-and-now" / "wait-and-see" | defined together with RP and WS | p. 164 |
| Theory 3.3: first-stage decisions identical across scenarios (nonanticipativity) | nonanticipativity definition; explicit constraints E(x) - x = 0 | pp. 21, 25-26, 118-119 |
| Theory 3.3: recourse function and its computational burden | Q(x) = expected value of decision x; difficulty = computing Q(x) for all x | pp. 104-105; also p. 113 (numerical integration) |
| Theory: convex piecewise-linear value function (why cuts work) | Thm. 2: Q(x) piecewise linear convex for finite xi; Thm. 32: Q_{t+1}(x_t) convex, polyhedral | p. 107; p. 151 |
| Theory 3.3: EVPI, WS bound | WS, RP, EVPI = RP - WS; WS <= RP <= EEV | pp. 163-166, Sec. 4.1, 4.3 |
| Theory/results: VSS, EEV (benchmark vs stochastic policy) | EV problem, EEV, VSS = EEV - RP; bounds 0 <= EVPI, VSS <= EEV - EV; examples | pp. 165-171; intro example pp. 9-10, 24 |
| Theory 3.3: multistage stochastic programs | gradual information, history-dependent decisions, nested-expectation formulation, DP recursion | pp. 149-151, Sec. 3.4 |
| Theory 3.3: scenario tree structure | tree, decision per node, single ancestor, descendants | pp. 21-22 (Fig. 3); p. 152 (Fig. 4) |
| Theory 3.3: curse of dimensionality of scenario trees | tree grows "bushy"; extensive form becomes extremely large with stages; exponential growth in periods | pp. 25-26; p. 152; p. 417; p. 427 |
| Theory 3.3: stages vs time periods | stage = before/after information; 36-month two-stage example; three-stage version | p. 58; **p. 65 (Sec. 2.4d)** |
| Theory: DP / MDP relationship, Markov structure | DP and MDPs, backward recursion, Markov assumptions, stationary infinite-horizon policy | pp. 89-90, Sec. 2.10b |
| Model/Method: why the Markov state is needed | if xi_t depends on the past, past realizations must enter the state; Grinold's transition-probability (p_ij) approach | p. 151; p. 155 |
| Theory 3.5 Benders: L-shaped (stochastic Benders) | algorithm, optimality cuts from probability-weighted duals, feasibility cuts, worked example | pp. 182-195, Sec. 5.1a-b |
| Theory 3.5 Benders: cuts as supporting hyperplanes, convergence | subgradient inequality from duality, finite convergence | pp. 189-191, 196-198 |
| Theory: single-cut vs multicut | multicut L-shaped, trade-off, rule of thumb | pp. 198-200 |
| Model: complete recourse / penalty (spillage, slack) variables | complete and relatively complete recourse; penalty variable for feasibility | pp. 113, 193, 423 |
| Theory 3.6 SDDP: nested Benders as parent of SDDP | nested L-shaped decomposition, NLDS(t,k), fast-forward-fast-back, finite convergence; Pereira and Pinto [1985] | pp. 266-269, Sec. 6.1 |
| Theory 3.6 SDDP: cuts may not be tight supports in multistage | remark on non-support cuts | p. 269, p. 275 |
| Theory 3.6 SDDP: forward/backward pass, bounds, CI on upper bound | SDDP and AND under serial independence; UB estimate eqs. 4.1-4.3; termination; convergence (Philpott and Guan 2008) | pp. 432-435, Sec. 10.4 |
| Model: end-of-horizon value | salvage-value/annuity approach; no-salvage assumption in example; terminal penalty for leftovers | p. 31; p. 270; p. 426 (Ex. 4); Sec. 10.2 |
| Model/extension: infinite horizon, stationary data | infinite-horizon fixed-point with discount, sampling outer linearisation (Birge and Zhao 2007); aggregation bounds | p. 436 (Ex. 2); pp. 422-425 |
| Uncertainty modelling: scenario generation/reduction | moment matching, scenario reduction, distribution metrics, serial independence | pp. 426-431, Sec. 10.3 |
| Theory: SAA | sample average approximation, convergence | pp. 390-391; p. 431 |
| Theory/related work: ADP | basis-function value approximation, bounds | pp. 436-438, Sec. 10.5 |
| Background/motivation: storage links periods | pumped storage as example of inter-period linkage | p. 417 |
| Analogy: multistage power capacity expansion | investment + operation with load-duration curve, construction delays, block separability | pp. 28-32, Sec. 1.3; pp. 153-155 |

## Useful quotes (with page numbers)
> "the computational burden of computing Q(x) for all x" (p. 105)

> "This quantity is the cost of ignoring uncertainty in choosing a decision." (p. 165, on VSS)

> "the number of periods leads to exponential increases in problem size" (p. 417)

> "Other state information in terms of the realizations of the random parameters up to time t should be included if the distribution ... is not independent of the past" (p. 151; abridged)

## Follow-up references to check (backward snowballing)
- Pereira and Pinto [1985] (nested decomposition in energy, p. 266) and [1991] (SDDP, p. 433) — `pereira1991` already in repo.
- Donohue and Birge [2006], abridged nested decomposition (p. 433).
- Philpott and Guan [2008], SDDP convergence proof (p. 434) — `philpott2008` already in references.bib.
- Grinold [1976], Markov-chain/transition-probability approach to multistage SP (p. 155) — conceptual precursor of Markov-chain SDDP.
- Van Slyke and Wets [1969], L-shaped method (p. 182).
- Birge [1985b], nested decomposition for multistage linear SP (p. 266); Birge and Louveaux [1988], multicut (p. 199).
- Madansky [1960], WS/RP/EEV inequalities (p. 166).
- Rockafellar and Uryasev [2000, 2002], CVaR (p. 85).
- Shapiro [2003], multistage SAA convergence (p. 431).
- Høyland and Wallace [2001]; Dupačová, Gröwe-Kuska and Römisch [2003]; Pflug [2001]; Kouwenberg [2001] (scenario generation, p. 429).
- Birge and Zhao [2007], infinite-horizon sampling outer linearisation (p. 436).
- Louveaux and Smeers [2011]; Manne [1974]; Chao [1981] — EVPI/VSS in energy models (p. 170).

