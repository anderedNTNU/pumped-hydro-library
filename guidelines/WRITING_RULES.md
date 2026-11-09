# Writing rules (from IØT's "Tips til rapportskriving", Stålhane, 27 Aug 2026)

A checklist distilled from [Rapportskriving-2026.pdf](Rapportskriving-2026.pdf) (text copy: `Rapportskriving-2026.txt`).
Claude follows this for all thesis text. **The supervisor's advice always comes first.**

## Audience and purpose
- [ ] Write for a fellow IØT student in the same specialisation. Theory from the spring of 4th year and autumn of 5th year can be explained. Earlier theory (simplex, branch-and-bound) is assumed known.
- [ ] Explain the application area (power markets, hydropower) well. The reader does not know it.
- [ ] Every section must serve the report's main message. Read your own text as if you knew nothing about the work.
- [ ] Project report and master thesis are graded separately and **must be clearly different**. The master thesis is more focused and original, with less general background.

## Structure (IMRaD; the slides show two possible versions, neither is required)
- [ ] Preface → Summary → Contents / List of Figures / List of Tables (generated automatically) / abbreviations or terminology → Introduction → (Background) → Related literature → Problem description → Mathematical model → Solution method → (Implementation) → Computational study → Concluding remarks → Future research → Appendices → References.
- [ ] **Placement:** no results in the method chapters. No data (numbers) in the model or problem description.
- [ ] A chapter with several sections opens by introducing them.
- [ ] Length: at most about 80 pages (project report) or 100 (master thesis), excluding appendices. Space should match importance.
- [ ] Write about what worked, not the whole story of everything you tried.
- [ ] Recommended order of writing: background → problem description → literature (start reading early) → model → method → results → preface, summary, introduction, conclusion, future research.

## Chapter checklists
**Title:** combine the method area with the application area, avoid repeated words and abbreviations, and use a subtitle for the method if useful. The master thesis title appears on the diploma.

**Preface:** short. Course name and code, thanks to supervisor and partners. For the master thesis: refer to the project report, say the thesis continues it, and **declare reused text** (self-plagiarism guidelines, IØT 10.04.2024).

**Summary / abstract:** at most 1 page, hourglass structure: background and motivation → knowledge gap → aim and method → main results and contributions → wider implications. The master thesis needs both an English and a Norwegian version.

**Introduction (usually 1.5–4 pages, non-technical, should spark interest):**
1. Why the topic matters
2. The research context, with high-level references
3. The motivation for the research
4. A short problem description and the research questions (high-level purpose, then operational aim: what and how)
5. Contributions and results
6. An outline of the rest of the report

**Background:** the application area, the industry and key facts and figures. Introduce terminology. It should support the problem description.

**Literature review:**
- [ ] Two purposes: (a) give an overview of the field, and (b) **position our work**, arguing that it is new and that our modelling and method choices make sense. Students often neglect (b).
- [ ] Use the **5 C's: Cite, Compare, Contrast, Critique, Connect.** Don't just list papers.
- [ ] Open by saying how the review is limited, how it is organised and how papers were found (see `literature/search-log.md`).
- [ ] Compare papers along several dimensions. A summary table comparing them with our work is encouraged.
- [ ] Use peer-reviewed, recognised journals. Treat arXiv, SSRN and ResearchGate with care. Check journal quality (Norwegian register: level 2 is best; ABS list).
- [ ] Project report: focus on the problem. Master thesis: methods can get more attention.

**Problem description (usually 1–2 pages, no data, an indication of scale at most):**
- [ ] Imagine explaining the problem to someone in 5 minutes, so they could then formulate the model: the setting, the input, the objective, the constraints, the decisions and what a solution looks like.
- [ ] Order: overall purpose → entities and their properties or input data → relations and interactions → decisions → how decisions are evaluated (the objective, in words).
- [ ] Separate **problem assumptions** (included here) from **modelling assumptions** (in the model chapter).

**Mathematical model:**
- [ ] Sections: modelling assumptions → modelling approach (e.g. discrete time, SDDP stages) → notation → model → extensions or alternatives.
- [ ] State every modelling assumption and choice (discrete or continuous time, end-of-horizon effects, ...). Figures help.
- [ ] Notation tables (indices, sets, parameters, variables) for large models.
- [ ] **Indices and variables in lowercase, parameters in uppercase, sets in uppercase `\mathcal{}`.** Use superscripts for multi-letter names. Limit Greek letters unless they are standard in the field. Use notation common in the literature.
- [ ] Declare every symbol you use, and no symbol you don't.
- [ ] The only numbers allowed in the formulation are logical ones (0 and 1). For big-M, state how tight a value should be.
- [ ] Every index in a constraint is either summed over or covered by "for all".
- [ ] Present the model all at once, by part, or one constraint at a time, depending on its size. The full model can go in an appendix.

**Solution method:** motivate the choice of method first (not "because the supervisor suggested it"), with references to its successful use elsewhere. Explain it at two levels: an overview (a flowchart) and then the details (pseudocode, abstract but complete).

**Implementation:** only if needed (many packages, or an instance generator). Otherwise briefly at the start of the computational study.

**Computational study:** introduction (purpose, the research questions restated, structure, software and hardware) → instances → technical study (solution time, gap, convergence) → economic study (managerial insights).

**Concluding remarks (1–2 pages, different from the summary):** the problem and method very briefly, main contributions, main results, and their significance. Then answer the research questions in detail: how close did we get, and what did we learn?

**Future research:** more important in the project report than in the master thesis. Extensions to the model and method, and new elements in the problem.

**Appendices:** A, B, ... (A.1, A.2). Full notation and models are welcome, but **no code**. Code goes to the supervisor, commented. Anything uploaded to Inspera is public, so no confidential data.

## Language
- [ ] Prefer active voice. Use present tense ("Fagerholt (2004) finds…"), consistently. Be careful with "will".
- [ ] Vary the verbs (constraints *ensure, enforce, state, link*), but **never vary defined terms** (e.g. always *discharge*, never *release* as a synonym).
- [ ] Precise, short sentences. Define abbreviations at first use. Don't use too many of them.
- [ ] Refer to "the project report" and "the master thesis".
- [ ] Number the pages. Avoid footnotes. Check spelling and grammar.

## Figures and tables
- [ ] **Table captions go above tables; figure captions go below figures.** Captions must be descriptive.
- [ ] Label axes, with units. Use consistent precision in numbers, and bold/italic used appropriately.
- [ ] Put our own (best) results in the rightmost column. Use explicit units ("seconds", not "time"). Include averages.

## Citations
- [ ] Author–year: "Fagerholt (2001) describes…", "Andersson et al. (2012)", "(Bertazzi and Speranza, 2012)". Not [1].
- [ ] One consistent style. BibTeX entries from Zotero. Poor referencing hurts the overall impression.
- [ ] **When in doubt, cite** (to avoid any suspicion of plagiarism).

## AI use
- [ ] A filled-in KI-deklarasjonsskjema is uploaded to Inspera with the project report and the master thesis. Keep `ai-usage.md` up to date.
- [ ] Follow NTNU's rules: https://i.ntnu.no/wiki/-/wiki/Norsk/Kunstig+intelligens+i+bachelor-+og+masteroppgaver
