---
bibkey: boydVandenberghe2004
title: "Convex Optimization"
authors: "Stephen Boyd, Lieven Vandenberghe"
year: 2004
venue: "Cambridge University Press (book)"
peer_reviewed: true
methods: [deterministic-lp-milp, benders-decomposition]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Standard textbook on convexity, LP and Lagrange duality. Source for local vs global optima in nonconvex NLP (pp. 9-10), local = global for convex problems (p. 138), LP duality and strong duality (pp. 224-227), shadow prices (pp. 241, 253) and the sensitivity results behind dual-based water values and cuts (pp. 249-253). Does not cover Benders, cutting planes, DP or stochastic programming."
---

# Convex Optimization (Boyd and Vandenberghe, 2004)

> **Page numbers.** All page numbers below are **printed** book pages. In our `paper.pdf` / `paper.txt`, **printed page = PDF page − 14** for the main text (e.g. printed p. 1 = PDF p. 15, p. 9 = PDF p. 23, p. 249 = PDF p. 263). Front matter uses roman numerals (printed p. xi = PDF p. 11). Our copy is the "Seventh printing with corrections 2009" (PDF p. 4). Pagination of the main text appears to match the 2004 first edition (unverified; the table of contents page numbers match the text).

## Research question / purpose
A graduate textbook whose goal is to help the reader "develop a working knowledge of convex optimization", i.e. the skills to "recognize, formulate, and solve convex optimization problems" (Preface, p. xii). It deliberately sits between modelling-oriented LP/NLP books and convex-analysis or algorithm-complexity books (p. xii). Its central message is that convex problems, like least-squares and LP, can be solved reliably and efficiently, and that "the challenge, and art, in using convex optimization is in recognizing and formulating the problem" (p. 8).

**Table of contents (relevant parts in bold).** Ch. 1 **Introduction** (pp. 1–17): **1.1 Mathematical optimization, 1.2 Least-squares and LP, 1.3 Convex optimization, 1.4 Nonlinear optimization** (pp. 9–11). Part I Theory: Ch. 2 Convex sets (pp. 21–66, incl. **2.5 separating and supporting hyperplanes**, pp. 46–51); Ch. 3 **Convex functions** (pp. 67–126, incl. **3.1 definitions and first-order conditions**, **3.2 operations preserving convexity**); Ch. 4 **Convex optimization problems** (pp. 127–214, incl. **4.1 terminology and equivalent problems**, **4.2 convex optimization, local/global optima**, **4.3 linear optimization problems**); Ch. 5 **Duality** (pp. 215–288: **5.1 Lagrange dual function, 5.2 dual problem, 5.3 geometric interpretation, 5.4 saddle point and price interpretation, 5.5 optimality conditions/KKT, 5.6 perturbation and sensitivity analysis**, 5.7–5.9). Part II Applications (Chs. 6–8: approximation, statistical estimation, geometric problems). Part III Algorithms (Chs. 9–11: unconstrained, equality-constrained, interior-point methods). Appendices A–C (pp. 631–684), references (p. 685), notation (p. 697).

## Setting
- **System:** none. This is a general mathematics/optimisation textbook. Examples come from engineering, statistics, finance, control and circuit design (pp. 2–3, 16–17). No hydropower, electricity markets or storage.
- **Markets:** none. The economic content is limited to the **price/tax interpretation** of Lagrange multipliers (§5.4.4, pp. 240–241) and the **shadow price** interpretation (p. 253).
- **Horizon and resolution:** not applicable. Static (single-stage) optimisation only. There is no multistage, dynamic or stochastic programming beyond brief examples.

