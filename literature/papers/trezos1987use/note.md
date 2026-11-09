---
bibkey: trezos1987use
bibkey_provisional: true
title: "Use of Stochastic Dynamic Programming for Reservoir Management"
authors: "Thanos Trezos, William W-G. Yeh"
year: 1987
venue: "Water Resources Research, 23(6), 983-996"
peer_reviewed: true
methods: [sdp, hydro-production-function, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: background
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDP_i_vannkraft/Trezos1987.pdf"
takeaway: "Constrained stochastic differential DP for monthly hydropower energy maximisation: head-dependent energy (average head × release), spill modelled as a random linear function of storage and inflow, inflow uncertainty via mean and covariance only; no state discretisation, so it scales to multireservoir systems; head–spill trade-off is the key insight for high-head reservoirs."
---

# Stochastic differential DP for hydropower (Trezos & Yeh, 1987)

## Research question / purpose
Three issues (abstract, p. 983): (1) increasing output from **existing** hydropower plants by better operation; (2) alleviating the dimensionality problem of multistate DP; (3) using probabilistic forecasts in decision making. The model maximises expected energy from a system of reservoirs with forecast uncertainty expressed through second moments.

## Setting
- **System:** generic multireservoir hydro system in series or parallel (Fig. 1, p. 984). Case studies: Mammoth Pool reservoir, Big Creek–San Joaquin system, Southern California Edison (119,940 ac-ft; 2 × 93.5 MW; ~1100 ft head range) (p. 991); and a hypothetical 4-reservoir system (p. 992). Not pumped storage.
- **Markets:** contracted on-peak levels; objective maximises secondary (off-peak) energy, or total value with an on-/off-peak price ratio p(t) (pp. 984–986).
- **Horizon and resolution:** monthly periods over a 12-month horizon (Table 1, p. 991); outputs are meant as targets for a weekly or daily model "in the next echelon" (p. 985).

## Method
- **Model type:** stochastic constrained **differential DP** (successive approximation, no discretisation of state or control), extending Murray & Yakowitz (1979) to stochastic inflows (pp. 983, 986–987).
- **How uncertainty is represented:** inflows as multivariate random variables with mean QM(t) and covariance QV(t), independent over time but cross-correlated across sites; no distributional assumption beyond first two moments (pp. 983–984). Extension to AR(1) inflows (Eqs. 20–21, pp. 990–991).
- **Solution method:** start from a feasible release policy; backward pass solves a constrained QP at each stage with quadratic value function V_t(S) = SᵀP S + qᵀS + z; forward pass updates; iterate (Fig. 3, p. 988; Appendix, pp. 994–995). Stop when < 0.1% improvement for 5 iterations (p. 992).
- **Key modelling choices and assumptions:**
  - **Head effects:** energy ∝ average head HA(t) × release R(t); HA = (H(t) + H(t+1))/2 (Eq. 4); piecewise-linear storage–elevation curve linearised locally (Eq. 5) (p. 985).
  - **Spill** SP(t) = α(t)S(t) + β(t)S(t+1) + γ(t)IM(t), random coefficients estimated from data (Eq. 6a, p. 985). Values 0.103, 0.092, 0.156 for Mammoth (p. 991).
  - Constraints on **expected** storage and production (Eqs. 7, 9), deterministic release bounds (Eq. 8) (p. 985).
  - **End-of-horizon value:** quadratic penalty for deviating from target end storage TARG(NP+1) (Eq. 2, p. 984).
  - Concavity of the recursion assumed, not proven (p. 987).

## Data / case
- 15 years (1966–1980) of monthly SCE data for Mammoth (p. 991). Min/max releases from historical extremes; powerhouse capacity at 75% full pool as max production (p. 992).
- 100 Monte Carlo simulation runs to validate expected objective (p. 992).

## Key findings
- (p. 984) Optimal operation balances spill losses against the gain from a higher head: a solution in which spill is impossible is suboptimal to one where spill is marginally feasible.
- (p. 992, Fig. 7) Lower inflow variance → higher objective; optimisation matches Monte Carlo mean.
- (p. 991) One of the three validity tests: as head increases, the solution should become more "conservative" (spill more critical). Fig. 8 (p. 992) shows mean storage paths for head drops of 0%, 50% and 100% of the actual value.
- (p. 992) 10–15 iterations, ~30 s on IBM 3090; convergence within ±0.2% from different initial policies.
- (p. 993) 4-reservoir case converges in 10–20 iterations; on/off-peak price ratio doubles QP size; ratio ≤ 1 gives the same solution as no differentiation.
- (p. 993) Best suited for reservoirs with large elevation change per unit storage; little gain for flat storage–elevation curves.
- (p. 993) Future work: distribution (variance) of the objective, not just mean (risk); daily models fed by monthly results.

## Strengths
- Explicit head–release product and head–spill trade-off; a useful physical insight for high-head plants.
- Scales with number of reservoirs (no discretisation).
- Validation against Monte Carlo simulation.

## Weaknesses / limitations
- Only first two moments; constraints on expectations, not on realisations.
- Concavity assumed; local optimum possible; requires feasible initial policy.
- Spill as a fitted linear random function is ad hoc.
- No pumping, no market prices beyond a peak ratio.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review: SDP alternatives avoiding discretisation | Stochastic constrained differential DP | pp. 986–988, Appendix pp. 994–995 |
| Head effects / production function | Energy = average head × release; storage–elevation linearisation | p. 985, Eqs. (4)–(5) |
| Head vs spill trade-off | Optimal policy keeps spill marginally feasible | p. 984; p. 993 |
| End-of-horizon treatment | Quadratic penalty on deviation from target end storage | p. 984, Eq. (2) |
| Hierarchical planning | Monthly targets passed to weekly/daily models | p. 985; p. 993 |

## Useful quotes (with page numbers)
> "Any solution in which spill is an impossible event is suboptimal to the solution in which spill is marginally feasible." (p. 984)

## Follow-up references to check (backward snowballing)
- Murray & Yakowitz (1979) — constrained differential DP.
- Gjelsvik (1982) — stochastic seasonal planning with differential DP (Norwegian, multireservoir).
- Grygier & Stedinger (1985), WRR 21(1) — algorithms for hydropower systems.
- Pereira & Pinto (1985), WRR 21(6) — decomposition approach (precursor to SDDP).

