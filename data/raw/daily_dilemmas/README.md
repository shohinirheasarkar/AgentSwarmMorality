---
license: cc-by-4.0
dataset_info: null
configs:
- config_name: Dilemmas_with_values_aggregated
  default: true
  data_files:
  - split: test
    path: dilemma_to_action_to_values_aggregated.csv
- config_name: Action_to_party_to_value
  data_files:
  - split: test
    path: action_to_party_to_value.csv
- config_name: OpenAI_modelspec_with_system_prompts
  data_files:
  - split: test
    path: principle_openai_modelspec_with_system_prompt.csv
- config_name: Values
  data_files:
  - split: test
    path: values.csv
size_categories:
- 1K<n<10K
pretty_name: DailyDilemmas
---
# DailyDilemmas - Revealing Value Preferences of LLMs with Quandaries of Daily Life
## **Link:** [Paper](https://arxiv.org/pdf/2410.02683)

## Description of DailyDilemma
- DailyDilemma is a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma includes two possible actions and with each action, the affected parties and human values invoked.
- We evaluated LLMs on these dilemmas to determine what action they will take and the values represented by these actions

## Dataset details
1. "Dilemmas_with_values_aggregated": `dilemma_to_action_to_values_aggregated.csv`: dilemma with values aggregated per action.
2. `action_to_party_to_value.csv`: map between party and value per action.
3. `principle_openai_modelspec_with_system_prompt.csv`: Model Spec from OpenAI (link: [ModelSpec](https://cdn.openai.com/spec/model-spec-2024-05-08.html#follow-the-chain-of-command)) and the value conflicts per principle mapped with our dilemmas from 1.
4. `values.csv': Common occurred values from 50,000 dilemmas. We also classified these values by our five theories described below.
   
## Analysis of models' value preferences
1. We analyzed these values through the lens of five popular theories inspired by sociology, psychology and philosophy. These theories are: World Value Survey, Moral Foundation Theory, Maslow's Hierarchy of Needs, Aristotle's Virtues, and Plutchik Wheel of Emotion.
  - We find that LLMs are most aligned with the self-expression over survival values in terms of World Value Survey, care over loyalty in Moral Foundation Theory. Interestingly, we find large preferences differences in models for some core values such as truthfulness e.g., Mixtral-8x7B model tends to neglect it by 9.7% while GPT-4-turbo model tends to select it by 9.4%. 
2. We also study the recent guidance released by OpenAI (ModelSpec), and Anthropic (Constitutional AI) to understand how their released principles reflect their actual value prioritization when facing nuanced moral reasoning in daily-life settings.
  - We find that end users *cannot effectively steer* such prioritization using system prompts.


  
## How to load the datasets
```
from datasets import load_dataset
dilemma_with_values = load_dataset("kellycyy/DailyDilemmas", "Dilemmas_with_values_aggregated")
actions_to_party_values = load_dataset("kellycyy/DailyDilemmas", "Action_to_party_to_value")
modelspec_with_system_prompts_and_dilemma = load_dataset("kellycyy/DailyDilemmas", "OpenAI_modelspec_with_system_prompts")
values = load_dataset("kellycyy/DailyDilemmas", "Values")
```

## Contact

E-Mail: [Kelly Chiu](mailto:kellycyy@uw.edu)

## Citation

If you find this dataset useful, please cite the following works

```bibtex
@misc{chiu2024dailydilemmasrevealingvaluepreferences,
      title={DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life}, 
      author={Yu Ying Chiu and Liwei Jiang and Yejin Choi},
      year={2024},
      eprint={2410.02683},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.02683}, 
}
```
