---
bibkey: mercier2017
title: "Provision of primary frequency control with variable-speed pumped-storage hydropower"
authors: "Thomas Mercier, Julien Jomaux, Mathieu Olivier, Emmanuel De Jaeger"
year: 2017
venue: "2017 IEEE Manchester PowerTech (doi:10.1109/PTC.2017.7980920); author version from UCLouvain repository"
peer_reviewed: true
methods: [hydro-production-function]
review_sections: [phs-technology, electricity-markets]
relevance: background
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/03_Reservemarkeder_og_vilkar/Innlimte_referanser_2026-10-29/mercier2017.pdf"
takeaway: "Technical conference paper: from scale-model pump-turbine characteristics, variable speed gives a pumping power range of ~24 % of max power (fixed speed: none) and a turbine range of ~53 %, both shrinking with head, so VS-PHS can provide FCR in both modes; FCR earned >15 €/MW/h in 2015–16, which would need ≥30 €/MWh arbitrage spreads to match."
---

# Primary frequency control (FCR) with variable-speed PHS (Mercier et al., 2017)

The available copy is the author/conference version (6 pages, no journal page numbers). Page numbers below are PDF pages 1–6.

## Research question / purpose
Clarify the **technical capability of variable-speed (VS) pumped-storage units to provide primary frequency control (FCR)**: what power range is available in pump and turbine modes at a given head, how this depends on head, and how VS units should be modelled and controlled in power-system studies (abstract and intro, pp. 1–2). The authors argue that economic studies of PHS ancillary services rely on vague operating-range assumptions, e.g. 20–100 % in turbine mode and 60–100 % in pump mode (p. 1).

## Setting
- **System:** a fictitious PHS unit scaled from laboratory measurements of a real Francis pump-turbine scale model (characteristics from Pannatier's 2010 EPFL thesis): 675 rpm nominal, 2 MW max pumping power, giving head 93.04 m and reference diameter 1.2413 m (p. 2). Simulated with a permanent-magnet synchronous machine and back-to-back converters (p. 4).
- **Markets:** FCR in Continental Europe (CE); the common FCR tender of Germany, Switzerland, Austria, the Netherlands and Belgium (weekly tenders, > 800 MW, > 25 % of CE FCR requirement) (p. 2).
- **Horizon and resolution:** dynamic simulation over ~90 s with 10-s frequency data from 2013 (Belgian TSO requirements) (p. 4–5).

## Method
- **Model type:** technical/engineering analysis, not optimisation. Operating ranges derived from unit numbers N11, Q11, T11 and manufacturer limits (cavitation, vortex rope, generator rating) on the T11–N11 chart (eqs. 1–2, p. 2; Fig. 1, p. 3). Transient model: rigid water column + static machine characteristics, first-order guide-vane dynamics, transfer functions for speed control (eqs. 3–4, p. 4), PMSM power control (Fig. 3, p. 5). MATLAB/Simulink/Simscape.
- **How uncertainty is represented:** none (historical frequency signal).
- **Key modelling choices and assumptions:** similitude hypothesis (Reynolds and roughness effects neglected) to scale model characteristics (footnote, p. 2).

## Data / case
- FCR requirements (CE): full activation within 30 s, saturation at ±0.2 Hz, deadband ±0.01 Hz (p. 2).
- FCR prices, Nov 2015–Oct 2016 (52 weekly tenders): average capacity price 15.73 €/MW/h, average marginal price 17.14 €/MW/h (p. 2).
- Simulated FCR amount: 20 % (turbine) and 12.5 % (pump) of rated pump power (p. 5).

## Key findings
- (p. 1) PHS is 99 % of grid-connected storage worldwide (citing IEA 2014); European PHS capacity could be increased up to 10× (citing Gimeno-Gutiérrez & Lacal-Arántegui 2013).
- (p. 2) Per MW, FCR earned > 15 €/MW/h, while arbitrage would need price spreads of at least 30 €/MWh to earn the same, so FCR "may seem a priori more lucrative" than arbitrage for storage, though it requires constant power variation.
- (p. 2, Fig. 2 p. 3) Fixed speed: a single power point in pump mode; VS gives a non-zero power range in pumping and lets both modes operate at lower heads; turbine-mode range unaffected by VS.
- (pp. 2–3) At a given head, allowed pumping range = **24 %** of max allowed power (ratio 0.76), turbine range = **53 %** (ratio 0.47); max allowed power falls with head, so the FCR a unit can offer should be computed at the **minimum operating head** (p. 3).
- (p. 3, p. 5) Continuous FCR provision requires operating away from zero output, implying frequent switches between pump and turbine mode, which has energy-market consequences.
- (p. 5) Simulations show VS units can follow FCR set-points in both modes with ~2 percentage-point mismatch (losses); water hammer is smaller in pump mode where guide vanes are fixed.

## Strengths
- Concrete, physically based numbers for VS operating ranges and their head dependence, rather than assumed ranges.
- Short and clear on FCR technical requirements and why VS matters for reserve provision while pumping.

## Weaknesses / limitations
- Small 2 MW fictitious unit scaled from a model; no economic optimisation; revenue comparison is a back-of-envelope.
- CE FCR market, not Nordic FCR-N/FCR-D; 2015–16 prices.
- No page numbers in this version; check the published PowerTech version before giving page-specific citations.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background (PHS technology): fixed vs variable speed; DFIM vs synchronous with full converter | Intro overview | p. 1 |
| Background (PHS technology): VS pumping power range and head dependence | 24 % pump / 53 % turbine; Fig. 2 | pp. 2–3 |
| Model: reserve capacity while pumping (assumption) | Fixed-speed pump has a single power point; VS has a range | p. 2 (Fig. 2), p. 5 |
| Background (markets): CE FCR product requirements and prices 2015–16 | 30 s, ±0.2 Hz; 15.73/17.14 €/MW/h | p. 2 |
| Background: PHS share of storage, European potential | 99 % (IEA 2014), up to 10× | p. 1 |
| Lit review: reserves can beat arbitrage for storage | FCR vs 30 €/MWh spread comparison | p. 2 |

## Useful quotes (with page numbers)
> "it may seem a priori more lucrative for an energy storage to provide FCRs than to do price arbitrage." (p. 2)

## Follow-up references to check (backward snowballing)
- [2] Gimeno-Gutiérrez & Lacal-Arántegui (2013) JRC assessment of European PHS potential (EUR 25940).
- [4] Beevers et al. (2015) PHS with improved operational flexibility using constant-speed Francis runners, Applied Energy 137.
- [7] Pérez-Díaz et al. (2015) Trends and challenges in PHS operation (filed as `perezdiaz2015trends`).
- [16] Pannatier (2010) EPFL PhD thesis on VS pump-turbine control strategies.

