---
date: 2026-11-10
who: anders
topic: lit-review-5.2-and-skill
---

# 2026-11-10 — Anders — Literature chapter 5.2 and the new review-writing skill

## Goal of the session
Get the literature chapter to Bore & Brensholm's level: first by drafts (v5–v7), then by assessment, then by rewriting 5.2 (perspective) sentence by sentence against the papers; finally decide to build a new skill that writes like the 14 A-level theses.

## What we found / worked out
- **Drafts v5, v6, v7** (`drafts/literature-review-v*/`, with HTML-based PDF previews): Anders judged all of them "way off". The assessment against Bore ch. 4: no search strategy, findings named but not reported, 14 sources reused, generic critique, no "connect" sentences, Table 3 without "This study".
- **5.2 rewritten in chat** (five paragraphs: system → owner → price-maker → price-taker → summary), every citation checked in `paper.txt`. Findings and page references are in `knowledge/topics/valuation-perspective.md`. Key corrections: Henden 2016 does *not* show a system optimum that leaves the owner nothing (figures read off; its conclusion contradicts its results on consumers); Sioshansi 2009 is the only study where welfare rises while the owner's value falls; Helseth, Mo & Helseth 2023 p. 7 is the source for "the producer's problem is its own expected profit"; not all four system studies say "socio-economic surplus".
- **Bore's 4.2 Stochasticity** read as the model for our 5.3; a shortened 5.3 drafted in chat (not in a file).
- **New skill (D-002):** built in the same session (continued after the first wrap-up). Step 1: `theses/lit-review-skill/measures/` (REPORT.md: the 12 reviews are median 2,500 words, 25 paragraphs, 30 works, 95-word paragraphs, 21-word sentences, 1.5 numbers per 1,000 words; closest four and Bore two reported separately; BANNED.md: 29 patterns the reviews never use, 44 rare). Step 2: codebook v1.1 (`codebook/CODEBOOK.md`) with Anders' structure dimensions; reliability test on Bore 2026 passed (role 86 %, kappa 0.83; all fields ≥ 81 %).

- **Later the same session:** the skill was tested on 5.3.1 (four versions; Anders' judgements became lessons 1–10 in `lessons.md`), given an independent reviewer with a checklist (`review-checklist.md`), `themes.md` (points per theme and how they are argued, from a part-E coding of all 316 paragraphs), `phrasing.md` (openers by role, verbs, register), and seven additions after comparing with a finance-thesis skill: exemplar reading with written observations, a contrast-set gap table (largest gap: connective sentence openers 26–30 % in the theses vs 1–7 % in Claude's drafts), a calibrated flag budget (Bore 1, Claude drafts 9–12, target 4), rhythm and punctuation metrics, relative tic flagging, `knowledge/chapter5-brief.md` with a `% src` rule, and scope and budget rules.

## Decisions
- D-001: literature chapter v5 six-part structure, own file not Overleaf (→ `knowledge/decisions.md`)
- D-002: new literature-review skill from the 14 theses, review only, closest four as tie-break, how and what (→ `knowledge/decisions.md`)

## Papers added or discussed
- `bradbury2014economic`, `abgottspon2016multihorizon`, `bore2026assessing`: added to Zotero via the connector; thesis repo pushed.
- `henden2016economic`, `sioshansi2009estimating`, `helseth2023hydropower`: notes extended with checked quotes and page numbers; `dallinger2019socioeconomic`, `henden2016economic` marked as in Zotero.
- Discussed against text: `helseth2013`, `helseth2017`, `ak2019quantifying`, `alic2023optimal`, `abgottspon2013stochastic`, `baslis2011midterm`, `fullnerRebennack2025`, `perezdiaz2015trends`, `perezdiaz2020medium`, `helseth2016`, `bore2026`, `lohndorf2013`, `belsnes2016applying`, `kloess2014bulk`, `warland2016stochastic`, `idso2024shortterm`, `schaffer2022stochastic`.

## Files changed
- `drafts/literature-review-v5|v6|v7/` (tex, main, CHANGES, PDF previews)
- `knowledge/topics/sddp-setup-vs-bore.md`, `knowledge/topics/valuation-perspective.md`
- `theses/lit-review-skill/` (measures, codebook, coding of Bore 2026)
- `literature/WANTED.md` (McDermott 2020), `ai-usage.md` (five rows)
- Thesis repo: `references.bib` (three keys), pushed to Overleaf and GitHub

## Open questions raised
- Q-001 McDermott 2020; Q-002 Baslis 2011 into Zotero; Q-003 two unidentified owner studies; Q-004 which 5.2 goes to Overleaf (→ `knowledge/open-questions.md`)

## Next steps
- [x] All 12 reviews coded (three Sonnet agents from the codebook alone; 30-paragraph spot-check by Claude: role 87 %, fields ≥ 83 %) and aggregated
- [x] Skill written: `.claude/skills/literature-review/` (SKILL.md, structure.md, paragraphs.md, language.md, topics.md); held-out test 83 %; profiler flags v7 and passes Bore 2026
- [x] User test on 5.3.1 done (drafts/literature-review-v8-test/); the judgements are in the skill
- [ ] Anders fills in the research questions and checks the five-sentence summary in `knowledge/chapter5-brief.md`
- [ ] Next section with the full workflow (exemplar reading, plan, draft, profiler, reviewer) before the chapter is drafted section by section
- [ ] Add Baslis & Bakirtzis 2011 and McDermott 2020 to Zotero; find the two missing owner studies (Anders)
- [ ] Decide which 5.2 text goes to Overleaf (group)