## Method
- **Model type:** theory and algorithms for convex optimisation: convex sets and functions, convex problems (LP, QP, SOCP, GP, SDP), Lagrange duality, and Newton/interior-point methods.
- **How uncertainty is represented:** not a theme. Uncertainty appears only in robust approximation (§6.4) and statistical estimation (Ch. 7), neither relevant to us.
- **Solution method:** interior-point methods (Ch. 11). The book explicitly **omits** "subgradient methods ..., bundle methods ..., cutting-plane methods ... and the ellipsoid method" (p. 16; also p. 13: it omits "quasi-Newton, conjugate-gradient, bundle, and cutting-plane algorithms").
- **Key definitions and results relevant to us:**
  - **Optimisation problem, LP and NLP** (§1.1, p. 1): problem (1.1) is an LP if objective and constraints are linear, "If the optimization problem is not linear, it is called a nonlinear program." Convexity generalises linearity, so "we can consider convex optimization to be a generalization of linear programming" (p. 2).
  - **Nonlinear optimisation** (§1.4, p. 9): the term for problems whose objective or constraint functions "are not linear, but not known to be convex". "Sadly, there are no effective methods for solving the general nonlinear programming problem". There are two compromises:
    - **Local optimisation** (§1.4.1, pp. 9–10) seeks "a point that is only locally optimal ... but is not guaranteed to have a lower objective value than all other feasible points". It needs an initial guess, gives little information about the distance to the global optimum, and is "more art than technology".
    - **Global optimisation** (§1.4.2, p. 10) finds the true global solution, but worst-case complexity "grows exponentially with the problem sizes".
    - Convex relaxation and Lagrangian relaxation give lower bounds for nonconvex problems (§1.4.3, p. 11).
  - **Convex function, first-order condition** (§3.1.1, p. 67; §3.1.3, p. 69): f is convex iff f(y) ≥ f(x) + ∇f(x)ᵀ(y − x) (Eq. 3.2). "The first-order Taylor approximation is in fact a global underestimator of the function" (p. 69). From local information (value and derivative at a point) one gets a global underestimator, "perhaps the most important property of convex functions" (p. 69). **This is the mathematical reason a Benders/SDDP cut built at one trial state is valid everywhere.**
  - **Pointwise maximum** (§3.2.3, pp. 80–81): the maximum of convex (e.g. affine) functions is convex. Example 3.5: f(x) = max{a_iᵀx + b_i} is piecewise-linear convex, and every piecewise-linear convex function can be written this way (p. 80). **This is the form of a cut-based outer approximation of a convex cost-to-go function** (for our concave profit-to-go: a minimum of affine functions).
  - **Partial minimisation preserves convexity** (§3.2.5, pp. 87–88): if f(x, y) is jointly convex and C convex, g(x) = inf_{y∈C} f(x, y) is convex. This underlies the convexity of an LP's optimal value as a function of the incoming state.
  - **Optimising over some variables** (§4.1.3, p. 133): inf_{x,y} f(x, y) = inf_x f̃(x) with f̃(x) = inf_y f(x, y). This is the principle behind splitting a problem into a first part plus an optimal-value ("future cost") function of the coupling variables.
  - **Epigraph form** (§4.1.3, p. 134; convex case p. 143) and **piecewise-linear minimisation as an LP** (p. 150–151): minimise t subject to a_iᵀx + b_i ≤ t, i = 1..m. This is how the α variable with cut constraints enters our weekly LP.
  - **Convex problem and local = global** (§4.2.1–4.2.2, pp. 136–138): a convex problem minimises a convex objective over a convex feasible set (convex f_i, affine h_i). "A fundamental property of convex optimization problems is that any locally optimal point is also (globally) optimal" (p. 138). Concave maximisation is also called a convex problem (p. 137). For quasiconvex problems, local optima need not be global (p. 139).
  - **LP forms** (§4.3, pp. 146–148): general LP (4.27), standard form (4.28), inequality form (4.29), conversion via slack variables and x = x⁺ − x⁻. "Linear programs are, of course, convex optimization problems" (p. 146).
  - **Lagrangian and dual function** (§5.1, pp. 215–216): L(x, λ, ν) = f₀ + Σλ_i f_i + Σν_i h_i. The dual function g = inf_x L is concave even for nonconvex problems (p. 216). It is a lower bound: g(λ, ν) ≤ p* for λ ⪰ 0 (Eq. 5.2, p. 216).
  - **LP duals** (pp. 219, 224–225): the dual of standard-form LP is maximise −bᵀν s.t. Aᵀν + c ⪰ 0 (5.20). The dual of inequality-form LP is maximise −bᵀλ s.t. Aᵀλ + c = 0, λ ⪰ 0 (5.22). "The dual of a standard form LP is an LP with only inequality constraints, and vice versa" (p. 225).
  - **Weak and strong duality** (§5.2.2–5.2.3, pp. 225–227): d* ≤ p* always (5.23). Strong duality d* = p* holds for convex problems under Slater's condition (p. 226); for affine constraints the refined Slater condition reduces to feasibility (pp. 226–227). For LP: "strong duality holds for any LP ... provided the primal problem is feasible", and likewise if the dual is feasible. It fails only if both primal and dual are infeasible (p. 227).
  - **Price or tax interpretation and shadow prices** (§5.4.4, pp. 240–241): λ_i is the price per unit violation of constraint i. With strong duality, a dual optimal λ* is "a set of prices for which there is no advantage to the firm in being allowed to pay for constraint violations", and is "sometimes called a set of shadow prices" (p. 241).
  - **Duality gap as certificate and stopping criterion** (§5.5.1, pp. 241–242): a primal feasible x and dual feasible (λ, ν) localise p* in [g(λ, ν), f₀(x)]. The gap is used as a nonheuristic stopping criterion (p. 242). This is analogous to stopping SDDP on the gap between lower and upper bounds.
  - **Complementary slackness and KKT** (§5.5.2–5.5.3, pp. 242–244): λ_i* f_i(x*) = 0, so the multiplier is zero unless the constraint is active (p. 243). KKT conditions (5.49) are necessary under strong duality (p. 243) and sufficient for convex problems (p. 244).
  - **Perturbation and sensitivity** (§5.6, pp. 249–253):
    - Perturbed problem with right-hand sides u, v; optimal-value function p*(u, v), which is **convex in (u, v) when the problem is convex** (p. 250).
    - **Global inequality** (5.57): p*(u, v) ≥ p*(0, 0) − λ*ᵀu − ν*ᵀv, an affine lower bound on p* from the dual optimum at one point (p. 250, Fig. 5.10 on p. 251). **This is the form of an optimality cut.** It needs only strong duality and attainment, not differentiability, and it is asymmetric: it gives a lower but no upper bound (p. 251).
    - **Local sensitivity** (5.58): if p* is differentiable at 0, λ_i* = −∂p*/∂u_i and ν_i* = −∂p*/∂v_i (p. 252). "The optimal Lagrange multipliers are exactly the local sensitivities of the optimal value with respect to constraint perturbations" (p. 252).
    - **Shadow price interpretation** (p. 253): for a firm with resource constraints, λ_i* tells "approximately how much more profit the firm could make, for a small increase in availability of resource i", and is the natural or equilibrium price of that resource.
  - **Max-min / saddle point** (§5.4.1–5.4.2, pp. 237–239): weak duality as sup inf ≤ inf sup; strong duality as a saddle point of the Lagrangian.

