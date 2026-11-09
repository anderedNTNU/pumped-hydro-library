---
bibkey: gjelsvik1999
title: "An algorithm for stochastic medium-term hydrothermal scheduling under spot price uncertainty"
authors: "A. Gjelsvik, M. M. Belsnes, A. Haugstad"
year: 1999
venue: "Proceedings of the 13th Power Systems Computation Conference (PSCC), Trondheim, Norway, 28 June–2 July 1999, pp. 1079–1085"
peer_reviewed: true
methods: [sddp-markov-chain, sdp, uncertainty-modelling, hydro-production-function]
review_sections: [modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "The origin of the SINTEF ProdRisk method: a price-taking producer's medium-term scheduling where the weekly spot price is a discrete Markov chain (SDP over price nodes) and reservoirs/inflows are continuous states handled by SDDP cuts, one cut set per price node; convexity in storage proven, transition probabilities estimated by grouping EMPS price scenarios each week; M=5 price levels give more reasonable reservoir operation than M=1 (mean price)."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/gjelsvik1999.pdf
---

# Combined SDP/SDDP for medium-term scheduling under spot price uncertainty (Gjelsvik, Belsnes & Haugstad, 1999)

_**Scanned PDF, no text layer: `paper.txt` is empty.** The note was written from page images (rendered with Windows.Data.Pdf). Conference pages 1079–1085 = PDF pages 1–7 (offset 1078). Page numbers below are the conference page numbers._

## Research question / purpose
Present a solution algorithm that takes spot-price uncertainty into account in medium-term hydrothermal scheduling for a small or medium-sized price-taking company in the deregulated Scandinavian market (p. 1079). The algorithm combines SDDP (for reservoirs and inflow) with ordinary SDP (for the price).

## Setting
- **System:** a company's hydro system (cascade of reservoirs), with thermal generation as buying options at fixed marginal cost (p. 1079). Test case: 4 reservoirs (A 11, B 64, C 66, D 10 Mm³), two stations (50 MW with 0.85, 150 MW with 1.2, presumably energy conversion factors) (p. 1084, Fig. 3). Not pumped storage.
- **Markets:** spot market only (sale y⁺ and purchase y⁻ at weekly average price ± transmission charge δ), with an optional firm demand d_t (p. 1080).
- **Horizon and resolution:** 1–3 years, weekly time steps; test case almost 3 years starting week 14, reservoirs 25% full (p. 1079, 1084). No intra-week resolution (weekly average price).

## Method
- **Model type:** multistage stochastic LP per stage, min E{Σ L_t − Φ(x_T)} with linear state transition x_t = F_t x_{t−1} + G_t u_t + ξ_t, power balance and bounds (eqs. 2–11, p. 1080). Stage cost L_t = c_tᵀu_t + (p_t+δ_t)y_t⁻ − (p_t−δ_t)y_t⁺ (eq. 5).
- **Production function:** P = f(q)h/h₀ with piecewise-linear f(q) and a head correction factor applied with *estimated* h; variable head not optimised directly because it "may lead to nonconvex problems" (p. 1079).
- **How uncertainty is represented:**
  - Inflow: discrete distribution of white noise (K outcomes) from a multivariable linear autoregressive inflow model (Røtting & Gjelsvik 1992), inflow state in x_t if serially dependent (p. 1080).
  - Price: discrete, time-inhomogeneous Markov chain on M price points per week, Pr(p_t = ζ_j | p_{t−1} = ζ_i) = ρ_ij(t) (eq. 12, p. 1081). Fitting: each week, the EMPS price scenarios are grouped into M groups; ζ_i is the group mean; ρ_ij = fraction of scenarios in group i at t−1 that are in group j at t (p. 1081, Sec. 3.3). Discretisation error acknowledged but not estimated (p. 1081).
  - Price and inflow treated as **independent** one week ahead, because for a "local" system there is no significant correlation between weekly local inflow and spot price (p. 1080–1081). As a heuristic, the forward pass uses the "observed" joint inflow-price scenarios to preserve longer-term coupling; this may cause gaps between upper and lower bounds (p. 1081).
- **Why price cannot be an SDDP state:** the p_t·y_t term makes the cost non-convex in (p_t, y_t), so the dependence of future cost on p_t cannot be represented by hyperplanes (p. 1081).
- **Solution method:** Bellman recursion α_{t−1}(x_{t−1}|p^i_{t−1}) = Σ_j Σ_k ρ_ij ψ_k min[L_t + α_t(x_t|p^j_t)] (eq. 13, p. 1081). Proof that each α_t(·|p^j) is convex piecewise linear in x (convex combination of convex LP value functions), so a separate set of cuts is kept for each price node (p. 1082, Fig. 2). Cut at t−1 for price node i = probability-weighted average (ρ_ij ψ_k) of subproblem values and duals (eq. 23). Because p_{t−1} does not enter the subproblem, only M (not M²) subproblems per state and inflow outcome are solved; ρ_ij enters only through averaging (p. 1082).
- **Algorithm:** forward simulation over a scenario set S* ("observed" inflow-price scenarios, choosing the price node closest to the scenario price) gives an upper-bound estimate J̄; backward recursion over all price nodes j, trial states and inflow outcomes k builds cuts; lower bound from first-stage problem; stop when |J̄ − J̲| is comparable to the standard deviation of J̄, or after a fixed number of iterations (p. 1082–1083). Cut limit per price node with overwriting; inflow loop innermost for warm starts (p. 1083).
- **End-of-horizon value:** Φ(x_T) from water values of an aggregated long-term model, a function of total storage (p. 1080, 1085).

## Data / case
50 price scenarios from an EMPS run of the Scandinavian system; δ_t = 1% of price; M = 5 and M = 1 (p. 1084). Fig. 1 shows the Norwegian weekly spot price 1995–1998, roughly 50–360 NOK/MWh (p. 1080).

## Key findings
- (p. 1080) Analyses of EMPS price series show strong week-to-week serial correlation of price, and little correlation between local weekly inflow and spot price.
- (p. 1082) Expected future cost functions conditional on each price node are convex and piecewise linear in storage → cuts per price node (the Markov-chain SDDP structure).
- (p. 1084, Fig. 4) With M = 5, the 10th percentile of total storage is rather low compared to ordinary practice; reservoirs run low when prices stay high for long.
- (p. 1084, Fig. 5) With M = 1 (mean price, no price model), variation in reservoir content is larger on the low side, operation differs in the last year, and there is more spillage; "the use of a price model (M = 5) gives the most reasonable operation".
- (p. 1084) Fixed-horizon simulation is not fully realistic: real operation updates forecasts and strategy; updating especially important with a mean-price forecast.
- (p. 1085) Implemented as a mid-term option in EOPS; tested on systems with 4 to >50 reservoirs; ~15 min for the test case, 1–2 h for larger systems on Unix.
- (p. 1085) Difficulties: Φ(x_T) from total storage may under-/over-value water in well-regulated vs other reservoirs; multi-year reservoirs; only ~50 scenarios give rough transition-probability estimates (could be improved by many synthetic inflow scenarios through the long-term model).
- (p. 1085) Economic gain of the stochastic price model not quantified because a long (e.g. 50-year) simulation was computationally infeasible.

## Strengths
- Clear and compact derivation of why price must be a discrete (Markov) state while storage can be a cut-approximated continuous state; the convexity argument is directly reusable.
- Practical fitting recipe for weekly transition probabilities from scenario sets.
- Explicit bounds/convergence criterion.

## Weaknesses / limitations
- Weekly average price only: no intra-week price profile, so no value of short-term flexibility (key for PHS).
- No pumping, no reserves; head effects only via fixed correction.
- Price-inflow independence assumed one step ahead; heuristic forward pass breaks the consistency of bounds.
- No out-of-sample economic evaluation; small scenario set (50).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: why price is a Markov state, not an SDDP cut state (non-convexity of p·y) | Explicit argument | p. 1081, Sec. 4.1 |
| Theory: convexity of cost-to-go per Markov node; cuts per node; cut averaging with ρ_ij ψ_k | Derivation, eqs. (13)–(23), Fig. 2 | p. 1081–1082, Sec. 4.2 |
| Method: estimating transition probabilities by counting scenario moves between weekly groups | Recipe | p. 1081, Sec. 3.3 |
| Method: price-inflow independence assumption (and its justification) | Local inflow vs price uncorrelated weekly | p. 1080–1081, Sec. 3.1 |
| Method: end-of-horizon water value from a long-term model | Φ(x_T) from aggregated model; pitfalls | p. 1080, 1085 |
| Method: bounds and stopping criterion | Upper bound from forward simulation, lower bound from first stage, stop when gap ~ std. dev. | p. 1083, step 4 |
| Model: head correction instead of variable head (convexity) | P = f(q)h/h₀ | p. 1079, Sec. 2.1 |
| Results/benchmark: stochastic price model vs mean price (M=5 vs M=1) | Qualitative reservoir and spillage comparison | p. 1084, Figs. 4–5 |
| Lit. review/research gap: no economic out-of-sample evaluation in original work | Stated limitation | p. 1085 |

## Useful quotes (with page numbers)
> "it is impossible to model the dependence of the expected future cost functions on p_t using hyperplanes the same way as for the state x_t" (p. 1081)

## Follow-up references to check (backward snowballing)
- Gjelsvik, Belsnes & Håland (1997), "A case of hydro scheduling with a stochastic price model", Hydropower '97, pp. 211–218 (application of the algorithm).
- Røtting & Gjelsvik (1992), "SDDP for seasonal scheduling in the Norwegian power system", IEEE TPWRS 7(1) 273–279.
- Pereira (1989), Electrical Power & Energy Systems 11(3) 161–169.
- Fosso et al. (1999), "Generation scheduling in a deregulated system. The Norwegian case".
- Flatabø et al. (1998), EOPS / short- and medium-term scheduling, EPSOM '98.

