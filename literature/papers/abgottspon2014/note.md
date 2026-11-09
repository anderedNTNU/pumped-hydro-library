---
bibkey: abgottspon2014
title: "Medium-term optimization of pumped hydro storage with stochastic intrastage subproblems"
authors: "Hubert Abgottspon, Göran Andersson"
year: 2014
venue: "18th Power Systems Computation Conference (PSCC 2014), Wrocław, Poland"
peer_reviewed: true
methods: [sdp, multistage-scenario-trees, deterministic-lp-milp, heuristics-simulation]
review_sections: [modelling-phs-plants, market-participation, research-gap]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "Weekly SDP water values for a Swiss PHS plant with hourly intrastage subproblems (DA + weekly secondary reserves); stochastic intrastage pays off (~10% profit/CVaR) only when reserves are included; perfect weekly foresight overvalues water."
---

# Stochastic intrastage subproblems for PHS (Abgottspon & Andersson, 2014)

> **Page convention.** The file in `paper.pdf` is the **arXiv preprint** (arXiv:1403.4819v1, 19 Mar 2014), 7 PDF pages, with no proceedings page numbers. All "p. X" below are **PDF pages of the arXiv version**. The PSCC proceedings version may differ slightly (the arXiv v1 still contains a German editorial note to the co-author on p. 5, so it is a pre-final draft).

## Research question / purpose
How should short-term (hourly) flexibility be represented in a medium-term (1-year, weekly-stage) self-scheduling model of a pumped-storage plant so that water values are neither under- nor overvalued? The paper proposes **stochastic intrastage subproblems** (a "multihorizon stochastic programming" idea, after Kaut et al.) inside a weekly SDP master problem, and compares it with three simpler alternatives: (1) weekly peak/off-peak prices, (2) price duration curves, (3) deterministic intrastage subproblems. All four are evaluated with and without revenue from secondary frequency control reserves, in a Monte Carlo operation simulation (pp. 1–2).

Stated contributions (p. 2): (i) first application of stochastic intrastage subproblems (to their knowledge); (ii) comparison of approaches to include short-term flexibility in medium-term hydro optimisation; (iii) extension with revenue from spinning reserves.

## Setting
- **System:** one "typical Swiss hydro power plant" (Fig. 3, p. 5): reservoir 1 is a **seasonal** storage, reservoir 2 a **daily** (small) reservoir; pumps 1&2 and turbines 1&2 operate between them; turbines 3&4 discharge from reservoir 2 and are qualified for secondary control. Natural inflows to the reservoirs. Capacities/volumes are **not reported** in the paper. For methods 1–2 the plant is aggregated to one reservoir, one pump, one turbine, with an infinite lower basin for pumping (Fig. 3b caption, p. 5).
- **Markets:** hourly **day-ahead** energy market; **secondary frequency control reserves** (Swiss market, "economically the most interesting one in Switzerland", p. 3): symmetric power bands, procured **weekly**, band held for the whole week; only the **capacity remuneration** is counted, energy-delivery payments neglected; activation assumed symmetric within the tender period (p. 3). No intraday, no forward.
- **Horizon and resolution:** 1 year, **T = 52 weekly stages** (Table I, p. 2); hourly intrastage time steps τ ∈ {1,…,168 h} (methods 3–4). The weekly stage length is chosen because secondary reserves are procured weekly in Switzerland (p. 3). One-year horizon justified by the assumption that annual inflow totals vary little for Alpine plants (p. 2).

## Method
- **Model type:** risk-neutral multistage stochastic program written as a DP recursion (eq. 1, p. 3): profit-to-go Φ_t(x_{t−1}) = max c_tᵀx_t + E[Φ_{t+1}], with water balance (eq. 2), market position (eq. 3), reserve operating band (eq. 4), bounds (eq. 5). Binary q_t ∈ {0,1} per turbine for reserve provision.
- **Decomposition (interstage / intrastage), pp. 1, 4–5:**
  - *Interstage (master) problem*: weekly water values as a function of seasonal-reservoir filling; decision = weekly discretised release W_t from the seasonal reservoir, taken without knowledge of the week's inflows and prices. Solved by **SDP**: seasonal reservoir filling and weekly discharge W_t are discretised (p. 1). Only seasonal reservoirs carry water values; the daily reservoir is not a state of the master problem.
  - *Intrastage subproblem*: hourly operation given W_t — reserve bid (here-and-now, first stage), then DA bidding and production. Method 3: deterministic MILP with perfect knowledge of the week (eqs. 10–11, p. 4). Method 4: multistage stochastic program on a scenario tree where **DA prices are revealed daily** and **inflows weekly** (eqs. 12–13, p. 5), solved as a **deterministic equivalent** with CPLEX (p. 2, p. 5). It cannot be decomposed dynamically because Σ W_t must hold in every scenario (p. 5).
  - Method 1 (eqs. 6–8, p. 4): weekly expected peak price for generation, off-peak price for pumping, aggregated plant; one constraint set per stage and W_t.
  - Method 2 (eq. 9, p. 4): price duration curves from sampled hourly prices; optimise hours of generation h_t^u and pumping h_t^p for given W_t; plant produces/pumps fully or not in each hour; piecewise-linear PDC → quadratic MIP.
