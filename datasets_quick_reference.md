# Quick Reference: Reasoning Datasets

快速参考表格 - 所有推理数据集一览

## 数学推理数据集 (Mathematical Reasoning)

| 数据集名称 | 数据量 | 难度 | HuggingFace ID | 语言 | 特点 |
|-----------|--------|------|----------------|------|------|
| GSM8K | 8.5K | 小学 | `gsm8k` | EN | 详细解题步骤 |
| MATH | 12.5K | 竞赛级 | `competition_math` | EN | LaTeX格式，多学科 |
| AQuA-RAT | 100K | 代数 | `aqua_rat` | EN | 多选题+推理 |
| MathQA | 37K | 中等 | `math_qa` | EN | 操作程序 |
| MetaMathQA | 395K | 各级 | `meta-math/MetaMathQA` | EN | 数据增强+CoT |
| CMATH | 1.7万 | 小学 | - | CN | 中文数学题 |

## 逻辑推理数据集 (Logical Reasoning)

| 数据集名称 | 数据量 | 类型 | HuggingFace ID | 语言 | 特点 |
|-----------|--------|------|----------------|------|------|
| LogiQA | 8.7K | 逻辑推理 | `logiqa` | CN/EN | 公务员考试 |
| ReClor | 6K | 阅读理解 | - | EN | 深度推理 |
| ProofWriter | 600K | 形式逻辑 | `allenai/proofwriter` | EN | 完整推理链 |
| FOLIO | 1.4K | 一阶逻辑 | - | EN | 专家标注 |
| AR-LSAT | 中量 | 分析推理 | - | EN | LSAT考题 |

## 常识推理数据集 (Commonsense Reasoning)

| 数据集名称 | 数据量 | 类型 | HuggingFace ID | 语言 | 特点 |
|-----------|--------|------|----------------|------|------|
| CommonsenseQA | 12K | 常识问答 | `commonsense_qa` | EN | 多选题 |
| StrategyQA | 2.7K | 隐式推理 | `wics/strategy-qa` | EN | 是非题 |
| PIQA | 21K | 物理常识 | `piqa` | EN | 日常交互 |
| COPA | 1K | 因果推理 | `super_glue` (copa) | EN | 因果关系 |
| CSQA 2.0 | - | 常识问答 | `tau/commonsense_qa_2.0` | EN | 更具挑战 |

## 综合推理数据集 (Comprehensive Reasoning)

| 数据集名称 | 数据量 | 领域 | HuggingFace ID | 语言 | 特点 |
|-----------|--------|------|----------------|------|------|
| MMLU | 15.9K | 57学科 | `cais/mmlu` | EN | 多任务 |
| BIG-Bench Hard | 23任务 | 综合 | `lukaemon/bbh` | EN | 最难任务 |
| ARC-Easy | 2.3K | 科学 | `ai2_arc` (ARC-Easy) | EN | 容易 |
| ARC-Challenge | 1.2K | 科学 | `ai2_arc` (ARC-Challenge) | EN | 困难 |
| OpenBookQA | 6K | 开卷 | `openbookqa` | EN | 知识+推理 |
| HellaSwag | 70K | 情境 | `hellaswag` | EN | 常识推理 |
| C-Eval | 13.9K | 52学科 | - | CN | 中文综合 |
| CMMLU | 多任务 | 综合 | `haonan-li/cmmlu` | CN | 中文MMLU |

## 代码推理数据集 (Code Reasoning)

| 数据集名称 | 数据量 | 难度 | HuggingFace ID | 语言 | 特点 |
|-----------|--------|------|----------------|------|------|
| HumanEval | 164 | 中等 | `openai_humaneval` | Python | OpenAI基准 |
| MBPP | 974 | 基础 | `mbpp` | Python | 带测试用例 |
| APPS | 10K | 各级 | `codeparrot/apps` | Python | 竞赛级 |
| CodeContests | 13K | 高难度 | `deepmind/code_contests` | 多语言 | DeepMind |

## 思维链数据集 (Chain-of-Thought)

| 数据集名称 | 数据量 | 类型 | HuggingFace ID | 语言 | 特点 |
|-----------|--------|------|----------------|------|------|
| MetaMathQA | 395K | 数学 | `meta-math/MetaMathQA` | EN | 详细步骤 |
| FLAN Collection | 大规模 | 多任务 | `conceptofmind/FLAN_2022` | EN | 指令微调 |
| WizardLM | 196K | 综合 | `WizardLM/WizardLM_evol_instruct_V2_196k` | EN | 进化指令 |

## 快速加载代码

### Python代码示例

