---
bibkey: mo2001
title: "Optimisation of hydropower operation in a liberalised market with focus on price modelling"
authors: "Birger Mo, Anders Gjelsvik, Asbjørn Grundt, Kjetil Kåresen"
year: 2001
venue: "2001 IEEE Porto Power Tech Conference, Porto, Portugal, 10–13 September 2001"
peer_reviewed: true
methods: [uncertainty-modelling, sddp-markov-chain, sdp]
review_sections: [price-volatility, modelling-phs-plants]
relevance: high
read_by: []
added: 2026-11-04
takeaway: "How SINTEF builds the weekly Markov price model used in SDP/SDDP hydro scheduling (ProdRisk lineage): per week, N price nodes from EMPS scenarios (5 nodes, min 6 scenarios per node for 70 scenarios), transition probabilities from counted scenario moves then adjusted by a small QP to preserve conditional and unconditional expected prices; extra extreme nodes for realistic simulation; notes that a first-order Markov chain forgets its state, so long-dated forward price uncertainty needs an added shift model."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/mo2001.pdf
---

# Markov price model for hydro scheduling in a liberalised market (Mo et al., 2001)

_IEEE Porto Power Tech 2001 conference PDF (6 pages, DOI 10.1109/PTC.2001.964603). The PDF shows no proceedings page numbers, so "p. X" below = PDF page X. Equations checked on rendered page images (the text layer garbles them)._

## Research question / purpose
Describe the structure and identification of a spot price model simple enough for stochastic (SDP/SDDP) optimisation of hydro operation and flexible contracts, while capturing as much of the price statistics as possible, including extremes; and extend it to represent long-term forward price uncertainty for integrated scheduling and hedging (p. 1–2).

## Setting
- **System:** Scandinavian market (~50% hydro, nearly 1000 hydro plants); producers using SINTEF scheduling models (refs [2] Fosso et al. 1999, [3] Gjelsvik et al. 1999, [4] Mo, Gjelsvik & Grundt 2001 integrated risk management) (p. 1–2).
- **Markets:** spot market; forward/futures contracts for hedging (Nord Pool).
- **Horizon and resolution:** weekly time resolution; price forecasts 2–3 years ahead (Fig. 1 shows 60 scenarios, 2 years, weekly) (p. 1–2).

## Method
- **Price forecasts (input):** fundamental approach using the EMPS model; each historical weather year (1931–2000, so at most 70 scenarios) gives one price scenario with equal probability; overlapping sequences (1931–33 = scenario 1, 1932–34 = scenario 2, ...) for a three-year horizon; scenarios may be adjusted to match current forward prices (p. 1).
- **Properties of the price forecast to preserve:** strong correlation with previous week's price; a minimum price (zero or cost of hydro generation); mean reversion; seasonal variation (p. 2).
- **Model structure:** discrete, time-inhomogeneous first-order Markov chain; N price nodes P_i(t) per week, transition probabilities p_ij(t); same price model for SDP and SDDP (p. 2, Fig. 2).
- **Node identification (Sec. II.A, p. 3):** user sets N and N_min (minimum scenarios per node). Lowest node = mean of the N_min lowest scenario values (p_min), highest = mean of the N_min highest (p_max); interval between split into N−2 equal intervals, node value = mean of scenarios inside; intervals widened until each has ≥ N_min scenarios; repeated independently each week; scenario-to-node membership recorded. With 70 scenarios, **5 nodes and N_min = 6** usually give a "good" result (p. 3).
- **Transition probabilities (Sec. II.B, p. 3–4):** initial estimate p_ij(t) = N^P_ij(t)/N_i(t) (count of scenarios moving from node i at t to node j at t+1) (eq. 1). Then adjusted by a nonlinear (quadratic) problem per week: minimise Σ_i (Σ_j p̃_ij P_j(t+1) − E_i(t+1))² + λ Σ_i Σ_j (p̃_ij − p_ij)², where E_i(t+1) is the mean next-week price of scenarios in node i; subject to rows summing to 1, Σ_i p̃_ij N_i(t) = N_j(t+1) (preserves the node population and so the unconditional distribution), 0 ≤ p̃_ij ≤ 1 (eqs. 2–6). λ = 0.01; solved with NAG E04UCF (p. 3–4).
- **Extreme prices (Sec. II.C, p. 4):** two extra nodes per week (highest and lowest price) so that simulated strategies behave realistically for price spikes (e.g. week ~70 spike in Fig. 1, only one scenario); expanded matrix leaves statistics between original nodes and first-stage decisions unchanged (eqs. 7–8).
- **Long-term price uncertainty (Sec. III, p. 4–5):** forward price = conditional expected spot price; because a first-order Markov chain "forget[s] its initial state at an exponential rate", the model has almost no uncertainty for long-dated forwards, so the hedging model would never change positions one year ahead. Ad hoc fix: superimpose a symmetric shift model (±Δ(t) with probability p_Δ(t), absorbing), estimated from observed forward price volatility; model becomes three times larger; analogous to one-factor vs multi-factor commodity models (Schwartz 1997). During simulation the shift is assumed not to occur (p. 5).