## Data / case
None. Numerical examples in Parts II–III are illustrative, often randomly generated ("typical") instances (p. 13).

## Key findings
- (p. 1) An optimisation problem is an LP if objective and constraints are linear. Otherwise it is a nonlinear program.
- (p. 2) Every LP is a convex optimisation problem, so convex optimisation generalises LP.
- (p. 6) Solving most LPs is "a mature technology". Interior-point complexity in practice is order n²m.
- (p. 9) Nonlinear optimisation means objective or constraints not linear "but not known to be convex". There are no effective methods for the general NLP. Even ten-variable problems can be very hard.
- (pp. 9–10) Local optimisation finds locally optimal points without a guarantee of global optimality. It needs a starting point, which "can greatly affect the objective value of the local solution obtained", and gives "Little information ... about how far from (globally) optimal the local solution is".
- (p. 10) Global optimisation finds the true optimum at worst-case exponential cost, so it is used only for small problems where the value of the global solution is high.
- (p. 11) Convex relaxations and Lagrangian duals give lower bounds for nonconvex problems.
- (p. 69) For a convex function, the first-order Taylor approximation is a global underestimator.
- (p. 80) The pointwise maximum of affine functions is a piecewise-linear convex function, and conversely.
- (pp. 87–88) Minimising a jointly convex function over some variables leaves a convex function of the others.
- (p. 138) In a convex problem every local optimum is a global optimum.
- (p. 216) The dual function is concave and gives a lower bound on p*, even for nonconvex problems.
- (p. 227) Strong duality holds for every feasible LP (or every LP with a feasible dual).
- (p. 241) Optimal dual variables are called shadow prices.
- (p. 250) The optimal value of a convex problem is a convex function of the constraint right-hand sides.
- (p. 250) Global sensitivity inequality (5.57): a dual optimum yields an affine lower bound on the perturbed optimal value.
- (p. 252) Local sensitivity (5.58): when p* is differentiable, multipliers equal minus its partial derivatives with respect to the right-hand sides.
- (p. 253) Economic reading: the multiplier is the marginal profit of one more unit of a constrained resource.

## Strengths
- The standard, very widely used reference for convexity, LP duality and sensitivity. Definitions and theorems are precise and self-contained.
- Gives the exact theoretical results we need to justify reading water values off LP duals and building cuts: convexity of the optimal-value function (p. 250), the affine lower bound (5.57) (p. 250), and the derivative interpretation (5.58) (p. 252), together with their assumptions.
- Clear geometric pictures: Fig. 5.10 (p. 251) shows p*(u) and its affine underestimator, which could inspire a figure for cuts. Fig. 3.2 (p. 69) shows the first-order underestimator.
- Freely available from the authors' website (unverified for the current URL), so easy for readers to check.

