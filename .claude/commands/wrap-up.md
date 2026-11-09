---
description: End the session. Write the session log, update shared knowledge, commit and push.
---

Wrap up this session so the rest of the group knows what happened. Work through these steps in order.

1. **Who and what.** Make sure you know who you worked with (Anders, Markus or Karoline). If you don't, ask. Choose a short kebab-case topic for the session, e.g. `sddp-cuts`.

2. **Sync first.** Run `git pull --rebase --autostash` in this repo. If thesis files were touched, do the same in `../pumped-hydro-thesis`. On a conflict, stop and resolve it with the user.

3. **Check that knowledge was recorded.** Go through the conversation and add anything still missing:
   - decisions → `knowledge/decisions.md`
   - new or answered questions → `knowledge/open-questions.md`
   - notation or terms → `knowledge/glossary-notation.md`
   - topic insights → `knowledge/topics/<topic>.md`
   - papers read or discussed → their `note.md`, then regenerate the lists if tags changed

4. **Write the session log** to `sessions/YYYY-MM-DD_<name>_<topic>.md`, from `sessions/_template.md`. Keep it to about one screen. Link to the files you changed rather than repeating them.

5. **Rewrite `knowledge/STATUS.md`** (do not append to it): where each chapter stands, the model, the top 3–5 next steps and the blockers. Update the "Last updated" line.

6. **Append a row to `ai-usage.md`** with the date, who, the categories, what AI was used for, and whether any text or code went into the thesis.

7. **Commit and push.**
   - **This repo:** `git add -A`, commit as `session: YYYY-MM-DD <name> <topic>`, then `git push`.
   - **Thesis repo**, only if `.tex`, figure or `references.bib` files changed: `git pull --rebase`, commit, `git push` (this goes to Overleaf), then `git push origin HEAD:main` (the GitHub backup).

8. **Report back** in at most 5 lines: what was saved, and anything the user needs to do.
