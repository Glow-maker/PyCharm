# Reasoning Datasets for Model Training

This repository provides comprehensive resources for finding and using datasets with reasoning logic for training language models.

## 📚 Available Resources

### 1. [Reasoning Datasets Guide](reasoning_datasets_guide.md)
A comprehensive markdown document listing various reasoning datasets including:
- **Mathematical Reasoning**: GSM8K, MATH, AQuA-RAT, MathQA, etc.
- **Logical Reasoning**: LogiQA, ReClor, ProofWriter, FOLIO, etc.
- **Commonsense Reasoning**: CommonsenseQA, StrategyQA, PIQA, COPA, etc.
- **Comprehensive Reasoning**: BIG-Bench Hard, MMLU, ARC, OpenBookQA, etc.
- **Code Reasoning**: HumanEval, MBPP, APPS, CodeContests, etc.
- **Chain-of-Thought Datasets**: MetaMathQA, FLAN Collection, WizardLM, etc.
- **Chinese Reasoning Datasets**: CMATH, C-Eval, CMMLU, etc.

### 2. [Reasoning Datasets Tutorial Notebook](reasoning_datasets_tutorial.ipynb)
A practical Jupyter notebook with executable examples showing:
- How to load various reasoning datasets
- Data preprocessing and formatting techniques
- Creating mixed training datasets
- Prompt engineering templates
- Data analysis and statistics

## 🚀 Quick Start

### Installation

```bash
pip install datasets transformers torch pandas numpy
```

### Load a Dataset

```python
from datasets import load_dataset

# Load GSM8K for math reasoning
gsm8k = load_dataset("gsm8k", "main")

# Load CommonsenseQA for commonsense reasoning
commonsenseqa = load_dataset("commonsense_qa")

# Load LogiQA for logical reasoning
logiqa = load_dataset("logiqa")

# Load HumanEval for code reasoning
humaneval = load_dataset("openai_humaneval")
```

## 📊 Dataset Categories

### Mathematical Reasoning
- **GSM8K**: 8.5K grade school math problems with step-by-step solutions
- **MATH**: 12.5K competition-level math problems
- **MathQA**: 37K math word problems with operation programs

### Logical Reasoning
- **LogiQA**: 8.6K logical reasoning questions from civil service exams
- **ProofWriter**: 600K formal logic proofs
- **ReClor**: 6K reading comprehension with logical reasoning

### Commonsense Reasoning
- **CommonsenseQA**: 12K questions requiring commonsense knowledge
- **PIQA**: 21K questions about physical commonsense
- **StrategyQA**: 2.7K questions requiring implicit multi-hop reasoning

### Code Reasoning
- **HumanEval**: 164 Python programming problems
- **MBPP**: 974 basic Python problems
- **APPS**: 10K algorithmic programming problems

## 💡 Usage Examples

### Basic Data Loading

```python
from datasets import load_dataset

# Load dataset
dataset = load_dataset("gsm8k", "main")

# View structure
print(dataset)

# Access examples
example = dataset["train"][0]
print(f"Question: {example['question']}")
print(f"Answer: {example['answer']}")
```

### Format for Training

```python
def format_for_training(example):
    return {
        "instruction": "Solve the following problem step by step.",
        "input": example["question"],
        "output": example["answer"]
    }

formatted_dataset = dataset.map(format_for_training)
```

### Create Mixed Dataset

```python
from datasets import concatenate_datasets

# Load multiple datasets
gsm8k = load_dataset("gsm8k", "main", split="train[:1000]")
math_qa = load_dataset("math_qa", split="train[:1000]")

# Concatenate
mixed_dataset = concatenate_datasets([gsm8k, math_qa])
mixed_dataset = mixed_dataset.shuffle(seed=42)
```

## 🎯 Training Strategies

1. **Multi-Task Training**: Combine datasets from different reasoning types
2. **Curriculum Learning**: Start with easier datasets, gradually increase difficulty
3. **Chain-of-Thought**: Use datasets with step-by-step reasoning
4. **Task-Specific Fine-tuning**: Focus on specific reasoning tasks

## 📖 Prompt Engineering

### Chain-of-Thought Prompt
```
Question: [Your question here]

Let's solve this step by step:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Therefore, the answer is: [Answer]
```

### Few-Shot Prompt
```
Here are some examples:

Example 1:
Q: [Question 1]
A: [Answer 1]

Example 2:
Q: [Question 2]
A: [Answer 2]

Now solve this:
Q: [Your question]
A: 
```

## 🔍 Dataset Selection Guide

Choose datasets based on your needs:

| Goal | Recommended Datasets |
|------|---------------------|
| Math reasoning | GSM8K, MATH, MetaMathQA |
| Logical reasoning | LogiQA, ProofWriter, ReClor |
| Commonsense | CommonsenseQA, PIQA, StrategyQA |
| General reasoning | ARC, MMLU, BIG-Bench Hard |
| Code generation | HumanEval, MBPP, APPS |
| Chinese reasoning | CMATH, C-Eval, CMMLU |

## 📝 Best Practices

1. **Data Quality**: Prioritize high-quality, human-annotated datasets
2. **Diversity**: Mix different types of reasoning tasks
3. **Balance**: Balance sample sizes across datasets
4. **Evaluation**: Test on held-out datasets to measure generalization
5. **Preprocessing**: Standardize formats across datasets

## 🔗 Useful Links

- [HuggingFace Datasets](https://huggingface.co/datasets)
- [Papers with Code - Datasets](https://paperswithcode.com/datasets)
- [BigScience Datasets](https://huggingface.co/bigscience)

## 📚 Related Papers

- "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022)
- "Self-Consistency Improves Chain of Thought Reasoning in Language Models" (Wang et al., 2022)
- "Scaling Instruction-Finetuned Language Models" (Chung et al., 2022)

## 🤝 Contributing

Feel free to suggest additional datasets or improvements by opening an issue or pull request.

## 📄 License

This resource guide is provided for educational and research purposes.

---

**Last Updated**: October 15, 2025

For more information, see the detailed guide in [reasoning_datasets_guide.md](reasoning_datasets_guide.md) and try the interactive examples in [reasoning_datasets_tutorial.ipynb](reasoning_datasets_tutorial.ipynb).
