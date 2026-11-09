---
bibkey: grini2023
title: "A stochastic policy algorithm for seasonal hydropower planning"
authors: "Håkon S. Grini, Anders S. Danielsen, Stein-Erik Fleten, Andreas Kleiven"
year: 2023
venue: "Energy Systems (Springer), online first, doi:10.1007/s12667-023-00609-9"
peer_reviewed: true
methods: [sddp-markov-chain, heuristics-simulation, two-stage-stochastic, uncertainty-modelling, hydro-production-function]
review_sections: [modelling-phs-plants]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/111_Grini_2023_A_stochastic_policy_algorithm_for_seasonal_hydropower_planning.pdf
takeaway: "NTNU benchmark of Markov-chain SDDP (125 price×inflow states per week, 2-year horizon) against rolling-intrinsic and a new sampled two-stage reoptimisation heuristic (STRO) on a Norwegian cascade (Matre Haugsdal); RI reaches 97.5% and STRO(7) 98.7% of the SDDP upper bound."
---

# Stochastic policy algorithm (STRO) vs SDDP for seasonal hydro planning (Grini et al., 2023)

_Our PDF is the open-access online-first version without journal page numbers; pages below are **PDF pages 1–24**. Final volume/pages not in our bib entry (unverified). The bib entry lists only "Grini, Håkon S. and others"; full author list: Grini, Danielsen, Fleten, Kleiven._

## Research question / purpose
How do forecast-based reoptimisation heuristics compare with SDDP for medium-term (seasonal) reservoir management, and can a new **Scenario-based Two-stage ReOptimization (STRO)** heuristic, which samples a few future scenarios at every decision and allows a non-deterministic ("stochastic") policy, close the gap (abstract, PDF p. 1; contributions pp. 2–3)? Motivation: SDDP needs convexity and stagewise independence, so serial correlation is handled by a linear state extension or by **discretising the exogenous state (Markov chain)**, which induces discretisation error (p. 2); heuristics allow any price/inflow model and non-convexities (p. 12).

## Setting
- **System:** Matre Haugsdal (180 MW, built 2016) and Vemundsbotn (1976) plants with six connected reservoirs in the Matre watercourse, western Norway; data from Eviny (pp. 15–17, Fig. 5, Tables 3–4). Reservoirs are "fast" (high inflow relative to storage), e.g. Gobotvatn 22.0 Mm³ with 134.6 Mm³/yr inflow, Svartevatn 60.8 Mm³, Skjerjevatn 70.5 Mm³ (pp. 16–17, Table 4). No minimum discharge; constant level limits. Some Table 3 cells garbled in extraction (unverified). No pumping.
- **Markets:** energy only (price-taker, revenue maximisation, operating costs ignored) (p. 4).
- **Horizon and resolution:** 2 years, **104 weekly stages** (p. 17). One decision per week (no intra-week resolution); discount factor γ; end-of-horizon value Φ_i(l_{i,T}) (p. 7, eq. 4).

## Method
- **Model type:** convex multistage stochastic LP for SDDP; same model re-solved as deterministic (RI) or two-stage stochastic LPs (STRO, eq. 7, p. 10).
- **How uncertainty is represented:**
  - *Price:* Schwartz–Smith two-factor model (short-term + long-term + seasonal factor on log price), estimated by Kalman filter + MLE from smoothed futures curves (Montel, trading 2006–2018); simulations start 1 Jan 2019 (pp. 6, 17).
  - *Inflow:* normalised, PCA-reduced AR(1) per component, back-transformed; negative values truncated to 0 (eq. 1); hourly inflow data 2009–2019 (pp. 6, 17).
  - *For SDDP:* 200k samples of each exogenous variable **discretised into a Markov chain with 125 discrete states per stage, each a combination of price and inflow**; no further reduction (p. 18).
  - *For RI/STRO:* continuous models directly; 1000 seeded level-1 scenarios (p. 18).
- **Solution method:** SDDP (Python package of Ding, Ahmed & Shapiro [10], gurobipy), 2000 iterations; RI = re-solve deterministic expected-value problem each stage; STRO(N) = each stage, sample N level-2 scenarios conditional on the current state, solve a two-stage LP with non-anticipative first stage, implement first-stage decision (pp. 9–11, 15).
- **Key modelling choices and assumptions:**
  - Head effects: head as piecewise-linear (concave, so SOS-2 unnecessary) function of average level; bilinear head×discharge via **McCormick envelopes** to stay convex (pp. 4, 7–8, Appendices A–B). Head variation 4.0–6.5% of head in this system (p. 4).
  - Constant turbine efficiency factor η_i (p. 7). No water delay (p. 7).
  - Marginal water value = slope of expected revenue vs initial level; decreases with level (p. 4).

