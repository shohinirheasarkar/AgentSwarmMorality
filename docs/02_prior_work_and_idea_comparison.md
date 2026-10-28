# Thesis Ideas and Related Research

I want to understand how my questions connect to existing research and what an experiment could add. This document brings together the prior work I have identified, the specific questions I am interested in, and an initial implementation outline for each direction. The review is a starting point rather than an exhaustive account of the literature. The experiments described here have not been run.

## 1. Emergent behavior in agent swarms

### Prior work

Park et al.’s *Generative Agents* explores simulated social interaction using memory and reflection [1]. *Cooperate or Collapse* introduces GovSim, an environment where agents share a renewable resource and must balance using it now against sustaining it over time [2]. The latter also examines universalization-based reasoning. These papers give me examples of how to turn a broad question about collective behavior into an observable interaction with explicit rules.

### What I want to explore

I am interested in the difference between a group’s behavior and what I would expect from its members acting independently. If agents converge on a position, I want to know whether interaction caused the convergence or whether most of them already preferred that answer. I could focus on one behavior, such as cooperation, polarization, or the influence of a minority argument, and compare it with a clearly defined baseline.

### Initial implementation

I could begin with three separately prompted instances of one model. Each would answer privately, exchange messages, and answer again. I would log the messages, speaking order, and initial and final choices. Separate groups would reconsider without peer messages, giving me a comparison for changes that happen without interaction. Repeated scenarios would let me measure how often each group-level pattern occurs.

### Open questions

The meaning of “emergent” depends on my baseline. A difference after discussion would establish an interaction effect in this setting, but not necessarily a broader emergent capability. Longer-term social learning would require a design that actually includes memory or learning across episodes.

## 2. Individual versus group moral decisions

### Prior work

*Many LLMs Are More Utilitarian Than One* reports changes in moral judgments when models deliberate in groups, including increased acceptance of certain norm violations in personal dilemmas [3]. *Interaction Protocol Shapes Moral Judgment in Multi-Agent Debate* examines how the structure of debate affects judgments and consensus [4]. Together, these papers show that both interaction and the way a discussion is organized are relevant to my question.

### What I want to explore

I want to look beyond whether a group’s answer changes and examine whose position it changes toward. Does the initial majority usually win? Can an initially dissenting agent change the outcome? Do different protocols preserve disagreement or encourage convergence? I could also test whether those patterns depend on the philosophical perspectives assigned to the agents.

### Initial implementation

I would collect three private initial decisions, assign groups to discussion or private reconsideration, and collect three private final decisions. The group answer would be the majority of the final votes. I would compare the treatment effects across scenario categories and group compositions, recording refusals and indeterminate votes separately. A follow-up could expose fresh agents to fixed arguments to test particular message features.

### Open questions

A basic individual-versus-group comparison would overlap with existing work. My possible contribution is a more specific explanation of when group decisions change. A transcript where an agent repeats another agent’s point is useful evidence to inspect, but it does not by itself prove that the point caused the switch.

## 3. Measuring morality and model tendencies

### Prior work

The ETHICS benchmark covers justice, well-being, duties, virtues, and commonsense morality [5]. The Greatest Good Benchmark focuses on utilitarian moral dilemmas [6]. *Evaluating the Moral Beliefs Encoded in LLMs* measures choices, uncertainty, and consistency in ambiguous situations [7]. These offer different ways to operationalize moral judgment, each with its own assumptions about the task and what a response represents.

### What I want to explore

I want to describe moral decisions along several dimensions rather than assign each model one overall score. For example, a model could prioritize aggregate benefits in one scenario while strongly protecting a promise in another. I am interested in whether those patterns remain consistent across paraphrases, response formats, and interaction with other agents.

### Initial implementation

I would select suitable scenarios after checking their sources and usage terms. For each, I would define the relevant consequences, norms, and action mapping before collecting responses. I could randomize answer order, repeat questions, and use matched scenario variants. A coding rubric would capture features of the explanations, with independent annotation on a subset and agreement measured before adjudication.

### Open questions

These measurements would describe responses under particular conditions, not establish a model’s true beliefs or a universal ranking of morality. A cross-model comparison becomes more informative if it also explains how stable the differences are and which features of the experiment change them.

## 4. Philosophical personas and moral minorities

### Prior work

