---
name: literature-review
description: Use whenever you plan, draft, rewrite, review or shorten the literature review (thesis chapter 5, or any literature text for the project report). Its structure, paragraph patterns, study reporting, language and citation ranges come from the 12 literature reviews of the 14 A-level NTNU theses in theses/ (measured by script; 316 paragraphs coded with a tested codebook), with the four closest theses deciding ties. Includes a draft profiler and a banned-word list derived from the same corpus.
---

# Writing the literature review (D-002)

**Principle.** Content comes from our papers (`literature/papers/<bibkey>/note.md` and `paper.txt`) and our model. Structure, paragraph patterns and language come from the reference theses, as measured. Wording is never taken from a thesis. Rule order when sources disagree: the IØT rules (`guidelines/WRITING_RULES.md`) → our decisions (`knowledge/decisions.md`) → the closest four theses → the corpus.

## Files
| File | Use it for |
|---|---|
| `structure.md` | chapter skeleton, theme sections, the shares to reproduce |
| `paragraphs.md` | what each paragraph type does, sentence by sentence; what to report about a study |
| `language.md` | size, sentence and citation targets; banned and rare words; the words the reviews do use |
| `topics.md` | what a review in our field covers and the table columns the closest theses use |
| `themes.md` | for each theme, the points the closest theses make, in order, and how each is argued (finding / claim with evidence / claim with backup / reasoning); the starting list for a section plan |
| `lessons.md` | what the user tests found wrong and the rule each finding adds; read after `paragraphs.md` |
| Evidence | `theses/lit-review-skill/` (measures, codebook, codings, reliability tests) |

## Hard rules
1. **Never copy.** Blueprints give functions, not sentences. No thesis is open while drafting.
2. **Never invent.** Every cited claim carries a key from `../pumped-hydro-thesis/references.bib` and says only what the paper supports; check it in `paper.txt`, not only in the note. Record the sentence and page you relied on in the chapter's CHANGES file. Missing papers go to Zotero first.
3. **Draft, don't take over.** Mark drafts `% DRAFT (Claude, date, who)`, log them in `ai-usage.md`, and change only the section asked for.
4. **Numbers:** at most about 1.5 per 1,000 words, only where the size of an effect carries the point, and only after the comparability caveat.
5. **Banned words** (`language.md`) never appear; rare words at most once per chapter.
6. **One paragraph, one point, stated first.** Studies are evidence for the point, not the point, except in a STUDY paragraph.

## Workflow
1. **Scope.** Who you are working with; which section; project report or thesis; whether the text goes to a draft file or to Overleaf.
2. **Read** `structure.md`, `paragraphs.md`, `language.md`, `topics.md`; `guidelines/WRITING_RULES.md`; `knowledge/STATUS.md`; the relevant `knowledge/topics/*.md`; and the `note.md` of every paper you will cite. For claims that matter, the passage in `paper.txt`.
3. **Plan the section** before writing a sentence. Start from the theme's point list in `themes.md`: keep the points that apply, add the ones our papers force, give each its argument mode. Then a table with one row per paragraph: role (from `paragraphs.md`), the point in one line, argument mode (finding / claim-evidence / claim-backup / reasoning), the works that back it (1 / 2 / 3+), whether it carries a limitation, a comparison, a consequence or a link to the thesis, what the last sentence does, and **the "this matters because …" sentence written out** (a row without one is a list, not a paragraph; see `lessons.md`). Claims about the literature as a whole say "many" unless counted. Check the plan against `structure.md`: opener, at most two single studies in a row, at least one comparison and one limitation per theme, a synthesis or gap at the end, the shares roughly met. Show the plan to the user for a new section or a restructure.
4. **Draft** paragraph by paragraph from the plan, each from its blueprint, at about 95 words and four sentences.
5. **Check.**
   - `py theses/lit-review-skill/measures/profile_draft.py <file.tex>`: every metric inside the closest-four range, or say why not; fix listed sentences over 35 words.
   - `py theses/lit-review-skill/measures/tics.py <file.txt>`: no banned pattern; rare ones at most once.
   - Read the first sentence of each paragraph in order: they must read as the argument of the section on their own.
   - For every citation, the checked sentence and page are in CHANGES.
6. **Hand over.** Say what was written, what was checked against `paper.txt` and what was not, which keys are missing from the bib, and log in `ai-usage.md`.

## Review mode
Do not edit. Run the profiler and the tic counter; map each paragraph to a role and compare the section with `structure.md` (openers, runs of studies, comparison and limitation present, closer); check study paragraphs against `paragraphs.md` (finding + dimensions + limitation or relation); list findings as location → problem → fix, structure first, then argument, then citations, then language.

## Known limits
- The grades of the 14 theses are assumed A-level (to be confirmed with the supervisor).
- Citation counts are by regular expression; the codings are about 85 % reliable (two tests, `theses/lit-review-skill/codebook/coding/RELIABILITY.md`); shares are robust, single percentages are not.
- The corpus is 12 reviews; a rule that rests on "Bore" rests on two theses by the same authors.
