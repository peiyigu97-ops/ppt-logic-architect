# Mode C - AUDIT

Review the logic of an existing deck or outline. **Do not rewrite it.** The output is a report: what is wrong, where, why it matters, and what kind of change would fix it.

## What AUDIT will and will not do

| Will | Will not |
|---|---|
| Reconstruct what the deck actually argues | Produce a replacement deck, outline, or rewritten slides |
| Rate each problem Critical, Major, or Minor | Reorder slides or propose a new section structure |
| Say where, why, impact, and the kind of fix | Invent evidence to patch gaps |
| Note what works so it is preserved | Silently fix anything |

A suggested fix describes the change in a sentence or two ("add the baseline condition to slide 9 or narrow the claim to the tested range"). It is not a rewritten slide. If the user wants the rewrite, offer RESTRUCTURE after the report.

## Procedure

### 1. Inventory (Phase 1)
Same slide table as RESTRUCTURE: number, title, type, claim, evidence, apparent role. Read speaker notes. State up front what the audit covers: **only what is in the file provided.** An argument the presenter will make aloud, but that is nowhere in the slides or notes, cannot be audited; say so rather than treating the absence as a flaw or as a defence.

### 2. Reconstruct the as-is argument (Phase 2)
Write the thesis the deck appears to hold, the supporting arguments, and the evidence given, as a short tree. Read the deck charitably first (the strongest sensible interpretation), then audit that reading. This prevents the audit from attacking a version of the deck the author never meant.

If no thesis can be identified, record it as a Critical finding (core argument unclear) and audit the supporting structure against the most plausible candidate thesis, stated explicitly.

Show the reconstruction at the Phase 2 gate. If the user corrects it, the audit changes with it.

### 3. Audit (Phase 5)
Use `references/logic-audit.md` for the passes and the issue taxonomy. Cover all ten audit questions:

1. Is the core thesis clear?
2. Do the supporting arguments support it?
3. Is the evidence sufficient, for each claim, as worded?
4. Does the section progression feel natural?
5. Are there logical jumps?
6. Is any cause-effect reversed or unsupported?
7. Are any concepts confused or used inconsistently?
8. Is information repeated without purpose?
9. Are key questions left unanswered?
10. Do conclusions go beyond the evidence?

For design and engineering decks, also run the research-to-solution checks in `references/design-research-reasoning.md`.

### 4. Report (Phase 6)
Fill `templates/logic-audit-report.md`. Every finding has:

- **ID** and **Severity**: Critical / Major / Minor
- **Location**: slide numbers (and quote the exact wording where it matters)
- **Issue type**: from the taxonomy
- **Specific cause**: what exactly is wrong, not "the logic is weak"
- **Potential impact**: what the audience would conclude wrongly, or what the presenter will not be able to defend
- **Suggested fix**: the kind of change, in a sentence or two

## Severity

| Level | Definition | Typical examples |
|---|---|---|
| **Critical** | The central thesis, or a decision that rests on it, is unsupported or contradicted. The audience would reach a wrong or unjustified conclusion | No identifiable thesis; the main conclusion goes beyond the only evidence; the key causal claim is correlation only; a contradiction between the headline result and a data slide |
| **Major** | A supporting argument is weakened, or credibility or comprehension is significantly damaged, but the thesis may survive | A missing baseline; a jump between sections; a key term used two ways; an unanswered obvious question |
| **Minor** | Local clarity, redundancy or wording issues with no effect on the conclusion | A duplicated slide; a topic-label headline on a slide whose evidence is otherwise sound; inconsistent numbering |

Calibrate honestly. Do not inflate severity to look thorough, and do not downgrade a problem to be polite. Do not pad the report: a clean deck gets a short report.

## AUDIT rules

- Findings must cite the deck. A finding that can't point to a slide or a passage is an opinion, not a finding.
- Distinguish **unsupported** (the deck gives no evidence) from **contradicted** (the deck's own evidence says otherwise). They are not the same severity.
- Distinguish "this is wrong" from "this is not shown". The second is a gap in the deck, not necessarily an error in the research.
- Include a short **What works** section, so the author keeps the strengths.
- Include the **unanswered questions** a sceptical member of the stated audience would ask.
- Never ask the user to approve rewrites you were not asked to make.
