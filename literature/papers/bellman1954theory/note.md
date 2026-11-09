---
bibkey: bellman1954theory
bibkey_provisional: true
title: "The Theory of Dynamic Programming"
authors: "Richard Bellman"
year: 1954
venue: "Bulletin of the American Mathematical Society 60(6), 503-515"
peer_reviewed: true
methods: [dynamic-programming, sdp]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Bellman's survey address: defines state variables, decisions as state transformations, policies and optimal policies; states the Principle of Optimality verbatim (p. 504); derives deterministic, stochastic, infinite-horizon and continuous-time functional equations; introduces approximation in function space vs. policy space (value vs. policy iteration)."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Dynamisk_programmering/Bellman1954.pdf
---

# The Theory of Dynamic Programming (Bellman, 1954)

_Page mapping: PDF page n = journal page 502 + n (journal pp. 503-515). Address delivered at the AMS Summer Meeting, Laramie, 3 Sept 1953; received 27 Aug 1954 (p. 503)._

## Research question / purpose
- Survey of "the fundamental concepts, hopes, and aspirations of dynamic programming" (p. 503), created to treat multi-stage decision processes.

## Setting
- **System:** generic "physical system whose state at any time t is determined by a set of quantities which we call state parameters, or state variables" (p. 503). Examples: production lines, inventory, investment, replacement (p. 503).
- **Markets / horizon:** n/a; finite N-stage, infinite, and continuous-time processes.

## Method
- **Terminology (p. 503):** decisions are transformations of the state variables; a sequence of decisions is a *policy*; the best policy under a criterion is an *optimal policy*.
- **Dimensionality argument (pp. 503-504):** enumerating all feasible policies is impractical ("excessive dimensionality"); it is sufficient to have "a general prescription which determines at any stage the decision to be made in terms of the current state of the system" (p. 504). For stochastic processes "the classical enumerative approach is virtually impossible" (p. 504).
- **Principle of Optimality (p. 504):** stated verbatim (see quote).
- **Functional equations:** deterministic N-stage f_N(p) = max_k f_{N-1}(T_k(p)) (eq. 3.3, p. 505); stochastic f_N(p) = max_k ∫ f_{N-1}(z) dG_k(p,z) (eq. 4.2, p. 506) ("the deterministic process may be considered to be merely a particular case of a stochastic process", p. 506); infinite stochastic process (eq. 5.1, p. 506); continuous deterministic process leading to a PDE (secs. 6, 9, pp. 506-510).
- **Duality between functions and policies (p. 506):** knowledge of an optimal policy yields the unique f_N; conversely, all optimal policies can be determined from {f_N}.
- **Solution approaches (sec. 12, pp. 512-513):** "approximation in function space" (successive approximation f_{n+1} = T(f_n), i.e. value iteration) and "approximation in policy space" (iterating on policies, with monotone convergence; i.e. the idea behind policy iteration).

## Data / case
Illustrative examples only: allocation/investment problem (p. 507), stochastic gold-mining (pp. 508-509), calculus of variations (pp. 509-510), eigenvalue problem (pp. 510-511), games of survival (pp. 511-512).

## Key findings
- (p. 504) Principle of Optimality, verbatim.
- (p. 504) DP reduces dimension to that of the decision problem at a single time, by expressing decisions as a function of the current state.
- (pp. 505-506) Recursive functional equations for deterministic and stochastic multistage processes; expected value of the final-state return is the criterion in the stochastic case (p. 506).
- (p. 506) The value function is unique even if optimal policies are not.
- (pp. 512-513) Value iteration (function space) vs. policy-space approximation with monotone convergence.

## Strengths
- Clear, citable, peer-reviewed statement of the principle of optimality and the state/decision/policy vocabulary. More accessible than the 1957 book.

## Weaknesses / limitations
- No computational experiments; the term "curse of dimensionality" is not used here (it appears in later Bellman work; see `rust2008dynamic`, p. 8, which attributes it to Bellman and Dreyfus 1962).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: DP, principle of optimality (`03_theory.tex:170`) | Verbatim statement of the principle | p. 504, sec. 2 |
| Theory: DP, state/decision/policy terminology | Definitions | p. 503 |
| Theory: DP, why not enumerate all decision sequences | Dimensionality argument; decision as function of current state | pp. 503-504 |
| Theory: SDP recursion with expectation | Stochastic functional equation | p. 506, eq. (4.2) |
| Theory: value iteration / policy iteration origin | Approximation in function vs. policy space | pp. 512-513, sec. 12 |

## Useful quotes (with page numbers)
> "PRINCIPLE OF OPTIMALITY. An optimal policy has the property that whatever the initial state and initial decisions are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decisions." (p. 504)

## Follow-up references to check (backward snowballing)
- Bellman (1953), An introduction to the theory of dynamic programming, RAND R-245 (ref. 3, p. 513).
- Bellman (1952), PNAS 38, 716-719 (ref. 5; filed as `bellman1952theory`).
- Arrow, Harris and Marschak (1951), Optimal inventory policy (ref. 2).

