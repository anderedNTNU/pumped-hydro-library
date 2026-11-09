---
bibkey: rust2008dynamic
bibkey_provisional: true
title: "Dynamic Programming"
authors: "John Rust"
year: 2008
venue: "The New Palgrave Dictionary of Economics, 2nd ed. (Palgrave Macmillan); this file is the author's draft dated 5 April 2006"
peer_reviewed: false
methods: [dynamic-programming, sdp, adp-reinforcement-learning]
review_sections: []
relevance: background
read_by: []
added: 2026-11-04
takeaway: "Concise encyclopedia survey of DP: history (Massé 1944 reservoir management as an early backward-induction application; Bellman coined the name at RAND), Bellman equation and principle of optimality, contraction/fixed-point theory, value vs policy iteration, and the curse of dimensionality (O([ND]^T) history-dependent vs O(NDT) Markovian) with ways to break it."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Dynamisk_programmering/Rust2008.pdf
---

# Dynamic Programming (Rust, 2008)

_Page numbers below are the draft's own page numbers (= PDF page). The published Palgrave entry has different pagination (not checked); cite the published version only after checking pages, or cite the draft explicitly._

## Research question / purpose
- Encyclopedia entry: brief history of DP (Sec. 2), main theory and relation to game theory and control (Sec. 3), survey of numerical DP (Sec. 4), and econometric use of DP models (Sec. 5) (p. 2).

## Setting
- Economics-oriented; generic sequential decision problems (SDPs) under uncertainty.

## Method / content
- **History (p. 2):** backward induction discovered independently in the mid-1940s (von Neumann and Morgenstern 1944; Wald 1947; Arrow, Blackwell and Girshick 1949). "Other early applications of backward induction include the work of Pierre Massé (1944) on statistical hydrology and the management of reservoirs" (p. 2). Bellman recognised the common structure and coined "dynamic programming" at RAND from 1949 (p. 2, fn. 2 with the anecdote on the name).
- **Theory (Sec. 3, pp. 3-14):** SDP definition; backward induction and the Bellman equation (p. 5); principle of optimality (Sec. 3.3, pp. 5-7); stationary Markovian infinite-horizon problems and the Bellman operator as a contraction (Sec. 3.4, pp. 8-10); time consistency limits (Sec. 3.6, p. 14).
- **Curse of dimensionality (pp. 8, 18-22):** history-dependent finite-horizon problems need O([ND]^T) operations; Bellman and Dreyfus (1962) named this the curse of dimensionality (p. 8, 18). With Markovian structure and time-separable utility it falls to O(NDT) (p. 19). Deterministic integration/approximation of continuous states suffers a curse in dimension d (pp. 21-22); Monte Carlo randomisation can break the curse for integration but not for nonconvex optimisation (p. 22).
- **Algorithms (pp. 19-24):** discretisation, function approximation, "neuro-dynamic programming" (p. 20), value iteration (successive approximations) and policy iteration (Howard 1960), the latter equivalent to Newton's method (pp. 23-24).

## Data / case
None.

## Key findings
- (p. 2) Massé (1944) used backward induction for reservoir management: a nice historical bridge between DP and hydropower.
- (p. 8, p. 18) Curse of dimensionality defined and attributed to Bellman and Dreyfus (1962).
- (p. 19) "The key to breaking the curse of dimensionality is the ability to recognize and exploit special structure in an SDP problem."
- (p. 22) Random algorithms (Monte Carlo) break the curse for integration; not for general nonconvex optimisation.

## Strengths
- Authoritative, compact overview with history; good for a single background citation on DP history and the curse of dimensionality.

## Weaknesses / limitations
- Draft, not peer reviewed; economics focus; no SDDP or hydro algorithms beyond the Massé mention; page numbers differ from the published entry.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: DP history, Bellman/RAND | Origins of backward induction; Bellman coined the term | p. 2, Sec. 2 |
| Background/Theory: DP used for reservoirs from the start | Massé (1944) reservoir management | p. 2 |
| Theory: curse of dimensionality (`03_theory.tex`, DP section, currently cites `labadie2004`) | Definition, O([ND]^T) vs O(NDT), Bellman and Dreyfus 1962 | pp. 8, 18-19 |
| Theory: value iteration vs policy iteration | Contraction mapping, Howard 1960, Newton equivalence | pp. 9-10, 23-24 |
| Theory: sampling-based approximation (link to SDDP) | Monte Carlo breaks the curse for integration | p. 22 |

## Useful quotes (with page numbers)
> "The key to breaking the curse of dimensionality is the ability to recognize and exploit special structure in an SDP problem." (p. 19)

## Follow-up references to check (backward snowballing)
- Massé, P. (1945), "Application des probabilités en chaîne à l'hydrologie statistique et au jeu des réservoirs", and Massé (1946), Les réserves et la régulation de l'avenir (refs. [54], [55]). Note: the text says "Massé (1944)" but the bibliography lists only 1945 and 1946; cite Massé with care.
- Bellman and Dreyfus (1962), Applied Dynamic Programming.
- Puterman (1994), Markov Decision Processes.

