---
bibkey: wohlin2014guidelines
bibkey_provisional: true
title: "Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering"
authors: "Claes Wohlin"
year: 2014
venue: "Proceedings of the International Conference on Evaluation and Assessment in Software Engineering (EASE '14), London, 13-14 May 2014, ACM"
peer_reviewed: true
methods: []
review_sections: [research-gap]
relevance: medium
read_by: []
added: 2026-11-04
takeaway: "Standard method reference for snowballing literature search: choose a diverse start set (e.g. via Google Scholar), iterate backward (reference lists) and forward (citations) snowballing with full-text inclusion decisions before reuse, stop when no new papers appear; replication found the same papers as a database-driven SLR."
source_path: C:/Users/Anders/code/pumped-hydro-workspace/literature/inbox/07_Metode_Benders_og_litteratursok/75_Wohlin_2014_Guidelines_for_snowballing_in_systematic_literature_studies.pdf
---

# Guidelines for snowballing in systematic literature studies (Wohlin, 2014)

_Page numbers below are PDF pages 1-10 of the conference paper (the PDF has no printed page numbers; ACM article number 38 is from memory, unverified). DOI 10.1145/2601248.2601268._

## Research question / purpose
- (1) Formulate a systematic snowballing procedure for systematic literature studies; (2) illustrate and evaluate it by replicating a published SLR (MacDonell et al.) (p. 1).
- Definitions: snowballing uses "the reference list of a paper or the citations to the paper to identify additional papers"; using references = **backward**, using citations = **forward** snowballing (p. 1).

## Setting
- Software-engineering SLRs; method is domain-independent. Replication topic: cross-company vs within-company effort estimation (p. 4).

## Method (the procedure, Figure 1, p. 4)
1. **Start set (pp. 2-3):** find a tentative start set, e.g. with Google Scholar to avoid publisher bias (p. 2). Good start set: covers different communities/clusters, not too small, diverse publishers/years/authors, built from research-question keywords plus synonyms; a seminal highly cited paper may help (p. 3). Only papers finally included count as the start set (p. 2).
2. **Iterations (p. 3):** for each included paper, do backward snowballing (screen reference list by basic criteria such as language, year, publication type; then title, venue, authors; then the place and context of the citation; then abstract and full text) and forward snowballing (citations in Google Scholar, screened the same way). Decide inclusion on the full paper *before* using it for further snowballing, otherwise rollbacks are needed; do one iteration at a time for traceability (p. 3).
3. **Stop** when an iteration finds no new papers; then contact authors and/or scan key venues (p. 4).
4. **Data extraction** can be done at the time of the inclusion decision (p. 4).

## Data / case
- Start set: 13 candidates from one Google Scholar query, 3 included (p. 5). Iteration 1: 7 new papers; iteration 2: 1; iteration 3: 0 (pp. 5-7). Final 11 papers; the same studies as the original two SLRs (p. 9).
- Efficiency: 3.7% of all candidates included overall; 6.8% when trivially excluded (year/title) candidates are removed (p. 7).

## Key findings
- (p. 2) Database searches depend on search strings; non-standard terminology makes them miss papers or return much noise; snowballing is an alternative first step.
- (pp. 8-9) Ten lessons learned, e.g. exclusion on basic criteria is fast (1); overlapping references signal coverage or a cluster (2); track how many new papers each iteration yields, which should decrease (7); if not, search again with synonyms (8); build a citation matrix (9) and timeline (10).
- (p. 9) Replication outcome matched the database-search SLRs; detailed-review effort similar.
- (p. 9) Snowballing "should not necessarily be seen as an alternative to database searches"; combining approaches is preferable. Snowballing is especially suited to *extending* an existing review.
- (p. 10) Conclusion: systematic snowballing is a viable starting point instead of always starting with database searches.

## Strengths
- Concrete, step-by-step, widely cited guideline; directly reusable as our documented search method.

## Weaknesses / limitations
- One replication only, in a small field where every paper cites the others (p. 9); the author had read the original study (validity threat, p. 9); start set had one common author (p. 5).

## Use it for… (lookup guide)
| Use in our thesis | What the paper provides | Where in the paper (page/section) |
|---|---|---|
| Lit. review: Literature Search and Scope, define snowballing | Backward vs forward snowballing definitions | p. 1, Sec. 1 |
| Lit. review: how the start set was chosen | Start-set criteria (diversity, synonyms, Google Scholar) | pp. 2-3, Sec. 3.1 |
| Lit. review: procedure description | Iteration steps, inclusion before reuse, stopping rule | pp. 3-4, Sec. 3.2-3.4, Fig. 1 |
| Lit. review: why not only database searches | Terminology problems with search strings | p. 2, Sec. 2 |
| Lit. review: limitations of our search | Cluster risk; combine with database search | pp. 8-9, lessons 2, 8; Sec. 5 |

## Useful quotes (with page numbers)
> "Snowballing refers to using the reference list of a paper or the citations to the paper to identify additional papers." (p. 1)

## Follow-up references to check (backward snowballing)
- Kitchenham and Charters (2007), Guidelines for performing SLRs in software engineering (ref. [7]).
- Webster and Watson (2002), MIS Quarterly, analysing the past to prepare for the future (ref. [2]).
- Jalali and Wohlin (2012), systematic literature studies: database searches vs. backward snowballing (ref. [19]).

