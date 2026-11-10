# Review checklist for a drafted section

Run by a reviewer who did not write the draft (a separate agent in review mode), with `structure.md`, `paragraphs.md`, `themes.md`, `lessons.md` and this file, and the draft. The reviewer reports every failed item as location → problem → fix. The writer fixes and the reviewer runs again; the draft is handed to the user only when every item under **Must** passes.

## Must (each paragraph)
| # | Check | Fails when |
|---|---|---|
| M1 | One point, stated in the first sentence | the first sentence names a study and the paragraph then wanders; or two points share a paragraph |
| M2 | The point is argued, not listed | the paragraph says what studies did and never says what it means (no consequence, limitation or implication sentence) |
| M3 | No claim beyond the sources | "all", "most", "the literature agrees", "typically" without several agreeing studies or a count; "cannot", "must" where the choice exists |
| M4 | No generalisation from one study | a sentence of the form "X matters more than Y" or "dependence has little effect" that rests on a single case; must read "in their case" or "varies between cases" |
| M5 | Every study earns its place | a study appears only as an exception, an aside or a definition, and does not carry the paragraph's point for our problem |
| M6 | Every cited claim matches the paper | the CHANGES file has no passage for it, or the passage says something narrower |
| M7 | Length | paragraph over 110 words, or any sentence over 30 words |
| M8 | Numbers | a number from one study that does not change the argument; any number before the comparability caveat |
| M9 | Banned words absent; rare words at most once in the section | see `language.md` |
| M11 | Links to the thesis state relevance only | a sentence says what our model does ("the present study keeps …", "our model uses …") instead of why the finding matters for the thesis; model description belongs in the contribution section |
| M10 | Closer | the last sentence restates the first, or ends on the last study's finding when the paragraph is a claim or group |

## Must (the section)
| # | Check | Fails when |
|---|---|---|
| S1 | Opens with the plain reason the theme matters, in one or two sentences | opens with a study, a mechanism, or a definition the background already gave |
| S2 | At most two single-study paragraphs in a row | |
| S3 | At least one comparison of named studies and at least one limitation attached to a named study | |
| S4 | Ends on a synthesis or on what the theme leaves open, and the synthesis claims only what the section showed | the synthesis introduces a new claim or generalises (M4) |
| S5 | Points and their order match the theme's list in `themes.md`, or the deviation is explained in PLAN.md | |
| S6 | Each paragraph's argument mode (finding / claim-evidence / claim-backup / reasoning) matches what the closest theses use for that point (`themes.md`) | a point the theses argue with evidence is given as a bare claim with backup, or a synthesis cites studies |
| S7 | Word count within ±15 % of the budget in PLAN.md; profiler flags at most 4, none on sentence length, paragraph length, hedges or connective openers | |
| S8 | Rhythm as in the theses: sentence lengths vary (s.d. 7–9, one or two sentences over 35 words), every third or fourth sentence opens with a connective, about one hedge and one booster per paragraph, at most one colon and two semicolons in the section | sentences chopped to one size; no connective openers; no boosters; colon-led lists |
| S9 | Every number and finding carries `% src:` on its line, and facts about our own work match `knowledge/chapter5-brief.md` | |

## Should (report, do not block)
- Shares roughly as in `structure.md`: about half the paragraphs open with a claim, a fifth cite 3+ works, a third state a limitation, a third draw a consequence, a quarter refer to the thesis.
- Hedges 4–10 and connectors 10–14 per 1,000 words; narrative and parenthetical citations about half and half.
- The first sentences of the paragraphs, read in order, make the argument of the section on their own.

## Output format
```
PASS/FAIL
M2 ¶3: lists which prices each study models; no sentence says why it matters → add "this lets the policy …" or cut the list
M4 ¶5: "dependence matters for operation rather than revenue" rests on Kleiven alone → "in their case"
S1: opens with a mechanism sentence → open with why uncertainty matters in plain terms
```
