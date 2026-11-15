---
date: 2026-11-15
who: anders
topic: method-checks-and-sddp-sources
---

# 2026-11-15 — Anders — Method checks against the literature, and eleven new SDDP sources

_One long session, 10 November (evening) to 15 November. The log of 2026-11-10 covers the work up to the skill test._

## Goal of the session
Make sure that every method choice in the model can be traced to a source: what the model is called, how the Markov states are built and tested, what each constraint in chapter 6 rests on, which values the implementation uses, and how our model compares with every SDDP study in the library.

## What we found / worked out
- **Chapter 5 drafts (10–11 Nov).** 5.2 and 5.3 drafted with the review skill; the fourth paragraph of Anders' own 5.2 rewritten to say more about each study (`drafts/literature-review-v8-test/`). Nothing went to Overleaf.
- **Level of the model.** The papers call weekly scheduling over one to three years medium-term; the TET4565 lecture uses other limits. Every operational source is placed on the hierarchy in `knowledge/topics/scheduling-hierarchy-horizons.md`.
- **Markov states and testing.** NVE's LA25 hourly prices (30 weather years, four model years) can give one scenario per weather year. A sourced recipe for the states and for testing is in `knowledge/topics/markov-states-method.md`. No hydropower study holds years back for testing.
- **Bore against us.** Bore et al. add one averaged cut per week for all states and never call their method Markov SDDP. Our Algorithm 1 keeps a cut set per week and state, as Gjelsvik 2010 and Philpott 2012 (`knowledge/topics/sddp-setup-vs-bore.md`, `markov-states-method.md` §6–10).
- **Chapter 6 element by element.** Most of the weekly model has the same form in Bore 2026, Helseth 2016 and Schindler 2024; what is ours alone is listed with options (`knowledge/topics/model-precedents.md`).
- **Implementation values.** The posted configuration for the simplified Duge case was checked value by value; three settings conflict with chapter 6 (`knowledge/topics/implementation-parameters.md`).
- **All SDDP sources against chapter 6.** 56 sources. Eleven model pumping, one of them sells reserve capacity (from turbines), none sells reserve from the pump, and none combines pumping with joint price–inflow states (`knowledge/topics/sddp-model-comparison.md`).
- **Explanations.** Water values and nested Benders decomposition against SDDP (`knowledge/topics/water-values-and-nested-benders.md`).

## Decisions
- D-003: research questions narrowed to the pump (→ `knowledge/decisions.md`)
- D-004: the model is called a medium-term scheduling model (→ `knowledge/decisions.md`)

## Papers added or discussed
- Added 2026-11-15, all in Zotero and `references.bib`: `helseth2018optimal`, `helseth2020nonconvex`, `hjelmeland2018impact`, `helseth2026considering`, `li2022solving`, `hole2025capacity`, `downward2020stochastic`, `garcia2025longterm`, `vanackooij2020conditional`, `bueno2023impact` (preprint), `philpott2023using` (report, grey).
- Added 2026-11-11: `helseth2020scheduling` (grey, in Zotero), `farahmand2026hydropower` (lecture slides, grey, not in Zotero).
- Discussed against the text: `bore2026`, `kleiven2023`, `dowson2020`, `gjelsvik2010`, `helseth2016`, `philpott2012`, `schindler2024`, `chazarra2018`, `pitorac2020technical`, `fullnerRebennack2025`, `ak2019quantifying`, `alic2023optimal`.

## Files changed
- `knowledge/topics/`: `scheduling-hierarchy-horizons.md`, `markov-states-method.md`, `model-precedents.md`, `implementation-parameters.md`, `sddp-model-comparison.md`, `water-values-and-nested-benders.md` (all new), `sddp-setup-vs-bore.md` (extended)
- `knowledge/`: `decisions.md` (D-003, D-004), `open-questions.md` (Q-005 to Q-010; Q-008 resolved), `glossary-notation.md`, `chapter5-brief.md`, `STATUS.md`
- `literature/`: thirteen new source folders (ten papers, three grey), generated lists, `WANTED.md`, `search-log.md`
- `drafts/literature-review-v8-test/` (5.2, 5.3, the 5.2 paragraph), `ai-usage.md`
- Thesis repo: `references.bib` only (twelve keys), pushed to Overleaf and GitHub. No `.tex` file changed.

## Open questions raised
- Q-005 cite the lecture or the compendium; Q-006 data and recipe for the Markov states; Q-007 implementation values and three conflicts with chapter 6; Q-009 reserves from units that are not running; Q-010 chapter 6 passages that no longer match (→ `knowledge/open-questions.md`)

## Next steps
- [ ] Decide Q-006 and get the inflow series for 1991–2020 that match the LA25 weather years (group)
- [ ] Decide Q-007 and Q-009, then update chapter 6 (Q-010) in one go (group; Anders said "not yet" to chapter 6)
- [ ] Name the source of the head 236.6 m and the NVE inflow figure in the configuration (whoever set them)
- [ ] In Zotero: correct "Hagenvik" to "Hågenvik" in `hagenvik2022comprehensive`; add Baslis 2011, McDermott 2020 and the NVE LA25 report (Anders)
- [ ] Fetch by hand the three open papers whose download was blocked (`literature/WANTED.md`)
- [ ] Continue chapter 5 with the skill: 5.5, 5.4, 5.1, 5.6, 5.7; the gap in 5.7 can use `sddp-model-comparison.md` §1
