---
bibkey: decaix2021
title: "CFD simulations of a Y-junction for the implementation of hydraulic short-circuit operating mode"
authors: "J. Decaix, D. Biner, J.-L. Drommi, F. Avellan, C. Münch-Alligné"
year: 2021
venue: "IOP Conference Series: Earth and Environmental Science, 774, 012013 (30th IAHR Symposium on Hydraulic Machinery and Systems)"
peer_reviewed: true
methods: [hydro-production-function]
review_sections: [phs-technology]
relevance: background
read_by: []
added: 2026-11-04
takeaway: "XFLEX HYDRO demonstrator at EDF's Grand-Maison PHS: hydraulic short-circuit (running pumps and turbines at the same time) lets a fixed-speed plant regulate power in pump mode; CFD shows the extra junction head losses are below 0.5 % of total head."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/03_Reservemarkeder_og_vilkar/Innlimte_referanser_2026-10-29/decaix2021.pdf"
---

# Hydraulic short-circuit at Grand-Maison, CFD of the Y-junction (Decaix et al., 2021)

PDF note: the first PDF page is an IOP cover sheet; the paper's own pages 1–10 follow. Page numbers below are the paper's printed numbers.

## Research question / purpose
Grand-Maison (EDF, built in the 1980s) has fixed-speed pumps, so its pumping power cannot be regulated. Hydraulic short-circuit (HSC), i.e. running pumps and turbines at the same time so that the net grid consumption can be adjusted, is to be demonstrated there within the EU H2020 project XFLEX HYDRO (abstract; pp. 1–2). HSC changes the flow paths in the penstock junctions, so the singular head losses must be quantified for a 1D plant model. The paper computes them with CFD (abstract, p. 2).

## Setting
- **System:** Grand-Maison PHS, France: a two-level plant with four Pelton turbines above the lower reservoir and eight reversible pump-turbines below it (abstract, p. 2). The studied junction connects three pump-turbines and two Pelton turbines (p. 4).
- **Markets:** none modelled; the motivation is flexibility for balancing variable renewables (pp. 1–2).
- **Horizon and resolution:** steady-state (and one 40 s unsteady) CFD, not an operations model.

## Method
- **Model type:** RANS CFD (Fluent; RNG k-ε and realizable k-ε), validated first on a canonical 90° T-junction against algebraic formulas (Gardel, Ito & Imai, Rennels, Idel'Cik) (pp. 2–4).
- **Uncertainty:** none.
- **Key choices:** head-loss coefficients K_PR (pump → upper reservoir) and K_PT (pump → Pelton turbine) as functions of the discharge ratio Q_T/Q_P from 0 (pure pump mode) to 1.25 (Pelton maximum flow is 25 % above the pump-turbine flow; the extra comes from the upper reservoir) (pp. 4–5).

## Data / case
Geometry from EDF; meshes of 4.4 and 8.2 million nodes (p. 3).

## Key findings
- (pp. 1–2) PHS can regulate pump power by variable speed or HSC. Variable speed is used in new plants ("Lienthal" [Linthal] and Nant de Drance); Kops II was designed for HSC; for existing plants adding variable speed can be prohibitively expensive, so HSC is "the first option" to adjust power in pump mode.
- (p. 6, p. 8) Junction head losses in HSC mode are below 0.5 % of the plant's total head; no unsteady phenomena; the number of units running does not affect the dimensionless coefficients.
- (p. 6) The turbulence models differ by about 25 % in two cases; a quadratic trend fits both coefficients (R² 0.93 and 0.89).

## Strengths
- Real demonstrator, gives a concrete industrial example of HSC and of why it is attractive for fixed-speed plants.

## Weaknesses / limitations
- Purely hydraulic/CFD; no economics, no market or operating results; no on-site validation (measurements too difficult, p. 2).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background: PHS technology (variable speed vs. hydraulic short-circuit) | Definition of HSC; variable speed in new plants, HSC as first option for existing fixed-speed plants; Kops II, Nant de Drance, Linthal examples | pp. 1–2, Sec. 1 |
| Model: two independent units may pump and generate simultaneously | Industrial evidence that simultaneous operation is a real mode, with junction losses < 0.5 % of head | p. 6, p. 8 (Conclusion) |

## Useful quotes (with page numbers)
> "Hydraulic short circuit consists in running pumps and turbines in the meantime" (abstract, p. 1)

## Follow-up references to check (backward snowballing)
- [3] Pérez-Díaz et al. 2014, EERA report on technological developments for PHS.
- [2] Pérez-Díaz et al. 2015, RSER 44 (already in papers/ as `perezdiaz2015trends`).
- [4] Deane, Ó Gallachóir, McKeogh 2010, RSER 14 (PHS techno-economic review).
- [5] Rocks & Meusburger 2015 (Kops II HSC).