## Data / case
- Hardware: Dell PowerEdge R640 nodes, 2× Xeon Gold 5115, 96 GB, up to 40 parallel processes (p. 15, Table 2).
- Results averaged over 10 runs, relative to SDDP (to hide confidential values) (p. 17).

## Key findings
- (p. 18, Table 5) Revenue relative to SDDP (=100): **RI 97.546%**, STRO(1) 97.249, STRO(2) 98.115, STRO(3) 98.411, STRO(4) 98.548, STRO(5) 98.611, STRO(6) 98.654, **STRO(7) 98.674**; run-to-run std ≈ 0.48–0.49%.
- (p. 18) RI is within 2.5% of SDDP, in line with Braaten et al. [4]; STRO(7) within 1.4%; biggest gain from N = 1 to 2, diminishing after; STRO beats RI for N ≥ 2. (Abstract rounds to "2.5 to 1.3%", p. 1.)
- (p. 18) Caveat: SDDP gives an upper bound on the discretised model, RI/STRO give lower bounds on the continuous model, so a gap always remains; seeding could not be applied to SDDP.
- (p. 19, Table 6) Runtimes: SDDP 11.38 h (2000 iterations, excl. discretisation); STRO(1)/RI 0.26 h; STRO(7) 11.88 h (40 parallel processes).
- (pp. 19–20) SDDP upper bound decreased only 0.2% after 200 iterations and 0.1% after 500; the last 1000 iterations gave < 0.03%. 125 states per stage is "relatively small".
- (p. 20) Medium-term planning only passes the value function to short-term planning, so a deterministic policy is not required.
- (p. 20) Limitations: one system, one price/inflow model; non-convex tests left for future work.

## Strengths
- Directly benchmarks **Markov-chain SDDP** against simple, widely used heuristics on a real Norwegian system with realistic price (futures-based) and inflow models.
- Honest discussion of bias (discretisation vs sampling) and of SDDP iteration counts.
- Shows that the RI heuristic is a strong baseline (~2.5% from SDDP).

## Weaknesses / limitations
- Energy only; weekly resolution with no intra-week price shape, so no short-term flexibility value.
- SDDP and heuristics are evaluated on different uncertainty representations (discretised vs continuous), so the comparison mixes policy and model error.
- Results only relative (no absolute revenues); single case; no pumping.
- McCormick relaxation of head is an approximation not quantified.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method: benchmark policies for SDDP | Rolling intrinsic and STRO; RI 97.5%, STRO(7) 98.7% of SDDP | PDF pp. 9–11, 18, Table 5 |
| Method: Markov-chain discretisation of price + inflow | 125 joint states per stage from 200k samples | PDF p. 18 |
| Theory: SDDP needs convexity + stagewise independence; Markov chain vs linear state extension | Discussion of the two approaches and discretisation error | PDF p. 2, p. 12 |
| Theory: SDDP convergence in practice | UB −0.2% after 200 iterations, −0.1% after 500, 2000 run | PDF pp. 19–20 |
| Model: head effects via McCormick | Piecewise head function + McCormick envelope constraints | PDF pp. 7–8, Apps. A–B |
| Model: marginal water value intuition | Slope of expected revenue vs initial level, decreasing in level | PDF p. 4 |
| Data: price model from futures | Schwartz–Smith 2-factor, Kalman/MLE, Montel 2006–2018 | PDF pp. 6, 17 |
| Lit review: SDDP state of the art for seasonal hydro | Statement with refs [12, 31] | PDF p. 2 |

## Useful quotes (with page numbers)
> "This algorithm is state of the art for solving the seasonal hydropower production planning problem" (PDF p. 2)

## Follow-up references to check (backward snowballing)
- [4] Braaten, Gjønnes, Hjertvik, Fleten (2016), linear decision rules for seasonal hydropower planning, Energy Procedia 87.
- [15, 16] Helseth, Mo, Warland — scenario-fan two-stage reoptimisation (cf. `helseth2017`).
- [1] Ávila, Papavasiliou, Löhndorf (2022), parallel and distributed SDDP, CMS.
- [10] Ding, Ahmed, Shapiro (2019), Python package for multistage stochastic programming (MSPPy).
- [11] Downward, Dowson, Baucke (2020), SDDP with stagewise-dependent objective uncertainty.
- [20] Löhndorf & Shapiro (2019), modelling time-dependent randomness in SDDP, EJOR (we have `lohndorf2019`); cited for the linear-state vs discretised (Markov) approaches (PDF p. 2).

