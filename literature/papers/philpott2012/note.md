---
bibkey: philpott2012
title: "Dynamic sampling algorithms for multi-stage stochastic programs with risk aversion"
authors: "A. B. Philpott, V. L. de Matos"
year: 2012
venue: "European Journal of Operational Research 218(2), 470-483"
peer_reviewed: true
methods: [sddp-markov-chain, risk-averse-cvar, uncertainty-modelling]
review_sections: []
relevance: high
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/philpott2012.pdf"
takeaway: "Markov-chain SDDP with one cut set per Markov state (multi-cut vs single-cut variants) plus a nested, time-consistent mean-CVaR risk measure, applied to 52-week New Zealand hydrothermal scheduling with 4 wet/dry inflow states; Markov policy beats the stagewise-independent one when inflows are Markovian, and risk aversion cuts worst-case cost and load shedding at modest expected-cost increase."
---

# Dynamic sampling with risk aversion and Markov chains (Philpott & de Matos, 2012)

_Version filed: author manuscript from Optimization Online, dated 9 February 2011 (27 pages). **Page numbers below are manuscript (= PDF) pages.** Journal pages are 470-483; no exact mapping is possible. Cite sections (2.1, 4.1, 5, 6) when page precision matters._

_Tagging note: `sddp-markov-chain` for Sec. 2.1 and 4.1 (Markov chain in SDDP, cut sets per Markov state), which is our method. `risk-averse-cvar` for Secs. 3-4 and 6. `uncertainty-modelling` for the construction of the wet/dry inflow Markov chain from historical data (p. 18). No review section: hydrothermal system cost minimisation, no PHS, no market participation._

## Research question / purpose
- Incorporate a time-consistent coherent risk measure (convex combination of expectation and CVaR) into multistage stochastic programming so it can be solved with an SDDP-type algorithm (abstract, p. 1).
- Describe a Markov-chain extension of SDDP for stagewise-dependent inflows (Sec. 2.1, pp. 5-7) and combine it with the risk measure, including risk aversion that depends on the Markov state (Sec. 4.1, pp. 13-14).
- Study the resulting policies for New Zealand long-term hydrothermal scheduling and compare risk-averse and risk-neutral policies (pp. 3, 14-25).

## Setting
- **System:** New Zealand hydrothermal system: 33 hydro plants (5400 MW), 12 thermal plants (2800 MW), 3-bus transmission (South Island, Hay, North Island) (p. 14); 9 storage reservoirs (8 South Island + head of Waikato chain), total capacity 7.5 billion m3; other hydro run-of-river (pp. 15, 18).
- **Markets:** none; central cost minimisation (fuel, shortage and flow-constraint penalties). Load shedding modelled as expensive thermal (pp. 15-17).
- **Horizon and resolution:** one year, **52 weekly stages**; weekly demand as a load duration curve with 3 blocks (peak, off-peak, shoulder) (pp. 17-18).

## Method
- **Model type:** multistage stochastic LP; stage LP (10) with power balance per bus, water balance v_{t+1} = v_t - A(q_t + s_t) + omega_t, bounds, linear hydro conversion factor gamma_m per station, cuts on future cost (p. 17). No losses, line capacities only (p. 17).
- **How uncertainty is represented:**
  - Standard SDDP assumes stagewise independence (p. 5). Alternative to an autoregressive model: let the distribution of the random data depend on an **underlying Markov state** (p. 5). If the state is continuous (AR), the future cost must be convex in it; if discrete (finite Markov chain), "we must enumerate a future cost function for each value that the state may take" and record a set of cuts for each Markov state (p. 5). They note Mo et al. (2001) used a similar approach for uncertainty in the objective (e.g. electricity prices) (p. 5).
  - Two-state example (Figs. 1-3, pp. 5-7): descendant nodes are the same in every state but with different probabilities, so cuts cannot be shared directly, but duals from one node are valid for all nodes with the same realisation; cuts for each state are formed with that state's transition probabilities (p. 6).
  - **Multi-cut** approach: a partial cut per successor state, all used in every state, combined with transition probabilities (theta^1 = q theta_ab + (1-q) theta_cd) (pp. 6-7). **Single-cut** approach: one aggregated cut per state using the conditional expectation (p. 7). Both keep two cut sets per stage; multi-cut gives larger stage problems but "is expected to require fewer iterations" (p. 7).
  - NZ case: historical inflows 1987-2006 (20 years) aggregated to North and South Island; each island-week classified **wet or dry** (dry if island inflow sum below historical average) giving **4 Markov states** (WW, DW, WD, DD); transition probabilities estimated from the 1987-2006 historical sequence (p. 18, Table 1, footnote 2). 20 openings per stage, 52 stages: > 2.25e66 scenarios (p. 18).
  - Simulation: random sequence of 52 states, then sample a historical weekly inflow record from the group of the simulated state (p. 18). **The Markov chain is assumed to be the true process** for benchmarking; testing other approximations of the real inflow process is left to future work (p. 18).
