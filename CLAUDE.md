# CLAUDE.md: Pumped hydro thesis library

This repo belongs to three NTNU IØT students, **Anders Drillestad, Markus Langholm and Karoline Årland**. It supports their project report (TIØ4500, autumn 2026), which continues into a master thesis (spring 2027):

> **Pumped Hydropower: Uncertainty-Aware Modelling of Long-Term Storage in the European Power Market**

This repo is the group's **shared memory**, started fresh on 2026-11-09 (see `README.md`). Anything worth knowing that comes up in a session goes here, so the next session starts from the same knowledge.

## 1. Start of every session
The SessionStart hook pulls this repo and `../pumped-hydro-thesis` and prints recent activity. Then:
1. Ask who you are working with (Anders, Markus or Karoline) if it is not obvious.
2. Read `knowledge/STATUS.md` and the newest 2–3 files in `sessions/`.
3. If the task touches a paper or topic, read its `note.md` or `knowledge/topics/` file before answering. Do not re-derive what is already written down.

## 2. Where things live
| What | Where |
|---|---|
| Thesis LaTeX source (synced with Overleaf) | `../pumped-hydro-thesis/` (a separate repo, see §6) |
| Papers: PDF, text copy, structured note | `literature/papers/<bibkey>/` (`paper.pdf`, `paper.txt`, `note.md`) |
| Grey literature (ENTSO-E, Statnett, NVE, IEA, …) | `literature/grey-literature/<bibkey>/` (`source.pdf`, `source.txt`, `note.md`) |
| Master list; papers by method and by topic | `literature/INDEX.md`, `literature/by-method/`, `literature/by-review-section/` (all generated) |
| Sources still missing; search log | `literature/WANTED.md`, `literature/search-log.md` |
| Reference theses (14) | `theses/` (see `theses/README.md`) |
| IØT report-writing guidance | `guidelines/`; **always follow `WRITING_RULES.md`** |
| Decisions, open questions, notation, topics, status | `knowledge/` |
| One log per Claude session | `sessions/` |
| AI usage record (for NTNU's KI-deklarasjon) | `ai-usage.md` |

Read `paper.txt` rather than the PDF, because it is faster. **Never copy or closely paraphrase a reference thesis.**

## 3. Recording knowledge (most important rule)
Write things down **as they happen**; do not wait for `/wrap-up`.
- **Decision** → append it to `knowledge/decisions.md` with the date, what was decided, why, and the alternatives rejected. Never delete one; reverse it with a new entry.
- **Open question** → `knowledge/open-questions.md`. When it is answered, move it to Resolved with the answer and date.
- **Notation or terms** → `knowledge/glossary-notation.md`. Check it before introducing any symbol.
- **Topic insight** → `knowledge/topics/<topic>.md`, linked from `knowledge/topics/README.md`.
- **Paper read or discussed** → its `note.md` (use `/add-paper` for new ones).

Keep entries short and factual, and cite with bibkeys (`[lohndorf2013sddp]`). Mark uncertain claims **(unverified)**. Never invent references, page numbers or results.

## 4. Literature
- **Bibkeys:** new papers follow Better BibTeX's `auth.lower + year + shorttitle(1,0).lower` (e.g. `lohndorf2013sddp`). Papers already cited keep their existing keys. Always take the key from `../pumped-hydro-thesis/references.bib`; never make one up.
- **Adding a paper:** follow `/add-paper`.
- **Generated lists:** `INDEX.md`, `by-method/*.md` and `by-review-section/*/papers.md` are rebuilt from the notes' tags with `bash literature/_tools/regenerate.sh`. Never edit below `<!-- GENERATED BELOW -->` by hand.
- **Tags:** use only these. To add one, add it here and create the matching `by-method/` file or `by-review-section/` folder in the same commit.
  - `methods:` `deterministic-lp-milp`, `two-stage-stochastic`, `multistage-scenario-trees`, `dynamic-programming`, `sdp`, `sddp-markov-chain`, `sddp-time-series`, `benders-decomposition`, `risk-averse-cvar`, `adp-reinforcement-learning`, `uncertainty-modelling`, `heuristics-simulation`, `hydro-production-function`.
  - `review_sections:` `ldes-seasonal-storage`, `phs-technology`, `electricity-markets`, `price-volatility`, `modelling-phs-plants`, `market-participation`, `reservoir-sizing-capacity`, `research-gap`.

## 5. Zotero
`references.bib` in the thesis repo is exported automatically from Zotero ("Mitt bibliotek") by Better BibTeX. **Never edit it by hand.**

When Zotero is running on this machine, Claude may add a missing paper itself through the local connector:
1. **Check it is running.** `curl http://127.0.0.1:23119/connector/ping` must answer "Zotero is running". The local API (`/api/...`) is not enabled, so the library cannot be searched this way.
2. **Check the library.** POST `{}` to `/connector/getSelectedCollection` and confirm the selected library is "Mitt bibliotek".
3. **Check for duplicates.** The connector cannot do this, so grep `references.bib` for the DOI and the key first.
4. **Add the item.** Fetch the metadata from Crossref by DOI. POST `{"sessionID", "uri", "items": [Zotero JSON item]}` to `/connector/saveItems`, with `extra: "Citation Key: <bibkey>"` to pin the key. Success returns 201.
5. **Push.** Better BibTeX updates `references.bib` within about 10 seconds. Check the diff, then commit and push the thesis repo (§6).

If Zotero is not running, ask the user to add the paper.

## 6. The thesis repo and Overleaf
`../pumped-hydro-thesis/` is connected **directly to Overleaf over git**:
- **Remotes:**
  - `overleaf` (branch `main`) is the **source of truth**, so plain `git pull` and `git push` go to Overleaf;
  - `origin` (GitHub `anderedNTNU/pumped-hydro-thesis`) is a **backup mirror only**.
- **Pull often:** people write in Overleaf at the same time, so run `git pull --rebase` right before editing a `.tex` file and again right before committing.
- **Scope:** edit only the chapter(s) the user asked for.
- **Push:** commit, then `git push`, then `git push origin HEAD:main`. Tell the user which files changed.
- **Rejected push:** pull and rebase, resolve any conflict with the user, and push again. Never force-push to Overleaf.

## 7. Writing thesis text
- **Rules:** read `guidelines/WRITING_RULES.md` before drafting or reviewing any thesis text, and follow it.
- **Audience:** a fellow IØT student in the same specialisation. Assume optimisation basics; do not assume they know power markets or hydropower.
- **Draft, don't take over.** Text you write is a draft for the students to rework. They are graded on their own work and must declare AI use, so log substantial drafting in `ai-usage.md`.

## 8. End of session
When the user says they are done, or runs `/wrap-up`, follow `.claude/commands/wrap-up.md`. If the user seems to be leaving without wrapping up, remind them. The SessionEnd hook commits and pushes leftovers as a safety net, but it does not write the summary.

## 9. Git
- **Commits:** small and descriptive, e.g. `lit: add lohndorf2013sddp`, `knowledge: decide weekly stages`, `session: 2026-11-10 anders`.
- **Merge conflict:** stop, show the user both versions, and resolve it together. Never discard someone else's text.
- **History:** never force-push and never rewrite history.
