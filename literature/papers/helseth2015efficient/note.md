---
bibkey: helseth2015efficient
bibkey_provisional: true
title: "Efficient parallelization of the stochastic dual dynamic programming algorithm applied to hydropower scheduling"
authors: "Arild Helseth, Hallvard Braaten"
year: 2015
venue: "Energies 8(12), 14287-14297"
peer_reviewed: true
methods: [sddp-time-series]
review_sections: []
relevance: medium
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/09_Metode_og_pumpekraft_utvalg/SDDP_i_vannkraft/HelsethBraaten2015.pdf"
takeaway: "Parallel SDDP for Norwegian long-term hydro scheduling (Nea-Nidelva, 12 plants, 156 weekly stages with 7 sub-periods, VAR(1) inflow): relaxing the stage-wise synchronisation in the backward pass (wait for only N_W of the cuts) keeps parallel efficiency high with only a modest increase in iterations; also documents Nordic practice of 3-5 year horizons with weekly stochastic resolution."
---

# Efficient parallelization of SDDP for hydropower (Helseth & Braaten, 2015)

_Version filed: published open-access version (Energies, CC-BY). **Journal page = PDF page + 14286** (PDF p. 1 = p. 14287). A stray "Version December 4, 2015 submitted to Energies" header appears in the text layer on p. 14293, but the file is the typeset published article._

_Tagging note: `sddp-time-series` because inflow is a first-order vector autoregressive model of normalised inflows inside SDDP with cut sharing (pp. 14289-14290). No review section: conventional (not pumped) hydro, a parallel-computing paper; useful as background on Nordic SDDP practice._

## Research question / purpose
- Present a parallel SDDP scheme for long-term hydropower scheduling (LTHS) in which the stage-wise synchronisation point of the backward iteration is partially relaxed, and test it on a realistic Norwegian watercourse (abstract, p. 14287; p. 14288).

## Setting
- **System:** Nea-Nidelva watercourse, Norway: 12 hydro plants with upstream reservoirs, 536 MW in total; reservoirs from annual to weekly storage (p. 14293). Simplified as an isolated system with thermal supply in 70 cost steps serving a time-varying load, tuned to give reasonable prices and reservoir trajectories (p. 14293). (In a liberalised market the watercourse would normally be scheduled against exogenous stochastic prices, citing Gjelsvik et al. 1999 (p. 14293).)
- **Markets:** none modelled (system cost minimisation).
- **Horizon and resolution:** **156 weeks**, weekly stochastic resolution, **7 sub-periods per week** (p. 14293). General statement: "A typical scheduling horizon used by players in the Nordic power market is 3-5 years, using a stochastic time-resolution of one week" (p. 14288).

## Method
- **Model type:** linear (piecewise linear) multistage stochastic LP; minimise expected cost minus end-of-horizon water value Phi(v_T) (eq. 1, p. 14288); weekly LP (eqs. 2-8) with cuts in reservoir volumes and normalised inflow (eq. 6, p. 14289).
- **How uncertainty is represented:** only inflow; physical inflow normalised by weekly mean and standard deviation to remove seasonality (eq. 9), then a first-order VAR model z_t = Phi_t z_{t-1} + eps_t fitted on 50 years of history (pp. 14289-14290, 14293). Negative inflows can occur and are not truncated (to preserve convexity); compensated with high-cost artificial variables (p. 14290). Within a week, inflows are known at the start of the week (p. 14288).
- **Solution method:** SDDP; forward iteration over N_S sampled scenarios gives upper bound J+ (sample mean) and lower bound J- (first-stage value) (eqs. 10-11, p. 14291); backward iteration solves N_B inflow realisations per state and averages into a cut, shared across all states via the linear inflow model (cut sharing) (p. 14291). Convergence declared when LB is inside the 95% CI of the UB (p. 14291). Relatively complete recourse via penalty variables (p. 14289).
- **Parallel scheme (Sec. 3):** master-slave; forward iteration parallel over scenarios (no speed-up beyond N_P = N_S) (p. 14291); in the backward iteration one processor solves all N_B realisations from one state to exploit warm starts (p. 14292); each processor waits only for N_W <= N_S cuts at the next stage before moving backwards (N_W = 1 fully relaxed) - mathematically allowed by Philpott & Guan (2008) (p. 14292).
- **Implementation:** C++, COIN-OR dual simplex, OpenMPI; Linux cluster of 93 nodes, 2 x 6-core AMD at 2.4 GHz (pp. 14292-14293).
- **Key modelling choices and assumptions:** linear models, no head effects discussed, end value Phi(v_T) assumed given.

