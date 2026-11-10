# Language and citations in a literature review

Targets measured on the 12 literature reviews of the reference theses (`theses/lit-review-skill/measures/REPORT.md`, `BANNED.md`). Figures are medians, with the closest-four range in brackets. Aim for the median; stay inside the range. `py theses/lit-review-skill/measures/profile_draft.py <file>` checks a draft against all of them.

## Size
| Metric | Target | Closest-four range |
|---|---|---|
| Share of the thesis prose | 11–15 % | 6–21 % (the two Bore theses: 20–21 %) |
| Words | about 2,700 | 1,550–3,600 |
| Paragraphs | about 28 | 14–36 |
| Level-2 sections (themes) | 5 | 1–6 (Bore: 6, incl. search strategy and contribution) |
| Words per leaf section | about 450 | 240–570 |
| Paragraphs per leaf section | 3 | 1–9 |
| Distinct works cited | about 30 | 13–32 |
| Words per distinct work | about 115 | 64–120 |

## Paragraphs
| Metric | Target | Range |
|---|---|---|
| Words | 95 | 91–104 (median per thesis); single paragraphs 30–200 |
| Sentences | 4 | 1–11 |
| Citations | 1 (median); 0 in a quarter of paragraphs, 3+ works in a fifth | |
| Start with an author name | under 10 % | 0–18 % |
| Refer to the thesis itself | about 15 % | 7–18 % |
| Contain a number with a unit or % | under 10 % | (all theses: 15 %) |

## Sentences
| Metric | Target | Range |
|---|---|---|
| Median length | 21–22 words | 20–22 |
| Over 35 words | under 5 % | 3–11 % |
| Hedges per 1,000 words (may, often, typically, likely, seems …) | about 8 | 4–10 |
| Connectors per 1,000 words (however, therefore, in contrast, although, whereas …) | about 11 | 10–14 |
| Numbers with a unit or % per 1,000 words | about 1.5 | 0–3 |

## Citations
- Narrative ("Helseth et al. (2016) found …") and parenthetical citations about half and half in the author–year theses.
- About 1.8 citations per 100 words; one work per citation is the norm. Group citations of three or more works appear in about one paragraph in five, to show that a point is established.
- No page numbers in citations.
- Present tense for what studies show ("find", "report", "show", "propose", "present", "demonstrate" are the common verbs); past tense only for the search procedure.

## Words the reviews never use (banned; corpus rate 0 in 36,000 words)
nuanced, foster, seamless, pivotal, paramount, delve, underscore (as a verb), notable, landscape, key role; it is worth noting, importantly, interestingly, in this context, to this end, in essence, in general, in summary; "this highlights/demonstrates/shows that", "these findings suggest/show", cannot be overstated, a growing body of, neither … nor; em-dash or spaced en-dash as a parenthesis; "(i) … (ii) …" lists in prose; "it is possible that", "to some extent".

## Words the reviews use at most about once per chapter (use sparingly)
vital, robust, numerous, a wide range of, leverage, utilise, facilitate, ensure, holistic, insight; it is important to note, notably, in recent years, taken together, as such, in particular, in conclusion, building on this, the following, "as discussed in"; not only / but also, serves as, plays a role, respectively; potentially, possibly, seems, appears, tends to, arguably, relatively, somewhat, generally, usually; moreover, similarly, nonetheless, accordingly, on the other hand, conversely, specifically, ultimately.

## Words the reviews do use, at these rates per 1,000 words (closest four)
however 2.7 · while 4.0 · may 2.3 · often 1.7 · although 1.3 · whereas 1.0 · both … and 1.8 · thus 0.9 · consequently 0.8 · in contrast 0.8 · highlight 0.9 · various 0.8 · significant 0.8 · the importance of 0.8 · therefore 0.6 · furthermore 0.6 · crucial 0.6 · overall 0.5 · further, 0.7 · in addition 0.4.

## Rules that follow
1. One paragraph, one point, stated in the first sentence; studies come after the point, not before it.
2. Studies are grammatical subjects and get active reporting verbs; do not stack citations at the end of a sentence.
3. A number only where its size carries the argument, and only after the text has said that numbers from different studies are not directly comparable.
4. End a paragraph on what the point means (a consequence, a limitation, or a link to the thesis), not on the last study's finding, in about half the paragraphs.
5. Never a paragraph that only lists what studies did. Never a paragraph that opens with "Author (year)" when the previous one did.
6. Hedge findings from one case ("may", "appears to", "in their case"); do not hedge what several studies agree on.

## Calibration of the profiler (2026-11-10)
`profile_draft.py` counts flags against the closest-four range, size metrics excluded. The reference reviews score: Bore 2026 **1**, Bore & Brensholm 3, EMPIRE 4, Norland 7; the eight reviews outside the closest four 8–16 (they are the range's outsiders by construction). Claude's v7 scored 12 and the first 5.3.1 draft 9. **Target for a draft: at most 4 flags, none on sentence length, paragraph length, hedges or connective openers.** A text can pass and still read badly; the reviewer checklist comes after the numbers, not instead of them.

## Where Claude's drafts differ from the closest four (contrast set: v7 and the first 5.3.1 draft, `theses/lit-review-skill/measures/GAPS.md`)
| Metric | Closest four | Claude v7 | Claude 5.3.1 v1 | Rule |
|---|---|---|---|---|
| Median paragraph words | 95 [91–104] | 119 | 120 | four to five sentences, under 110 words |
| Sentences over 35 words | 4 % [3–11] | 13 % | 4 % | split anything over 30 |
| Sentence-length s.d. | 8.2 [7.4–9.3] | 10.7 | 7.1 | vary length: p10 about 12, p90 about 32; do not chop every sentence to the same size |
| Sentences over 40 words | 1.6 % [1.3–4.5] | 6.9 % | 0 % | keep one or two long sentences per section, none over 45 |
| Hedges per 1,000 | 7.7 [4.4–10.3] | 3.6 | 8.3 | about one per paragraph |
| Boosters per 1,000 (clearly, significantly, particularly, crucial, essential, key …) | 5.4 [4.1–7.1] | 1.6 | 0 | about one per paragraph; the theses do call things important and significant |
| Connectors per 1,000 | 11 [10–14] | 6.4 | 13 | |
| Sentences opening with a connective | 29 % [26–30] | 1 % | 7 % | **every third or fourth sentence starts with However, While, Although, Consequently, Furthermore, In contrast, Similarly …** This is the largest single gap. |
| Colons per 1,000 | 0.55 [0.3–0.6] | 2.8 | 3.3 | no colon-led lists in prose; at most one colon per section |
| Semicolons per 1,000 | 0.75 [0–3.6] | 2.3 | 13 | at most one or two per section |
| Paragraphs referring to the thesis | 16 % [7–18] | 4 % | 20 % | |
| "we/our/us" per 1,000 | 0.3 [0–2.3] | 0.2 | 0 | the theses say "this thesis", "the authors", seldom "we" |

**Words Claude overuses relative to the reviews** (from the contrast set, topic words removed): because, every, same, together, known, only, small, find/finds, gain, keep/keeps, reduces, raises, falls, matters, little, considerably, "rather than", therefore, whereas, report/reported, assess.
**Words the reviews use that Claude's drafts avoid:** however (2.3 vs 0.5 per 1,000), while (3.1), approach, results, found, method, framework, solution, using, based, been, important, often, different, through, provide, one, section, value, research, potential, increase.
