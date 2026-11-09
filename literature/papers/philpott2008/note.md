---
bibkey: philpott2008
title: "On the convergence of stochastic dual dynamic programming and related methods"
authors: "A. B. Philpott, Z. Guan"
year: 2008
venue: "Operations Research Letters 36(4), 450-455"
peer_reviewed: true
methods: [benders-decomposition, sddp-time-series]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/philpott2008.pdf"
takeaway: "Proves almost-sure finite convergence of a broad class of sampling-based multistage Benders algorithms (SDDP, AND, ReSa, CUPPS; class 'DOASA') from the finiteness of distinct cut coefficients, needing only that every scenario is sampled infinitely often in the forward pass and every outcome in the backward pass; repairs a gap in earlier proofs."
---

# Convergence of SDDP and related methods (Philpott & Guan, 2008)

_Version filed: author manuscript from the Humboldt-Universitaet open archive (14 pages). **Page numbers below are manuscript (= PDF) pages.** Journal pages are 450-455; no exact mapping is possible._

_Tagging note: `benders-decomposition` because the paper analyses multistage (sampled) Benders decomposition. `sddp-time-series` because the proof assumes stagewise-independent RHS randomness, with ARMA RHS processes covered by state augmentation (p. 3). The paper does **not** treat Markov-chain SDDP; see "Relation to our work" for how the result is carried over to our MC-SDDP._

## Research question / purpose
- Give a simpler, rigorous proof of almost-sure convergence for a broad class of sampling algorithms for multistage stochastic LPs that includes SDDP, AND, ReSa and CUPPS (pp. 1-2).
- Remove an unstated independence assumption ("Assumption 1") used in the earlier proofs of Chen & Powell (1999) and Linowsky & Philpott (2005) (p. 2, pp. 8-9).
- Make explicit the "finiteness argument" Donohue alluded to (convergence follows from re-sampling) (p. 2).

## Setting
- **System:** generic multistage stochastic linear programs with recourse; SDDP's energy/hydro use is mentioned only as motivation (p. 1).
- **Markets:** n/a.
- **Horizon and resolution:** T stages, finite.

## Method
- **Model type:** multistage stochastic LP, nested form [LP1]-[LPt] with Q_{T+1} = 0 (p. 3).
- **Assumptions** (pp. 2-3):
  - (A1) randomness only in constraint right-hand sides;
  - (A2) finite discrete outcome set per stage with positive probabilities;
  - (A3) stagewise independence (an ARMA RHS process is allowed through state augmentation with independent residuals, citing Infanger & Morton);
  - (A4) every stage LP feasible region nonempty and bounded.
- **How uncertainty is represented:** finite scenario tree, stagewise independent.
- **Solution method:** outer approximation of the expected cost-to-go by cuts; approximate problems [AP_t^k] give lower bounds; first cut is the trivial cut theta >= -infinity; cuts are never removed, so optimal values are monotone in k (pp. 3-4).
  - *Cut Calculation Algorithm (CCA)* (p. 5): sample a subset of outcomes, solve, store extreme-point duals; for each outcome pick the best stored dual; average with probabilities into a cut. By (A1) the dual extreme points do not depend on the outcome, so stored duals give valid cuts.
  - *Lemma 1* (pp. 6-7): although dual vectors grow with k, the set of distinct cut coefficient pairs at each stage is finite, and after some iteration k_t no new cut appears.
  - *DOASA class* (pp. 7-8): forward pass samples one outcome per stage (one scenario), backward pass applies CCA at the forward states. Two sampling properties:
    - **FPSP**: every scenario is traversed infinitely many times w.p. 1 in the forward pass;
    - **BPSP**: every stage outcome is visited infinitely many times w.p. 1 in the backward pass.
    Independent sampling with positive probabilities satisfies both by Borel-Cantelli (p. 8).
  - *DOASA-N* (fixed set of N pre-sampled scenarios): converges in finitely many iterations to a policy whose value is a lower bound, but not necessarily optimal (Lemma 2, p. 10). With the full universe of scenarios and BPSP it converges to an optimal solution (Lemma 3, pp. 10-11).
  - *Theorem 4* (p. 12): under FPSP and BPSP, DOASA converges w.p. 1 to an optimal solution of [LP1] in a finite number of iterations.
- **Key modelling choices and assumptions:** linear, RHS-only uncertainty, finite outcomes, bounded feasible stage problems (relatively complete recourse is implied by A4).

## Data / case
- None (purely theoretical).

## Key findings
- (pp. 2, 8-9) Earlier proofs for CUPPS (Chen & Powell) and MSBD (Linowsky & Philpott) rely on an implicit assumption that a convergent subsequence of iterates is independent of the sampled outcomes; without it they are incomplete.
- (pp. 6-7, Lemma 1) Finitely many distinct cuts can ever be generated per stage.
- (p. 10, Lemma 2) An algorithm that only re-traverses a fixed sample of N scenarios converges finitely, but only to a policy whose value is a lower bound on the optimal expected cost.
- (p. 12, Theorem 4) Almost-sure finite convergence of DOASA under FPSP and BPSP.
- (p. 13) SDDP, AND and ReSa use independent forward sampling and solve all outcomes in the backward pass, so BPSP holds trivially and FPSP follows by Borel-Cantelli. The authors note that "some commercial implementations of SDDP do not re-sample" and are therefore closer to DOASA-N than to DOASA.
- (p. 13, Lemma 5) The Sample Intersection Property of Linowsky & Philpott plus independent sampling implies FPSP/BPSP; their Lemma 8 remains unproven without independent backward sampling.

## Strengths
- Short, clean proof based on two checkable sampling properties.
- Makes explicit the practical requirement: forward scenarios must be **re-sampled** each iteration.
- Widely cited as the standard convergence reference for SDDP (e.g. by `dowson2020` p. 16, `philpott2012` p. 13, `helseth2015efficient` p. 14292).

## Weaknesses / limitations
- Finite convergence is "almost sure" but says nothing about the rate; with an astronomically large number of scenarios it gives no practical guarantee (this critique is made explicitly in `shapiro2020`, PDF p. 11).
- Requires RHS-only, stagewise-independent, finite-outcome LPs; objective (price) uncertainty and Markov chains are not covered directly.
- Manuscript version; journal pagination differs.

## Use it for... (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: SDDP convergence (w.p. 1, finite) | Theorem 4 under FPSP/BPSP | p. 12; properties p. 8 |
| Theory: SDDP as sampled multistage Benders with outer approximation; LB from cuts | [AP_t^k] approximations, monotone LB | pp. 3-4 |
| Theory: assumptions behind SDDP (RHS uncertainty, finite outcomes, stagewise independence, ARMA via state augmentation) | (A1)-(A4) | pp. 2-3 |
| Method: why forward paths must be re-sampled each iteration | DOASA-N (fixed sample) only converges to a lower-bounding policy; commercial codes that do not re-sample | p. 10, p. 13 |
| Method: one scenario per forward pass is a valid SDDP variant | DOASA samples a single scenario per iteration | pp. 7-8 |

## Useful quotes (with page numbers)
> "Some commercial implementations of SDDP do not re-sample and so are more akin to DOASA-N than DOASA." (p. 13)

## Follow-up references to check (backward snowballing)
- Chen & Powell (1999), CUPPS, JOTA 102.
- Linowsky & Philpott (2005), convergence of sampling-based decomposition, JOTA 125.
- Donohue & Birge (2006), abridged nested decomposition.
- Infanger & Morton (1996), cut sharing with interstage dependency, Math. Prog. 75.
- Girardeau, Leclere & Philpott (2015), extension to convex problems (cited by `dowson2020`).