- **Risk measure (Secs. 3-4):**
  - VaR is non-convex; CVaR is the tightest convex safe approximation (p. 8). rho(Z) = (1 - lambda) E[Z] + lambda CVaR_{1-alpha}[Z]; translation equivariance forces the weights to sum to one (pp. 8-9). Equivalent to the mean-deviation-from-quantile of Miller & Ruszczynski (p. 9). Nested, time-consistent (Ruszczynski 2010) (pp. 9-10).
  - Implementation: auxiliary variable u_{t+1} (VaR level) chosen at stage t, v_t >= cost - u_t; stage problem (9) with cuts in (x_t, u_{t+1}) (pp. 10-13). Still RHS-only LPs, so standard SDDP applies and it "converges almost surely ... under mild conditions on the sampling process" by Philpott & Guan (2008) (p. 13).
  - Upper bound: needs conditional sampling, prohibitively expensive; they run the risk-averse model for the number of iterations the risk-neutral model needed to converge (p. 13).
  - With Markov chains: one cut set per Markov state; u acts as an extra state variable (p. 13). lambda_t cannot depend on the state observed in stage t (it appears in the t-1 problem), but can depend on the state in t-1; this needs Markov persistence (p > 0.5, q > 0.5) to make sense and costs extra computation because cuts can then only be added to visited states (p. 14).
- **Solution method / settings:** SDDP with **N = 1 scenario per forward pass** (cites de Matos et al. 2010 as better than N = 200); **fixed number of iterations** instead of the Pereira-Pinto test, which "can be misleading" (p. 5). 4000 iterations (16,000 for state-dependent lambda) (p. 19). Validation on T = 4, 4 openings (64 scenarios) against the deterministic-equivalent LP in CPLEX 11.0: LBs match to ~1e-9 (pp. 19-20, Table 4).
- **Key modelling choices and assumptions:** linear hydro production (constant conversion factor), relatively complete recourse via penalties, no minzone constraint (p. 23), a risk weight (most likely lambda; the Greek symbol is lost in the text extraction, unverified) set to 0 in stage 1 and T+1 (p. 18). The CVaR quantile level used in the experiments could not be found in the extracted text (unverified); p. 8 only says alpha is "typically" small, e.g. 0.05.

## Data / case
- NZ system, 2006 calendar-year data, historical inflows 1987-2006 (pp. 17-18). Cases (Table 2, p. 19): lambda_L = 0, 0.5, 0.9 with stagewise-independent or Markov (M) policy, plus "4 Ls" with lambda depending on previous-stage state (WW 0, DW 0.5, WD 0.5, DD 0.9; Table 3). Policies evaluated on 4000 inflow scenarios sampled from the Markov chain (p. 21).

