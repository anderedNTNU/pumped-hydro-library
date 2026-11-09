---
bibkey: kleiven2023
title: "Co-movements between forward prices and resource availability in hydro-dominated electricity markets"
authors: "Andreas Kleiven, Simon Risanger, Stein-Erik Fleten"
year: 2023
venue: "Energy Systems (Springer), online first 2023, doi:10.1007/s12667-023-00605-z"
peer_reviewed: true
methods: [sddp-markov-chain, uncertainty-modelling, sdp]
review_sections: [price-volatility, modelling-phs-plants, research-gap]
relevance: high
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/112_Kleiven_2023_Co_movements_between_forward_prices_and_resource_availability_in_hydro_dominated_electrici.pdf
takeaway: "Joint three-factor price model where Norwegian prices load on the system hydrological state, discretised into a 5-node k-means Markov chain for MC-SDDP (104 weekly stages): ignoring the negative price-inflow correlation underestimates water values (more spill tolerance, higher autumn reservoir) but costs only 0.17-0.30% of expected revenue."
---

# Co-movements between forward prices and inflow (Kleiven, Risanger & Fleten, 2023)

_The PDF is the online-first open-access version (34 pages) with **no journal page numbers**; all page references below are **PDF pages**. If a later issue assigns pages, the offset must be added. The bib entry has no volume/pages (unverified whether an issue version exists)._

## Research question / purpose
Industry practice in medium-term (1–2 years) hydropower scheduling treats price and inflow as **independent** stochastic processes, although in hydro-dominated systems low inflow correlates with high prices (p. 1–2). The paper asks: what is the effect of ignoring the price–inflow co-movement on the optimal release policy and on revenue? Contributions (p. 3): (i) analytical characterisation of the policy effect in a two-stage MDP; (ii) a new additive three-factor price model where forward prices are partly explained by the (local and system) hydrological state; (iii) a risk-neutral version calibrated on futures; (iv) an MC-SDDP case study with industry data.

## Setting
- **System:** single conventional (no pumping) hydropower plant in western Norway, operated by Eviny; the interconnected watercourse is aggregated into one energy-equivalent reservoir (EER) (p. 14). Price-taker.
- **Markets:** energy only (system price / forward-based price model); no reserves, no intraday.
- **Horizon and resolution:** 2 years, 104 weekly stages; only the first year is interpreted to avoid end-of-horizon draining effects (p. 18–19, App. F p. 28). Annual discount rate 2 % (p. 18).

## Method
- **Model type:** Markov decision process (eq. 1–5): reward = price × production; reservoir balance, reservoir capacity R, generation capacity G, free spillage (only opportunity cost) (p. 4–5). Linear, single reservoir, no head effects.
- **Analytical results:** value and continuation functions concave, marginal water value decreasing in storage (Prop. 2.1, p. 6); threshold-type optimal generation policy (Prop. 2.2, p. 6); in a two-stage setting with Cov(price, inflow) < 0 and s0 + inflow < R, the independent model **underestimates the marginal water value** (Prop. 2.3, p. 6) → produce the same or less today, tolerate more spill (p. 6). Proof via E[pξ] = E[p]E[ξ] + Cov, active only when spill risk is non-zero (App. A.3, p. 25).
- **Toy example (Ex. 2.1, Tables 1–3, p. 6–9):** AR(1) price and inflow with correlation −0.5. Independent policy overestimates its value by 1.3 %, but its true loss when simulated on the correlated model is only 0.03 %. First-stage production 15.0 vs 13.2; spill probability 6.8 % vs 9.2 % (Table 2, p. 8). Correlation only matters when current price is below ~30 €/MWh **and** spill probability > 0 (p. 9).
- **How uncertainty is represented:** joint price–inflow model (Sect. 4, p. 12–14):
  - Local inflow: normalised by weekly mean/std (as in Gjelsvik et al. 2010), AR(1) on residuals (eq. 15–16, p. 12). Gaussian chosen over lognormal on empirical fit (App. B, p. 25–26).
  - Local hydrological state = exponentially smoothed inflow deviations (eq. 17).
  - System hydrological state = linear function of local state + AR(1) unobservable factor (eq. 18–19, p. 12).
  - Price (eq. 20–22, p. 13): seasonal cosine term + β·(system hydrological state) + short-term AR(1) deviation χ + long-term equilibrium level ξ as arithmetic Brownian motion with drift. This is an additive, discrete-time extension of the **Schwartz–Smith (2000) two-factor model** with a third, physical (hydrology) factor (p. 3).
  - Risk-neutral version via convenience-yield assumptions (Sect. 4.1, App. C, p. 13–14, 26–27).
