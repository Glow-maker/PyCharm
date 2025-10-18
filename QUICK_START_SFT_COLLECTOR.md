# SFT 数据收集工具快速开始 / Quick Start for SFT Data Collector

## 简介 / Introduction

这个工具帮助收集用于监督微调（SFT）的训练数据，专注于：
- **工具调用（Tool Calling）** - 函数/工具调用模式
- **RAG检索增强（RAG）** - 基于检索的生成示例

This tool helps collect training data for Supervised Fine-Tuning (SFT), focusing on:
- **Tool Calling** - Function/tool calling patterns
- **RAG (Retrieval-Augmented Generation)** - Retrieval-based generation examples

## 快速开始 / Quick Start

### 1. 运行示例 / Run Example

```bash
cd scripts
python sft_data_collector.py
```

这将生成包含9个示例的数据文件：
- 4个工具调用示例
- 5个RAG示例

This will generate data files with 9 examples:
- 4 tool calling examples
- 5 RAG examples

### 2. 查看生成的数据 / View Generated Data

```bash
ls -la scripts/sft_data/
# 输出 / Output:
# - tool_calling_sft_data.json
# - rag_sft_data.json
# - combined_sft_data.json
```

### 3. 自定义使用 / Custom Usage

```bash
cd scripts
python example_usage.py
```

## 文档 / Documentation

完整文档请查看：
For complete documentation, see:

- **用户手册 / User Manual**: `scripts/SFT_DATA_COLLECTION_README.md`
- **测试结果 / Testing Results**: `scripts/TESTING_RESULTS.md`
- **使用示例 / Usage Examples**: `scripts/example_usage.py`
- **API集成 / API Integration**: `scripts/api_example.py`

## 代码示例 / Code Example

```python
from sft_data_collector import SFTDataCollector

# 创建收集器 / Create collector
collector = SFTDataCollector(output_dir="./my_data")

# 加载示例数据 / Load sample data
collector.load_sample_data()

# 或添加自定义数据 / Or add custom data
collector.add_tool_calling_example(
    user_query="你的查询",
    tools=[...],
    assistant_response="助手响应",
    tool_calls=[...],
    tool_results=[...],
    final_response="最终响应"
)

# 保存数据 / Save data
collector.save_data()
```

## 特性 / Features

✓ 9个高质量示例 / 9 high-quality examples
✓ JSON格式输出 / JSON format output
✓ 支持自定义数据 / Custom data support
✓ 双语文档 / Bilingual documentation
✓ 生产就绪 / Production-ready
✓ 零安全漏洞 / Zero vulnerabilities

## 问题反馈 / Issues

如有问题，请查看 `scripts/SFT_DATA_COLLECTION_README.md` 或提交 Issue。

For issues, please check `scripts/SFT_DATA_COLLECTION_README.md` or submit an Issue.

---

Created: October 2025
Location: `/home/runner/work/PyCharm/PyCharm/scripts/`