- **Why SDP, not SDDP (p. 1):** reserve provision (binary, with a minimum generation set point) makes the master problem's profit-to-go **non-concave** (Fig. 1a, p. 3), so "it is difficult to apply" SDDP; only a few basins enter the master problem so SDP's dimensionality is acceptable; and the solution method is not the focus.
- **How uncertainty is represented:** water inflows and market prices; data process assumed Markovian so Φ_t depends only on the current data (p. 3); expectation over **sampled** random data (p. 3). For the simulation, distributions are estimated (insufficient historical data) and **correlated** inflows and prices are sampled (p. 6). In method 4, two DA price scenarios per day give 2⁷ = 128 weekly scenarios (footnote 3, p. 6); vector size 24·(2¹+…+2⁷) = 6096 vs 168 for the deterministic version (pp. 5–6). Exact price model / number of samples in the optimisation: not stated.
- **Key modelling choices and assumptions:**
  - Reserves: all-or-nothing per qualified turbine (zero or maximum quantity), turbine must run between q_min + q_max and ū − q_max when providing (eq. 4, p. 3; exact signs in the extracted equations are partly garbled, (unverified)); remuneration c_t^q known in advance, set to the minimum one can expect to be accepted (p. 3).
  - Market position m_t bounded to prevent speculation (eq. 5, p. 3).
  - Methods 3–4: daily-reservoir filling ignored in the profit-to-go and not carried between weeks, i.e. daily reservoirs empty at start and end of each week (p. 5).
  - Energy–water conversion via generic functions f_u(u), f_p(p) (Table I, p. 2); **no head dependence** discussed (unverified whether head effects are included; nothing in the text suggests so).
  - No end-of-horizon value discussed explicitly (unverified).
- **Evaluation (Sec. III, p. 6):** Monte Carlo operation simulation over one year, 100 samples, receding horizon: (1) sample correlated inflows and prices, (2) weekly MIP decides whether to offer secondary reserves, (3) **hourly production heuristic** mimicking an operator — fulfil reserve obligations first, then generate or pump by comparing filling-dependent water values with market prices. Output: profit distribution; reported metrics expected profit, relative standard deviation and CV@R10% (mean of the 10% worst) (Table II, p. 7).

## Data / case
Typical Swiss PHS plant (Fig. 3, p. 5), no numerical plant data given. Market data with "clearly present" peak/off-peak periods (p. 7); source and years not stated. Solver: CPLEX dual simplex (LP/QP), branch-and-cut (MIP), MATLAB with 4 workers on a 4-core PC (p. 6, Fig. 4a).

## Key findings
- (p. 6) **Computation:** method 1 solves in 15 s, 30–200× faster than the others; Fig. 4a: ~0.2 min (M1), 7.8 min (M2), 37.3 min (M3), 51.3 min (M4); only method 4 needs notably more memory; method 4 cost grows exponentially with intrastage stages, stochasticity or plant complexity. One stochastic intrastage subproblem: 0.41 s vs 0.12 s deterministic (footnote 3).
- (p. 6, Fig. 4b) **Water values:** the more short-term dynamics are modelled, the higher the water value. Methods 1–2 relatively **undervalue** short-term revenue; method 3 (perfect weekly foresight) **overvalues** it; method 4 should be more realistic. Water values of methods 3 and 4 are similar: ~80% differ by < 10%.
- (p. 6, Fig. 5b) Both methods 3 and 4 use the seasonal reservoir up to its maximum without spilling; method 4 arguably more conservative (releases water earlier); operation differs more than water values do.
- (p. 7, Table II) Expected profit without / with secondary reserves (units not stated; likely M€, unverified): M1 34.24 / 34.99; M2 29.13 / 30.44; M3 34.80 / 35.85; M4 33.40 / **39.14**. CV@R10%: M1 32.66 / 33.27; M2 27.90 / 29.03; M3 33.27 / 33.47; M4 31.82 / **36.28**. Relative std: 2.19/2.53%, 1.95/2.47%, 2.36/3.99%, 2.57/4.10%.
- (p. 7) Method 1 "astonishingly good", but only because the data had clear peak/off-peak structure, which "will or already is not anymore the case". Method 2 worse than expected: the simplified (aggregated) plant uses non-existing resources too efficiently. Without reserves, method 3 beats method 4. **With reserves, method 4 beats all others, raising expected profit and CV@R10% by around 10%.**
- (p. 7, Conclusions) Stochastic intrastage subproblems "make only sense" if the market structure is sufficiently complex (as with secondary reserves); more complex plant structures may be another reason, but testing this is left for future work.