## Key findings
- (p. 7) Multi-cut vs single-cut trade-off for Markov-state cut sets.
- (pp. 19-20, Table 4) Implementation validated exactly against the deterministic equivalent.
- (p. 21, Table 5) Expected total operating cost: Markov risk-neutral policy 405.798 M$ (lowest); stagewise-independent risk-neutral 407.071 M$, i.e. **+1.27 M$ from wrongly assuming independence when inflows are Markovian**. Risk-averse policies cost +3.7 to +13.0 M$ (about 1-3%).
- (p. 21, Table 6) Worst scenario: independent risk-neutral policy 823.8 M$ vs about 628-644 M$ for all others; the Markov risk-neutral policy "performs creditably in this worst case" (631.0 M$).
- (p. 22, Fig. 7) Over the 200 worst outcomes the stagewise-independent risk-neutral policy is first-order stochastically dominated by the others.
- (p. 22) The nested risk measure controls high costs in the next few periods, not the distribution of total annual cost.
- (pp. 22-23, Fig. 9) Risk-averse policies store more water in the first half of the year and end the year with higher reservoirs; they cost more in wet scenarios (Fig. 8).
- (p. 23, Fig. 10; p. 25, Table 7) Risk-neutral policies breach the NZ minzone often; risk-averse ones mostly do not; load-shedding probability 0.085% (independent RN), 0.025% (Markov RN), 0 for all risk-averse cases.
- (p. 25) Conclusions: risk aversion is easy to add; a dynamic risk measure is a promising alternative to minzone penalties (hard minzones violate relatively complete recourse); weakness is the difficulty of estimating the policy value.

## Strengths
- One of the earliest clear descriptions of Markov-chain SDDP with explicit cut-set-per-state construction and the multi-cut/single-cut distinction.
- Transparent Markov-chain construction from historical data, with transition probabilities estimated from the historical sequence.
- Out-of-model comparison of policies on a common simulated benchmark; exact validation on a small instance.
- Weekly 52-stage hydro case directly comparable in structure to ours.

## Weaknesses / limitations
- Benchmark assumes the fitted Markov chain is the true inflow process (p. 18), so out-of-sample robustness to misspecification is not tested; our out-of-sample evaluation on unseen data addresses exactly this gap.
- Only 2 states per island (wet/dry by threshold), not clustering; prices not modelled (cost minimisation).
- No statistical upper bound in the risk-averse case; stopping by fixed iteration count (pp. 5, 13).
- Linear production, no head effects, no pumping.
- Manuscript version; journal page numbers differ.

## Use it for... (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3.x: Markov representation in SDDP; cut set per Markov state | Construction, two-state example, why cuts cannot be shared directly across states | Sec. 2.1, pp. 5-7 |
| Model: future value as sum over successor states of alpha_{s+1,m'} (multi-cut) | Multi-cut vs single-cut; size vs iterations trade-off | pp. 6-7 |
| Method: building the Markov chain from historical data; estimating transitions | Wet/dry classification per island, 4 states, transitions from 1987-2006 sequence; simulation by sampling a historical week from the state's group | p. 18, Table 1 |
| Method: SDDP settings (one forward scenario per iteration, fixed iterations, misleading PP stopping test) | Choices and justification | p. 5; p. 19 |
| Method: validating an SDDP implementation on a small instance | Deterministic-equivalent check, T = 4, 64 scenarios | pp. 19-20, Table 4 |
| Results / discussion: value of modelling temporal dependence | +1.27 M$ expected cost and far worse worst case under stagewise-independent policy | p. 21, Tables 5-6 |
| Discussion / future work: risk aversion (CVaR) in SDDP | Nested mean-CVaR, auxiliary VaR state, state-dependent lambda, more water stored, no UB | Secs. 3-4.1, pp. 8-14; pp. 22-25 |
| Problem description: risk-neutral assumption limitation | Risk-averse policies keep higher reservoirs and avoid shortages at ~1-3% cost | pp. 21-25 |

## Useful quotes (with page numbers)
> "we record a set of cuts for each state in the Markov chain instead of just one for the stage." (p. 5)

## Follow-up references to check (backward snowballing)
- Mo, Gjelsvik & Grundt (2001), integrated risk management with price uncertainty in the objective (IEEE TPWRS 16) - related to `mo2001` (Porto PowerTech) in our bib.
- de Matos, Philpott, Finardi & Guan (2010/2011), "Solving long-term hydrothermal scheduling problems" (PSCC 2011) - source of the N = 1 recommendation.
- Shapiro (2011) - `shapiro2011`.
- Ruszczynski (2010), risk-averse DP for MDPs (time consistency).
- Philpott, de Matos & Finardi (2013), coherent risk measures and upper bounds.
- Infanger & Morton (1996), cut sharing with interstage dependency.

