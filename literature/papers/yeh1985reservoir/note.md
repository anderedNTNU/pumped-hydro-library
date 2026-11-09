---
bibkey: yeh1985reservoir
bibkey_provisional: true
title: "Reservoir Management and Operations Models: A State-of-the-Art Review"
authors: "William W-G. Yeh"
year: 1985
venue: "Water Resources Research, 21(12), 1797-1818"
peer_reviewed: true
methods: [deterministic-lp-milp, two-stage-stochastic, dynamic-programming, sdp, risk-averse-cvar, heuristics-simulation, hydro-production-function]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDP_i_vannkraft/Yeh1985.pdf"
takeaway: "Classic critical review of reservoir operation models before SDDP: LP (incl. stochastic LP, recourse, chance constraints, linear decision rules), DP variants (IDP/DDDP, IDPSA, SDP, reliability-constrained DP, differential DP, progressive optimality), NLP, simulation and real-time systems (CVP, TVA, Hydro-Québec); standard source for the curse of dimensionality, SDP with Markov inflows (Eq. 29) and hierarchical long/short-term decomposition."
---

# Reservoir operations review (Yeh, 1985)

## Research question / purpose
Review the state of the art of mathematical models for reservoir operation, including simulation: LP, DP, NLP and simulation, with historical development, merits, limitations and research recommendations (abstract, p. 1797). Capacity expansion is explicitly excluded (p. 1797).

## Setting
- **System:** generic single and multiple multipurpose reservoirs (irrigation, water supply, hydropower, flood control, navigation). Not pumped storage.
- **Markets:** none; hydropower enters as energy, firm power or power cost.
- **Horizon and resolution:** discusses long-range (monthly/yearly, stochastic) vs short-range (hourly/daily, often deterministic) operation (p. 1803) and hierarchical monthly → daily → hourly models (p. 1812).

## Method
Review. Structure (table of contents, p. 1797): LP models (stochastic LP, Markov-process LP, recourse, chance constraints, linear decision rules) pp. 1798–1802; DP models pp. 1802–1808; NLP pp. 1808–1809; simulation pp. 1809–1811; real-time operation with CVP, TVA, Hydro-Québec pp. 1811–1813; conclusions p. 1813.

## Key findings
- (p. 1797) "No general algorithm exists"; the choice depends on system characteristics, data, objectives and constraints.
- (p. 1798) Ending-state requirement: whatever the horizon, the release policy must leave the system in a state "conducive to satisfactory future operations" (the unstated continuing-operations constraint).
- (pp. 1799–1800) Two-stage stochastic programming with recourse ("here and now" vs "wait and see"); conceptually straightforward but difficult and computationally expensive in applications.
- (p. 1800) Chance-constrained LP neither penalises violations nor gives recourse; Hogan et al. warn its usefulness is limited.
- (pp. 1800–1802) Linear decision rules: simple but conservative (overly large reservoirs) and not guaranteed optimal.
- (p. 1803) **Curse of dimensionality** limits DP for multireservoir systems: "problems should have no more than a few state variables at a time"; dimensionality reduction requires decomposition and iterative procedures.
- (p. 1803) DP suited to: capacity expansion (progressive network), deterministic DP for short-range operation, **stochastic DP for long-range operation**.
- (pp. 1803–1804) IDP/DDDP example: 2 reservoirs (40 × 20 states) → 640,000 transitions vs 81 with IDP; IDP may converge to local optima.
- (p. 1804) **Stochastic DP** with Markov inflows: recursion Eq. (29) over storage S_t and previous inflow I_{t+1} with transition probabilities P[I_t | I_{t+1}]; must be solved backwards.
- (pp. 1805–1806) Reliability-constrained DP (Askew; Rossman; Sniedovich): penalty or Lagrangian formulations; limited to long-range planning; operators are wary of probabilistic constraints.
- (p. 1806) Differential DP avoids discretisation for linear-quadratic problems (Gjelsvik 1982 for a five-reservoir Norwegian-type system).
- (p. 1807) SDP for multireservoir systems usually assumes no cross-correlation of inflows, giving rough policies.
- (p. 1812) Nonlinearity in hydropower comes from variable head (forebay from average storage, tailwater from release) and power vs release; time decomposition helps: head effects matter least in short-term models and detailed power calculations belong in hourly optimisation.
- (p. 1813) Conclusions: LP handles high dimension and gives global optima; DP handles nonlinear and stochastic problems but suffers the curse of dimensionality; NLP not really viable unless separable; real-time operators are reluctant to use optimisation models.

## Strengths
- Comprehensive, structured, widely cited (Scholar ~2,300 per KILDEINFO). Good historical framing.

## Weaknesses / limitations
- 1985: predates SDDP (Pereira & Pinto 1985 is not reviewed as SDDP), electricity markets and pumped storage.
- Descriptive; few quantitative comparisons.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: curse of dimensionality | "no more than a few state variables"; decomposition needed | p. 1803 |
| Theory: SDP with Markov inflows | Recursion Eq. (29)–(31) | p. 1804 |
| Model: end-of-horizon / continuing operations | Final state conducive to future operation | p. 1798 |
| Lit review: two-stage recourse and chance constraints | here-and-now vs wait-and-see; critique of chance constraints | pp. 1799–1800 |
| Model: hierarchical decomposition, head effects | Head nonlinearity; long- vs short-term models | pp. 1811–1812 |
| Lit review: reliability-constrained DP | Askew, Rossman, Sniedovich | pp. 1805–1806 |
| Lit review: practice gap | Operators reluctant to use optimisation | pp. 1813–1814 |

## Useful quotes (with page numbers)
> "problems should have no more than a few state variables at a time" (p. 1803)

## Follow-up references to check (backward snowballing)
- Gjelsvik (1982) — stochastic seasonal planning with differential DP.
- Turgeon (1980, 1981a, b) — multireservoir hydro SDP, aggregation/decomposition.
- Loucks & Falkson (1970) — comparison of DP, policy iteration and LP for Markov models.
- Becker & Yeh (1974) — LP–DP real-time CVP.

