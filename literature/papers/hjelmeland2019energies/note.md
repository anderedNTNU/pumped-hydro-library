---
bibkey: hjelmeland2019energies
title: "Medium-Term Hydropower Scheduling with Variable Head under Inflow, Energy and Reserve Capacity Price Uncertainty"
authors: "Martin N. Hjelmeland, Arild Helseth, Magnus Korpås"
year: 2019
venue: "Energies, 12(1), 189"
peer_reviewed: true
methods: [sddp-time-series, hydro-production-function, uncertainty-modelling, benders-decomposition]
review_sections: [market-participation, modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/Innlimte_referanser_2026-10-29/hjelmeland2019energies.pdf
takeaway: "Non-convex SDDP (MILP forward pass, strengthened Benders cuts) for a Norwegian 3-reservoir system with head-dependent generation and VAR(1) inflow, energy and reserve-capacity prices as objective-coefficient uncertainty; SB cuts give much better policies at ~5× runtime, but gaps stay large (36% with price uncertainty)."
---

# MTHS with variable head and reserve price uncertainty (Hjelmeland et al., 2019)

_Page numbers are the article's own pages (1–15 of Energies 12, 189)._

## Research question / purpose
Can SDDP, improved with strengthened Benders (SB) cuts from SDDiP, solve a **non-convex** medium-term hydropower scheduling (MTHS) problem with **variable head** and uncertainty in **inflow, energy price and reserve-capacity price**, and how can the shape (non-concavity) of the expected future profit (EFP) function be inspected beforehand (abstract, p. 1; contributions p. 2)?

## Setting
- **System:** Norwegian system with 3 reservoirs and 2 power stations (13.8 MW and 365 MW); a short-term and a long-term reservoir both feed the large station (only one can be depleted at a time, different heads) (pp. 9–10, Fig. 5). Same system as in hjelmeland2019tste [7]. No pumping.
- **Markets:** energy + reserve capacity, where reserve capacity is "a composition of the provision of primary and secondary reserves"; market details left to short-term scheduling (p. 3). Symmetric/rotating reserves via constraints (4)–(5).
- **Horizon and resolution:** 104 weekly stages (2 years); 21 time steps per week representing three time blocks of the day (p. 10). MTHS normally covers 1–3 years (p. 1).

## Method
- **Model type:** multistage stochastic MILP (eqs. 1–8, pp. 2–3), solved by SDDP with binary variables kept in the forward pass and relaxed in the backward pass (eqs. 16–23, p. 7).
- **How uncertainty is represented:** a **VAR(1)** model on normalised inflow, energy price and reserve-capacity price (eqs. 14–15, p. 5), with correlations between processes. Prices are **objective-coefficient uncertainty**, handled with the saddle-function approach of Downward, Dowson & Baucke [15]: an auxiliary state u_t carries the price, and cut coefficients for it are the sampled price (pp. 5, 7–8, eq. 29, Fig. 4). Fitted to 70 historical years of inflow and energy prices from a fundamental market model; historical primary-reserve prices for reserve prices (p. 9). 15 branches per stage in the backward pass (p. 10).
- **Solution method:** SDDP with Benders (B) or strengthened Benders (SB) cuts. SB cut: solve the Lagrangian of the MIP once with the LP duals as multipliers to get a tighter right-hand side (eqs. 24–27, pp. 7–8). Convergence not guaranteed (non-concave), result is approximate (p. 8). 3 forward scenarios per iteration, 50 iterations, final simulation with 300 scenarios; C++ + Gurobi 7.5; no SDDP parallelisation (p. 10).
- **Key modelling choices and assumptions:**
  - **Generation function**: non-concave in discharge and net head, modelled as a union of concave regions (one binary per region, i.e. per unit started in a fixed sequence), each bounded by hyperplanes in (q, h) (eqs. 9–13, p. 4, Fig. 1). Avoids bilinear terms and McCormick grids.
  - Rationale: concave discharge-only PQ is fine for energy-only, loosely constrained systems, but when plants run at low output for ancillary services (or environmental minimum flows) the linear model sees more output than feasible and **overestimates profit** (p. 3).
  - **Head function**: concave for most Norwegian reservoirs; high-head plants are less head-sensitive than elsewhere (pp. 4–5, Fig. 2).
  - Weekly decision problem: 1858 constraints, 1152 variables (837 continuous, 315 binary) (p. 10).
  - The Nordic state of the art is hybrid SDP-SDDP with price Markov chain + AR inflow; adding a reserve market extends the Markov chain and raises cost, as in helseth2016 [13] (p. 2). This paper instead uses one VAR(1) for all processes.

## Data / case
- 70 historical years (inflow + fundamental-model prices) for the VAR(1); historical primary reserve prices (p. 9).
- EFP visualisation (p. 6, Fig. 3): extensive form on a tractable tree, one-year horizon, loop over initial reservoir levels for constant, concave, original and non-concave head functions, with and without reserve sales; LP relaxation gives a concave EFP that significantly overestimates the true EFP.

## Key findings
- (p. 6–7) The EFP for the real head function is not highly non-concave, so a cut (concave) approximation is a fair compromise; the head function shape strongly affects EFP shape.
- (p. 11, Table 1) With inflow + reserve + energy price uncertainty: B cuts UB 1,209,510 / LB 502,838 kNOK, **gap 58.4%**, 5 h 17 min; SB cuts UB 820,466 / LB 525,493, **gap 36.0%**, 23 h 59 min. Inflow-only: B gap 47.1% (5 h 52 min); SB gap **8.4%** (34 h 31 min).
- (p. 10) SB cuts give significantly tighter cuts and a better policy; runtime about 5× B cuts; upper bound still improving after 50 iterations.
- (p. 11, Figs. 7–8) Water values with SB cuts are generally lower than with B cuts (tighter RHS lowers the concave EFP).
- (p. 11, Fig. 9) With B cuts the model sees too much future profit and keeps reservoir 2 very high; with SB cuts the reservoir is used better. Water values change sharply around week 18 (spring flood, spillage risk).
- (p. 11) Including objective-term (price) uncertainty slows convergence markedly; small validation cases converge slowly (p. 11).
- (p. 13) Conclusions: model includes correlations among processes and detailed hydro; SB cuts better policy at ~5× time; price uncertainty slows convergence.

## Strengths
- One correlated stochastic model for inflow, energy and reserve prices (no independence assumption between inflow and price).
- Head-dependent, unit-sequenced generation function inside SDDP.
- Simple EFP-visualisation procedure to judge whether convex approximations are acceptable.
- Transparent bounds and run times.

## Weaknesses / limitations
- Very large optimality gaps with price uncertainty (36–58%), only 3 forward scenarios per iteration and 50 iterations; policy quality uncertain.
- Reserve product is an abstract aggregate of primary + secondary reserves; no activation, no market timing.
- No comparison of profit with vs without reserves, so the value of reserve participation is not reported.
- Conventional hydro, no pumping; no out-of-sample/historical evaluation.
- Convergence not guaranteed (non-concave).

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review: SDDP common/state of the art in hydro scheduling | SDDP "commonly used"; hybrid SDP-SDDP is "currently the state-of-the-art in the Nordic power system" | pp. 1–2, Sec. 1 |
| Method: Markov chain vs VAR for price uncertainty | Markov chain avoids bilinear price×generation; extra markets enlarge the chain | p. 2 |
| Method: inflow–price correlation weak at weekly level | Cites [12] that weekly inflow–price correlation is not too significant | p. 2 |
| Limitations: linear PQ overestimates profit at low output / reserves | Rationale for non-concave generation function | p. 3, Sec. 2.1 |
| Model: head effects for Norwegian plants | High head, concave head function, less head-sensitive | pp. 4–5 |
| Theory: convergence/bounds with non-convexity | B vs SB cuts, gaps 8–58%, runtime ×5 | pp. 7–8, 10–11, Table 1 |
| Lit review (market participation): reserves in SDDP | Reserve capacity (primary+secondary) with stochastic price | pp. 3, 5, 9 |

## Useful quotes (with page numbers)
> "For the MTHS problem, a hybrid stochastic dynamic programming (SDP)-SDDP method is currently the state-of-the-art in the Nordic power system." (p. 2)

> "the linear optimization model will observe a higher power output than what is physically feasible and thus overestimate the system's potential profit" (p. 3)

## Follow-up references to check (backward snowballing)
- [15] Downward, Dowson, Baucke (2018/2020), SDDP with stagewise-dependent objective uncertainty (Oper. Res. Lett. 48(1), 2020).
- [16] Hjelmeland, Helseth, Korpås (2018), impact of modelling details on the generation function, J. Phys. Conf. Ser. 1042.
- [12] Gjelsvik, Mo, Haugstad (2010), Handbook chapter on SDDP in hydro-dominated systems.
- [6] Zou, Ahmed, Sun (2018), SDDiP, Math. Program.
- [23] Steeger (thesis/chapter cited for non-convexity indices, "Chp. 7.2") (unverified).

