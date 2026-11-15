# Water values in our model, and nested Benders decomposition against SDDP

Written 2026-11-15 at wrap-up, from Anders' questions on 2026-11-13 and 2026-11-14. Sources read in `paper.txt`; statements marked "our reasoning" follow from the ch. 6 formulation and are not taken from a paper.

## 1. Water values
- **Definition.** The water value for week s and Markov state m is the slope of the binding cut of that week and state: the expected marginal value of water stored at the **end** of the week, in EUR/Mm3 (ch. 6, `eq:cut_coefficients`; per MWh by `eq:water_value_energy`). `helseth2016` p. 941: the expected water values at a stage and state "can be found as the coefficients" of the binding cut for that stage and state.
- **Built from next week.** The cuts of week s come from solving week s+1 in every state at a trial volume and weighting the values and duals with the transition probabilities of state m (ch. 6; `philpott2012` p. 7).
- **Not a constant.** Which cut binds depends on the end-of-week volume, so the water value is a decreasing step function of that volume. The weekly problem chooses generation, pumping and the end volume together. "Generate above the water value and pump below it" is true only at the optimum, with the water value read at the end volume the problem itself chose (our reasoning).
- **Week 15.** A water value "for week 15" is the value of one more unit of water at the end of week 15, which is the start of week 16 (ch. 6 wording: "at the end of the week").
- **What the week-1 problem gives.** Its objective is the upper bound U_n on the expected discounted profit over the whole horizon: this week's profit plus the cut approximation of the rest. It is not the profit earned. The earned profit is estimated by simulating the policy on forward paths, which gives the lower bound and its confidence interval (ch. 6, `eq:training_estimate`; `helseth2016` pp. 939–940).
- **Across weeks.** At the same volume the value function of an earlier week is at least the discounted expectation of the next week's: F_{s,m}(V) ≥ β·Σ π·F_{s+1,m'}(V). The plant can idle for a week at zero profit, and more water is never worse when spillage is free (our reasoning). The value function is therefore large in week 1 and falls towards the end of the horizon, where it is zero by `eq:terminal_value`.

## 2. Nested Benders decomposition (NBD) against SDDP
Source: `fullnerRebennack2025`, Sec. 5.2 (journal pp. 442–444) and Sec. 14.5 (p. 500). Journal page = PDF page + 414.

| | Nested Benders decomposition | SDDP |
|---|---|---|
| Uncertainty | a full scenario tree; every node has its own history | stagewise-independent outcomes, or a Markov chain |
| Forward pass | solves every node of the tree | solves the nodes along a few sampled paths |
| Value functions and cuts | one per node; a cut helps only the node it was built for | one per stage (or per stage and Markov state); a cut is shared by all scenarios that pass the stage |
| Bounds | valid lower and upper bounds in every iteration, so the stopping test is deterministic (p. 443) | one bound is a sample mean, so convergence is judged with a confidence interval |
| Size that can be solved | "four or five stages at maximum" and some hundred to a few thousand scenarios (p. 443) | many stages, for example 52 or 104 weeks |

- SDDP "can be interpreted as a sampling variant" of NBD that lowers the effort per iteration but relies on stagewise independence (p. 443). It does not remove the exponential growth of the worst-case cost with the number of stages (p. 444).
- In a general scenario tree, sampling paths does not help, because each cut would improve one node only (p. 443).
- Other sources say the same in one sentence: `helseth2018optimal` p. 2 and `helseth2026considering` p. 12 (SDDP as a sampling-based variant of multi-stage Benders decomposition); `vanackooij2020conditional` p. 174 (nested decomposition uses the whole tree, SDDP samples).
- **Where our model sits.** Price and inflow are not independent from week to week. The Markov chain restores what SDDP needs: given the state, the next week depends on nothing else, so one cut set per week and state is enough. With three states that is three cut sets per week instead of one per tree node (3^51 nodes in the last of 52 weeks; our arithmetic).
- A hybrid of NBD and SDDP is described as closely related to the hybrid SDP/SDDP method (Sec. 14.5, p. 500).