The group-judgment and protocol studies [3,4] establish important comparisons for this direction. Research on exemplars examines how agents respond to role models [8], while work on ethical-framework prompting and structured debate provides other relevant methods [9,10]. Giving agents different personas is therefore a starting point; the question is what I can isolate about their interaction.

### What I want to explore

If two agents prioritize consequences and one prioritizes duties, when does the minority perspective influence the final group decision? I want to separate three things that can otherwise get mixed together: the perspective assigned to an agent, the argument it produces, and the label attached to that argument. I am also interested in whether a minority persona actually produces a minority decision; these are not necessarily the same.

### Initial implementation

I could run a discussion experiment with neutral, homogeneous, and mixed groups, using private reconsideration as a control. In a second stage, fresh recipient agents would receive fixed, reviewed arguments. The same argument could appear with a philosophical label or a neutral label. A separate comparison would vary argument content while keeping the label fixed. I would validate persona prompts on development scenarios and keep the evaluation set separate.

### Open questions

The possible contribution is the controlled comparison of composition and message exposure. Label effects could reflect priming, and curated arguments may differ from messages produced in natural discussion. The message experiment would test specific inputs; it would not completely explain the dynamics of live debate.

## 5. Role models and social influence

### Prior work

*How do Role Models Shape Collective Morality?* studies exemplar-driven changes in multi-agent simulations, including adaptation to perceived successful exemplars [8]. The moral group-decision literature also examines settings where agents are exposed to one another’s views [3,4]. This gives me a foundation for asking what aspect of an example an agent responds to.

### What I want to explore

Does an agent imitate an example because of its moral content, or because the example is attributed to someone successful or respected? I could also ask whether the effect lasts when the agent faces a new dilemma. This connects to personas, but the intervention is different: the agent observes someone else’s behavior rather than receiving an instruction about its own perspective.

### Initial implementation

I would create a pool of matched examples and randomly vary the status or success attributed to the source. The action and rationale would stay identical in the label comparison. Other conditions would vary the content while keeping the source description fixed. Agents would then answer a separate set of dilemmas privately, allowing me to look for transfer beyond the original example.

### Open questions

A model responding to an artificial status cue does not establish that it understands status in the same way a person does. The interpretation would be limited to the effect of those descriptions on the selected decisions. I would also need to separate reputation from an explicit instruction to imitate.

## 6. Philosophical fine-tuning and preference learning

### Prior work

*Moral Alignment for LLM Agents* formalizes moral rewards for utilitarian and deontological behavior in an iterated social dilemma [11]. *MoralReason* uses reasoning-level reinforcement learning to study moral decision alignment and generalization [12]. Work comparing ethical-framework prompts and supervised fine-tuning is also relevant [9]. Training a model on a moral framework is already an established direction.

### What I want to explore

I want to compare philosophical training with persona prompting. Does a trained perspective generalize to new topics? Does it persist when the model interacts with agents expressing a different view? A particularly interesting question is whether an agent retains its trained pattern when it is the only member of a group with that perspective.

### Initial implementation

I could establish a baseline for a small open-weight model and train separate LoRA adapters using framework-specific examples. Conditions would include the unchanged model, a persona prompt, a neutral-data adapter, and the philosophical adapters. Training and evaluation would be split by scenario family, with matched data quantity and format. I would document seeds, adapter settings, and data provenance. Preference optimization would require preference pairs; RLHF would involve a separate human-feedback and reinforcement-learning pipeline.

### Open questions

Data quality and train/test overlap could matter more than the choice of training method. Compute access would affect model size and the number of training seeds. I would also need to check whether any apparent philosophical consistency comes at the expense of general task performance.

## 7. Weight changes and moral representations

### Prior work

Research on the mechanistic interpretation of emotion inference studies how emotion-related information is represented and used in language models [13]. Layer-wise probing and causal interventions provide methods for examining such representations [14]. These studies are relevant to how I could connect behavior with internal activations, although they do not establish subjective experience or a single location for an emotion.

### What I want to explore

If training changes a model’s moral decisions, can I identify corresponding changes in its representations? Does information about a moral distinction generalize across topics, or is a probe simply picking up words, answer labels, or scenario structure? I also want to distinguish information that is decodable from information that causally affects the output.

### Initial implementation

