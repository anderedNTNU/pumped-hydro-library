---
bibkey: bueno2023impact
bibkey_provisional: true    # not in references.bib yet (Zotero was not running 2026-11-15); key follows the Better BibTeX pattern
title: "Impact of environmental constraints in hydrothermal energy planning"
authors: "Luís Felipe Bueno, André Luiz Diniz, Rafael Durbano Lobato, Claudia Sagastizábal, Kenny Vinente"
year: 2023
venue: "Report of the 9th Brazilian Study Group with Industry (CEPEL and CCEE), arXiv:2308.05091v1 (10 August 2023)"
peer_reviewed: false
methods: [sddp-time-series, benders-decomposition, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-15
takeaway: "Study-group report: storage-dependent minimum and maximum outflow rules are added to a simplified Brazilian long-term model solved with SDDP.jl, with a survey of how environmental constraints are treated in SDP, SDDP and SDDiP. The penalties on the slack variables that keep the subproblems feasible strongly change the water values; the model is solved over twice the analysed horizon to avoid the end effect, with one forward path per iteration."
---

# Environmental constraints in SDDP hydrothermal planning (Bueno et al., 2023)

_Preprint and workshop report, **not peer reviewed**, 39 pages. Page numbers are arXiv pages (= PDF pages). Downloaded 2026-11-15 from arxiv.org/pdf/2308.05091. System cost minimisation; no pumping._

## Research question / purpose
What happens to the operating policy and the water values of a hydro-dominated system when water is prioritised for other uses through outflow rules that depend on the reservoir level, and how can such rules be put into an SDDP model (abstract, pp. 1–2; pp. 4–5)?

## Setting
- **System:** a subset of hydro and thermal plants of the north-eastern Brazilian subsystem (São Francisco river), single bus (p. 13, p. 21, Appendix A p. 29).
- **Markets:** none; minimisation of thermal cost and deficit cost.
- **Horizon and resolution:** monthly stages; analysed horizon 12 months, **optimised horizon 24 months** (p. 22).

## Method
- **Model type:** multistage stochastic linear program (eq. 5, pp. 13–14), with either 0–1 variables or piecewise-linear approximations for the environmental constraints (Sec. 6, pp. 14–20).
- **How uncertainty is represented:** inflow scenarios (p. 14, Remark 5.1).
- **Solution method:** SDDP with SDDP.jl in Julia (JuMP, Gurobi); an SDDiP test with the volume discretised in 10 and 100 parts (pp. 21, 23–24).
- **Training settings (p. 21):** the official model Newave was run with 10 forward simulations per iteration, the Julia model with **a single one**; both reach the same lower bound, the Julia model in more iterations (p. 22). Evaluation over 100 simulations (p. 21).
- **Feasibility:** SDDP.jl needs complete recourse, so slack variables with penalties are added to the outflow constraints (p. 22).
- **End of horizon:** "To circumvent the 'end-of-world effect'" the model is solved over 2T = 24 months and analysed over T = 12 (p. 22).

## Survey of environmental constraints (Sec. 3, pp. 6–10)
- **Types (p. 6):** time-varying minimum or maximum release; time-varying minimum or maximum storage level; maximum average release within a time window; maximum variation of turbined outflow or of storage between consecutive time steps (ramping); maximum variation of the water level downstream.
- **Effect on water values (p. 6, citing Guisández et al.):** water values rise as the minimum outflow requirement becomes stricter and fall as the ramping limit becomes stricter.
- **In SDP (p. 8):** nonconvex constraints can be included directly, at the cost of state discretisation; Schäffer et al. 2022 for Norwegian state-dependent rules.
- **In SDDP (pp. 8–9):** state dependence in the right-hand side is manageable; a nonconvex feasible region must be convexified; "if-then-else" rules given as tables are nonconvex. The report notes that a combination of SDP and SDDP has long been used in Norway.
- **In SDDiP (p. 10):** exact but not yet mature for large systems; Helseth et al. 2020 as the example (`helseth2020nonconvex`).

## Model elements (pp. 2, 13–20)
- **Sets:** months, thermal plants, hydro plants, scenarios, volume ranges for the minimum and maximum outflow rules.
- **Variables:** hydro and thermal output, turbine discharge, spillage, reservoir volume, power deficit, **deficit (slack) of the minimum outflow constraint, deficit of the maximum outflow constraint**, binaries that mark the active volume range.
- **Constraints:** demand balance on one bus; water balance; production function with constant efficiency; bounds; **minimum and maximum total outflow that depend on the operating range of the reservoir** (restriction, attention, normal) (p. 15; for Três Marias the minimum outflow is 100 or 150 m3/s with a threshold at 30 % storage).
- **Parameters:** thermal costs, deficit cost (7643.82 $/MWh, p. 29), penalty on the slack variables.

## Key findings
- (pp. 11–12, illustrative two-stage example) A minimum outflow raises the water value, most at low storage; a maximum outflow lowers it, most at high storage, and the water value is zero above the volume that can be released.
- (p. 23) With the environmental constraints and a penalty of 100, the lower bound is fifty times larger than without them, because of the penalised slack; stored energy rises towards the end of the year and thermal generation replaces hydro.
- (p. 2, p. 25) The penalties on the slack variables strongly affect the water values: a higher penalty tightens the constraints, lowers outflow and raises storage.
- (pp. 23–24) SDDiP with a coarse discretisation converges faster but to a different bound and operation.

## Strengths
- A compact survey of environmental constraints in dynamic-programming-type hydro models, with the convexity argument.
- Practical details that papers often omit: slack penalties, the doubled horizon, one forward path per iteration.

## Weaknesses / limitations
- Not peer reviewed; a workshop report on a simplified test system (p. 13).
- Constant efficiency, single bus, monthly stages.
- No measure of solution quality beyond the lower bound.

## Use it for… (lookup guide)
| Use in our thesis | What the report provides | Where (page/section) |
|---|---|---|
| Model: penalty on a slack variable changes the water values (our end-volume penalty) | finding | pp. 2, 23, 25 |
| Model: optimised horizon longer than the analysed horizon against the end effect | 24 months solved, 12 analysed | p. 22 |
| Method: one forward path per iteration gives the same bound as ten, in more iterations | Newave comparison | pp. 21–22 |
| Model: list of environmental constraints that stay linear | survey | p. 6 |
| Limitation: level-dependent rules are nonconvex and need binaries or approximation | discussion | pp. 9–10, 15 |

## Useful quotes (with page numbers)
> "penalties of slack variables strongly affect the obtained water values" (p. 2)

## Follow-up references to check (backward snowballing)
- Guisández, Pérez-Díaz & Wilhelmi: the influence of environmental constraints on the water value (Energies, 2016, open access) and the economic impact of minimum flows and ramping (their [17], [18]).
- Schäffer, Helseth & Korpås (2022), SDP with state-dependent maximum discharge: in the library as `schaffer2022stochastic`.
