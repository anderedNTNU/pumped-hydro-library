# Stopping rules, end of horizon and artificial water in the SDDP sources

**Checked 2026-11-26 (Claude with Anders).** Anders asked what the SDDP articles do about three things: when they stop training, whether they solve more years than they report in order to escape the end of the horizon, and whether they use artificial water. All 56 SDDP sources of `sddp-model-comparison.md` Section 2 were searched in the PDF text for the three topics, and the passages were read. Page numbers are printed pages where the journal's page range is known, otherwise "PDF p.". For `gjelsvik1999` the text could not be extracted. Nine sources are method texts, surveys or toolchain descriptions without a case of their own.

## 1. Result in short
- **Stopping.** Three kinds of rule are in use. The confidence-interval test of Pereira and Pinto is written down in many papers, but it is the rule that actually stops the run in only five. About twenty run a fixed number of iterations or stop at a cap. About eight stop when the bound, the gap or the cuts no longer move. The review of `fullnerRebennack2025` (p. 450) says the same: in practice SDDP is commonly stopped after a fixed number of iterations, a fixed time, or when the bound has stalled, and none of these guarantees an optimal policy.
- **Extra years.** Solving a longer horizon than the one reported is an established practice. `fullnerRebennack2025` (pp. 458–459) calls adding 60 more monthly stages to a 60-stage problem a common practice. The Norwegian owner studies mostly do something else: they put end-value cuts at the end, taken from a longer run or from a long-term model, and several combine this with a horizon that is longer than the period they report.
- **Artificial water.** Very common, but for another purpose. It is a penalised slack in the water balance of every week that keeps each weekly problem feasible. It is not how these papers handle the end of the horizon.
- **A penalised end-volume target**, which is what our implementation has, is used by `lohndorf2013` (pumped storage), `seifert2025` (battery) and Bore's master thesis.
- **Both.** Yes: an end condition and artificial water appear together in several sources, because they solve different problems.

## 2. Stopping rules
**A. Confidence-interval test is the operative rule** (stop when the bound from the first stage lies inside the confidence interval of the simulated value)
| Source | What it says |
|---|---|
| `pereira1991` | proposes the test with a 95 % interval (p. 368); the case converges in five iterations with 50 inflow sequences (p. 373) |
| `tilmant2008` | same test (PDF p. 8); converges after 11 iterations with 20 sequences (PDF p. 11) |
| `helseth2015efficient` | lower bound within the 95 % interval of the upper bound (p. 14291) |
| `li2022solving` | upper bound within the 95 % interval of the lower bound; 31 iterations (PDF p. 11) |
| `papavasiliou2018application` | the Pereira–Pinto test together with a requirement of a small standard deviation of the mean cost (PDF p. 4) |

**The test is stated, but something else stops the run:** `helseth2016` (p. 939, cap p. 940), `helseth2018optimal` (p. 6994; found sensitive to the case and the sampling settings, p. 6996), `helseth2022hydropower` (PDF pp. 4, 7), `hjelmeland2019tste` (p. 485), `helseth2025` (PDF pp. 9, 37), `helseth2026considering` (PDF p. 15), `bueno2023impact` (PDF p. 8), `dematos2015improving` (PDF p. 6), `philpott2012` (PDF p. 5).
**Criticism of the test:** `shapiro2011` (pp. 65, 67), `fullnerRebennack2025` (p. 449: a larger sample variance or a smaller sample makes it stop earlier), `philpott2012` (PDF p. 5), `dematos2015improving` (PDF p. 6: a fixed number of iterations was more reliable).