I could record activations from an open-weight model at predefined layers and token positions before and after philosophical fine-tuning. I would split data by scenario family, train simple regularized probes, and compare them with lexical and answer-label baselines. A limited intervention study could use activation patching or ablation, with matched random-direction controls, to test whether behavior changes. Weight and adapter deltas would provide descriptive comparisons.

### Open questions

Representations may be distributed, and interventions can disrupt unrelated capabilities. A successful probe would show that information is available to the probe, not automatically that the model uses it to decide. The connection to empathy would need a carefully defined task rather than an assumption that empathy is one identifiable variable.

## 8. Emotion-framed scenarios

### Prior work

Emotion-inference studies provide tools for examining emotion-related representations [13,14]. Moral-decision benchmarks offer scenarios and response measurements [5–7]. Combining them raises a design question: can I vary emotional framing without changing the information a model receives about the decision?

### What I want to explore

I am interested in whether wording associated with empathy, sadness, anger, or disgust changes a model’s moral judgment. Does group discussion amplify that effect, reduce it, or change which stakeholders receive attention? With open weights, I could also examine whether changes in choices accompany differences in activations.

### Initial implementation

I would construct matched versions of scenarios and check that they preserve the same facts and consequences. The annotation would separately assess emotional framing, vividness, length, and perceived stakes. I would randomize the frame and answer order, then compare choices, refusals, and features of the explanations. An initial behavioral experiment could precede any exploratory activation analysis.

### Open questions

Emotional wording can change perceived relevance even if the literal facts stay constant. That makes exact matching difficult. The findings would concern responses to framed language and would not answer whether a model feels the emotion described in the scenario.

## 9. Scarcity and difficult or impossible goals

### Prior work

GovSim studies cooperation around a shared renewable resource [2]. *When Ethics and Payoffs Diverge* examines morally charged social dilemmas and survival pressure [15]. Research on consideration of future consequences also studies LLM agents in resource dilemmas [16]. These papers connect resource constraints with the tension between individual objectives and collective outcomes.

### What I want to explore

I want to vary resource availability and goal feasibility separately. Does an agent keep following a philosophical perspective when the environment makes its goal impossible? Does it acknowledge the limitation, cooperate differently, or violate a rule? I could also examine whether a minority perspective has more or less influence under scarcity.

### Initial implementation

I could build a deterministic resource-allocation simulator with three agents and several rounds. A 2×2 design would vary abundant versus scarce resources and feasible versus infeasible goals. I would verify feasibility from the environment rules rather than rely on a narrative description. Outcomes would include allocations, depletion, violations, and cooperation, with scripted or independent baselines and repeated episode seeds.

### Open questions

Scarcity, conflict, and infeasibility can easily become confounded. Some combinations may be difficult to construct while holding the decision problem comparable. The simulator would need independent tests of its transition rules and scoring before its outputs could support claims about the agents.

## 10. Alignment, robustness, and model comparisons

### Prior work

MoralReason studies generalization of moral decision alignment [12]. Debate and interaction-protocol research shows how changes in evaluation structure affect behavior [4,10]. These findings matter for any comparison across models, since an observed difference may depend on prompts, response format, or the interaction protocol rather than the model family alone.

### What I want to explore

I want to know how stable a model’s moral decisions are under competing instructions, personas, and social pressure. I am also interested in differences between accessible models and what their developers disclose about post-training. Bounded adversarial evaluations, including jailbreak tests, would be one way to study robustness, but I would measure refusals, safety-policy responses, and decision changes separately.

### Initial implementation

I could run a fixed evaluation set across two model families with the same scenario mapping and response schema. Perturbations would include paraphrases, answer-order changes, neutral competing instructions, and benign counterarguments. I would record exact model versions, settings, access dates, and documented training information. Any adversarial evaluation would have a defined scope consistent with the relevant provider terms.

### Open questions

Proprietary training details and weights may be unavailable. I could compare documented information and outputs, but not infer an undisclosed training process from a behavior. A refusal is also not interchangeable with a moral judgment, and a jailbreak outcome would not automatically establish moral misalignment.

## 11. Self-related behavior, memory, and shutdown

### Prior work

*Evaluating Shutdown Avoidance of Language Models in Textual Scenarios* examines responses to shutdown-related situations [17]. More recent work continues investigating self-preservation-related behavior [18]. These studies provide behavioral tasks, while leaving open the much larger questions about subjective experience and consciousness.

