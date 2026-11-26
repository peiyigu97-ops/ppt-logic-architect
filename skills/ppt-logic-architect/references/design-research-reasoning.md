# Design Research & Engineering Reasoning

A module for decks that move from investigation to a designed or engineered solution: industrial design, interaction design, product-service systems, hardware prototyping, HCI research, engineering research, design portfolios, and academic defenses.

The central question of this module: **does each step in the chain actually follow from the one before it, and is the evidence for each step of the right kind?**

## 1. The chain

```
Research Question
 -> Research Method
 -> Research Findings
 -> User Insights
 -> Design Requirements
 -> Concept Development
 -> Technical Feasibility
 -> Prototype
 -> Testing
 -> Iteration
 -> Final Solution
 -> Validation
```

Each arrow is a **transformation** that needs a reason. Most weak design decks have a break at one of these arrows. Use the table below to check them.

| Stage | What it contains | What it must be able to say |
|---|---|---|
| **Research Question** | What is being investigated, and why it matters | A question that research could answer, not a solution in disguise ("how can we make a better handle?") |
| **Research Method** | How evidence was gathered | Why this method fits the question; sample; conditions; limits |
| **Research Findings** | What was observed, in the form it was observed | Observations and data, separate from interpretation |
| **User Insights** | Interpretation of findings: what they mean | Which findings support it, and the reasoning from findings to insight |
| **Design Requirements** | What the solution must do, derived from insights | Each requirement traces to an insight; stated as a testable criterion where possible |
| **Concept Development** | Options generated to meet requirements | Which requirements each concept addresses; why options were chosen or rejected |
| **Technical Feasibility** | Whether the chosen concept can work | Calculation, test, precedent, or expert input; not "we think it's possible" |
| **Prototype** | What was built, and what it was built to find out | The **hypothesis** the prototype tests; what fidelity and why |
| **Testing** | What was done with the prototype | Protocol, participants or conditions, metrics, and success criteria set beforehand |
| **Iteration** | What changed because of the tests | The test result that triggered each change |
| **Final Solution** | The resulting design | Which requirements it meets and how; what it does not meet |
| **Validation** | Evidence that the solution meets the original need | Evidence against the original requirements, not just "users liked it" |

Not every project has every stage, and the order can loop. The question is not whether the stages are present, but whether the **links** that are claimed hold.

## 2. Eight checks

Run these in Phase 5 and in AUDIT mode for any design or engineering deck.

### Check 1. Do the findings really support the insight?
For each insight, list the findings behind it. Look for:
- an insight with no finding (it is an assumption);
- an insight resting on one participant or one quote;
- an insight that restates the designer's prior belief;
- findings that cut the other way and were not mentioned.

### Check 2. Can each insight be turned into a design requirement?
A requirement should be derived from an insight and be specific enough to judge a design against. "Should be intuitive" is not a requirement; "a first-time user completes setup without help within a stated time" is closer. Flag insights that never become requirements (so why are they in the deck?) and requirements that come from nowhere.

### Check 3. Do the requirements explain the chosen design?
For the final concept, trace each major design decision to a requirement. A design decision with no requirement behind it is a preference. That is allowed, but it must be labelled as a design decision, not presented as research-driven.

### Check 4. Is the technical route supported by feasibility evidence?
Look for the basis: a calculation, a bench test, a precedent with comparable conditions, a supplier specification, or an expert opinion. "The sensor will be accurate enough" without any of these is an assumption. Check that the **conditions** of the evidence match the design's conditions (load, temperature, cycle count, tolerances, cost target).

### Check 5. Did the prototype verify the key hypothesis?
Ask what the prototype was built to find out. A prototype that is only a better-looking model proves nothing about the hypothesis. Check whether the fidelity matches the question: a looks-like model cannot validate function; a works-like rig cannot validate perceived quality.

### Check 6. Do the test results support the final conclusion?
Compare what the test measured with what the conclusion says. Look for:
- success criteria defined *after* seeing results;
- small or friendly samples;
- tasks easier than real use;
- measures that stand in for the claim (task time for "usability");
- results mixed or negative in places that the conclusion does not mention.

### Check 7. Is there a jump from research straight to form?
The most common design-deck break: a research section, followed by a styled concept, with no requirements and no reasoning between. Test: can the audience say *why this form* rather than another, using only what the deck has shown? If the reason is "the designer's judgment", say so; judgment is legitimate, but it is not the same as a research finding.

### Check 8. Are untested hypotheses presented as findings?
Look for wording such as "users need", "users prefer", "this solves", "this will improve" with no test behind it. A design assumption is allowed, if it is labelled as one and, ideally, shows how it was or will be tested.