**B. Fixed number of iterations, or a cap**
| Source | Iterations | Forward paths per iteration |
|---|---|---|
| `gjelsvik2010` | typically 50–100 (p. 52); convergence judged by the largest change in a reservoir trajectory, with a minimum and a maximum number (p. 44) | 50–70 |
| `helseth2013` | at most 60 (p. 1433) | 54 weather scenarios |
| `helseth2015cooptimizing` | at most 100 (PDF p. 5) | 80 |
| `helseth2016` | at most 60; final simulation on 1000 scenarios (p. 940) | 200 |
| `hjelmeland2016combined` | 15 (PDF p. 4) | – |
| `hjelmeland2019tste`, `hjelmeland2019energies` | 50 (p. 488; PDF p. 11) | 2 and 3 |
| `helseth2020nonconvex` | at most 30 (PDF p. 5) | – |
| `helseth2024approximating` | at most 80 (PDF p. 5) | 70 |
| `larsen2015evaluation` | 15, enough for the upper bound to stabilise (PDF p. 5) | 100 |
| `gudbjerg2024exploring` (ProdRisk) | 50 (PDF p. 35) | – |
| `grini2023` | 2000; the upper bound moved 0.2 % after 200 and 0.1 % after 500 (PDF pp. 19–20) | – |
| `philpott2012` | 4000, one case 16,000 (PDF p. 19) | 1 |
| `dematos2015improving` | fixed number (PDF p. 6) | 1 or more |
| `lohndorf2019` | 1000 (p. 655) | 1 |
| `shapiro2020` | 300, each with 10 parallel passes (PDF pp. 14–15) | 10 |
| `bueno2023impact` | 400 (PDF p. 22) | 1 against 10 compared |
| `hole2025capacity` | 1000 (PDF p. 16) | – |
| `chancelier2026optimal`, `downward2020stochastic`, `dowson2020` | 1000, 2000, 1000 (PDF pp. 19, 12, 24) | – |
| Bore's master thesis | 50, no convergence test (`sddp-setup-vs-bore.md`) | 1 |

**C. The bound, or the solution, has stopped moving**
| Source | Rule |
|---|---|
| `helseth2018optimal` | stabilisation of the upper bound (p. 6996); no threshold given |
| `helseth2022hydropower` | stabilisation of the upper bound (PDF p. 7); no threshold given |
| `helseth2025` | visual inspection of the bound and the gap after a predefined number of iterations (PDF p. 37) |
| `seifert2025` | upper bound improves by less than 0.1 over the last 3000 iterations, after 5000 initial ones; otherwise 18,000 (PDF p. 14) |
| `bore2026` (conference paper) | change in the mean lower bound below a threshold and two penalty-free solutions in a row; 10–31 iterations (PDF pp. 3–4) |
| `abgottspon2015hydro`, `abgottspon2016multihorizon` | a gap threshold in the algorithm; in practice a fixed number of iterations or until the gap no longer improves (PDF p. 56; PDF pp. 8–9) |
| `vanackooij2020conditional` | backward and forward values within 0.1 % (pp. 180, 195) |
| `lohndorf2013` | a new cut is kept only if it improves the approximation by more than ε (PDF p. 16); 25 iterations in the test (PDF p. 26) |

**Not stated:** `kleiven2023` lists the three kinds without saying which was used (PDF p. 11); nothing found in `dimoski2018hydropower`, `hjelmeland2016case`, `hjelmeland2018impact`, `gjelsvik2005considering`, `hagenvik2022comprehensive`, `schuller2024practical`, `philpott2023using`, `garcia2025longterm`.

