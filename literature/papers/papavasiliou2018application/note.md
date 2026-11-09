---
bibkey: papavasiliou2018application
bibkey_provisional: true
title: "Application of Stochastic Dual Dynamic Programming to the Real-Time Dispatch of Storage Under Renewable Supply Uncertainty"
authors: "Anthony Papavasiliou, Yuting Mou, Léopold Cambier, Damien Scieur"
year: 2018
venue: "IEEE Transactions on Sustainable Energy 9(4) (DOI 10.1109/TSTE.2017.2748463); filed copy is the authors' manuscript"
peer_reviewed: true
methods: [sddp-time-series, uncertainty-modelling]
review_sections: [modelling-phs-plants, market-participation]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDDP_i_vannkraft/Papavasiliou2018.pdf"
takeaway: "SDDP (FAST toolbox, 10-node lattice, 96 × 15-min stages) for real-time dispatch of German pumped hydro under multiplicative-AR renewable forecast error: stochastic policy beats a fixed day-ahead PHS schedule by ~1.1–1.2% of daily cost; perfect foresight adds only 0.8%."
---

# SDDP for real-time dispatch of storage (Papavasiliou et al., 2018)

> **Page convention.** The filed PDF is the authors' manuscript (from ap-rg.eu), numbered pp. 1–11 (+ references). Page numbers below are **manuscript pages**, not journal pages. The published version is IEEE TSTE vol. 9, no. 4, 2018; the journal page range (believed 1760–1768) is unverified. Cite the published version but check page numbers there.

## Research question / purpose
Can multi-stage stochastic economic dispatch, solved with SDDP, manage pumped hydro storage in **real-time** operations under renewable supply uncertainty, and what is it worth compared with a deterministic policy that fixes the PHS schedule from day-ahead? (pp. 1–2)

## Setting
- **System:** German power system 2013–2014: 228 buses, 312 lines, 292 conventional units; aggregate PHS 5.867 GW and 38 GWh storage; round-trip efficiency 76.5% (p. 6).
- **Markets:** system operator perspective (cost minimisation). Unit commitment fixed from a weekly day-ahead UC with primary, secondary and tertiary reserve requirements; then real-time economic dispatch (p. 6).
- **Horizon and resolution:** 24 h with 15-min steps → 96 stages (Thursday 25 Sept 2014) (p. 6).

## Method
- **Model type:** multi-stage stochastic LP (linearised DC power flow, ramp limits, piecewise-linear costs, load and production shedding) (pp. 5–6).
- **How uncertainty is represented:** renewable production = day-ahead forecast × ratio y_t, with a **multiplicative AR(1)** model y_{t+1} = (c + φ·y_t)·ε_t (after Cabral); ε_t discretised into 10 equally likely quantile nodes per stage (p. 4). The AR state y_t is part of the decision state, so the noise is stagewise independent (pp. 3–4). The uncertainty structure is a "lattice", described as a discrete Markov process but implemented with serial independence (p. 3, fn. 1). Multiplicative model energy score 0.26 vs 0.46 for additive AR(1) (p. 5).
- **Solution method:** SDDP in the authors' open-source MATLAB **FAST** toolbox (forward Monte Carlo passes for upper bound, backward passes for cuts; lower bound from stage 1) (p. 3). Settings: 10 nodes, 50 forward samples, 10 iterations, 4.3 h, gap 2.8% (Table I, p. 6).
- **Key modelling choices and assumptions:** PHS stored energy s_g = s_{g,t−1} + 0.25·(η_d·pd_g − pp_g/η_p) (p. 5); no feasibility cuts needed because of load shedding (p. 3); unit commitment fixed in real time (p. 4).

## Data / case
ENTSO-E transparency (load, renewables 2013–2014, conventional capacity), EEX (PHS), regelleistung.net (reserve requirements) (p. 6).

