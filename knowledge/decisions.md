# Decisions

Append-only, newest at the bottom. If a decision is reversed, add a new entry that says "supersedes D-xxx".
Decisions from before the fresh start are in the old repo (`pumped-hydro-workspace/knowledge/decisions.md`); bring one over only if the group confirms it again.

Format:

```
## D-001 — YYYY-MM-DD — <short title>
**Decided:** ...
**Why:** ...
**Alternatives considered:** ...
**Source:** session log / supervisor meeting / paper
```

## D-001 — 2026-11-09 — Literature chapter v5 structure
**Decided:** The literature chapter draft v5 uses six parts: scope and search; valuation of pumped storage and its capacities; uncertainty and price dynamics; market participation; solution methods (plant detail woven in); research gap and positioning. Methods (SDP, SDDP, two-stage, rolling horizon) are first named in the methods part. The draft is kept as a separate file in `drafts/literature-review-v5/`, not in Overleaf.
**Why:** Four thematic parts as in Bore & Brensholm (their 4.2–4.6); v4 mixed what is asked (perspective, capacities) with how it is modelled, and had thin sections over the same studies.
**Alternatives considered:** keep v4's eight parts; a separate part on physical modelling (seven parts); replace or merge with the Overleaf v10 (ch. 4).
**Source:** session with Anders 2026-11-09 (handoff of v4).

## D-002 — 2026-11-10 — A new literature-review writing skill, built from the 14 reference theses
**Decided:** Build a new skill for writing the literature review (chapter 5), from scratch, from the 14 theses in `theses/`. It covers both *how* a review is written (chapter and subsection structure, paragraph blueprints, how studies and their limitations are reported, sentence and citation ranges) and *what* a review in our field covers (topics, from the closest theses). Rules rest on the consensus of all reviews; where the corpus splits, the closest four decide (Bore 2026, Bore & Brensholm 2025, EMPIRE 2024, Norland 2025); where they split, the two Bore theses decide. Every rule states which of the three it rests on. Literature review only to start; other chapter types later if it works. Scripts measure what can be counted; paragraphs are coded with a short codebook tested by a second independent pass first. Validation: two held-out reviews, the profiler must prefer Bore 2026 over our v7, then one subsection of chapter 5 rewritten and judged by Anders. Skill at `.claude/skills/literature-review/`; evidence under `theses/lit-review-skill/`.
**Why:** The v4–v7 drafts and today's rewrites of 5.2 were judged "way off" against Bore & Brensholm; the group wants text that matches the A-level theses in structure and density, with the rules visible and measurable.
**Alternatives considered:** reuse the thesis-writing skill built in the old workspace on 2026-11-08/09 (rejected by Anders: start fresh, do not consider it); all chapter types at once (rejected: too big to judge).
**Source:** session with Anders 2026-11-10.

## D-003 — 2026-11-11 — Research questions narrowed to the pump
**Decided:** The research questions are (1) how a conventional reservoir hydropower plant can gain from adding a pump; (2) how the charging capacity (pumping power) affects the value of a long-duration energy storage such as pumped storage; (3) how these values change with the volatility and persistence of electricity prices. Working wording in `knowledge/chapter5-brief.md`; chapter 1 fixes the final text.
**Why:** Anders' decision of 2026-11-11. The earlier wording varied pumping power, generating power and reservoir capacity jointly; the group narrows it to the pump, which is the decision a reservoir owner actually faces, and frames the plant as long-duration storage.
**Alternatives considered:** keep the three-capacity question (rejected: too wide for the project report); drop the price-behaviour question (rejected: it is the group's distinct contribution).
**Source:** session with Anders 2026-11-11.