## 3. End of the horizon
| Approach | Sources |
|---|---|
| **End-value function or end-value cuts**, from a long-term model or from an earlier, longer run | `gjelsvik2005considering` (EOPS, PDF p. 4); `gjelsvik2010` (aggregated SDP water values, p. 54); `helseth2013` (p. 1427); `helseth2015cooptimizing` (PDF pp. 5–6); `helseth2016` (cuts from a few initial runs, p. 940); `helseth2018optimal` (cuts from runs with a four-year horizon, p. 6995); `helseth2020nonconvex` (PDF p. 4); `helseth2022hydropower` (PDF p. 2); `helseth2015efficient` (p. 14288); `helseth2024approximating` (PDF p. 2); `helseth2025` (PDF p. 10); `helseth2026considering` (PDF p. 15); `hjelmeland2016case` (p. 130); `grini2023` (value of the remaining water per reservoir, PDF p. 7); `tilmant2008` (PDF p. 3); `philpott2012` (zero or a convex function, PDF p. 4) |
| **A longer horizon than the one reported** | `gjelsvik2005considering`: three years, results from the second, ideally five with results from year three or four (PDF p. 4). `hjelmeland2016case`: two years, results for the first 78 weeks (p. 127). `kleiven2023`: two years with zero end value, only the first year reported (PDF pp. 18–19). `helseth2025`: 156 weeks, the first two years simulated (PDF pp. 39, 42). `bueno2023impact`: 24 months solved, 12 analysed (PDF pp. 8, 22). `shapiro2020`: 60 stages added to 60; the effect remains when the discount factor is near one (PDF p. 14). `lohndorf2019`: 120 months, an intermediate 12 months reported (pp. 655, 658–659). `dematos2015improving`: 120 stages (PDF p. 17). `fullnerRebennack2025`: adding 60 stages is common practice, with only the first half implemented (pp. 458–459) |
| **Horizon set by the reservoir** | ProdRisk is normally set up for 2–5 years, depending on the regulation capability (`helseth2020scheduling` p. 32); 104–208 weeks depending on the largest reservoir (`hagenvik2022comprehensive`, `schuller2024practical`, PDF p. 2); 208 weeks in `gudbjerg2024exploring` (PDF p. 35) |
| **Infinite horizon** (the last week is linked to the first with a discount factor) | `philpott2023using` (PDF p. 4) and `hole2025capacity` (PDF pp. 3, 6), discount factor 0.9; `dowson2020` (PDF pp. 11, 24); `shapiro2020` (periodical SDDP) |
| **End volume fixed** | `bore2026`: end volume equal to start volume (PDF p. 4, eq. 4); `li2022solving`: end volumes as a boundary condition (PDF p. 11) |
| **End volume with a penalty** | `lohndorf2013`: the value function of the last stage penalises any content below the initial levels, so that the reservoirs are not emptied (PDF p. 26). `seifert2025`: start and end level with a penalised slack, and no bidding on the last day (PDF pp. 8, 12–13). Bore's master thesis: emergency water in the last week at 10 mEUR/GWh, which makes the end condition feasible (`sddp-setup-vs-bore.md`). `dowson2020` on an earlier farm model: a penalty for ending below the start, replaced by an infinite horizon (PDF p. 23) |
| **Nothing** | `dimoski2018hydropower`: no end restriction, and the authors note that emptying the reservoir would be a poor decision in reality (PDF p. 12) |

`gjelsvik2010` (pp. 53–54) states the problem: without a good final value function the strategy may be poor for the last year or so of the study period, and the results from that period may mislead. `helseth2016` (p. 940) and `helseth2018optimal` (p. 6995) name a longer horizon as the alternative to end-value cuts and choose the cuts to save computation time.

## 4. Artificial water
A slack in the water balance or on the reservoir limit, with a high cost in the objective, so that every weekly problem has a solution (relatively complete recourse):
`helseth2015cooptimizing` (PDF p. 4); `helseth2016` (artificial water supply w_h at 10^6 EUR/Mm³, pp. 934, 939); `hjelmeland2016combined` ("tank water", needed because the inflow model can give negative inflow, PDF p. 2); `hjelmeland2019tste` (pp. 482, 489); `helseth2022hydropower` (slack on the lower reservoir bound, PDF p. 3); `helseth2015efficient` (p. 14289); `helseth2025` (PDF p. 9); `bore2026` (emergency water, PDF pp. 1, 4); `larsen2015evaluation` (PDF p. 5); `dimoski2018hydropower` (PDF p. 8); `seifert2025` (PDF p. 13); `schuller2024practical` (in the short-term model, PDF p. 4); `philpott2012` (soft constraints, since hard ones break relatively complete recourse, PDF p. 25); `hole2025capacity` (PDF p. 19).

Warnings: the penalty is hard to choose and may distort the value functions (`fullnerRebennack2025` pp. 511–512); penalties on slack variables strongly affect the water values (`bueno2023impact` PDF p. 2); penalty variables add an inconsistency between the forward and backward runs and may slow convergence (`gjelsvik2010` p. 51).

