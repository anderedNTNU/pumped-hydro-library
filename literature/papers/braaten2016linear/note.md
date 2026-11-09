---
bibkey: braaten2016linear
bibkey_provisional: true
title: "Linear decision rules for seasonal hydropower planning: modelling considerations"
authors: "Simen V. Braaten, Ola Gjønnes, Knut Hjertvik, Stein-Erik Fleten"
year: 2016
venue: "Energy Procedia 87, 28-35 (5th International Workshop on Hydro Scheduling in Competitive Electricity Markets)"
peer_reviewed: true
methods: [risk-averse-cvar, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Tutorial: seasonal (52-week, weekly) hydro scheduling with pumping as a robust LP with affine decision rules in zero-mean price/inflow forecast errors over a scenario convex-hull polytope; illustrative 2-reservoir cascade gives sensible but conservative policies; memory matters mainly near spill and the end target."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/10_Mellom_og_langtidslagring/01_Produsentmodeller_og_tidsskalaer/Braaten2016.pdf
---

# Linear decision rules for seasonal hydro planning (Braaten et al., 2016)

DOI: 10.1016/j.egypro.2015.12.354. Open access. NTNU (Fleten group), data from Powel AS.
**Page mapping:** journal p. = PDF p. + 27 (p. 28 = PDF 1, p. 35 = PDF 8).

## Research question / purpose
An introductory guide for hydropower practitioners on modelling and implementing **linear decision rules (LDR)** for the seasonal planning problem, with uncertainty in multiple inflow series and price (p. 28). Claimed novelties: zero-mean forecast errors as the uncertain parameters, slopes on multiple uncertainty types, and a more thorough discussion of limited dependence ("memory") on past uncertainty (p. 28-29).

## Setting
- **System:** generic multi-reservoir cascade; illustration is a two-reservoir cascade, upper reservoir M7 with pumped storage and highest degree of regulation, lower M6 generation only, different inflow series (p. 33).
- **Markets:** price-taker selling at a (forecast) weekly price; no reserves, no intra-week detail.
- **Horizon and resolution:** 52 weeks starting in January, weekly periods (p. 33).

## Method
- **Model type:** deterministic LP (eqs. 1-8, p. 29): maximise discounted Σ price × energy coefficient × (discharge, pumping, spill) over reservoirs and weeks; reservoir balance with upstream connections; bounds on reservoir, generation (MW via energy coefficients), pumping (negative generation with its own energy coefficient, decided at the upstream reservoir), total discharge incl. bypass, spill ≥ 0 (p. 29-30). Every reservoir has a real or dummy power station below (p. 29).
- **How uncertainty is represented:** zero-mean forecast errors in price and each inflow series; uncertainty set = **polytope Hξ ≤ h, the convex hull of 3000 scenarios** from a time-series model tuned to a market model (p. 33; scenarios similar to Gjelsvik et al. 2010, ref. [6]).
- **Solution method:** robust optimisation with affine rules x = x̂ + Σ K·ξ over a memory set (eq. 9, p. 30). Worst-case constraints are dualised (LP duality) to obtain a finite LP in intercepts, slopes and dual variables (eqs. 10-15, p. 31). Reservoir volumes cannot have limited memory because they accumulate all past decisions (p. 32). The expected-profit objective becomes the deterministic term plus Σ slope × Cov(price error, ξ), which captures cross- and autocorrelation (eq. 18, p. 33).
- **Key modelling choices and assumptions:** no head effects (constant energy coefficients); end-of-horizon target volume 66.8 % in week 52 for every reservoir instead of a water value (p. 33); full memory set in the example (p. 33); constraints hold for every point of the polytope (robust feasibility), objective is expected value.

## Data / case
Powel AS data; mean of 3000 scenarios as forecast. LP of 131,021 rows × 295,128 columns, 249 s in CPLEX 12.6.1 (p. 33).

## Key findings
- (p. 33, Fig. 2) Simulated reservoir trajectories on the 3000 scenarios are "rather similar ... regardless of the inflow and price development": the rule counteracts deviations. Most spread during snow melt (weeks 17-33) and for M6 in weeks 22-40.
- (p. 33) M6 (lowest degree of regulation) is drained first, then M7; both emptied during the high initial winter price and refilled at low summer prices.
- (p. 33-34, Fig. 4) Discharge slopes are positive in the current price and inflow errors. M7 generation depends only on its own inflow; **pumping is independent of both inflow errors and reacts only to the previous period's price**: "pumping is used mainly as a financial opportunity, rather than as a tool to balance reservoir levels" (p. 34).
- (p. 34) Long memory matters mainly (i) around week 30, when reservoirs approach their maximum (avoid spill), with dependence on up to 10 previous weeks of inflow error, and (ii) at the end, to hit the target volume. Elsewhere memory can be reduced with little loss.
- (p. 35) Future work: larger systems, comparison with alternative methods (runtime, objective, schedule), quantifying the approximation error.

## Strengths
- Clear, reproducible LP derivation of LDR with dualised robust constraints; scales as a single LP.
- Explicit handling of price-inflow correlation via covariance terms (p. 33).
- Pumping included as negative generation; interpretable slope matrices.

## Weaknesses / limitations
- No comparison with SDP/SDDP or any benchmark; no objective-value or out-of-sample profit reported, only trajectory plots (p. 33-35).
- Affine rules + robust feasibility over the full convex hull are conservative (trajectories pinned near the forecast).
- Weekly resolution only; constant energy coefficients; fixed end-target volume rather than water values; no reserves.
- Short conference paper; formulas garbled in the PDF.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review: modelling PHS / alternative methods to SDDP | LDR robust LP for seasonal planning with pumping | p. 28-33, Sec. 2-3 |
| Lit. review: end-of-horizon treatment | Fixed target volume 66.8 % at week 52 vs. our water-value approach | p. 33 |
| Model discussion: what drives pumping in seasonal models | Pumping reacts only to previous-week price, "financial opportunity" | p. 34 |
| Theory: price-inflow correlation | Covariance term in the expected objective | p. 33, eq. 18 |
| Limitations of approximate policies | No benchmark, approximation error unquantified (stated as future work) | p. 35 |

## Useful quotes (with page numbers)
> "pumping is used mainly as a financial opportunity, rather than as a tool to balance reservoir levels." (p. 34)

## Follow-up references to check (backward snowballing)
- [1] Gronvik, Hadziomerovic, Ingvoldstad, Egging, Fleten (2014), "Feasibility of linear decision rules for hydropower scheduling", PMAPS.
- [3] Zugno, Morales, Madsen (2014), robust CHP management via LDR, ENERGYCON.
- [6] Gjelsvik, Mo, Haugstad (2010), SDDP in hydro-dominated systems, Handbook of Power Systems I.

