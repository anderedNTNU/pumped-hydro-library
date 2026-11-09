---
bibkey: helseth2022hydropower
bibkey_provisional: false
title: "Hydropower Scheduling with State-Dependent Discharge Constraints: An SDDP Approach"
authors: "Arild Helseth, Birger Mo, Hans Olaf Hågenvik, Linn E. Schäffer"
year: 2022
venue: "Journal of Water Resources Planning and Management 148(11), 04022061 (doi:10.1061/(ASCE)WR.1943-5452.0001609)"
peer_reviewed: true
methods: [sddp-time-series, hydro-production-function, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "literature/inbox/02_Driftsplanlegging_og_optimering/23_Helseth_2022_Hydropower_scheduling_with_state_dependent_discharge_constraints_An_SDDP_approach.pdf"
takeaway: "Volume-dependent max-discharge (environmental) constraints made SDDP-compatible by LP relaxation plus a time-dependent auxiliary lower volume bound; using the minimum accumulated inflow as the bound is recommended; 3-yr weekly SDDP, VAR-1 inflow, 4000 out-of-sample MIP simulations; +47 k€ and +458 k€/yr vs plain relaxation."
---

# State-dependent discharge constraints in SDDP (Helseth et al., 2022)

> **Page convention.** Article 04022061, pp. 1–13 (printed as 04022061-1 … -13) = PDF pages 1–13. Cited below as "p. X".

## Research question / purpose
How can a **state-dependent maximum-discharge constraint** (no discharge from a reservoir in a summer period if its volume is below a threshold; common in Norwegian and Swedish concessions for recreational purposes) be embedded in SDDP-based medium-term scheduling, which requires convexity, **without compromising computation time** (pp. 1–2)?

## Setting
- **System:** two Norwegian cascaded conventional hydro systems: System 1 resembles **Bergsdalen** (western Norway; constraint on reservoir 2: no discharge weeks 18–35 if volume < 145 Mm³) (p. 7, Fig. 7); System 2 resembles the main string of **Rjukan** (constraint on the upper reservoir: no discharge weeks 18–48 if volume < 734 Mm³, but water available at week 18 may be used; modelled with a parallel "virtual reservoir") (p. 9, Fig. 12).
- **Markets:** risk-neutral **price-taker** maximising expected profit from energy sales (p. 2). No reserves.
- **Horizon and resolution:** 3-year horizon, **weekly decision stages with no time steps inside the stage** (pp. 2, 6). Weekly stages are "the standard approach when computing water values for producers in the Nordic market" (p. 2).

## Method
- **Model type:** multistage stochastic LP solved by SDDP; weekly stage problem eqs. (4a)–(4j) (p. 3): profit = Σ price·generation − penalty C·slack on lower volume bound + future profit α_{t+1}; reservoir balance with inflow from the normalised inflow state; **PQ-curve** as piecewise-linear segments with decreasing efficiency (eq. 4c, Fig. 1); binary δ that opens the waterway only if v ≥ threshold (eqs. 4d–4e, 4j); Benders cuts in reservoir and inflow states (eq. 4g); copy constraint for the inflow state to get its dual (eq. 4h). No discounting (p. 3).
- **How uncertainty is represented:** inflow only (price deterministic, to isolate the constraint–price interaction "without loss of generality"; the SDP price layer of ProdRisk can be added, p. 2). Inflow normalised per week (eq. 2) and fitted as a **VAR(1)** (eq. 3) with **three-parameter lognormal residuals** to avoid negative inflows (pp. 2–3). Whole-week inflow known at the start of the week (p. 2). Model validated against 62 historical years: correct mean and 0-percentile, wet extremes less well captured (p. 6, Fig. 5).
- **Solution method:** standard SDDP (forward simulation with sampled residuals; backward recursion with K openings; **cut sharing** across scenarios since residuals are stage-wise independent) (p. 4, Fig. 2). Upper bound eq. (5), lower bound = simulated profit eq. (6). **Convergence = stabilisation of the upper bound** (Shapiro 2011) (pp. 4, 7).
- **Relaxations (pp. 4–6):** REF ignores the constraint; **SLIN** relaxes δ ∈ [0,1] (convex but loose because the threshold is high); a tighter linearisation from the start volume (eq. 7) is bilinear and would break convexity (McCormick envelopes possible but need a valid lower bound) (p. 5). **ELIN**: introduce a time-dependent auxiliary lower volume bound V̲ (eq. 8) set **before** running SDDP — it cannot be updated dynamically because of cut sharing (p. 5). ELIN-MIN uses the minimum and ELIN-MED the average accumulated inflow from 10,000 sampled scenarios (pp. 5–6, Fig. 4). Bounds too high force slack use at penalty C and distort water values (p. 5).
- **Key modelling choices and assumptions:** risk-neutral, price-taker; weekly stages; penalty C tuned to the maximum price level (p. 6); initial reservoirs at 50%; 100 forward scenarios, 12 backward openings (p. 6); two deterministic price scenarios = weekly average Nord Pool system prices 2018 and 2020, repeated each year; price–inflow correlation neglected (p. 6).
- **Evaluation:** strategies (cuts) from each case are simulated on a **common, pre-sampled set of 4000 out-of-sample inflow scenarios**, with the **MIP** (non-relaxed) stage problem in simulation (p. 7).

## Data / case
Julia/JuMP + CPLEX 12.10, Intel i7-9850H, 64 GB RAM, no parallelism (p. 7). Run times ≈ 90 min (System 1) and ≈ 130 min (System 2) for constrained cases; REF 10–12% faster (pp. 7, 10).

## Key findings
- (pp. 7, 10) The different relaxations do **not** change computation time notably.
- (p. 7) Water values are read as the reservoir coefficients of the binding cut at a given stage and state; they are sensitive to the constraint, most so with high (2018) summer prices (pp. 7–8, Figs. 9–10).
- (p. 9, Table 1) System 1, increase in expected annual profit vs REF (k€): SLIN 205/9, ELIN-MIN 252/11, ELIN-MED 301/8 (2018/2020 prices), against annual profit of 30–50 M€ (p. 8).
- (p. 12, Table 2) System 2 (k€): SLIN 2107/463, ELIN-MIN 2565/628, ELIN-MED 2329/534. ELIN-MED is overly conservative because bounds are often violated in the backward pass (Fig. 14, p. 10), causing lost generation at good prices and more spill (p. 10).
- (p. 11) Recommendation: use the **minimum accumulated inflow** over the constraint period as the auxiliary bound; gain vs standard relaxation +47 k€ (System 1) and +458 k€ (System 2) per year with high constraint-period prices.
- (pp. 11–12) More frequent high prices in a low-carbon system make such constraints more important; further work: stochastic price and inflow together, comparison with SDP or SDDiP.
- (p. 2) SDDiP handles non-convexity with proven convergence but is computationally prohibitive for operational use.

## Strengths
- Clear SDDP stage-problem formulation with PQ-curve, cuts and inflow state — a good template.
- Out-of-sample evaluation with a common scenario set and the exact (MIP) model in simulation.
- Transparent, pre-computed bound; explains why dynamic tightening conflicts with cut sharing.

## Weaknesses / limitations
- Deterministic price, inflow-only uncertainty; no price–inflow correlation.
- Only two systems; gains are modest relative to annual profit.
- No sub-weekly time resolution (no time steps inside the stage).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: SDDP forward/backward pass, cut sharing | Concise description with figure | p. 4, Fig. 2 |
| Theory: convergence criterion (upper-bound stabilisation) | Cites Shapiro 2011; used in practice | pp. 4, 7 |
| Method: water values from cuts | Water value = coefficient of binding cut | p. 7 |
| Method: out-of-sample evaluation | 4000 common out-of-sample scenarios; MIP in simulation | p. 7 |
| Model: weekly stages as Nordic standard | Statement with refs (Gjelsvik 2010; Helseth 2018) | p. 2 |
| Model: PQ-curve segments | Eq. (4c), Fig. 1 | p. 3 |
| Model limitation: environmental constraints omitted (`06_mathematical_model.tex:104–105`) | Why state-dependent constraints are non-convex; relaxation + auxiliary bound | pp. 2, 4–6 |
| Uncertainty: inflow model alternative to Markov chain | VAR(1), 3-parameter lognormal residuals, validation vs 62 years | pp. 2–3, 6, Fig. 5 |
| Lit review: SDDiP is too slow for operational use | Statement | p. 2 |
| Background: Norway hydro share | 143 TWh/yr, 96% of production in 2017 | p. 1 |

## Useful quotes (with page numbers)
> "The use of weekly decision stages is the standard approach when computing water values for producers in the Nordic market" (p. 2)

## Follow-up references to check (backward snowballing)
- Helseth et al. (2018), "Hydropower scheduling toolchains: comparing experiences in Brazil, Norway, and USA and implications for synergistic research" (cited p. 1–2 for SDDP being most used in the Nordics) (unverified title).
- Helseth et al. (2020), SDDiP for state-dependent discharge constraints.
- Schäffer et al. (2020, 2022), review / SDP for non-convex environmental constraints.
- Hjelmeland et al. (2018), SDDiP for hydropower — likely the bib entry `hjelmeland2019tste` ("Nonconvex medium-term hydropower scheduling by stochastic dual dynamic integer programming", IEEE TSTE 10); year differs (2018 online vs 2019 issue).
- Cerisola, Latorre & Ramos (2012), SDDP for non-convex hydrothermal models.