## Weaknesses / limitations
- No Benders decomposition, cutting-plane methods, subgradient methods, dynamic programming or (multistage) stochastic programming. The authors say so explicitly (pp. 13, 16). It cannot be cited for SDDP or Benders cuts as such, only for the convex-analysis and duality facts behind them.
- Minimisation convention throughout. Our model maximises profit, so signs must be mirrored: concave value function, cuts as upper bounds, and multiplier signs depending on how the constraint is written (p. 137 covers concave maximisation only briefly).
- The local sensitivity result (5.58) assumes differentiability of p*. For LPs, p* is piecewise linear and not differentiable at breakpoints (degenerate LPs). There the multiplier is not unique and gives only a one-sided bound via (5.57). Subgradients of p* are not developed in the main text (the term appears only in passing, e.g. p. 338). Use another source (e.g. Birge and Louveaux) for the subgradient view.
- Integer programming and MILP are not treated, so don't cite it for MIP complexity.

## Use it for… (lookup guide)
| Use in our thesis | What the book provides | Where in the book (printed page/section) |
|---|---|---|
| Theory 3.1: definition of LP vs NLP | LP if objective and constraints linear; otherwise nonlinear program; convex optimisation generalises LP | pp. 1–2, §1.1 |
| Theory 3.1: NLP, local vs global optima (already cited) | NLP = not linear, not known to be convex; local methods find local optima only; global methods are exponential | pp. 9–10, §1.4.1–1.4.2 |
| Theory 3.1: LP local optimum is global (currently cited to `lundgren2010`) | Any locally optimal point of a convex problem is globally optimal; LPs are convex | p. 138 §4.2.2; p. 146 §4.3 |
| Theory 3.1: LP standard/inequality form | Eqs. (4.27)–(4.29), slack variables | pp. 146–148, §4.3 |
| Theory 3.1: dual problem, weak/strong duality (currently cited to `lundgren2010`) | LP duals (5.20), (5.22); weak duality (5.23); strong duality for feasible LPs | pp. 224–227, §5.2 |
| Theory 3.1: dual variables as shadow prices | Price/tax interpretation; "shadow prices"; marginal profit of a resource | pp. 240–241 §5.4.4; p. 253 |
| Theory 3.x / Model: dual value = marginal value of storage (water value) | Local sensitivity λ* = −∂p*/∂u (5.58), valid where p* is differentiable | pp. 251–252, §5.6.3 |
| Theory 3.x (Benders/SDDP): cuts are valid global bounds | p*(u, v) convex for convex problems; global inequality (5.57) gives an affine bound from one dual solution; Fig. 5.10 | pp. 250–251, §5.6.1–5.6.2 |
| Theory 3.x: supporting hyperplanes / first-order underestimator | f(y) ≥ f(x) + ∇f(x)ᵀ(y − x); supporting hyperplane theorem | p. 69 §3.1.3; p. 51 §2.5.2 |
| Theory 3.x: cut approximation is piecewise-linear convex | Max of affine functions = PWL convex (and converse); PWL minimisation as LP via epigraph | p. 80 Ex. 3.5; pp. 134, 150–151 |
| Theory 3.x: convexity of value functions (future cost) | Partial minimisation preserves convexity; optimising over some variables | pp. 87–88 §3.2.5; p. 133 §4.1.3 |
| Theory 3.x: convergence gap / stopping criterion | Duality gap localises p*; nonheuristic stopping criterion | pp. 241–242, §5.5.1 |
| Theory 3.x: complementary slackness | Multiplier zero unless the constraint is active | p. 243, §5.5.2 |
| **Not** for: Benders, cutting planes, SDDP, DP, stochastic programming, MILP | Explicitly not covered | pp. 13, 16 |

## Useful quotes (with page numbers)
> "If the optimization problem is not linear, it is called a nonlinear program." (p. 1)

> "Sadly, there are no effective methods for solving the general nonlinear programming problem (1.1)." (p. 9)

> "A fundamental property of convex optimization problems is that any locally optimal point is also (globally) optimal." (p. 138)

> "... the first-order Taylor approximation is in fact a global underestimator of the function." (p. 69)

> "... the optimal Lagrange multipliers are exactly the local sensitivities of the optimal value with respect to constraint perturbations." (p. 252)

> "For this reason a dual optimal λ* is sometimes called a set of shadow prices for the original problem." (p. 241)

## Follow-up references to check (backward snowballing)
- Kelley (1960), "The cutting-plane method for solving convex programs" [Kel60], cited on p. 16. It is the origin of the cutting-plane idea behind Benders/SDDP outer approximation.
- Rockafellar (1970), *Convex Analysis* [Roc70] (p. 16), for subgradients and conjugate duality if a more rigorous source is needed.
- Luenberger [Lue95], for the price interpretation of duality (p. 59).
- Bertsekas (1999), *Nonlinear Programming* [Ber99] (p. 16), covers local methods, duality and DP in one book.

