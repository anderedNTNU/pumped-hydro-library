---
bibkey: murphy2013benders
bibkey_provisional: true
title: "Benders, Nested Benders and Stochastic Programming: An Intuitive Introduction"
authors: "James Murphy"
year: 2013
venue: "Cambridge University Engineering Department, Technical Report CUED/F-INFENG/TR.675 (also Optimization Online 2013/12/4157)"
peer_reviewed: false
methods: [benders-decomposition, two-stage-stochastic, multistage-scenario-trees]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Tutorial that derives Benders decomposition from LP duality, applies it to two-stage stochastic LPs (L-shaped method: feasibility and optimality cuts, unicut vs multicut) and extends it to multistage trees (nested Benders: decisions passed down, cuts passed up; fast-forward/fast-back sequencing), emphasising that the recourse function is convex piecewise linear so cuts give an outer linearisation."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/39_Murphy_2013_Benders_nested_Benders_and_stochastic_programming_An_intuitive_introduction.pdf
---

# Benders, nested Benders and stochastic programming (Murphy, 2013)

_Page mapping: printed page = PDF page - 6 (printed p. 1 = PDF p. 7; contents on PDF p. 5). Page numbers below are printed pages._

## Research question / purpose
- Explain nested Benders for large-scale stochastic programming "in a way that is intelligible to someone coming to it for the first time" (abstract). Explicitly "a tutorial, rather than a literature review" with limited references (p. 1).

## Setting
- Generic stochastic linear programs on scenario trees; no application.

## Method (structure of the tutorial)
- Asides on LP and duality (pp. 2-8): feasibility, boundedness, optimum at a corner point, weak/strong duality.
- **Benders basic idea (pp. 9-13):** Benders (1962) split MIPs into an integer and an LP part; for stochastic programming the split is of a large LP (deterministic equivalent) into smaller LPs (p. 9). Fixing y gives subproblem PX; its dual gives a bound as a function of y over dual corner points; relaxing to a subset of these constraints gives the master problem; stop when upper and lower bounds coincide (pp. 10-13).
- **Stochastic programming structure (pp. 14-19):** recourse problems as trees, deterministic equivalent form (p. 17), discretisation (p. 18).
- **L-shaped method (pp. 20-38):** feasibility cuts (pp. 20-28), optimality cuts (pp. 29-34): Q(y) = expected subproblem value; each Q(y,u) is "piecewise linear and convex", so Q(y) is convex piecewise linear (p. 31); dual solution at a trial y gives a supporting linear lower bound (pp. 32-33); "optimality cuts create an outer linearization of Q(y)" (p. 34). Unicut vs multicut (p. 37; multicut converges faster for some problems, citing Birge and Louveaux 1988). Convergence and worst-case remarks (p. 38).
- **Nested Benders (pp. 39-47):** multistage problem viewed as nested two-stage problems (p. 40); solutions passed down the tree and cuts passed up (p. 41); sequencing heuristics fast-forward, fast-back, fast-forward-fast-back (p. 42; FFFB found faster by Wittrock 1985); termination test at every node (pp. 42-43); worked walkthrough (pp. 44-47).
- **Extras (pp. 47-50):** unicut/multicut in nested form, aggregation of stages, parallelisation (Dempster and Thompson 1998), list of alternative methods (p. 49).

## Data / case
None (illustrative made-up numbers in the walkthrough, p. 44).

## Key findings
- (p. 9) Benders' original use was MIP; in stochastic programming all master/subproblems are LPs.
- (p. 31) The expected recourse function is convex and piecewise linear in the first-stage decision.
- (pp. 32-34) Optimality cuts are supporting hyperplanes from subproblem duals; together an outer linearisation; bounds converge.
- (p. 37) Multicut adds one cut per subproblem per iteration.
- (pp. 40-42) Nested Benders: forward pass of decisions, backward pass of cuts; sequencing is heuristic.
- (pp. 49-50) Thompson (1997) concluded only simplex, nested Benders and interior-point methods need to be considered for SP on sequential machines.

## Strengths
- Very readable, step-by-step intuition; good for writing an accessible Theory section.

## Weaknesses / limitations
- Not peer reviewed; deliberately limited references; does not cover SDDP (sampling, stagewise independence, Markov chains). Minor slip: on p. 37 multicut is attributed to "Birge and Louveaux (1969)", but the reference list gives 1988.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: Benders decomposition (`03_theory.tex:302`) master/subproblem, bounds | Derivation from duality; master problem; UB/LB stopping | pp. 9-13 |
| Theory: Benders, optimality cuts as lower approximation of convex function | Q(y) convex piecewise linear; supporting cuts; outer linearisation | pp. 31-34 |
| Theory: two-stage SP and L-shaped method | Deterministic equivalent and L-shaped | pp. 17, 20 |
| Theory: SDDP motivation (nested Benders forward/backward) | Decisions down, cuts up; sequencing heuristics | pp. 39-43 |
| Theory: unicut vs multicut | Definitions | p. 37 |

## Useful quotes (with page numbers)
> "It is sometimes said that optimality cuts create an outer linearization of Q(y)." (p. 34)

## Follow-up references to check (backward snowballing)
- Van Slyke and Wets (1969), L-shaped linear programs, SIAM J. Appl. Math. 17, 638-663.
- Birge and Louveaux (1988), multicut algorithm, EJOR 34(3), 384-392.
- Dempster and Thompson (1998), parallelization and aggregation of nested Benders, Ann. Oper. Res. 81, 163-187.

