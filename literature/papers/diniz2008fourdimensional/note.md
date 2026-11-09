---
bibkey: diniz2008fourdimensional
bibkey_provisional: true
title: "A Four-Dimensional Model of Hydro Generation for the Short-Term Hydrothermal Dispatch Problem Considering Head and Spillage Effects"
authors: "André Luiz Diniz, Maria Elvira Piñeiro Maceira"
year: 2008
venue: "IEEE Transactions on Power Systems 23(3), pp. 1298–1308 (doi:10.1109/TPWRS.2008.922253)"
peer_reviewed: true
methods: [hydro-production-function, deterministic-lp-milp, benders-decomposition]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "literature/inbox/02_Driftsplanlegging_og_optimering/11_Diniz_2008_Four_dimensional_model_of_hydro_generation_head_and_spillage_effects.pdf"
takeaway: "Reviews hydro production function (HPF) approaches and proposes a concave piecewise-linear 'AHPF' of storage, turbined outflow and spillage (convex hull + least-squares correction + secant in spillage), used in Brazil's DESSEM; 5 discharge grid points give ~0.18% average error."
---

# 4-D piecewise-linear hydro production function (Diniz & Maceira, 2008)

> **Page convention.** Journal pp. 1298–1308 = PDF pages 1–11 (journal page = PDF page + 1297).

## Research question / purpose
For the large-scale, network-constrained, one-week hourly hydrothermal dispatch problem (Brazilian ISO), how can the non-linear hydro production function (HPF) be represented accurately enough while keeping the problem a fast LP? The paper (i) reviews approaches to model the HPF and (ii) proposes a 4-D piecewise-linear model, generation = f(storage V, turbined outflow Q, spillage S) (p. 1298).

## Setting
- **System:** centralised Brazilian hydrothermal system: 110 hydro plants (4 pumped-storage, pumping modelled as separate units), 59 thermal plants, 3457 buses, 4889 lines, DC network (p. 1304).
- **Markets:** none — centralised cost-minimisation dispatch by the ISO (p. 1303).
- **Horizon and resolution:** 168 h (one week, hourly), third week of April 2006; average demand ≈ 43,000 MW (p. 1304).

## Method
- **Model type:** deterministic LP dispatch in DESSEM (CEPEL), solved by "dual dynamic programming" = multistage Benders decomposition, with a pre-set unit commitment; end-of-week system cost-to-go function from CEPEL's medium-term model gives the value of stored water (pp. 1303–1304).
- **How uncertainty is represented:** deterministic.
- **HPF physics (pp. 1298–1299):** P = k·η·q·h_net (eq. 1); net head = forebay level f(V) − tailrace level f(Q, sometimes S) − penstock losses (eq. 2); turbine efficiency from the hill curve (depends on head and flow), generator efficiency on power (eqs. 3–4). Complications: forbidden zones, number of running units, start/stop sequence, non-convex regions (Fig. 1).
- **Head effects (p. 1299):** daily forebay variation has little effect for plants with large dams; but for nearly run-of-river plants over a week, neglecting head–storage dependence can lose accuracy; tailrace rises with discharge → productivity falls with flow → concave HPF; penstock losses ≈ quadratic in flow.
- **Review of approaches (pp. 1300–1301):** concave piecewise-linear or quadratic in Q at fixed head (for plants with little head effect); families of curves per head (accurate but makes the problem iterative); composite/biquadratic functions of Q and V; best-efficiency-point models; spillage via total outflow (assumes spill only at max turbine flow); **pumped storage**: extend the HPF to the third quadrant with negative flow/power, usually with discrete pumping values, or model pumping as a separate (duplicated) unit (p. 1300, Fig. 4).
- **Proposed AHPF (pp. 1301–1303):** assumptions: constant turbine-generator efficiency; penstock losses as a % of output; forebay and tailrace as 4th-degree polynomials; forbidden zones ignored at first and checked after dispatch (p. 1301). Steps: (1) grid of (V, Q) points, exact HPF at S = 0 (eq. 6); (2) 3-D convex hull (custom algorithm with a derivative-based pre-processing that removes non-concave points, pp. 1301–1302); (3) least-squares correction factor because the hull is always optimistic (eq. 8, p. 1302); (4) secant approximation in the spillage dimension, since HPF is convex in S (eq. 9, p. 1303). Final constraint: generation ≤ each hyperplane (eq. 10); cost minimisation drives the point onto the surface (p. 1303).

