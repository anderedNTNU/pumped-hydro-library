---
bibkey: gjelsvik2010
title: "Long- and Medium-term Operations Planning and Stochastic Modelling in Hydro-dominated Power Systems Based on Stochastic Dual Dynamic Programming"
authors: "Anders Gjelsvik, Birger Mo, Arne Haugstad"
year: 2010
venue: "In: Rebennack S. et al. (eds), Handbook of Power Systems I, Energy Systems, Springer, Berlin, pp. 33–55"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, sdp, uncertainty-modelling, hydro-production-function, risk-averse-cvar]
review_sections: [modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Standard reference for the Nordic (SINTEF ProdRisk) SDDP: price-taker 'local' model with weekly stages, reservoirs + VAR(1) normalised inflow as continuous cut states and weekly spot price as a discrete Markov chain (cuts per price node, combined SDP/SDDP); price-inflow assumed independent, observed scenarios in the forward pass; typical settings (50–100 iterations, 50–75 scenarios, 7 price points, K≤30), bound gaps 1–2% (small) to 10–15% (large systems); joint inflow-price modelling flagged as the main open challenge."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDDP_i_vannkraft/Gjelsvik2010.pdf
---

# Nordic SDDP for long- and medium-term hydro scheduling (Gjelsvik, Mo & Haugstad, 2010)

_Book chapter, DOI 10.1007/978-3-642-02493-1_2. Journal (book) page = PDF page + 32 (p. 33 = PDF p. 1). Page numbers below are book pages._

## Research question / purpose
Review how SDDP has been adapted to hydro scheduling in the Nordic countries (p. 33): (1) a "local" model for one company's system, price-taker with exogenous stochastic price (main focus), combining SDDP with ordinary SDP; (2) a "global" EMPS-like multi-area model with endogenous price. Discusses stochastic modelling of inflow and price, extensions (head, risk), computation and experience.

## Setting
- **System:** local: a geographically confined system with a single power balance and no internal bottlenecks, typically one company (p. 34). Global: ~20 areas, ~40 inflow series, Nord Pool + northern Europe (p. 48–49). Conventional reservoir hydro; no pumped storage discussed.
- **Markets:** spot market sales/purchases at weekly average price ± transmission charge; optional firm demand (usually zero in the Nordic market); optional market limits or price-elastic steps (p. 38). Forward contracts in the risk-control extension (p. 46–47). No reserves.
- **Horizon and resolution:** weekly time steps; medium-term up to 2–3 years, long-term 3–5 years or more (p. 35). Optional "load periods" inside the week: hours with similar prices lumped (e.g. night/day), non-sequential, one power balance per load period (p. 38).

## Method
- **Model type:** multistage stochastic LP (eqs. 14–19, p. 41): min E{Σ L_t − Φ(x_T)}, x_t = F_t x_{t−1} + G_t u_t + ε_t, with stage cost L_t = c_tᵀu_t + (p_t+δ_t)y_t⁻ − (p_t−δ_t)y_t⁺ (eq. 8, p. 38).
- **Production function:** P = f(Q)·h/h₀, f piecewise linear and concave, head correction with estimated h; variable head cannot be handled directly (non-convex), a fair approximation where head is large relative to variations (p. 35–36).
- **Inflow model:** S weather-year scenarios (overlapping sequences from up to 70+ years); normalise weekly inflow z = (q − mean_t)/std_t; vector AR(1) z_t = Φ z_{t−1} + ε_t fitted by regression, often separately per season; error discretised to K values by PCA (typically 3 components kept) or by sampling residuals (p. 36–37). Previous inflow is part of the state (state-space enlargement).
- **Price model:** price is a discrete state because the p_t·y_t product makes future cost non-convex in (reservoir, price) (p. 39); M price points per week; Markov transitions ρ_ij(t) (eq. 9) estimated as in Mo et al. (2001b): group scenario prices each week into M groups, count moves, then adjust by minimising squared deviations of conditional expected price plus ω × squared deviation from counted probabilities, subject to row sums = 1 and node-population preservation (eqs. 10–13, p. 40–41).
- **Price-inflow dependence:** processes treated as independent, using marginal distributions; reason: a local system's inflow may not follow the total-system hydrological state that drives price (p. 40). Coupling over longer periods partly kept by using observed inflow-price scenarios in the forward pass (p. 44).
- **Solution method:** hybrid SDP/SDDP (Fig. 2, p. 42): one set of cuts per discrete price point; recursion eq. (20) over M price outcomes and K inflow outcomes; single-transition subproblems (21)–(22); p_{t−1} does not enter the subproblem, so only M subproblems per trial state and inflow outcome (p. 43). Decisions are made after observing ε_t and p_t (weekly hazard-decision, justified by weekly adjustability and better near-term forecasts) (p. 42). Forward pass: observed scenarios, linear interpolation between neighbouring price points' cuts for off-grid prices, upper bound from average cost (p. 43–44). Backward pass gives lower bound. Convergence in practice judged by maximal change in reservoir trajectories with min/max iteration counts (p. 44). Cut limit per price point with overwriting of rarely binding cuts — "a crucial part of the algorithm" (p. 44). Relaxation for cuts/reservoir balances, warm starts with dual simplex (p. 44).
- **End-of-horizon value:** Φ(x_T) from aggregated water values of a long-term (SDP) model distributed to reservoirs by heuristics; mainly a function of total storage (p. 39, 53–54).
- **Extensions:** (4.1) head-variation heuristic of Gjelsvik & Haugstad (2005): two-pass run, head sensitivity coefficients c̃ = price × (ΔP/Δh)/area terms for downstream and upstream plants, averaged over inflow scenarios, added as linear cost terms (eqs. 23–26, p. 45–46). (4.2) Risk control: accumulated profit as a state with sub-period profit targets and user-defined penalty (a utility function); forward contract positions as states, trading as controls (Mo et al. 2001a) (p. 46–47).

## Data / case
Numerical example from Gjelsvik & Haugstad (2005): 11-reservoir system, ~3,270 GWh/yr, average price 15.4 EUR/MWh; four plants with head variations of 45, 70, 17, 26 m on nominal heads of 300–500 m (p. 47–48, Fig. 3). Fig. 1: weekly Nord Pool spot price 2003–2007 (roughly 10–90 EUR/MWh) (p. 39).

## Key findings
- (p. 34) Long-term (3–5 yr) sets end conditions (marginal water values) for medium-term (1–2 yr), which feeds short-term (days–1 week).
- (p. 34) Water value method (SDP) only feasible for very few reservoirs, hence aggregation; SDDP allows detailed multi-reservoir stochastic optimisation.
- (p. 47) Head correction raised average income by 0.13 EUR/MWh and generation by ~1% despite more spill; changes reservoir strategy considerably (moves water to reservoir 7 to raise head).
- (p. 47) Local-model results used as marginal water values/release volumes for the first 1–2 weeks into short-term scheduling and day-ahead bidding; cuts can be passed directly to short-term models.
- (p. 49) Global model converges more slowly (days on one processor).
- (p. 50–51) Inflow modelling problems: non-stationarity, residuals depending on initial state (snowmelt week 24 example, Fig. 5), PCA dimensionality (16-area Nordic: 7 PCs for 90% variance, 3 for 75%), negative inflows from linear AR (penalty variables; log transform would break convexity).
- (p. 51) Observed vs model-consistent forward inflows: inconsistency can distort results (CO₂ quota price example corrected with 1,000 consistent scenarios); authors still prefer observed series in the local model to keep inflow-price coupling.
- (p. 52) Typical computation: 50–100 iterations, S = 50–70 scenarios, K ≤ 30, ~1,000 cuts per cost function; 28 reservoirs/13 stations/4 load periods: ~460 variables, 33–60 constraints per subproblem; 75 scenarios, 7 price points, K = 10, 2.5-year horizon, 50 iterations ≈ 10 h single core, ~108 million LPs. Finer intra-week resolution grows the subproblem roughly linearly.
- (p. 53) Used by power companies on systems with 4 to >50 reservoirs; yields reliable incremental water values per reservoir.
- (p. 53) Only 50–75 observed price scenarios → rough transition probabilities; "joint modelling of inflow and price remains a challenge".
- (p. 53) Bound gaps 1–2% for small single-inflow models, 10–15% for larger systems, mainly due to forward/backward inconsistency and simplified price/inflow models.
- (p. 53–54) Poor Φ(x_T) can make the last year of the strategy non-optimal; ensure long enough study period.

## Strengths
- The canonical, accessible description of the price-Markov SDDP used in Nordic practice, with implementation details and typical parameter values.
- Frank discussion of practical issues (bound gaps, inflow model flaws, end value).

## Weaknesses / limitations
- Weekly price level only (load periods non-chronological): no intra-week chronology, so storage cycling/pumping value is not captured.
- No pumped storage, no reserves; head only via heuristics.
- Price-inflow independence; forward/backward inconsistency.
- Review chapter: limited numerical validation.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: Markov-chain SDDP structure (cuts per price node) | Hybrid SDP/SDDP, eqs. (20)–(22), Fig. 2 | pp. 41–44, Sec. 3 |
| Theory: why price can't be a cut state (p·y non-convex) | Argument | p. 39, Sec. 2.5 |
| Method: transition probabilities from scenario counts, moment-preserving adjustment | Eqs. (9)–(13) | pp. 40–41, Sec. 2.5 |
| Method: hazard-decision assumption within weekly stages | Justification | p. 42, Sec. 3.2 |
| Method: end-of-horizon water value and its pitfalls | Φ(x_T) from aggregated SDP | pp. 39, 53–54 |
| Method: convergence/bounds practice; typical gaps | Stopping rules; 1–2% vs 10–15% gaps | pp. 44, 53 |
| Method: typical SDDP settings and run times | Iterations, scenarios, K, cuts, 10 h case | p. 52, Sec. 8 |
| Model: production function with head correction; head heuristic | Eq. (1), (23)–(26) | pp. 35–36, 45–46 |
| Model: intra-week load periods vs chronological hours | Load-period description | p. 38 |
| Lit. review/research gap: joint inflow-price modelling open | Explicit statements | pp. 40, 52–53 |
| Lit. review: risk control via profit-state penalties | Sec. 4.2 | pp. 46–47 |
| Background: water values passed to short-term bidding | Sec. 4.3 | p. 47 |
| Background: Nordic hydro ~50% of generation; Norway ~99% hydro | Intro | pp. 33–34 |

## Useful quotes (with page numbers)
> "joint modelling of inflow and price remains a challenge" (p. 53)

## Follow-up references to check (backward snowballing)
- Gjelsvik & Wallace (1996), SINTEF/EFI TR A4438 (origin of the SDP/SDDP combination).
- Gjelsvik, Belsnes & Haugstad (1999) [`gjelsvik1999`]; Mo et al. (2001b) [`mo2001`]; Mo et al. (2001a), IEEE TPWRS 16(2) 216–221 (risk management).
- Gjelsvik & Haugstad (2005), head variations heuristic (also in inbox as `19_Gjelsvik_2005_...`).
- Iliadis et al. (2006), hybrid SDP/SDDP risk benchmarking.
- Røtting & Gjelsvik (1992); Stage & Larsson (1961); Scott & Read (1996).
- Philpott & Guan (2008) convergence (in `references.bib` as `philpott2008`).