## Key findings
- (p. 6, Table I) Lattice size trade-off: 4 nodes converge well but represent uncertainty coarsely (worse cost); 20 and 100 nodes worse gaps and longer runs; 10 nodes chosen. Literature uses K = 2–100 nodes, I = 5–3000 iterations, M = 1–50 samples.
- (p. 4, fn. 3) The Pereira–Pinto stopping rule (lower bound within 95% CI of upper bound) "may lead to premature convergence".
- (p. 7, Table II) Daily cost: perfect foresight 18,231 k€, stochastic 18,378 k€, deterministic 18,594 k€. Text: stochastic saves 1.2% of deterministic cost; perfect foresight a further 0.8% (abstract says 1.1%).
- (p. 7, Fig. 4–5) Stochastic PHS schedule varies widely across outcomes; deterministic schedule tracks its median. The stochastic policy generates or pumps more aggressively depending on whether renewables exceed or fall short of forecast.
- (p. 8, Fig. 6) Optimal storage use tends to equalise marginal prices across hours, outcomes and locations.
- (p. 8, Table III) Without transmission constraints the value of the stochastic solution drops to 0.3%; ramp constraints have negligible effect; "Stochastic Hydro" (only PHS from SDDP, rest myopic) captures almost all the benefit. Multi-period anticipation for storage matters more than look-ahead for thermal units.
- (p. 9) Spatial correlation: using 10 historical analogue days as equally likely nodes changes value functions by 7.5% on average (L1), < 10% in all stages.
- (p. 9) Run time ∝ K·I·M·H; (p. 10) online decision from stored cuts takes 0.027 s per stage problem; value functions apply even for realisations not in the lattice, unlike scenario-tree decisions.
- (p. 9) Weekly or monthly PHS models with coarse steps can produce storage value functions that feed the real-time model.

## Strengths
- Clear, compact explanation of SDDP mechanics, lattice, bounds and stopping rules, with honest run-time and convergence reporting.
- Shows why value functions (cuts) give a policy that can be evaluated on realisations outside the training lattice (p. 10).
- Realistic large network case.

## Weaknesses / limitations
- Single day, single case; only 10 SDDP iterations, gap 2.8%, while the value of stochastic solution is ~1%, which is close to the optimality gap.
- System operator perspective, not an owner; no prices, no reserves in real time (reserves only in the UC step).
- Serial independence plus AR state rather than a true Markov chain; the improvement versus deterministic is confirmed only at 94.5% confidence (p. 7, fn. 7).
- Manuscript version; abstract (1.1%) and text (1.2%) disagree slightly.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: SDDP forward/backward passes, bounds, NLDS | Concise algorithm description | pp. 2–3, Sec. II |
| Theory: stopping rule and premature convergence | Pereira–Pinto criterion + caution | p. 4, fn. 3; p. 3–4 Sec. II-D |
| Theory: lattice / Markov process terminology | Lattice definition, serial independence assumption | p. 3, Sec. II-C, fn. 1; Appendix A p. 10–11 |
| Method: choice of number of nodes per stage | Table I trade-off and literature ranges | p. 6, Table I |
| Method: policy evaluation out of sample with stored cuts | Value functions usable for unseen realisations | p. 10, Sec. V-B |
| Method: chaining coarse long-term value functions into finer models | Explicit suggestion | p. 9, Sec. V-A |
| Uncertainty modelling: AR process in state variable vs Markov lattice | AR in state; multiplicative AR; spatial-correlation options | pp. 4–5, Sec. III-A; p. 9, Sec. IV-D |
| Lit. review: PHS modelling / value of stochastic solution for PHS | VSS ≈ 1.1–1.2%, perfect foresight 0.8% | p. 7, Table II |

## Useful quotes (with page numbers)
> "dispatching pumped hydro resources while being mindful of the multi-period evolution of the system is more crucial than dispatching conventional resources with a short look-ahead" (p. 9)

## Follow-up references to check (backward snowballing)
- [29] Cabral (2016), multiplicative autoregressive multivariate periodic inflow model, PhD thesis, UFRJ.
- [27] Homem-de-Mello, de Matos & Finardi (2011), sampling strategies and stopping criteria for SDDP, *Energy Systems* 2(1):1–31.
- [26] Shapiro (2011), analysis of SDDP, *EJOR* 209:63–72 (the premature-convergence caution in fn. 3; already in our library as `shapiro2011`).
- [28] Shapiro, Tekaya, da Costa & Soares (2013), risk-neutral and risk-averse SDDP, *EJOR* 224:375–391.
- [7] Deane, McKeogh & Ó Gallachóir (2013), intertemporal targets for large PHS with stochastic optimisation, *IEEE TPWRS* 28(3):2147–2155 (inbox has `Deane2013.pdf`).
- [9] Nürnberg & Römisch (2002), two-stage planning model for hydro-thermal power scheduling under uncertainty, *Optim. Eng.* 3(4):355–378.

