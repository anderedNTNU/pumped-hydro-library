# Codebook for literature-review paragraphs (D-002, step 2, v1.1)

v1.1 (2026-11-10): sharpened after the reliability test on Bore 2026 (see `coding/RELIABILITY.md`): CLAIM vs GROUP, the STUDY threshold, B5, B6, B7 and the note that B4 is independent of the role.

Purpose: describe what each paragraph of the 12 reference literature reviews *does* and how it is built, so the skill can state, with shares, what an A-level review paragraph looks like. Coding is by reading; everything countable is left to `measures/measure.py`.

Unit: one prose paragraph from `corpus/segmented/<id>.jsonl` inside the review units of `measures/measure.py`. Code every paragraph on A, B and C. For paragraphs that mention studies, also code D once per study.

## A. Role (exactly one)
| Code | The paragraph mainly … | Typical signs |
|---|---|---|
| OPEN | says what the chapter or section reviews and why, or how the literature was found | first paragraph; no finding; "this chapter", "the following" |
| CLAIM | makes a general statement about the field and backs it with studies | first sentence is a claim without a named study; studies follow as evidence |
| STUDY | explains one study in depth (what it did and found) | one work carries ≥ 3 sentences |
| GROUP | lists several studies that do or find the same thing | a shared point, then 2–4 works with ≤ 2 sentences each |
| COMPARE | sets two or more named studies against each other on a stated dimension | "whereas", "in contrast", "while X …, Y …" between named works |
| CRITIQUE | has the limitation of a study or group as its main point | "however", "did not", "neglects", with the consequence |
| SYNTH | sums up what the theme's literature establishes, without new studies | "overall", "taken together"; few or no citations |
| GAP | says what is missing or what this thesis does about it | "remains", "has not been", "this thesis", "our contribution" |

Tie-break: the role is what the *first and last* sentences serve. A paragraph that opens with a claim and then explains one study is STUDY if the study is the point, CLAIM if the study is only evidence for the opening statement.
- **CLAIM vs GROUP:** GROUP when the point is what the named studies share or do ("several studies have used DE"); CLAIM when the studies are evidence for a statement about the field or the problem ("uncertainty matters, as X and Y show").
- **STUDY threshold:** at least two sentences on one work *and* the work is the point of the paragraph.
- **COMPARE** needs the contrast to be the point; a contrast inside a CLAIM or GROUP paragraph is coded in B4 only.

## B. Structure (one value each)
| Field | Values | Question |
|---|---|---|
| B1 opener | claim / study / transition / question | What does the first sentence do? *claim* = a statement about the field or problem; *study* = names a work and what it did; *transition* = links to the previous paragraph or announces the topic |
| B2 backing | 0 / 1 / 2 / 3+ | How many distinct works support the paragraph's main point? |
| B3 limitation | none / named / group | Is a limitation stated, of a named study or of the studies as a group? |
| B4 compare | yes / no | Are two named studies set against each other? Independent of the role: a CLAIM or GROUP paragraph can have B4 = yes |
| B5 consequence | yes / no | *yes* only if a sentence states what the point means for modelling, for a decision or for the thesis, with an evaluative or modal verb ("should", "must", "is important for", "implies", "may lead to", "which matters because"). A restated finding, a pointer to a section, or "as this subsection shows" is *no* |
| B6 link | none / implicit / explicit | *explicit* = names this thesis, this study, our model, the research questions, or the authors' own earlier project; *implicit* = refers to the thesis's own sections or to "the methodology adopted" without naming the thesis; *none* otherwise |
| B7 closer | consequence / study / claim / limitation / pointer | What does the last sentence do? *pointer* = announces what follows or refers to a section, table or figure |
| B8 number | yes / no | Does it give a number with a unit or a percentage from a study? |

## C. Theme position (one value)
| Field | Values |
|---|---|
| C1 | first / middle / last paragraph of its leaf section, or only |

## D. Per study mentioned (STUDY, GROUP, COMPARE, CRITIQUE; one row per work)
Tick each attribute the paragraph reports about the work:
| Attribute | Example of what counts |
|---|---|
| aim | what the study set out to do |
| method | model type, algorithm, formulation |
| case | plant, system, country, data |
| markets | which products or markets are modelled |
| uncertainty | which inputs are stochastic and how |
| horizon | planning horizon or time resolution |
| finding | what it found, in words |
| number | a result with a unit or % |
| limitation | what it did not do or where it falls short |
| relation | explicit relation to another named work ("builds on", "unlike", "confirms") |
| use | what it means for this thesis |

## Coding rules
1. Read the whole paragraph before coding A. Decide A first, then B, then D.
2. Code what the paragraph *does*, not what it is about. A paragraph about SDDP that compares two SDDP studies is COMPARE.
3. B2 counts works that back the *main* point, not every citation (a citation for a definition does not count).
4. B3 *named* needs a named study and a stated shortcoming; "limited research exists" is GAP, not a limitation.
5. B5 *yes* needs a sentence that draws a consequence; restating the finding is *no*.
6. When unsure between two codes, pick the one the last sentence supports, and note the doubt in a `note` column.

## Output format
One CSV per thesis, `coding/<id>.csv`, columns:
`thesis, section, pos, role, b1_opener, b2_backing, b3_limitation, b4_compare, b5_consequence, b6_link, b7_closer, b8_number, c1_position, studies (D rows as "work: attr,attr;work: attr"), note`

## Reliability test (before coding the other eleven)
1. Code Bore 2026 (36 paragraphs) once.
2. A second coder, on another model, codes the same 36 from this file alone, without seeing the first coding.
3. Compare A and B1–B8 paragraph by paragraph. Target: ≥ 80 % agreement on A and on each B field. Below that, sharpen the definitions here and repeat on Bore & Brensholm 2025.
4. Record both codings and the agreement in `coding/RELIABILITY.md`.

## What the skill will take from this
- Shares of each role per theme section and where in the section they sit (all / closest four / Bore two).
- How often a paragraph opens with a claim and backs it with 1, 2 or 3+ works; how often a limitation is attached and to what; how often the paragraph ends on a consequence; how often it links to the thesis.
- Which attributes a study paragraph reports, and how many.
- These become the paragraph blueprints and the checklist in the skill, each with the share it rests on.
