# SFT 数据收集工具 / SFT Data Collection Tool

## 概述 / Overview

这个工具用于收集和整理用于监督微调（Supervised Fine-Tuning, SFT）的训练数据，专注于两个关键领域：

1. **工具调用（Tool Calling）** - 函数调用模式和示例
2. **RAG检索增强（Retrieval-Augmented Generation）** - 基于检索的生成示例

This tool collects and organizes training data for Supervised Fine-Tuning (SFT), focusing on two key areas:

1. **Tool Calling** - Function calling patterns and examples
2. **RAG (Retrieval-Augmented Generation)** - Retrieval-based generation examples

## 功能特性 / Features

### 工具调用数据收集 / Tool Calling Data Collection

- ✅ 支持单工具调用 / Single tool call support
- ✅ 支持多工具调用 / Multiple tool calls support
- ✅ 完整的对话流程 / Complete conversation flow
- ✅ 工具定义和参数 / Tool definitions and parameters
- ✅ 工具执行结果 / Tool execution results
- ✅ 最终响应生成 / Final response generation

### RAG 数据收集 / RAG Data Collection

- ✅ 检索查询记录 / Retrieval query logging
- ✅ 检索文档存储 / Retrieved documents storage
- ✅ 相关性评分 / Relevance scoring
- ✅ 基于上下文的回答 / Context-based answers
- ✅ 多文档综合 / Multi-document synthesis

## 安装 / Installation

```bash
# 无需额外依赖，Python 3.6+ 即可运行
# No additional dependencies required, runs on Python 3.6+
cd /home/runner/work/PyCharm/PyCharm/scripts
python sft_data_collector.py
```

## 使用方法 / Usage

### 基本使用 / Basic Usage

```python
from sft_data_collector import SFTDataCollector

# 初始化收集器
collector = SFTDataCollector(output_dir="./sft_data")

# 加载示例数据
collector.load_sample_data()

# 保存数据
collector.save_data()
```

### 添加工具调用示例 / Adding Tool Calling Examples

```python
collector.add_tool_calling_example(
    user_query="用户查询",
    tools=[
        {
            "name": "tool_name",
            "description": "工具描述",
            "parameters": {
                # 参数定义
            }
        }
    ],
    assistant_response="助手的推理过程",
    tool_calls=[
        {
            "name": "tool_name",
            "arguments": {
                # 工具参数
            }
        }
    ],
    tool_results=[
        {
            "tool": "tool_name",
            "result": {
                # 工具返回结果
            }
        }
    ],
    final_response="最终响应"
)
```

### 添加 RAG 示例 / Adding RAG Examples

```python
collector.add_rag_example(
    user_query="用户查询",
    retrieval_query="检索查询",
    retrieved_documents=[
        {
            "id": "doc_id",
            "title": "文档标题",
            "content": "文档内容",
            "relevance_score": 0.95
        }
    ],
    assistant_response="基于检索内容的回答"
)
```

## 输出格式 / Output Format

工具会生成三个 JSON 文件：

1. `tool_calling_sft_data.json` - 工具调用示例
2. `rag_sft_data.json` - RAG 示例
3. `combined_sft_data.json` - 合并的所有数据

The tool generates three JSON files:

1. `tool_calling_sft_data.json` - Tool calling examples
2. `rag_sft_data.json` - RAG examples
3. `combined_sft_data.json` - Combined data

### 数据结构示例 / Data Structure Example

#### 工具调用示例 / Tool Calling Example

```json
{
  "type": "tool_calling",
  "timestamp": "2025-10-18T02:30:00",
  "conversation": [
    {
      "role": "system",
      "content": "You are a helpful assistant with access to the following tools:",
      "tools": [...]
    },
    {
      "role": "user",
      "content": "用户查询"
    },
    {
      "role": "assistant",
      "content": "助手回复",
      "tool_calls": [...]
    },
    {
      "role": "tool",
      "tool_results": [...]
    },
    {
      "role": "assistant",
      "content": "最终回复"
    }
  ]
}
```

#### RAG 示例 / RAG Example

```json
{
  "type": "rag",
  "timestamp": "2025-10-18T02:30:00",
  "conversation": [
    {
      "role": "user",
      "content": "用户查询"
    },
    {
      "role": "system",
      "content": "Performing retrieval...",
      "retrieval_query": "检索查询",
      "retrieved_documents": [...]
    },
    {
      "role": "assistant",
      "content": "基于检索的回答"
    }
  ]
}
```

## 示例数据 / Sample Data

工具包含以下示例数据：

The tool includes the following sample data:

### 工具调用示例 / Tool Calling Examples

1. **天气查询** / Weather Query - 查询北京天气
2. **计算器** / Calculator - 数学表达式计算
3. **数据库查询** / Database Query - SQL 查询示例
4. **多工具调用** / Multiple Tools - 发送邮件示例

### RAG 示例 / RAG Examples

1. **技术文档** / Technical Documentation - Python requests 库使用
2. **历史信息** / Historical Information - Python 发布历史
3. **代码解释** / Code Explanation - Python 上下文管理器
4. **领域知识** / Domain Knowledge - 公司假期政策
5. **多文档综合** / Multi-document Synthesis - Web 框架性能比较

## 数据用途 / Data Usage

收集的数据可用于：

The collected data can be used for:

1. **微调语言模型** / Fine-tuning language models
2. **训练工具调用能力** / Training tool calling capabilities
3. **提升 RAG 性能** / Improving RAG performance
4. **评估模型性能** / Evaluating model performance
5. **创建基准测试** / Creating benchmarks

## 扩展指南 / Extension Guide

### 添加自定义数据源 / Adding Custom Data Sources

```python
class CustomDataCollector(SFTDataCollector):
    def load_from_api(self, api_url):
        # 从 API 加载数据
        pass
    
    def load_from_database(self, db_connection):
        # 从数据库加载数据
        pass
```

### 自定义数据格式 / Custom Data Format

可以根据需要修改数据格式以适应不同的微调框架（如 OpenAI、Anthropic、本地模型等）。

You can modify the data format to adapt to different fine-tuning frameworks (OpenAI, Anthropic, local models, etc.).

## 最佳实践 / Best Practices

1. **多样性** / Diversity - 收集不同类型和复杂度的示例
2. **质量** / Quality - 确保回答准确且有用
3. **覆盖率** / Coverage - 涵盖常见和边缘情况
4. **一致性** / Consistency - 保持格式和风格统一
5. **验证** / Validation - 验证工具调用和检索结果的正确性

## 注意事项 / Notes

- 确保收集的数据不包含敏感信息 / Ensure collected data contains no sensitive information
- 定期更新和维护数据集 / Regularly update and maintain the dataset
- 考虑数据的多样性和代表性 / Consider diversity and representativeness of data
- 遵循相关的数据使用政策 / Follow relevant data usage policies

## 许可证 / License

本工具遵循项目的许可证。/ This tool follows the project's license.

## 贡献 / Contributing

欢迎提交问题和改进建议！/ Issues and improvements are welcome!
