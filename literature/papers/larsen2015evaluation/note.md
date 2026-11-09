---
bibkey: larsen2015evaluation
bibkey_provisional: true
title: "Evaluation of scenario reduction methods for stochastic inflow in hydro scheduling models"
authors: "Camilla Thorrud Larsen, Gerard L. Doorman, Birger Mo"
year: 2015
venue: "2015 IEEE Eindhoven PowerTech, doi:10.1109/PTC.2015.7232819"
peer_reviewed: true
methods: [sddp-time-series, uncertainty-modelling]
review_sections: [modelling-phs-plants]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/06_Hydrologi_statistikk_og_data/31_Larsen_2015_Evaluation_of_scenario_reduction_methods_for_stochastic_inflow_in_hydro_scheduling.pdf
takeaway: "Compares fast forward selection, k-means and bracket-mean discretisation of the AR(1) inflow-noise distribution (K = 3, 7) for SDDP on the Tokke system: out-of-sample, k-means is clearly worst (−9.5 MNOK at K = 3) and most sensitive to K, and the gap widens with more variable prices."
---

# Scenario reduction for stochastic inflow in SDDP (Larsen, Doorman & Mo, 2015)

_6-page IEEE PowerTech conference paper. The PDF carries no proceedings page numbers; page references are **PDF pages 1–6**. Not in `references.bib`: provisional key. The venue (Eindhoven PowerTech 2015) is inferred from the DOI `PTC.2015.7232819` (unverified in the PDF itself)._

## Research question / purpose
How does the choice of scenario-reduction method used to discretise the inflow noise for SDDP affect the quality of the resulting hydro scheduling policy, measured by out-of-sample simulation (p. 1–2)? Three methods compared: fast forward selection (FFS, Kantorovich distance; Dupačová et al. 2003, Heitsch & Römisch 2003), k-means clustering, and the "bracket mean" method (Høyland & Wallace 2001) (p. 1–2). The paper stresses that scenario quality should be judged on the optimisation outcome, not only on statistics (p. 2, citing Kaut & Wallace).

## Setting
- **System:** modified Tokke system, southern Norway: 7 interconnected reservoirs and plants, 986 MW installed (p. 4). Conventional hydro (no pumping in the described model).
- **Markets:** day-ahead only; price-taker; **deterministic** exogenous weekly price (Nord Pool NO1 2014 weekly averages, plus a variance-inflated version with the same annual mean) (p. 5, Fig. 4).
- **Horizon and resolution:** 1 year, weekly decisions, starting first week of January (p. 5).

## Method
- **Model type:** multistage stochastic LP, revenue maximisation minus penalty for reservoir-bound violations; water balance, reservoir and discharge bounds (p. 5).
- **How uncertainty is represented:** univariate inflow series ("Eggedal", NVE, 1958–2013, 2912 weekly observations) deseasonalised by subtracting weekly mean and dividing by weekly std, then AR(1) (eq. 1–2, p. 3). The AR(1) noise is stagewise independent, so two-stage reduction methods apply per stage; the noise empirical distribution (right-skewed, non-normal) is the original scenario set; it is reduced to K = 3 or K = 7 discrete outcomes, and a full scenario tree arises by evolving the AR model with these outcomes each stage (p. 3–4).
- **Scenario-reduction methods (p. 3–4):** FFS: greedy selection minimising Kantorovich distance, deleted scenarios' probability reassigned to nearest kept one. K-means (squared Euclidean; centres inherit cluster probability N_k/N). Bracket mean: sort, split into K equal-count intervals, take interval means, probability 1/K.
- **Solution method:** SDDP in C++ with "selective sampling" (Penna et al. 2011): forward scenarios sampled from the full tree (100 per pass, resampled each iteration), backward openings = K; stopped after 15 iterations when the upper bound stabilised (p. 2, 5). The paper notes that a stochastic price would require the hybrid SDP/SDDP approach of Gjelsvik et al. 2010 (p. 5).
- **Evaluation:** out-of-sample simulation on 1000 exogenous inflow scenarios generated from the estimated AR model by sampling from the original noise set (p. 5).

## Data / case
Tokke system (986 MW), Eggedal inflow series 1958–2013 from NVE, Nord Pool NO1 2014 weekly prices (p. 4–5).

