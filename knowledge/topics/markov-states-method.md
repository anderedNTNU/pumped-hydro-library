# Building the weekly Markov states, and what to test the policy on: precedents we can copy

Written 2026-11-12 (Claude with Anders), after Anders downloaded NVE's LA25 hourly prices and asked for a method from the hydropower literature that the group can reuse and defend. Every statement about a paper below was read in its `paper.txt` on 2026-11-12 unless marked "note". Related: `sddp-setup-vs-bore.md` (Bore's data and clustering), Q-006.

## 1. The data we now have
NVE, *Timespriser for norske prisområder fra LA25* (published 2025-06-20, from Langsiktig kraftmarkedsanalyse 2025):
- one CSV per price area (NO1–NO5) and model year (2030, 2035, 2040, 2050); columns `aar, uke, uketime, pris`;
- **30 weather scenarios, 1991–2020** (`aar` is the weather year), not 29; 52 weeks × 168 hours per year (an ISO model year of 8,736 hours, so every week is complete and there is no week 53);
- price in øre/kWh, real 2023 NOK; also offered in SINTEF price-series format for parallel and serial simulation;
- NVE's own caveats: wind, solar, inflow and temperature-dependent demand vary between weather scenarios, but gas, coal and CO2 prices are the same in all of them, and outages are not modelled, so "the price variation in the simulations often becomes lower than what we observe in the actual market".

NO2, computed from the files (2026-11-12):
| Model year | Mean price | S.d. of weekly mean prices | Mean within-week s.d. of hourly prices | Lag-1 autocorrelation of weekly mean | Hours ≤ 0.5 øre |
|---|---|---|---|---|---|
| 2030 | 71.3 | 23.0 | 14.8 | 0.88 | 2.9 % |
| 2035 | 56.9 | 28.0 | 15.6 | 0.88 | 5.9 % |
| 2040 | 56.0 | 30.0 | 16.7 | 0.86 | 7.3 % |
| 2050 | 59.7 | 30.7 | 21.3 | 0.78 | 7.0 % |

The four model years share the same 30 weather years, so they differ only in the power system. Volatility rises and persistence falls from 2030 to 2050. This is a ready-made, explainable way to vary price behaviour for RQ3 (same weather, different system), alongside or instead of perturbing the chain.

The LA25 report itself is not in the library yet (added to `literature/WANTED.md`); it is needed to cite the data.

