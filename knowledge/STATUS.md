# Project status

**Last updated:** 2026-11-15 by Claude (with Anders). `/wrap-up` rewrites this file every session.

## Where we are
- **Research questions and level (D-003, D-004):** adding a pump, the charging capacity of a long-duration storage, and price volatility and persistence. The model is a medium-term scheduling model; "long-term" only for the storage and for system models.
- **Literature chapter (ch. 5):** the group's own structure stands (perspective, uncertainty, markets, capacities, methods, gap). 5.2 has Anders' five-paragraph text with a rewritten fourth paragraph, and 5.3 has a compact draft, both in `drafts/literature-review-v8-test/`. Not written with the skill yet: 5.1, 5.4, 5.5, 5.6, 5.7. Overleaf still holds ch. 4 v10 from 2026-11-09. Evidence for the gap is in `knowledge/topics/sddp-model-comparison.md`: of 56 SDDP sources, eleven model pumping, none sells reserve capacity from the pump, and none combines pumping with joint price–inflow Markov states.
- **Model (ch. 6):** unchanged in Overleaf since 2026-11-10. Every element is traced to sources in `knowledge/topics/model-precedents.md` and `sddp-model-comparison.md`. Ours alone: reserve from the pump with its limit, reserves from units that are not running, the price standard deviation as a clustering feature, held-out test paths. Four passages no longer match later decisions (Q-010).
- **Markov states and data:** a sourced recipe exists (NVE LA25 weather years, joint K-means per week, counting, test on the chain and on the weather years; `knowledge/topics/markov-states-method.md`). Not decided (Q-006); the matching inflow series is missing.
- **Implementation:** the configuration for the simplified Duge case is checked value by value in `knowledge/topics/implementation-parameters.md`. Three settings conflict with ch. 6: the end-volume target, the stopping rule and the pump's reserve limit (Q-007).
- **Review-writing skill (D-002):** built and tested on 5.2 and 5.3; unchanged since 2026-11-10 (`.claude/skills/literature-review/`).
- **Sources:** 141 papers, 64 grey sources, 14 theses. Eleven SDDP sources were added on 2026-11-15 and are in Zotero and `references.bib`.

## Next steps
1. Group decisions that block the model text: Q-006 (data and recipe for the states), Q-007 (implementation values and the three conflicts), Q-009 (reserves from units that are not running).
2. Get the inflow series for 1991–2020 that match the LA25 weather years.
3. Update ch. 6 in Overleaf once 1 is settled (Q-010).
4. Draft the remaining ch. 5 sections with the skill, starting with 5.5 (capacities) and 5.7 (gap).
5. Zotero housekeeping: Baslis 2011, McDermott 2020, the NVE LA25 report, and the spelling of Hågenvik.

## Blockers
- The inflow series for the LA25 weather years is not in hand (Q-006).
- The sources of two values in the configuration are unknown: head 236.6 m and the NVE inflow figure (Q-007).
- McDermott 2020 and two owner studies from the old text are not in the library (Q-001, Q-003).
- Grades of the 14 reference theses are still unconfirmed with the supervisor.
