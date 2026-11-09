---
bibkey: zhang2026unlocking
title: "Unlocking mid-to-long-term flexibility: why seasonal pumped storage outperforms conventional pumped storage in wind-solar dominated grids"
authors: "Zhang, Meng; Li, Peiquan; Yao, Yaling; Kanji, Ai Relanjiang; Zhao, Ziwen; Chen, Diyi; De Assis Brasil Weber, Natália; Hunt, Julian David"
year: 2026
venue: "Energy Conversion and Management 348, 120750"
peer_reviewed: true
methods: [deterministic-lp-milp, uncertainty-modelling]
review_sections: [ldes-seasonal-storage, modelling-phs-plants, reservoir-sizing-capacity, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "System-perspective, hourly one-year MILP unit commitment for Qinghai (China) comparing a 4,200 MW seasonal PHS with conventional (daily) PHS across 9 k-means++ wind/solar typical years: SPS cuts curtailment, emissions and operating cost (≈1/5), but capex is 1.33× and LCOE higher (0.58 vs 0.52 CNY/kWh); no markets."
---

# Seasonal vs conventional pumped storage in wind-solar grids (Zhang et al., 2026)

_Article-numbered paper; page numbers are the article's own pages 1–21. Published online 14 Nov 2025._

## Research question / purpose
How do **seasonal pumped storage (SPS)** and **conventional pumped storage (CPS)** differ in their ability to handle mid-to-long-term (seasonal) wind and solar variability? The two stated questions (p. 2): (i) what framework can optimise a power system while reflecting the stochastic and seasonal nature of wind and solar, and (ii) how can SPS benefits be quantified and how does SPS differ fundamentally from CPS. Claimed gaps (p. 3): research focuses on short-term flexibility; no systematic SPS-vs-CPS comparison of mid-to-long-term regulation; evaluations are one-dimensional.

## Setting
- **System:** the regional power system of **Qinghai Province, China** (wind 8,430 MW, solar 16,010 MW, > 60% of installed capacity; 17% renewable curtailment in 2021) (p. 11). One planned **4,200 MW** SPS: upper reservoir on a primary Yellow River tributary, lower reservoir = the existing **Longyangxia** hydropower reservoir, connected by a **21 km pressure pipeline** (p. 11). The CPS alternative has (by my derivation, see below) the same installed capacity. SPS and CPS design differences in energy storage capacity and discharge duration are given in **Fig. 7(d)** (p. 11), which the text extraction does not capture (**values unverified**). CPS is described as daily/intra-day regulation, SPS as seasonal or multi-seasonal regulation with much larger reservoirs (p. 11).
- **Markets:** none. Centralised system cost minimisation (unit commitment/dispatch); no prices, no reserve products. Policy remark: capacity markets or long-term contracts may be needed to pay for SPS's long-duration flexibility (p. 19).
- **Horizon and resolution:** one year, **hourly** (indicators summed over 8,760 h, Eqs. 33, 35, p. 10).

## Method
- **Model type:** deterministic **MILP** unit commitment and dispatch, solved in GAMS (p. 8). Minimises total operating cost: start-up/shut-down, fixed, ramping, curtailment, transmission, loss of load and carbon costs (Eq. 5–12, pp. 6–7). Power balance with a flexibility-deficit term (unserved load or curtailment) (Eq. 13, p. 7).
- **PHS constraints (pp. 7–8):** min/max generating power as shares of rated power (Eq. 14), ramp limits (Eq. 15), pumping min/max and ramps (Eqs. 16–17), no simultaneous pumping and generation for **fixed-speed** units (Eq. 18), reservoir bounds (Eq. 19), water balance with inflow, pumping (× η_p), generation (÷ η_g), spillage and mandatory release (Eq. 20), generation limited by upper-reservoir content (Eq. 21), pumping limited by free capacity (Eq. 22). Transmission corridor limits (Eq. 23). Other constraints are deferred to refs [47, 48].
- **How uncertainty is represented:** **k-means++ clustering** of historical wind and solar output time series into typical years (Sec. 2.1, pp. 3–5): features are mean, variance, SD and coefficient of variation. Wind: High-Wind Year (mean output factor 0.366, CV 0.51), Normal (0.357, CV 0.607), Low (0.24, CV 0.533); solar: High-Irradiance (0.247, CV 1.265), Normal (CV 1.274), Low (0.237, CV 1.269) (p. 5). 3 × 3 wind-solar combinations × {SPS, CPS} = **18 scenarios** (Table 2, p. 11), each solved **deterministically** (perfect foresight within the year). No stochastic optimisation and no probabilities attached to scenarios.
- **Data (p. 8):** PV and wind availability factors from Global Solar Atlas and renewables.ninja; runoff from ERA5 via the atlite toolkit and HydroBASINS catchments, **daily flow spread uniformly over 24 h**; hydro power from design head with Eq. 25 (efficiency 0.8–0.9 for conventional hydro, **0.75–0.77 for pumped storage**); load synthesised from typical provincial load profiles scaled to daily peak/valley (Eq. 26).
- **Cost parameters (p. 7, p. 9):** coal emission factor 0.979 tCO₂/MWh; value of lost load 4,051 CNY/MWh; hydro spill cost 800 CNY/MWh; wind/solar curtailment 0.3196 CNY/kWh; transmission 0.02 CNY/kWh; capital cost **SPS 25.165 vs CPS 18.967 million CNY/MW**. LCOE with 8% discount rate and 50-year life (Fig. 12 caption, p. 15); capex sensitivity 80–120% (p. 14).
- **Multi-criteria evaluation (Sec. 2.3, pp. 9–10):** technical (curtailment rate CTR, net-load peak–valley difference NPD, carbon emissions CEM, flexibility adequacy rate FAR, flexibility deficiency rate FDR), economic (capital cost, operating cost, LCOE) and unit-stability (power adjustment frequency PAF, regulation mileage RGM, unit start frequency USF) indicators; weights from entropy and coefficient-of-variation methods, combined by a Lagrange-multiplier rule (Eqs. 36–41).
- **Key modelling choices and assumptions:** **no head effects** (fixed design head, constant efficiencies); fixed-speed units; no end-of-horizon storage value stated (unverified how the year-end reservoir level is set); capacities fixed (no sizing optimisation).

## Data / case
Qinghai Province (36.56N, 101.74E). Data are confidential (p. 20). Typical-year profiles in Figs. 4–5 (pp. 5–6). Seasonal pattern: wind higher Jan–Apr and Oct–Dec; solar higher Jan–May and Oct–Dec; both lower in the wet season June–September (p. 6).

## Key findings
- (p. 12) Curtailment: in the high-wind/high-irradiance case, SPS gives an August curtailment rate of 4.35% vs 18.14% for CPS; annual 5.47% vs 12.3%. In the low/low case the difference vanishes (1.93% vs 1.80%). SPS stores summer surplus for winter.
- (p. 12) Net-load peak–valley difference: SPS 1.5% lower (low/low) to 10.6% lower (high/high, 11,234 vs 12,567 MW).
- (p. 12, p. 17) Emissions: SPS reaches zero annual emissions in the high-wind scenarios; CPS emissions are far higher (e.g. JPaA 12.51 Mt vs PSaA 206.3 Mt, p. 17).
- (p. 13) Flexibility adequacy: SPS better in the high-flow season (July–October; September 0.649 vs 0.271); CPS slightly better in the low-flow season (January–March; February 0.863 vs 0.839), because SPS gives priority to continuous generation in the dry season and pumps less.
- (p. 14) Economics: investment SPS 10,569.3 vs CPS 7,966.234 "million CNY" (**1.33×**); operating cost lowest for SPS at 16.945 "billion" vs 86.563 "billion" for CPS (≈ 5.1×). Every SPS scenario has lower operating cost than every CPS scenario.
- (pp. 14–16) **LCOE: SPS 0.58 vs CPS 0.52 CNY/kWh on average**; SPS LCOE is linear in capex and reaches 0.8 CNY/kWh in high/high (≈ 37% above CPS); in low/low the CPS LCOE is about 1% above SPS. Operating savings do not offset the higher capex under most conditions.
- (p. 16) Regulation mileage: SPS ≈ 765 MW per adjustment vs CPS 397 MW; CPS adjusts far more often (≈ 2,750–4,770 times/yr): SPS does large, long-duration regulation, CPS frequent small adjustments.
- (pp. 18–19) Combined weights: technical 45.81%, economic 26.84%, stability 27.35%; average score SPS 98.03 vs CPS 68.6. Highest weight: CEM 18.68%, operating cost 17.75%, RGM 17.07%.
- (pp. 19–20) Discussion: SPS value is greatest where VRE share is high, there is a seasonal mismatch between VRE and demand, and topography allows large reservoirs. The paper did **not** study hybrid operation (daily cycling plus ancillary services). It calls for co-optimisation models that stack long-term arbitrage and short-term ancillary-service revenue.

## Strengths
- Direct comparison of short-duration (daily) and seasonal pumped storage in the same system model; explicitly about **storage duration**.
- Hourly resolution over a full year, so both intra-day and seasonal cycling are visible.
- Typical-year construction by k-means++ clustering is transparent and is similar to how we cluster weekly samples into Markov states.
- Separates capex, operating cost and LCOE, showing that system benefit ≠ asset profitability.

## Weaknesses / limitations
- Uncertainty is scenario analysis only: each typical year is solved with perfect foresight, so seasonal storage value is an upper bound (no forecast error, no adaptive policy, no water values).
- No markets or prices; benefits are system cost savings, which are not the owner's revenue. No reserves.
- Key design data for SPS vs CPS (reservoir volume, energy, duration) are only in Fig. 7(d); fixed head and constant efficiency; hourly inflow from daily flow spread evenly.
- Multi-criteria score depends on weighting choices; with the scores close to 100 for SPS, the 98.03 vs 68.6 contrast says little about magnitude.
- Internal inconsistencies (my checks): 25.165 M CNY/MW × 4,200 MW ≈ 105,700 M CNY, about 10× the reported 10,569.3 "million CNY" (p. 14; Table 3 is in units of 10,000 CNY, so units are unclear). CPS emissions given as 2.02–2.90 × 10⁹ t (p. 12) but 206.3 Mt (p. 17). Several figure references are off (RGM results "in Fig. 12" are in Fig. 13; start-ups "in Fig. 13" are in Fig. 14, p. 16). Ref. [8] lists the Norwegian PSH review authors by first name ("Livia P, Kaspar V, Leif L"). The claim that inter-seasonal arbitrage "typically offers far greater economic returns than intra-day markets" (p. 19) is not shown in the paper.
- Single region (Qinghai); limited generalisability, as the authors say (p. 19).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background 2.1 (LDES/seasonal storage): why seasonal storage matters with high VRE | Shift from short-term balance to mid-to-long-term flexibility; CPS limited by storage scale | pp. 1–2, Sec. 1.1–1.2 |
| Background 2.1: Norway/Switzerland as seasonal-storage examples | Norway's reservoir network and Swiss seasonal balancing cited (refs [8], [9]) | p. 2 |
| Lit. review 5.5: storage duration comparison (daily vs seasonal PHS) | SPS vs CPS at same MW; curtailment, emissions, operating cost, LCOE | pp. 12–16, Sec. 4 |
| Lit. review 5.5: capex of seasonal vs conventional PHS | 25.165 vs 18.967 M CNY/MW (1.33×); LCOE 0.58 vs 0.52 CNY/kWh; 8%, 50 yr | p. 9, p. 14, p. 16, Fig. 12 |
| Lit. review 5.3: system-perspective PHS modelling | Hourly MILP unit commitment with PHS constraints | pp. 6–8, Sec. 2.2 |
| Method: clustering for representative scenarios | k-means++ steps, features (mean, CV), typical wind/solar years | pp. 3–5, Sec. 2.1, Eqs. 1–4 |
| Research gap 5.6: need for value stacking of long-term arbitrage + ancillary services | Explicit future-research statement | pp. 19–20, Sec. 6(iii) |
| Discussion: seasonal storage pumps less in dry season, CPS cycles daily | FAR seasonal results | p. 13 |
| Discussion: pumped-storage efficiency values | 0.75–0.77 for PSH, 0.8–0.9 for conventional hydro | p. 8, Eq. 25 |

## Useful quotes (with page numbers)
> "the investment cost of SPS is 1.33 times that of CPS" (p. 1)

_Further key statements are paraphrased with page numbers under Key findings._

## Follow-up references to check (backward snowballing)
- [10]/[48] Hunt et al. (2020), Global resource potential of seasonal pumped hydropower storage, Nat. Commun. 11 — key LDES/SPS background source.
- [18] Hunt et al. (2018), SPS vs conventional reservoir dams, water–energy–land nexus, Energy Convers. Manage.
- [14] Hunt, de Freitas & Pereira Jr. (2017), review of SPS combined with cascade dams in Brazil, RSER.
- [20] Sepulveda et al. (2021), The design space for long-duration energy storage, Nat. Energy — key LDES source.
- [37] Dowling et al. (2020), Role of long-duration energy storage in VRE systems, Joule.
- [4] Sánchez-Pérez et al. (2022), Effect of modelled time horizon on quantifying the need for long-duration storage, Appl. Energy — relevant for horizon choice.
- [8] Pitorac, Vereide & Lia (2020), Technical review of existing Norwegian pumped storage plants, Energies — **directly relevant to Aurland 3 / Norway** (author names garbled in the paper's reference list).
- [9] SFOE (2012), Swiss potential for hydropower generation and storage (grey literature).
- [11] Guerra et al. (2025), Towards robust and scalable dispatch modelling of LDES, RSER.