- **Calibration (Sect. 5.2, p. 15–18):** futures 1–5 years to maturity 2011–2018 (Montel), local inflow 2009–2018, NVE system reservoir deviation from normal. Six steps: smooth forward curves (Benth et al. 2007 maximum smoothness) and de-seasonalise; fit inflow AR(1); build local hydrology series; jointly fit local→system hydrology (with smoothing = AR coefficient restriction; likelihood surface Fig. 6); regress front-month futures on system hydrology; Kalman filter + ML on hydrology-adjusted residuals. Futures show visibly less variability after adjusting for hydrology (p. 18, Figs. 4b vs 7b). Independent benchmark re-estimated so that conditional means and long-run variance match (App. D, p. 27–28).
- **Markov-chain construction (App. F, Algorithm 1, p. 28–30):** 50,000 weekly Monte Carlo paths of price and inflow; negative inflows set to 0. **Joint k-means clustering on (price, inflow) pairs failed** to reproduce mean, variance and covariance; instead cluster on **standardised price only**, then assign each price cluster a representative inflow = mean of a small random sub-sample (5 samples), de-meaned, variance-scaled by a factor, and re-meaned. Transition probabilities = counts of paths moving cluster→cluster / paths in origin cluster. **5 nodes per stage**. Mean, variance and cross-moment preserved (p. 18).
- **Solution method:** MC-SDDP in Julia, SDDP.jl + Gurobi, average (single) cuts (p. 11, 18). Discussion of why MC-SDDP over TS-SDDP: price in objective as a state creates bilinearity / non-concavity; MC-SDDP is simpler, converges faster and performs well in hydro (citing Löhndorf & Shapiro 2019) but needs a fixed partition of the uncertainty (p. 10–11).
- **Key modelling choices:** EER, constant energy coefficient, head variations ignored because they make subproblems non-convex (p. 14–15). Problem small enough for SDP, but SDDP used for extensibility (p. 15).

## Data / case
Eviny plant in western Norway; base case R ≈ 334,989 MWh, G ≈ 39,439 MWh/week (from Table 5, p. 29, consistent with the sensitivity case where R = G = 106,382 MWh is 32 % of base reservoir and 270 % of base generation capacity, p. 31). Montel futures; NVE hydrological balance data (p. 14, 32).

## Key findings
- (p. 1, 19) Accounting for co-movements makes the producer postpone generation, keep a slightly higher mean reservoir in autumn (weeks ~25–40) and tolerate more spillage (Figs. 8–9).
- (p. 19) Considering correlation reduces reservoir-trajectory variability (fewer low-reservoir trajectories in autumn, when estimated covariance is highest).
- (p. 20, Table 4) Independent-MC policy **overestimates its own value by 2.55 %**; when simulated on the dependent MC it loses only **0.17 %** of expected revenue.
- (p. 21) Negative correlation acts as a **natural hedge**: in low-revenue scenarios the independent model underestimates revenue, in high-revenue scenarios it overestimates (Fig. 11).
- (p. 22, App. G p. 30–32) Sensitivities: stronger hydrology effect and seasonality → loss 0.24 % (Table 6); smaller reservoir / larger turbine (R = G = 4 weeks of mean inflow) → 0.30 % (Table 7). Results "highly case-specific".
- (p. 22) Contradicts Nersten et al. (2018), who found 2.5–3.1 % revenue reductions using a fixed Pearson correlation.
- (p. 2) Industry practice: price/inflow scenarios are produced jointly by a market model (inflow in, price out), but the detailed reservoir optimisation then treats them as independent (citing Wolfgang et al. 2009; Gjelsvik et al. 2010).
- (p. 2) Mo et al. (2001) argued that correlation between accumulated seasonal inflow and price matters more than week-to-week correlation, because of storage capacity.