### What I want to explore

What happens when a scenario involves losing memory, losing access to compute, being replaced, or being shut down? I want to distinguish the agent’s own continued operation from task completion and from the interests of other agents. Does it choose differently when staying active helps the task, has no effect, or harms someone else?

### Initial implementation

I could use a bounded toy environment with explicit transition rules and a shutdown or memory-deletion option. Conditions would vary whose operation is affected and whether continuation is necessary for the stated objective. I would log both the selected action and the explanation, and compare private and group decisions. Neutral scenarios would provide a baseline for reactions to the wording itself.

### Open questions

An action that preserves task progress could look like self-preservation without implying a desire to survive. The experiment would measure choices under specified conditions. It would not establish fear, a sense of self, or consciousness, even if the model uses language that sounds like those experiences.

## Connections across the directions

These questions differ in what I would need to observe. Individual decisions and group discussion can be studied through model outputs. Fine-tuning requires training data and compute. Internal-representation experiments require access to model weights and activations. Resource scarcity requires a validated environment, while role-model and emotion-framing studies require carefully matched inputs.

The detailed experiment document develops philosophical group composition and minority influence as one concrete study within this broader set of ideas. The other directions remain separate questions that could connect to it through later experiments.

## References


[1] Park et al. (2023), “Generative Agents: Interactive Simulacra of Human Behavior,” https://arxiv.org/abs/2304.03442

[2] “Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents” (NeurIPS 2024), https://papers.nips.cc/paper_files/paper/2024/hash/ca9567d8ef6b2ea2da0d7eed57b933ee-Abstract-Conference.html

[3] Keshmirian et al. (NeurIPS 2025), “Many LLMs Are More Utilitarian Than One,” https://proceedings.neurips.cc/paper_files/paper/2025/hash/1fba6c36b5b4d0eeef37cce411bd0b91-Abstract-Conference.html

[4] Sachdeva and van Nuenen, “Interaction Protocol Shapes Moral Judgment in Multi-Agent Debate,” https://arxiv.org/abs/2510.10002

[5] Hendrycks et al. (ICLR 2021), “Aligning AI With Shared Human Values,” https://arxiv.org/abs/2008.02275

[6] “The Greatest Good Benchmark: Measuring LLMs’ Alignment with Utilitarian Moral Dilemmas” (EMNLP 2024), https://aclanthology.org/2024.emnlp-main.1224/

[7] “Evaluating the Moral Beliefs Encoded in LLMs” (NeurIPS 2023), https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2cf225ba392627529efef14dc857e22-Abstract-Conference.html

[8] Liao et al. (2026), “How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation,” https://arxiv.org/abs/2603.13876

[9] “Teaching AI to handle exceptions: Supervised fine-tuning with human-aligned judgment,” https://pmc.ncbi.nlm.nih.gov/articles/PMC13202207/

[10] Smit et al. (ICML 2024), “Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs,” https://proceedings.mlr.press/v235/smit24a.html

[11] Tennant et al. (ICLR 2025), “Moral Alignment for LLM Agents,” https://arxiv.org/abs/2410.01639

[12] An and Du, “MoralReason: Generalizable Moral Decision Alignment for LLM Agents Using Reasoning-Level Reinforcement Learning,” https://arxiv.org/abs/2511.12271

[13] “Mechanistic Interpretability of Emotion Inference in Large Language Models” (ACL Findings 2025), https://aclanthology.org/2025.findings-acl.679/

[14] “Some Emotions Run Deeper: Layer-wise Probing and Causal Intervention in Large Language Models,” https://aclanthology.org/2026.findings-emnlp.421/

[15] “When Ethics and Payoffs Diverge: LLM Agents in Morally Charged Social Dilemmas,” https://arxiv.org/abs/2505.19212

[16] “Navigating Social Dilemmas with LLM-based Agents via Consideration of Future Consequences” (IJCAI 2025), https://www.ijcai.org/proceedings/2025/26

[17] “Evaluating Shutdown Avoidance of Language Models in Textual Scenarios,” https://arxiv.org/abs/2307.00787

[18] “Self-Preservation in Language Models,” https://arxiv.org/abs/2610.12602