## 2. What the literature does
| Study | Data behind the states | How the states and transitions are built | What the finished policy is tested on |
|---|---|---|---|
| `mo2001` (the ProdRisk price model) | Price scenarios from the EMPS model, one per historical weather year, equal probability; "these scenarios also give a direct link between spot price and local inflow" (p. 1) | Per week, N price nodes; a minimum number of scenarios per node "ensures that each transition probability is based [on] a minimum number of" scenarios; transitions first by counting scenario moves, then adjusted "to maintain the conditional expected spot price"; "if the total number of scenarios equals 70, five price nodes and minimum 6 scenarios to define a node usually give a 'good' result" (pp. 3–4) | Strategy simulated two years ahead (p. 5, note) |
| `gjelsvik2010` (and `gjelsvik1999`, note only: its text copy is empty) | S observed weather years of inflow; price scenarios from EMPS | "the price values within each week are grouped in M groups", node value = group mean, transitions from which scenarios go from group to group (p. 40–41, citing Mo et al. 2001); inflow by a normalised vector AR(1), treated as independent of price | "on the forward run we use the 'observed' inflow-price scenarios. This heuristic is intended to take care of any coupling between inflow and price"; "it is most realistic to use observed series of inflow and price, since that helps keep the correct coupling" (pp. 44, 51–52). Warns that this can open gaps between the bounds, because the fitted models are not fully consistent with the observed scenarios |
| `helseth2020scheduling` (SINTEF report on ProdRisk) | Price forecast from EMPS; historical weather years | Price as a discrete Markov chain built from the price forecast (Mo et al. 2001); VAR(1) inflow | "In the SDP/SDDP forward pass ProdRisk uses the historical price and inflow scenarios directly. This preserves the correlation between inflows and market prices" (p. 34) |
| `helseth2016` | 80 price scenarios from EMPS run on 80 historical inflow years | Scenarios sorted per stage into clusters, average cluster prices, 9 nodes; transitions by counting; "we slightly adjusted transition probabilities to ensure that the transition probability matrix was ergodic" (pp. 937, 940) | "a final forward simulation using 1000 sampled scenarios" from the same model (p. 940) |
| `schaffer2022stochastic` (followed by `alic2023optimal`) | Historical or forecast inflow and price | Fit an autoregressive model with serial correlation in inflow and cross-correlation between inflow and price; sample 10 000 scenarios; K-means per week, "each node represents one inflow value and one price value"; transitions = "share of scenarios transitioning between the different nodes from one week to the next" (p. 575) | "1000 scenarios, randomly selected from the originally sampled scenarios" (p. 577) |
| Bore & Brensholm 2026 (thesis; paper `bore2026assessing`) | 44 weather years: DA prices from a fundamental model for the 2030 system, NO2 inflow for the same years scaled to the plant | Per week, joint K-means of price and inflow into 3 clusters; the median series of each cluster is the input; transitions from observed transition frequencies (thesis pp. 28–29; paper p. 3) | The historical inflow trajectories with their DA price simulations, week by week with the cuts, no Markov chain (thesis p. 33) |
| `schuller2024practical`, `gudbjerg2024exploring`, `hagenvik2022comprehensive` (ProdRisk + SHOP simulators) | 30 historical weather scenarios with a price prognosis for a future system built on the same weather scenarios (Schüller: 1986–2015, 2035 system, p. 4) | ProdRisk's price model (as Mo 2001) | The same 30 weather scenarios, simulated week by week (Schüller: 52 × 30 = 1,560 runs) |
| `kleiven2023` | Futures and local inflow | Parametric joint price–inflow model discretised to a lattice | Simulation on the chain itself (in-sample, note) |

**What they share.** One scenario per weather year with equal probability; states per week from grouping or clustering those scenarios; transition probabilities by counting which scenarios move between which states; and the finished policy simulated on scenarios, either the weather-year scenarios themselves (ProdRisk practice, Bore, the simulator studies) or scenarios sampled from the fitted model (Helseth 2016, Schäffer 2022). **None of them holds back weather years for testing.**

## 3. The recipe proposed for us (to copy: Bore & Brensholm 2026, on the foundations of Mo et al. 2001 and Gjelsvik et al. 2010)
Our data have exactly the form these studies use: prices for a future system simulated over historical weather years, and inflow for the same years.

1. **Scenarios.** Each weather year 1991–2020 is one scenario: the hourly NO2 price of the chosen model year and the plant's inflow in that weather year. Equal probability (Mo 2001, p. 1). Pairing by weather year keeps the price–inflow coupling (Mo 2001; Gjelsvik 2010, pp. 51–52).
2. **States per week.** For each week, describe each year by its weekly mean price and weekly inflow, and cluster the 30 points into three clusters with K-means (Bore 2026: joint clustering, K = 3; Schäffer 2022: each node one inflow and one price value). Three states keep about ten years per state, in line with Mo's rule that each transition probability must rest on a minimum number of scenarios (6 per node with 70 scenarios and 5 nodes); five states would leave about six years per state and too few per transition.
3. **What a state contains.** The hourly price series and inflow of the cluster's median year (Bore 2026), so that the within-week price pattern comes from a simulated week and not from an average. Alternative with precedent: cluster mean of the weekly price with a fixed within-week profile (`helseth2015cooptimizing`, `alic2023optimal`).
4. **Transitions.** Probability of going from state i in week t to state j in week t+1 = the share of the years in state i that are in state j the week after (Mo 2001 eq. 1; Gjelsvik 2010; Helseth 2016; Schäffer 2022; Bore 2026). Report the matrices. If a state becomes absorbing or unreachable, adjust minimally and say so, as Helseth 2016 did for ergodicity.
5. **Training.** SDDP samples its forward paths from this chain (Bore 2026; `helseth2016` re-samples scenarios in every iteration). Then the bounds refer to one consistent model; Gjelsvik 2010 (p. 44) notes that using observed scenarios in the forward pass instead can open a gap between the bounds.
6. **Testing.** After convergence, simulate the policy week by week on each of the 30 weather-year scenarios with their own hourly prices and inflow; in each week use the cuts of the state that year belongs to. Report the mean and the spread over the 30 years. This is what ProdRisk does (`helseth2020scheduling` p. 34), what Gjelsvik 2010 argues for, what Bore 2026 does (thesis p. 33), and what the simulator studies do with 30 weather scenarios (`schuller2024practical` p. 4).
7. **What to say about the test.** The test years are the years the chain was built from; the policy has only seen three representative weeks per week, not the 30 actual ones. So it tests how much is lost by the three-state approximation, not performance on unseen weather. The literature above tests the same way. A separate convergence figure comes from simulating on the chain itself (Helseth 2016, Kleiven 2023).