Our weekly model needs no such slack: idling, selling no reserves and spilling is always feasible (ch. 6, "Initial Bounds and Feasibility").

## 5. Against our implementation (`implementation-vs-chapter6.md`)
| Our implementation | Nearest sources |
|---|---|
| 104 reported weeks plus 156 extension weeks | the practice of `fullnerRebennack2025` pp. 458–459, `shapiro2020`, `bueno2023impact`, `gjelsvik2005considering`, `kleiven2023`, `helseth2025`. No source solves five years to report two, but ProdRisk uses 2–5 years depending on the reservoir, and ours holds 2.9 years of inflow |
| Soft end-volume target with a penalty | `lohndorf2013`, `seifert2025`, Bore's master thesis. No Norwegian owner study does this; they use end-value cuts |
| Extension and end target together | each has precedents, the pair is not found in one source. With a three-year extension the target should matter little for the reported weeks; this can be shown by running with zero end value instead |
| Stop when the upper bound changes by less than 25,000 EUR three times in a row; one forward path | bound stabilisation in `helseth2018optimal`, `helseth2022hydropower` (no threshold given) and `seifert2025` (a far longer window); one path per iteration in `philpott2012`, `lohndorf2019`, `bueno2023impact`, Bore |
| One final path | every source that reports results simulates many paths afterwards: 300 (`hjelmeland2019tste`), 1000 (`helseth2016`, `lohndorf2013`), 4000 (`helseth2022hydropower`), 10,000 (`seifert2025`, `chancelier2026optimal`) |

## 6. Where the end condition sits, and whether an extension plus an end requirement is common (Anders' follow-up, 2026-11-26)
- **Where the end-value cuts sit.** In the Helseth studies the training and the simulation cover the same horizon, and the cuts are placed after its last week. The backward recursion starts from a predefined final value function at the end of the planning horizon (`helseth2016` p. 939), the scheduling horizon is two years (p. 939), and the final simulation of 1000 scenarios covers the same two years, with profits adjusted for the difference between final and initial reservoir levels (p. 940). The longer run is a separate, earlier run that only produces the end cuts: "a few initial model runs" (`helseth2016` p. 940), with a four-year horizon in `helseth2018optimal` (p. 6995).
- **Training longer than what is reported, with an end condition as well:** `helseth2025` (156 weeks with a predefined final value function, PDF pp. 10, 39; the first two years simulated, PDF p. 42); `gjelsvik2005considering` (end valuation from EOPS, a three-year horizon with results from the second year, ideally five years with results from year three or four, PDF p. 4); the advice of `gjelsvik2010` p. 54 (a final value function, and a study period that is long enough).
- **So:** an extension together with an end condition is SINTEF practice, but the end condition there is a value function (cuts), not a volume requirement. A volume requirement with a penalty is found without an extension (`lohndorf2013`, `seifert2025`, Bore). No source combines an extension with a penalised volume requirement.
- **Our end requirement is a value function.** A penalty C on the shortfall below V^final,min equals the terminal value function Φ(V) = −C·max(0, V^final,min − V): one cut with slope C below the target and zero above (our observation). `lohndorf2013` describes its final-stage value function in these terms (PDF p. 26).
- **In our runs** the requirement sits in week 260, the last week of the horizon that is both trained and simulated. Nothing is imposed at week 104; the value of the water left after week 104 is in the cuts of week 104 (ch. 6, `eq:oos_tail`). `helseth2016` instead adjusts the profits for the difference between final and initial reservoir levels (p. 940).
- **Term.** In the sources artificial water is a slack in the water balance of every week (`helseth2016` pp. 934, 939). Our shortfall variable relaxes only the end target and adds no water (implementation document, Section 9.3). "Terminal shortfall" is the more precise name.

## 7. A set-up that can be attributed to named sources (proposal to the group, 2026-11-26)
Anders asked what we can do so that the report can say "as in A, B, C and D". This is a proposal, not a decision (Q-007). No single source has the whole package; each choice is attributed on its own.

