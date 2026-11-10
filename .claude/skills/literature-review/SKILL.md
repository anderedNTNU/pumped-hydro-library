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
| `phrasing.md` | how the theses phrase each kind of paragraph: openers by role, reporting verbs, hedging, register; read before drafting |
| `lessons.md` | what the user tests found wrong and the rule each finding adds; read after `paragraphs.md` |
| `review-checklist.md` | the Must and Should items an independent reviewer runs on every draft before hand-over |
| `knowledge/chapter5-brief.md` | the facts: the thesis in five sentences, research questions, binding decisions, every reportable number with its source and check status, must-contain and source pack per section; the only source for statements about our own work |
| Evidence | `theses/lit-review-skill/` (measures, codebook, codings, reliability tests) |

## Hard rules
1. **Never copy.** Blueprints give functions, not sentences. No thesis is open while drafting.
2. **Never invent.** Every cited claim carries a key from `../pumped-hydro-thesis/references.bib` and says only what the paper supports; check it in `paper.txt`, not only in the note. Record the sentence and page you relied on in the chapter's CHANGES file, and put `% src: <bibkey> p. N` on the same line as every number and every finding in the `.tex`. Facts about our own model and the research questions come only from `knowledge/chapter5-brief.md`. Missing papers go to Zotero first.
3. **Draft, don't take over.** Mark drafts `% DRAFT (Claude, date, who)`, log them in `ai-usage.md`, and change only the section asked for.
4. **Numbers:** at most about 1.5 per 1,000 words, only where the size of an effect carries the point, and only after the comparability caveat.
5. **Banned words** (`language.md`) never appear; rare words at most once per chapter.
6. **One paragraph, one point, stated first.** Studies are evidence for the point, not the point, except in a STUDY paragraph.
7. **Precedent rule: every structural choice has a named model in the theses.** The section layout copies the layout of one thesis's section whose *setup* fits ours, whatever its subject: a section that classifies two approaches and gives a study and a drawback for each is the model for any classifying section; one that compares market compositions study by study is the model for any comparison of configurations; one that walks through methods in order is the model for a methods section. Copy the setup (sub-sections or not, how many paragraphs, what the first and last do, how studies enter), never the content. Every paragraph names in the plan the thesis paragraph it imitates (`<id> Pnn` from `theses/lit-review-skill/codebook/coding/<id>.paragraphs.txt`) and matches its shape: opener kind, length band, argument mode, how studies are reported, closer kind. Only the content is ours. If no thesis paragraph does what the plan wants, the plan changes, not the rule. Prefer models from the closest four; another thesis's paragraph is an acceptable model when the closest four have none on that point.

## Workflow
1. **Scope.** Who you are working with; which section; project report or thesis; whether the text goes to a draft file or to Overleaf. **One section per session.** Set the word budget from `structure.md` (a leaf section about 450 words, a theme with sub-sections about 900) or from the plan, and hold it within ±15 %. A long section is split into two parts that share one plan.
2. **Read** `knowledge/chapter5-brief.md` first, then `structure.md`, `paragraphs.md`, `phrasing.md`, `language.md`, `topics.md`, `themes.md`, `lessons.md`; `guidelines/WRITING_RULES.md`; `knowledge/STATUS.md`; the relevant `knowledge/topics/*.md`; and the `note.md` of every paper you will cite. For claims that matter, the passage in `paper.txt`.
3. **Read two exemplar sections in full, then write observations.** Open the matching sections of two of the closest theses (same theme) in `theses/lit-review-skill/codebook/coding/<id>.paragraphs.txt` and read them whole. Before planning, write five observations into PLAN.md: how the section opens; paragraph length and how paragraphs end; how numbers and uncertainty are stated; how citations are made; how the section closes and links to the thesis. Imitate those patterns; never their sentences. Close the files before drafting.
   **Plan the section** before writing a sentence. Start from the theme's point list in `themes.md`: keep the points that apply, add the ones our papers force, give each its argument mode. For each point, read the matching paragraphs of the closest theses in `theses/lit-review-skill/codebook/THEMES_RESULTS.md` (same theme, same point) and take from them how the point is opened, how far it is hedged, how many findings carry it and how it closes; that is the model for the paragraph, not a sentence of theirs. Save the plan as a comment block at the top of the section's `.tex` as well, so a later session continues from it. Then a table with one row per paragraph: **the model paragraph it imitates (`<id> Pnn`)**, role (from `paragraphs.md`), the point in one line, argument mode (finding / claim-evidence / claim-backup / reasoning), the works that back it (1 / 2 / 3+), whether it carries a limitation, a comparison, a consequence or a link to the thesis, what the last sentence does, and **the "this matters because …" sentence written out** (a row without one is a list, not a paragraph; see `lessons.md`). Claims about the literature as a whole say "many" unless counted. Check the plan against `structure.md`: opener, at most two single studies in a row, at least one comparison and one limitation per theme, a synthesis or gap at the end, the shares roughly met. Show the plan to the user for a new section or a restructure.
4. **Draft** paragraph by paragraph from the plan, each from its blueprint, at about 95 words and four sentences.
5. **Check, before the user sees anything.**
   - `py theses/lit-review-skill/measures/profile_draft.py <file.tex>`: every metric inside the closest-four range, or say why not; split every sentence over 30 words.
   - `py theses/lit-review-skill/measures/tics.py <file.txt>`: no banned pattern; rare ones at most once.
   - **Independent review:** start a separate agent in review mode with `review-checklist.md`, the skill files and the draft (never the plan's "intended" reading, never the earlier drafts). Fix every failed Must item, run the reviewer again, and repeat until it passes. Two rounds are normal; the user is not the first reviewer.
   - For every citation, the checked sentence and page are in CHANGES.
6. **Hand over.** Report the word count against the budget, the profiler's flag count (target at most 4; Bore 2026 scores 1), the reviewer's verdict, every open `\todo` or `% TODO` marker, what was checked against `paper.txt` and what was not, and which keys are missing from the bib. Log in `ai-usage.md`. Push to Overleaf only after the user says so; then update `knowledge/chapter5-brief.md` and STATUS so the next session starts from current facts.

## Review mode
Do not edit. Run the profiler and the tic counter; map each paragraph to a role and compare the section with `structure.md` (openers, runs of studies, comparison and limitation present, closer); check study paragraphs against `paragraphs.md` (finding + dimensions + limitation or relation); list findings as location → problem → fix, structure first, then argument, then citations, then language.

## Known limits
- The grades of the 14 theses are assumed A-level (to be confirmed with the supervisor).
- Citation counts are by regular expression; the codings are about 85 % reliable (two tests, `theses/lit-review-skill/codebook/coding/RELIABILITY.md`); shares are robust, single percentages are not.
- The corpus is 12 reviews; a rule that rests on "Bore" rests on two theses by the same authors.
