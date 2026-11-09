---
bibkey: bellman1952theory
bibkey_provisional: true
title: "On the Theory of Dynamic Programming"
authors: "Richard Bellman"
year: 1952
venue: "Proceedings of the National Academy of Sciences of the USA 38(8), 716-719"
peer_reviewed: true
methods: [dynamic-programming, sdp]
review_sections: []
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Bellman's first short note on dynamic programming: multistage (possibly stochastic) decision problems reduce to functional equations f(p) = max_k T_k(f), where finding an optimal sequence reduces to finding an optimal first operation; existence/uniqueness proved by successive approximations."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Dynamisk_programmering/Bellman1952.pdf
---

# On the Theory of Dynamic Programming (Bellman, 1952)

_Page mapping: PDF page n = journal page 715 + n (journal pp. 716-719). The PDF is a scan of four page images with no text layer, so `paper.txt` is empty; this note was written from the page images. Communicated by J. von Neumann, 5 June 1952; author at the RAND Corporation._

## Research question / purpose
- Introduces "a class of mathematical problems" arising when "a bounded or unbounded sequence of operations" must be performed to achieve a result, especially when each operation produces a stochastic event whose result is used to determine subsequent operations (p. 716).
- Two "dual" fundamental problems: maximise the yield obtained in a given time, or minimise the time or cost to accomplish a task (p. 716).
- Core idea: the problem of determining an optimal *sequence* of operations "may be reduced to that of determining an optimal first operation" (p. 716). This is the germ of the principle of optimality, though the principle is not stated by name here (it is stated explicitly in Bellman 1954, p. 504; see `bellman1954theory`).

## Setting
- **System:** none; abstract mathematics. Toy examples: searching N boxes for a ball (p. 716), dividing a resource x into two parts with returns g(y) and h(x-y) and depreciation factors a, b (pp. 716-717).
- **Markets:** n/a.
- **Horizon and resolution:** finite or unbounded number of stages.

## Method
- **Model type:** functional equation f(p) = max/min_k T_k(f) (eq. 1.1), typically T_k(f) = g_k(p) + h_k(p) f(S_k p), with S_k a point transformation (eq. 1.2, p. 716). This is the recursive (Bellman) equation in its earliest published form: immediate return plus (discounted/weighted) value of the resulting state.
- **How uncertainty is represented:** stochastic outcomes via probability vectors (Theorem 3, eqs. 2.5-2.7, pp. 717-718).
- **Solution method:** "The proof in all three cases employs the method of successive approximations" (p. 718), i.e. value iteration.
- **Key results:** Theorem 1: unique bounded solution of f(p) = max_k (g_k(p) + h_k(p) f(S_k p)) if |h_k| <= c2 < 1 (a contraction-type condition) (p. 717). Theorems 2-3: existence/uniqueness for the allocation equation and a stochastic search equation (pp. 717-718). Theorems 4-7: explicit solutions of particular equations (pp. 718-719), e.g. the two-option "gold-mining" type equation whose solution is piecewise linear (Theorem 4, p. 718).

## Data / case
None.

## Key findings
- (p. 716) Optimal sequence of decisions reduces to an optimal first decision followed by optimal behaviour from the resulting state; this yields functional equations of the form (1.1)-(1.2).
- (p. 717) DP is "intimately related" to Wald's sequential analysis and to Arrow-Blackwell-Girshick (1949) and Arrow-Harris-Marschak (1951).
- (p. 717) Existence and uniqueness of a bounded solution when the "future" coefficient is bounded by c2 < 1.
- (p. 718) Proofs by successive approximations.
- (p. 719) "Detailed proofs and further results will appear in another publication."

## Strengths
- Earliest published statement of the DP functional equation; short (4 pages); authoritative origin citation.

## Weaknesses / limitations
- Very terse, no proofs, no computational discussion; principle of optimality not named. For a citable verbatim statement of the principle, `bellman1954theory` (p. 504) or the existing `bellman1957` book is better.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: Dynamic Programming, historical origin | First published DP functional equation; "optimal sequence reduces to optimal first operation" | p. 716, eqs. (1.1)-(1.2) |
| Theory: SDP, stochastic transitions | Stochastic version with probability vectors | pp. 717-718, Thm 3 |
| Theory: value iteration / convergence | Existence/uniqueness via successive approximations, contraction-type bound c2 < 1 | pp. 717-718, Thm 1 |

## Useful quotes (with page numbers)
> "the problem of determining an optimal sequence of operations may be reduced to that of determining an optimal first operation." (p. 716)

## Follow-up references to check (backward snowballing)
- Arrow, Blackwell and Girshick (1949), Econometrica 17, 214-244 (p. 719, ref. 1).
- Arrow, Harris and Marschak (1951), Optimal inventory policy (p. 719, ref. 2).
- Wald (1950), Statistical Decision Functions (p. 719, ref. 3).

