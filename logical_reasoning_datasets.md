# 逻辑推理数据集 / Logical Reasoning Datasets with Think Blocks

本文档整理了包含思考过程（think blocks）的逻辑推理数据集，适用于训练具有推理能力的AI模型。

This document organizes logical reasoning datasets that include think blocks (reasoning traces), suitable for training AI models with reasoning capabilities.

---

## 目录 / Table of Contents

1. [Zebra Puzzle 斑马谜题](#1-zebra-puzzle-斑马谜题)
2. [Ordering Puzzle 排序谜题](#2-ordering-puzzle-排序谜题)
3. [Graph Puzzle 图谜题](#3-graph-puzzle-图谜题)
4. [ARC-AGI-1/2 抽象推理挑战](#4-arc-agi-12-抽象推理挑战)
5. [BARC 基准抽象推理语料库](#5-barc-基准抽象推理语料库)
6. [其他推荐数据集](#6-其他推荐数据集--other-recommended-datasets)

---

## 1. Zebra Puzzle 斑马谜题

### 数据集描述 / Description
斑马谜题是一类经典的约束满足逻辑推理问题。最著名的是爱因斯坦谜题，需要通过一系列线索推导出正确答案。

Zebra Puzzles are classic constraint satisfaction logic problems. The most famous is Einstein's Riddle, which requires deriving the correct answer through a series of clues.

### 推荐数据集 / Recommended Datasets

#### LogiQA / LogiQA 2.0
- **链接 / Link**: https://github.com/lgw863/LogiQA-dataset
- **HuggingFace**: https://huggingface.co/datasets/lucasmccabe/logiqa
- **特点 / Features**:
  - 包含逻辑推理题目
  - 有中英文版本
  - 包含详细的推理步骤
  - 适合训练思维链模型

#### PuzzleBench
- **链接 / Link**: https://github.com/declare-lab/puzzle-reasoning
- **Paper**: arXiv:2312.10263
- **特点 / Features**:
  - 包含Zebra谜题及其变体
  - 提供推理步骤标注
  - 多样化的难度级别
  - 结构化的思考过程

#### BigBench Logic Puzzles
- **链接 / Link**: https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/logical_deduction
- **特点 / Features**:
  - 包含大量逻辑演绎题目
  - 包括Zebra puzzle类型
  - 有详细的推理链
  - 适合few-shot学习

---

## 2. Ordering Puzzle 排序谜题

### 数据集描述 / Description
排序谜题要求根据给定的约束条件对一组对象进行排序或排列。

Ordering puzzles require sorting or arranging a set of objects based on given constraints.

### 推荐数据集 / Recommended Datasets

#### AR-LSAT (Analytical Reasoning LSAT)
- **链接 / Link**: https://github.com/zhongwanjun/AR-LSAT
- **Paper**: "Towards Complex Analytical Reasoning: A Dataset and Baselines"
- **特点 / Features**:
  - 来自LSAT考试的分析推理题
  - 包含排序、分组等多种类型
  - 提供详细的推理步骤
  - 高质量的思考过程标注

#### ProofWriter
- **链接 / Link**: https://allenai.org/data/proofwriter
- **HuggingFace**: https://huggingface.co/datasets/allenai/proofwriter
- **特点 / Features**:
  - 包含形式化证明步骤
  - 逐步推理过程
  - 多种深度的证明树
  - 适合训练推理模型

#### CLUTRR
- **链接 / Link**: https://github.com/facebookresearch/clutrr
- **特点 / Features**:
  - 关系推理和排序
  - 包含推理步骤
  - 可配置的复杂度
  - 系统性测试推理能力

---

## 3. Graph Puzzle 图谜题

### 数据集描述 / Description
图谜题涉及图结构的推理，如路径查找、图着色、图同构等问题。

Graph puzzles involve reasoning about graph structures, such as path finding, graph coloring, and graph isomorphism.

### 推荐数据集 / Recommended Datasets

#### GraphQA
- **链接 / Link**: https://github.com/Lukeming-tsinghua/GraphQA
- **特点 / Features**:
  - 基于图结构的问答
  - 包含推理路径
  - 多跳推理
  - 结构化思考过程

#### DRUM (Differentiable Reasoning on Graphs)
- **链接 / Link**: https://github.com/alisadeghian/DRUM
- **Paper**: "Learning to Reason Over Scene Graphs"
- **特点 / Features**:
  - 图上的可微推理
  - 包含推理步骤
  - 支持复杂的图推理
  - 神经符号推理

#### GNN Reasoning Datasets
- **链接 / Link**: https://github.com/snap-stanford/ogb
- **特点 / Features**:
  - Open Graph Benchmark
  - 多种图推理任务
  - 标准化评估
  - 适合图神经网络

#### PathQA
- **链接 / Link**: Research datasets for path reasoning on graphs
- **特点 / Features**:
  - 路径推理问题
  - 逐步推理过程
  - 多种图复杂度
  - 适合训练推理能力

---

## 4. ARC-AGI-1/2 抽象推理挑战

### 数据集描述 / Description
ARC (Abstraction and Reasoning Corpus) 是Chollet提出的测试通用AI推理能力的基准。

ARC (Abstraction and Reasoning Corpus) is a benchmark proposed by Chollet to test general AI reasoning capabilities.

### 推荐数据集 / Recommended Datasets

#### ARC-AGI (Original)
- **链接 / Link**: https://github.com/fchollet/ARC-AGI
- **Kaggle Competition**: https://www.kaggle.com/c/abstraction-and-reasoning-challenge
- **特点 / Features**:
  - 视觉抽象推理
  - 需要少样本学习
  - 测试核心智能
  - 包含训练集和评估集

#### ARC-AGI-1
- **链接 / Link**: https://github.com/arc-prize/arc-prize
- **特点 / Features**:
  - 第一版ARC数据集
  - 400个训练任务
  - 400个评估任务
  - 需要找到潜在模式

#### ARC-AGI-2 (Extended)
- **链接 / Link**: https://github.com/neoneye/arc-dataset-collection
- **特点 / Features**:
  - 扩展版ARC数据集
  - 包含合成任务
  - 更多训练样本
  - 社区贡献的任务

#### ConceptARC
- **链接 / Link**: https://github.com/victorvikram/ConceptARC
- **Paper**: "ConceptARC: An Abstract Reasoning Corpus with Explicit Conceptual Labels"
- **特点 / Features**:
  - 带有概念标签的ARC
  - 明确的推理步骤
  - 概念层面的解释
  - 便于训练和理解

#### RE-ARC (Reasoning-Enhanced ARC)
- **链接 / Link**: Research extensions to ARC
- **特点 / Features**:
  - 增强的推理步骤
  - 逐步解决方案
  - 思考过程标注
  - 适合训练推理模型

---

## 5. BARC 基准抽象推理语料库

### 数据集描述 / Description
BARC (Benchmark for Abstraction and Reasoning Corpus) 是对ARC的改进和扩展，提供了更多标注和推理步骤。

BARC (Benchmark for Abstraction and Reasoning Corpus) is an improvement and extension of ARC, providing more annotations and reasoning steps.

### 推荐数据集 / Recommended Datasets

#### BARC Dataset
- **链接 / Link**: https://github.com/xu-song/BARC
- **特点 / Features**:
  - 基于ARC的改进
  - 更详细的标注
  - 包含推理步骤
  - 提供解题思路

#### Mini-ARC
- **链接 / Link**: https://github.com/bilalsal/mini-arc
- **特点 / Features**:
  - 简化版的ARC
  - 适合初学者
  - 包含详细解释
  - 逐步推理过程

#### ARC-like Synthetic Datasets
- **链接 / Link**: Community generated datasets
- **特点 / Features**:
  - 合成的类ARC任务
  - 可控的难度
  - 大量训练数据
  - 包含生成规则

---

## 6. 其他推荐数据集 / Other Recommended Datasets

### Chain-of-Thought Datasets 思维链数据集

#### GSM8K
- **链接 / Link**: https://github.com/openai/grade-school-math
- **HuggingFace**: https://huggingface.co/datasets/gsm8k
- **特点 / Features**:
  - 数学推理题
  - 包含详细解题步骤
  - 思维链标注
  - 8000+训练样本

#### MATH Dataset
- **链接 / Link**: https://github.com/hendrycks/math
- **HuggingFace**: https://huggingface.co/datasets/hendrycks/math
- **特点 / Features**:
  - 高难度数学题
  - 详细的解题过程
  - 多个难度级别
  - 12,500个问题

#### StrategyQA
- **链接 / Link**: https://github.com/eladsegal/strategyqa
- **HuggingFace**: https://huggingface.co/datasets/strategy-qa/strategy-qa
- **特点 / Features**:
  - 需要隐式推理
  - 多步推理问题
  - 包含推理策略
  - 2,780个问题

#### EntailmentBank
- **链接 / Link**: https://allenai.org/data/entailmentbank
- **HuggingFace**: https://huggingface.co/datasets/allenai/entailment_trees_emnlp2021_od
- **特点 / Features**:
  - 包含完整推理树
  - 逐步蕴含推理
  - 多步推理链
  - 适合训练推理模型

### Logic and Reasoning Benchmarks 逻辑推理基准

#### ReClor
- **链接 / Link**: https://github.com/yuweihao/reclor
- **HuggingFace**: https://huggingface.co/datasets/reclor
- **特点 / Features**:
  - 标准化逻辑推理测试
  - 来自GMAT和LSAT
  - 高质量标注
  - 6,000+问题

#### LogicNLI
- **链接 / Link**: https://github.com/asnani04/logicnli
- **特点 / Features**:
  - 逻辑自然语言推理
  - 包含推理步骤
  - 多种逻辑关系
  - 系统性评估

#### bAbI Tasks
- **链接 / Link**: https://research.facebook.com/downloads/babi/
- **特点 / Features**:
  - 20个推理任务
  - 测试不同推理能力
  - 简单到复杂的推理
  - 包含推理路径

### Spatial and Temporal Reasoning 空间和时间推理

#### SPARTQA
- **链接 / Link**: https://github.com/Jacobsonradical/SPARTQA
- **特点 / Features**:
  - 空间推理问题
  - 包含推理步骤
  - 多种空间关系
  - 适合空间推理训练

#### TIMESTEP
- **链接 / Link**: Research datasets for temporal reasoning
- **特点 / Features**:
  - 时间推理问题
  - 包含时序推理
  - 事件排序
  - 时间关系推理

---

## 使用建议 / Usage Recommendations

### 训练模型的最佳实践 / Best Practices for Training Models

1. **混合多种数据集** / Mix Multiple Datasets
   - 结合不同类型的推理问题
   - 提高模型的泛化能力
   - 平衡不同难度的样本

2. **重点关注思考过程** / Focus on Thinking Process
   - 使用包含详细推理步骤的数据
   - 训练模型生成中间推理步骤
   - 评估推理过程的正确性

3. **渐进式训练** / Progressive Training
   - 从简单任务开始
   - 逐步增加难度
   - 使用课程学习策略

4. **提示工程** / Prompt Engineering
   - 设计合适的推理提示
   - 引导模型展示思考过程
   - 使用Chain-of-Thought等技术

### 数据集选择指南 / Dataset Selection Guide

| 应用场景 / Use Case | 推荐数据集 / Recommended Datasets |
|---------------------|----------------------------------|
| 逻辑演绎 / Logical Deduction | LogiQA, ReClor, BigBench Logic |
| 数学推理 / Mathematical Reasoning | GSM8K, MATH, ProofWriter |
| 视觉推理 / Visual Reasoning | ARC-AGI, ConceptARC, BARC |
| 图推理 / Graph Reasoning | GraphQA, DRUM, PathQA |
| 自然语言推理 / NLI | EntailmentBank, LogicNLI, bAbI |
| 复杂推理 / Complex Reasoning | AR-LSAT, StrategyQA, CLUTRR |

---

## 数据集评估标准 / Dataset Evaluation Criteria

### 思考块质量 / Think Block Quality
- **完整性** / Completeness: 是否包含完整的推理过程
- **可解释性** / Interpretability: 推理步骤是否清晰易懂
- **正确性** / Correctness: 推理逻辑是否正确
- **粒度** / Granularity: 推理步骤的细致程度

### 数据集规模 / Dataset Scale
- **训练样本数** / Training Samples: 至少1000+样本
- **评估样本数** / Evaluation Samples: 至少200+样本
- **多样性** / Diversity: 问题类型的多样性

### 技术特性 / Technical Features
- **格式化** / Formatting: 是否有标准格式
- **可访问性** / Accessibility: 是否容易获取和使用
- **维护状态** / Maintenance: 是否持续更新
- **社区支持** / Community Support: 是否有活跃社区

---

## 相关资源 / Related Resources

### 研究论文 / Research Papers
- **Chain-of-Thought Prompting**: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022)
- **Self-Consistency**: "Self-Consistency Improves Chain of Thought Reasoning" (Wang et al., 2022)
- **Tree of Thoughts**: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" (Yao et al., 2023)
- **Least-to-Most Prompting**: "Least-to-Most Prompting Enables Complex Reasoning" (Zhou et al., 2022)

### 工具和框架 / Tools and Frameworks
- **LangChain**: 用于构建推理链的框架
- **DSPy**: 声明式自优化提示框架
- **Guidance**: 结构化提示生成
- **Semantic Kernel**: Microsoft的推理框架

### 评估工具 / Evaluation Tools
- **HELM**: 全面的语言模型评估
- **lm-evaluation-harness**: 标准化评估工具
- **BIG-Bench**: 大规模基准测试

---

## 更新日志 / Update Log

- **2025-10-15**: 初始版本创建
  - 添加主要数据集类别
  - 包含详细的数据集信息
  - 提供使用建议和资源链接

---

## 贡献 / Contributing

欢迎贡献更多数据集信息和使用经验！

Contributions of additional dataset information and usage experiences are welcome!

---

## 许可证 / License

本文档采用 CC BY 4.0 许可证。各数据集遵循其各自的许可证。

This document is licensed under CC BY 4.0. Individual datasets follow their respective licenses.
