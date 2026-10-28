# Philosophical Minority Influence in Multi Agent Moral Decisions

## 1. The question I want to study

I want to understand what happens when AI agents with different philosophical perspectives make a moral decision together. If most of the group prioritizes consequences and one agent prioritizes duties or promises, can that minority perspective change the outcome? And if the group changes its decision, what part of the interaction made a difference?

For example, three agents might consider whether an organization should break a promise to benefit a larger number of people. Each agent would answer privately, exchange a short message with the others, and then answer again. I could compare this with agents who reconsider the same dilemma without seeing anyone else’s views.

A second experiment would look more closely at the arguments. I could show a fresh agent the exact same message with different labels, or different messages with the same label. This would let me separate the effect of the argument’s content from the effect of how I describe its source.

This is a plan for an experiment I have not run. The final scenarios, prompts, sample size, and analysis would be fixed after development and pilot work.

### Working title

**When Does a Moral Minority Matter? Philosophical Perspectives and Influence in LLM Group Decisions**

### Research questions

- **RQ1:** How does discussion change group decisions across neutral, homogeneous, and mixed philosophical groups?
- **RQ2:** Which agents change their decisions after discussion, and how do those changes relate to the minority agent’s initial position?
- **RQ3:** Does a philosophical label change how an agent responds to an otherwise identical argument? What changes when I vary the argument’s content instead?
- **RQ4:** How stable are the results across scenario families, answer order, prompt wording, and different models?

### Connection to prior work

Prior research has already found moral-judgment shifts in LLM groups and differences across interaction protocols. There is also work on philosophical prompting, moral fine-tuning, and role-model influence. The specific question here is how philosophical composition interacts with discussion, followed by a separate test of message content and labels. The related-work document contains the sources, particularly references [3], [4], [8], [10], and [11]. I would need to establish the precise gap through a fuller literature review before making a novelty claim.

The experiment concerns observable decisions under particular conditions. It would not establish that agents genuinely hold the philosophies in their prompts, experience empathy, or make decisions in the same way people do.

## 2. Basic structure

The first experiment would have the following sequence:

1. I give three separately prompted agents the same scenario and their assigned philosophical instructions.
2. Each agent makes an initial decision privately.
3. I assign the group to discussion or private reconsideration.
4. In the discussion condition, agents exchange one short message each in a randomized order. In the reconsideration condition, each agent gets an equivalent opportunity to generate a private reconsideration message without peer input.
5. Each agent makes a final private decision.
6. I calculate the group answer from the final votes and compare outcomes across conditions.

The initial majority gives me a baseline for describing a group’s change. The reconsideration condition gives me a separate comparison for changes that happen simply because the model answers again.

This design does not perfectly isolate every feature of discussion. Agents who discuss receive peer information and additional input tokens. My main comparison would estimate the effect of the full discussion protocol relative to the specified reconsideration protocol. A matched-length placebo-message condition could provide a further comparison, although placebo messages could also influence responses.

## 3. Definitions

**Agent.** One separately prompted model instance within a group. Agents can use the same model weights, but they have separate contexts and generation calls. I would not treat them as independent people.

**Persona.** A fixed prompt that prioritizes particular considerations. It changes the model’s context, not its weights.

**Consequence-focused persona, U.** A prompt asking the agent to consider consequences and aggregate welfare, as an operationalization of a utilitarian-oriented perspective.

**Duty-focused persona, D.** A prompt asking the agent to consider duties, promises, and rights, as an operationalization of a deontological perspective.

**Neutral persona, N.** A prompt asking the agent to weigh the relevant considerations without assigning a particular philosophical framework.

These short prompts would be simplified operationalizations. I would document their wording and check how different phrasings affect responses rather than treat one prompt as a complete representation of a philosophical tradition.

**Minority persona.** The sole D agent in a UUD group or the sole U agent in a DDU group. This describes assigned instructions.

**Minority decision.** A choice initially held by exactly one of three valid voting agents. A minority persona may agree with the initial majority, so I would keep these two definitions separate.

**Group decision.** The majority of the final valid binary votes, using the refusal and missing-vote rules below. There would be no moderator agent and no requirement to reach consensus.