### Choices the precedents leave open (must be stated in ch. 6 or 8)
- **Scaling before clustering.** Price and inflow have different units; Bore does not say what was done. Normalising each by its weekly mean and standard deviation follows the inflow normalisation of Gjelsvik 2010 (p. 36–37) and is the natural choice; state it.
- **Year boundary.** For a horizon longer than a year, the transition from week 52 to week 1 can use consecutive weather years (Mo 2001 uses overlapping sequences 1931–33, 1932–34, …; NVE supplies a serial-simulation format).
- **Hold-out years.** No study in the library holds years back. A leave-some-years-out run can be added as a robustness check, but it has no precedent to cite.

### The alternative if 30 years prove too few
`schaffer2022stochastic` (p. 575), followed by `alic2023optimal`: fit an autoregressive model to the weekly series (serial correlation in inflow, cross-correlation with price), sample 10 000 scenarios, K-means into about five nodes, count transitions, and simulate 1000 of the sampled scenarios. It gives smoother transition matrices, but it adds a statistical model to defend, works on weekly averages (so the hourly pattern needs a separate rule), and tests on synthetic years.

## 4. Consequences for the research questions
- RQ1–2 (adding a pump; its capacity): model year 2030 with the recipe above.
- RQ3 (volatility and persistence): the same recipe on model years 2035, 2040 and 2050 gives chains built from the same weather with more volatile and less persistent prices (table in §1). This is easier to explain than editing the chain by hand, and both can be done. NVE's caveat that simulated price variation is lower than observed belongs in the limitations.

## 5. Evaluation: new forward passes from the same chain, or other data? (added 2026-11-12, Anders' question)
Read in `paper.txt` on 2026-11-12 unless marked "note".

**New forward passes sampled from the same stochastic model (no other data):**
- `helseth2016`: "a final forward simulation using 1000 sampled scenarios" (p. 940); the chain comes from 80 EMPS price scenarios, inflow from an AR(1) model.
- `hjelmeland2019energies`: "the final simulation is carried out with 300 scenarios. We use the same sampled scenarios for all cases. From the final simulation, a confidence interval is computed" (p. 10).
- `hjelmeland2019tste`: "a final simulation of 300 forward scenarios was performed to evaluate the policy by calculating a 95% confidence interval of the lower bound"; the same scenarios for all methods (p. 7).
- `hjelmeland2016case`, `hjelmeland2016combined`: 50 sampled scenarios, then a final run of the same scenarios in a more detailed simulator model.
- `kleiven2023`: both policies simulated on the (dependent) Markov chain (Table 4; note).
- `dimoski2018hydropower`: results "based on the revenues obtained by 50.000 simulated paths through the lattice" (p. 11); also a backtest, below.
- `schaffer2022stochastic` (SDP): 1000 scenarios drawn from the 10 000 that built the chain (p. 577).

