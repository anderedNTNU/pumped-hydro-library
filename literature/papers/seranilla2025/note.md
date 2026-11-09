---
bibkey: seranilla2025
title: "A Survey on the Applications of Stochastic Dual Dynamic Programming and its Variants"
authors: "Bonn Kleiford Seranilla, Nils Löhndorf"
year: 2025
venue: "Optimization Online preprint (2025)"
peer_reviewed: false
methods: [sddp-markov-chain, sddp-time-series, benders-decomposition]
review_sections: [modelling-phs-plants, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Systematic survey of 186 SDDP application papers (1991-2022): ~76% energy, ~60% hydro-thermal scheduling (Brazil dominant, Norway mostly medium-term); storage applications are recent and few; adoption limited by history, state-space size, stagewise independence (MC approach said to lack convergence guarantees) and data availability."
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/Innlimte_referanser_2026-10-29/seranilla2025.pdf"
---

# Survey of SDDP applications (Seranilla and Löhndorf, 2025)

_Page mapping: 24 PDF pages; printed page numbers at the page foot equal PDF page numbers (p. 1 unnumbered). Pages 1-13 main text, 14-15 appendix tables, 16-24 references._

_Relation to the thesis version: this preprint is essentially Chapter 2 of Seranilla's PhD thesis (`seranilla2023applications`, thesis pp. 27-54), same search (to December 2022), same 186 papers and same discussion. Cite this preprint (co-authored with Löhndorf) for the survey; cite the thesis only for its Ch. 1 tutorial or Ch. 3 MSPLib benchmark._

_Tagging note: `sddp-markov-chain` and `sddp-time-series` because the survey discusses both ways of handling stagewise dependence (Löhndorf and Shapiro 2019) and their limits (pp. 3, 12). `benders-decomposition` for the history section (pp. 2-3). `modelling-phs-plants` and `research-gap` because it maps where SDDP has been applied (hydro-thermal, storage) and shows storage/market applications are a recent minority._

## Research question / purpose
- Comprehensive survey of SDDP in practical applications: identify domains where SDDP has been used for MSP problems affected by the curse of dimensionality, and the factors that facilitated or hindered its adoption (abstract, p. 1; goals, p. 2).
- Three survey questions: in which problems and sectors SDDP is used; the research's contribution (theoretical, methodological, other); how valuable SDDP is for the problem (p. 4).

## Setting
- **System:** literature on SDDP applications (energy, finance, operations management, water, disaster management, mining).
- **Markets:** energy markets/trading section (pp. 8-9).
- **Horizon and resolution:** hydro-thermal planning classified as long-term (≥3 years, monthly stages), medium-term (1-2 years, weekly or monthly) and short-term (hours to days) (p. 6).

## Method
- **Model type:** systematic literature survey.
- **Search:** Emerald Insight, Scopus, JSTOR, Web of Science; journal articles up to December 2022; keywords "stochastic dual dynamic programming", "SDDP", "stochastic dual dynamic integer programming", "SDDiP"; non-English, conference-only and book chapters excluded; title, then abstract, then intro/conclusion, then full-text screening (pp. 3-4). Result: 186 publications in 61 journals (p. 4, Table 1 p. 5).
- **Also:** informal interviews with researchers at ICSP 2023 informed the discussion (pp. 11, 13).
- **Background section:** Benders (1962), L-shaped (Van Slyke and Wets 1969), nested Benders (Birge 1985), SDDP and extensions incl. stagewise dependence, risk aversion and SDDiP (pp. 2-3).

## Data / case
- 186 papers. Journal counts: EJOR 19, IEEE TPWRS 14, Math. Programming 10, IEEE TSTE 9, J. Water Resour. Plan. Manage. 9, IJEPES 9, SIAM J. Optim. 9, EPSR 7, WRR 7, CMS 7, others 43 (Table 1, p. 5).

## Key findings
- (p. 1) SDDP is "widely recognized as the predominant methodology" for large-scale multistage stochastic linear programs.
- (p. 3) Vanilla SDDP assumes stagewise independence; Löhndorf and Shapiro (2019) give two ways around it: autoregressive time series via extra state variables, and Markov-chain discretisation. Guigues and Römisch (2012a,b) and Shapiro et al. (2013) are the first risk-averse SDDP papers. SDDiP (Zou et al. 2019) needs discrete uncertainty and binarised state variables.
- (p. 4) Energy dominates; the Brazilian hydro-thermal system is the primary focus; secondary lines are finance and operations management.
- (p. 6) Over 100 publications address the hydro-thermal production problem with SDDP; variations come from horizon, uncertainty process and geography (Figs. 3-4).
- (pp. 6-7) Long-term planning focuses on inflow uncertainty (historical sampling, autoregressive models, non-linearities); some include demand uncertainty.
- (p. 7) End-of-horizon effect: optimal policies tend to empty reservoirs at the horizon end; "most works" double the planning horizon (e.g. 10 instead of 5 years) to hedge against this (no citation given).
- (p. 7) Medium-term planning often includes price and cost uncertainty so producers can trade optimally; examples: Kristiansen (2006), Löhndorf et al. (2013), de Matos et al. (2015), Helseth et al. (2016), Rebennack (2016), Hjelmeland et al. (2018, 2019), Borges et al. (2022).
- (p. 8) Short-term economic dispatch with reserves (Lu et al. 2019) and ancillary services (Street et al. 2017).
- (pp. 8-9) Energy markets/trading: Bonnans et al. (2012) energy contracts; Bruno et al. (2016) real options; Wozabal and Rameseder (2020) and Shinde et al. (2022) day-ahead and intraday bidding of virtual power plants; Steeger and Rebennack (2017) price-maker bidding; Löhndorf and Wozabal (2021) gas storage; Scheben et al. (2020) on how storage and renewables affect price structures (Norway case).
- (p. 9) Energy storage: MSP for storage is "relatively recent"; distributed storage first addressed by Gangammanavar and Sen (2016); then grid storage, microgrids, batteries (degradation), gas storage, and hydro storage with batteries (Alvarez et al. 2017). Pumped hydro is named as a storage type but no PHS-specific SDDP paper is singled out.
- (p. 11) Until 2016 all energy-sector SDDP papers addressed hydro-thermal scheduling; this history created the perception that SDDP is only for energy.
- (p. 11) State-space limitation: efficiency drops with many state variables; the Brazilian flagship case had only 4 state variables per stage (the reservoir energy levels).
- (p. 12) Stagewise-independence limitation: many economic and natural processes are Markovian; the AR approach is restricted to right-hand-side uncertainty and linear cases, and the Markov-chain approach, "although allows modeling any parameter as Markovian data process, has no convergence guarantees".
- (p. 12) Data availability limits accurate uncertainty modelling and hence adoption.
- (p. 13) Energy ≈ 76% of articles; hydro-thermal production ≈ 60%, followed by renewables, markets/trading/investments, storage, and grid management.
- (p. 14, Table 2) Norway: long-term Rotting and Gjelsvik (1992); medium-term Mo et al. (2001), Kristiansen (2006), Helseth and Braaten (2015), Helseth et al. (2016), Hjelmeland et al. (2018, 2019), Scheben et al. (2020), Helseth and Mo (2022), Helseth et al. (2022); no Norwegian short-term entries.

## Strengths
- Only systematic, quantitative map of SDDP applications; co-authored by a leading MC-SDDP author (Löhndorf).
- Useful classification tables by country and horizon (pp. 14-15) for snowballing Nordic hydro SDDP papers.
- Clear statement of the four adoption barriers, including stagewise dependence and data availability (pp. 11-12).

## Weaknesses / limitations
- Preprint, not peer reviewed; literature cut-off December 2022 although dated 2025.
- Mostly descriptive listing; little critical comparison of modelling choices or results.
- Some technical statements are loose or wrong: Benders is described as splitting into a "pure linear" master and "pure integer" subproblem (p. 2), which is the reverse of the usual MILP setup (the thesis version, p. 12, has it right); "with a few iterations, the upper and lower bounds converge" (p. 3) overstates practical convergence.
- The claim that the Markov-chain approach "has no convergence guarantees" (p. 12) is stated without reference; check against Philpott and de Matos (2012) and Löhndorf and Shapiro (2019) before repeating it.
- End-of-horizon "doubling" claim (p. 7) unsupported by citations.
- Few PHS-specific or reserve-market SDDP papers identified.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Theory 3 (SDDP): SDDP as predominant MSLP method; history Benders → L-shaped → nested Benders → SDDP | Background Sec. 2.1-2.2 | pp. 1-3 |
| Theory 3 (Representation of Uncertainty in SDDP): AR vs Markov-chain approaches and their limits | Sec. 2.2 and 5.3 | pp. 3, 12 |
| Theory 3 (Terminal Value Functions): end-of-horizon effect | Sec. 4.1.1 | p. 7 |
| Literature review (modelling of PHS plants): horizon classes for hydro planning | long/medium/short definitions | p. 6 |
| Literature review: medium-term hydro SDDP with price uncertainty (incl. Norwegian SINTEF work) | Lists of papers | p. 7; Table 2 p. 14 |
| Literature review (market participation): SDDP for bidding and trading | Sec. 4.1.3 | pp. 8-9 |
| Literature review / research gap: storage applications of SDDP are recent and few | Sec. 4.1.4; share statistics | pp. 9, 13 |
| Research gap / limitations: barriers to SDDP adoption (state space, dependence, data) | Sec. 5 | pp. 11-12 |
| Snowballing: Norwegian and other hydro SDDP papers by horizon | Tables 2-3 | pp. 14-15 |

## Useful quotes (with page numbers)
> "the second approach, although allows modeling any parameter as Markovian data process, has no convergence guarantees" (p. 12)

Paraphrased: from 1991 until 2016 all published energy-sector works using SDDP were centred on the hydro-thermal scheduling problem (p. 11); energy accounts for about 76% and hydro-thermal production for about 60% of the surveyed works (p. 13).

## Follow-up references to check (backward snowballing)
- Löhndorf, Wozabal and Minner (2013). Optimizing trading decisions for hydro storage systems using ADDP. Operations Research 61.
- Helseth and Braaten (2015); Helseth et al. (2016); Hjelmeland et al. (2018, 2019); Helseth and Mo (2022); Helseth et al. (2022) (Norwegian medium-term hydro SDDP; several in inbox `09_.../SDDP_i_vannkraft`).
- Wozabal and Rameseder (2020). Optimal bidding of a virtual power plant on the Spanish day-ahead and intraday market. EJOR (unverified title).
- Shinde et al. (2022). Day-ahead and intraday bidding with SDDP (unverified details).
- Löhndorf and Wozabal (2021). Gas storage valuation in incomplete markets. EJOR 288.
- Gangammanavar and Sen (2016). Distributed storage with MSP.
- Alvarez et al. (2017). A generic storage model based on a future cost piecewise-linear approximation. IEEE TSG.
- Scheben et al. (2020). Impact of inflow randomness, storage and renewables on prices (Norway case) (unverified details).
- Füllner and Rebennack (2021 preprint; in repo as `fullnerRebennack2025`).
- Abgottspon et al. (2014) risk-averse medium-term hydro with spinning reserves (cited in the thesis version's bibliography; in repo: `abgottspon2014`).

