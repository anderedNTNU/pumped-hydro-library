# The mathematical model, element by element: who uses the same formulation, and what is ours alone

Written 2026-11-13 (Claude with Anders). Model checked: `../pumped-hydro-thesis/Sections/06_mathematical_model.tex` as of thesis commit b767ad1 (2026-11-10). Equation labels are the LaTeX labels in that file. Paper equations and pages were read in `paper.txt` on 2026-11-13 unless marked "note". This file replaces the old workspace file `weekly-model-from-literature.md` (2026-11-05, three papers only), which the header comment of ch. 6 still points to.

Verdicts: **Same** = a paper has the constraint in the same form. **Adapted** = the idea is in a paper, our form differs (how is stated). **Own** = no paper in the library has it.

Main sources: Bore et al. (2026), paper `bore2026assessing`, weekly LP eqs. (1)–(13), p. 4. `helseth2016`, weekly LP eqs. (2)–(13), pp. 938–939. `schindler2024`, model (C) p. 12 and the reduced trader LP with Prop. 4, pp. 15–18. `philpott2012` and `gjelsvik2010` for cuts per Markov state.

## 1. Weekly operating model
| Element (label) | Same formulation in | Difference from ours | Verdict |
|---|---|---|---|
| Energy revenue, generation minus pumping at the day-ahead price (`eq:objective_energy`) | Bore (1), Helseth (2) for generation; pumping bought at the hourly price in Schindler (C) (spot bid = generation − pumping), `ak2019quantifying` eq. (1), `alic2023optimal` eq. (10) | Bore also has intraday buy and sell | **Same** |
| Capacity payment per product, hour and direction (`eq:weekly_objective`) | Bore (1): hourly aFRR up/down, FCR-N, FCR-D; Helseth (2): weekly blocks | none against Bore. Setting the downward price to zero for symmetric products is our bookkeeping | **Same** (Bore) |
| Generator, upward headroom p^G + Σ r^{G+} ≤ P^{G,max} (`eq:gen_max`) | Helseth (7); Bore (11) | none | **Same** |
| Generator, downward Σ r^{G−} ≤ p^G (`eq:gen_min`) | Bore (10): Σ_down y ≤ p − C^min | ours is Bore with C^min = 0. Helseth instead has the spinning rule (6) with β from (13) | **Adapted** |
| Pump, headroom up and down (`eq:pump_max`, `eq:pump_min`) | Schindler Prop. 4 (PDF p. 17): a reserve-down call-off can be absorbed by pumping, up to output plus maximum pumping; `chazarra2018`: variable-speed units give up and down reserve in pumping mode; `dallinger2019socioeconomic` p. 491: with pump turbines the plant "needs not to generate electricity in order to be able to provide negative balancing energy" | Schindler writes it for the plant as a whole; Chazarra with binaries per unit and mode. Nobody writes one linear constraint per unit | **Adapted** |
| Four reserve variables r^{G+}, r^{G−}, r^{P+}, r^{P−} | `chazarra2018`: upward and downward reserve in generating mode and in pumping mode, four variables per unit, eqs. (30)–(37), pp. 106–108; in pumping mode the upward reserve is current minus minimum consumption and the downward reserve is maximum minus current consumption (p. 106) | ours has no on/off binaries and a minimum of zero, so it is linear (corrected 2026-11-13; first listed as Own) | **Adapted** |
| Generator reserve limit R^{G,max} (`eq:gen_reserve_limit`) | Helseth (12): 0 ≤ r ≤ R^max per station | none | **Same** |
| Pump reserve limit R^{P,max} (`eq:pump_reserve_limit`) | none | by analogy with Helseth (12) | **Own** |
| Volume limits (`eq:volume_limits`) | Helseth (10), Bore (5), Schindler (C) | none | **Same** |
| Water margin for upward reserve, generator term (`eq:energy_up`) | Helseth (8): "enough water in the reservoir to deliver up-regulation reserves" for the whole period | none; Helseth calls it conservative. Bore (5) uses fixed margins instead | **Same** (Helseth) |
| Water margin, pump term η^P r^{P−}/κ | none | follows Schindler's logic (the balance must hold under full activation), but the term itself is ours | **Own** |
| No margin for downward reserve | Helseth (no such constraint); Schindler (free spill) | Bore has a fixed downward margin | **Same** (Helseth) |
| Initial volume (`eq:initial_state`) | Bore (2) | none | **Same** |
| Water balance with pumping and both efficiencies (`eq:water_balance`) | `zhang2026unlocking` eq. (20): storage + pumping × η_p + inflow − outflow − spill − generation/η_g; Schindler (C); `lohndorf2013` (reservoir balance with pumps, "head effects can be ignored") | Bore (9) and Helseth (3) have no pump | **Same** |
| Weekly inflow spread evenly over the periods (`eq:uniform_inflow`) | Helseth (3): the week's inflow enters each time step by its share | Bore has an hourly inflow series | **Same** (Helseth) |
| One constant conversion factor per unit, κ = 2.725H (`eq:energy_constant`) | Schindler (constant efficiencies in MWh/m³); `lohndorf2013`; `gudbjerg2024exploring` (pump efficiency fixed) | Bore (8), Helseth (4) and Alic use piecewise-linear discharge curves for the turbine, so ours is simpler than the Norwegian studies. 2.725 is ρg/3.6·10⁶, a physical constant | **Same** (Schindler); simpler than Bore/Helseth |
| Unlimited spillage, no penalty | Schindler (PDF p. 11: "one can spill unlimited amounts of water"); Helseth (3) has a spill variable | none | **Same** |
| Commitment covered by the two units (`eq:alloc_up`, `eq:alloc_down`) | Helseth (5): the obligation for the watercourse is allocated to stations | ours allocates between two units of one plant | **Adapted** |
| Product limit R^max_f (`eq:commit_limit`) | Bore (12); Helseth (11) | none | **Same** |
| Symmetric products c↑ = c↓ (`eq:symmetric`) | Helseth: "allocated capacity should be spinning and symmetric" (one variable for both directions) | written as an equality for a subset of products | **Adapted** |
| Power continuous from zero, no minimum output, no start-up | Schindler (0 ≤ g ≤ ḡ, 0 ≤ p ≤ p̄, no integers) | Bore has C^min ≤ p (7); Helseth has β (6). `helseth2013` shows start-up costs can be linearised for pumps (eqs. 14–19) | **Same** (Schindler) |
| Reserves from a unit at standstill | Helseth p. 939: the spinning requirement "is easily relaxed … e.g. omitting (6)" | no study actually sells FCR or aFRR from idle units with zero minimum output | **Own** (combination); stated as optimistic in the assumptions table |
| Pump and turbine may run at the same time | Schindler has no constraint (Lemma 2: no benefit without reserves); `chazarra2017` (hydraulic short-circuit raises reserve income) | `gudbjerg2024exploring` and `zhang2026unlocking` eq. (18) forbid it | **Same** (Schindler, Chazarra 2017) |
| One reservoir; the lower reservoir never limits | storage-valuation papers with a single store (`sioshansi2009estimating`, `bradbury2014economic`) | every hydropower paper with a pump models both reservoirs (Alic, Schindler, Löhndorf 2013, Gudbjerg) | **Own** among hydropower scheduling models |
| Always feasible by idling and spilling, no artificial water | Schindler | Helseth (2)–(3) and Bore (1), (5) buy artificial or emergency water at a penalty | **Same** (Schindler) |