**Data other than the sampled paths of the chain:**
- The weather-year scenarios the chain was built from, with their actual series: ProdRisk practice (`gjelsvik2010` pp. 44, 51–52; `helseth2020scheduling` p. 34), Bore & Brensholm 2026 (thesis p. 33), `schuller2024practical`, `gudbjerg2024exploring`.
- Realised history: `dimoski2018hydropower` backtests the policy on "the realized weekly inflows and average area spot prices over the entire simulation horizon" (Sec. 3.8, p. 11); `helseth2024approximating` simulates the detailed system on "30 historical inflow years (1961–1990)" (p. 6); `lohndorf2019` evaluates on the historical inflow record (pp. 658–659, note).
- A separately sampled set from the same model (SDDP without a Markov chain): `helseth2022hydropower`, "a fixed set of 4,000 out of sample inflow scenarios" (p. 7); `helseth2024approximating`, "2000 separately sampled inflow scenarios" (p. 6); `larsen2015evaluation`, strategies "simulated on a different sample than was used to solve the problem" (p. 1).

**Reading.** Simulating new paths from the same chain is the common evaluation in the Markov-chain SDDP papers and is what gives the statistical bound with a confidence interval. It answers how good the policy is if the world behaves like the chain; it cannot show what is lost by reducing the data to a few states. The studies that want that use the underlying weather years or realised history. Truly unseen data (years held back from building the model) appears in none of them; the "out-of-sample" sets of Helseth 2022 and Larsen 2015 are new draws from the same fitted model.

**For us:** do both, since both are cheap once the cuts exist: (a) a few hundred new forward passes from the chain, mean and confidence interval, as Hjelmeland 2019 and Helseth 2016, which is also the convergence check; (b) the 30 weather years with their actual hourly series, as Bore 2026 and ProdRisk practice, for the reported results.

## 6. Is Markov-chain SDDP the same as the hybrid SDP/SDDP of ProdRisk? (added 2026-11-12, Anders' question)
Not identical; the same mechanism applied to different parts of the uncertainty. Read in `paper.txt` on 2026-11-12.
- **Shared mechanism:** one set of cuts (one expected-value function) per discrete Markov state, and the expectation over next week's states taken with the transition probabilities. `gjelsvik2010` (p. 42): "at each discrete price point there is now instead a set of cuts representing the expected future cost function as a function of the continuous state variables". `dowson2020` puts Gjelsvik et al. (1999) and Philpott and de Matos (2012) in the same class, "algorithms for the Markovian policy graph setting". `fullnerRebennack2025` (Sec. 14, hybrid SDP/SDDP): "The idea of addressing this using a Markov chain goes back to Gjelsvik et al."
- **Hybrid SDP/SDDP (Gjelsvik et al.; ProdRisk; `helseth2016`):** only part of the uncertainty is in the chain. `fullnerRebennack2025`: "one part of the uncertainty is treated as in standard SDDP (allowing for cut-sharing between scenarios), while another is treated by enumerating separate expected value functions for each [Markov state] (cuts cannot be shared between Markov states), this is often referred to as a hybrid SDP/SDDP method". The price (objective coefficient) is the chain; the inflow (right-hand side) is an autoregressive time series whose previous value is a state inside the cuts; "it is usually assumed that the uncertainty in the RHS and in the objective are independent of one another".
- **Markov-chain SDDP, MC-SDDP (`lohndorf2019`; Philpott and de Matos 2012; Löhndorf et al. 2013 call it ADDP; ours):** the whole Markovian data process is discretised into the chain ("Markov Chain discretization of the random data process"), so price and inflow sit together in each state and no independence assumption is needed; the reservoir is the only continuous state. Its counterpart TS-SDDP puts all dependence into time-series states.
- **So:** the hybrid is MC-SDDP for the price plus TS-SDDP for the inflow. Ours is pure MC-SDDP. Wording for ch. 6: "Markov-chain SDDP (Löhndorf and Shapiro, 2019), where a separate set of cuts is kept for each Markov state, an idea that goes back to the combined SDP/SDDP method of Gjelsvik et al. (1999)". Do not write that the two are the same method.
- **Correction:** on 2026-11-12 Claude first told Anders the two names denote the same structure; that was too strong and is replaced by the above.

- **Correction 2026-11-13 on Bore 2026:** Bore's chain is joint price–inflow as ours, but Algorithm 1 adds a single cut per week, weighted over all pairs of current and next state by P[curr, next]·π_curr, and adds it to the models of every state. The value of stored water is therefore the same in all states of a week; the chain drives the sampling but not the cuts. Bore is thus not MC-SDDP in the sense of Löhndorf and Shapiro or Philpott and de Matos, who keep a cut set per state. See `sddp-setup-vs-bore.md`.