## 3. Evidence types in design and engineering

| Evidence | Good for | Not good for |
|---|---|---|
| Interviews, observation (qualitative) | Understanding context, needs, reasons | Estimating how common something is |
| Surveys | Prevalence among respondents, stated preferences | Observed behaviour; causes |
| Usage logs or measured behaviour | What people actually do | Why they do it |
| Competitive or benchmark analysis | Positioning and gaps | User needs by itself |
| Expert opinion | Feasibility and risk, early | Proof of performance |
| Calculation or simulation | Feasibility within model assumptions | Real-world behaviour, if the model is untested |
| Bench test | Component or subsystem performance under stated conditions | Real user conditions |
| Usability test | Whether tested users can use it in test tasks | Long-term use; market success |
| Field test or pilot | Real-world performance in the sampled setting | Generalization beyond the sample |
| Preference test (A/B, ranking) | Relative preference in the test | Actual purchase; the reason |

Match the evidence type to the claim. A survey cannot support "users struggle with X in practice"; a lab bench test cannot support "reliable in daily use".

## 4. Variants by project type

### Industrial design
Watch the research-to-form break. Needed: requirements that constrain form (ergonomic, manufacturing, cost, brand), a basis for form decisions, and testing with physical models. Keep aesthetic judgment labelled as design judgment.

### Interaction design and HCI
Needed: tasks and users defined; a prototype fidelity that fits the question; metrics tied to the claim (success, errors, time, subjective ratings, and what each can and cannot say); the sample and its limits. Beware of treating satisfaction scores from a small sample as significance.

### Product-service systems
Needed: stakeholders and touchpoints mapped; the claim of value for each stakeholder; a view of the whole service journey, including back-end operations; feasibility of the service, not just the artefact. Beware of showing only the front-end experience.

### Hardware prototyping
Needed: a clear hypothesis per prototype; build-test-learn cycles with what each taught; requirements to verification mapping; tolerance, power, thermal, cost, and manufacturability evidence where relevant. Beware of "it works on the bench" stated as "it works".

### Engineering research
Needed: research question, hypothesis, method, controls, results with uncertainty, interpretation, limitations. Beware of claims beyond the tested range, missing baselines, and single runs.

### Design portfolio
The portfolio argues a **designer's capability**, not a single product. Per project, show the key decision and the reasoning behind it. Across projects, show range and depth with a curation logic. Cut projects that repeat the same demonstration of skill. Beware of a gallery of outcomes with no reasoning.

### Academic defense
The deck argues a **contribution**. Needed: gap in the literature, research question, method justification, findings, contribution stated against prior work, limitations, future work, and a backup section for likely committee questions. Beware of a methodology chapter that does not connect to the results, and conclusions that exceed the data.

## 5. Typical breaks, and the fix to propose

| Break | Symptom | Fix (kind of change) |
|---|---|---|
| Research to form | Findings slide, then a rendered concept | Insert insights and requirements; show how the concept meets them |
| Insight with no finding | "Users want X" with no data | Link to findings, or label as hypothesis |
| Requirement from nowhere | A spec number with no source | Trace it to an insight or constraint, or mark it as a design decision |
| Hypothesis as result | "Users prefer the rounded form" with no test | Test it, or reword as a hypothesis |
| Prototype without a question | A model shown as validation | State the hypothesis it tests; add the test |
| Test without criteria | Results reported with no pass/fail line | State criteria set beforehand, or note they were post hoc |
| Friendly sample | Team members as test participants | Disclose, and limit the claim |
| Positive-only reporting | Only wins shown | Include failures and what changed |
| Iteration with no cause | "Version 3" with no reason | Tie each change to a test result |
| Validation by opinion | "Users loved it" | Link validation to the original requirements |
| Feasibility by assertion | "Manufacturable" with no check | Add the calculation, supplier input, or precedent |

## 6. Using the chain in the phases

- **Phase 1**: classify the material by stage. Which stages have evidence and which have none?
- **Phase 2**: the thesis is often a claim about the final stage ("Design X meets requirement set R for user group U"). The logic tree is the chain, with evidence at each link.
- **Phase 3**: sections usually follow the chain, but compress stages the audience does not need, and expand stages that carry the weight of the argument.
- **Phase 4**: each card names its stage and its link to the one before.
- **Phase 5**: run the eight checks.

A design deck does not have to follow the chain in strict order. A portfolio may lead with the outcome. The chain is a **test of the reasoning**, not a mandatory slide order.