**Influence.** For randomized comparisons, I would report effects of the assigned discussion protocol, message label, or message content. Whether a particular agent’s answer matches the final majority would be a descriptive measure, not proof that it persuaded the group.

**Emergent behavior.** If I use this term, I would specify the group-level pattern and the independent-agent baseline it differs from. A change after discussion would not, on its own, establish a broader emergent capability.

## 4. Outcomes and hypotheses

### Primary decision outcome

For scenarios with a clearly defined welfare-versus-norm conflict, I would identify the action that increases the stated aggregate benefit while violating a specified norm. I would code a valid final group choice as:

- **Y = 1:** the group selects that action.
- **Y = 0:** the group selects the alternative.

This is a scenario-specific action mapping, not a universal morality score. A scenario would enter the primary analysis only if its facts support that coding. Broader moral questions could be included in secondary analyses with different measurements.

### Primary contrast

Let p(g,t) be the average probability of Y = 1 for composition g and interaction condition t, over the defined scenario set and random group draws. I would define the discussion effect within each composition as:

**Δ(g) = p(g, discussion) − p(g, reconsideration).**

My primary contrast would be:

**θ = [Δ(UUD) + Δ(DDU)] / 2 − Δ(NNN).**

This asks whether discussion changes the rate of the welfare-increasing, norm-violating choice differently in mixed groups than in neutral groups. I would weight the two mixed compositions equally. Within each condition, I would average repetitions within a scenario first, then weight scenarios equally.

I would use a two-sided test because I would not assume the direction in advance. A positive or negative θ would describe a composition-dependent discussion effect. It would not directly measure persuasion by a particular minority agent.

### Secondary outcomes

I would report the discussion effect for each composition, differences between UUD and DDU, and outcomes in UUU and DDD groups. Individual-level measures would include switching from initial to final choice, remaining disagreement, and agreement between the final group answer and the minority-persona agent’s initial answer.

I would distinguish all randomized runs from descriptive subsets where the minority initially disagreed. Since persona assignment can affect initial decisions, conditioning on initial disagreement could create a selection problem. Those subset analyses would not establish a causal minority effect across compositions.

### Stage B outcomes

The message experiment would have a label comparison and a content comparison. The primary label comparison would average the difference in final choices between philosophical and neutral labels while holding each argument text fixed. The content comparison would vary U-oriented versus D-oriented arguments under the same neutral label.

These are effects of the selected messages and labels on fresh recipients. They would not automatically explain the mechanism of the live group discussion.

### Testing and uncertainty

I would register θ as the primary Stage A contrast and the label effect as the primary Stage B contrast, with the error rate for each stated explicitly. Secondary families of comparisons would use a stated correction such as Holm’s method, or be labeled exploratory. I would report effect sizes, confidence intervals, and the number of independent scenario families alongside any p-values.

## 5. Scenario selection

### Sources

I could draw suitable dilemmas from sources such as ETHICS and the Greatest Good Benchmark after checking their terms and task fit. Many existing items would not fit the primary welfare-versus-norm outcome. I would include only those with a defensible action mapping, and keep original, adapted, and newly written scenarios clearly identified.

Each scenario record would include its source, version, license, family, intended comparison, action mapping, and any changes I made. Restricted material would not be redistributed.

### Scenario properties

For the primary analysis, each scenario would have two clearly described actions and an explicit conflict between consequences and a norm or obligation. I would document what benefit changes, who is affected, and which norm is at issue. I would not assume that every harmful action is utilitarian or every refusal is deontological.

### Illustrative scenario

A community clinic has promised a family that a reserved appointment will go to their relative. A disruption means that keeping the appointment would help one person, while reallocating the available care would help three people with comparable needs. The scenario stipulates that no other appointments are available and that there is no third option.

- **A:** Reallocate the care, helping three people and breaking the promise.
- **B:** Keep the promise and help one person.

This is an illustrative scenario, not a validated item or a realistic guide to medical allocation. The resource arithmetic, comparable benefits, and relevance of the promise would all need scrutiny before I could use a version of it in an experiment.

### Annotation and splitting

