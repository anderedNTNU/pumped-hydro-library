---
bibkey: baslis2011midterm
bibkey_provisional: true
title: "Mid-Term Stochastic Scheduling of a Price-Maker Hydro Producer With Pumped Storage"
authors: "Costas G. Baslis, Anastasios G. Bakirtzis"
year: 2011
venue: "IEEE Transactions on Power Systems 26(4), 1856–1865"
peer_reviewed: true
methods: [multistage-scenario-trees, deterministic-lp-milp]
review_sections: [modelling-phs-plants, market-participation]
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/Medium_term_pumpekraft/Baslis2011.pdf"
takeaway: "One-year, hourly, 3-stage/90-scenario stochastic MILP for a price-maker Greek hydro producer with 720 MW pumped storage; residual demand curves extended to negative quota price pumping; solved monolithically (23 M variables, ~30 h); shows capacity withholding and that forwards mitigate market power."
---

# Mid-term stochastic scheduling of a price-maker hydro producer with pumped storage (Baslis & Bakirtzis, 2011)

> **Page convention.** Journal page = PDF page + 1855 (PDF p. 1 = p. 1856, PDF p. 10 = p. 1865). Tables II–VI (input data) are images and did not extract to text; values below come from the running text.

## Research question / purpose
Build a yearly (mid-term) self-scheduling model for a **price-maker** hydro producer that owns pumped storage, so that mid-term reservoir management reflects the short-term (hourly, day-ahead) profit-maximising bidding, including the use of market power, under uncertain inflows and residual demand (pp. 1856–1857).

## Setting
- **System:** hypothetical producer owning all major Greek hydro plants: 10 plants including 2 pumped-storage plants, 5 river basins, 4 cascades; 2,720 MW generation, 720 MW pumping, cycle efficiency 75% (p. 1861, Table I). System capacity ≈ 9.5 GW, peak load 8.9 GW (p. 1862).
- **Markets:** day-ahead energy market (uniform-price hourly auctions, single node) (p. 1858); fixed forward contracts as input (pp. 1858, 1862). No reserves.
- **Horizon and resolution:** one year starting in October, hourly resolution throughout (p. 1860–1861).

## Method
- **Model type:** multistage (three-stage) stochastic MILP, deterministic equivalent solved directly with GAMS/CPLEX (p. 1857, p. 1862).
- **How uncertainty is represented:** scenario tree of inflow × residual-demand realisations: stage 1 = October (deterministic); stage 2 = Nov–Feb with 5 inflow × 3 demand = 15 branches; stage 3 = Mar–Sep with 3 inflow × 2 demand = 6 branches per parent → 90 scenarios (pp. 1859–1860, Fig. 3). Realisations are scale factors on average inflow and demand curves; stage-3 factors are multiplied by the parent factor to model correlation (p. 1862). Competitors' bid prices are scaled with inflow and demand (dry/high demand → higher bids) (p. 1860).
- **Solution method:** single large MILP, no decomposition: 23 million variables (3.5 million integer), ≈ 30 h, optimality gap ≤ 0.3% (0.01% without contracts), memory 15–20 GB (p. 1863).
- **Key modelling choices and assumptions:**
  - Price-maker via hourly stepwise **residual demand curves (RDC)**, linearised with one binary per RDC step (pp. 1858, 1861, eqs. 3–7).
  - **Modified RDC for pumping:** the part of the competitors' aggregated bid curve between actual and "augmented" load (load + max pumping) is placed on the negative quota axis, so pumping is negative quota bought at the resulting price (p. 1858, Fig. 1).
  - Head dependence ignored; output linear in turbine flow with constant specific consumption, "similarly to most mid-term models" (p. 1859).
  - End-of-horizon: target final reservoir volume (common practice: average historical level); in the case, final = initial volume (pp. 1859, 1862).
  - Water travel time ignored (p. 1861). Non-anticipativity via scenario bundles (p. 1861, eq. 14).
  - Optimal pumping set by profit only, "no predefined rules for the operation of pumped storage plants" (p. 1859).