## 2. Long-term model and SDDP
| Element (label) | Same formulation in | Difference | Verdict |
|---|---|---|---|
| Weekly stages; the week's prices and inflow known at its start | Bore p. 3; Helseth p. 938; `gjelsvik2010` | none | **Same** |
| Joint price–inflow Markov states | Bore p. 3; `schaffer2022stochastic`; `alic2023optimal` | Helseth and ProdRisk keep inflow outside the chain | **Same** (Bore) |
| Recursion with expectation over next week's states (`eq:bellman`, `eq:expected_future`) | `philpott2012` Sec. 2.1; `gjelsvik2010` eq. (20); `lohndorf2019` | none | **Same** |
| One set of cuts per week and state, one expected cut per trial volume (`eq:cuts`, `eq:cut_coefficients`) | `philpott2012` p. 7 ("a set of cuts for each state in the Markov chain"); `gjelsvik2010` p. 42; Bore Algorithm 1; Helseth (9) | none | **Same** |
| Cut slope from the dual of the incoming volume | `pereira1991`; all of the above | none | **Same** |
| Weekly discount factor β | `kleiven2023` p. 18 (2 % a year); `finnah2021`; `dowson2020` | Bore and Helseth 2016 do not discount | **Same** (Kleiven) |
| Zero terminal value after extra weeks (`eq:terminal_value`, S^ext) | `shapiro2020` p. 14: "to deal with the so-called end-of-horizon effect, 60 more stages are added"; `lohndorf2019` p. 655; `kleiven2023` (two years, first interpreted); Helseth p. 940 names a longer horizon as the alternative to end-value cuts | Bore forces end volume = start volume (4) | **Same** (Shapiro, Löhndorf) |
| Bound α ≤ M̄ before cuts exist (`eq:alpha_bound`) | `fullnerRebennack2025` Algorithm 1 and Remark 3.2 (cut approximations must be initialised with a valid bound) | the formula for B_s (`eq:weekly_bound`) is our derivation | device **Same**, formula **Own** |
| K forward paths sampled from the chain; all states in the backward pass | Helseth p. 940 (200 scenarios re-sampled per iteration); Bore Algorithm 1 (one path) | none | **Same** |
| Stop when the upper bound is inside the confidence interval of the lower bound (`eq:stopping_rule`) | Helseth pp. 939–940 | Bore runs a fixed number of iterations | **Same** (Helseth) |
| Capacity prices deterministic and equal in all states | `helseth2015cooptimizing` (FCR prices "as deterministic input"); Bore paper p. 5 (deterministic capacity prices, listed as a limitation) | Helseth 2016 makes them stochastic | **Same** |
| Water value per MWh, λ/(κη^G) (`eq:water_value_energy`) | unit conversion | | bookkeeping |