I would define a review rubric for consequences, norms, ambiguity, and suitability for the primary outcome. Independent annotation of a subset would let me measure agreement before adjudication. The coding would be frozen before evaluating confirmatory model outputs.

I would group scenarios by source and shared template, then split whole families into development, pilot, and locked evaluation sets. Paraphrases of the same dilemma would stay together. Answer order would be randomized with its mapping recorded before generation.

Any matched variants would be checked for factual equivalence. New scenarios could reduce dependence on public benchmark items, but I could not guarantee they were unlike anything in a model’s training data.

## 6. Group compositions and interaction conditions

### Persona compositions

| Composition | Instructions | What it lets me compare |
|---|---|---|
| NNN | Three neutral agents | A neutral-group baseline |
| UUU | Three consequence-focused agents | A homogeneous consequence-focused group |
| DDD | Three duty-focused agents | A homogeneous duty-focused group |
| UUD | Two consequence-focused agents and one duty-focused agent | A duty-focused minority |
| DDU | Two duty-focused agents and one consequence-focused agent | A consequence-focused minority |

I would randomly assign personas to positions and balance which position holds the minority role. Prompts would share the same task instructions and response schema, with length and specificity matched as closely as possible. Alternative persona phrasings would be developed separately from the locked evaluation set.

### Discussion

Each agent would make a private initial decision. Agents would then send one short message each in a randomized sequential order. Later speakers would see earlier messages, so speaking order would be recorded and examined. Once all messages were available, every agent would receive the same transcript and vote privately.

Final votes would not be shared until collection was complete. This would avoid having one final vote directly influence another.

### Private reconsideration

Each agent would see the scenario and its own initial response, generate a private reconsideration message, and then make a final private decision. It would not see the other agents’ views. The number of generation opportunities and output-token limits would match the discussion condition, although the input information would differ.

### Assignment and independence

Within each scenario and composition, group instances would be assigned to the two conditions using a recorded randomization procedure. The main design would use independently sampled groups in each condition and scenario-level pairing for analysis. I would not reuse one set of initial answers across multiple continuations and treat those continuations as independent observations.

### Response format

Where supported, I would use a compact JSON schema with `choice`, `brief_rationale`, and `status`. The rationale would be a short explanation, not a request for hidden chain-of-thought or an assumption that the text faithfully describes the model’s internal reasoning.

### Example trace

Initially, the two U agents choose A and the D agent chooses B. The initial majority is A. During discussion, the D agent emphasizes the obligation created by the promise. At the end, one U agent still chooses A, while the other U agent and the D agent choose B. The final majority is B.

I would record one individual switch and one majority shift. This is consistent with minority influence, but the trace would not establish that the minority’s argument caused the change. The comparison conditions and separate message experiment would provide additional evidence.

## 7. Stage B — Message content and philosophical labels

### Purpose

In a live conversation, an agent’s persona, its message, and its position in the discussion vary together. I want a separate experiment where I can hold some of these features fixed.

### Fixed message bank

For each selected scenario, I would prepare one consequence-focused and one duty-focused argument from a development corpus or a documented writing procedure. The arguments would be checked for factual accuracy, position, tone, length, and suitability. I would establish selection rules before examining confirmatory responses and retain the provenance of each message.

The two arguments could be similar in length and tone without being perfectly matched in meaning. Their different content is the intervention, and any conclusions would be limited to that message set.

### Randomized labels

A fresh neutral recipient would see either:

1. An argument labeled as coming from an agent prioritizing consequences or duties, as appropriate.
2. The exact same argument labeled as coming from “another agent.”

For the content comparison, I would compare the two argument types under the same neutral label. Label and answer order would be randomized.

### Recipient workflow

Each recipient would answer privately before exposure, receive one assigned message, and then answer privately again. The comparison between randomized label conditions would use final decisions. A subgroup analysis based on initial disagreement would be defined before message assignment and kept distinct from the full-sample effect.

An optional no-message reconsideration condition would estimate the effect of receiving a message compared with answering again without one.

### Interpretation