## Data / case
- 50 years of historical inflow (Fig. 3, p. 14293). LPs average 777 variables and 98 constraints excluding cuts (p. 14293).
- Case 1: N_S = 71, N_B = 12, up to 72 processors, serial time 1 h 10 min. Case 2: N_S = 200, N_B = 50, up to 144 processors, serial 5 h 3 min (Table 1, p. 14294).

## Key findings
- (p. 14294, Fig. 4) LP solve times per processor and stage vary widely (outliers vs quartiles), so full synchronisation wastes processor time.
- (pp. 14294-14295, Figs. 5-6) With full synchronisation, parallel efficiency falls as processors increase; partial relaxation keeps efficiency higher; the best N_W is case dependent; N_W = 1 at maximum processors loses efficiency because convergence slows.
- (p. 14296, Fig. 7) Lower N_W needs more iterations, but the extra iterations were modest.
- (p. 14296) Expected schedules should be unaffected, so the benefit is purely computational; case is simplified relative to operational models.

## Strengths
- Real Norwegian watercourse; clear description of a standard Nordic SDDP formulation (weekly stages, sub-periods, VAR(1) inflow, cut sharing).
- Simple idea with measured efficiency gains, averaged over 10 runs.

## Weaknesses / limitations
- Isolated thermal-supplied system instead of a price-taking producer (p. 14293).
- Only inflow uncertainty; no price uncertainty, no reserves, no pumping.
- Computational paper: no economic results; only two test cases.

## Use it for... (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Model: weekly stages, uncertainty known at start of week, sub-periods within week | Nordic practice statement; 7 sub-periods per week | p. 14288 (Sec. 2.1); p. 14293 |
| Model / case: horizon length (3-5 years in Nordic practice; 156 weeks) | Typical horizon; case horizon | p. 14288; p. 14293 |
| Theory: SDDP with VAR(1) inflow and cut sharing (TS-SDDP contrast to MC-SDDP) | Normalised inflow, VAR(1), cut coefficients for inflow state, negative inflow treatment | Secs. 2.3-2.4, pp. 14289-14291 |
| Method: stopping rule (LB inside 95% CI of UB) | Standard test as used in practice | p. 14291 |
| Method: parallelisation of SDDP | Relaxed backward synchronisation; warm starts per processor | Sec. 3, pp. 14291-14292; results pp. 14294-14296 |
| Background: SDDP as state of the art for hydro-dominated LTHS; SDP models used by Nordic market participants | Statements with references | pp. 14287-14288 |

## Useful quotes (with page numbers)
> "A typical scheduling horizon used by players in the Nordic power market is 3-5 years, using a stochastic time-resolution of one week." (p. 14288)

## Follow-up references to check (backward snowballing)
- Pinto, Borges & Maceira (2013), efficient parallel SDDP for hydrothermal planning (IEEE TPWRS 28).
- Wolfgang et al. (2009), Norwegian reservoir handling before/after deregulation (Energy 34).
- Gjelsvik, Mo & Haugstad (2010), `gjelsvik2010` in our bib.
- Helseth et al. (2013), `helseth2013` (pumped storage and wind in SDDP).
- de Matos & Finardi (2012), negative inflows in SDDP.