## Strengths
- Directly addresses the weekly-stage / hourly-subproblem coupling that our model uses, and makes the **information structure within the week** explicit (Fig. 2, p. 5).
- Clean **benchmark design**: four representations of short-term flexibility, compared on the same plant and on the same out-of-sample Monte Carlo simulation, with and without reserves.
- Reports risk metrics (CV@R10%, rel. std) alongside expected profit.
- Explicit argument for why reserves (binary, minimum set point) break concavity and hence SDDP (p. 1).

## Weaknesses / limitations
- Single, unspecified plant; no plant parameters, no market data description → results not reproducible and hard to generalise (authors acknowledge plant dependence, p. 6).
- SDP with discretised reservoir and release; only the seasonal reservoir is a state; the daily reservoir is reset to empty each week (p. 5).
- Inflows revealed weekly even in method 4 (for tractability, p. 5); scenario tree grows as 2⁷ per week.
- Reserves: capacity payment only, known in advance, all-or-nothing per turbine, symmetric activation assumed (p. 3).
- Evaluation uses an operator heuristic for hourly dispatch, not the optimisation model itself, so profit differences mix policy quality and heuristic behaviour.
- Short conference paper; arXiv draft with unfinished editorial note (p. 5); units of Table II not stated.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review 5.3: SDP for PHS scheduling with hourly detail | Weekly SDP master + hourly intrastage subproblems; four ways to represent short-term flexibility | pp. 1–5, Sec. I-A, II-C to II-F |
| Lit. review 5.4: energy + reserve participation | DA bidding + weekly symmetric secondary reserve capacity; reserves raise expected profit and make detailed modelling worthwhile | p. 3 (market rules), p. 7 (Table II, conclusions) |
| Model: why reserves must be modelled as continuous/convex in SDDP | Binary reserve provision with minimum generation → non-concave profit-to-go → SDDP hard | p. 1 (Sec. I-A), Fig. 1a p. 3 |
| Model: justification of weekly stages | Weekly stages because reserves procured weekly; weekly profit-to-go sensible for medium-term | p. 3 |
| Model limitation: within-week perfect foresight | Deterministic intrastage (week known in advance) overvalues water values; stochastic intrastage more realistic | p. 5 (Sec. II-E), p. 6 (Fig. 4b) |
| Method: out-of-sample evaluation design | Monte Carlo operation simulation, 100 samples, receding horizon, hourly heuristic, profit distribution, CV@R10% | p. 6 (Sec. III-3), p. 7 Table II |
| Method: benchmarks | Peak/off-peak weekly prices; price-duration curves; deterministic intrastage — as simpler policies to compare against | pp. 4–5, Table II p. 7 |
| Background: peak/off-peak price structure fading | Method 1 good only because data had clear peak/off-peak periods, "will or already is not anymore the case" | p. 7 |
| Research gap | PHS + reserves + water values exists (SDP, one Swiss plant), but no SDDP, no configuration comparison | whole paper |

## Useful quotes (with page numbers)
> "the more short-term dynamics are considered the higher the water value is" (p. 6)

> "the third method assumes perfect weekly knowledge it overvalues the water value" (p. 6)

> "Therefore it is difficult to apply an iteration algorithm like stochastic dual dynamic programming." (p. 1) — context: non-concave profit-to-go caused by reserves.

## Follow-up references to check (backward snowballing)
- [1] Pritchard, Philpott & Neame (2005), hydroelectric reservoir optimisation in a pool market, Math. Prog. 103 — origin of inter/intrastage decomposition.
- [3] Löhndorf, Wozabal & Minner (2013), ADDP for hydro storage trading, Oper. Res. 61(4) — already in bib as `lohndorf2013`; cited here as a deterministic-intrastage approach.
- [4] Kaut et al. (2013), multi-horizon stochastic programming, CMS.
- [2] Abgottspon & Andersson (2012), integrating ancillary services into medium-term hydro optimisation, SEPOPE.
- [12] Abgottspon, Bucher & Andersson (2012), SDP for unified short- and medium-term planning, PMAPS.
- [19] Abgottspon et al. (2014), risk-averse medium-term hydro optimisation with spinning reserves, PMAPS.
- [6] Densing (2013), dispatch planning with newsvendor duals and occupation times, EJOR 228.
- [17] Cerisola, Latorre & Ramos (2012), SDDP for nonconvex hydrothermal models, EJOR 218 — relevant to nonconvexity in SDDP.

