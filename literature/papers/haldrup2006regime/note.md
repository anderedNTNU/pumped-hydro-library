---
bibkey: haldrup2006regime
bibkey_provisional: true
title: "A regime switching long memory model for electricity prices"
authors: "Niels Haldrup, Morten Ørregaard Nielsen"
year: 2006
venue: "Journal of Econometrics 135(1-2), 349-376 (2006). PDF filed here = Aarhus University Dept. of Economics Working Paper No. 2004-02 (1 April 2004)"
peer_reviewed: true
methods: [uncertainty-modelling]
review_sections: [price-volatility, electricity-markets]
relevance: medium
read_by: []
added: 2026-11-04
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/11_Web_search_2026-11-04/haldrup2006regime.pdf
takeaway: "Hourly Nord Pool area prices 2000-2003 are highly persistent but mean-reverting (AR roots 0.99, unit root and I(0) both rejected; fractional d = 0.41-0.52, highest in Norway, linked to hydro reservoirs); a Markov-switching SARFIMA with observable congestion/non-congestion regimes (persistent states, mean durations 5-77 h) fits far better than a single-regime model."
---

# Regime-switching long-memory model for Nordic electricity prices (Haldrup & Nielsen, 2006)

_**Version warning:** the PDF is the **2004 working paper** (Aarhus WP 2004-02, 33 PDF pages), not the J. Econometrics 2006 article (135(1–2), 349–376; citation confirmed by ref. [15] in `boomsma2014bidding`). Page numbers below are the **working-paper printed page numbers** (printed page = PDF page − 2). The published version may differ in content and numbering; get the journal PDF before citing page numbers. Table 5 is garbled in the text extraction; only values restated in the text are used._

## Research question / purpose
Develop a **Markov regime-switching model that allows long memory (fractional integration) within each regime**, motivated by Nord Pool: when there is no transmission congestion, bilateral area prices are identical; with congestion they differ. The paper asks whether regime switching and long memory co-exist in Nordic prices, how ignoring regimes biases inference on (fractional) cointegration, and whether the switching model forecasts better (abstract, p. 1; pp. 2–3).

## Setting
- **System:** Nord Pool day-ahead (Elspot) area prices: Mid Norway (MNO), South Norway (SNO), West Denmark (WDK), East Denmark (EDK), Sweden (SWE), Finland (FIN) (p. 6).
- **Markets:** day-ahead spot only (p. 5).
- **Horizon and resolution:** hourly prices 3 Jan 2000 – 25 Oct 2003, 33,308 observations (EDK from 29 Sep 2000, 26,828) (p. 6). Forecasts 1–24 h ahead (p. 14).

## Method
- **Model type:** econometric time-series model.
- **Baseline (eq. 1, p. 7–8):** multiplicative seasonal ARFIMA (SARFIMA): A(L)(1 − aL²⁴)(1 − L)^d (y_t − μ) = ε_t, with an 8th-order AR polynomial (within-day), a daily quasi-difference, after removing deterministic hour-of-day, day-of-week and month-of-year dummies. Chosen over longer AR lags and weekly stochastic seasonality on fit and residual whiteness.
- **Regime-switching model RS-SARFIMA (eq. 2–3, p. 10):** all parameters (including d, seasonal dummies, variance) differ by regime s_t ∈ {0 = non-congestion, 1 = congestion}; s_t follows a two-state **Markov chain** with transition matrix P = [[p00, 1−p00],[1−p11, p11]]. Because identical prices define non-congestion, the **regime is observable** (not latent as in Hamilton 1989), so transition probabilities are estimated by **counting transitions**: p̂00 = n00/(n00+n01), p̂11 = n11/(n10+n11) (eq. 4–5, p. 10). For log relative prices, regime 0 is deterministic (zero).
- **Estimation:** conditional ML (eq. 6, p. 10), in Ox; LR test of switching vs non-switching, χ² with 12 df (p. 11–12).
- **Forecasting (Sect. 5, p. 14):** Monte Carlo simulation 24 h ahead, 1,000 replications, median and 95 % bands; last 24 h held out.

## Data / case
Nord Pool hourly area prices (see Setting). In 2001, a single Nordic price held **52 %** of the time and two price areas **30 %** of the time (p. 6). Norway is almost 100 % hydro; Nordic supply 55 % hydro, 24 % nuclear, 20 % thermal/CHP (p. 4, fn. 2).

