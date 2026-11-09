---
bibkey: labadie2004
title: "Optimal Operation of Multireservoir Systems: State-of-the-Art Review"
authors: "John W. Labadie"
year: 2004
venue: "Journal of Water Resources Planning and Management, 130(2), 93-111"
peer_reviewed: true
methods: [dynamic-programming, sdp, deterministic-lp-milp, two-stage-stochastic, benders-decomposition, heuristics-simulation, adp-reinforcement-learning, hydro-production-function, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Classic review of multireservoir optimisation (LP, network flow, NLP, DP/SDP, optimal control, heuristics). Standard source for the curse of dimensionality (p. 100), for implicit vs explicit stochastic optimisation (pp. 96, 101) and for the end-of-horizon term in the objective (p. 95). Does not cover SDDP, pumped storage or electricity markets."
---

# Multireservoir optimisation review (Labadie, 2004)

## Research question / purpose
Gives an overview of optimisation methods for managing and operating **multireservoir** systems, and suggests directions for future research. It updates an earlier review (Labadie 1997, UCOWR Water Resources Update) (p. 94). The motivation is that few new large storage projects are being built in developed countries, so attention shifts to operating existing systems better (p. 93). The review covers methods "designed to prevail over the high-dimensional, dynamic, nonlinear, and stochastic characteristics of reservoir systems", multiobjective extensions, and heuristic methods: genetic algorithms, neural networks and fuzzy rule-based systems (abstract, p. 93; p. 94).

## Setting
- **System:** generic multireservoir water-resource systems (water supply, flood control, irrigation, hydropower). Examples come mainly from the US (Colorado-Big Thompson, Central Valley Project, TVA, Missouri) and also Brazil, Korea, Sri Lanka, Venezuela, Canada (Hydro-Québec) and Zambezi. **Not pumped storage.** Hydropower is one objective among several.
- **Markets:** none. There is no electricity-market or price-based formulation. The hydropower objective is maximising generation or firm energy (Eq. 2, p. 95). The word "price" appears only as dual/node prices in network models (p. 98).
- **Horizon and resolution:** generic. Time steps "may be hourly, daily, weekly, monthly, or even seasonal". Hierarchical schemes pass long-term monthly or seasonal results to short-term hourly or daily operation (p. 95; p. 105).

## Method
- **Model type:** a review. It sets up a generic deterministic problem: Eq. (1) objective, Eq. (2) hydropower objective, Eq. (3) mass balance with connectivity matrix C, Eqs. (4)–(5) storage and release bounds, Eq. (6) target or secondary-objective constraints (pp. 95–96). The stochastic counterpart is Eq. (13), with chance constraints in Eqs. (14)–(15) (p. 101).
- **How uncertainty is represented:** two families.
  - **Implicit stochastic optimisation (ISO)**, "Monte Carlo optimization": deterministic optimisation over long historical or synthetic inflow series, with operating rules then inferred by regression (Fig. 2, p. 96).
  - **Explicit stochastic optimisation (ESO)**: works directly on probability distributions, without perfect foresight (Fig. 5, pp. 101–102). This includes chance constraints, stochastic LP (two-stage with Benders), SDP (independent or lag-1 inflow states, Eqs. 24–26, p. 103), sampling SDP (Kelman et al. 1990), and stochastic optimal control (LQG, ELQG).
- **Solution methods reviewed:** LP and simplex variants; network flow (RELAX, HEC-PRM); MILP; separable programming; NLP (SLP, SQP, augmented Lagrangian/MOM, GRG); discrete DP and its variants (coarse grid with interpolation, DPSA, IDP/DDDP); DDP; discrete-time optimal control (OCT); SDP; aggregation/disaggregation; LQG/ELQG; multiobjective methods (ε-constraint, weighting, goal programming, MCDA); real-time control with forecasting; GA, RL, ANN, fuzzy rule-based (pp. 96–107).
- **Key modelling points:**
  - Objective (1) includes discount factors and a **final term Φ_{T+1}(s_{T+1})** "representing future estimated benefits or costs beyond time horizon T" (p. 95).
  - Hydropower objective (2): efficiency e_i is a function of average head and discharge, and average head is a function of beginning- and end-of-period storage (and of discharge if tailwater effects are included). This is "a highly nonconvex function characterized by many local maxima", and it can be discontinuous or nondifferentiable if individual turbine loading is modelled (p. 95).
  - Evaporation and losses that depend on storage make the feasible set nonconvex (p. 95).
  - Bounds can be relaxed into penalty terms when long hydrologic sequences make the problem infeasible (p. 96).

## Data / case
None of its own. It is a literature review: about 15 pages of text (pp. 93–107) and about 5 pages of references (pp. 107–111).

## Key findings
- (p. 94) Possible reasons for the long-noted gap between theory and real-world use of reservoir optimisation (Yeh 1985; Wurbs 1993), seven in all:
  1. operators distrust models;
  2. hardware limits once forced simplifications;
  3. optimisation is harder to understand than simulation;
  4. many models do not handle risk and uncertainty well;
  5. the wide range of methods is confusing;
  6. DP needs custom code;
  7. many methods produce only "period-of-record" solutions instead of conditional operating rules.

  Decision support systems (MODSIM, RiverWare, CALSIM, OASIS) are helping to close this gap.
- (p. 95) There is a generic objective with discounting and a terminal-value term. Hierarchical planning lets long-term results feed short-term operation. The hydropower objective is nonconvex because of head and efficiency.
- (p. 96) The problem is "dynamic, potentially nonlinear, and nonconvex; and large-scale", and becomes stochastic once inflows, demands and economic parameters are random. The review groups the strategies into ISO, ESO, real-time control with forecasting, and heuristics.
- (p. 96) The main drawback of ISO is that its optimal policies are "unique to the assumed hydrologic time series". Regression-inferred rules can have poor correlations.
- (p. 97) Five advantages of LP: it solves large problems efficiently; it converges to a global optimum; it needs no initial solution; duality supports sensitivity analysis; cheap solvers exist. MILP is "considerably less efficient" and likely intractable for ISO.
- (p. 98) Generalized network solvers are reported 11–17 times faster than revised simplex (Sun et al. 1995). SLP is the most efficient NLP method in comparisons (Hiew 1987; Grygier and Stedinger 1985), but it is not guaranteed to converge.
- (p. 99) "Next to linear programming, dynamic programming has been the most popular optimization technique" for reservoir operation (citing Yakowitz 1982). DP's effort grows **linearly in the number of stages**. In discrete form it handles nonlinear, nonconvex and even discontinuous relations. Recursion is Eq. (11) and the terminal condition Eq. (12). Bellman's principle of optimality is stated here.
- (p. 100) DP yields **feedback (closed-loop) policies r*_t(s_t)**. "Except for optimal control theory, the development of optimal feedback policies is unique to dynamic programming."
- (p. 100) **Curse of dimensionality:** with m discretisation levels for each of n reservoirs, computation and storage scale as **m^n**. "For system dimensions beyond three connected reservoirs, rapid access memory requirements exceed the capacity of modern computing hardware." Coarse-grid interpolation, DPSA and IDP/DDDP ease the problem but "fail to vanquish it completely". In IDP/DDDP the effort per iteration is ∝ 3^n.
- (p. 101) ESO "is designed to operate directly on probabilistic descriptions"; optimisation "is performed without the presumption of perfect foreknowledge", but for multireservoir systems it is computationally harder than ISO. Infinite-horizon Markov decision formulations need no terminal term and give seasonally stationary policies (Bertsekas 1987).
- (p. 102) Chance-constrained models are overly conservative (Loucks and Dorfman 1975). The two-stage stochastic LP is described, with **Benders decomposition** for large scenario sets: project onto the coupling variables, solve the subproblems via the dual, and coordinate through a master problem. Applied to the PG&E hydropower system (Jacobs et al. 1995).
- (p. 103) SDP (Eq. 24) is a Markov decision process that assumes temporally uncorrelated inflows. Lag-1 correlation requires the previous inflow as an extra state (Eq. 25). Policies are found by value or policy iteration, solving seasonal cycles until the policies become stationary. Multireservoir SDP is "more aggravated by state dimensionality than in the deterministic case", especially when spatial correlation must be kept. Sampling SDP (Kelman et al. 1990) uses scenarios directly but does not remove the dimensionality problem. Scenario approaches raise concerns about very small joint scenario probabilities over long horizons.
- (p. 104) Aggregation into an equivalent reservoir (Hall 1970; Turgeon 1980 with SDP and potential energy; Saad et al. 1996 with neural networks for Hydro-Québec) loses information during aggregation.
- (p. 105) Long-range ISO/ESO guide curves (weekly, monthly or seasonal) can be tracked by real-time models at hourly or daily resolution. Using forecasts is preferable, even with forecast errors, to reactive control.
- (p. 106) Optimising hydropower revenue subject to water-quality constraints (Hayes et al. 1998) gave "significant improvement" in downstream water quality "with only modest losses in hydropower benefits". GAs handle constraints poorly (penalty terms) and are computationally expensive for ISO/ESO.
- (p. 107) Reinforcement learning solves SDP-like problems without explicit transition probabilities. ANNs could approximate the DP cost-to-go function (neuro-dynamic programming, Bertsekas and Tsitsiklis 1996).
- (p. 107, conclusions) Real-world implementations "remain limited or have not been sustained". The keys to success are trust, better "packaging" of models, and linkage with simulation models. Private and quasi-public power systems have stronger financial incentives to adopt optimisation.

## Strengths
- Broad, well-organised taxonomy (ISO vs ESO, method by method). Each method comes with its documented advantages, disadvantages and computational scaling.
- Clear generic formulation: objective with terminal value, mass balance, bounds. It is easy to cite for the "standard" reservoir problem.
- Highly cited (unverified count), so it is an accepted reference for the curse of dimensionality and the DP feedback-policy property.

## Weaknesses / limitations
- **No SDDP.** Pereira and Pinto (1991) and stochastic dual DP are not discussed at all (checked by full-text search). Its picture of the state of the art in stochastic multireservoir optimisation is therefore incomplete for hydropower scheduling, so don't cite it for SDDP.
- No electricity markets, prices or price uncertainty. Inflow is treated as the dominant source of uncertainty (p. 101). Nothing on pumped storage.
- Written from a water-resources and civil-engineering point of view (supply, flood control, operating rules), not a power-system one.
- Dated (2004). Hardware statements such as "beyond three connected reservoirs" are tied to that era.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: dynamic programming, curse of dimensionality | m^n scaling with m levels and n reservoirs; memory infeasible beyond about 3 reservoirs (2004 hardware); mitigations (coarse grid, DPSA, IDP/DDDP) | p. 100, "Discrete Dynamic Programming Models" |
| Theory: DP recursion and Bellman principle | Recursion Eq. (11), terminal condition Eq. (12); effort linear in number of stages | p. 99 |
| Theory: DP gives feedback policies | "development of optimal feedback policies is unique to dynamic programming" (apart from optimal control) | p. 100 |
| Theory: SDP formulation, lag-1 inflow state | Eqs. (24)–(26); independent inflows vs previous inflow as state; value or policy iteration until seasonally stationary | p. 103 |
| Theory: SDP worse dimensionality for multireservoir systems | "more aggravated by state dimensionality than in the deterministic case" | p. 103 |
| Theory: two-stage stochastic LP and Benders (brief) | Verbal description of Benders for scenario LPs; PG&E application | p. 102 |
| Model: end-of-horizon value term | Φ_{T+1}(s_{T+1}), "future estimated benefits or costs beyond time horizon T"; discount factors | p. 95, Eq. (1) |
| Model: generic reservoir constraints | Mass balance with connectivity matrix (Eq. 3), storage and release bounds (Eqs. 4–5), penalty relaxation | pp. 95–96 |
| Model: head effects, nonconvex hydropower objective | Eq. (2): efficiency as a function of head and discharge; "highly nonconvex", many local maxima | p. 95 |
| Method: ISO vs ESO, why stochastic optimisation | ISO policies are "unique to the assumed hydrologic time series"; ESO has no perfect foresight | pp. 96, 101 (Figs. 2, 5) |
| Method: hierarchical long-/short-term planning | Long-term monthly or seasonal results passed to hourly or daily operation | pp. 95, 105 |
| Lit. review: classic method landscape before SDDP | LP, network, NLP, DP, SDP, control, heuristics, RL/ANN | pp. 96–107 |
| Lit. review: environmental vs hydropower trade-off | Water-quality constraints at modest hydropower cost (Hayes et al. 1998) | p. 106 |
| **Not** for: SDDP, PHS, electricity markets, price uncertainty | Not covered | — |

## Useful quotes (with page numbers)
> "For system dimensions beyond three connected reservoirs, rapid access memory requirements exceed the capacity of modern computing hardware." (p. 100)

> "Except for optimal control theory, the development of optimal feedback policies is unique to dynamic programming." (p. 100)

> "The primary disadvantage of this approach is that optimal operational policies are unique to the assumed hydrologic time series." (p. 96, on ISO)

> "...optimization is performed without the presumption of perfect foreknowledge of future events." (p. 101, on ESO)

## Follow-up references to check (backward snowballing)
- Yakowitz (1982), "Dynamic programming applications in water resources" (already in repo as `yakowitz1982`), cited on p. 99 for DP's popularity.
- Bellman (1957), *Dynamic Programming*: principle of optimality and curse of dimensionality (pp. 99–100).
- Kelman et al. (1990), sampling SDP (p. 103).
- Turgeon (1980), SDP with an aggregated potential-energy state for hydropower (p. 104).
- Jacobs et al. (1995), stochastic LP with Benders for the PG&E hydropower system (p. 102).
- Tejada-Guibert et al. (1995), multireservoir SDP, Trinity-Shasta (p. 103).
- Bertsekas and Tsitsiklis (1996), neuro-dynamic programming (p. 107).
- Labadie (1997), the earlier version of this review (p. 94).