## 3. States, evaluation and comparisons (sections 6.5–6.6)
| Element | Same in | Difference | Verdict |
|---|---|---|---|
| K-means per calendar week on paired price and inflow | Bore thesis p. 28; `schaffer2022stochastic` p. 575; `alic2023optimal` p. 12 | the text cites `lohndorf2019` p. 653, which builds its lattice by stochastic approximation, not K-means on data; cite Bore and Schäffer instead | **Same**, citation to fix |
| Features: mean price, **standard deviation of price**, inflow; standardised | none uses the price standard deviation; Bore does not say how features are scaled | | **Own** (the third feature and the scaling) |
| Representative = the actual sample closest to the centre | Bore: the median series of each cluster | close, not identical | **Adapted** |
| Transition probabilities by counting (`eq:transition`) | `mo2001` eq. (1); `gjelsvik2010`; Helseth p. 937; Schäffer; Bore | none | **Same** |
| Merging states with too little support | `mo2001` p. 3: a minimum number of scenarios per node | Mo widens intervals rather than merging | **Adapted** |
| Test paths "not used to fit the uncertainty model", a validation set for the number of states | none (see `markov-states-method.md` §5: no study holds years back) | | **Own**; conflicts with the recipe proposed under Q-006 |
| Observed week assigned to the nearest state in simulation | `gjelsvik2010` p. 44; `lohndorf2019` pp. 653–654 | none | **Same** |
| Profit plus the cut-based value of remaining water (`eq:oos_profit`–`eq:oos`) | Helseth p. 940: profits "adjusted for the deviations between final and initial reservoir levels" | ours reports the two parts separately | **Adapted** |
| Benchmarks: perfect foresight; energy-only; stagewise-independent states | Bore & Brensholm 2025 (deterministic model); Helseth case A and Bore "No CMP"; `kleiven2023` (independent chain) | | **Same** |
| Benchmark: weekly cyclic operation | none | | **Own** |
| Durations D^G, D^P and the interaction contrast (`eq:durations`, `eq:interaction`) | "hours of storage" in `sioshansi2009estimating`; the contrast is a standard factorial contrast | analysis design, not part of the optimisation model | **Own** (analysis) |

## 4. What is ours alone, in one list
1. (Corrected 2026-11-13: not ours alone.) The four reserve variables per unit and direction and the pump's headroom are in `chazarra2018` with binaries and a minimum consumption; ours is the linear version.
2. The pump's reserve limit R^{P,max}.
3. The pump term in the water margin.
4. Reserves from idle units combined with zero minimum output.
5. A pumped-storage plant with one reservoir and an unlimited lower reservoir inside a hydropower scheduling model.
6. The formula for the starting bound B_s.
7. The price standard deviation as a clustering feature, and the scaling of features.
8. Held-out test paths and a validation set.
9. The weekly cyclic benchmark and the interaction contrast.