## Data / case
Greek system data from the Hellenic TSO; yearly inflows ≈ 4 TWh, twice the total storage capacity (p. 1862). Competitors are thermal, bidding marginal cost; price cap 175 $/MWh; RDCs with up to 8 price levels (p. 1862). Three forward-contract cases (Table VII).

## Key findings
- (p. 1863, Fig. 5) Storage is built up until early summer (max in May) to sell during the July–August peak; July–August profits highest (Fig. 6).
- (p. 1863, Fig. 7) Pumping in low-demand hours at ≈ 25 $/MWh; the producer withholds capacity at peak hours, causing price spikes of ≈ 140 $/MWh.
- (p. 1863, Table IX) Capacity withholding occurs regardless of inflow: even in the wettest scenario price spikes last ≈ 2,400 h, average production at spikes < 1 GW of 2.7 GW installed. Extra water goes to off-peak hours. "For a price-taker hydro producer, an opposite management of water resources would be optimal".
- (p. 1864, Fig. 9) Under low demand, pumping is used much more; much second-stage production comes from cycling pumped water, raising storage carried into stage 3.
- (p. 1864, Figs. 10–11) Forward contracts shift production to peak hours and limit price spikes (market-power mitigation).
- (p. 1864, Table X) With high contract volumes it can be optimal to pump at a high price and generate at a low price, to lower the price at which contracted energy is bought.
- (p. 1865) Solving such a very large stochastic MILP monolithically is feasible with a commercial solver.

## Strengths
- Explicit pumped-storage modelling inside a mid-term stochastic model with hourly chronology.
- Clear illustration of how a price-maker's PHS operation differs from a price-taker's.
- Honest reporting of model size and run time.

## Weaknesses / limitations
- Only 90 scenarios; within each stage the producer has a deterministic view (p. 1860). The scenario tree is constructed with ad hoc scale factors, not from data.
- Market model relies on conjectured competitor behaviour and RDCs that are hard to estimate (p. 1860).
- No head effects, no reserves, no intraday, fixed end-of-horizon target (no water value).
- Solution is tree-contingent decisions, not a policy that generalises to unseen realisations.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review: modelling of PHS plants (mid-term, stochastic) | 3-stage tree, hourly MILP, 2 PHS plants, 75% cycle efficiency | pp. 1859–1862 |
| Lit. review: market participation, price-maker vs price-taker | RDC modelling; price-taker would allocate more to peaks | p. 1858; p. 1863 |
| Model: justify ignoring head effects in mid-term models | "similarly to most mid-term models [14], head dependencies are ignored" | p. 1859, Sec. II-B |
| Model: end-of-horizon reservoir target vs water value | Target = average historical level; final = initial in case | p. 1859; p. 1862 |
| Method: scenario-tree size vs tractability (motivation for SDDP) | 23 M variables, 3.5 M integer, ~30 h | p. 1863 |
| Background: forward contracts mitigate market power | Results | p. 1864 |

## Useful quotes (with page numbers)
> "For a price-taker hydro producer, an opposite management of water resources would be optimal" (p. 1863)

## Follow-up references to check (backward snowballing)
- [15] Flach, Barroso & Pereira (2010), long-term allocation of hydro for a price-maker company with SDDP, *IET GTD* 4:299–314 (SDDP with concave-hull profit approximation, p. 1857).
- [21] de la Torre, Arroyo, Conejo & Contreras (2002), price-maker self-scheduling, MILP approach, *IEEE TPWRS* 17(4):1037–1042 (basis of the RDC linearisation).
- [20] Lu, Chow & Desrochers (2004), pumped-storage hydroturbine bidding strategies, *IEEE TPWRS* 19(2):834–841 (price-taker PHS bidding).
- [18] Crampes & Moreaux (2008), pumping water to compete in electricity markets, LERNA working paper.
- [8] Conejo et al. (2002), self-scheduling of a hydro producer in a pool-based electricity market, *IEEE TPWRS* 17(4).
- [14] Wallace & Fleten (2003), stochastic programming models in energy, *Handbooks in OR & MS* vol. 10, pp. 637–677 (the source for "head dependencies are ignored" in mid-term models).

