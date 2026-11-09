---
bibkey: dantzig1955linear
bibkey_provisional: true
title: "Linear Programming under Uncertainty"
authors: "George B. Dantzig"
year: 1955
venue: "Management Science 1(3-4), 197-206"
peer_reviewed: true
methods: [two-stage-stochastic, multistage-scenario-trees]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Founding paper of stochastic programming with recourse: first-stage decisions are fixed before uncertainty, later-stage activities adapt; proves the expected recourse cost is convex in the first-stage decision (two-stage and m-stage), shows the m-stage problem reduces recursively (as in DP) and that a discrete-scenario two-stage problem is one large LP (deterministic equivalent)."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Stokastisk_programmering/Dantzig1955.pdf
---

# Linear Programming under Uncertainty (Dantzig, 1955)

_Page mapping: PDF page n = journal page 196 + n (journal pp. 197-206; PDF page 11 is an INFORMS copyright page). The PDF is a scan with no text layer, so `paper.txt` is (nearly) empty; this note was written from the page images. Author at the RAND Corporation._

## Research question / purpose
- Extend LP to uncertain demands (stimulated by A. Ferguson's airline fleet allocation problem, p. 197).
- Models where activities are divided into two or more stages; only first-stage quantities must be fixed in advance, later stages depend on earlier stages and on random demands (Summary, p. 197).
- Assumes *complete recourse*: "whatever be the choice of activities in the earlier stages ... there is a possible choice of activities in the latter stages" (p. 197).

## Setting
- **System:** generic; examples are a minimum-expected-cost diet (pp. 197-198), shipping to an outlet with uncertain demand (two-stage, p. 198), a three-stage extension with storage carried between stages (p. 199), resource allocation to destinations with uncertain demand (pp. 199-202).
- **Horizon:** two-stage and general m-stage.

## Method
- **Model type:** two-stage and multistage stochastic linear programs with recourse (general structure eq. 20, p. 202; m-stage staircase eq. 29, p. 204).
- **How uncertainty is represented:** random right-hand sides with known distributions; finite scenarios b2^(1..k) with probabilities p_i in the solution of Example 5 (p. 206).
- **Objective:** "minimize total expected costs" (p. 200); footnotes note Markowitz's mean-variance alternative when variation matters (pp. 198, 200).
- **Key results:**
  - Scarf's theorem: expected shortage cost is convex in supply (pp. 200-201); a lemma that expectations of convex functions are convex (p. 201).
  - Convex expected recourse cost can be piecewise-linearised to give a standard LP (pp. 201-202).
  - Two-stage convexity theorem: φ0(X1) = E[inf over X2 of φ(X1, X2 | E2)] is convex, and the optimal first stage minimises φ0 (eq. 21, p. 203; proof pp. 203-204).
  - m-stage theorem: an equivalent (m-1)-stage problem is obtained by replacing the last stage with E inf over X_m (eq. 30, p. 205). Dantzig notes this "is a standard technique in 'dynamic programming'" and refers to Bellman (p. 205).
  - Deterministic equivalent: with k scenarios the two-stage problem is one LP with first-stage X1 and scenario copies X2^(i) (eq. 33, p. 206), and "it appears likely that techniques can be developed to handle large k" (p. 206).
  - Expected-value substitution is in general not optimal (p. 206), although it may be a good starting solution (Ferguson case improved by 15%).

## Data / case
Toy numerical example: ship 100 items, demand uniform on [70, 80]; optimal shipment 75 with expected cost 77.5 (pp. 205-206).

## Key findings
- (p. 197) Two-/multi-stage structure with complete recourse.
- (p. 203) Convexity of the expected second-stage (recourse) cost in the first-stage decision.
- (p. 205) Recursive stage-by-stage reduction, explicitly linked to DP; but "it appears hopeless that such functions can be computed except in very simple cases" (p. 205): the convexity is valuable because local optimum = global optimum.
- (p. 206) Deterministic equivalent LP for finite scenarios; replacing random vectors by their means is not optimal in general.

## Strengths
- Origin of the recourse model; the convexity results are exactly what later make cutting-plane methods (L-shaped, nested Benders, SDDP) valid.

## Weaknesses / limitations
- No algorithm for large scenario counts; only toy examples. Proof for unbounded φ omitted (p. 204).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: Stochastic optimisation, origin of recourse | Two-/multi-stage LP under uncertainty, complete recourse | p. 197 (Summary) |
| Theory: Two-stage, recourse function convex | Convexity theorem for expected second-stage cost | pp. 203-204, eq. (21) |
| Theory: Multistage, stage-wise recursion (link to DP) | m-stage reduction, "standard technique in dynamic programming" | p. 205, eq. (30) |
| Theory: deterministic equivalent / scenario LP | Finite-scenario LP | p. 206, eq. (33) |
| Theory: EVPI / why not just use expected values | Expected-value substitution not optimal in general | p. 206 |
| Theory: SDDP cuts valid because value function convex | Convexity of expected recourse cost | pp. 200-205 |

## Useful quotes (with page numbers)
> "it is not possible to get in a position where the programming problem admits of no solution." (p. 197, on complete recourse)

## Follow-up references to check (backward snowballing)
- Bellman (1953), An introduction to the theory of dynamic programming, RAND R-245 (ref. 1, p. 206).
- Markowitz (1953), Portfolio selection thesis (ref. 5).
- Ferguson and Dantzig (1954), RAND RM-1369 (ref. 4).