Where ours is simpler than the two closest studies: one constant conversion factor instead of a piecewise-linear discharge curve (Bore, Helseth), no minimum output (Bore), no penalty water (both).

## 5. Things in ch. 6 that no longer match later decisions
- Sections 6.5–6.6 describe held-out data and a validation set; the recipe proposed on 2026-11-12 (Q-006) tests on the weather years the chain was built from. One of the two must change.
- "Long-term model" and "From Weekly Operation to Long-Term Planning" conflict with D-004 (medium-term).
- The header comment points to a file in the old workspace; point it here instead.

## 6. The elements that are ours alone, one by one (added 2026-11-13, Anders' question)
1. **Pump reserve limit R^{P,max}.** No paper has a separate cap. In `chazarra2018` the pump's reserve is bounded by its range between minimum and maximum consumption (p. 106). `entsoe2019psh` (slide 5): fixed-speed pumps cannot regulate active power; variable-speed pumps can "typically only within ~70–100 %" of power. Option with a source: set R^{P,max} = 0.3·P^{P,max} for a variable-speed pump and 0 for a fixed-speed one, and say so.
2. **Pump term in the water margin.** If the pump must reduce by r MW for a whole period, η^P·r·Δ/κ less water reaches the reservoir. The term extends Helseth (8) to the pump with the same worst-case logic (full activation for the whole period). `chazarra2018` handles reserve water differently: the water balance includes the expected real-time use of reserves as a percentage of the cleared capacity. Defensible as the direct analogue of Helseth (8); state it as such.
3. **Reserves from idle units with zero minimum output.** The most consequential one. `chazarra2018`: "When a unit is off in generating mode … there is no available secondary regulation reserve" (eq. 32, p. 108). Bore keeps C^min ≤ p (7); Helseth has the spinning rule (6). The response times in the market documents (FCR-D 86 % within 7.5 s; FCR-N 63 % within 60 s; aFRR full activation within 5 min, `ph24_statnett_reserve_overview`, `ph24_statnett_afrr`) cannot be met by a stopped unit for FCR. The model therefore sells FCR from units that are not running, mostly in hours where they would otherwise be off, and overstates reserve income. Options: keep it and report it as an upper bound (as the assumptions table does); or bring back a linear running rule for the FCR products in the form of Helseth (6), which keeps the model an LP; or run both and report the difference.
4. **One reservoir, unlimited lower reservoir.** Fine for a plant that pumps from a lake, fjord or reservoir much larger than a week of pumping; not for a small lower pond. Alic, Gudbjerg, Schindler and Löhndorf (2013) all model the lower reservoir. It removes one state variable, which keeps the cuts one-dimensional. Keep as an assumption and say which plants it covers.
5. **Formula for the starting bound B_s.** Harmless: any valid upper bound gives the same policy. One sentence is enough; a large constant would also do.
6. **Price standard deviation as a third clustering feature, and the scaling.** Reason: two weeks with the same mean price but different spread are worth different amounts to a pump. No precedent; Bore and Schäffer cluster on price level and inflow only. With 30 years and three clusters a third feature spreads the clusters thinner. Option: base case as Bore (two features), the three-feature version as a sensitivity tied to RQ3. The scaling has to be stated in either case (Gjelsvik 2010 normalises inflow by weekly mean and standard deviation).
7. **Held-out test paths and a validation set.** No hydropower study does this, and with 30 weather years a split leaves too few years to estimate transitions. Replace with the two-part evaluation in `markov-states-method.md` §5 (new paths from the chain; the 30 weather years), or keep a leave-some-years-out run as a robustness check without a citation.
8. **Weekly cyclic benchmark.** Forces each week to end where it started, so the difference to the SDDP policy is the value of moving water between weeks. It isolates what the long-duration storage adds, which is why it is useful, but no paper has it; it needs one explaining sentence, not a citation.
9. **Interaction contrast between two parameters.** Written for the earlier research questions (pump, turbine and reservoir jointly). After D-003 only the pump is varied, so it is needed only if pump size is crossed with the price model year; otherwise it can go.

