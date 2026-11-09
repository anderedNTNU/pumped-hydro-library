---
bibkey: helseth2015cooptimizing
bibkey_provisional: true
title: "Co-optimizing sales of energy and capacity in a hydropower scheduling model"
authors: "Arild Helseth, Birger Mo, Marte Fodstad, Martin N. Hjelmeland"
year: 2015
venue: "2015 IEEE PowerTech, Eindhoven, pp. 1–6 (doi:10.1109/PTC.2015.7232252)"
peer_reviewed: true
methods: [sddp-markov-chain, sddp-time-series, uncertainty-modelling]
review_sections: [market-participation, electricity-markets, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Precursor of helseth2016: hybrid SDP/SDDP (spot-price Markov chain, AR inflow) for a 986 MW Norwegian cascade selling day-ahead energy and FCR-N capacity co-optimised within each week, with deterministic 2013 FCR prices; reserves keep reservoirs higher before the spring flood and use more water in summer/autumn, revenue +2.58 %, which the authors call too optimistic (unlimited reserve demand, LP without start/stop, same-week co-optimisation instead of sequential decisions)."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/helseth2015cooptimizing.pdf
---

# Co-optimising energy and FCR capacity in SDP/SDDP (Helseth et al., 2015)

_Page convention: the IEEE PDF has no printed page numbers; "p. X" = page X of the 6-page paper (= PDF page; proceedings pagination given as pp. 1–6 in the citing paper hjelmeland2016combined, ref. [17]). Equations (4)–(7) are partly garbled in the text extraction, so their exact symbols are paraphrased._

## Research question / purpose
Propose and test a way to include **sales of reserve capacity** (Norwegian primary reserve, FCR-N) in the hybrid SDP/SDDP medium-term scheduling algorithm of Gjelsvik et al. (1999), so that energy and capacity sales are co-optimised for a price-taking producer (abstract, p. 1). Emphasis on the Norwegian primary reserve market, "which seems to offer a certain potential for additional revenue ... particularly in the low-load (summer) season" (pp. 1–2).

## Setting
- **System:** Norwegian watercourse in NO2 with 7 reservoirs and 7 stations, total 986 MW (p. 4, Fig. 5) — the same system as in `helseth2016`. Station 5 has maximum efficiency at 79 % of capacity (260 MW) and can offer 33 MW FCR (p. 5). No pumping.
- **Markets:** day-ahead (Elspot) energy + FCR-N capacity, symmetric and spinning (p. 4). Market background (p. 2): FCR-N active in 49.90–50.10 Hz via governor droop for generators > 10 MVA; two Norwegian primary reserve markets since 2008, a **weekly** market for 6 time blocks and a **daily** market with hourly procurement; Statnett marginal pricing. Fig. 1: weekly-market volumes are large in the low-load season (weeks 20–30) because the TSO secures spinning reserve early when prices are low; Fig. 2: FCR-N daily price vs NO2 spot 2013, weekly FCR price slightly higher in summer (p. 2).
- **Horizon and resolution:** 1-year planning horizon, weekly stochastic stages; 21 time steps per week; capacity sold in 6 blocks (weekday night/day/evening, weekend night/day/evening), in line with the weekly Norwegian primary reserve market (p. 3, Fig. 4).

## Method
- **Model type:** multistage stochastic LP; weekly decomposed LP (1)–(7) inside the hybrid SDP/SDDP algorithm (pp. 3–4).
  - Objective (1): future expected revenue α_t + Σ spot price × generation + Σ FCR block price × block duration × reserved capacity.
  - (2) water balance with discharge segments, spill and upstream inflows; (3) generation = Σ energy equivalent × segment discharge (piecewise linear, concave).
  - (4) **spinning requirement**: reserved capacity in a time step ≤ the station's generation (MW) in that step — "ensuring that the producer do not offer more reserve capacity than what is already spinning" (p. 4).
  - (5) reserve + generation ≤ installed capacity.
  - (6) Benders cuts per price point.
  - (7) **droop-based cap**: 0 ≤ r_hb ≤ a limit set by the FCR frequency band (0.1 Hz), the station's droop setting ρ_h and P_max (exact expression garbled in the text extraction, unverified); "The capacity sold to the FCR market cannot exceed the physical limit dictated by the droop setting" (p. 4).
- **How uncertainty is represented:** weekly inflow (AR model, sampled in both forward and backward passes so that convergence is guaranteed, p. 4) and weekly average spot price as a **discrete Markov chain** (price points, transition probabilities computed beforehand following Mo et al. 2001 [15]; cuts stored per price point and stage, p. 3, Fig. 3). Price profile scaling gives one price per time step (p. 3). **FCR prices deterministic**: a two-dimensional energy×FCR Markov chain is possible in principle, but because Nordic balancing market design changes often and there are few years of complete data, recent observed FCR prices are used as deterministic input (p. 3). At the start of each week all prices for the week are known (p. 2–3).
- **Solution method:** hybrid SDP/SDDP (Gjelsvik et al. 1999 [11]); price state handled by DP because it violates SDDP convexity (p. 3). 5 price points, 80 forward samples, 8 backward samples, max 100 iterations; C++ with Gurobi dual simplex; ~42 h per run on an i7 1.73 GHz, 16 GB; "good convergence properties" (p. 5).
- **Key modelling choices and assumptions:** price taker in both markets; no demand obligations (p. 3); complete recourse via penalty variables (omitted from the written model, p. 4); same end-value cuts in both cases (p. 5); no head effects; no start/stop.

## Data / case
- Spot price scenarios from the EMPS fundamental model [16]; FCR prices from the Norwegian weekly market (daily-market prices are similar, Fig. 2) (p. 4).
- Two cases: dual-market (energy + FCR) and single-market (energy only) (pp. 4–5).

## Key findings
- (p. 5, Fig. 6) Station 5 is kept spinning at 33 MW for a substantial share of time to sell FCR; conversely, when the single-market case runs at full capacity, 33 MW is often withheld from spot and sold as FCR.
- (p. 5, Fig. 7) With reserves, total reservoir content is kept **higher in winter/spring** (capacity withheld), and **more water is used in summer** to keep units spinning.
- (p. 5, Fig. 8) Water values (duals of (2)), dual minus single market, for the 4 largest reservoirs: **lower before the spring flood (around time step 400), higher in summer and autumn**. (Contrast with `helseth2016`, where water values were generally lower with reserves.)
- (p. 5) Expected revenue **+2.58 %** with FCR sales, "which is too optimistic compared to the actual opportunities that producers see in today's market". Three reasons (pp. 5–6): (1) unlimited market room for the reserves offered (the TSO buys a limited total); (2) LP with no start/stop binaries and a concave PQ curve lets stations "generate electricity at low rates at an artificially high efficiency for the purpose of delivering reserves"; (3) all prices of both markets are known at the start of the week, so the two markets are co-optimised deterministically instead of the sequential decisions under uncertainty that happen in reality.
- (p. 6) Water-value comparisons need a longer analysis period and case-specific end-value cuts to limit end effects.
- (p. 6) Conclusion: a capacity market can be added "by a modest extension" of the energy-only model with low added computational burden; the model overestimates profit but gives useful insight.
- (p. 1) Repeats "SDDP seems to be the state-of-the-art method" for long- and medium-term scheduling in hydro-dominated regions.

## Strengths
- Short, clear formulation of reserve capacity in a weekly SDDP subproblem (spinning, capacity and droop constraints).
- Honest self-critique of the overestimation mechanisms, which later papers (hjelmeland2016combined, hjelmeland2016case, helseth2016) each address.
- Good small description of the 2013 Norwegian FCR-N markets with the seasonal volume/price pattern.

## Weaknesses / limitations
- FCR prices deterministic; sequential market clearing not represented (fixed in `helseth2016`).
- No minimum-generation link: reserve ≤ generation lets a station run at 33 MW to sell 33 MW (fixed partly in `helseth2016` with β = max(P_min/R_max, 1), and tested against a MIP simulator in `hjelmeland2016combined`).
- No water-for-reserve constraint; no head effects; no pumping.
- 1-year horizon with fixed end-value cuts (authors flag end effects).
- No out-of-sample test; revenue numbers given only as one % figure.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review (market participation): first SDDP model with energy + FCR capacity | Hybrid SDP/SDDP extension, +2.58 % revenue | pp. 1, 3–5 |
| Limitations: why LP reserve models overestimate | Three reasons: unlimited reserve demand, LP without start/stop, co-optimised within week | pp. 5–6, Sec. IV-B |
| Model: simple reserve constraints | Spinning (4), capacity (5), droop cap (7) | p. 4, Sec. III-C |
| Model: intra-week time steps and reserve blocks | 21 steps, 6 blocks per week | p. 3, Fig. 4 |
| Model: deterministic vs stochastic reserve price | Why reserve prices were kept deterministic (few years of data, changing market design) | p. 3, Sec. III-A |
| Results discussion: reserves shift seasonal water use and water values | Higher reservoirs before spring flood, more use in summer; water values lower before flood, higher summer/autumn | p. 5, Figs. 7–8 |
| Background (electricity markets): Norwegian FCR-N markets 2013, summer volume peak | Weekly vs daily markets, Figs. 1–2 | p. 2, Sec. II |
| Lit review: SDDP is state of the art in hydro-dominated systems | Same sentence as in helseth2016 | p. 1 |

## Useful quotes (with page numbers)
> "stations are allowed to generate electricity at low rates at an artificially high efficiency for the purpose of delivering reserves." (p. 5)

## Follow-up references to check (backward snowballing)
- [11] Gjelsvik, Belsnes, Haugstad (1999), hybrid SDP/SDDP under spot price uncertainty, PSCC (cf. `gjelsvik1999`).
- [15] Mo, Gjelsvik, Grundt, Kåresen (2001), price modelling (= `mo2001`).
- [9] Helseth, Gjelsvik, Mo, Linnet (2013), hydrothermal scheduling with pumped storage and wind, IET GTD (= `helseth2013`).
- [13] Kristiansen (2007), the Nordic approach to market-based provision of ancillary services, Energy Policy 35.
- [14] Statnett (2013), terms for the primary reserve market (Norwegian).