## Key findings
- (p. 4, Table I) Original noise: mean 0, std 0.789, skewness 2.029. K = 3: FFS std 0.510, k-means 0.684, B-mean 0.568; K = 7: 0.694 / 0.764 / 0.692. K-means best preserves std but strongly overstates skewness (15.6 at K = 3, 13.6 at K = 7). FFS slightly biases the mean at K = 3.
- (p. 5, Table II, original prices, MNOK) K = 3: FFS 1298.79, k-means 1289.29, B-mean 1298.47; K = 7: 1297.85, 1297.47, 1298.68. Only k-means at K = 3 is noticeably worse.
- (p. 5–6, Table III, variance-inflated prices) K = 3: 1392.39 / 1378.42 / 1392.29; K = 7: 1392.03 / 1388.68 / 1390.78. The k-means gap grows when prices are more variable, "since the potential benefits of a more efficient use of the available water will increase with increasing price variations" (p. 6).
- (p. 6) Differences of ~1.6 MNOK are within sampling error (re-running with a new out-of-sample set reversed the B-mean K = 3 vs K = 7 ordering).
- (p. 6) Conclusion: no unanimous winner; FFS and B-mean perform similarly; k-means "substantially worse" and much more sensitive to K for this problem.
- (p. 1) Long-term models usually favour uncertainty representation over technical detail.
- (p. 2) Multivariate processes are commonly handled by PCA and all-against-all combination of per-component scenarios.

## Strengths
- Clean, controlled comparison: same original scenario set, same SDDP, same out-of-sample set; evaluation by policy performance rather than statistics only.
- Realistic Norwegian multi-reservoir system and long NVE inflow record.
- Shows interaction between price variability and the cost of a poor inflow discretisation.

## Weaknesses / limitations
- Deterministic price; univariate inflow; only K = 3 and 7; only 15 SDDP iterations; single test system and single out-of-sample set (acknowledged sampling error, p. 6).
- K-means is applied to a 1-D noise distribution where its centroid placement over-weights the tail (high skewness); the result may not transfer to clustering of multivariate weekly profiles.
- Short conference paper: few details on k-means initialisation (k-means++ cited) and on convergence/gap.
- Inflow uncertainty only; no Markov chain.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Method: inflow model (weekly standardisation + AR(1), Nordic practice) | Equations and justification | Sect. III-A, eq. 1–2, p. 2–3 |
| Method: number of clusters / discretisation quality | K-means worst at K = 3, sensitive to K; FFS, bracket mean robust | Tables II–III, p. 5–6 |
| Method: out-of-sample policy evaluation design | 1000 exogenous inflow scenarios, same for all cases | p. 5 |
| Method: moment preservation of discretisations | Mean/std/skewness table for K = 3, 7 | Table I, p. 4 |
| Lit. review 5.3: SDDP for Norwegian hydro with inflow uncertainty | SDDP with selective sampling, Tokke case | Sect. II, p. 2; Sect. IV, p. 4–5 |
| Argument: value of good uncertainty representation rises with price volatility | Gap widens with variance-inflated prices | p. 5–6 |
| Background: long-term models prioritise uncertainty over technical detail | Statement citing Fosso et al. 1999 | p. 1 |

## Useful quotes (with page numbers)
> "the K-means method is not appropriate compared to the other scenario reduction methods for this hydro scheduling problem." (p. 6)

> "The quality of the scenario reduction method should be measured in terms of the solution to the underlying optimization problem" (p. 2)

## Follow-up references to check (backward snowballing)
- Latorre, Cerisola & Ramos (2007), EJOR 181(3): clustering algorithms for scenario-tree generation of hydro inflows (ref. [9]).
- Penna, Maceira & Damázio (2011), PSCC: selective sampling for SDDP (ref. [12]).
- Høyland & Wallace (2001), Management Science: scenario trees by moment matching / bracket mean (ref. [15]).
- Kaut & Wallace (2007), Pacific J. Optim.: evaluation of scenario-generation methods (ref. [16]).
- Heitsch & Römisch (2003); Dupačová, Gröwe-Kuska & Römisch (2003): probability-metric scenario reduction (refs. [6]–[7]).
- Homem-de-Mello, de Matos & Finardi (2011), Energy Systems: sampling strategies and stopping criteria in SDDP (ref. [11]).
- de Oliveira et al. (2010): optimal scenario tree reduction for streamflows (ref. [8]).

