# What a literature review in our field covers

From the review chapters of the four closest theses (Bore 2026, Bore & Brensholm 2025, EMPIRE 2024, Norland 2025; `theses/lit-review-skill/codebook/coding/<id>.paragraphs.txt`). This is a map of topics a reader in our field expects, not a template for wording or sources.

## Themes and their sub-questions
| Theme | Bore 2026 / Bore & Brensholm 2025 | Norland 2025 | EMPIRE 2024 |
|---|---|---|---|
| Search strategy | own section: prior review extended, quality criteria, backward snowballing with a cited method | – | – |
| Uncertainty | why it pays (stochastic vs deterministic); inflow; weather and temperature; prices by market, price-taker vs price-maker, bid volumes and activation; representing it: correlation structures, scenario trees and Markov chains, data length, number of states, granularity | coordinated bidding under uncertainty; tractability, scenario reduction, simplified stochastic structure | deterministic vs stochastic vs hybrid in system models; perfect information in hydro storage |
| Plant / physical modelling | non-convexity of the production function; head dependency; MILP vs successive LP; Norwegian high-head context; trade-off with computation | – | regulated hydro as generator vs storage; pumped vs regulated hydro |
| Markets | coordinated vs sequential bidding; market compositions (DA+ID, DA+aFRR, DA+symmetric reserves, hypothetical products) with effect sizes after a comparability caveat; activation modelling; forward contracts and price-making noted as out of scope | multi-market participation with reserves; price-making vs price-taking; DSM and storage in reserve markets | – |
| Investment / capacity | investment perspective as the least explored part; revenues vs upgrade cost | capacity expansion and decarbonisation pathways; price volatility and investment | – |
| Solution methods | deterministic equivalent; SDP; SDDP and its extensions (risk, cuts, multi-horizon); SDDP with multi-market participation; Benders; successive LP; multi-objective | – | model structure and time resolution of system models |
| Contribution | gap stated from a named earlier study; what the thesis does; comparison table with own row | same, with table | same |

## What our review must therefore cover (chapter 5)
- Search strategy (Bore has it; the IØT guidelines ask for it).
- Perspective: system vs owner, price-taker vs price-maker (checked claims in `knowledge/topics/valuation-perspective.md`).
- Uncertainty: which inputs, dependence, timing of information, representation by weekly states, price volatility and persistence (our research question).
- Plant modelling: pumping, head, efficiency, linear vs non-convex.
- Markets: energy, reserve capacity, activation; what each adds and costs.
- Capacities: adding a pump, upgrading units, large expansions and price effects, reservoir sizing.
- Solution methods last: two-stage, rolling horizon, SDP, SDDP, applications to owners.
- Gap and contribution with Table 3, our study in the last row.

## Comparison-table columns used by the closest four
Bore: planning horizon, hydraulic modelling, stochastic variables, market participation, solution method. EMPIRE: horizon, granularity, uncertainty, inter-seasonal linkage, hydro representation. Norland: market coverage, uncertainty, flexibility assets, investment. Ours: perspective and asset, time and uncertainty, model representation, market focus, capacity question.

## The gap sentence they all use
"To the author's best knowledge, there is a research gap concerning …" or "… remains relatively unexplored in the literature", followed by the nearest study and what it did not do, then "this thesis …" and the research questions.