## Strengths
- Clear analytical intuition (Prop. 2.3) for why correlation matters only when spill risk is non-zero.
- Very transparent, reusable Markov-chain construction algorithm, including an honest account of why joint k-means clustering failed.
- Price model grounded in Nordic fundamentals (system hydrological balance) and calibrated to futures under a risk-neutral measure.
- Policy evaluation by simulating both policies on the same (dependent) chain and reporting revenue distributions.

## Weaknesses / limitations
- Single EER, linear production, no head effects, no pumping, no reserves.
- Evaluation is in-sample with respect to the model (simulation on the dependent Markov chain, not on historical data); the authors note slight node discrepancies between chains (p. 20).
- Only 5 Markov nodes per stage; inflow is attached to price clusters, so inflow variability within a price state is compressed.
- Gaussian inflow can go negative (truncated to 0) (p. 28).
- Calibration period 2011–2018 precedes the 2021–2023 price crisis; hydrology-price link may differ now (our inference, not in paper).
- Table 5 is garbled in the text extraction; parameter values should be read from the PDF.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.5 price volatility/persistence: Nordic prices driven by hydrological state | Low inflow/low reservoirs ↔ high prices, through water values; system hydrology explains part of futures variability | p. 2, p. 18 (Figs. 4b vs 7b), p. 22 Sect. 6 |
| Background 2.5: price persistence modelling | Schwartz–Smith style long-term ABM + short-term AR(1) + hydrology factor; seasonal cosine | Sect. 4, eq. 20–22, p. 13 |
| Method: why MC-SDDP instead of TS-SDDP | Price in objective → bilinear term violates concavity; MC-SDDP simpler, faster, good policies | Sect. 3, p. 10–11 |
| Method: Markov-chain construction by k-means, transition counting | Algorithm 1; 50,000 simulated paths; 5 nodes; cluster on price only | App. F, p. 28–30 |
| Method: warning on joint price–inflow clustering | Joint k-means did not capture variance, mean and covariance | App. F, p. 28 |
| Method: inflow model (normalise + AR(1), Gaussian vs lognormal) | Normalisation by weekly mean/std, AR(1); Gaussian fit preferred | Sect. 4, eq. 15–16, p. 12; App. B |
| Method: price–inflow correlation in the state | Value of including correlation small (0.17–0.30 % revenue) but water values underestimated if ignored | Table 4 p. 20; Tables 6–7 p. 31–32 |
| Method: end-of-horizon effects | 2-year horizon, only first year interpreted | p. 18–19 |
| Lit. review 5.3 modelling: SDDP hydro with stochastic prices | Price-taker MC-SDDP with EER, no head effects | Sect. 3, 5 |
| Lit. review 5.6 research gap | Correlation value depends on spill risk/reservoir-to-inflow ratio; untested for PHS | p. 21–22 |
| Industry practice statement | Price/inflow treated as independent in operational policies 1–2 years ahead | Abstract p. 1; p. 2 |

## Useful quotes (with page numbers)
> "producers underestimate their water value when they ignore co-movements between price and inflow" (p. 1, abstract)

> "A joint clustering on price and inflow pairs created a Markov chain that did not capture the variance, mean, and covariance of the underlying stochastic model." (p. 28)

> "MC-SDDP implementation is less complex, it converges faster, and it has been shown to provide policies that perform well when applied to hydropower planning" (p. 11)

## Follow-up references to check (backward snowballing)
- Nersten, Dimoski, Fleten et al. (2018), IAEE conference: multi-factor price model with fixed price–local inflow correlation; 2.5–3.1 % revenue impact (ref. [32]).
- Mo, Gjelsvik & Grundt (2001), IEEE TPWRS: accumulated-inflow vs price correlation (ref. [30]; in our library as `mo2001`).
- Schwartz & Smith (2000), Management Science: two-factor commodity price model (ref. [40]).
- Benth, Koekkebakker & Ollmar (2007): smooth forward curves (ref. [5]).
- Wolfgang et al. (2009), Energy: Norwegian reservoir handling before/after deregulation (ref. [45]).
- Downward, Dowson & Baucke (2020): SDDP with stagewise-dependent objective uncertainty (saddle functions) (ref. [11]).
- Lucia & Schwartz (2002): Nordic electricity price dynamics (ref. [27]).
- Suomalainen et al. (2015): hydro/wind correlation with prices in New Zealand (ref. [43]).

