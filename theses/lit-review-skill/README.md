# Evidence behind the `literature-review` skill (D-002)

The skill itself is `.claude/skills/literature-review/`. This folder holds what it rests on and the scripts that rebuild it.

| Path | Content |
|---|---|
| `measures/measure.py` | counts chapter, section, paragraph and sentence metrics of the 12 literature reviews in `theses/corpus/segmented/` → `REPORT.md`, `units.csv`, `sections.csv`, `paragraphs.csv` |
| `measures/tics.py` | rate per 1,000 words of candidate writing tics in the reviews and in any draft → `BANNED.md` |
| `measures/profile_draft.py` | measures a draft `.tex` or `.txt` the same way and flags metrics outside the closest-four range |
| `codebook/CODEBOOK.md` | paragraph codebook v1.1 (role; opener; works backing the point; limitation; comparison; consequence; link; closer; number; study attributes) |
| `codebook/coding/extract.py` | writes the numbered paragraphs of each review |
| `codebook/coding/<id>.coder1.csv` | the coding of each review (Bore 2026 by the session's Claude; the others by Claude Sonnet agents from the codebook alone) |
| `codebook/coding/compare.py`, `RELIABILITY.md` | reliability tests: Bore 2026 double-coded (role 86 %, kappa 0.83; all fields ≥ 81 %); 30-paragraph spot-check of the agent codings (role 87 %; all fields ≥ 83 % with B7 merged) |
| `codebook/coding/<id>.points.csv`, `themes.py` → `codebook/THEMES_RESULTS.md` | part E: each paragraph's point in one line, argument mode (finding / claim-evidence / claim-backup / reasoning / description), findings reported, theme; the basis of the skill's `themes.md` |
| `codebook/coding/aggregate.py` → `codebook/CODING_RESULTS.md` | shares per role, structure field and study attribute, for all 12, the closest four and the two Bore theses |

Validation so far (2026-11-10): held-out size metrics: 60 of 72 inside the range of the other ten (empire-2024 and hope-kvamme-2025 are the outliers, both far from our topic); the profiler places Bore 2026 inside every closest-four range and flags our v7 on length, paragraph length, long sentences, hedges, connectors and self-reference. Still to do: rewrite one subsection of chapter 5 with the skill and have Anders judge it against Bore.

Rebuild: `py measures/measure.py`, `py measures/tics.py`, `py codebook/coding/aggregate.py` (Python 3.12, standard library).
