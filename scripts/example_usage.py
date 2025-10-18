#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
示例：如何使用 SFT 数据收集器
Example: How to use the SFT Data Collector
"""

from sft_data_collector import SFTDataCollector


def example_custom_tool_calling():
    """示例：添加自定义工具调用数据"""
    collector = SFTDataCollector(output_dir="./my_custom_sft_data")
    
    # 示例 1: 文件操作工具
    collector.add_tool_calling_example(
        user_query="请帮我读取 /data/config.json 文件的内容",
        tools=[
            {
                "name": "read_file",
                "description": "读取文件内容",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "文件路径"
                        }
                    },
                    "required": ["file_path"]
                }
            }
        ],
        assistant_response="我将为您读取该文件。",
        tool_calls=[
            {
                "name": "read_file",
                "arguments": {
                    "file_path": "/data/config.json"
                }
            }
        ],
        tool_results=[
            {
                "tool": "read_file",
                "result": {
                    "content": '{"api_key": "xxx", "timeout": 30}',
                    "size": 45,
                    "encoding": "utf-8"
                }
            }
        ],
        final_response="文件内容如下：\n```json\n{\"api_key\": \"xxx\", \"timeout\": 30}\n```\n文件大小为 45 字节。"
    )
    
    # 示例 2: API 调用工具
    collector.add_tool_calling_example(
        user_query="获取 GitHub 仓库 python/cpython 的星标数",
        tools=[
            {
                "name": "github_api",
                "description": "调用 GitHub API 获取仓库信息",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "仓库所有者"},
                        "repo": {"type": "string", "description": "仓库名称"}
                    },
                    "required": ["owner", "repo"]
                }
            }
        ],
        assistant_response="让我查询 GitHub API。",
        tool_calls=[
            {
                "name": "github_api",
                "arguments": {
                    "owner": "python",
                    "repo": "cpython"
                }
            }
        ],
        tool_results=[
            {
                "tool": "github_api",
                "result": {
                    "name": "cpython",
                    "full_name": "python/cpython",
                    "stars": 58234,
                    "forks": 29876,
                    "language": "Python"
                }
            }
        ],
        final_response="python/cpython 仓库目前有 58,234 个星标，29,876 个 fork。"
    )
    
    return collector


def example_custom_rag():
    """示例：添加自定义 RAG 数据"""
    collector = SFTDataCollector(output_dir="./my_custom_sft_data")
    
    # 示例 1: 产品文档查询
    collector.add_rag_example(
        user_query="如何配置数据库连接池？",
        retrieval_query="数据库连接池配置方法",
        retrieved_documents=[
            {
                "id": "doc_db_001",
                "title": "数据库连接池配置指南",
                "content": "配置连接池需要设置以下参数：max_connections（最大连接数），min_connections（最小连接数），timeout（超时时间）。推荐配置：max_connections=20, min_connections=5, timeout=30。",
                "relevance_score": 0.96
            },
            {
                "id": "doc_db_002",
                "title": "性能优化最佳实践",
                "content": "连接池大小应根据并发请求数和数据库负载确定。过大会浪费资源，过小会导致连接等待。",
                "relevance_score": 0.88
            }
        ],
        assistant_response="""配置数据库连接池需要注意以下几点：

1. **基本参数设置**：
   - max_connections: 最大连接数，推荐设置为 20
   - min_connections: 最小连接数，推荐设置为 5
   - timeout: 连接超时时间，推荐设置为 30 秒

2. **调优建议**：
   - 根据实际并发请求数调整连接池大小
   - 避免连接池过大造成资源浪费
   - 避免连接池过小导致连接等待

示例配置：
```python
pool_config = {
    'max_connections': 20,
    'min_connections': 5,
    'timeout': 30
}
```"""
    )
    
    # 示例 2: 代码库搜索
    collector.add_rag_example(
        user_query="在项目中如何实现用户认证？",
        retrieval_query="用户认证实现方法 authentication",
        retrieved_documents=[
            {
                "id": "code_001",
                "title": "auth/authentication.py",
                "content": "def authenticate_user(username, password):\n    user = User.query.filter_by(username=username).first()\n    if user and check_password_hash(user.password, password):\n        return user\n    return None",
                "relevance_score": 0.94
            },
            {
                "id": "doc_security_001",
                "title": "安全实践文档",
                "content": "用户密码应使用 bcrypt 或 argon2 进行哈希存储。认证成功后应生成 JWT token 用于后续请求验证。",
                "relevance_score": 0.92
            }
        ],
        assistant_response="""在项目中实现用户认证的步骤如下：

1. **密码存储**：使用 bcrypt 或 argon2 对密码进行哈希处理
2. **验证流程**：
   ```python
   def authenticate_user(username, password):
       user = User.query.filter_by(username=username).first()
       if user and check_password_hash(user.password, password):
           return user
       return None
   ```
3. **Token 生成**：认证成功后生成 JWT token 用于后续请求

这样可以确保用户密码安全，并提供无状态的认证机制。"""
    )
    
    return collector


def main():
    """主函数：演示如何使用数据收集器"""
    print("=" * 60)
    print("SFT 数据收集器使用示例")
    print("Example Usage of SFT Data Collector")
    print("=" * 60)
    
    # 创建自定义工具调用数据
    print("\n1. 创建自定义工具调用数据...")
    tool_collector = example_custom_tool_calling()
    
    # 创建自定义 RAG 数据
    print("2. 创建自定义 RAG 数据...")
    rag_collector = example_custom_rag()
    
    # 合并数据
    print("3. 合并所有数据...")
    combined_collector = SFTDataCollector(output_dir="./my_custom_sft_data")
    combined_collector.tool_calling_data = tool_collector.tool_calling_data
    combined_collector.rag_data = rag_collector.rag_data
    
    # 保存数据
    print("4. 保存数据到文件...")
    combined_collector.save_data()
    
    print("\n" + "=" * 60)
    print("完成！数据已保存到 ./my_custom_sft_data 目录")
    print("Done! Data saved to ./my_custom_sft_data directory")
    print("=" * 60)


if __name__ == "__main__":
    main()
