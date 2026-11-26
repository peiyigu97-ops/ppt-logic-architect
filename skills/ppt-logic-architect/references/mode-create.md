# Mode A - CREATE

Build a complete presentation architecture from scattered material: notes, documents, data, papers, images, transcripts.

## Procedure

### 1. Analyze the input (Phase 1)
Read every source. Give each an ID. Do not skim; a source that is not read is reported as "not read" rather than silently dropped.

### 2. Extract and classify (Phase 1)
For each meaningful item, record its type and source:

| Type | Test |
|---|---|
| Fact | Stated by a source and checkable, e.g. "The device weighs 142 g (S3, spec sheet)" |
| Data | A measurement, with its method and conditions |
| Claim-by-source | Someone's assertion, not independently supported here |
| Assumption | Taken as true without evidence |
| Open question | Unknown or unverified |
| Noise | True but serves no likely argument (record it; decide later) |

Keep numbers exactly as the source gives them, with units and conditions. If two sources disagree, record both and flag the conflict. Do not average them away.

### 3. Fix purpose, audience, central question (Phase 1)
- **Purpose / decision**: what should be different after the presentation? Inform, persuade, get a decision, get approval, earn a grade, win a project?
- **Audience**: who, what they already know, what they must decide, what they will doubt.
- **Central question**: the one question the deck answers for this audience. If you cannot write it as a question, the purpose is not yet clear.

Infer from the material where possible. Ask only what the material cannot answer.

### 4. Build the central thesis (Phase 2)
The thesis is the answer to the central question, in one sentence. Test it:

1. **Is it a claim?** A topic ("Our research on X") is not a thesis.
2. **Could it be wrong?** If nobody could disagree, it says nothing.
3. **Does the evidence support exactly this?** Check population, conditions, metric, and strength of language.
4. **Does it answer the central question, and only that?**
5. **Is it scoped?** State where it stops holding.

If the evidence supports only a narrower thesis, write the narrower thesis. Say what you narrowed and why.

### 5. Build the logic tree (Phase 2)
Thesis, then supporting arguments (usually two to five), then evidence. Use `references/pyramid-principle.md` for the structure and `references/method-selection.md` to decide whether MECE, SCQA, or a research chain applies. Link each leaf to `E#`. A branch with no evidence gets a `G#`. Write the objections a sceptical audience member would raise and where the tree answers them.

### 6. Design the sections (Phase 3)
Choose the ordering principle on purpose, and say what it is:

| Ordering | Fits |
|---|---|
| Answer first, then support (top-down) | Decision-makers, short time, executive audiences |
| Problem, then cause, then solution | Persuasion and proposals |
| Question, method, results, interpretation, limits | Research and technical reports |
| Chronological or process order | Design process stories, case studies, post-mortems |
| Simple to complex | Teaching and explanation |
| General to specific | Reviews and overviews |

Ordering is a choice with a reason, not a default. Each section gets a role in the argument and a one-sentence section claim.

### 7. Build the progression (Phase 3)
Between every pair of adjacent sections, name the relation: *because*, *therefore*, *however*, *for example*, *which raises the question*, *so we then need to...*. If you cannot name it, the order is arbitrary or a section is missing.

### 8. Generate the slide cards (Phase 4)
One complete card per slide (ten fields). Allocate slides from the budget: a rough rule is one to three minutes per content slide depending on density, but treat it as a heuristic, not a requirement. Put supporting detail the audience may ask for in the appendix.

### 9. Audit (Phase 5)
Run `references/logic-audit.md`. Fix Critical issues in the phase that caused them.

### 10. Deliver (Phase 6)
Fill the five templates with the approved content.

## CREATE-specific traps

- **Material-driven structure**: the deck mirrors the order of the notes. Structure follows the argument, not the source.
- **Everything goes in**: each fact feels too good to drop. Use the cut list and the appendix.
- **Thesis written last**: a deck assembled from topics, with a "conclusion" bolted on. The thesis comes in Phase 2, before sections.
- **Evidence stretched to fit**: a thesis stronger than the data. Narrow the thesis.
- **Gaps hidden**: a weak spot smoothed over with confident wording. List it and let the user decide.
