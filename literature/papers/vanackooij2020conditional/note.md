---
bibkey: vanackooij2020conditional
bibkey_provisional: true    # not in references.bib yet (Zotero was not running 2026-11-15); key follows the Better BibTeX pattern
title: "On conditional cuts for stochastic dual dynamic programming"
authors: "Wim van Ackooij, Xavier Warin"
year: 2020
venue: "EURO Journal on Computational Optimization 8(2), 173–199 (doi:10.1007/s13675-020-00123-y)"
peer_reviewed: true
methods: [sddp-time-series, uncertainty-modelling]
review_sections: []
relevance: background
read_by: []
added: 2026-11-15
takeaway: "SDDP variant for Markovian uncertainty that needs neither a scenario tree nor a Markov chain nor extra state variables: the cut coefficients are made functions of the current uncertainty by regression on a set of sampled scenarios (as in Longstaff–Schwartz). Motivated by seasonal hydro storage valuation, but tested on gas storage facing a market price; the authors name the need to construct a Markov chain from scenarios as a weakness of the Markov-chain approach."
---

# Conditional cuts in SDDP (van Ackooij & Warin, 2020)

_Published version, open access, downloaded 2026-11-15 from link.springer.com. Page numbers below are **journal pages 173–199** (PDF page + 172). The authors are at EDF R&D. **The numerical cases are gas storage, not hydropower**; hydro reservoir valuation is the stated motivation._

## Research question / purpose
SDDP assumes stagewise-independent uncertainty. The usual remedy for dependent (Markovian) uncertainty is to enlarge the state vector, which is not always possible and never possible for uncertainty in the cost coefficients. Can the conditional expectations in the dynamic programming equations be estimated directly from a set of scenarios instead (abstract, p. 173; p. 175)?

## Setting
- **System:** storage facing a market: the owner injects gas bought on the market or withdraws and sells it; one facility, extended to five and ten dimensions; then storage with a consumption (load) constraint (pp. 186–194).
- **Markets:** spot price only (p. 187).
- **Horizon and resolution:** one year, weekly decisions, 52 steps (p. 187).

## Method
- **Model type:** multistage stochastic linear program (eq. 1, p. 176).
- **How uncertainty is represented:** a Markovian process given as sampled scenarios (eq. 11, p. 181); a mean-reverting forward-curve (HJM) price model in the storage case (p. 187); an AR(1) process in the comparison with classical SDDP (p. 192).
- **Solution method:** SDDP in which the cut slope and intercept depend on the current value of the uncertainty. The conditional expectation is computed by linear regression on local basis functions over meshes of the uncertainty space, with Monte Carlo samples in both the forward and the backward step (Sec. 3, pp. 180–186). Implemented in the open-source library StOpt (p. 186).
- **Relation to nested decomposition (p. 174):** both methods approximate cost-to-go functions with cutting planes; they differ in how the upper bound is obtained. Nested decomposition uses the whole scenario tree and is applied to problems with some hundred or a few thousand scenarios; SDDP samples and needs stagewise independence.
- **Relation to Markov chains (p. 181):** a Markov chain is named as another way to represent the uncertainty (Mo 2001, Philpott and de Matos 2012). The authors' objection is that one must "create" a chain when the data are a set of scenarios, and that a tree or chain built from samples is an artificial representation that may introduce modelling error. They do not compare with a Markov chain.

## Model elements (storage case, p. 187)
- **State:** stored volume, between zero and a maximum.
- **Decision:** injection or withdrawal per step, bounded by a **maximum injection rate and a maximum withdrawal rate**.
- **Objective:** minus price times the injected quantity (buy when injecting, sell when withdrawing); the store is empty at the start.
- No inflow, no efficiency loss, no end condition in this test.
- This is the structure of a pure pumped storage without inflow: charge and discharge limits, a volume limit and a stochastic price.

## Data / case
- Volatility and mean reversion 0.5; a flat forward curve with a small seasonal sine term, so most of the value comes from volatility (pp. 187–188).
- 20,000 trajectories for optimisation and 40,000 for simulation (p. 188).

## Key findings
- (p. 188, Table 1) Storage value: 1.280 without uncertainty against about 1.43–1.46 with it (millions of numeraire), so the value of the storage here comes mostly from price volatility.
- (p. 188, Table 2) A trinomial tree gives a slightly higher value (1.478 / 1.486); in the tree approach the simulation is sampled on the tree, so its discretisation error stays in the result.
- (p. 194) Classical SDDP cannot treat price uncertainty by adding states, because the stage problems become bilinear.
- (pp. 196–197) With conditional cuts high-dimensional storage problems can be valued from a set of scenarios; for autoregressive right-hand-side uncertainty the method is competitive with the classical state augmentation.

## Strengths
- A clear statement of what a Markov chain or tree built from scenarios adds to the model (a discretisation that the evaluation then inherits).
- Storage facing a price, with out-of-sample style simulation.

## Weaknesses / limitations
- Gas storage, no hydropower case; no inflow and no efficiency.
- No comparison with Markov-chain SDDP.
- Regression on meshes scales poorly with the dimension of the uncertainty.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory: nested (Benders) decomposition against SDDP | short comparison | p. 174 |
| Limitation of our Markov chain: built from scenarios, so a discretisation error enters training and same-chain evaluation | argument | pp. 181, 188 |
| Literature review 5.6: alternatives to Markov chains for price uncertainty in SDDP | conditional cuts by regression | pp. 180–186 |
| Results chapter: the value of a storage facing prices comes largely from volatility | Table 1 | p. 188 |

## Useful quotes (with page numbers)
> "it is necessary to 'create' a Markov chain if the initial data is available in the form of a set of scenarios" (p. 181)

## Follow-up references to check (backward snowballing)
- de Queiroz & Morton (2013), sharing cuts under aggregated forecasts, Operations Research Letters.
- Infanger & Morton (1996), cut sharing with interstage dependency.
- Valladão, Silva & Poggi (2019), time-consistent risk-constrained dynamic portfolio optimisation with Markov chains in SDDP (cited as Valladão et al. 2019).