```python
from datasets import load_dataset

# 数学推理
gsm8k = load_dataset("gsm8k", "main")
math = load_dataset("competition_math")
mathqa = load_dataset("math_qa")

# 逻辑推理
logiqa = load_dataset("logiqa")
proofwriter = load_dataset("allenai/proofwriter")

# 常识推理
commonsenseqa = load_dataset("commonsense_qa")
piqa = load_dataset("piqa")
copa = load_dataset("super_glue", "copa")

# 综合推理
mmlu = load_dataset("cais/mmlu", "all")
arc_easy = load_dataset("ai2_arc", "ARC-Easy")
arc_challenge = load_dataset("ai2_arc", "ARC-Challenge")
openbookqa = load_dataset("openbookqa", "main")
hellaswag = load_dataset("hellaswag")

# 代码推理
humaneval = load_dataset("openai_humaneval")
mbpp = load_dataset("mbpp")
apps = load_dataset("codeparrot/apps")

# 思维链
metamath = load_dataset("meta-math/MetaMathQA")
```

## 数据集选择建议

### 按训练目标选择

| 训练目标 | 推荐数据集组合 |
|---------|---------------|
| 数学能力 | GSM8K + MATH + MetaMathQA |
| 逻辑推理 | LogiQA + ProofWriter + ReClor |
| 常识理解 | CommonsenseQA + PIQA + StrategyQA |
| 通用推理 | MMLU + ARC + OpenBookQA + BIG-Bench |
| 代码生成 | HumanEval + MBPP + APPS |
| 中文推理 | CMATH + C-Eval + CMMLU + LogiQA |

### 按难度递进

1. **入门级**: PIQA, COPA, ARC-Easy, MBPP
2. **中级**: GSM8K, CommonsenseQA, HumanEval, ARC-Challenge
3. **高级**: MATH, ReClor, OpenBookQA, APPS
4. **专家级**: BIG-Bench Hard, CodeContests, Competition Math

### 按数据量

| 规模 | 数据集示例 |
|-----|-----------|
| 小型 (< 2K) | COPA, FOLIO, StrategyQA |
| 中型 (2K-10K) | GSM8K, LogiQA, CommonsenseQA, ARC |
| 大型 (10K-50K) | MATH, PIQA, MathQA |
| 超大型 (> 50K) | AQuA-RAT, HellaSwag, MetaMathQA |

## 数据集质量评分

| 数据集 | 质量 | 标注 | 推理深度 | 推荐度 |
|--------|------|------|---------|--------|
| GSM8K | ⭐⭐⭐⭐⭐ | 人工 | 多步 | ⭐⭐⭐⭐⭐ |
| MATH | ⭐⭐⭐⭐⭐ | 人工 | 深度 | ⭐⭐⭐⭐⭐ |
| MetaMathQA | ⭐⭐⭐⭐ | 合成 | 多步 | ⭐⭐⭐⭐ |
| CommonsenseQA | ⭐⭐⭐⭐⭐ | 人工 | 中度 | ⭐⭐⭐⭐⭐ |
| LogiQA | ⭐⭐⭐⭐⭐ | 人工 | 深度 | ⭐⭐⭐⭐⭐ |
| MMLU | ⭐⭐⭐⭐⭐ | 人工 | 各级 | ⭐⭐⭐⭐⭐ |
| HumanEval | ⭐⭐⭐⭐⭐ | 人工 | 中度 | ⭐⭐⭐⭐⭐ |
| ProofWriter | ⭐⭐⭐⭐ | 合成 | 深度 | ⭐⭐⭐⭐ |

## 混合数据集配方

### 通用推理模型
```
30% 数学推理 (GSM8K + MATH)
25% 常识推理 (CommonsenseQA + PIQA)
20% 逻辑推理 (LogiQA + ProofWriter)
15% 科学推理 (ARC + OpenBookQA)
10% 代码推理 (HumanEval + MBPP)
```

### 数学专家模型
```
40% GSM8K
30% MATH
20% MetaMathQA
10% MathQA
```

### 代码专家模型
```
40% MBPP
30% HumanEval
20% APPS
10% CodeContests
```

### 中文推理模型
```
30% CMATH
30% C-Eval
20% CMMLU
20% LogiQA (中文)
```

## 评估基准

| 基准测试 | 评估内容 | 难度 | 使用场景 |
|---------|---------|------|---------|
| GSM8K | 数学推理 | 中 | 基础数学能力 |
| MATH | 高级数学 | 高 | 竞赛级数学 |
| MMLU | 综合知识 | 中-高 | 通用能力 |
| BIG-Bench Hard | 综合推理 | 极高 | 前沿能力 |
| HumanEval | 代码生成 | 中 | 编程能力 |
| C-Eval | 中文知识 | 中-高 | 中文能力 |

## 最佳实践总结

✅ **推荐做法**
- 混合多种推理类型
- 使用包含推理步骤的数据集
- 从简单到困难递进训练
- 定期在测试集上评估
- 平衡不同数据集的样本量

❌ **避免做法**
- 只使用单一类型数据集
- 忽视数据质量
- 数据分布严重失衡
- 过度依赖合成数据
- 缺乏评估验证

## 资源链接

- 📚 详细指南: [reasoning_datasets_guide.md](reasoning_datasets_guide.md)
- 💻 实战教程: [reasoning_datasets_tutorial.ipynb](reasoning_datasets_tutorial.ipynb)
- 🏠 主页: [README.md](README.md)

---

**更新时间**: 2025-10-15
