# Lessons from the user tests

What Anders found wrong in text written with the skill, and the rule each finding adds. Read this after `paragraphs.md`. Each test adds a section.

## Test 1: 5.3.1 Sources of uncertainty (2026-11-10)
The draft followed the plan and the measured shares, passed the profiler after one revision, and was still "a good deal worse than Bore". The faults were in the argument, not the form:

1. **A paragraph that lists what studies do is not an argument.** "A treats X, B adds Y, C keeps only Z" must say what the choice *means*: what a model gains by modelling a further input as stochastic, what it loses by not doing so, and what limits the choice (data, dimensionality). The closest theses' claim-backup paragraphs still end on a consequence. Rule: in a GROUP or CLAIM paragraph, after the studies, write the sentence "this matters because …", and if there is none, the paragraph has no point.
2. **Do not claim more than the sources show.** "All studies …", "most studies …" and "the studies that … all" need a count; without one write "many". "Cannot leave out" is false when the choice exists (inflow can be modelled as known); write "is an important element" and say that both are done.
3. **Do not bring in a case only because it is the exception.** A closed-loop plant without inflow is a different problem and does not belong in a paragraph about inflow uncertainty for our plant. A study enters a paragraph only if it carries the point for our case.
4. **Say what the stochastic strategy is good for, not only that it earns more.** The reader wants the mechanism (a policy that holds across the range of outcomes; the risk the deterministic plan does not see), stated before the numbers.
5. **Prefer the ideal and its limit over a list of variants.** "Ideally every price would be stochastic; each added variable multiplies the states and the data needed" says in two sentences what a list of who-models-what says in five.
6. **Sentence length is the Claude fault the profiler catches first.** The first draft had a 31-word median and 38 % over 35 words. Write the paragraph, then split every sentence over 30 words before running the profiler.

What the profiler could not see: items 1–5. They are argument faults, so the planning step now requires, for each paragraph row, the "this matters because" sentence written out before drafting (see SKILL.md, step 3).

## Test 1, second round (2026-11-10)
7. **Open a theme with the plain reason, not a mechanism sentence.** "Stochastic modelling can give a better representation of reality" was preferred over a sentence about strategies holding up across outcomes. Say why the theme matters in the simplest terms first; mechanisms belong with the study that shows them.
8. **Never generalise from one study.** "Dependence matters for operation rather than revenue" rested on Kleiven alone and was rejected as a general claim. A finding from one case is reported as that case's result ("in their case"); a general statement needs several studies that agree, or is written as "varies between cases".
9. **A comparison paragraph can be shorter and higher-level than the blueprint.** Fewer numbers and examples, one sentence per study, then the point. Numbers from a single study (a correlation of −0.43) rarely earn their place.

## Test 1, third round (2026-11-10)
10. **A link to the thesis says why a finding matters for it, never what our model does.** "The present study keeps price and inflow in joint states" was rejected as odd in the middle of a review. The closest theses link with relevance ("important for the modelling assumptions adopted in this thesis", "helpful in the development of the methodology"); what the model does belongs in the contribution section, the table and the method chapter. Also the group's own rule: the own model only briefly at the end.
