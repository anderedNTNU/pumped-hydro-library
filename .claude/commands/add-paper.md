---
description: File a paper: folder, text copy, structured note, tags and generated lists.
argument-hint: <bibkey> or <path to PDF>
---

Add this paper to the library: $ARGUMENTS

1. **Bibkey.** Pull `../pumped-hydro-thesis` and look the paper up in `references.bib`. Use its exact key.
   - If it is not there and Zotero is running on this machine, add it yourself via the local connector (CLAUDE.md, "Zotero"). Otherwise ask the user to add it to Zotero.
   - Never make up a key.
   - Grey literature (ENTSO-E, NVE, Statnett, IEA, …) goes in `literature/grey-literature/<bibkey>/`, with `source.pdf` and `source.txt` instead. The rest of the steps are the same.

2. **Files.** Create `literature/papers/<bibkey>/` and put the PDF there as `paper.pdf`. Ask the user for the PDF if no path was given.
   Then run `pdftotext -layout paper.pdf paper.txt` in that folder. If the text comes out empty, the PDF is a scan: tell the user.

3. **Read** `paper.txt`: at least the abstract, introduction, method, results and conclusion. Skim the rest.

4. **Note.** Copy `literature/_templates/paper-note.md` to `note.md` and fill in every field. Rules:
   - Tags come only from the list in CLAUDE.md, and a paper can have several.
   - `relevance` is `high` (directly shapes our model or gap), `medium` (comparable work) or `background`.
   - Give page numbers for key claims and quotes.
   - Ask the user who has read it, for `read_by`. If nobody has, leave it empty.

5. **Regenerate** the lists with `bash literature/_tools/regenerate.sh`, and fix any tag warnings.

6. **Commit** as `lit: add <bibkey>`. Push at `/wrap-up`, or now if the user asks.