| Choice | Do this | Same as | What must hold in the code |
|---|---|---|---|
| Horizon | solve more weeks than are reported, and report only the first 104 | `kleiven2023` (two years solved, the first reported, PDF pp. 18–19); `shapiro2020` (60 + 60 months, PDF p. 14); `bueno2023impact` (24 months solved, 12 analysed, PDF pp. 8, 22); `lohndorf2019` (120 months, an intermediate 12 reported, pp. 655, 658–659); called common practice by `fullnerRebennack2025` (pp. 458–459) | already true. The sources double the horizon; ours is 104 + 156. The longer extension is argued from the reservoir: it holds 2.9 years of inflow, and ProdRisk is set up for 2–5 years depending on the regulation capability (`helseth2020scheduling` p. 32) |
| End of the extension, alternative A | no value on water after the last week | `kleiven2023` (PDF p. 23, eq. 40), `shapiro2020`, `bueno2023impact` | remove the end target and its penalty. This is chapter 6 as it stands. Shapiro and Ding warn that the effect can remain when the discount factor is close to one (PDF p. 14), and ours is 0.97 a year, so the test with a longer extension is needed |
| End of the extension, alternative B | a final value function that penalises ending below the start volume | `lohndorf2013` (PDF p. 26), `seifert2025` (PDF pp. 12–13); `bore2026` with a hard requirement (PDF p. 4). A final value function together with a long horizon: `gjelsvik2010` (p. 54), `helseth2025` (PDF pp. 10, 39, 42) | set the end target equal to the start volume (now 915.69 against 868.158 Mm³). Chapter 6 must then be changed |
| Training | one forward path per iteration, a fixed number of iterations, and a report of how much the bound moved at the end | `philpott2012` (PDF pp. 5, 19), `lohndorf2019` (p. 655), `grini2023` (PDF pp. 19–20) | drop the early stop. Or keep it and describe it as stabilisation of the upper bound (`helseth2018optimal` p. 6996, `helseth2022hydropower` PDF p. 7, `shapiro2011` p. 71), with the threshold stated as our own |
| Evaluation | simulate the trained policy on 1000 sampled paths | `helseth2016` (p. 940), `lohndorf2013` (PDF p. 26), `kleiven2023` (PDF pp. 20–21) | add a simulation loop. The first 104 weeks are enough (`helseth2025` simulates the first two of three years, PDF p. 42) |
| Artificial water | none | – | every weekly problem is feasible without it |

- **Choosing between A and B.** Run A with the present extension and with a longer one. If the water values and the schedule of weeks 1–104 do not move, A is enough. If they move, the end still reaches the reported weeks, and B is the better choice.
- **Not in `references.bib`:** `larsen2015evaluation`, `dematos2015improving`, `gjelsvik2005considering`. `bueno2023impact` is an arXiv report and `seifert2025` a preprint.
- **Chapter 6:** the stopping section follows the confidence-interval rule of `helseth2016` with K paths (D-024). The training row above would replace it, which is a decision for the group.

## 8. Recommended end value after week 260 (Anders' question, 2026-11-26)
Question: how should the value of water after five years be set when two years are reported? Recommendation to the group, not a decision (Q-007).

**Take the end value from the model itself: the cuts of the same week one year earlier.**
1. Run 1 with no value on water after week 260 (chapter 6 as it stands).
2. Run 2 with the cuts of week 208 from run 1 as end-value cuts after week 260, state by state.
3. Compare the water values and the schedule of weeks 1–104 in the two runs. If they agree, the end value does not reach the reported weeks, and that is the documentation. If they differ, repeat step 2 with the cuts of the latest run until weeks 1–104 stop changing.

**Sources.**
- The same procedure in the two owner SDP studies of our review: the water values at the end of the horizon start at zero, are replaced by the water values of the start of the year, and the model is solved again until they stabilise (`helseth2017iet` p. 1643; `alic2023optimal` PDF pp. 12–13, for a pumped-storage cascade). Both assume that the system and the expected prices and inflow do not change after the year.
- End-value cuts taken from a few initial runs of the SDDP model itself: `helseth2016` (p. 940), `helseth2018optimal` (p. 6995, initial runs with a four-year horizon). Which week the cuts are taken from is not stated there; taking them one year before the end is our reading.
- The same idea inside one training run, as an infinite horizon where the last week is linked to the first: `philpott2023using` (PDF p. 4), `hole2025capacity` (PDF p. 6), `dowson2020`.

