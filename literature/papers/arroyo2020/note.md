---
bibkey: arroyo2020
title: "On the Use of a Convex Model for Bulk Storage in MIP-Based Power System Operation and Planning"
authors: "José M. Arroyo, Luis Baringo, Ana Baringo, Ricardo Bolaños, Natalia Alguacil, Noemi G. Cobos"
year: 2020
venue: "IEEE Transactions on Power Systems 35(6), 4964-4967 (letter)"
peer_reviewed: true
methods: [deterministic-lp-milp]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Two small counterexamples (unit commitment; transmission expansion) show that the common convex (LP) storage model, without a binary charge/discharge variable, can yield simultaneous charging and discharging at the optimum even when published sufficient conditions (pre-contingency costs; round-trip efficiency < 1) hold, giving cheaper but physically infeasible schedules and even infeasible investment plans."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/arroyo2020.pdf
---

# Convex storage model in MIP-based operation and planning (Arroyo et al., 2020)

_Page mapping: PDF page n = journal page 4963 + n (journal pp. 4964-4967)._

## Research question / purpose
- Test whether criteria from the literature (Wen et al. 2016: presence of storage operating costs; Zhao et al. 2018: round-trip efficiency below one) are sufficient to drop binary variables and use a convex storage model in MIP problems (pp. 4964-4965).

## Setting
- **System:** generic bulk storage unit in (i) a 2-generator, 2-hour unit commitment and (ii) a 2-bus, 2-hour transmission expansion planning problem (pp. 4965-4967).
- **Markets:** none (cost minimisation).
- **Horizon and resolution:** two hourly periods.

## Method
- **Model type:** MILP; storage model eqs. (1)-(4) (energy balance with charge/discharge efficiencies, energy bounds, power bounds), with or without binary z_t that forbids simultaneous charging and discharging (eqs. 13-15) (pp. 4964-4965).
- **Solution:** CPLEX branch-and-cut to 0% gap (p. 4966).
- **Key point:** the convex model's feasible set allows four combinations including "charging and discharging in the same time period", which "cannot be physically implemented" (Fig. 1, p. 4965).

## Data / case
- UC: demands 10 and 36 MW, storage 5-13 MWh, 12 MW, efficiency 0.9, charge/discharge cost $0.1/MWh (p. 4966).
- TEP: two disconnected buses, candidate 100 MW line ($5000), storage 100 MW / 100 MWh, charge efficiency 0.9 (p. 4967).

## Key findings
- (p. 4966) In UC, the relaxed model is cheaper because simultaneous charge/discharge in hour 1 dissipates energy and lets the cheap generator meet ramping, avoiding the expensive unit; the period-1 marginal price is negative; the schedule is infeasible for the true MIP.
- (p. 4967) In TEP, the relaxed model avoids the line investment by simultaneous charge/discharge in hour 2; an infeasible plan becomes "feasible".
- (p. 4967) Conclusion: the convex model may not prevent simultaneous charging and discharging, which "may lead to suboptimality and even infeasibility".

## Strengths
- Minimal, transparent counterexamples; widely cited justification for explicitly preventing simultaneous charge/discharge.

## Weaknesses / limitations
- Letter; toy systems; cost-minimising system context, not a price-taking producer. Does not consider units that genuinely can pump and generate at once.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model assumptions: simultaneous pumping and generation (`06_mathematical_model.tex:59`) | Convex storage model permits simultaneous charge/discharge | p. 4965, Sec. II, Fig. 1 |
| Results/discussion: why we report simultaneous pump/generation frequency (`06_mathematical_model.tex:962`) | Counterexamples showing it can be optimal in LP (energy dissipation, negative price) | pp. 4966-4967, Tables I-II |
| Lit. review: modelling of PHS plants, binary vs LP formulations | Standard MIP storage constraints with binary z | p. 4965, eqs. (11)-(15) |

## Useful quotes (with page numbers)
> "charging and discharging in the same time period cannot be physically implemented." (p. 4965)

## Follow-up references to check (backward snowballing)
- Li, Guo, Sun and Wang (2016), sufficient conditions for exact relaxation of complementarity constraints for storage-concerned economic dispatch, IEEE TPWRS 31(2).
- Cobos, Arroyo, Alguacil and Wang (2018), robust energy and reserve scheduling with bulk storage and wind, IEEE TPWRS 33(5).
- Pozo, Contreras and Sauma (2014), unit commitment with ideal and generic energy storage units.

