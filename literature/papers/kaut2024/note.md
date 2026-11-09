---
bibkey: kaut2024
title: "Handling of long-term storage in multi-horizon stochastic programs"
authors: "Michal Kaut"
year: 2024
venue: "Computational Management Science 21, article 27 (26 pp.)"
peer_reviewed: true
methods: [multistage-scenario-trees, uncertainty-modelling, deterministic-lp-milp]
review_sections: [reservoir-sizing-capacity, ldes-seasonal-storage, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/kaut2024.pdf
takeaway: "Shows that multi-horizon investment models using short representative operational scenarios (days/weeks) cannot size long-term storage correctly, and adds constraints for scaled inventory changes, seasonal scenario groups, probability-limited scenario repetitions and multi-year periods (HyOpt); seasonal sequencing raised the required storage capacity almost 8× in a toy example."
---

# Long-term storage in multi-horizon stochastic programs (Kaut, 2024)

_Article number 27; the PDF's "Page X of 26" equals PDF page X, so page references below are article pages = PDF pages._

## Research question / purpose
Multi-horizon stochastic programming decouples strategic (investment) nodes from operational scenarios to keep large energy-system models tractable (EMPIRE, stochastic TIMES, HyOpt), but this decoupling "prevents accurate modelling of long-term storages, such as hydropower with multi-year reservoirs" (p. 1). With representative days/weeks, storage capacities end up sized for the representative period, not for the year they represent (p. 4). The paper gives formulas for approximating inventory levels **and required storage capacities** in such models (p. 1, 4).

## Setting
- **System:** generic energy-system design model HyOpt (SINTEF); test case is an offshore installation electrified by wind turbines + hydrogen storage (electrolyser, H2 tank, fuel cell), constant 20 MW load (p. 13–14). No hydropower case.
- **Markets:** none (cost minimisation of a system design).
- **Horizon and resolution:** time structures 1 × 1 year, 1 × 5 years, 5 × 1 year; operational scenarios hourly, either full-length (8760 h per year) or 4/8 representative weeks per year (p. 14, Table 4).

## Method
- **Model type:** deterministic-equivalent LP of a two-level (multi-horizon) scenario tree: strategic nodes with attached operational scenarios (p. 2–4, Figs. 2–3). Solved with FICO Xpress 8.14 (p. 15).
- **How uncertainty is represented:** operational scenarios attached to each strategic node, weighted and time-scaled by multipliers M = W × T_SP/T_SC (eq. 1–2, p. 5); weights are not probabilities when scenarios differ in length (Table 1, p. 5). Representative weeks chosen as the week closest to the seasonal mean capacity factor ("mean") or plus the worst week ("mean+min") (p. 14). Footnote: for multidimensional randomness, clustering (k-medoids) would be needed (p. 14).
- **Storage formulations (Sect. 4, p. 6–13):**
  1. Scale each scenario's inventory change by its multiplier to get the strategic-period change (eq. 4, following Strømholm & Rolfsen 2021) with a common starting level for all scenarios in a node (p. 6–7).
  2. Show that the min capacity from a "fan" of scenarios is an underestimate because the same scenario will occur consecutively (example: 35 → 44–54, p. 7).
  3. **Scenario groups** for sequential seasons: seasons chained in order, scenarios random within a group (p. 8–10). Toy example: required capacity 25 as random fan vs **195** when seasons are sequenced (≈ 8×) (p. 8, Figs. 5–6).
  4. **Repeated scenarios:** limit consecutive repetitions by a probability threshold P_R (5 %): seq = ln(P_R)/ln(weight), extra bound eq. (6) on the last repetition (p. 10–11).
  5. **Multi-year periods:** eq. (7)–(8) for drift across years (p. 11–12).
  6. **Initial/final levels:** cyclic constraints with time scopes `oper-scenario` (batteries), `scen-group` (weeks–months, small hydro / medium H2), `strat-node` (inter-seasonal, mid-size hydro), `overall` (large multi-year hydro reservoirs) (p. 12–13). Alternative is assigning a value to final inventory (p. 12).
- **Key modelling choices:** inventory assumed to change linearly through repetitions; only the last repetition needs an extra constraint (p. 11). Mosel implementation in App. A (p. 18–25).

## Data / case
Wind speed at Ekofisk (North Sea) 2018–2022 from MET Norway Frost API, converted with a Vestas V164/8000 power curve; cost data from open HyOpt test case (p. 13–14). Seasons Dec–Nov (p. 14).

## Key findings
- (p. 1, 4) Multi-horizon models with representative periods could not previously be used for **dimensioning long-term storage**.
- (p. 8) Sequencing seasonal scenarios raised the minimal storage capacity from 25 to 195 (almost eight times) in the toy example, with the same net annual change (−5).
- (p. 15, Table 5) Representative-week variants reduce model size 6.5–32.5× and solve 5–6× (5 × 1) to >100× (1 × 5) faster than the full hourly model.
- (p. 15) "mean+min" costlier than "mean"; "groups" costlier than "fan" (grouping forces handling consecutive occurrences); "mean+min_groups" can be costlier than the full model.
- (p. 17) The repetition constraint can be **conservative**: if scenarios actually alternate, true capacity need is lower (example: 4 repeats force capacity ≥ 80).
- (p. 17–18) More wind variability is met by a mix of more H2 storage and more wind capacity, making it hard to isolate the effect on storage size.

## Strengths
- Clear, constructive treatment of a known blind spot of representative-period capacity-expansion models.
- Open-source implementation (HyOpt Mosel code, App. A; public test case).
- Explicit mapping between storage time scale and cyclic-constraint scope (p. 12–13).

## Weaknesses / limitations
- Test case is offshore wind + hydrogen, not hydro or PHS; no prices or market revenue.
- Capacity approximation is heuristic (repetition probability threshold P_R = 5 % chosen ad hoc) and can be conservative (p. 17).
- No comparison against a sequential stochastic optimisation (SDP/SDDP) benchmark; no out-of-sample evaluation.
- Results figures (Figs. 8–10) give only qualitative description in text.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review 5.5 sizing: representative periods mis-size long-term storage | Decoupling prevents correct sizing; capacities fit representative periods, not the year | p. 1, Sect. 2.2 p. 4 |
| Lit. review 5.5: magnitude of error from ignoring chronology | Toy example 25 vs 195 capacity units | Sect. 4.3, p. 8, Figs. 5–6 |
| Background 2.1 LDES: storage time scales (daily, seasonal, multi-year) | Four cyclic-scope classes mapped to batteries, H2, mid-size and large hydro | Sect. 4.4, p. 12–13 |
| Method: end-of-horizon storage treatment (value vs cyclic constraint) | Two common strategies named | p. 12 |
| Research gap: why we use sequential weekly stages instead of representative weeks | Consecutive occurrences of states drive storage need; repetition constraint | Sect. 4.2–4.3.2, p. 6–11 |
| Lit. review: multi-horizon models in energy (EMPIRE, TIMES, hydro) | List of applications incl. Abgottspon & Andersson 2016 | p. 2 |

## Useful quotes (with page numbers)
> "the decoupling prevents accurate modelling of long-term storages, such as hydropower with multi-year reservoirs." (p. 1)

> "it has so far been impossible to use a multi-horizon model for dimensioning long-term storages" (p. 4)

## Follow-up references to check (backward snowballing)
- Abgottspon & Andersson (2016), Energy Procedia 87: multi-horizon modelling in hydropower planning (in our library as `abgottspon2016multihorizon`).
- Strømholm & Rolfsen (2021), NHH master thesis: flexible hydrogen production and storage sizing to exploit electricity price fluctuations; source of the end-of-period inventory formula (p. 4, 7).
- Kaut (2021), CMS 18(3): scenario generation by selection from historical data.
- Maggioni, Allevi & Tomasgard (2019), Ann. Oper. Res.: bounds in multi-horizon stochastic programs.
- Backe et al. (2022), SoftwareX: EMPIRE model; Skar et al. (2016).
- Seljom & Tomasgard (2015); Ringkjøb et al. (2020): short-term variability in long-term energy system models.