## Data / case
Brazilian system data (ONS website), April 2006; Pentium 4 3 GHz (p. 1304). Small-reservoir plants with large relative head variation listed in Table IV (p. 1305); spillage studied for Salto Santiago, Marimbondo, Tucuruí (pp. 1305–1306).

## Key findings
- (p. 1304, Table III) With storage linearised around the initial volume, **5 grid points in Q give an average AHPF error ≈ 0.18%**; up to 10 points still helps; beyond 10 the gain does not justify CPU time. Using the piecewise-linear HPF does not increase CPU time significantly versus constant head.
- (p. 1304) "the effect of the stored volume on the hydro generation is actually almost linear in the short-term planning"; larger deviations may occur for multi-week horizons and very high inflows.
- (p. 1304, Fig. 11) >90% of errors below 1%; the largest (10–40%) at very small generation (small absolute differences).
- (p. 1305, Fig. 12) Concave real HPF → error can be made arbitrarily small; non-concave HPF → a minimum error remains however fine the grid.
- (p. 1305) Highest spillage deviations at low storage + high spill, rare in practice; when spilling the water value is near zero, so errors have little economic impact. Worst plant (Tucuruí) up to ≈ 15%.
- (p. 1306) In real-time operation, changes in unit commitment would change the real HPF; adjustments needed.

## Strengths
- Good compact review of HPF modelling options, including a short note on PHS (p. 1300).
- Single linear function of V, Q, S; no iterations; proven at very large scale.
- Error analysis against the exact HPF.

## Weaknesses / limitations
- Constant turbine-generator efficiency and penstock losses as % of output (p. 1301) — exactly the simplifications later criticised by Kong et al. (2020).
- Concave approximation cannot capture non-concave regions; forbidden zones handled outside the LP.
- Deterministic, cost-minimising ISO setting; no prices or reserves.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review: representations of head, efficiency (`04_literature_review.tex:44`) | Taxonomy of HPF models (concave PL, quadratic, family of curves, biquadratic, best-efficiency points, spillage) | pp. 1300–1301, Sec. III |
| Model assumptions: constant head (`06_mathematical_model.tex:69`) | Forebay variation matters little for large dams; storage effect almost linear short-term | p. 1299 (Sec. II-D), p. 1304 |
| Theory: HPF definition | P = k η q h_net; net head = forebay − tailrace − losses | p. 1298 eq. (1); p. 1299 eq. (2) |
| PHS modelling | Third-quadrant HPF; discrete pumping; pumping as separate unit | p. 1300 Sec. III-D, Fig. 4; p. 1304 |
| Model extension: convex head-dependent production function | Convex hull + least-squares correction (AHPF) | pp. 1301–1303, eqs. (6)–(10) |
| Spillage modelling | Spillage raises tailrace; secant in S; errors economically small because water value ≈ 0 when spilling | pp. 1300, 1303, 1305 |
| Discretisation accuracy | 5 points ≈ 0.18% error, >10 points not worth it | p. 1304, Table III |

## Useful quotes (with page numbers)
> "the effect of the stored volume on the hydro generation is actually almost linear in the short-term planning." (p. 1304)

## Follow-up references to check (backward snowballing)
- Conejo et al. (2002), self-scheduling of a hydro producer (ref. 3).
- Finardi & da Silva (2006), hydro unit commitment by dual decomposition and SQP (ref. 5).
- Diniz, Maceira & Terry (2004), HPF in medium/short-term models, SEPOPE (ref. 27).
- Maceira et al. (2002), CEPEL chain of optimisation models (ref. 29).

