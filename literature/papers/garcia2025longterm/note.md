---
bibkey: garcia2025longterm
bibkey_provisional: false   # in references.bib since 2026-11-15 (added through Zotero, key pinned)
title: "Long-Term Hydrothermal Bid-Based Market Simulator"
authors: "Joaquim Dias Garcia, Alexandre Street, Mario Veiga Pereira"
year: 2025
venue: "IEEE Transactions on Energy Markets, Policy and Regulation 3(2), 144–156 (doi:10.1109/TEMPR.2025.3537665); filed copy is the arXiv preprint 2403.07270v2"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, uncertainty-modelling]
review_sections: [market-participation, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-15
takeaway: "Simulator of a bid-based hydrothermal market (Brazil, 60 monthly stages): each hydro owner's problem is solved with a mixed autoregressive (inflow) and Markovian (price or rivals' bids) SDDP, price-makers through a convexified revenue function, and the agents are iterated to an equilibrium. States the Markov-chain reformulation with one future cost function per Markov state and estimates the chain from jointly distributed scenarios of inflow, renewables, bids and spot prices."
---

# Bid-based hydrothermal market simulator with Markovian SDDP (Garcia et al., 2025)

_Our copy is the **arXiv preprint v2** (15 Nov 2024, 12 pages, two columns); published in IEEE TEMPR 3(2), pp. 144–156. Page numbers below are **arXiv pages**; check the published version before quoting. Downloaded 2026-11-15 from arxiv.org/pdf/2403.07270. The authors are at PSR and PUC-Rio._

## Research question / purpose
How can a long-term hydrothermal market with strategic (price-making) and price-taking owners be simulated when each owner faces intertemporal water decisions under uncertainty, and how much market power do concentration and forward contracts leave in the Brazilian system (abstract, p. 1; contributions, pp. 2–3)?

## Setting
- **System:** Brazilian power system; first the Southeast subsystem (46 thermal and 21 hydro plants), then the whole system (137 thermal, 364 wind and solar, 32 hydro plants) (pp. 8, 10). No pumping.
- **Markets:** spot market cleared from price and quantity bids; forward contracts as fixed price and quantity (pp. 6–8). No reserves.
- **Horizon and resolution:** 5 years in 60 monthly stages; one load block in the first study, five in the second; 1000 sampled scenarios (pp. 8, 10).

## Method
- **Model type:** multistage stochastic programs per agent inside an iterative (diagonalisation) equilibrium loop (Fig. 4, pp. 7–8).
- **Two ways to handle stagewise dependence in SDDP (p. 5):**
  - autoregressive reformulation, for uncertainty in the right-hand side (inflow): lagged values become state variables;
  - **Markov reformulation**, for uncertainty in objective or left-hand-side coefficients (prices): the paper traces it to the combined SDDP and SDP method developed for price-taker hydro bidding (Gjelsvik et al. 1999) and says that it has more recently been "termed Markovian SDDP" (Löhndorf and Shapiro). The model then has **one future cost function for each possible future Markov state**, each with its own epigraph variable and cuts, weighted by the transition probabilities in the objective (eqs. 6–8).
  - The two are not exclusive: the agents' models use the autoregressive form for inflow and the Markov form for revenue (p. 6).
- **Owner models (pp. 6–7):** a price-taker maximises spot price times energy, with spot-price scenarios from any model, for instance from the centralised SDDP simulation. A price-maker faces a revenue that depends on its own offer; the nonconvex revenue function is replaced by its convex hull so that SDDP applies. Forward contracts add a fixed revenue and an obligation to deliver.
- **Markov chain estimation (pp. 7–8):** from jointly distributed scenarios of inflow, renewable generation, bids and spot prices, an expectation-maximisation algorithm (Silva et al.) gives the transition probabilities for all stages and assigns every scenario of every stage to a Markov state.
- **Bounds and evaluation (p. 4):** averaging forward passes gives a statistical bound and the first-stage problem a deterministic bound; after training, a final forward simulation over sampled scenarios gives all primal and dual results.
- **Key modelling choices and assumptions:** hydro generation linear in turbine flow; all plants of a cascade belong to one agent; convexified revenue (stated as simplifications, p. 11).

## Model elements (centralised model, eqs. 9–15, p. 5; agent model, eqs. 16–22, p. 6)
- **Sets:** agents (price-makers, price-takers), thermal, hydro and renewable plants, upstream plants, lags of the inflow model, vertices of the convex hull, scenarios, stages.
- **Parameters:** thermal cost and capacity; maximum turbine flow; maximum storage; inflow autoregressive coefficients; renewable availability; demand; bids of other agents; forward price and quantity; transition probability matrices.
- **Variables:** storage, turbine flow, spill, thermal and renewable generation, inflow (as state), energy offer, convex-hull weights.
- **Constraints:** load balance; water balance with upstream turbine flow and spill; bounds on storage, flow and generation; the autoregressive inflow equation; for agents, the energy offer equals the agent's generation and the revenue lies in the convex hull.
- **Terminal condition:** future cost zero after the last stage (p. 5).

## Data / case
- Brazilian market operator data; Julia, JuMP, Xpress; about 3 hours per simulation on a cluster (p. 9).

## Key findings
- (p. 9, Fig. 5) Spot prices rise quickly with market concentration; market power shows up mostly as extra spillage, while average reservoir levels change little.
- (pp. 9–10) Forward contracts at 75–100 % of expected generation almost remove the market power.
- (p. 10) In the whole system, three price-makers with 32 %, 9 % and 7 % of firm energy can raise prices although the concentration index is low.
- (p. 10, Fig. 9) Price peaks from market power fall at the end of the dry season and in the month with the highest inflow, when spilling is easy.

## Strengths
- A recent, explicit statement of Markov-chain SDDP for an owner facing prices, including the form of the cuts.
- Markov chain built from joint scenarios of several variables.

## Weaknesses / limitations
- Monthly stages; no short-term price variation within a stage beyond load blocks.
- Linear generation; convexified revenue; no proof that the iteration reaches an equilibrium (p. 8).
- The number of Markov states and the SDDP iteration settings are not given in the text we read.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method: Markov-chain SDDP has a future cost function per Markov state; origin in Gjelsvik 1999 | eqs. (6)–(8) and text | p. 5 |
| Method: inflow as autoregressive state and price as Markov state in the same model | statement | pp. 5–6 |
| Data (Q-006): Markov chain estimated from jointly distributed scenarios of inflow and price | EM estimation | pp. 7–8 |
| Model: price-taker owner maximising spot price times energy with prices from a system model | revenue function (23) | p. 6 |
| Literature review 5.2: price-taker against price-maker owners | definitions and market-power results | pp. 3, 9–10 |

## Useful quotes (with page numbers)
> "one FCF for each possible future Markov state" (p. 5)

## Follow-up references to check (backward snowballing)
- Silva, Valladão & Homem-de-Mello, a data-driven approach for Markov models in SDDP (their [47]; the EM estimation).
- Flach, Barroso & Pereira (2010), long-term allocation of hydro generation for a price-maker company with SDDP, IET GTD (their [24]).
- Steeger & Rebennack (2017), dynamic convexification within nested Benders decomposition for strategic bidding, EJOR 257(2) (their [25]).