## 7. Who else has price and inflow in the Markov chain? (added 2026-11-13, Anders' question)
Read in `paper.txt` on 2026-11-13 unless marked "note".

| Study | What is in the chain | States per stage | Solution method | Value function per state? |
|---|---|---|---|---|
| `kleiven2023` | price and inflow as pairs: "a Markov chain with five price and inflow pair nodes" (App. F) | 5 | SDDP on the chain | yes |
| `dimoski2018hydropower` | "all nodes of the price and inflow lattice", state S = {P, Y} | 100 | ADDP of Löhndorf et al. (2013), in QUASAR | yes |
| `grini2023` | each state "a combination of price and inflow" (p. 18, note) | 125 | SDDP | yes |
| `lohndorf2013` | weather, inflow and gas price in the chain; hourly prices follow from the state by regression | 30 × gas-price lattice | ADDP | yes |
| `schaffer2022stochastic` | "each node represents one inflow value and one price value" (p. 575) | not fixed in the method; K-means | SDP (reservoir on a grid) | yes, a table per node |
| `alic2023optimal` | joint inflow and price, following Schäffer | 5 | SDP | yes |
| `helseth2017iet` | "uncertainties in inflow and both energy and reserve capacity prices are considered through a discrete Markov chain" (abstract) | 5 inflow × 15 price | SDP | yes |
| `perezdiaz2020medium` | three separate chains: inflow, energy price, reserve curve | 5 inflow states | SDP | yes |
| Bore & Brensholm 2026 | joint DA price and inflow | 3 | SDDP | no, one cut per week (see `sddp-setup-vs-bore.md`) |

Not in this group: `helseth2016`, `gjelsvik2010`, `mo2001` and ProdRisk (price only in the chain, inflow as a time series); `hjelmeland2019energies` (both as a VAR(1) time series); `lohndorf2019` and `philpott2012` (inflow only).

**Closest to our algorithm** (joint price–inflow chain, SDDP, value function per node): `kleiven2023`, then `dimoski2018hydropower`, `grini2023` and `lohndorf2013`. All four come from the same NTNU and Löhndorf line of work and build the chain by fitting a continuous model and discretising it, not by clustering weather years.

## 8. Kleiven et al. (2023): the same algorithm as ours? (added 2026-11-13, Anders' question)
Read in `paper.txt` on 2026-11-13 (Sec. 3 pp. 12–13, Sec. 5.3, App. F with Algorithm 1).

**The algorithm is the same scheme as in our ch. 6.**
- States: the water in the reservoir (endogenous) and a price–inflow pair (exogenous). "We use a Markov chain with five price and inflow pair nodes"; 104 weekly stages (App. F).
- They name the method: "We implement the Markov chain SDDP in Julia using the SDDP package [Dowson and Kapelevich] and the Gurobi solver" (Sec. 5.3), and choose MC-SDDP over TS-SDDP because price times a decision in the objective would break concavity (p. 12–13, citing Löhndorf and Shapiro).
- Forward pass: starts from a given initial state, samples the uncertainty stage by stage, solves each stage problem and stores the reservoir state (p. 13).
- Backward pass: from T−1 backwards; at each stored state the next stage is solved "for all ω_{t+1}", and the values and subgradients are averaged into one cut, eqs. (13)–(14); "we use average cuts".
- Stopping: when new cuts no longer reduce the upper bound, at an iteration limit, or by a statistical bounds criterion (p. 13). The numbers of iterations and forward paths are not stated.
- Results from simulating 1000 scenarios on the chain; 2 % annual discount rate; two years solved and the end of the horizon read with caution (Sec. 5.3).
- The paper does not write out that each Markov node has its own cuts. That follows from MC-SDDP as defined by Löhndorf and Shapiro and from the Markovian policy graph of the SDDP package (`dowson2020`), where every node has its own value function.

