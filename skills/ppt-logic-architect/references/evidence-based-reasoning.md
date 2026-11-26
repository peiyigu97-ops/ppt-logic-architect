# Evidence-Based Reasoning

How claims are supported, how sources are tracked, and how facts, inferences, and assumptions are kept apart. This is the baseline for every deck; it is not optional.

## 1. Claim, Evidence, Warrant

Based on the argument model associated with Stephen Toulmin.

| Element | Question it answers | Example |
|---|---|---|
| **Claim** | What are we asserting? | "Walking accuracy stays within tolerance" |
| **Evidence** | What was observed? | "MAE 2.3 bpm, n=8, treadmill walk" |
| **Warrant** | Why does that evidence support that claim? | "The lab's acceptance threshold is MAE of 3 bpm or less, so 2.3 is within it" |
| **Qualifier** | How far and how sure? | "In a pilot of eight participants, one wrist position" |
| **Rebuttal** | What would make the claim fail? | "Higher cadence, sweaty skin, other wrist positions" |

The warrant is the most commonly missing piece. Audiences accept evidence and claim, then ask "so what?" or "compared to what?". State it.

## 2. Statement types

Label every substantive statement.

| Type | Definition | Test |
|---|---|---|
| **Fact** | Sourced and checkable | Can someone verify it from the source? |
| **Data** | A measurement with method and conditions | Are the method, units, sample, and conditions stated? |
| **Inference** | Reasoned from facts | Can the chain be shown step by step? |
| **Assumption** | Taken as true without evidence | Does the deck depend on it? |
| **Opinion** | A source's judgment | Is it attributed? |

The most common error: **inference reported as data**, and **assumption reported as fact**. Mark inferences as such in headlines and cards ("suggests", "is consistent with") and keep the data separate.

## 3. Evidence status and confidence

| Status | Meaning |
|---|---|
| **Sourced** | Directly supported by an identified source |
| **Derived** | Follows from sourced evidence by stated reasoning |
| **Assumed** | Not supported; the deck relies on it |
| **Missing** | Needed but absent |

| Confidence | Criteria |
|---|---|
| **High** | Direct measurement or strong source; method sound; scope matches the claim; consistent across sources or repeated |
| **Medium** | One source, or a limited sample, or indirect but reasonable; scope partly matches |
| **Low** | Anecdotal, small or biased sample, extrapolated beyond the tested conditions, or secondhand |
| **None** | No evidence (a gap) |

Confidence is how well the evidence supports the claim *as worded*, not how strongly someone believes it. The same data can be High confidence for a narrow claim and Low for a broad one. When confidence is low, narrow the claim rather than raising the confidence rating.

## 4. Scope matching

Check, for each claim and its evidence:
- **Population**: same people, devices, materials?
- **Conditions**: same environment, load, duration, task?
- **Metric**: the measure actually relates to the claim?
- **Time**: long enough for what is claimed?
- **Strength of verb**: "shows", "suggests", "is consistent with", "proves", "causes".

A mismatch on any of these is an evidence-claim gap.

## 5. Source tracking

- Every input gets `S#` (source). Every usable piece of support gets `E#` (evidence), with the exact location in the source (page, section, timestamp, row).
- Every claim gets `C#` and the list of `E#` supporting it.
- Keep numbers and wording exactly as sourced. Put your own calculations in a separate "Derived" row with the calculation shown.
- If sources conflict, record both. Do not choose silently.

## 6. Evidence quality flags

Note any that apply:

| Flag | Concern |
|---|---|
| Single run | No repeatability |
| No baseline or control | Cannot attribute an effect |
| No variance reported | Cannot judge reliability |
| Small sample | Descriptive only; not generalizable |
| Convenience sample | May not represent the target users |
| Selected window | A favourable period, not the full run |
| Survivorship | Only successes are shown |
| Proxy metric | The measure only stands in for what is claimed |
| Self-report | Opinions and recall, not behaviour |
| Unverified citation | Source is cited but not provided |

## 7. Fact, inference, and causation

- **Correlation is not causation.** A causal claim needs ordering, a mechanism, control of alternatives, or an intervention. Say what is missing.
- **An inference chain is weaker than its weakest link.** Show each link.
- **Absence of evidence** (no problems found) is not evidence of absence unless the search could have found them.

## 8. Handling gaps

Record each gap:

```
G#: <what is missing>
Affects: <claims or slides>
To close: <what evidence or work would close it>
Options: narrow the claim | mark as assumption | collect evidence | defer
```

Present options to the user. Do not select "fill with something plausible".

## 9. Never fabricate

Do not invent numbers, sources, quotes, participants, citations, sample sizes, or study results, even when asked to "make it look complete". If a number is needed to illustrate a structure, write `[value needed]`. In examples that must show data, label them clearly as fictional.
