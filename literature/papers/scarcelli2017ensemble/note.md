---
bibkey: scarcelli2017ensemble
bibkey_provisional: true
title: "Ensemble of Markovian stochastic dynamic programming models in different time scales for long term hydropower scheduling"
authors: "R.O.C. Scarcelli, M.S. Zambelli, S. Soares, A.A.F.M. Carneiro"
year: 2017
venue: "Electric Power Systems Research 150, 129–136"
peer_reviewed: true
methods: [sdp, uncertainty-modelling, hydro-production-function]
review_sections: []
relevance: background
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/51_Scarcelli_2017_Ensemble_of_Markovian_stochastic_dynamic_programming_models_long_term_hydropower_scheduling.pdf"
takeaway: "Single-reservoir Brazilian hydrothermal SDP: Markov (PAR(1)) inflow models fitted on 1–12-month aggregated inflows, combined in a one-year-ahead deterministic NLP, cut simulated cost 0.4–2.1% versus standard monthly Markovian SDP."
---

# Ensemble of Markovian SDP models at different time scales (Scarcelli et al., 2017)

> **Page convention.** Journal page = PDF page + 128 (PDF p. 1 = p. 129, PDF p. 8 = p. 136).

## Research question / purpose
Can long-term hydropower scheduling (LTHS) under inflow uncertainty be improved by modelling inflows aggregated over longer time scales (2, 3, 4, 6, 12 months) instead of only month to month? Aggregated inflows have a lower coefficient of variation, so a model that "foresees" the coming wet season may decide better than the standard monthly Markovian SDP (MSDP) (pp. 129–131).

## Setting
- **System:** hypothetical single-reservoir hydrothermal systems built from four real Brazilian plants (Furnas, Foz do Areia, Serra da Mesa, Sobradinho) with different hydrological regimes (p. 132, Table 1). Conventional hydro, no pumping.
- **Markets:** none. Centralised cost minimisation: thermal generation covers constant demand minus hydro (p. 130).
- **Horizon and resolution:** monthly stages; the SDP is run backward to a steady-state monthly policy (p. 130). Simulation over May 1932 – April 2012 historical inflows (p. 132).

## Method
- **Model type:** stochastic dynamic programming with a discretised reservoir state and a lagged-inflow state, plus a deterministic one-year-ahead nonlinear model in the proposed variant.
- **How uncertainty is represented:** inflow only. A first-order periodic autoregressive model PAR(1), so inflow is a **Markov chain** conditioned on last month's inflow. Conditional log-normal density (eqs. 11–13), discretised into N inflow ranges with probabilities from integrating the density (eqs. 14–15) (p. 130).
- **Solution method:**
  - *MSDP-M* (standard): recursion α_t(x_{t−1}, y_{t−1}) = min E[ψ(d_t − g_t) + α_{t+1}(x_t, y_t)], with null terminal cost, iterated until the monthly decision functions converge (steady state) (p. 130, eq. 10).
  - *MSDP-A* (proposed): separate MSDP_b models for inflows aggregated over b ∈ {1,2,3,4,6,12} months, each with its own PAR_b(1) model. Each month, their expected inflows (scaled to monthly values by average-inflow shares, eqs. 16–21) and their decisions (giving the end-of-year storage via water balance, eq. 22) feed a deterministic 12-month nonlinear model solved by SQP. Only the first month's discharge is applied (p. 132).
  - Benchmark: deterministic DP with perfect foresight (DP-PF), an upper bound (p. 132).
- **Key modelling choices and assumptions:**
  - Production g = k·h·q with constant efficiency k; net head h = forebay level φ(x̄) − tailrace level θ(u) − penstock loss, with φ and θ polynomials up to 4th degree; head uses average storage over the month (eqs. 2–4, p. 130). Head effects are therefore modelled.
  - Quadratic thermal cost function ψ; demand constant and equal to the plant's installed capacity (p. 132).
  - Spillage is not a decision variable; no evaporation (p. 130).

## Data / case
- Table 1 (p. 132): P_max 1050–1676 MW, active storage 3,805–43,250 hm³, Q_max 1,095–3,601 m³/s.
- Historical monthly inflows 1932–2012 (data from CCEE/NEWAVE deck, p. 132).

## Key findings
- (p. 131, Fig. 2) The coefficient of variation of inflow falls as more months are aggregated, so annual inflows are relatively more predictable than monthly ones.
- (p. 134, Furnas) MSDP-A has 2.6 m³/s less average spillage than MSDP-M, about 6,500 hm³ over the simulation (~34% of reservoir capacity), and about 1.5% lower average cost (≈ US$ 4.7 million/yr at US$ 52.85/MWh).
- (p. 135, Foz do Areia) 2.12% cost reduction; spillage 8 m³/s lower. Relative to perfect foresight, MSDP-M costs +18.6% and MSDP-A +16.5% (Table 5).
- (p. 136) Serra da Mesa 1.14% and Sobradinho 0.4% cost reduction. In all cases MSDP-A keeps higher average storage (higher head → higher productivity) and spills less.
- (pp. 133–135, Tables 2–9) Gap to perfect foresight is large for both SDP variants (≈ 9–19% cost), showing the value of inflow information.

## Strengths
- Clear, reproducible SDP formulation with a Markov (PAR(1)) inflow model and head-dependent production.
- Long historical out-of-sample-like simulation (80 years) with a perfect-foresight bound as reference.

## Weaknesses / limitations
- Single-reservoir, cost-minimising hydrothermal systems with a synthetic constant demand. No prices, no markets, no pumping.
- The proposed MSDP-A is a heuristic combination ("ensemble") of SDP policies and a deterministic look-ahead, not an optimal policy of a single model.
- Simulation uses the same historical record the inflow models were fitted on, so it is not a clean out-of-sample test (in-sample, unverified whether any split was used: none is described).
- Some odd definitions: "efficiency" is defined as the percentage ratio between spillage and discharge, and "productivity" as generation divided by inflow (p. 135).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: SDP and curse of dimensionality | Short statement of SDP as closed-loop policy over discrete states, exponential growth | p. 129, Sec. 1 |
| Method: Markov-chain inflow from PAR(1) | Conditional log-normal model and discretised transition probabilities | p. 130, Sec. 2.1, eqs. 10–15 |
| Discussion: limits of first-order Markov assumption / inflow persistence | Aggregated inflows less variable; multi-month look-ahead improves decisions | p. 131 (Fig. 2); pp. 134–136 |
| Model: head-dependent production function (contrast to our linear choice) | g = k·h·q with polynomial forebay/tailrace | p. 130, eqs. 2–4 |
| Evaluation design: perfect-foresight benchmark | DP-PF as upper bound in simulation | p. 132, Sec. 3; Tables 2–9 |

## Useful quotes (with page numbers)
> "an annual MSDP model could perform relatively better than a monthly one since the uncertainty of inflows on annual basis is relatively smaller" (p. 131)

## Follow-up references to check (backward snowballing)
- [4] Stedinger, Sule & Loucks (1984), SDP models for reservoir operation, *Water Resour. Res.* 20(11).
- [18] Zambelli, Luna & Soares (2009), LTHS with deterministic NLP and annual inflow forecasting, PowerTech Bucharest.
- [20] Tejada-Guibert, Johnson & Stedinger (1995), value of hydrologic information in SDP, *Water Resour. Res.* 31(10).
- [25] Siqueira et al. (2006), SDP for LTHS with different streamflow models, PMAPS.

