---
bibkey: hjelmeland2019tste
title: "Nonconvex Medium-Term Hydropower Scheduling by Stochastic Dual Dynamic Integer Programming"
authors: "Martin N. Hjelmeland, Jikai Zou, Arild Helseth, Shabbir Ahmed"
year: 2019
venue: "IEEE Transactions on Sustainable Energy, 10(1), 481–490"
peer_reviewed: true
methods: [sddp-time-series, benders-decomposition, hydro-production-function, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDDP_i_vannkraft/Hjelmeland2018.pdf
takeaway: "First application of SDDiP (binary state expansion, Lagrangian/strengthened Benders/integer cuts) to Norwegian medium-term hydro scheduling with unit commitment, non-convex PQ curves and VAR(1) inflow+price; strengthened Benders cuts close most of the gap cheaply, exact convergence is possible but slow, and price uncertainty via big-M blows up the gap."
---

# SDDiP for non-convex medium-term hydro scheduling (Hjelmeland et al., 2019)

_Our copy is the **accepted manuscript** (NVA repository), paginated 1–10; the published version is IEEE TSTE 10(1), pp. 481–490 (online 2018). Page numbers below are **manuscript pages**; journal page ≈ manuscript page + 480 (unverified, layout may differ). Inbox file name says 2018 (online year); bib key uses the issue year 2019._

## Research question / purpose
Can the stochastic dual dynamic integer programming (SDDiP) method of Zou, Ahmed & Sun solve the medium-term hydropower scheduling (MTHS) problem **with non-convexities** (unit commitment, minimum generation, non-convex generation curves, topological restrictions) to optimality, how can stagewise-dependent inflow and energy price be included, and which cut families work best (abstract, p. 1; contributions p. 2)?

## Setting
- **System:** Norwegian system with 3 reservoirs, 2 power stations, 414 MW total; two lower reservoirs with uneven head feed the same station (one at a time); one is 2% of the other's size with equal inflow, and linear SDDP tended to overestimate the ability to avoid spillage (p. 7). Same system as hjelmeland2019energies.
- **Markets:** energy sold to the market (price-taker) plus **spinning, symmetric reserve capacity** at a **deterministic** reserve price for simplicity (stochastic extension via helseth2016 [16]) (p. 3).
- **Horizon and resolution:** 52 weekly decision stages (p. 7); intra-week resolution not stated in the extracted text (unverified). Validation case with 6 stages (p. 7).

## Method
- **Model type:** multistage stochastic mixed-integer program (eq. 2, p. 2). State variables: reservoir levels, generator status, inflow and energy price (p. 2).
- **How uncertainty is represented:** inflow and energy price normalised (seasonal mean/std), shifted to be non-negative, fitted to a **VAR(1)** (eqs. 4–5, p. 3); **fast forward selection** scenario reduction gives a finite set of noise outcomes (9 branches per stage) (pp. 3, 7). The alternative "outer Markov chain" for price [30] is noted, with the drawback of two independent stochastic processes (p. 3). Mean and std from price forecasts of a fundamental model with 70 historical inflow years; single inflow and price series (p. 7).
- **Solution method:** SDDiP (Algorithm 1, p. 5): **binary expansion** of all state variables, local copy variables z_t = x_{t−1} (10c), and cut families: Benders (11), Lagrangian (12)–(14), strengthened Benders (15) (Lagrangian solved once with LP duals), integer optimality cuts (pp. 4–6). Benders cuts first until a stable upper bound, then other families (p. 6). An "approximate SDDiP" keeps continuous states and uses only B and SB cuts (p. 6).
- **Price × generation bilinearity:** binary expansion of the price state and big-M linearisation (eqs. 6a–6f, pp. 3–4); the VAR(1) equality becomes ≤ to keep feasibility (p. 4). Big-M weakens all cuts (p. 6). **Theorem 1** (p. 7): v* ≤ v_LP ≤ v̄_LP (LP with expected price), giving an upper bound to evaluate policy quality.
- **Key modelling choices and assumptions:** non-convex power–discharge curve per station with two units started in order (Fig. 1, p. 3); **head dependence omitted** given modest head variation in most Norwegian stations (p. 3); binary restrictions on spillage/bypass and on which reservoir the station draws from (p. 3); start-up costs and penalties for relatively complete recourse (p. 2). Authors' experience: including the non-convex generation function matters when selling both energy and reserves, so capacity sales are not overestimated, especially with low energy and high capacity prices (p. 3).

## Data / case
- Stage problem: 137 constraints, 182 variables (120 continuous, 62 binary); 52 stages; 9 branches; 2 forward scenarios per iteration; 50 iterations; final simulation of 300 scenarios with 95% CI; Python 3.5 + Gurobi 7.0 on a laptop (i7-4600U, 16 GB) (p. 7).
- Validation: 6 stages, convex generation, expected values: SB+L converges (iteration 567); B and SB alone stall; SB roughly halves the gap vs B (p. 7, Fig. 4).

## Key findings
- (p. 8, Table I, Case I inflow uncertainty only, kEUR) SDDiP: B gap 13.89% (16,792 s); B-SB 4.13% (17,716 s); B-SB-I 3.87% (30,277 s). Approximate problem: B 12.88% (742 s); B-SB **3.63% (1,176 s)**.
- (p. 8, Table II, Case II inflow + energy price) Standard gaps ~48–61% because of the loose upper bound; with Theorem 1's bound: B 11.24%, B-SB 7.37%, B-SB-I 7.50%; approximate B 10.80%, B-SB 7.15% (2,869 s).
- (p. 8) SB cuts significantly improve gap and policy for a modest increase in time; integer optimality cuts add little for their cost (large coefficients slow subproblems: 0.02 s → 0.08 s); Lagrangian cuts too expensive for the full case.
- (p. 8) For this system it seems "more important to adjust the right-hand side of the EFP function than to fine-tune its shape", likely because Norwegian high-head stations are not very head-sensitive; systems with stronger head effects may need Lagrangian/integer cuts.
- (p. 9) Conclusions: method works very well without price uncertainty; the big-M price formulation is the weak spot; approximate SDDiP with SB cuts gives satisfactory results for non-convex MTHS; exact closure needs Lagrangian or integer cuts.
- (p. 1, abstract) SDDP is "a state-of-the-art algorithm for long- and medium-term hydropower scheduling with a linear problem formulation".

## Strengths
- Rigorous treatment of non-convexity with convergence guarantee (SDDiP) and a practical approximate variant.
- Clear comparison of cut families with bounds and times; Theorem 1 provides a usable upper bound under price uncertainty.
- Explains why linear SDDP misrepresents small reservoirs/spillage and reserve sales.

## Weaknesses / limitations
- Small model (62 binaries per stage), single inflow and price series, 2 forward scenarios: hard to generalise.
- Reserve price deterministic; no value-of-reserves analysis.
- Big-M price treatment gives very weak bounds; VAR constraint relaxed to ≤.
- No head effects; no pumping; no out-of-sample evaluation.
- Accepted manuscript, not final typeset version.

## Use it for… (lookup guide)
_The main reason this note exists: when someone later needs a source for a claim, a modelling choice or a section, this tells them whether this paper is it, and where in the paper to look._
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review / theory: SDDP is state of the art for linear hydro scheduling | Abstract statement | p. 1 (AM) |
| Theory: SDDP needs convexity; non-convexities (UC, PQ curves) are a known issue | Sec. I-B review of McCormick, Lagrangian, local cuts | pp. 1–2 |
| Method: why a price Markov chain (vs price as SDDP state) | Bilinear price×generation term; outer Markov chain alternative | pp. 2–4 |
| Limitations: linear model overstates reserve sales / spillage avoidance | Experience statements | p. 3, p. 7 |
| Theory: cut families and bounds | B, SB, Lagrangian, integer cuts; Theorem 1 | pp. 5–7 |
| Results benchmark: typical SDDP gaps and run times in Norwegian MTHS | Tables I–II | p. 8 |

## Useful quotes (with page numbers)
> "it seems more important to adjust the right-hand side of the EFP function than to fine-tune its shape by adjusting the cut coefficients" (p. 8, AM)

## Follow-up references to check (backward snowballing)
- [27] Zou, Ahmed, Sun (2018), Stochastic dual dynamic integer programming, Math. Program.
- [15] Hjelmeland, Korpås, Helseth (2016), combined SDDP and simulator with sales of capacity, EEM.
- [21] Cerisola, Latorre, Ramos (2012), SDDP for non-convex hydrothermal models, EJOR.
- [22] Thome et al. (2013), non-convexities in hydrothermal planning with SDDP (PSR).
- [28] Philpott, Wahid, Bonnans (2016), MIDAS.
- [30] outer Markov chain for price in SDDP (reference number from text; likely Gjelsvik et al. 1999) (unverified).

