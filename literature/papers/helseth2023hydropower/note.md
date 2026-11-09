---
bibkey: helseth2023hydropower
bibkey_provisional: false
title: "Hydropower Scheduling Toolchains: Comparing Experiences in Brazil, Norway, and USA and Implications for Synergistic Research"
authors: "Arild Helseth, Albert C. G. Melo, Quentin M. Ploussard, Birger Mo, Maria E. P. Maceira, Audun Botterud, Nathalie Voisin"
year: 2023
venue: "Journal of Water Resources Planning and Management 149(7), 04023030 (ASCE)"
peer_reviewed: true
methods: [sddp-time-series, sdp, heuristics-simulation]
review_sections: [modelling-phs-plants, electricity-markets, research-gap]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Comparative review of hydro scheduling toolchains (Brazil NEWAVE/DECOMP/DESSEM, Norway EMPS/ProdRisk/SHOP, US Colorado River CRSS/CRMMS/GTMax): in decentralised Norway the producer is a price-taking, risk-neutral profit maximiser, long- and medium-term models are coupled by price forecasts (Mo et al. 2001) and medium/short-term by cuts; reserves across the toolchain flagged as an under-researched gap."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/82_Helseth_2023_Hydropower_Scheduling_Toolchains_Comparing_Experiences_in_Brazil_Norway_and_USA_and_Implic.pdf
---

# Hydropower scheduling toolchains in Brazil, Norway and USA (Helseth et al., 2023)

_Page numbers below are the article's page suffixes: "p. 5" = 04023030-5. The inbox PDF has 12 pages; text extracted from pp. 1–9 (pp. 10–12 are references). Not in `references.bib` yet: key is provisional and must be added to Zotero. DOI 10.1061/JWRMD5.WRENG-5911._

## Research question / purpose
How are operational hydro scheduling toolchains (linked long-, medium- and short-term models) organised in three hydro-dominated systems, and how do institutions drive their design? Aim: identify similarities/differences and directions for synergistic research (p. 1–2).

## Setting
- **System:** Brazil (109 GW hydro, 396 TWh/yr, 168 plants), Norway (34 GW, 141 TWh/yr, 351 plants >10 MW, 9 GW exchange), US Colorado River System (4 GW, 8 TWh/yr, 60 plants) (p. 2, Table 1).
- **Markets:** centralised cost-based dispatch (Brazil), liberalised Nordic market (Norway), multipurpose water-first federal operation (CRS).
- **Horizon and resolution:** long-term multi-year (NEWAVE 5 years monthly; EMPS 3–5 years), medium-term months (DECOMP) or years (ProdRisk), short-term 1–2 weeks (SHOP) / 1 week half-hourly (DESSEM) (p. 4–5).

## Method
- **Model type:** qualitative comparative review; no new model.
- **How uncertainty is represented (as described):** inflow is "the most important uncertainty" over the scheduling period (p. 3); NEWAVE: inflow via periodic AR models and a CVaR risk measure (p. 4, 7); ProdRisk: market price as stochastic exogenous variable within SDDP (Gjelsvik & Wallace 1996; Gjelsvik et al. 1999; Mo et al. 2001) (p. 5); SHOP deterministic (p. 5).
- **Solution method (as described):** SDP and SDDP use temporal decomposition with state variables (reservoir volumes, past inflows); SDDP avoids discretising states and suits many reservoirs (p. 3). Coupling between models by dual (cuts, prices) or primal (volumes, rule sets) information (p. 8).

## Data / case
Descriptive system data from EPE, SSB, NVE, UWM (2023) (p. 2).

## Key findings
- (p. 3) Water is a cost-free resource with an opportunity cost; finding it is "an essential part of the scheduling process"; multiyear storage needs multi-year horizons.
- (p. 3) Decision stages of weeks or months because inflows are predictable on seasonal (snowmelt) or sub-monthly (rainfall) scales; time steps inside stages either load blocks or chronological.
- (p. 4) History: Brazil adopted SDP in 1979; SDDP developed at CEPEL late 1980s (Pereira 1989; Pereira & Pinto 1991); 1993 extension with periodic AR inflow; NEWAVE official since 1998.
- (p. 5) Norway: EFI started SDP-based modelling 1962; EMPS around 1974 combining optimisation and rule-based simulation; after the 1991 liberalisation price forecasting became essential and the producer became a profit maximiser; ProdRisk implements SDDP with exogenous stochastic price (Gjelsvik et al. 2010); SHOP (successive LP, possibly MILP) deterministic short-term model for bidding.
- (p. 5) Use of scheduling models is not mandatory in Norway (contrast with Brazil).
- (p. 7) Decentralised Norwegian objective: "Given a forecast of future market prices: maximize the expected profit..." under price-taker, risk-neutral assumption; price-taking "believed to hold fairly well for the Nordic market"; risk handled financially through forwards/futures.
- (p. 8) Norway: LTS and MTS typically coupled by power prices (Mo et al. 2001); MTS and STS may be coupled by cuts (Gjerden et al. 2016); STS needs exogenous price forecasts. No upstream feedback from shorter- to longer-term models in any toolchain.
- (p. 8) Research gaps: how much STS detail LTS/MTS need; combined short- and long-term VRES uncertainty "remains a challenge"; reserves/ancillary services handled in LTS (Helseth 2021), MTS (Helseth 2016) and STS (Aasgård 2018) but "the coordinated treatment through the toolchain has received little attention".
- (p. 9) Future: SDDiP for nonconvexities (Hjelmeland 2018), aggregation (Blom 2020), ML; need for open data and test cases.

## Strengths
- Authoritative (SINTEF, CEPEL, Argonne, MIT, PNNL authors); concise history of SDP/SDDP adoption and model roles.
- Clear statement of the Nordic producer's problem: price-taker, risk-neutral, profit-maximising.

## Weaknesses / limitations
- Descriptive; no quantitative comparison. Little on pumped storage. US case only the Colorado River.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background: Nordic producer is a price-taking, risk-neutral profit maximiser | Explicit objective formulation and justification | p. 7, "Decentralized Approach" |
| Background/theory: opportunity cost of water / water values | Water is cost-free but has opportunity cost | p. 3 |
| Method: weekly stages justified by inflow predictability | Stage length discussion | p. 3 |
| Lit. review: SINTEF toolchain (EMPS, ProdRisk, SHOP) and coupling by prices/cuts | Toolchain description, Fig. 2–3 | p. 5, 8 |
| Lit. review: history of SDP→SDDP (Brazil, Norway) | Dates and references | p. 4–5 |
| Research gap: reserves across the toolchain; combined short/long-term uncertainty | Explicit open questions | p. 8, "Future Challenges" |
| Background: Norwegian hydro capacity numbers | Table 1 (34 GW, 141 TWh, 351 plants) | p. 2 |

## Useful quotes (with page numbers)
> "the coordinated treatment through the toolchain has received little attention" (p. 8)

## Follow-up references to check (backward snowballing)
- Helseth & Melo (2020), technical review of Brazilian and Norwegian models and toolchains.
- Gjelsvik & Wallace (1996); Gjelsvik et al. (1999) [`gjelsvik1999`]; Mo et al. (2001) [`mo2001`]; Gjelsvik et al. (2010) [`gjelsvik2010`].
- Gjerden et al. (2016), coupling MTS and STS by cuts.
- Pérez-Díaz et al. (2022), review of hydro scheduling in liberalised markets.
- Helseth et al. (2021) reserves in LTS; Aasgård (2018) reserves in STS.