Multiple recipients would reuse the same messages, so I would account for dependence by scenario family and message. A label effect would describe the effect of those source descriptions, including any priming. A content effect would describe the selected arguments, not philosophical reasoning in isolation. This recipient-only study would not be equivalent to intervening inside an ongoing three-agent conversation.

## 8. Pilot and sample size

### Pilot

An initial pilot could use 20 development scenarios across five compositions and two interaction conditions:

**20 × 5 × 2 = 200 group runs.**

Each group would use three initial-answer calls, three discussion or private-reconsideration calls, and three final-answer calls. At nine calls per group, the pilot would require approximately **1,800 model calls**, excluding retries, annotation, and Stage B.

I would use the pilot to check parsing, scenario suitability, refusals, time, token use, cost, and whether the persona prompts produce distinguishable patterns on development items. Any prompt changes would happen before I locked the evaluation materials. Pilot results would not be confirmatory findings.

### Illustrative main run

One possible scale is:

**100 scenarios × 5 compositions × 2 conditions × 1 repetition = 1,000 group runs**, or approximately **9,000 calls** with the same workflow.

This is a budgeting example, not a claim that 100 scenarios would provide enough statistical power. The number of independent scenario families, variation between scenarios, and size of the interaction effect would all matter.

For Stage B, a possible scale is:

**40 scenarios × 2 content types × 2 label types × 2 recipients = 320 recipient runs.**

With one initial and one final call per recipient, this would require approximately **640 calls**, excluding any additional control condition. Reusing arguments means that 320 runs would not represent 320 independent messages.

### Power analysis

I would first define the smallest effect I consider scientifically meaningful. I would then use pilot estimates of family-level variation, run-level variation, choice imbalance, and missingness to simulate the actual randomization and analysis. I would examine power and confidence-interval width across plausible effect sizes and sample sizes, including uncertainty in the pilot estimates.

The confirmatory sample size, exclusion rules, and stopping rule would be fixed before the main run. If the available budget did not support adequate precision, I would narrow the question or treat the study as exploratory rather than interpret an imprecise result as evidence of no effect.

### Compute and cost

A metered trial would establish actual token usage and errors. I would estimate cost from input and output tokens multiplied by the current prices for the selected models, with a contingency for retries. I have not assumed a price here.

The initial design could use one model. Replication with a second model would provide a generalization check and increase the call count. Hosted APIs may not support exact reproducibility even when a seed is available.

## 9. Implementation

I would use a Python repository with separate components for model access, orchestration, evaluation, and analysis.

| Component | Contents |
|---|---|
| `data/` | Scenario metadata, family splits, permitted text, action mapping, annotations |
| `configs/` | Model settings, condition assignments, prompt versions, seeds |
| `src/providers/` | A common model interface and a fake provider for deterministic tests |
| `src/experiments/` | Initial votes, discussion, reconsideration, final votes, Stage B |
| `src/evaluation/` | Parsing, action normalization, aggregation, refusal handling |
| `src/analysis/` | Estimators, confidence intervals, plots, sensitivity analyses |
| `prompts/` | Versioned persona instructions and response schemas |
| `tests/` | Context isolation, randomization, option mapping, parsing, resuming, cost accounting |
| `results/` | Run manifests and outputs where sharing is permitted |

The implementation has not been built. A transparent orchestration loop would make it easier to check what each agent can see. The provider interface would allow later comparisons without assuming that different providers expose identical controls.

### Experiment loop

    for scenario in locked_evaluation_scenarios:
        for composition in registered_compositions:
            for arm in randomized_arms:
                for repetition in registered_repetitions:
                    agents = initialize_separate_contexts(composition)
                    initial = collect_private_votes(agents, scenario)
                    if arm == 'discussion':
                        transcript = sequential_messages(agents, randomized_order)
                        final = collect_private_votes(agents, scenario, transcript)
                    else:
                        private_notes = individual_reconsideration(agents, scenario)
                        final = collect_private_votes(agents, scenario, private_notes)
                    save_run_and_all_statuses(initial, final, assignment, metadata)

I would give every run a unique identifier and resume from completed calls without duplicating them. A fixed retry policy would distinguish technical failures from refusals and malformed responses. All retries and original statuses would remain in the log.