## Key findings
- (p. 4) Mechanism: with adequate reservoirs, cheap hydro lowers prices and transmission is used to capacity; with low reservoirs, net flow is south→north and prices are high (thermal).
- (p. 6) Prices show "huge fluctuations and outliers" but the general level is "highly persistent possibly with mean reversion"; jumps arise because storage of electricity is difficult and from congestion switches (p. 6–7).
- (p. 7, Table 2) **ADF rejects a unit root for all series although AR roots are 0.988–0.996** (WDK 0.910); KPSS also strongly rejects I(0) → neither I(1) nor I(0) fits; "high persistence but mean reversion".
- (p. 8, Table 3) Fractional d (SARFIMA): EDK 0.41, WDK 0.31, SWE 0.44, FIN 0.41, **SNO 0.52, MNO 0.52** → long memory, borderline non-stationary, mean-reverting. Norway highest; explained by hydro: river flows and reservoirs exhibit long memory (Hurst 1951, 1956) (p. 8).
- (p. 8) Within-year persistence is partly seasonal variation from hydro reservoir levels; strong hour-of-day and day-of-week seasonality; ACF of SNO log prices decays slowly over 4 weeks (672 lags) (Fig. 2).
- (p. 11, Table 4) Both regimes are persistent: p̂00 = 0.873–0.987 (mean non-congestion duration **7.9–76.6 h**), p̂11 = 0.785–0.898 (mean congestion duration **4.7–9.8 h**); non-congestion more persistent. E.g. SNO–SWE p00 = 0.953, p11 = 0.898 (21.2 h / 9.8 h); WDK–SNO 0.877 / 0.888.
- (p. 12–14) Ignoring regimes gives misleading (fractional) cointegration inference in two directions: spurious cointegration (EDK–SWE: relative-price d = 0.05 in non-switching model, but cointegration only in regime 0) or missed cointegration (WDK–SWE). Non-switching estimates are a "convex combination" of regime behaviour (p. 13).
- (p. 13–14) LR tests 144–6528 vs 1 % critical value 26.22: regime switching overwhelmingly significant.
- (p. 15–17) Out of sample: similar median forecasts for single prices; switching model has more density concentrated around the outcome one step ahead; clearly superior for relative prices, especially when the sample ends in the more persistent regime 0 (p. 16–17).
- (p. 17) Suggested extensions: multiple regimes/price areas; transition probabilities depending on weather, flows; volatility models with regime switching and long memory.

## Strengths
- Empirically careful (unit root + KPSS + fractional d), Nordic, hourly, multiple areas.
- Observable Markov regimes estimated by transition counting, conceptually close to how we estimate transition probabilities between clustered states.
- Links long memory in Nordic prices explicitly to hydro reservoir dynamics.

## Weaknesses / limitations
- Regimes are **congestion states at hourly scale**, not price-level or hydrological regimes at weekly scale; persistence of hours to days, not seasons.
- Old sample (2000–2003) before market coupling, large-scale wind/solar and the 2021–2023 crisis.
- Mean (first moment) only; volatility not modelled (p. 3, 17).
- Working-paper version; journal version may differ.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.5: Nordic prices persistent but mean-reverting | AR roots ≈ 0.99, ADF and KPSS both reject; "high persistence but mean reversion" | Table 2, p. 7 |
| Background 2.5: long memory linked to hydro | d = 0.41–0.52, highest for Norway; Hurst reservoirs argument | Table 3, p. 8 |
| Background 2.5: seasonality (hourly, weekly, yearly) | Strong hour/day seasonality; within-year persistence from reservoir levels | p. 8, Fig. 2 |
| Background 2.5: jumps/spikes and storage difficulty | Huge fluctuations, outliers; jumps since electricity storage is difficult | p. 6–7 |
| Method: Markov-chain price states justified | Markov-switching regimes significant (LR 144–6528) and persistent | Table 4 p. 11; pp. 13–14 |
| Method: transition-probability estimation by counting | p̂ij = nij / Σ nij for observable states | eq. 4–5, p. 10 |
| Background 2.4: bidding zones and congestion | Single Nordic price 52 % of hours in 2001; area prices diverge with congestion | pp. 5–6 |

## Useful quotes (with page numbers)
> "the general level of these series tend to be highly persistent possibly with mean reversion" (p. 6, WP version)

## Follow-up references to check (backward snowballing)
- Lucia & Schwartz (2001/2002), Review of Derivatives Research: Nordic price and derivative dynamics, mean reversion.
- Carnero, Koopman & Ooms (2003): periodic heteroscedastic RegARFIMA for daily European prices; long memory in Norwegian prices.
- Knittel & Roberts (2001): deregulated electricity price dynamics, mean reversion and jumps.
- Diebold & Inoue (2001), J. Econometrics: long memory and regime switching are easily confused.
- Hamilton (1989), Econometrica: Markov-switching models.

