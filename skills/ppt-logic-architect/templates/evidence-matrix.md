# Evidence Matrix

> Template. Makes every claim traceable to its source, and every gap visible. IDs must be consistent across all five deliverables: `S#` sources, `E#` evidence items, `C#` claims, `G#` gaps. Never fabricate a number or source; write `[value needed]`.

## 1. Source register

| ID | Source | Type (paper, data file, interview, spec, image, notes ...) | What it contains | Read? | Reliability note |
|---|---|---|---|---|---|
| S1 | <name / path> | <type> | <summary> | Yes / Partly / No | <e.g. single author, unverified> |

## 2. Evidence items

| ID | Source & location | Statement type (Fact / Data / Inference / Assumption / Opinion) | Content (exact numbers, units, conditions) | Method / sample | Quality flags |
|---|---|---|---|---|---|
| E1 | S1, p.4 | Data | <...> | <n, conditions> | <e.g. single run; no baseline> |

## 3. Claim-to-evidence map

| Claim | Slide(s): page and address (e.g. p.5, 三·1) | Evidence | Status (Sourced / Derived / Assumed / Missing) | Confidence (High / Medium / Low / None) | Scope match? (population / conditions / metric / time / verb) | Notes |
|---|---|---|---|---|---|---|
| C1 | 4 | E1, E2 | Sourced | Medium | Partly: <which dimension does not match> | <...> |

## 4. Assumptions

| ID | Assumption | Used in | Risk if false | How it could be tested |
|---|---|---|---|---|
| A1 | <...> | C#, slide # | <...> | <...> |

## 5. Conflicts between sources

| Item | Source A says | Source B says | Handling |
|---|---|---|---|
| <...> | <...> | <...> | <kept both / asked user / chose A because ...> |

## 6. Gap register

| ID | What is missing | Affects (C# / slides) | What would close it | Options (narrow / assume / collect / defer) | Decision |
|---|---|---|---|---|---|
| G1 | <...> | <...> | <...> | <...> | <user's decision> |

## 7. Coverage summary

- Claims total: <n>   Sourced: <n>   Derived: <n>   Assumed: <n>   Missing: <n>
- Confidence: High <n> / Medium <n> / Low <n> / None <n>
- Slides carrying a Low or None confidence claim: <list>
