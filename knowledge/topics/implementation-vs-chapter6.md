# The implemented model against chapter 6

**Compared 2026-11-17 (Claude with Anders).** Anders sent the group's description of the Python implementation: *MarkovSDDP4 Weekly operating model and solution algorithm*, dated 16 November 2026 (17 pages; notebook `Models/MarkovSDDP4/markov_sddp.ipynb` with `duge.yaml`, in the folder `PreKMeansModelAndResults5Years`). It was compared with `../pumped-hydro-thesis/Sections/06_mathematical_model.tex` and `08_case_study.tex` as pulled from Overleaf the same day (chapter 6 last changed 2026-11-10, commit b767ad1). The equation numbers of the implementation document, (2)–(26), follow the order of the equations in chapter 6 one to one, so both describe the same model text. Only the document was read, not the code.

## 1. Result in short
- **The weekly operating model is the same**, equation for equation. The implementation is the special case with one reserve product (FCR-N, symmetric, downward price zero).
- **The recursion, the cuts and the starting bounds are the same**, apart from where the discount factor is placed.
- **Five things differ:** the end of the horizon, the training loop and stopping rule, how the Markov states are made, the length of the horizon, and the evaluation of the finished policy.

## 2. The same
| Element | Chapter 6 | Implementation |
|---|---|---|
| Energy constant κ = 2.725 H | `eq:energy_constant` | (2) |
| Weekly profit: net day-ahead revenue plus capacity payments | `eq:objective_energy`, `eq:weekly_objective` | (3), (4) |
| Unit limits with reserve headroom, four inequalities | `eq:unit` | (5a)–(5d) |
| Reserve limit per unit and direction | `eq:unit_reserve_limits` | (6a)–(6b) |
| Reservoir limits; upward water margin for one full period, with the pump term | `eq:reservoir` | (7a)–(7b) |
| Initial volume; water balance; uniform inflow shares | `eq:initial_state`, `eq:water_balance`, `eq:uniform_inflow` | (8), (9), (10) |
| Reserve allocation between the units; product limits; symmetry | `eq:commitment`, `eq:product_limits` | (11a)–(12c) |
| Reservoir volume as the only state between weeks | `eq:weekly_link` | (14) |
| Recursion and conditional expectation over the next state | `eq:bellman`, `eq:expected_future` | (15), (16) |
| One cut set per week and current state; one cut per state and trial volume holding the expectation; dual of the initial-volume constraint as slope | `eq:cuts`, `eq:cut_coefficients` | (19c), (21) |
| Weekly bound B_s and bound on future profit | `eq:weekly_bound`, `eq:initial_bound_value` | (23), (24a) |
| Capacity prices the same in all states; state observed before the week; hourly commitments; no activation; both units may run in the same hour | assumption tables | Section 7 |

The implementation reads an hourly inflow from the scenario file instead of spreading a weekly total, but the current data are uniform within the week, so the result is the same.

## 3. Different
| # | Element | Chapter 6 (Overleaf) | Implementation | Already recorded |
|---|---|---|---|---|
| 1 | End of the horizon | Last week maximises its own profit (`eq:final_week`); value after week N is zero (`eq:terminal_value`); no end-volume requirement; the assumption table says the same | Last week has a soft minimum end volume of 915.69 Mm³; the shortfall d is a new variable, penalised at 1,000,000 EUR/Mm³ in the objective, (17a)–(17b). Two new parameters, one new variable, one new constraint | Q-007 (1) |
| 2 | Training loop and stopping | K forward paths per iteration; mean and standard error of their profits (`eq:training_estimate`); stop when the upper bound lies inside the confidence interval (`eq:stopping_rule`, after `helseth2016`) or at N^max; then a final simulation on a larger set of paths | One forward path per iteration, started by one path with empty cuts; stop when the upper bound changes by less than 25,000 EUR three times in a row, or after 6 hours or 300 iterations; no standard error (set to 0 as a placeholder); one final path | Q-007 (2) |
| 3 | Markov states | K-means per calendar week on mean price, price standard deviation and inflow; the sample nearest the centre represents the state; transitions counted per week (`eq:transition`); 4, 8 or 12 states as candidates; a validation set and held-out test paths | Three prescribed states (low, medium, high): the 2011–2015 weather-year profiles with NVE 2030 NO2 prices, with the price multiplied by 0.8, 1.0 and 1.2 and the inflow by 1.1, 1.0 and 0.9 in the same order; one prescribed transition matrix used in every week; the first state is medium; no clustering and no estimation | Q-006 |
| 4 | Horizon | S = 104, S^ext = 52, N = 156 (`08_case_study.tex`) | S = 104, S^ext = 156, N = 260 | new |
| 5 | Evaluation of the policy | Evaluation on unseen paths; profit of the reported weeks plus the continuation value of the remaining water (`eq:oos_profit`–`eq:oos`); four benchmarks (perfect foresight, weekly cyclic, stagewise-independent, energy-only); configuration contrasts; five validation checks | Not in this notebook: one final path with its hourly schedule; undiscounted revenue for the first 104 weeks and for all 260, without a continuation value. The document says further evaluation is in separate notebooks, which it does not describe | new |

## 4. Same content, different notation
- **Where the discount factor sits.** Chapter 6 writes the objective as Π + β·α with undiscounted cut coefficients and α ≤ M̄_{s+1}. The code writes Π + α, puts β inside the cut level and slope, (21a)–(21b), and uses α ≤ β·M̄_{s+1}. The two are equivalent: the code's α is β times that of chapter 6. A consequence: the cut slope stored by the code is the water value discounted by one week, so a water value read from the code is β times the λ_ℓ of chapter 6 (0.99941 with the current settings).
- **Path profit.** Chapter 6 defines J_k as the discounted weekly profits. The code subtracts the discounted end penalty as well, (25).
- **Reserve products.** Chapter 6 is written for a set of products; the code has FCR-N only. The literature table of the group's draft says "DA, mFRR, aFRR" (Q-011).
- **Values not yet in the thesis:** the annual discount factor 0.97 and the plant data stand only in the configuration (`implementation-parameters.md`).

## 5. What follows
Before results are reported, the text and the code must say the same on the five points of Section 3. The earlier recommendations stand (`implementation-parameters.md` Sections 3 and 5): keep an end target and describe it in chapter 6; choose one stopping rule and add a final simulation on many paths whichever is chosen. Points 3 and 5 depend on Q-006 and on what the other notebooks do. Chapter 6 is not changed until the group decides (Q-010).
