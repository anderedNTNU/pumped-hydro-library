---
bibkey: gjelsvik2005considering
bibkey_provisional: true
title: "Considering Head Variations in a Linear Model for Optimal Hydro Scheduling"
authors: "Anders Gjelsvik, Arne Haugstad"
year: 2005
venue: "SINTEF Energy Research conference paper; venue not printed in the PDF (NVA/Brage record hdl.handle.net/11250/3134055) (unverified)"
peer_reviewed: false        # venue and review status not stated in the PDF (unverified)
methods: [hydro-production-function, sddp-time-series]
review_sections: [modelling-phs-plants]
relevance: high
read_by: []
added: 2026-11-04
source_path: "literature/inbox/02_Driftsplanlegging_og_optimering/19_Gjelsvik_2005_Considering_head_variations_in_a_linear_model_for_optimal_hydro_scheduling.pdf"
takeaway: "Heuristic head-sensitivity cost coefficients added to the linear SDDP model ProdRisk (weekly stages): two-pass scheme, scenario-averaged coefficients keep convexity; simulated income +1 to +6.4 NOK/MWh and ~1% more generation in two Norwegian systems."
---

# Head variations in a linear SDDP scheduling model (Gjelsvik & Haugstad, 2005)

> **Page convention.** The PDF has no journal page numbers; pages cited are PDF pages 1–9.

## Research question / purpose
How can the effect of variable head be included in a **linear** stochastic medium-term scheduling model based on SDDP (ProdRisk), which needs linearity/convexity, for cascaded systems where an exact treatment is not possible (p. 1)?

## Setting
- **System:** Norwegian cascaded conventional hydro (no pumping). Case 1: two rivers, ≈ 2200 GWh/yr; reservoir 2 head variation up to 30 m (≈ 60% of nominal head), reservoir 6 variation ≈ 50 m with nominal head > 900 m (pp. 4–5). Case 2: two rivers, ≈ 3270 GWh/yr; four plants with head variation 45, 70, 17 and 26 m and nominal heads ≈ 300–350 m (p. 5–6).
- **Markets:** a single power market with prices (possibly time-varying within the week) (p. 3). No reserves.
- **Horizon and resolution:** weekly stages, possibly finer price sub-intervals within the week (p. 2); 3-year horizon in tests, results taken from year 2 (p. 4).

## Method
- **Model type:** ProdRisk — SDDP combined with SDP (Gjelsvik et al. 1999), mid-term scheduling; states are reservoir contents and inflow states (pp. 1, 4).
- **How uncertainty is represented:** stochastic inflow (and price in ProdRisk); tests simulated on 50–60 historical inflow years (p. 4). The paper does not detail the price model.
- **Head correction (pp. 2–3):** assume generation is linear in head, P = f(u)·(h_i − h_j)/h_0 (eq. 1). With release fixed, a volume change ΔV changes power by ΔP = P/(A·(h_i − h_j))·ΔV (eq. 3), where A is the reservoir surface area; a submerged outlet couples the downstream level (eq. 4). Valuing ΔP at the market price gives extra linear cost terms Σ c_ti ΔV_ti (eqs. 5–7). The coefficient for a reservoir rewards storage for the plant below and penalises it for the plant above, so it can be positive or negative (p. 3). Mean reservoir level of the week (average of start and end) is used, so V at the end of week t affects weeks t and t+1 (eq. 8, p. 3).
- **Solution procedure (p. 4):** (1) run ProdRisk without head coefficients; (2) from the resulting release, reservoir and price trajectories, compute c_ti per inflow scenario; (3) **average over inflow scenarios** (state-independent coefficients are required because cuts must be valid across states / convexity); (4) re-run with the perturbed cost function. Repeating is possible; coefficients could oscillate, but tests indicate convergence after a few repetitions and that recalculation is usually not necessary.
- **Key modelling choices and assumptions:** linear head–power relation around a nominal schedule; release held fixed for the sensitivity; scenario-averaged coefficients; end-of-horizon valuation from EOPS (SDP on aggregate model), whose influence is reduced by the 3-year horizon (p. 4).

## Data / case
Two anonymised Norwegian systems (Figs. 1 and 4); 50–60 years of historical inflow; average prices 194 NOK/MWh (Case 1) and 123 NOK/MWh (Case 2) (pp. 5, 7).

## Key findings
- (p. 5) **Case 1:** with head coefficients, income +6.4 NOK/MWh (≈ US$1/MWh, ≈ 3% of the 194 NOK/MWh average price — our calculation), generation ≈ +1%, no significant extra spill. Strategy changes: upstream reservoirs are drawn down to raise the head above the downstream plant (Figs. 2–3, pp. 5–6).
- (p. 7) **Case 2:** income +1 NOK/MWh (avg price 123), generation ≈ +1% despite more spill; reservoir 8 storage rises dramatically and its spill doubles while its plant's generation is unchanged — "the real optimum may well be somewhere in between" (p. 7, Fig. 7, p. 8).
- (p. 8) Head coefficients give better economics, higher expected generation and strategies more acceptable to owners (avoid clearly unwise strategies), while preserving convexity and linearity.
- (p. 8) Caveats: sampling errors, end-point valuation simplifications, errors in the stochastic inflow/price models; and the baseline (ignoring head completely) is a weak comparison.

## Strengths
- Simple, transparent, keeps the SDDP problem linear and convex — directly usable in a cut-based model like ours.
- Explains why coefficients must be state-independent in SDDP (p. 4).
- Simulation-based evaluation on long historical inflow records; horizon trick to neutralise end-value effects (p. 4).

## Weaknesses / limitations
- Heuristic; no optimality guarantee; possible oscillation.
- Short paper, few details on ProdRisk's price model and convergence.
- Venue not stated in the PDF; likely not a journal paper.
- Only conventional hydro; no pumping.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Limitation: constant head (`06_mathematical_model.tex:69`) | Ignoring head gives a "less than optimal strategy"; size: +1–6.4 NOK/MWh income, +1% generation | p. 1 (Sec. 1); pp. 5, 7 |
| Theory: SDDP needs convexity; state-dependence must be in the cuts | Explanation why head coefficients are averaged over scenarios | p. 4 |
| Future work: head-dependent extension compatible with SDDP | Head-sensitivity coefficients eqs. (1)–(8) and two-pass procedure | pp. 2–4 |
| Lit review: modelling approaches, head and efficiency (`04_literature_review.tex:44`) | Linear SDDP + heuristic head correction vs exact single-reservoir solutions | pp. 1–2, 8 |
| Method: evaluation design | Simulation on 50–60 historical inflow years; 3-year horizon, report year 2 to avoid end-value bias | p. 4 |
| Background: ProdRisk | ProdRisk = SDDP + SDP, mid-term, can include hedging | p. 1 |

## Useful quotes (with page numbers)
> "An optimization model that does not in some way take head variations and their effects on generation into account will generally produce a less than optimal strategy" (p. 1)

## Follow-up references to check (backward snowballing)
- Gjelsvik, Belsnes & Haugstad (1999), PSCC — already in references.bib as `gjelsvik1999`.
- Pereira (1989), Optimal stochastic operations scheduling of large hydroelectric systems, IJEPES 11(3).
- Mo, Gjelsvik & Grundt (2001), integrated risk management of hydro scheduling and contracts.
- Flatabø et al. (1998), EOPS / short- and medium-term scheduling in Norway.

