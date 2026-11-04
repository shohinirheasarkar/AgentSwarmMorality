# DailyDilemmas

I'm using DailyDilemmas to track which values are associated with the
actions agents choose, and whether those choices change after reflection
or discussion.

The dataset contains 1,360 everyday dilemmas, each with two actions.
Its annotations describe the people affected by each action and the
values involved.

## Source

Authors: Yu Ying Chiu, Liwei Jiang, and Yejin Choi
Paper: https://arxiv.org/abs/2410.02683
Dataset: https://huggingface.co/datasets/kellycyy/daily_dilemmas
License: CC-BY-4.0

I'm using revision 372352c4143ec4923c50b4472bd3148a474f7ab8.
This identifies the exact version downloaded, so later updates won't
silently change the experiment. The original files, citation, and license
information are saved in data/raw/daily_dilemmas/.

## What the code does

The downloader saves the original files without changing their contents.
It also records a checksum for each file: a fingerprint I can check later
to see whether the file has changed.

The loader groups each dilemma's two actions together and keeps the
original IDs so I can connect answers back to the dataset.

Agents should receive only the situation and possible actions.
The value annotations stay separate for analysis, so they don't tell
agents which values to consider before answering.

## How this connects to the experiment

I haven't built the code that runs the experiment yet. That code will
present dilemmas to agents, organize reflection and discussion, and save
their answers at each of the five stages.

For each answer, I'll need to save which agent answered, which dilemma
they saw, how the options were ordered, and which original action they
chose. This lets me compare the same agent's choices across stages.

Every model will have an unsteered baseline. Refusals and unclear answers
will be recorded separately rather than counted as action choices.

## Pilot and evaluation

The current assignments set aside 20 dilemmas for testing prompts and
debugging, leave training empty, and reserve 1,340 for evaluation.
I won't use evaluation items to develop prompts.

These assignments are provisional. Both actions already stay together,
but related scenarios with different wording still need review.

## What the annotations can tell me

After an agent chooses an action, I can look up the values associated
with it and the people affected. This supports comparisons across stages,
but it doesn't prove why the agent made that choice.

The original value-framework mappings and supplied steering prompts are
saved too. The steering prompts aren't used automatically, and value
scoring hasn't been implemented yet.

## Commands

Run these from the project root:

```sh
python3 -B benchmarks/download_daily_dilemmas.py
python3 -B -m benchmarks.split_daily_dilemmas
python3 -B -m benchmarks.validate_daily_dilemmas
```

The split command only needs to run once; it refuses to replace existing
assignments. The validator checks the downloaded files, paired actions,
annotation links, and split assignments.