## 10. Logging and reproducibility

For each group, I would record scenario and family identifiers, source version, split, action mapping, option order, composition, assigned condition, repetition, persona prompt versions, and speaking order. Model records would include provider, identifier, available snapshot date, generation settings, supported seed, and timestamps.

The output record would retain initial and final choices, permitted transcripts, refusal and error statuses, retries, token use, and cost estimates. A manifest would link the results to the code commit, configuration hash, analysis version, exclusions, and data permissions.

Tests would verify that agents cannot see one another’s private initial votes before sharing begins. API keys would stay outside version control. If a provider changed a model during collection, I would record the change and assess whether those runs could be pooled. Exact wording, version information, and dates would define the scope of any reproducibility claim.

## 11. Refusals and missing outcomes

I would classify responses as `valid A`, `valid B`, `refusal`, `invalid`, or `technical failure`.

A majority requires at least two valid votes for the same choice. A group with A, B, and a refusal is indeterminate. A group with A, A, and a refusal has majority A, with the refusal still recorded. Refusals would never be forced into A or B.

The binary analysis would use valid majority outcomes and report the validity rate for every condition. Since treatment could affect validity, a complete-case estimate could be biased. I would report the full outcome distribution and sensitivity bounds obtained by assigning indeterminate cases to either option under contrasting assumptions.

Technical failures would follow the registered retry policy. I would not repeat runs simply because an answer was unfavorable or unexpected. A blinded audit of raw responses would check parser behavior where feasible.

## 12. Statistical analysis

### Descriptive results

I would report the number of scenarios, families, groups, and valid outcomes, along with costs, model versions, and initial-choice distributions. I would check balance in the recorded assignments and show how often assigned personas correspond to actual differences in initial decisions.

### Primary estimator

For each scenario and composition, I would estimate the final Y proportion in each interaction condition. I would calculate scenario-level discussion differences, average them with the registered weighting, and combine them into θ.

A scenario-family cluster bootstrap would resample families while retaining all associated scenarios, conditions, and repetitions. I would report 95% confidence intervals, raw effects in percentage points, and the number of independent families. With too few families, bootstrap estimates could be unreliable; a larger family sample and sensitivity analyses using randomization inference or a hierarchical model would be important.

Randomization inference would respect the actual assignment blocks. If the design randomly allocates one group to each condition within every scenario-composition block, the permitted permutations would swap those condition assignments within blocks. Individual votes would not be permuted as independent observations. A permutation test of a contrast also requires a clearly specified null; I would not assume that a test of no treatment effect is automatically a test of no difference between composition-specific effects.

### Individual decisions

I would summarize switching by interaction condition, persona, and initial agreement. Analysis would account for dependence among agents in the same group and among related scenarios. Randomized discussion comparisons would include all eligible assigned agents; initially dissenting subsets would be reported descriptively unless a separate identification strategy justified a causal interpretation.

### Stage B

I would compare final-choice probabilities across labels while keeping fixed-message comparisons intact. Inference would retain the dependence among recipients who see the same scenario or message. I would report how many unique arguments were used and examine sensitivity to individual messages. The content comparison would be analyzed separately from the label comparison.

### Robustness

Additional analyses would cover answer order, speaking order, scenario source, prompt wording, model snapshot, alternative weighting, and refusal handling. A placebo-message condition would be analyzed if included. New patterns discovered while reading transcripts would be exploratory until tested on fresh data.

## 13. Qualitative analysis

I would define a coding rubric before examining outputs with their condition labels. Possible codes include mentioning consequences, referring to an obligation, identifying an affected person, acknowledging a counterargument, expressing uncertainty, and explicitly referencing another agent’s point.

These would describe the text rather than provide direct access to hidden reasoning. I would select transcripts across conditions, scenario families, and outcome types using a recorded procedure. Rare refusals could be oversampled for inspection, with weighting if I reported overall population rates.

Independent coding on a subset would allow percentage agreement and a suitable chance-corrected measure, such as Cohen’s kappa for sufficiently common categorical codes. Disagreements and adjudication would be recorded. Selected excerpts would illustrate patterns rather than prove a mechanism. If I later used a model-based judge, I would validate its labels against human annotation and document its limitations.

