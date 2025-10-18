#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple Flask API for SFT Data Collection
简单的 Flask API 用于 SFT 数据收集

This script demonstrates how to integrate the SFT data collector
with a REST API for real-time data collection.
"""

import json
from datetime import datetime
from sft_data_collector import SFTDataCollector

# Note: This is a demonstration script showing how to integrate with Flask
# To use this, you would need to install Flask: pip install flask

# Uncomment the following lines to use the Flask API:
"""
from flask import Flask, request, jsonify

app = Flask(__name__)
collector = SFTDataCollector(output_dir="./api_sft_data")


@app.route('/api/collect/tool_calling', methods=['POST'])
def collect_tool_calling():
    '''
    Endpoint to collect tool calling data
    
    POST /api/collect/tool_calling
    Body: {
        "user_query": "...",
        "tools": [...],
        "assistant_response": "...",
        "tool_calls": [...],
        "tool_results": [...],
        "final_response": "..."
    }
    '''
    try:
        data = request.json
        collector.add_tool_calling_example(
            user_query=data['user_query'],
            tools=data['tools'],
            assistant_response=data['assistant_response'],
            tool_calls=data['tool_calls'],
            tool_results=data['tool_results'],
            final_response=data['final_response']
        )
        return jsonify({
            "status": "success",
            "message": "Tool calling example added",
            "total_examples": len(collector.tool_calling_data)
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


@app.route('/api/collect/rag', methods=['POST'])
def collect_rag():
    '''
    Endpoint to collect RAG data
    
    POST /api/collect/rag
    Body: {
        "user_query": "...",
        "retrieval_query": "...",
        "retrieved_documents": [...],
        "assistant_response": "..."
    }
    '''
    try:
        data = request.json
        collector.add_rag_example(
            user_query=data['user_query'],
            retrieval_query=data['retrieval_query'],
            retrieved_documents=data['retrieved_documents'],
            assistant_response=data['assistant_response']
        )
        return jsonify({
            "status": "success",
            "message": "RAG example added",
            "total_examples": len(collector.rag_data)
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


@app.route('/api/save', methods=['POST'])
def save_data():
    '''Save all collected data to files'''
    try:
        collector.save_data()
        return jsonify({
            "status": "success",
            "message": "Data saved successfully",
            "stats": {
                "tool_calling_examples": len(collector.tool_calling_data),
                "rag_examples": len(collector.rag_data),
                "total_examples": len(collector.tool_calling_data) + len(collector.rag_data)
            }
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


@app.route('/api/stats', methods=['GET'])
def get_stats():
    '''Get statistics about collected data'''
    return jsonify({
        "tool_calling_examples": len(collector.tool_calling_data),
        "rag_examples": len(collector.rag_data),
        "total_examples": len(collector.tool_calling_data) + len(collector.rag_data)
    }), 200


if __name__ == '__main__':
    print("Starting SFT Data Collection API...")
    print("Endpoints:")
    print("  POST /api/collect/tool_calling - Add tool calling example")
    print("  POST /api/collect/rag - Add RAG example")
    print("  POST /api/save - Save collected data")
    print("  GET  /api/stats - Get collection statistics")
    app.run(debug=True, host='0.0.0.0', port=5000)
"""


def example_api_usage():
    """
    示例：如何使用 API 收集数据
    Example: How to use the API for data collection
    """
    print("=" * 60)
    print("API 使用示例 / API Usage Example")
    print("=" * 60)
    print("\n要使用 API，需要安装 Flask：")
    print("To use the API, install Flask:")
    print("  pip install flask\n")
    
    print("然后取消注释脚本中的 Flask 代码并运行：")
    print("Then uncomment the Flask code in the script and run:")
    print("  python api_example.py\n")
    
    print("示例 API 调用 / Example API Calls:")
    print("-" * 60)
    
    # Tool calling example
    tool_example = {
        "user_query": "What's the weather in Shanghai?",
        "tools": [{
            "name": "get_weather",
            "description": "Get weather information",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                }
            }
        }],
        "assistant_response": "Let me check the weather.",
        "tool_calls": [{
            "name": "get_weather",
            "arguments": {"location": "Shanghai"}
        }],
        "tool_results": [{
            "tool": "get_weather",
            "result": {"temperature": 22, "condition": "Sunny"}
        }],
        "final_response": "The weather in Shanghai is sunny with 22°C."
    }
    
    print("\n1. 添加工具调用示例 / Add Tool Calling Example:")
    print("POST /api/collect/tool_calling")
    print(json.dumps(tool_example, indent=2, ensure_ascii=False))
    
    # RAG example
    rag_example = {
        "user_query": "What is machine learning?",
        "retrieval_query": "machine learning definition",
        "retrieved_documents": [{
            "id": "doc_1",
            "title": "ML Introduction",
            "content": "Machine learning is a subset of AI...",
            "relevance_score": 0.95
        }],
        "assistant_response": "Machine learning is a subset of artificial intelligence..."
    }
    
    print("\n2. 添加 RAG 示例 / Add RAG Example:")
    print("POST /api/collect/rag")
    print(json.dumps(rag_example, indent=2, ensure_ascii=False))
    
    print("\n3. 保存数据 / Save Data:")
    print("POST /api/save")
    
    print("\n4. 获取统计信息 / Get Statistics:")
    print("GET /api/stats")
    
    print("\n" + "=" * 60)
    print("使用 curl 示例 / Using curl examples:")
    print("-" * 60)
    print("\n# Add tool calling example")
    print("curl -X POST http://localhost:5000/api/collect/tool_calling \\")
    print("  -H 'Content-Type: application/json' \\")
    print("  -d @tool_calling_example.json")
    print("\n# Save data")
    print("curl -X POST http://localhost:5000/api/save")
    print("\n# Get stats")
    print("curl http://localhost:5000/api/stats")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    example_api_usage()
