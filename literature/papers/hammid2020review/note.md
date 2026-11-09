---
bibkey: hammid2020review
bibkey_provisional: true
title: "A Review of Optimization Algorithms in Solving Hydro Generation Scheduling Problems"
authors: "Ali Thaeer Hammid, Omar I. Awad, Mohd Herwan Sulaiman, Saraswathy Shamini Gunasekaran, Salama A. Mostafa, Nallapaneni Manoj Kumar, Bashar Ahmad Khalaf, Yasir Amer Al-Jawhar, Raed Abdulkareem Abdulhasan"
year: 2020
venue: "Energies 13(11), 2787 (doi:10.3390/en13112787)"
peer_reviewed: true
methods: [heuristics-simulation]
review_sections: [modelling-phs-plants, research-gap]
relevance: background
read_by: []
added: 2026-11-04
source_path: "literature/inbox/02_Driftsplanlegging_og_optimering/20_Hammid_2020_Review_of_optimization_algorithms_in_solving_hydro_generation_scheduling_problems.pdf"
takeaway: "Broad, shallow survey (96 papers) of short-, daily-, mid- and long-term hydro scheduling methods, dominated by metaheuristics (GA, PSO, DE, bee/ant colony) with summary tables; names pumped storage in long/mid/short-term scheduling as future work. Weak quality; use only for a general 'many methods exist' statement."
---

# Review of optimisation algorithms for hydro generation scheduling (Hammid et al., 2020)

> **Page convention.** Article 2787, pp. 1–21 = PDF pages 1–21.

## Research question / purpose
Survey the optimisation methods (classical and especially heuristic/metaheuristic) used for long-, mid- and short-term hydro scheduling (LMSTHS), and compare them by case study, constrained parameters, technique and main goal (abstract, p. 1; p. 4).

## Setting
- **System:** any hydro scheduling problem; reviewed cases are mostly Chinese cascades, plus Portugal, Norway, Switzerland, Brazil, Canada, Iran, India (Tables 1–4, pp. 8–15).
- **Markets:** not a focus; a few mid-term entries mention Nord Pool, forwards and ancillary services (Table 3, p. 11).
- **Horizon and resolution:** classifies papers into short-term, daily, mid-term and long-term (Fig. 4, p. 6; Sec. 4.1–4.3).

## Method
- **Model type:** literature review; 96 articles by publication year (Fig. 3, p. 4).
- **Generic formulation (Sec. 3, pp. 4–5):** maximise total power production Σ_i Σ_t P (eq. 1); constraints on power limits, power as a polynomial (quadratic) function of discharge and reservoir volume (eq. 5), net head limits from upstream/downstream levels (eqs. 7–12), flow rate, storage, water density/temperature and efficiency bounds (eqs. 13–18). The formulation is generic and partly odd (e.g. density and temperature bounds).
- **How uncertainty is represented:** not analysed systematically.
- **Solution method:** narrative summaries + tables per horizon (Tables 1–4).

## Data / case
None (review).

## Key findings
- (p. 2) Classical methods (MILP, DP, LP) were used first; heuristic methods are "regarded as elastic, multipurpose, and effective" for non-convex, non-linear problems.
- (p. 5) Repeats the standard decomposition of hydro scheduling into long-, mid- and short-term sub-problems (Fig. 4, p. 6).
- (pp. 6, 8) Short-term table lists Belsnes et al. (2016) as "stochastic successive linear programming", "first-order approximation to the optimization of water head" (Table 1, ref. 28).
- (pp. 10–11, Table 3) Mid-term: Nordic/Swiss SDP and SDDP work (Abgottspon et al.; Helseth, Fodstad & Mo; Hjelmeland et al.) listed among other methods.
- (pp. 11–13, Table 4) Long-term: Markovian SDP (Brazil), SDDP (Mo et al.; Hjelmeland et al.), many metaheuristics.
- (p. 16) Conclusion: future work on AC power flow, integration with wind and solar, and "The impact of pumped water storage on the solution of LMSTHS problem has additional study potential".

## Strengths
- Wide coverage of method names and case locations; summary tables.

## Weaknesses / limitations
- Shallow, descriptive; no critical comparison of solution quality; generic formulation with physically odd constraints.
- **Table 3 (p. 11) and Table 4 (pp. 14–15) are visibly misaligned** in the published PDF (rows do not line up across columns), so the reference ↔ method ↔ case mapping is unreliable.
- Several summaries misread the cited work (e.g. p. 12 describes Hjelmeland et al. as a "stochastic DDP scheduling model according to MIP" with "29.2% greater" revenue — check against the original before reusing).
- Little on uncertainty modelling, SDDP theory, markets or PHS.

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit review intro: many optimisation methods exist for hydro scheduling | Survey of 96 papers, classical vs heuristic | pp. 1–4, Fig. 3 |
| Background: long/mid/short-term decomposition | Restated with figure | p. 5, Fig. 4 (p. 6) |
| Research gap (weak): PHS impact as future work | Conclusion statement | p. 16 |
| Lit review: metaheuristics as an alternative we do not pursue | GA/PSO/DE/colony algorithms per horizon | Tables 1–4, pp. 8–15 |

## Useful quotes (with page numbers)
> "The impact of pumped water storage on the solution of LMSTHS problem has additional study potential" (p. 16)

## Follow-up references to check (backward snowballing)
- Nazari-Heris et al. (2017), short-term scheduling with heuristic algorithms, RSER 74 (ref. 6).
- Hjelmeland, Korpås & Helseth (2016), combined SDDP and simulator model (ref. 71) — check against the original.
- Helseth, Fodstad & Mo (2016), energy and reserve capacity markets (ref. 59) — in bib as `helseth2016`.