**The chain is built differently from the recipe proposed for us (§3).**
- Input: 50,000 weekly Monte Carlo paths from a fitted continuous price–inflow model, not weather years.
- "A joint clustering on price and inflow pairs created a Markov chain that did not capture the variance, mean, and covariance of the underlying stochastic model. Instead, we only cluster on prices and map the corresponding inflows to each price cluster" (App. F). K-means on standardised prices; transitions by counting.
- The inflow of a price cluster is the mean of its inflows plus a scaled sample around the mean, so that mean, variance and covariance with price are kept (Algorithm 1, lines 15–21).
- "Simulations verify that it is representative of the continuous price and inflow processes."

**For us.** The warning about joint clustering applies to our proposed recipe (joint K-means on price and inflow, as Bore): check that the three states per week reproduce the mean and variance of price and inflow and their covariance, which is the TODO already at the end of ch. 6. If they do not, Kleiven's alternative has a source: cluster on price only and attach the inflows of the years in each price cluster.

### Does Kleiven get a cut for each Markov state each week? (added 2026-11-13)
- **In the paper:** not shown. The cut is written θ_t ≤ α_t^k + β_t^k s_t (eq. 12), with a stage index and an iteration index only, although assumption A1 treats the value function "for a fixed ω_t" (pp. 12–13).
- **In the implementation they name:** yes. They use the SDDP package for Julia with a Markov chain (Sec. 5.3). In that package a Markovian graph has one node per pair of stage and Markov state (SDDP.jl API reference, `MarkovianGraph`, read at sddp.dev on 2026-11-13), and `dowson2020` associates a subproblem and a cost-to-go function with each node. So each of the five states of a week has its own cuts.
- **How many cuts per iteration:** the package's training option `refine_at_similar_nodes` (on by default) adds the cut found at one node to the other nodes with the same children, each with its own transition probabilities. With the default, every state of a week on the sampled path gets a cut in each iteration, which is what our Algorithm 1 does ("one cut for every state m"). The paper does not say which settings were used.
- **For ch. 6:** cite `philpott2012` and `dowson2020` for cuts per Markov state; `kleiven2023` supports the use of a joint price–inflow chain with this method, not the cut indexing itself.

### Kleiven 2023 vs ours, sorted by how certain it is (added 2026-11-13, re-read for Anders)
**Stated in the paper in words (certain):**
1. A fixed number of price–inflow states per week: five nodes, 104 weekly stages (App. F).
2. Forward pass: start in week 1 from a given reservoir state, sample the uncertainty, solve the week, save the resulting reservoir state, continue to the last week; the pass ends with a list of reservoir states, one per week (p. 13).
3. Backward pass: from the second-to-last week backwards through that list; with the saved state fixed, the next week is solved for all its outcomes, and the values and gradients are averaged into a cut that is used in the next forward pass (p. 13, eqs. 13–14).
4. The chain's transition probabilities are counted from scenarios moving between clusters (App. F, Algorithm 1), and the method is run with the SDDP package for Julia (Sec. 5.3).

**Follows from the package, not written in the paper:**
- The forward pass draws the next state with the chain's transition probabilities (the package's default forward sampling uses the probabilities of the graph as defined; SDDP.jl API reference, `InSampleMonteCarlo`, read 2026-11-13).
- Cuts are kept per week and state, and by default added to all states of a visited week (see above).

**Not stated anywhere:** number of forward paths per iteration, number of iterations, package settings.

### Kleiven 2023: is "one cut per Markov state per week" said in the paper? (added 2026-11-13, third check)
- **No sentence says it.** Searched the text for per-node, per-state, per-cluster and conditional wording: nothing.
- **The model definition implies it.** Eqs. (2)–(3), p. 10–11: the value function is V_t(s_{t−1}, ω_t) and the continuation function is Θ_{t+1}(s_t, ω_t), the expectation of V_{t+1} given ω_t. The function that the cuts approximate therefore has the current price–inflow state as an argument, so it is a different function for each of the five states.
- **The cut formula drops the index.** Eq. (12) writes θ_t ≤ α_t^k + β_t^k s_t with week and iteration only, and eqs. (13)–(14) write a plain expectation.
- **The software does it** (see above).
- **How to cite:** Kleiven for the state-dependent continuation function (eq. 3); `philpott2012` p. 7 for the explicit statement that a set of cuts is recorded for each state of the Markov chain.

