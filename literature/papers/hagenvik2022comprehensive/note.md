---
bibkey: hagenvik2022comprehensive
bibkey_provisional: true
title: "A Comprehensive Simulator for Hydropower Investment Decisions"
authors: "Hans Olaf Hågenvik, Siri Mathisen, Arild Helseth, Birger Mo"
year: 2022
venue: "2022 17th International Conference on Probabilistic Methods Applied to Power Systems (PMAPS), IEEE, doi:10.1109/PMAPS53380.2022.9810621 (accepted version, 6 pages)"
peer_reviewed: true
methods: [sddp-time-series, deterministic-lp-milp, heuristics-simulation, hydro-production-function]
review_sections: [modelling-phs-plants, reservoir-sizing-capacity, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/11_Web_search_2026-11-04/hagenvik2022comprehensive.pdf
takeaway: "First paper on SINTEF's ProdRisk-SHOP simulator: ProdRisk SDDP cuts (weekly) used as end-of-week values in week-by-week detailed SHOP MILP simulations, with 'snipping' of the cascade to cut runtime; Sira-Kvina case (upgrading Duge's two reversible pump-turbines) gives +0.4 MEUR/yr (MTM), +1.3 (full STM), +0.4 (snipped STM)."
---

# ProdRisk–SHOP simulator for hydropower investment decisions (Hågenvik, Mathisen, Helseth & Mo, 2022)

_Accepted manuscript, 6 PDF pages; proceedings page numbers not shown, so pages below are PDF pages 1–6. Table I is garbled in the text extraction; only numbers restated in the text are used. Inbox file name uses "hagenvik"; the surname is Hågenvik._

## Research question / purpose
Present a simulator for hydropower **investment analysis** that couples a medium-term SDDP model (MTM, ProdRisk) with a detailed deterministic short-term model (STM, SHOP), so that profit estimates reflect physical details (head-dependent flows, unit-level pumping, licence limits) that the convex SDDP strategy model cannot include (p. 1). Two contributions: (i) the MTM–STM simulator framework, validated on a real case; (ii) mathematical formulation and validation of **system "snipping"** (simulating only the part of the cascade around the investment with reduced cuts) to save computation time (p. 2).

## Setting
- **System:** Sira-Kvina watercourse, south-western Norway (multiple reservoirs and plants on two branches meeting above Tonstad) (p. 3). Investment: **upgrade the runners of the two reversible pump-turbines at Duge PSP** [14].
- **Markets:** energy (spot) only; risk-neutral price-taker, so each river system is optimised independently (p. 1). No reserves.
- **Horizon and resolution:** MTM planning horizon usually **104–208 weeks**, weekly decision stages, known inflow and price within each week (p. 2); STM weekly deterministic problems run sequentially week by week; results over 52 weeks shown (p. 4).

## Method
- **Model type:** simulation framework (Python, using APIs of ProdRisk and SHOP; CPLEX) (p. 2, Fig. 1).
  - **MTM (ProdRisk):** SDDP; stochastic models of inflow and price in the backward recursion, recorded/predicted series in forward simulation (p. 2). Cuts: α ≤ Φ_j + π_j(v − v_j) + μ_j(z − z_j), with reservoir volumes v and inflows z (eq. 1, p. 2).
  - **STM (SHOP):** deterministic, successive linearisation + MILP; all physical details (p. 1–2); uses MTM cuts as end-of-week water value; end state of one week = start of the next; run once per scenario without re-optimising the strategy (p. 2).
- **How uncertainty is represented:** scenario set of inflow and price (typically 30) consistent with the MTM's sample space (p. 2). Case: inflows from 1958–2017 with +5 % for climate change; prices from a fundamental market model for a 2030 low-emission scenario [17] (p. 4). ProdRisk's internal price model not described here (classified `sddp-time-series` by analogy with `schuller2024practical`; unverified).
- **Snipping (Sect. III, p. 2–3):** MTM runs for the whole watercourse; STM only for M reservoirs of N = M + D + U. Upstream releases become inflow; cut terms for upstream/downstream reservoirs and inflows are moved to the right-hand side using MTM-simulated values (scenario-specific cuts, eq. 3–6); downstream-reservoir coefficients are kept to preserve the reference to sea level (eq. 4–6). If the STM reproduced MTM volumes, the same cuts bind; the cut form leaves the STM free to deviate (p. 3).
- **Key modelling choices (p. 4–5):**
  - Kilen–Gravatn–Valevatn: one reservoir in MTM; two in STM with head-dependent tunnel/channel flow.
  - **Duge may pump from Kilen only above 651 masl** — included in STM, not in MTM (convexity).
  - Pumps: STM models two pump units separately (one unit ≈ 40 m³/s, two ≈ 60 m³/s), consumption depending on head, tunnel losses, penstocks and start-up costs; MTM models one pumping unit whose max pumping volume decreases linearly with head at constant power (p. 5).
  - Snipped system: Svartevatn, Gravatn, Kilen; plants Duge and Tjørhom (p. 4).

## Data / case
Sira-Kvina (Fig. 2); 60 inflow years (1958–2017) (Fig. 7 counts "all 60 scenarios"); 2030 price scenario [17]. Runtimes: MTM **26 h** (7 parallel processes), STM **58 h** full system vs **10 h** snipped (Xeon Silver 4116, 16 GB) (p. 5).

## Key findings
- (p. 4–5) Estimated **increase in annual income from the Duge upgrade: 0.4 MEUR (MTM), 1.3 MEUR (full STM), 0.4 MEUR (snipped STM)**; all three give ≈ 0.3–0.4 MEUR higher net income at Duge itself; the full STM additionally shows a markedly higher income at **Tonstad** (largest plant), possibly from extra flexibility in Svartevatn operation (p. 5).
- (p. 4, Fig. 3–4) Reservoir operation of Svartevatn qualitatively similar across MTM, full STM, snipped STM; Duge production differs in the 100 % percentile after June, averages close.
- (p. 5, Fig. 5) Kilen–Gravatn flow: little difference between full and snipped STM; snipped STM sufficient for such details.
- (p. 5, Fig. 6–7) Pump activity: STM respects the 651 masl pumping restriction, MTM cannot; all models agree that more efficient pump-turbines increase pumping at Duge.
- (p. 5) Because simulation (STM) and strategy (MTM) models differ, **optimality of the simulated results is not guaranteed**; the two complement each other.
- (p. 5) Snip boundaries matter: reservoirs of sufficient capacity at each end of the snip avoid MTM results constraining the STM.
- (p. 5) Future work: re-running/updating cuts from the initial state during simulation (later done in `rex2024hydropower`).

## Strengths
- Real Norwegian PHS investment (Duge RPT upgrade) analysed with industry tools; shows where convex SDDP misses pump physics (head-dependent capacity, licence limits).
- Concrete, reusable math for passing cuts to a sub-system.

## Weaknesses / limitations
- Very short (6 pp.); economic Table I unreadable in extraction; little detail on price model or scenario count actually used (30 "typically", 60 inflow years).
- Large spread between estimates (0.4 vs 1.3 MEUR) without a clear explanation, illustrating model-chain inconsistency.
- No reserves, no strategy updating, risk-neutral.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review 5.3: industry tool chain ProdRisk + SHOP | MTM (SDDP cuts) → STM (MILP) week by week | Sect. I–II, pp. 1–2, Fig. 1 |
| Lit. review 5.5: PHS investment (pump-turbine upgrade) valuation | Duge upgrade: +0.4/1.3/0.4 MEUR/yr | p. 4–5, Table I |
| Lit. review 5.3: what convex SDDP cannot model for pumps | Head-dependent pump capacity, 651 masl pumping limit, unit-level pumping | pp. 4–5 |
| Method: cuts as end-of-week value | Cut form α ≤ Φ + π(v − v_j) + μ(z − z_j) | eq. 1, p. 2 |
| Lit. review 5.6 gap: no optimality guarantee in simulation | Strategy/simulation mismatch | pp. 1, 5 |
| Background: Duge PSP | Two RPTs (see `pitorac2020technical`) | p. 3 |

## Useful quotes (with page numbers)
> "there is no guarantee of the optimality of the simulation results." (p. 5)

## Follow-up references to check (backward snowballing)
- [14] Mo & Hågenvik (2020), HydroCen Report 19: applying the ProdRisk–SHOP simulator for investment decisions.
- [2] Hjelmeland, Korpås & Helseth (2016), PSCC: combined SDDP and simulator with sales of capacity.
- [10] Mo, Martino, Naversen & Aronsen (2018): benchmarking hydro operation by simulator.
- [13] Gjelsvik, Mo & Haugstad (2010), Handbook of Power Systems I: SDDP for hydro-dominated systems.
- [1] Cerisola, Latorre & Ramos (2012), EJOR: SDDP for nonconvex hydrothermal models.
- [17] Schäffer, Mo & Graabak (2019), EEM: prices and value of flexible generation in Northern Europe 2030.