**Why this and not the alternatives.**
- It needs no number without a source: no target volume and no penalty rate.
- Step 1 is the zero-value variant of `kleiven2023` and `shapiro2020`, so the procedure contains the test that `shapiro2020` (PDF p. 14) shows is needed when the discount factor is close to one.
- Zero value alone lets the model sell the start stock during the five years (868 Mm³ on top of 2445 Mm³ of inflow, `implementation-parameters.md` Section 3), which lowers the water values.
- A penalised end target at the start volume (`lohndorf2013`, `seifert2025`, `bore2026`) is the fallback if a second run is not possible: one changed number, but the penalty rate stays a choice of ours.

**Assumption to state:** the year after the horizon is like the last year of the horizon.
**In the code:** week 260 gets a future-value variable limited by the fixed end cuts, and the starting bound on future profit must include an upper bound on the end value (the end cuts evaluated at the full reservoir).
**Reporting two years:** the profit of weeks 1–104 plus the value of the water left after week 104, read from the cuts of week 104 (ch. 6, `eq:oos_tail`); `helseth2016` (p. 940) adjusts for the difference between final and initial reservoir levels in the same spirit.

## 9. How the others use artificial water (Anders' question, 2026-11-26; extends Section 4)
- **What it is.** An extra variable in every weekly problem: water the model can add, or a limit it may break, at a cost far above any market price. It guarantees that every weekly problem has a solution, which SDDP needs (`fullnerRebennack2025` pp. 510–512).
- **Why they need it.** Something in their models can become impossible to satisfy:
  | Source | What can become impossible | The slack | Cost |
  |---|---|---|---|
  | `hjelmeland2016combined` (PDF p. 2), `gjelsvik2010` (p. 51) | the inflow model can give negative inflow when the reservoir is empty | "tank water" that fills the reservoir; penalty variables | "very costly" |
  | `helseth2016` (pp. 934, 939), `helseth2015cooptimizing` (PDF p. 4) | the water balance | artificial water supply to each reservoir | 10^6 EUR/Mm³ |
  | `helseth2022hydropower` (PDF pp. 3, 6) | an environmental lower limit on the reservoir | slack on the lower reservoir bound | tuned to the highest price, so that it is not used in order to produce |
  | `dimoski2018hydropower` (PDF p. 8), `larsen2015evaluation` (PDF p. 5) | a minimum summer level; the reservoir bounds | slack on the limit | "sufficiently large" |
  | `bueno2023impact` (PDF p. 22), `philpott2012` (PDF p. 25) | outflow limits; minimum storage zones | slack with a penalty | varied in the tests |
  | `bore2026` (PDF p. 4) and Bore's master thesis | the reservoir limits, and the requirement that the end volume equals the start volume | emergency water | 10 mEUR/GWh in the thesis |
  | `seifert2025` (PDF pp. 12–13) | the stored energy needed to cover the reserved FCR power | slack on the storage constraints | penalty term in the objective |
- **It is meant not to be used in the finished policy.** `bore2026` counts only penalty-free iterations as valid lower bounds (PDF p. 3). In `seifert2025` the storage violations disappear after about 12,000 iterations (PDF p. 15). `hjelmeland2019tste` reports that a few extreme scenarios of the final simulation use it (p. 489). `helseth2022hydropower` counts the weekly problems with a violation in each backward pass (PDF p. 10).
- **Side effects.** The penalty enters the cuts and raises the water values (`helseth2022hydropower` PDF p. 10; `bueno2023impact` PDF p. 2), and it can slow convergence (`gjelsvik2010` p. 51).
- **For us.** None of these causes exists in our weekly model: inflow is never negative, there is no minimum level above V^min and no minimum flow, and standing still with no reserves is always feasible. Artificial water would only be needed if we add a requirement that can be impossible, such as a hard end volume. With end-value cuts (Section 8) it is not needed at all.
