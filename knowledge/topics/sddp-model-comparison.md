# SDDP sources against the chapter 6 model: what they have that we lack, and what we have that none of them has

Written 2026-11-15 (Claude with Anders, on Anders' request). Model checked: `../pumped-hydro-thesis/Sections/06_mathematical_model.tex`, thesis commit b767ad1 (2026-11-10).

**Sources checked (56):** the 55 entries tagged `sddp-markov-chain` or `sddp-time-series`, plus `li2022solving` (a modified SDDP inside a one-day model). Eleven were added on 2026-11-15 (Section 7). This file complements `model-precedents.md`, which also draws on papers that do not use SDDP (Schindler 2024, Chazarra 2018, Alic 2023).

**How it was checked.** "text" = the passage was read in `paper.txt` on 2026-11-15. "note" = taken from the source's structured note, which was written from the text copy and gives the page. `gjelsvik1999` is a scanned PDF, so only its note could be used. Where a source is not listed for an element, the element was not found in its note or text; that is not proof of absence.

## 1. Result in short
- **What they have and we lack.** Almost all of it is already named as an assumption in the two assumption tables of chapter 6: one reservoir, continuous power from zero, constant head and efficiency, free spillage, no start-up cost, ramp limit or environmental rule, reserves without a running unit, no activation, deterministic capacity prices, the whole week known in advance. Three things in the SDDP sources are not named there: a charge on electricity bought for pumping (`gjelsvik2010`; possibly meant by "other operating costs"), intraday trading (`bore2026`, `lohndorf2013`, `seifert2025`) and forward contracts (`mo2001`, `garcia2025longterm`). System elements (demand, thermal plants, transmission) do not apply to a price taker (Section 3).
- **Which omissions the sources show to matter.** Reserves without a running rule: linear models overstate the reserve a producer can deliver (`hjelmeland2018impact` p. 1, citing `hjelmeland2016combined`). The whole week known in advance: finer resolution and within-week uncertainty raise the level and spread of water values (`helseth2026considering` p. 21). Penalties on slack variables change the water values (`bueno2023impact` p. 2), which concerns the end-volume penalty in the implementation (Q-007).
- **What we have and no SDDP source has** (Section 5): reserve capacity sold from the pump (variables r^{P+}, r^{P−}, the pump headroom constraints, the limit R^{P,max} and the pump term in the water margin); reserves from units that are not running; the bound formula B_s; the price standard deviation as a clustering feature; held-out test paths with a validation set; the weekly cyclic benchmark and the interaction contrast. (Corrected 2026-11-15: a pumped-storage plant with a single reservoir was first listed here; it has precedents, see Section 8.)
- **The combination is the gap.** Eleven SDDP sources model pumping. Only one of them sells reserve capacity (`abgottspon2015hydro`, from its turbines). None sells reserve from the pump, and none combines pumping with joint price–inflow Markov states.

## 2. The sources, one line each
"Owner" = profit-maximising price taker with exogenous prices. "System" = cost minimisation with demand, so prices are results, not inputs.

| Source | Perspective | Stage (inside the stage) | Price uncertainty | Inflow | Pump | Reserve capacity |
|---|---|---|---|---|---|---|
| `gjelsvik1999` (note only) | owner | week | Markov price nodes | sampled outcomes | no | no |
| `gjelsvik2010` | owner; also system | week (load periods) | Markov price nodes | sampled outcomes | no | no |
| `mo2001` | owner | week | builds the price Markov model | – | no | no |
| `gjelsvik2005considering` | owner | week | ProdRisk price model | inflow states | no | no |
| `helseth2015cooptimizing` | owner | week (21 steps) | Markov, 5 price points | AR | no | FCR-N, price deterministic |
| `helseth2016` | owner | week (21 steps, 6 reserve blocks) | Markov, energy × capacity price nodes | AR(1) | no | yes, price stochastic |
| `helseth2018optimal` | owner | week (21 steps) | Markov, 3 energy × 2 capacity clusters | AR(1) | no | yes |
| `hjelmeland2016combined`, `hjelmeland2016case` | owner | week (21 steps) | Markov price nodes | AR(1) | no | FCR-N, price deterministic |
| `hjelmeland2018impact` | owner | week (21 steps) | none | weekly inflow | no | capacity market, deterministic |
| `hjelmeland2019tste` | owner | week | VAR(1), binary expansion | VAR(1) | no | yes, price deterministic |
| `hjelmeland2019energies` | owner | week (21 steps) | VAR(1) with saddle cuts | VAR(1) | no | yes, price stochastic |
| `hjelmeland2019phd` | owner | thesis that collects the five above | | | no | yes |
| `helseth2020nonconvex` | owner | week | none | inflow model | no | no |
| `helseth2022hydropower` | owner | week (none) | none | VAR(1) | no | no |
| `larsen2015evaluation` | owner | week | none | AR(1), reduced | no | no |
| `dimoski2018hydropower` | owner | week | lattice from a forward-price model | lattice | no | no |
| `kleiven2023` | owner | week (none) | joint price–inflow nodes | joint | no | no |
| `grini2023` | owner | week (none) | 125 joint states | joint | no | no |
| `bore2026` | owner | week (hours) | joint K-means states | joint | no | aFRR, FCR-N, FCR-D, prices deterministic |
| `gudbjerg2024exploring` | owner | week (56 three-hour steps) | ProdRisk price layer | SDDP part | **yes** | no |
| `hagenvik2022comprehensive`, `schuller2024practical` | owner | week (three-hour steps) | ProdRisk | ProdRisk | **yes** (Duge) | no |
| `lohndorf2013` | owner | day (hours) | lattice | lattice | **yes**, upper and lower reservoir | no |
| `abgottspon2015hydro` | owner | day or week (hours) | sampled, independent | sampled | **yes** | secondary reserve from turbines |
| `abgottspon2016multihorizon` | owner | day (hours) | none in the case | none in the case | **yes** | no |
| `li2022solving` | owner | hour, one day | scenario tree, independent | – | no | no |
| `downward2020stochastic` | owner (example) | 12 stages | autoregressive price as a state | – | no | no |
| `garcia2025longterm` | owners in a market | month | Markov chain on joint scenarios | AR | no | no |
| `seifert2025` | battery owner | 4-hour block, 3 days | three-dimensional Markov chain | – | charge and discharge | FCR, price stochastic |
| `chancelier2026optimal` | storage owner | hour, one day | Markov chain by quadrature | – | charge and discharge | no |
| `vanackooij2020conditional` | gas storage owner | week, one year | conditional cuts | – | injection and withdrawal | no |
| `helseth2013` | system | week (7 or 24 sub-periods) | price states for an outside market | lag-1 model | **yes** | no |
| `papavasiliou2018application` | system | 15 minutes, one day | – | – (renewables AR) | **yes**, aggregate | fixed beforehand |
| `philpott2023using`, `hole2025capacity` | system | week (load blocks), infinite horizon | – | independent | **yes** (Lake Onslow) | no |
| `helseth2025` | system | week (1–8 hour steps) | – | VAR(1); wind and solar inside the week | as an extension | system requirement |
| `helseth2024approximating` | system | week (42 four-hour steps) | – | VAR(1) | no | system requirement |
| `helseth2026considering` | system | week (2–24 hour steps) | – | VAR(1); wind and solar inside the week | no | no |
| `pereira1991`, `dematos2015improving`, `lohndorf2019`, `shapiro2020`, `bueno2023impact` | system (Brazil) | month | – | independent, autoregressive or Markov | no | no |
| `philpott2012` | system (New Zealand) | week (3 load blocks) | – | Markov chain | no | no |
| `helseth2015efficient` | one watercourse with thermal supply | week (7 sub-periods) | – | VAR(1) | no | no |
| `tilmant2008` | multipurpose reservoirs | month | – | AR(1) | no | no |
| `shapiro2011`, `philpott2008`, `dowson2020`, `fullnerRebennack2025`, `seranilla2023applications`, `seranilla2025`, `roald2023`, `helseth2020scheduling`, `helseth2023hydropower` | theory, tutorials, surveys and toolchain descriptions | | | | | |

## 3. What the SDDP sources have that our model lacks

### 3.1 Sets
| Set in other models | Sources | In ours |
|---|---|---|
| Several reservoirs or stations, with the set of upstream reservoirs | nearly all hydropower sources, e.g. `helseth2018optimal` (nomenclature, p. 1, text), `gjelsvik2010`, `grini2023` | one reservoir |
| Discharge segments of a station (piecewise-linear generation) | `helseth2016` eq. (4), `helseth2018optimal` eq. (10c), `helseth2020nonconvex` eqs. (3c)–(3d) (text), `helseth2022hydropower` eq. (4c), `bore2026` eq. (8) | one conversion factor |
| Units of a plant with on/off status | `li2022solving` eqs. (7)–(8), (20)–(25) (text), `hjelmeland2019tste`, `abgottspon2016multihorizon` | one generating and one pumping unit, continuous |
| Reserve-market blocks that group time steps | `helseth2016` (6 weekly blocks), `hjelmeland2016combined` | hourly products only |
| Energy markets (day-ahead, intraday sell, intraday buy) | `bore2026` (set E, text), `lohndorf2013`, `seifert2025` | day-ahead only |
| Price clusters separate from inflow outcomes; energy-price × capacity-price nodes | `gjelsvik2010`, `helseth2016`, `helseth2018optimal` p. 7 (text) | joint price–inflow states |
| Lags of an inflow model | `pereira1991`, `tilmant2008`, `garcia2025longterm` (text) | none |
| Scenarios of wind and solar inside the stage | `helseth2026considering` p. 5 (text), `helseth2025` | none |
| Load blocks of a duration curve | `philpott2012`, `philpott2023using`, `hole2025capacity` (text), `gjelsvik2010` | chronological hours |
| Volume ranges that switch a rule on and off | `bueno2023impact` (text), `helseth2020nonconvex` | none |
| Maintenance window; investment options | `helseth2018optimal`; `hole2025capacity` (text) | none |
| System sets: network nodes and lines, thermal plants, renewable plants, load types, agents | the system sources; `garcia2025longterm` | not applicable to a price taker |

### 3.2 Parameters
| Parameter in other models | Sources | In ours |
|---|---|---|
| Minimum output of a unit | `bore2026` eq. (7), `helseth2016` (stations with 70 and 50 MW minimum), `helseth2013` (minimum pumping capacity, text) | zero |
| Energy equivalent per discharge segment; maximum discharge per segment | `helseth2018optimal` (nomenclature, text) | one factor κη^G |
| Maximum bypass; spillway capacity | `helseth2018optimal` eq. (10k), `helseth2020nonconvex` eq. (3h); `philpott2023using` p. 3 (text) | none, spillage unlimited |
| Cost or penalty on spillage | `downward2020stochastic` p. 12 (text) | none |
| Time-dependent reservoir, discharge and bypass limits | `helseth2018optimal` (limits per time step), `helseth2020nonconvex` eqs. (3f)–(3h) (text) | constant V^min, V^max |
| Minimum and maximum outflow, also by storage range | `bueno2023impact` p. 15, `philpott2023using` p. 4 (minimum flows in some cases) (text) | none |
| Start-up and shutdown cost, minimum up and down time, forbidden zone | `li2022solving` p. 09 (text), `hjelmeland2019tste`; linearised start-up cost for pumps and units in `helseth2013` Sec. 2.4 (text) | none |
| **Transmission charge on electricity sold and bought** | `gjelsvik2010` (purchase from the spot market, transmission charge, text lines 276–304; "mostly neglected" in practice), `gjelsvik1999` (note) | none; pumping is bought at the day-ahead price |
| Market-share limit; price response | `bore2026` (intraday limited to 10 % of hourly volume, text), `lohndorf2013`, `garcia2025longterm` | none |
| Scaling factors that turn a weekly average price into prices per time step | `helseth2018optimal` (nomenclature, text), `helseth2016`, `helseth2015cooptimizing` | hourly profile stored in each state |
| Stochastic capacity price | `helseth2016`, `helseth2018optimal` p. 7, `hjelmeland2019energies`, `seifert2025` | deterministic |
| Inflow model coefficients (autoregressive) | `helseth2022hydropower`, `helseth2026considering` pp. 13–14 (text), `tilmant2008`, `garcia2025longterm` | none |
| Penalty on artificial, emergency or "tank" water and on slack variables | `helseth2016`, `bore2026` (text), `hjelmeland2016combined`, `helseth2022hydropower`, `seifert2025` (3,000 EUR/MWh), `bueno2023impact` p. 22 (text) | none in ch. 6 (the implementation has one, Q-007) |
| End-value function or end-value cuts from a longer run or another model | `helseth2016`, `helseth2018optimal` p. 7 (text), `helseth2020nonconvex` p. 4 (text), `gjelsvik2005considering`, `tilmant2008`, `grini2023`, `li2022solving` eq. (14) (text) | zero after extra weeks |
| Risk parameters | `philpott2012`, `lohndorf2019`, `shapiro2020` (CVaR), `chancelier2026optimal` (utility) | risk neutral |
| Forward contract price and quantity; firm demand | `garcia2025longterm` p. 7 (text), `mo2001`, `gjelsvik2010` | none |
| Investment cost of capacity | `hole2025capacity` p. 7 (text) | pump capacity is varied by re-solving |
| Number of backward openings | sources with sampled inflow, e.g. `helseth2018optimal` (12), `helseth2026considering` (10) | all Markov states are solved, no sampling in the backward pass |
| System parameters: demand, thermal cost, rationing cost, line capacities | the system sources | not applicable |

### 3.3 Constraints and variables
| Constraint or variable in other models | Sources | What it would mean for us |
|---|---|---|
| **Reserve only from a unit that is running** (capacity sold ≤ generation, or a factor on it) | `helseth2016` eqs. (6), (13); `helseth2018optimal` eq. (10d), p. 7 (text); `hjelmeland2019phd` eq. (3.1); `bore2026` eqs. (7), (10) | ours sells reserve from idle units; see `model-precedents.md` §6 item 3 |
| Bypass variable | `helseth2018optimal`, `helseth2020nonconvex` (text) | not needed with one reservoir |
| Lower reservoir balance | `lohndorf2013`, `gudbjerg2024exploring`, `abgottspon2016multihorizon`; river chain in `philpott2023using` | a second state variable |
| State-dependent maximum discharge | `helseth2020nonconvex` eqs. (4)–(5) (text), `helseth2022hydropower` | nonconvex; plant-specific |
| Ramping limits | `helseth2024approximating`, `papavasiliou2018application` (note); named as an option in `helseth2026considering` p. 15 (text) | rarely binding at hourly steps |
| Start-up logic, with binaries or linearised | `li2022solving`, `hjelmeland2019tste`; `helseth2013` eqs. (14)–(19) (text) | the linearised form keeps the LP |
| Head effects | `gjelsvik2005considering`, `gudbjerg2024exploring`, `li2022solving` eqs. (9)–(13) (text) | nonlinear |
| Energy margin for downward reserve as well as upward | `seifert2025` eq. (10b) (text): the state of charge must leave room for the reservation in both directions; `bore2026` eq. (5) | ours has no downward margin because spillage is free |
| Intraday trading; bid curves | `bore2026`, `lohndorf2013`, `seifert2025`, `chancelier2026optimal` | another market |
| Within-stage uncertainty: the stage decision is made before wind, solar or prices of the stage are known | `helseth2026considering` pp. 5–7 (text), `helseth2025`, `lohndorf2013` (bids before prices), `grini2023` | ours knows the whole week |
| Inflow as a state variable in the cuts | `helseth2018optimal` p. 7 (text), `helseth2022hydropower`, `helseth2026considering`, `tilmant2008` | ours has inflow inside the Markov state |
| Price as a continuous state (saddle cuts, binary expansion, conditional cuts) | `downward2020stochastic`, `hjelmeland2019energies`, `hjelmeland2019tste`, `vanackooij2020conditional` (text) | alternative to the Markov chain |
| End volume equal to start volume; start and end state of charge fixed | `bore2026` eq. (4); `seifert2025` eq. (10c) (text) | conflicts with ch. 6, see Q-007 |
| Infinite horizon on a yearly cycle with discounting; serial simulation where one year's end is the next year's start | `hole2025capacity` p. 6, `philpott2023using` p. 4 (text), `dowson2020`; `gudbjerg2024exploring` | alternative to the extra weeks |
| Capacity as a state variable chosen inside SDDP | `hole2025capacity` pp. 6–7 (text) | an alternative to re-solving for each pump size |
| Maintenance binaries | `helseth2018optimal` | not relevant |
| Forward contracts, risk measures | `garcia2025longterm`, `mo2001`, `gjelsvik2010`; `philpott2012`, `lohndorf2019` | outside the scope of the research questions |
| Demand balance, thermal generation, rationing, transmission, wind and solar generation | the system sources | not applicable to a price taker |

## 4. Our sets, parameters, variables and constraints: which SDDP sources have the same
Verdicts as in `model-precedents.md`: **Same**, **Adapted**, **None** (no SDDP source).

| Our element (label) | SDDP sources with the same | Verdict |
|---|---|---|
| Set T, hours of the week | `bore2026`; hours inside the stage also in `lohndorf2013`, `abgottspon2015hydro`, `helseth2025` | Same |
| Set F^C of reserve products with a price per hour and direction | `bore2026` | Same |
| Set F^{C,sym} | symmetric products are modelled with one variable in `helseth2016`, `helseth2018optimal` p. 7, `seifert2025` | Adapted (bookkeeping) |
| Sets S and M: weekly stages; states that hold both price and inflow | `bore2026`, `kleiven2023`, `grini2023`, `dimoski2018hydropower`; joint chain also in `garcia2025longterm` pp. 7–8 (text) | Same |
| Set L_{s,m}: cuts per week and Markov state | `gjelsvik1999`, `gjelsvik2010`, `helseth2016`, `helseth2018optimal` pp. 6–7 (text), `philpott2012`; "one FCF for each possible future Markov state" in `garcia2025longterm` p. 5 (text); `downward2020stochastic` p. 2 (text) | Same; not `bore2026` |
| V^min, V^max, V^in, V^init, P^{G,max}, Δ_t | all | Same |
| P^{P,max} | `helseth2013` (maximum and minimum pumping capacity, text), `lohndorf2013` (text line 356), `philpott2023using` p. 11, `gudbjerg2024exploring` | Same |
| H, κ, η^G: one constant conversion factor | `kleiven2023`, `philpott2012`, `philpott2023using` p. 3, `lohndorf2013`, `garcia2025longterm` p. 6, `bueno2023impact` p. 13 (text) | Same; writing it through the head H is ours |
| η^P | `philpott2023using` p. 5 (77 % round trip, text), `gudbjerg2024exploring` (pump efficiency 0.8, text), `papavasiliou2018application` (note) | Same |
| I and φ_t: weekly inflow spread evenly | `helseth2016`, `helseth2018optimal` (relative duration of the time step, text), `philpott2023using` p. 4 (inflow constant over the week, text) | Same |
| C^E_DA: an hourly price profile in each state | `bore2026` | Same; the Helseth papers scale a weekly average |
| C^{C↑}, C^{C↓} deterministic and equal in all states | `bore2026`, `helseth2015cooptimizing`, `hjelmeland2016combined`, `hjelmeland2019tste` | Same |
| R^max_f | `bore2026` eq. (12); `seifert2025` (FCR bids at most half the rated power, text) | Same |
| R^{G,max} | `helseth2016` eq. (12) and 10 % of installed capacity; `helseth2018optimal` eq. (10l) and p. 7 (text) | Same |
| **R^{P,max}** | none | **None** |
| S, S^ext, N: more weeks solved than reported | `shapiro2020`, `lohndorf2019`, `bueno2023impact` p. 22 (24 months solved, 12 analysed, text), `kleiven2023`, `gjelsvik2005considering`, `hjelmeland2016case` | Same |
| π: transition probabilities per week | `mo2001`, `gjelsvik2010`, `helseth2016`, `bore2026`, `kleiven2023` | Same |
| β: weekly discount factor | `kleiven2023`; annual factor to the power 1/52 in `philpott2023using` p. 4 and `hole2025capacity` pp. 23–24 (text); `grini2023`, `pereira1991`, `shapiro2020`, `dowson2020` | Same |
| B_s, M̄_s | a starting bound is required (`fullnerRebennack2025`); the formula is not in any source | device Same, formula **None** |
| Variables v, w, p^G, α | all | Same |
| Variable p^P | the eleven sources with pumping in Section 2 | Same |
| c↑, c↓, r^{G+}, r^{G−} | `bore2026` eqs. (10)–(12) | Same |
| **r^{P+}, r^{P−}** | none in hydropower. In `seifert2025` the reservation reduces the battery's power in both directions (text, p. 12) | **None** for a pump; Adapted from a battery |
| Generator headroom (`eq:gen_max`) | `helseth2016` eq. (7), `helseth2018optimal` eq. (10e) (text), `bore2026` eq. (11) | Same |
| Downward reserve ≤ output (`eq:gen_min`) | `bore2026` eq. (10) with a minimum output | Adapted |
| **Pump headroom (`eq:pump_max`, `eq:pump_min`)** | none | **None** |
| Generator reserve limit (`eq:gen_reserve_limit`) | `helseth2016` eq. (12), `helseth2018optimal` eq. (10l) | Same |
| **Pump reserve limit (`eq:pump_reserve_limit`)** | none | **None** |
| Volume limits, initial volume, weekly continuity | all | Same |
| Water margin, generator term (`eq:energy_up`) | `helseth2016` eq. (8), `helseth2018optimal` eq. (10f), p. 7 (text) | Same |
| **Water margin, pump term** | none in hydropower; `seifert2025` eq. (10b) is the same idea for a battery | **None**; Adapted from a battery |
| Water balance with pumping (`eq:water_balance`) | `lohndorf2013`, `papavasiliou2018application`, `philpott2023using` p. 4 (pumping as a release with a negative conversion factor, text), `helseth2013` | Same |
| Commitment split between the two units (`eq:alloc_up`, `eq:alloc_down`) | `helseth2016` eq. (5) splits a watercourse obligation between stations | Adapted |
| Product limits and symmetry (`eq:commit_limit`, `eq:symmetric`) | `bore2026`; `helseth2016`, `seifert2025` | Same; Adapted |
| Free spillage, no penalty | `kleiven2023` p. 5 (text) | Same |
| Continuous power from zero, no start-up | `kleiven2023`, `philpott2012` | Same |
| **Reserves from a unit that is not running** | none; every hydropower source with reserves has a running rule or a minimum output | **None** |
| Pumped storage with one reservoir (the lower reservoir never limits) | `papavasiliou2018application`: one stored-energy variable per pumped-hydro unit, no lower reservoir (text). A single store facing a price also in `seifert2025`, `chancelier2026optimal`, `vanackooij2020conditional` p. 187 (text). Outside SDDP: `abgottspon2014` p. 5 and `liu2025analytical` (text), see Section 8 | Same (corrected 2026-11-15; first listed as None) |
| Recursion, expectation over next week's states (`eq:bellman`, `eq:expected_future`) | `gjelsvik2010`, `philpott2012`, `lohndorf2019`, `garcia2025longterm` eqs. (6)–(8) | Same |
| Zero value after the last week (`eq:terminal_value`) | `philpott2008`, `garcia2025longterm` p. 5 (text), `shapiro2020` | Same |
| One expected cut per state and trial volume (`eq:cuts`, `eq:cut_coefficients`) | `gjelsvik1999` eq. (23) (note), `kleiven2023` | Same; `garcia2025longterm` keeps one function per future state instead |
| K forward paths; every state solved in the backward pass | `gjelsvik2010` p. 44; `helseth2018optimal` p. 6 ("one loops through each discrete price cluster", text) | Same |
| Stop when the upper bound is inside the confidence interval (`eq:stopping_rule`) | `helseth2016`; `helseth2018optimal` p. 6, `helseth2015efficient`, `li2022solving` pp. 10–11, `helseth2025` (text or note) | Same. In practice `helseth2018optimal` p. 8 and `helseth2022hydropower` stop on a stable upper bound |
| K-means per calendar week on paired price and inflow | `bore2026` | Same |
| **Price standard deviation as a third feature; standardised features** | none | **None** |
| Representative week = the sample closest to the centre | `bore2026` uses the median series | Adapted |
| Transition probabilities by counting (`eq:transition`) | `mo2001`, `helseth2016`, `bore2026`; `garcia2025longterm` estimates them by expectation maximisation | Same |
| **Held-out test paths and a validation set for the number of states** | none. Nearest: policies simulated on historical inflow years after training in `philpott2023using` pp. 11–12 and `hole2025capacity` p. 17 (text); a separately sampled set of 1000 scenarios in `helseth2020nonconvex` p. 5 (text) | **None** |
| Profit and remaining water value reported separately (`eq:oos_profit`–`eq:oos`) | `helseth2016` p. 940 adjusts profit for the change in reservoir level | Adapted |
| Benchmarks: perfect foresight; energy only; independent states | `abgottspon2015hydro` (perfect information, note); `helseth2016`, `helseth2018optimal` cases A and B, `bore2026`; `kleiven2023` | Same |
| **Weekly cyclic benchmark; interaction contrast; durations D^G, D^P** | none | **None** (analysis design) |

## 5. Ours alone among the SDDP sources
| Element | Precedent outside SDDP | Comment |
|---|---|---|
| Reserve capacity from the pump: r^{P+}, r^{P−}, `eq:pump_max`, `eq:pump_min` | `chazarra2018` (MILP, per unit and mode), `schindler2024` (plant level) | among SDDP sources only the battery in `seifert2025` reserves power in both directions |
| Pump reserve limit R^{P,max} | none | `seifert2025` caps the reservation at half the rated power as a "conservative assumption"; see `implementation-parameters.md` §4 |
| Pump term in the water margin | none | the battery analogue is `seifert2025` eq. (10b) |
| Reserves from units that are not running | none | optimistic; the assumptions table says so |
| Formula for the bound B_s | none | harmless |
| Price standard deviation as a clustering feature, with standardised features | none | |
| Held-out test paths and a validation set | none | conflicts with the recipe under Q-006 |
| Weekly cyclic benchmark, interaction contrast, durations | none | analysis design, not part of the model |

Sets and parameters that are only bookkeeping (F^{C,sym}, κ = 2.725H, φ_t) are not counted as ours alone.

## 6. Facts from the new sources that bear on open questions
- **Cuts per Markov state (earlier discussion with Anders).** `helseth2018optimal`: cuts are "built and stored for each price cluster", and the backward iteration loops through each price cluster and each state trajectory (pp. 6–7). `garcia2025longterm` p. 5: the Markov reformulation has one future cost function per future Markov state; the paper traces it to Gjelsvik et al. (1999) and says it has since been "termed Markovian SDDP". `downward2020stochastic` p. 2: with a Markov chain "cuts must be added for all of the discretized Markov states". Garcia et al. thus treat the hybrid SDP/SDDP method and Markov-chain SDDP as one approach, where `fullnerRebennack2025` keeps them apart.
- **End of the horizon (Q-007).** Solved horizon twice the analysed one in `bueno2023impact` p. 22. Infinite horizon with discounting in `hole2025capacity` and `philpott2023using`; Hole et al. write that a finite horizon needs very long horizons for a steady-state result (p. 3). End-value cuts from a four-year run in `helseth2018optimal` p. 7. Start and end state fixed with a penalised slack in `seifert2025`.
- **Penalty size (Q-007).** `bueno2023impact` pp. 2, 25: the penalties on slack variables strongly affect the water values.
- **Stopping rule (Q-007).** `helseth2018optimal` p. 8: the confidence-interval test was sensitive to the case and the sampling settings, so stabilisation of the upper bound was used. `bueno2023impact` pp. 21–22: one forward path per iteration reaches the same bound as ten, in more iterations. `hole2025capacity` p. 16: fixed limit of 1000 iterations.
- **Discount factor.** 0.9 a year in `philpott2023using` (chosen "for convenience", p. 21) and `hole2025capacity`; 2 % in `kleiven2023`. `bore2026` uses 3 %, 7 % and 10 % for the net present value of the investment, not inside SDDP (text), so the 0.97 in the configuration matches Bore's lowest rate but for another purpose.
- **Round-trip efficiency.** 77 % in `philpott2023using` p. 5; 76.5 % in `papavasiliou2018application` (note). The 0.765 in the configuration is therefore what SDDP studies assume for a generic plant; Pitorac's plant data still put Duge near the low end of 65–80 %.
- **Reserve limit.** 10 % of installed capacity again in `helseth2018optimal` p. 7.
- **Within-week foresight.** `helseth2026considering` p. 3: assuming that uncertainties are known within the stage is reasonable for inflow, less so for wind and solar; with finer time resolution the level and spread of water values rise (p. 21).
- **Pump capacity as a decision.** `hole2025capacity` puts capacity in the SDDP model as a state variable chosen in a first node (pp. 6–7).
- **Tariff on pumping.** `gjelsvik2010` has a transmission charge on purchases and sales, mostly neglected in practice. Ours has none; whether a grid tariff applies to the pump's consumption is a case question.

## 7. Search of 2026-11-15 and the eleven sources added
Asked for: ten more SDDP papers on hydropower or pumped hydro from after 2016. Searched arXiv (API) and OpenAlex (title, abstract and full-text search, open access, from 2017), plus two web searches. Only open-access copies from publishers or repositories were downloaded. Logged in `literature/search-log.md`.
- Hydropower, peer reviewed: `helseth2018optimal`, `helseth2020nonconvex`, `hjelmeland2018impact`, `helseth2026considering`, `li2022solving`, `hole2025capacity`, `downward2020stochastic`, `garcia2025longterm`.
- Hydropower, not peer reviewed: `philpott2023using` (technical report, the only SDDP study of a seasonal pumped storage found), `bueno2023impact` (study-group report).
- Storage, peer reviewed: `vanackooij2020conditional` (motivated by hydro reservoirs, tested on gas storage).
- An OpenAlex title-and-abstract search for "dual dynamic programming" together with pumped, pumping or pump, from 2017, gave 7 hits, none of them an owner's pumped-storage study.
- All eleven are in `references.bib` since 2026-11-15 (added through Zotero with the keys pinned; thesis commit 26db8fb).

## 8. Constraints shared by the models with a pump (Anders' question, 2026-11-15)
Question: is there a constraint that every other model with a pump has and ours lacks? **No.** Checked across the SDDP sources with pumping and the other pump and storage models in the library; "text" = read in `paper.txt` on 2026-11-15, otherwise from the note.

What every pump model has, ours included: a limit on pumping power, an efficiency loss between pumping and generating, and limits on the stored volume or energy.

Three things are common but not universal:
| Constraint | Models that have it | Models without it, like ours |
|---|---|---|
| The source of the pumped water is limited (a lower reservoir, or the water balance of a river) | models of a specific watercourse: `lohndorf2013`, `abgottspon2013stochastic`, `abgottspon2015hydro`, `abgottspon2016multihorizon`, `schindler2024`, `alic2023optimal`, `ak2019quantifying`, `gudbjerg2024exploring`, `hagenvik2022comprehensive`, `schuller2024practical`, `braaten2016linear`; river chain in `philpott2023using` pp. 4–5 (text) | `abgottspon2014` p. 5: the aggregated plant assumes "an infinite lower basin for pumping" (text); `liu2025analytical`: the lower reservoir is "effectively unlimited", a large lake or river (text); `papavasiliou2018application`: one stored-energy variable per pumped-hydro unit (text); stores in energy units in `naval2025optimization`, `finnah2022integrated`, `lohndorf2023`, `sioshansi2009estimating`, `bradbury2014economic`, `kloess2014bulk`, `sauhats2016optimal` |
| The pump cannot run at any power from zero (minimum power, on/off, or a fixed operating point) | `lohndorf2013` (minimum and maximum capacities with binaries), `abgottspon2015hydro`, `abgottspon2016multihorizon` (on/off pumps, forbidden zones), `chazarra2016stochastic` (fixed operating point), `chazarra2017`, `chazarra2018` (range between minimum and maximum consumption), `naval2025optimization` (minimum 38.93 of 113.5 MW), `zhang2026unlocking`, `finnah2022integrated` (working range 5–10 MW), `helseth2013` (minimum pumping capacity, linearised start-up, text) | `alic2023optimal`: the pump resembles a fully-fed or doubly-fed machine rather than a fixed-speed pump, which the authors treat as an upper bound on flexibility (text, p. 14); `schindler2024` (no on/off constraints); `papavasiliou2018application`; `philpott2023using`; the storage-valuation papers |
| Pumping and generating cannot happen at the same time | `gudbjerg2024exploring` p. 22, `chazarra2016stochastic` (within a unit), `chazarra2018` eq. (43), `chazarra2017` in the conventional configuration, `zhang2026unlocking` eq. (18) | `schindler2024` (no constraint; shows it is never needed when spill is free), `chazarra2017` with hydraulic short-circuit, the linear storage models |

Less common: a start-up cost on the pump (`chazarra2017`, `chazarra2018`, `naval2025optimization`, `finnah2022integrated`, linearised in `helseth2013`); a charge on the energy pumped (`finnah2022integrated`, grid fees on the stored energy, Assumption 5, text; an operating cost per MWh pumped in `naval2025optimization`).

- **Correction.** The single reservoir was listed as ours alone on 2026-11-13 and 2026-11-15. It is not: `abgottspon2014`, `liu2025analytical` and `papavasiliou2018application` make the same assumption for pumped storage. The rows in Sections 1, 4 and 5 and in `model-precedents.md` are corrected.
- **For the Duge case.** The lower-reservoir limit is the one of the three that Duge actually has: pumping is not allowed when the lower reservoir is below about 650 masl (`pitorac2020technical` p. 16; `hagenvik2022comprehensive` p. 5; `schuller2024practical` p. 5). Hågenvik et al. note that the medium-term model cannot represent this rule while the short-term model can. The lower reservoir itself is large (926 Mm3, `pitorac2020technical` Table 2).

## 9. Who lets the pump provide reserves (Anders' question, 2026-11-15)
**Yes, several do, but no SDDP model of a hydropower plant does.** Read in `paper.txt` on 2026-11-15 unless marked "note".

| Source | Model | How the pump (or the charging side) provides reserve | Where |
|---|---|---|---|
| `chazarra2018` | MILP, price-taking variable-speed pumped storage, day-ahead and secondary reserve | in pumping mode the upward reserve is the current minus the minimum consumption and the downward reserve the maximum minus the current consumption; fixed-speed units pump at a single point and give no reserve while pumping | p. 106; eqs. (30)–(37), p. 108 |
| `chazarra2017` | MILP, pumped storage with hydraulic short-circuit | fixed-speed units "are not able to provide load-frequency control" when pumping; with pump and turbine running together (short-circuit) the plant regulates while it consumes. Ternary units raise income by 165.5 % and 141.3 % over the conventional plant in the two weeks studied (note) | pp. 345–346; p. 350 |
| `schindler2024` | planner–trader decomposition, cascade with pumps, spot and reserve | plant level: down-reserve bids are limited by spot bids plus pumping capacity | Prop. 4, PDF p. 17 (note) |
| `dallinger2019socioeconomic` | Austrian storage plants, spot and balancing | with pump-turbines added the operating range is about −70 % to 100 % of turbine capacity, so the plant need not generate to offer negative balancing | p. 491 |
| `deane2013derivation` | system unit commitment with a pumped-storage plant | each unit gives up to 100 MW spinning reserve when generating and "a full 250 MW in pumping mode" | p. 2148 |
| `drury2011value` | MILP, compressed-air storage, energy and reserves | while charging, spinning reserve up to the amount it is charging | p. 4961, Fig. 1 |
| `byrne2016estimating`, `elgersma2026` | generic storage, linear and mixed-integer | regulation or reserve capacity limited together with charging and discharging power | notes |
| `seifert2025` | **SDDP**, battery, FCR with day-ahead and intraday | the reserved power is held in both directions; reservation capped at half the rated power | p. 12, eq. (10b) |

**Who does not.** `chazarra2016stochastic` excludes the pumped-storage units from reserve provision (p. 72, note). `abgottspon2014` and `abgottspon2015hydro` sell secondary reserve from the qualified turbines only (note). Every SDDP hydropower source with reserves has no pump (Section 2).

**What decides it is the machine.**
- Fixed-speed pump: one operating point. It can give upward reserve only by being switched off (`deane2013derivation`, `drury2011value`), and no continuous regulation (`chazarra2017` p. 345; `mercier2017` p. 2; `entsoe2019psh` slide 5).
- Variable-speed pump: regulation between its minimum and maximum consumption (`chazarra2018` p. 106; `perezdiaz2015trends` p. 781, Fig. 5); about 70–100 % of power (`entsoe2019psh`, `eera_2016`).
- Hydraulic short-circuit (pump and turbine together): the turbine regulates while the pump runs (`chazarra2017`; `perezdiaz2015trends` p. 776; `kong2020overview`, note).

**Market rules.** `eera_2016` (citing an ENTSO-E survey of 2015; dated): only a few European systems (France, Belgium, Great Britain, Switzerland, Germany, Austria) allowed pumped storage to provide both containment and restoration reserves in pumping mode. Statnett: consumption or storage that meets the requirements can deliver aFRR, and production and consumption can bid in the mFRR capacity market (`ph24_statnett_afrr`, `ph24_statnett_mfrr`, notes).

**Against our model.** Ours lets the pump give reserve in both directions from any power level, limited by R^{P,max}. That is wider than `chazarra2018`, where the range lies between a minimum and a maximum consumption and the unit must be pumping. With R^{P,max} = 0.3·P^{P,max} and the reserve taken only while pumping, ours would match the variable-speed case; for a fixed-speed pump only upward reserve by stopping is defensible, which does not serve a symmetric product such as FCR-N.
