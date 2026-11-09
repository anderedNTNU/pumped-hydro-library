# CLAUDE.md: Pumped hydro source library

This repo belongs to three NTNU IØT students, **Anders Drillestad, Markus Langholm and Karoline Årland**. It holds the sources for their project report (TIØ4500, autumn 2026) and master thesis (spring 2027), *Pumped Hydropower: Uncertainty-Aware Modelling of Long-Term Storage in the European Power Market*. It is a clean start: it holds the sources only, not the earlier project work (see `README.md`).

## Layout
| What | Where |
|---|---|
| Papers: PDF, text copy, structured note | `literature/papers/<bibkey>/` (`paper.pdf`, `paper.txt`, `note.md`) |
| Grey literature (ENTSO-E, Statnett, NVE, IEA, …) | `literature/grey-literature/<bibkey>/` (`source.pdf`, `source.txt`, `note.md`) |
| Master list | `literature/INDEX.md` (generated) |
| Papers by method / by topic | `literature/by-method/<tag>.md`, `literature/by-review-section/<tag>/papers.md` (generated) |
| Note template | `literature/_templates/paper-note.md` |
| Sources still missing; search log | `literature/WANTED.md`, `literature/search-log.md` |
| Reference theses | `theses/` (see `theses/README.md`) |

Read `paper.txt` rather than the PDF, because it is faster. Never copy or closely paraphrase a thesis's text.

## Adding a paper
1. **Bibkey.** Take it from the group's Zotero library (Better BibTeX: `auth.lower + year + shorttitle(1,0).lower`, e.g. `lohndorf2013sddp`). Never make up a key. If the paper is not in Zotero, ask the user to add it first.
2. **Files.** Create `literature/papers/<bibkey>/` with `paper.pdf`, then run `pdftotext -layout paper.pdf paper.txt`. If the text is empty, the PDF is a scan.
3. **Note.** Copy the template to `note.md` and fill in every field, with page numbers for key claims. Use only the tags below.
4. **Regenerate** with `bash literature/_tools/regenerate.sh`, and fix any tag warnings.
5. **Commit** as `lit: add <bibkey>`.

Never invent references, page numbers or results. Mark uncertain claims **(unverified)**.

## Tags
To add a tag, add it here and create the matching `by-method/` file or `by-review-section/` folder in the same commit.

`methods:` `deterministic-lp-milp`, `two-stage-stochastic`, `multistage-scenario-trees`, `dynamic-programming`, `sdp`, `sddp-markov-chain`, `sddp-time-series`, `benders-decomposition`, `risk-averse-cvar`, `adp-reinforcement-learning`, `uncertainty-modelling`, `heuristics-simulation`, `hydro-production-function`.

`review_sections:` `ldes-seasonal-storage`, `phs-technology`, `electricity-markets`, `price-volatility`, `modelling-phs-plants`, `market-participation`, `reservoir-sizing-capacity`, `research-gap`.

Generated files keep any text above the line `<!-- GENERATED BELOW -->`; never edit below it by hand.

## Git
Small, descriptive commits. Never force-push or rewrite history.
