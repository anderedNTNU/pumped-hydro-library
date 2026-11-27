# Supervisor feedback on the draft of 27 November 2026 (theory to SDP, literature review)

Received by Anders on 2026-11-27 and pasted into the session. The draft is `ProjectReportPumpedHydro_TeoriTOM_SDP_3LR.pdf`; its source was merged into the Overleaf project the same day (thesis commit 544d461, see Q-012). Next meeting with the supervisor: Wednesday 2 December 2026. The points below are a summary in English; the wording is ours.

## Chapter 2, Theory

1. Generally good: the main concepts are covered without too much detail.
2. Section 2.2 cites the textbooks (Birge and Louveaux, Boyd and Vandenberghe) too often. State once at the start of 2.2 that the section is based on them and remove the in-text citations. Applies to 2.2 only.
3. The whole chapter must connect to the case study: every concept the case study needs is introduced here. If EVPI is computed, explain it precisely with mathematical expressions.
4. Too few mathematical expressions: only the LP form. The Bellman equation is only in Figure 2; the two-stage problem and the recourse function are only described in words. Introduce notation here that is reused in the SDDP part and the model chapter.
5. Remove theory that is not used. Keep only what (a) is relevant for the case study or the model, or (b) is needed to understand other theory that is used.
6. Wait-and-see: say that it connects to the deterministic problem introduced earlier.
7. "Stage" is used in both stochastic programming and dynamic programming. Explain in the DP part how a stage there differs.
8. Figure 2: must be explained in the text ("Figure 2 presents how a value function is determined by discretizing over system states ..."). Make it more general ("system state at the end of the stage" instead of "reservoir volume"). Beta is not explained in the text.
9. Duality: connect it explicitly to water values (the dual of the reservoir balance) and to Benders cuts.
10. Convexity, when the SDDP part is included: the literature review says several times that SDDP needs linear approximations, so the theory must explain why SDDP needs convex subproblems. This is also an argument for shortening the NLP/MIP part.

## Chapter 3, Literature review

11. Many good references, cited correctly, compared across studies.
12. Missing: a clearer story through the chapter. For each paragraph: which part of the story does it tell? Example: the opening sentence on long-term consequences and operational detail should lead to which model types achieve this, with the point that SDDP is a good framework for it.
13. Missing: the methods, especially early. Avoid "system models"; say which mathematical model each study uses. Example: "Helseth et al. (2013) show, with a case study of the Icelandic power system using an SDDP framework, that ...".
14. Table 1 is useful. Pumping (yes/no) and possibly reservoir sizes could be a column there instead of a separate section.
15. Section 3.4 has sentences explaining what stochastic optimisation is; covered in chapter 2, remove.
16. Replace "As this groups knowledge" with "To the best of our/the authors' knowledge".
17. Replace imprecise phrases such as "clearly impact" and "more realistic" with what the study shows, briefly and with numbers.

## Small things

18. URLs in the running text and a broken cross-reference ("section ??").
19. Table 1 has a placeholder ("Source 6"); Sauhats and Zisos are neither mentioned in the text nor in the reference list; "Helseth et al. (2018)" in the text appears as "Helseth, Mo et al. 2017" in the reference list.
20. Choose British or American spelling.
21. A loose unnumbered heading in chapter 2 ("Optimization Theory").
22. Typos: "lang term", "hydropwoer", "where needed", "sell reservoir capacity".

## What the library already answers (checked 2026-11-27)

- "Source 6" links to ScienceDirect PII S0196890425012749, an Energy Conversion and Management article; this is very probably `zhang2026unlocking` (same journal, volume 348, article 120750). Confirm by opening the link.
- The SIAM link (10.1137/23M1575093) is `fullnerRebennack2025`.
- The MDPI link (Energies 12(1), 189) is `hjelmeland2019energies`.
- "Helseth et al. (2018)" is `helseth2017` in `references.bib` (IET GTD 12(2), DOI 10.1049/iet-gtd.2017.0903): online 2017, printed in a 2018 issue. One year must be chosen and used in text and table.
- Sauhats and Zisos are in `references.bib` as `sauhats2016optimal` and `zisos2023mixing`; the table uses `\href` links instead of citations, which is why they are missing from the reference list.
- The IEEE link (document 9919382, feasibility cuts in SDDP) is not in `references.bib` or the library.
