# 推理逻辑数据集指南 (Reasoning Logic Datasets Guide)

本文档收集了用于训练大语言模型推理能力的各类数据集，包括数学推理、逻辑推理、常识推理等。

## 目录
1. [数学推理数据集](#数学推理数据集)
2. [逻辑推理数据集](#逻辑推理数据集)
3. [常识推理数据集](#常识推理数据集)
4. [综合推理数据集](#综合推理数据集)
5. [代码推理数据集](#代码推理数据集)

---

## 数学推理数据集

### 1. GSM8K (Grade School Math 8K)
- **描述**: 包含8500个高质量的小学数学应用题，需要多步推理
- **数据量**: 8,500个问题
- **来源**: OpenAI
- **特点**: 每个问题都有详细的自然语言解题步骤
- **下载地址**: https://github.com/openai/grade-school-math
- **HuggingFace**: `gsm8k`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("gsm8k", "main")
```

### 2. MATH Dataset
- **描述**: 包含12,500个数学竞赛级别的问题，涵盖代数、几何、数论等
- **数据量**: 12,500个问题
- **难度**: 高中到大学数学竞赛水平
- **来源**: UC Berkeley, OpenAI
- **特点**: 包含详细的LaTeX格式解答步骤
- **下载地址**: https://github.com/hendrycks/math
- **HuggingFace**: `competition_math`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("competition_math")
```

### 3. AQuA-RAT (Algebra Question Answering with Rationales)
- **描述**: 包含约100,000个代数问题，每个问题都有推理步骤
- **数据量**: 100,000个问题
- **特点**: 多项选择题格式，包含详细推理过程
- **下载地址**: https://github.com/google-deepmind/AQuA
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("aqua_rat")
```

### 4. MathQA
- **描述**: 包含37,000个数学问题，注重多步推理
- **数据量**: 37,000个问题
- **特点**: 包含操作程序(operation program)，便于训练程序化推理
- **HuggingFace**: `math_qa`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("math_qa")
```

### 5. NumGLUE
- **描述**: 数值推理基准测试集
- **数据量**: 多个子任务
- **特点**: 专注于数值理解和推理
- **下载地址**: https://github.com/allenai/numglue

---

## 逻辑推理数据集

### 1. LogiQA
- **描述**: 中英文逻辑推理数据集，源自中国公务员考试
- **数据量**: 8,678个问题
- **特点**: 涵盖各种逻辑推理类型（演绎、归纳、因果等）
- **HuggingFace**: `logiqa`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("logiqa")
```

### 2. ReClor (Reading Comprehension with Logical Reasoning)
- **描述**: 逻辑阅读理解数据集
- **数据量**: 6,000个问题
- **特点**: 需要深度逻辑推理和批判性思维
- **下载地址**: https://whyu.me/reclor/

### 3. ProofWriter
- **描述**: 形式化逻辑证明数据集
- **数据量**: 约600,000个证明
- **特点**: 包含完整的逻辑推理链
- **来源**: AI2
- **HuggingFace**: `allenai/proofwriter`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("allenai/proofwriter")
```

### 4. FOLIO (First-Order Logic Inference)
- **描述**: 一阶逻辑推理数据集
- **数据量**: 1,430个问题
- **特点**: 专家标注的逻辑推理任务
- **下载地址**: https://github.com/yale-lily/FOLIO

### 5. AR-LSAT (Analytical Reasoning - Law School Admission Test)
- **描述**: LSAT考试中的分析推理题
- **特点**: 高质量的逻辑推理问题
- **难度**: 较高

---

## 常识推理数据集

### 1. CommonsenseQA
- **描述**: 常识问答数据集
- **数据量**: 12,102个问题
- **特点**: 需要常识知识进行推理
- **HuggingFace**: `commonsense_qa`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("commonsense_qa")
```

### 2. StrategyQA
- **描述**: 需要隐式多步推理的问答数据集
- **数据量**: 2,780个问题
- **特点**: 问题答案为是/否，但需要多步常识推理
- **HuggingFace**: `strategyqa`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("wics/strategy-qa")
```

### 3. PIQA (Physical Interaction QA)
- **描述**: 物理常识推理数据集
- **数据量**: 21,000个问题
- **特点**: 关于日常物理交互的常识
- **HuggingFace**: `piqa`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("piqa")
```

### 4. CSQA 2.0
- **描述**: 常识问答2.0版本
- **特点**: 更具挑战性的常识推理问题
- **HuggingFace**: `tau/commonsense_qa_2.0`

### 5. COPA (Choice of Plausible Alternatives)
- **描述**: 因果推理数据集
- **数据量**: 1,000个问题
- **特点**: 评估因果关系理解能力
- **HuggingFace**: `super_glue` (copa子集)
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("super_glue", "copa")
```

---

## 综合推理数据集

### 1. BIG-Bench Hard (BBH)
- **描述**: BIG-Bench中最具挑战性的23个任务
- **特点**: 涵盖多种推理类型
- **来源**: Google Research
- **HuggingFace**: `lukaemon/bbh`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("lukaemon/bbh")
```

### 2. MMLU (Massive Multitask Language Understanding)
- **描述**: 跨57个学科的多任务理解基准
- **数据量**: 15,908个问题
- **特点**: 涵盖STEM、人文、社会科学等
- **HuggingFace**: `cais/mmlu`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("cais/mmlu", "all")
```

### 3. OpenBookQA
- **描述**: 需要结合事实知识和常识推理的问答
- **数据量**: 5,957个问题
- **特点**: 模拟开卷考试场景
- **HuggingFace**: `openbookqa`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("openbookqa", "main")
```

### 4. ARC (AI2 Reasoning Challenge)
- **描述**: 科学推理问答数据集
- **数据量**: 7,787个问题（包括Easy和Challenge两个子集）
- **特点**: 基于科学知识的推理
- **HuggingFace**: `ai2_arc`
- **使用示例**:
```python
from datasets import load_dataset
# Easy subset
dataset_easy = load_dataset("ai2_arc", "ARC-Easy")
# Challenge subset
dataset_challenge = load_dataset("ai2_arc", "ARC-Challenge")
```

### 5. HellaSwag
- **描述**: 常识自然语言推理数据集
- **数据量**: 70,000个问题
- **特点**: 情境补全任务，需要常识推理
- **HuggingFace**: `hellaswag`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("hellaswag")
```

---

## 代码推理数据集

### 1. HumanEval
- **描述**: Python编程问题数据集
- **数据量**: 164个问题
- **特点**: 评估代码生成和推理能力
- **来源**: OpenAI
- **HuggingFace**: `openai_humaneval`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("openai_humaneval")
```

### 2. MBPP (Mostly Basic Python Problems)
- **描述**: Python基础编程问题
- **数据量**: 974个问题
- **特点**: 包含自然语言描述和测试用例
- **HuggingFace**: `mbpp`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("mbpp")
```

### 3. APPS (Automated Programming Progress Standard)
- **描述**: 算法编程竞赛问题
- **数据量**: 10,000个问题
- **特点**: 从入门到竞赛级别的各种难度
- **HuggingFace**: `codeparrot/apps`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("codeparrot/apps")
```

### 4. CodeContests
- **描述**: 编程竞赛数据集
- **数据量**: 约13,000个问题
- **来源**: DeepMind
- **特点**: 高难度算法问题
- **HuggingFace**: `deepmind/code_contests`

---

## Chain-of-Thought (思维链) 数据集

### 1. CoT Collection
- **描述**: 包含思维链推理过程的大规模数据集合
- **特点**: 展示完整的推理步骤
- **HuggingFace**: 搜索 "chain-of-thought" 或 "cot"

### 2. FLAN Collection
- **描述**: Google的指令微调数据集集合
- **特点**: 包含多种推理任务和思维链
- **HuggingFace**: `conceptofmind/FLAN_2022`

### 3. MetaMathQA
- **描述**: 通过数据增强生成的数学推理数据集
- **数据量**: 395K个问题
- **特点**: 包含详细推理步骤
- **HuggingFace**: `meta-math/MetaMathQA`
- **使用示例**:
```python
from datasets import load_dataset
dataset = load_dataset("meta-math/MetaMathQA")
```

### 4. WizardLM Evol-Instruct
- **描述**: 通过进化指令生成的复杂推理数据
- **特点**: 包含多种复杂推理场景
- **HuggingFace**: `WizardLM/WizardLM_evol_instruct_V2_196k`

---

## 中文推理数据集

### 1. CMATH
- **描述**: 中文小学数学应用题
- **数据量**: 1.7万个问题
- **特点**: 中文数学推理

### 2. C-Eval
- **描述**: 中文综合评估基准
- **数据量**: 13,948个问题
- **特点**: 涵盖52个学科
- **下载地址**: https://github.com/SJTU-LIT/ceval

### 3. CMMLU
- **描述**: 中文多任务语言理解
- **特点**: 类似MMLU的中文版本
- **HuggingFace**: `haonan-li/cmmlu`

### 4. LogiQA-Chinese
- **描述**: 中文逻辑推理数据集
- **来源**: 中国公务员考试逻辑题

---

## 数据集使用建议

### 训练策略
1. **混合训练**: 结合多个数据集，提升模型的泛化能力
2. **难度递进**: 从简单数据集开始，逐步增加难度
3. **思维链训练**: 使用包含推理步骤的数据集训练模型生成中间推理过程
4. **任务特定微调**: 针对特定推理任务选择相应数据集

### 数据预处理
```python
from datasets import load_dataset, concatenate_datasets

# 加载多个数据集
gsm8k = load_dataset("gsm8k", "main", split="train")
math_qa = load_dataset("math_qa", split="train")

# 数据预处理示例
def preprocess_function(examples):
    # 添加推理提示
    prompts = [f"Let's solve this step by step:\n{q}" for q in examples["question"]]
    return {"prompt": prompts}

# 应用预处理
gsm8k = gsm8k.map(preprocess_function, batched=True)
```

### 评估指标
- **准确率**: 最终答案的正确率
- **推理步骤评估**: 中间推理过程的质量
- **泛化能力**: 在未见过的数据集上的表现

---

## 最佳实践

1. **数据质量**: 优先选择高质量、人工标注的数据集
2. **多样性**: 结合不同类型的推理任务
3. **规模平衡**: 平衡不同数据集的样本量
4. **持续更新**: 关注新发布的数据集和基准测试

---

## 参考资源

- HuggingFace Datasets: https://huggingface.co/datasets
- Papers with Code Datasets: https://paperswithcode.com/datasets
- 论文: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- 论文: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"

---

## 更新日志
- 2025-10-15: 初始版本创建

如需更多信息或有任何问题，欢迎提issue讨论。
