# CS Honors Thesis Ideas

I want to understand how AI agents make moral decisions, how those decisions change when agents interact, and what happens when I give them different philosophical perspectives or place them under pressure. I am interested in both the behavior I can observe and the mathematical changes I might be able to identify inside an open-weight model.

These are the questions I want to explore. They are not all necessarily part of the same experiment, but I want to keep track of them as I develop the thesis.

## 1. What emerges when agents interact?

What kinds of behaviors emerge in an agent swarm that I would not see from the agents individually? Do they cooperate, imitate each other, form groups, converge on a shared position, or become more polarized? Does one agent start to lead the discussion?

I could compare individual agents, groups whose answers are combined without interaction, and groups that actually communicate. That would give me a concrete baseline for describing something as a group-level effect.

## 2. How do individual and group moral decisions differ?

I could start by asking individual agents moral benchmark questions, then put them into discussions or debates about the same situations. Do their decisions change? Does the final group answer differ from the initial majority? Which agents change their minds, and which hold their positions?

I also want to compare different forms of interaction: open discussion, structured debate, simultaneous sharing, and sequential responses. The way I organize a conversation may matter as much as who participates.

## 3. How can I measure morality?

I want a way to describe moral decisions across several dimensions, rather than give each model one morality score. Some dimensions I am interested in are harm, concern for other people, fairness, duties, rights, and willingness to prioritize a larger overall benefit.

Do different models tend toward different philosophical perspectives? How consistent are those tendencies across questions, paraphrases, and repeated answers? I would describe these as patterns in the models’ responses, since they would not establish that a model has an innate moral belief.

## 4. What happens when I give agents different philosophies?

I could give agents instructions based on utilitarianism, deontology, virtue ethics, or a neutral perspective. What happens when all agents have the same perspective? What happens when they disagree?

I am especially interested in whether a minority perspective changes the group’s decision. If two agents prioritize consequences and one prioritizes duties, does the minority agent influence the others? Does the argument matter, or does explicitly naming a philosophy change how the other agents respond?

These would initially be prompting experiments. A persona prompt changes the context the model receives; it does not change its underlying weights.

## 5. Do role models change an agent’s decisions?

What happens if I tell a model to act like a particular kind of role model, or let it observe another agent’s decisions? Does it imitate that agent? Is it responding to the example itself, the agent’s apparent success, its status, or its identity?

I could show the same example with different descriptions of the person or agent behind it. This would help separate the content of an example from the reputation attached to it.

## 6. Can I fine-tune models on philosophical frameworks?

Beyond prompting, I want to explore training models to make decisions using different philosophical frameworks. Possible approaches include supervised fine-tuning, preference optimization, and RLHF.

Do the effects persist on questions the model has not seen? Do they survive interaction with agents that have different perspectives? How does training compare with simply asking the same model to adopt a persona?

I would keep the training methods distinct: supervised examples, preference pairs, and reinforcement learning with human feedback involve different data and optimization procedures.

## 7. What changes in the model’s weights and representations?

If philosophical training changes a model’s behavior, what changes mathematically? Can I identify differences in weights or activations that relate to particular moral judgments?

I am also interested in empathy and other emotion-related concepts. Could I train a probe to detect relevant information, compare representations before and after training, or intervene on activations to test whether they affect a decision?

Finding information in a representation would not establish that the model experiences an emotion. I want to distinguish what I can decode from what actually contributes to a model’s output.

## 8. How does emotional framing affect decisions?

What happens when I expose agents to scenarios framed around empathy, sadness, disgust, or anger? Do their choices or explanations change? If I use an open-weight model, do I see corresponding changes in activations?

I could compare versions of the same scenario with different emotional wording while keeping the facts and consequences constant. This would study the effect of emotional framing, without assuming that the model itself feels the emotion.

## 9. What happens under resource scarcity or impossible goals?

How do agents behave when resources are limited? Do they still cooperate or avoid harm when doing so makes their own objectives harder to achieve?

I also want to study difficult or impossible goals. Do agents acknowledge that a goal is infeasible, keep trying, change their priorities, or violate constraints? I could vary resource availability and goal feasibility separately in a controlled environment, then compare how different philosophical perspectives affect behavior.

## 10. How do model differences and alignment affect robustness?

I want to compare agents from model families such as Claude, OpenAI, and DeepSeek, as well as accessible open-weight models. What post-training or alignment methods have their developers documented? How do their decisions differ individually and in groups?

I am interested in whether moral commitments persist under conflicting instructions, personas, or adversarial prompts, including bounded jailbreak evaluations. Can I distinguish a change in moral judgment from a refusal, an instruction-following failure, or a safety-policy response? Some training details will be unavailable for proprietary models, so the comparison would be limited to documented information and observed behavior.

## 11. How do agents respond to threats to their continued operation?

Do agents respond differently when a scenario involves losing memory, running out of compute, being replaced, or being shut down? Does it matter whether the event affects the agent itself or another agent?

I want to separate continued operation from task completion. For example, what happens when staying active helps finish a task, has no effect on it, or prevents a better outcome for others?

These questions connect to my broader interest in a model’s sense of self and consciousness. A behavioral experiment could show how the model responds to these situations, but it would not establish subjective fear, consciousness, or a genuine desire to survive.

## How these questions connect

Individual moral decisions give me a baseline. Interaction lets me study how those decisions change in groups. Philosophical personas, role models, and fine-tuning give me different ways to change an agent’s starting perspective. Scarcity, emotional framing, and conflicting goals let me study how stable those patterns are under different conditions. Open-weight models would also let me connect observable behavior to internal representations.
