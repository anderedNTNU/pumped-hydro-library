---
bibkey: ahlfors2021weekly
bibkey_provisional: true
title: "Weekly planning of hydropower in systems with large volumes and varying power generation: A literature review"
authors: "Charlotta Ahlfors, Mikael Amelin"
year: 2021
venue: "2021 IEEE Madrid PowerTech (conference proceedings), DOI 10.1109/PowerTech46648.2021.9495058"
peer_reviewed: true
methods: []
review_sections: [modelling-phs-plants]
relevance: background
read_by: []
added: 2026-11-04
source_path: "C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/02_Driftsplanlegging_og_optimering/04_Ahlfors_2021_Weekly_planning_of_hydropower_in_systems_with_large_volumes_and_varying_power_generation.pdf"
takeaway: "Short KTH review of long/mid/short-term hydropower planning; finds the horizon definitions inconsistent across the literature and proposes that weekly (1–3 week) planning belongs to mid-term planning."
---

# Weekly hydropower planning: a literature review (Ahlfors & Amelin, 2021)

> **Page convention.** Proceedings pages = PDF pages (printed page numbers 2–7 on PDF pages 2–7; p. 1 unnumbered). Pp. 6–7 are the summary tables. The official IEEE Xplore page range was not checked (unverified).

## Research question / purpose
Review hydropower planning across time frames (long, mid, short term), with a particular focus on *weekly* planning (horizon 1–3 weeks), which the authors say is rarely treated as its own category. Goal: summarise earlier reviews, present representative studies for each time frame, and propose a consistent definition of the planning horizons (pp. 1–2).

## Setting
- **System:** generic; hydropower in systems with a large share of variable renewables (wind, solar). Authors at KTH, with a Swedish-producer motivation (p. 5).
- **Markets:** mentions day-ahead (spot) bidding for short-term planning, reserves and forwards in some of the reviewed mid-term papers.
- **Horizon and resolution:** classification only. Fig. 1 (p. 1): long term = "years or several months", mid term = "months or weeks", short term = "week or days".

## Method
- **Model type:** narrative literature review (no own model). Papers are summarised in three tables: earlier reviews (Table I), long- and mid-term papers (Table II), short-term papers (Table III) (pp. 6–7).
- **How uncertainty is represented:** n/a (the review notes for each paper whether it is stochastic).
- **Solution method:** n/a.
- **Key modelling choices and assumptions:** n/a.

## Data / case
None. 43 references, spanning water-value methods from the 1960s to 2021 (p. 2).

## Key findings
- (p. 1) Long-term planning: one to several years, stochastic inflow and prices, coarse time resolution; output is water values or a weekly discharge plan. Mid-term: smaller reservoirs, finer resolution, output may also be water values. Short-term: next few days, for spot-market bidding.
- (p. 2) Cites Hammid et al. (2020), who define short term as 2–14 days, mid term 3–18 months, long term 1–5 years. This illustrates the definitional inconsistency.
- (p. 2) SDDP (Pereira 1989) allows multi-reservoir modelling without aggregation; the inflow model is a major factor for SDDP results; recent SDDP research covers convergence, strategic bidding, risk aversion, emissions, and wind and pumped-storage integration (citing Helseth et al. 2016).
- (p. 2) SDP strengths and weaknesses are summarised via Zambelli et al. (2011) and Scarcelli et al. (2017): Scarcelli's aggregated Markovian SDP reduces costs compared with the standard Markovian model.
- (p. 3) Mid-term examples: Chazarra et al. (2016) weekly scheduling with day-ahead + secondary reserve markets ("significantly higher expected income" when participating in both); Abgottspon & Andersson (2013) forwards + pumped storage (+20% profit); Hjelmeland et al. SDDiP for nonconvex mid-term scheduling (time-consuming to solve to optimality); Helseth et al. (2020) nonconvex environmental constraints, one-year horizon with weekly stages.
- (p. 4) Fodstad et al. (2016): only small additional value from balancing-market participation in a small Norwegian system (as summarised by the review).
- (p. 4, Conclusion) The planning-horizon definitions are "ambiguous and vary"; the authors propose using Fig. 1 so that weekly planning belongs to mid-term planning. Few weekly-planning models exist, especially for systems with much variable generation.
- (p. 5) Future work: weekly models for Swedish producers with variable renewables and stochastic inflow and prices; combining planning across markets; integrating maintenance.

## Strengths
- Compact map of the planning hierarchy, with a clear statement that the terms long, mid and short term are not used consistently.
- Tables I–III give a quick overview of who did what and where (country of case study).

## Weaknesses / limitations
- Short and descriptive; no systematic search method, no critical comparison.
- The reference numbering in Table II does not match the text: the text treats [17] (Helseth et al. 2016) as an SDDP overview and [20] (Peng et al., robust wind/PV/hydro dispatch) as a long-term paper, while Table II lists [17] as "Hybrid SDP/SDDP" under long term and puts [20] under mid term. The "Conclusions" columns in Tables II–III are also misaligned in the PDF. Check the original paper before citing a specific paper via this review.
- Despite the title, it presents no weekly-planning model and very few weekly-planning papers. Pumped storage is mentioned only in passing.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Background / Theory: planning hierarchy (long, medium, short term) | Fig. 1 definition; long-term output is water values or a weekly plan | p. 1, Sec. I-A, Fig. 1; p. 2, Sec. II-A |
| Statement that horizon definitions vary in the literature | Explicit conclusion plus Hammid et al. example (2–14 d / 3–18 mo / 1–5 yr) | p. 2 (Sec. I-B); p. 4 (Sec. III) |
| Literature review: pointer to mid-term multi-market papers (Chazarra 2016, Abgottspon 2013, Hjelmeland, Helseth) | One-paragraph summaries | p. 3, Sec. II-B; Table II p. 6 |
| Research gap: few weekly models with variable renewables and multiple markets | Conclusion and future-work statement | pp. 4–5, Sec. III |

## Useful quotes (with page numbers)
> "the definitions of the different planning time frames are ambiguous and vary" (p. 4)

> "This means that weekly planning of hydropower belongs to mid term planning." (p. 4)

## Follow-up references to check (backward snowballing)
- [6] Hammid et al. (2020), *Energies* 13(11):2787, review of hydro scheduling optimisation algorithms (gives horizon definitions).
- [21] Chazarra et al. (2016), *EPSR* 130:67–77, weekly scheduling in day-ahead and secondary reserve markets (a note exists at `papers/chazarra2016stochastic/`).
- [25] Hjelmeland, Helseth & Korpås (2016), medium-term scheduling with sales of capacity (Lysebotn).
- [38] Fodstad, Helseth & Henden (2016), start/stop in multi-market short-term scheduling (small balancing-market value).
- [11] Vardanyan & Amelin (2011), short-term hydro planning with much wind.

