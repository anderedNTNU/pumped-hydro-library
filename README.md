# Pumped hydro: source library

This is a clean start for the TIØ4500 project and master thesis of Anders Drillestad, Markus Langholm and Karoline Årland (NTNU IØT, 2026–27). The thesis is *Pumped Hydropower: Uncertainty-Aware Modelling of Long-Term Storage in the European Power Market*.

It holds:
- **`literature/`**: 131 papers and 61 grey-literature sources, each in its own folder with a PDF, a text copy and a structured note;
- **`theses/`**: 14 reference theses, with text copies, one profile per thesis and a segmented corpus;
- **`guidelines/`**: IØT's report-writing guidance;
- **`ai-usage.md`**: the AI usage record for NTNU's KI-deklarasjon, carried over in full;
- **`knowledge/`** and **`sessions/`**: decisions, open questions, notation, status and session logs, started empty.

## Setup
1. Clone this repo and `pumped-hydro-thesis` next to each other:

   ```
   code/
     pumped-hydro-library/
     pumped-hydro-thesis/
   ```
2. Open `pumped-hydro-library` in Claude Code. The SessionStart hook pulls both repos.

It was copied on 2026-11-09 from `pumped-hydro-workspace` (commit `6870edd`), which is kept as it was. The following were left behind on purpose, so the group can start fresh:
- the earlier decisions, open questions and session logs;
- literature syntheses and the comparison table;
- the writing skill and its playbooks;
- the parts of each paper note that tied it to the old drafts ("Relation to our work", "Citation check").

The PDFs in the untracked `literature/inbox/` were not copied either.

See `CLAUDE.md` for how the library is kept.