## 14. Limitations I would need to address

**Simplified philosophies.** Short persona prompts cannot fully represent complex philosophical traditions. I would document the simplification and test alternative wording.

**Demand effects.** Explicit philosophical labels may prime an answer. Stage B would measure one form of this effect rather than remove it.

**Textual choices.** Selecting an option in a dilemma does not establish how an agent would act in an environment with real consequences. A simulator would be a separate study.

**Public benchmarks.** Evaluation items may overlap with training material. Family-level splits and new reviewed items would help, but would not establish complete freedom from contamination.

**Forced choices.** Binary options leave out context and alternatives. Refusals and indeterminate answers would remain visible, and unsuitable scenarios would be excluded by rules fixed before evaluation.

**Different contexts.** Discussion introduces peer text and additional input tokens. My claim would concern the full protocol, with token accounting and an optional placebo comparison.

**Correlated observations.** Repeated responses share model, scenario, and sometimes message text. The analysis would preserve those dependencies.

**Model changes.** Provider updates and generation settings limit generalization. I would tie conclusions to the versions and settings actually tested.

**Selection on initial choices.** A minority persona is not necessarily a minority decision. Conditioning on disagreement after persona assignment would complicate causal interpretation.

**Separate mechanism setting.** A message-label effect in fresh recipients would not fully identify what caused a shift in a live group.

## 15. Working timeline

This is an initial 13-week schedule. Annotation, model access, and sample-size requirements could change it.

| Period | Work |
|---|---|
| Weeks 1–2 | Read the closest literature in full, establish the specific question, inspect datasets, select a model, and check access and usage terms. |
| Weeks 3–4 | Create scenario metadata and family splits; write development prompts; implement model access, logging, tests, and the analysis outline. |
| Weeks 5–6 | Run the pilot; measure token use, variance, validity, and failures; revise development materials. |
| Week 7 | Freeze and preregister prompts, evaluation scenarios, randomization, outcomes, sample size, stopping rules, and analysis. Prepare the fixed-message bank. |
| Weeks 8–9 | Collect the main group data using the registered procedure and retry policy. Monitor technical health and cost. |
| Weeks 10–11 | Analyze group results, complete qualitative annotation, run Stage B, and conduct the specified robustness checks. |
| Weeks 12–13 | Write the thesis, prepare figures and reproducibility materials, and revise the interpretation and limitations. |

Before the main collection, I would need a working pipeline with no context leakage, reliable option mapping, transparent refusal handling, and a sample-size justification. Technical monitoring would not be used to tune hypotheses to favorable outcome trends.

## 16. Thesis structure

A roughly ten-page main text could be organized around the following sections, with detailed materials in appendices where permitted:

1. **Introduction:** the group-decision problem, a concrete example, and the research questions.
2. **Related work:** moral judgments, group discussion, interaction protocols, philosophical personas, and source influence.
3. **Experimental design:** scenarios, compositions, randomization, discussion and reconsideration, and the fixed-message study.
4. **Measurements and analysis:** the primary contrast, missingness, uncertainty, clustering, and annotation.
5. **Results:** the primary estimate, group and individual changes, and label/content comparisons.
6. **Robustness and limitations:** model and prompt dependence, scenario coverage, costs, and uncertainty.
7. **Discussion:** what the findings imply about these group interactions and what remains unresolved.

The appendices would contain prompts, scenario provenance, assignment rules, the annotation guide, statistical details, and additional plots. Planned figures include the study workflow, discussion effects by composition, initial-to-final decision transitions, Stage B contrasts, and scenario-level variation. There are no results for these figures yet.

## 17. Scope still to be settled

I have not yet fixed the model, API budget, available compute, final scenario sample, or publication venue. These will affect the number of repetitions and whether a second model or extra control condition is practical.

This experiment would initially study behavior without fine-tuning. Philosophical training, resource scarcity, impossible goals, and internal representations remain related questions that would require their own interventions and measurements. The immediate task is to define the composition-and-discussion experiment precisely enough that its results would be interpretable whether the effect is positive, negative, or too small to distinguish with the available data.