## Data / case
EMPS-based price scenarios (Fig. 1: 2-year weekly scenarios, NOK/MWh, highest price 700 NOK/MWh not shown). Implemented in SINTEF models [2], [3] (in use for about one year) and [4] (being tested by Norsk Hydro) (p. 5).

## Key findings
- (p. 5, Fig. 4) SDP strategy simulated two years ahead: including extreme price nodes raises the simulated minimum reservoir level in winter and changes the spring maxima; without extremes, the highest week-15 reservoir level corresponded to an extremely low price, with extremes to a high price.
- (p. 5, Fig. 5) Conditional expected spot price seen from week 20 converges to almost the same value by week 104 regardless of initial node (Markov chain memory loss).
- (p. 6) Each improvement in identification or structure improved simulated economic results and gave more "realistic" reservoir content in many tests; first-stage improvements hard to verify quantitatively.
- (p. 6) Further work: 70 scenarios are too few for risk management; generate more price scenarios per inflow year, e.g. AR model on EMPS-vs-observed price differences.

## Strengths
- Concrete, reproducible recipe for Markov price model construction from scenarios, with recommended parameter values (N = 5, N_min = 6, λ = 0.01).
- Explicitly preserves conditional and unconditional expected prices; treats extremes.
- Identifies the memory-loss limitation of first-order Markov chains for long-term price persistence.

## Weaknesses / limitations
- Weekly price level only; no intra-week profile.
- Price-only Markov chain (inflow handled separately in the optimisation models).
- Little quantitative validation; EMPS scenarios as the only data basis.
- Text inconsistency: says "Equation (6) is used to fulfill the requirement regarding the unconditional expected future price" (p. 4), but eq. (6) is p̃_ij ≤ 1; the population constraint (4) is what does this (likely a typo).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method: Markov-chain construction from weekly samples | Node identification + counted transitions, eq. (1) | p. 2–3, Sec. II.A–B |
| Method: preserving expected prices when estimating transitions | QP eqs. (2)–(6), λ = 0.01 | p. 3–4, Sec. II.B |
| Method: number of states / minimum members per state | 5 nodes, ≥ 6 of 70 scenarios | p. 3 |
| Method: representing price extremes / spikes | Extra extreme nodes, eqs. (7)–(8) | p. 4, Sec. II.C |
| Background: properties of Nordic weekly prices (autocorrelation, mean reversion, seasonality, floor) | List | p. 2 |
| Background/limitation: Markov chain forgets initial state; long-term forward uncertainty missing | Discussion + Fig. 5 | p. 4–5, Sec. III |
| Lit. review: Nordic fundamental price forecasting (EMPS scenarios from historical weather years) | Description | p. 1 |
| Background: correlation of inflow and price for producers | Low inflow ↔ high prices | p. 1 |

## Useful quotes (with page numbers)
> "a Markov model will tend to forget its initial state at an exponential rate" (p. 4)

## Follow-up references to check (backward snowballing)
- Mo, Gjelsvik & Grundt (2000/2001), "Integrated risk management of hydro power scheduling and contract management", IEEE TPWRS (ref [4]).
- Gjelsvik, Belsnes & Haugstad (1999) [`gjelsvik1999`].
- Fosso, Haugstad, Mo & Wangensteen (1999), "Generation scheduling in a deregulated system: the Norwegian case", IEEE TPWRS 14, 75–81.
- Schwartz (1997), "The stochastic behavior of commodity prices", J. Finance.
- Schjølberg & Mo (2001), extension of price forecasts (ref [6]).

