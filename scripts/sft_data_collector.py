"""
SFT Data Collector for Tool Calling and RAG
============================================

This script collects and organizes Supervised Fine-Tuning (SFT) data for:
1. Tool/Function Calling patterns
2. RAG (Retrieval-Augmented Generation) examples

The data can be used for fine-tuning language models to improve their
ability to use tools and perform retrieval-augmented generation.
"""

import json
import os
from typing import List, Dict, Any
from datetime import datetime


class SFTDataCollector:
    """Collects and manages SFT training data for tool calling and RAG."""
    
    def __init__(self, output_dir: str = "./sft_data"):
        """
        Initialize the SFT data collector.
        
        Args:
            output_dir: Directory to save collected data
        """
        self.output_dir = output_dir
        self.tool_calling_data = []
        self.rag_data = []
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def add_tool_calling_example(self, 
                                  user_query: str,
                                  tools: List[Dict[str, Any]],
                                  assistant_response: str,
                                  tool_calls: List[Dict[str, Any]],
                                  tool_results: List[Dict[str, Any]],
                                  final_response: str) -> None:
        """
        Add a tool calling example to the dataset.
        
        Args:
            user_query: The user's original query
            tools: List of available tools/functions
            assistant_response: Assistant's reasoning before tool call
            tool_calls: List of tool calls made by the assistant
            tool_results: Results returned by the tools
            final_response: Final response incorporating tool results
        """
        example = {
            "type": "tool_calling",
            "timestamp": datetime.now().isoformat(),
            "conversation": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant with access to the following tools:",
                    "tools": tools
                },
                {
                    "role": "user",
                    "content": user_query
                },
                {
                    "role": "assistant",
                    "content": assistant_response,
                    "tool_calls": tool_calls
                },
                {
                    "role": "tool",
                    "tool_results": tool_results
                },
                {
                    "role": "assistant",
                    "content": final_response
                }
            ]
        }
        self.tool_calling_data.append(example)
    
    def add_rag_example(self,
                       user_query: str,
                       retrieved_documents: List[Dict[str, Any]],
                       retrieval_query: str,
                       assistant_response: str) -> None:
        """
        Add a RAG example to the dataset.
        
        Args:
            user_query: The user's original query
            retrieved_documents: Documents retrieved from the knowledge base
            retrieval_query: The query used for retrieval
            assistant_response: Final response using retrieved context
        """
        example = {
            "type": "rag",
            "timestamp": datetime.now().isoformat(),
            "conversation": [
                {
                    "role": "user",
                    "content": user_query
                },
                {
                    "role": "system",
                    "content": "Performing retrieval...",
                    "retrieval_query": retrieval_query,
                    "retrieved_documents": retrieved_documents
                },
                {
                    "role": "assistant",
                    "content": assistant_response
                }
            ]
        }
        self.rag_data.append(example)
    
    def save_data(self) -> None:
        """Save collected data to JSON files."""
        # Save tool calling data
        if self.tool_calling_data:
            tool_calling_file = os.path.join(self.output_dir, "tool_calling_sft_data.json")
            with open(tool_calling_file, 'w', encoding='utf-8') as f:
                json.dump(self.tool_calling_data, f, ensure_ascii=False, indent=2)
            print(f"Saved {len(self.tool_calling_data)} tool calling examples to {tool_calling_file}")
        
        # Save RAG data
        if self.rag_data:
            rag_file = os.path.join(self.output_dir, "rag_sft_data.json")
            with open(rag_file, 'w', encoding='utf-8') as f:
                json.dump(self.rag_data, f, ensure_ascii=False, indent=2)
            print(f"Saved {len(self.rag_data)} RAG examples to {rag_file}")
        
        # Save combined data
        combined_data = {
            "tool_calling": self.tool_calling_data,
            "rag": self.rag_data,
            "metadata": {
                "total_examples": len(self.tool_calling_data) + len(self.rag_data),
                "tool_calling_examples": len(self.tool_calling_data),
                "rag_examples": len(self.rag_data),
                "generated_at": datetime.now().isoformat()
            }
        }
        combined_file = os.path.join(self.output_dir, "combined_sft_data.json")
        with open(combined_file, 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, ensure_ascii=False, indent=2)
        print(f"Saved combined data to {combined_file}")
    
    def extend_from(self, other_collector: 'SFTDataCollector') -> None:
        """
        Extend data from another collector.
        
        Args:
            other_collector: Another SFTDataCollector instance to merge data from
        """
        self.tool_calling_data.extend(other_collector.tool_calling_data)
        self.rag_data.extend(other_collector.rag_data)
    
    def load_sample_data(self) -> None:
        """Load sample tool calling and RAG data for demonstration."""
        # Sample Tool Calling Examples
        self._add_sample_tool_calling_examples()
        
        # Sample RAG Examples
        self._add_sample_rag_examples()
    
    def _add_sample_tool_calling_examples(self) -> None:
        """Add sample tool calling examples."""
        
        # Example 1: Weather query
        self.add_tool_calling_example(
            user_query="What's the weather like in Beijing today?",
            tools=[
                {
                    "name": "get_weather",
                    "description": "Get current weather information for a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city name"
                            },
                            "unit": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "Temperature unit"
                            }
                        },
                        "required": ["location"]
                    }
                }
            ],
            assistant_response="I'll check the weather in Beijing for you.",
            tool_calls=[
                {
                    "name": "get_weather",
                    "arguments": {
                        "location": "Beijing",
                        "unit": "celsius"
                    }
                }
            ],
            tool_results=[
                {
                    "tool": "get_weather",
                    "result": {
                        "location": "Beijing",
                        "temperature": 15,
                        "condition": "Partly cloudy",
                        "humidity": 65,
                        "wind_speed": 12
                    }
                }
            ],
            final_response="The current weather in Beijing is partly cloudy with a temperature of 15°C. The humidity is at 65% and wind speed is 12 km/h."
        )
        
        # Example 2: Calculator
        self.add_tool_calling_example(
            user_query="Calculate 234 * 567 + 89",
            tools=[
                {
                    "name": "calculator",
                    "description": "Perform mathematical calculations",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "Mathematical expression to evaluate"
                            }
                        },
                        "required": ["expression"]
                    }
                }
            ],
            assistant_response="I'll calculate that expression for you.",
            tool_calls=[
                {
                    "name": "calculator",
                    "arguments": {
                        "expression": "234 * 567 + 89"
                    }
                }
            ],
            tool_results=[
                {
                    "tool": "calculator",
                    "result": {
                        "expression": "234 * 567 + 89",
                        "result": 132767
                    }
                }
            ],
            final_response="The result of 234 × 567 + 89 is 132,767."
        )
        
        # Example 3: Database query
        self.add_tool_calling_example(
            user_query="Find all users who registered in the last 7 days",
            tools=[
                {
                    "name": "query_database",
                    "description": "Query the database with SQL",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "SQL query to execute"
                            },
                            "parameters": {
                                "type": "object",
                                "description": "Query parameters"
                            }
                        },
                        "required": ["query"]
                    }
                }
            ],
            assistant_response="I'll query the database to find users who registered in the last 7 days.",
            tool_calls=[
                {
                    "name": "query_database",
                    "arguments": {
                        "query": "SELECT * FROM users WHERE registration_date >= DATE_SUB(NOW(), INTERVAL 7 DAY) ORDER BY registration_date DESC"
                    }
                }
            ],
            tool_results=[
                {
                    "tool": "query_database",
                    "result": {
                        "rows": [
                            {"id": 1234, "username": "user1", "email": "user1@example.com", "registration_date": "2025-10-15"},
                            {"id": 1235, "username": "user2", "email": "user2@example.com", "registration_date": "2025-10-14"},
                            {"id": 1236, "username": "user3", "email": "user3@example.com", "registration_date": "2025-10-13"}
                        ],
                        "count": 3
                    }
                }
            ],
            final_response="I found 3 users who registered in the last 7 days:\n1. user1 (user1@example.com) - registered on Oct 15\n2. user2 (user2@example.com) - registered on Oct 14\n3. user3 (user3@example.com) - registered on Oct 13"
        )
        
        # Example 4: Multiple tool calls
        self.add_tool_calling_example(
            user_query="Send an email to john@example.com about tomorrow's meeting at 2 PM",
            tools=[
                {
                    "name": "get_current_time",
                    "description": "Get the current date and time",
                    "parameters": {"type": "object", "properties": {}}
                },
                {
                    "name": "send_email",
                    "description": "Send an email",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "to": {"type": "string", "description": "Recipient email"},
                            "subject": {"type": "string", "description": "Email subject"},
                            "body": {"type": "string", "description": "Email body"}
                        },
                        "required": ["to", "subject", "body"]
                    }
                }
            ],
            assistant_response="I'll first check the current date and then send the email.",
            tool_calls=[
                {
                    "name": "get_current_time",
                    "arguments": {}
                },
                {
                    "name": "send_email",
                    "arguments": {
                        "to": "john@example.com",
                        "subject": "Meeting Reminder - Tomorrow at 2 PM",
                        "body": "Hi John,\n\nThis is a reminder about our meeting scheduled for tomorrow (October 19, 2025) at 2:00 PM.\n\nBest regards"
                    }
                }
            ],
            tool_results=[
                {
                    "tool": "get_current_time",
                    "result": {"date": "2025-10-18", "time": "14:30:00"}
                },
                {
                    "tool": "send_email",
                    "result": {"status": "sent", "message_id": "msg_12345"}
                }
            ],
            final_response="I've sent an email to john@example.com about tomorrow's meeting at 2 PM. The email has been successfully delivered."
        )
    
    def _add_sample_rag_examples(self) -> None:
        """Add sample RAG examples."""
        
        # Example 1: Technical documentation
        self.add_rag_example(
            user_query="How do I use the Python requests library to make POST requests?",
            retrieval_query="Python requests library POST method tutorial",
            retrieved_documents=[
                {
                    "id": "doc_001",
                    "title": "Python Requests Library Documentation",
                    "content": "To make a POST request using the requests library, use requests.post(url, data=data). You can pass data as a dictionary for form data, or use json=data for JSON payloads.",
                    "relevance_score": 0.95
                },
                {
                    "id": "doc_002",
                    "title": "HTTP Methods in Python",
                    "content": "The POST method is used to send data to a server. In requests, you can specify headers, authentication, and timeout parameters.",
                    "relevance_score": 0.87
                }
            ],
            assistant_response="To make POST requests using the Python requests library, you can use the `requests.post()` method. Here's how:\n\n```python\nimport requests\n\n# For form data\ndata = {'key': 'value'}\nresponse = requests.post('https://api.example.com/endpoint', data=data)\n\n# For JSON data\njson_data = {'key': 'value'}\nresponse = requests.post('https://api.example.com/endpoint', json=json_data)\n```\n\nYou can also specify additional parameters like headers, authentication, and timeout as needed."
        )
        
        # Example 2: Historical information
        self.add_rag_example(
            user_query="When was the Python programming language first released?",
            retrieval_query="Python programming language release date history",
            retrieved_documents=[
                {
                    "id": "doc_101",
                    "title": "History of Python",
                    "content": "Python was conceived in the late 1980s by Guido van Rossum. Python 0.9.0 was first released in February 1991. Python 2.0 was released in 2000, and Python 3.0 was released in 2008.",
                    "relevance_score": 0.98
                },
                {
                    "id": "doc_102",
                    "title": "Python Timeline",
                    "content": "Guido van Rossum started working on Python in December 1989. The language was named after Monty Python's Flying Circus.",
                    "relevance_score": 0.85
                }
            ],
            assistant_response="Python was first released in February 1991 as version 0.9.0. The language was conceived in the late 1980s by Guido van Rossum, who started working on it in December 1989. The language was named after the comedy group Monty Python's Flying Circus."
        )
        
        # Example 3: Code explanation with context
        self.add_rag_example(
            user_query="Explain what a context manager is in Python and give an example",
            retrieval_query="Python context manager explanation examples",
            retrieved_documents=[
                {
                    "id": "doc_201",
                    "title": "Python Context Managers",
                    "content": "A context manager is an object that defines the runtime context to be established when executing a with statement. Context managers use __enter__ and __exit__ methods. The most common use case is file handling.",
                    "relevance_score": 0.96
                },
                {
                    "id": "doc_202",
                    "title": "With Statement in Python",
                    "content": "The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks. It ensures that resources are properly released even if an error occurs.",
                    "relevance_score": 0.91
                },
                {
                    "id": "doc_203",
                    "title": "Context Manager Examples",
                    "content": "Example: with open('file.txt', 'r') as f: content = f.read(). The file is automatically closed even if an exception occurs.",
                    "relevance_score": 0.89
                }
            ],
            assistant_response="A context manager in Python is an object that defines a runtime context for executing code within a `with` statement. It uses the `__enter__` and `__exit__` methods to set up and tear down resources.\n\nThe main benefits are:\n1. Automatic resource cleanup\n2. Proper exception handling\n3. Cleaner, more readable code\n\nHere's a common example with file handling:\n\n```python\nwith open('file.txt', 'r') as f:\n    content = f.read()\n    # Use the content\n# File is automatically closed here, even if an exception occurred\n```\n\nThis ensures the file is properly closed even if an error occurs during reading."
        )
        
        # Example 4: Company/Domain specific information
        self.add_rag_example(
            user_query="What are the vacation policies for full-time employees?",
            retrieval_query="company vacation policy full-time employees",
            retrieved_documents=[
                {
                    "id": "doc_301",
                    "title": "Employee Handbook - Time Off Policy",
                    "content": "Full-time employees are entitled to 15 days of paid vacation per year after completing 1 year of service. New employees accrue vacation time at a rate of 1.25 days per month during their first year.",
                    "relevance_score": 0.99
                },
                {
                    "id": "doc_302",
                    "title": "Benefits Overview",
                    "content": "Vacation days can be carried over up to a maximum of 5 days into the next calendar year. Employees must submit vacation requests at least 2 weeks in advance.",
                    "relevance_score": 0.93
                }
            ],
            assistant_response="According to the company's vacation policy for full-time employees:\n\n1. **Vacation Entitlement**: Full-time employees receive 15 days of paid vacation per year after completing 1 year of service.\n\n2. **Accrual During First Year**: New employees accrue vacation time at a rate of 1.25 days per month during their first year.\n\n3. **Carryover**: You can carry over up to 5 vacation days into the next calendar year.\n\n4. **Request Process**: Vacation requests must be submitted at least 2 weeks in advance.\n\nPlease check with HR if you have specific questions about your individual situation."
        )
        
        # Example 5: Multi-document synthesis
        self.add_rag_example(
            user_query="Compare the performance characteristics of different Python web frameworks",
            retrieval_query="Python web frameworks performance comparison FastAPI Flask Django",
            retrieved_documents=[
                {
                    "id": "doc_401",
                    "title": "FastAPI Performance",
                    "content": "FastAPI is one of the fastest Python frameworks, built on Starlette and Pydantic. It uses async/await and can handle 20,000+ requests per second in benchmarks.",
                    "relevance_score": 0.94
                },
                {
                    "id": "doc_402",
                    "title": "Flask Performance Analysis",
                    "content": "Flask is a lightweight framework with good performance for small to medium applications. It typically handles 5,000-10,000 requests per second. It's synchronous by default but can use async extensions.",
                    "relevance_score": 0.92
                },
                {
                    "id": "doc_403",
                    "title": "Django Performance Guide",
                    "content": "Django is a full-featured framework with batteries included. Performance is typically 3,000-8,000 requests per second. It includes an ORM, admin interface, and many built-in features that add overhead but increase developer productivity.",
                    "relevance_score": 0.90
                }
            ],
            assistant_response="Here's a comparison of performance characteristics for popular Python web frameworks:\n\n**FastAPI**\n- Performance: ~20,000+ requests/second\n- Built on Starlette and Pydantic\n- Native async/await support\n- Best for: High-performance APIs, async operations\n\n**Flask**\n- Performance: ~5,000-10,000 requests/second\n- Lightweight and flexible\n- Synchronous by default, async via extensions\n- Best for: Small to medium applications, microservices\n\n**Django**\n- Performance: ~3,000-8,000 requests/second\n- Full-featured with ORM, admin, auth built-in\n- More overhead but higher developer productivity\n- Best for: Full-stack applications, rapid development\n\nThe choice depends on your specific needs: FastAPI for maximum performance, Flask for simplicity, or Django for feature-rich applications."
        )


def main():
    """Main function to demonstrate data collection."""
    print("SFT Data Collector for Tool Calling and RAG")
    print("=" * 50)
    
    # Initialize collector
    collector = SFTDataCollector(output_dir="./sft_data")
    
    # Load sample data
    print("\nLoading sample data...")
    collector.load_sample_data()
    
    # Save data
    print("\nSaving data...")
    collector.save_data()
    
    print("\n" + "=" * 50)
    print("Data collection complete!")
    print(f"Total examples collected: {len(collector.tool_calling_data) + len(collector.rag_data)}")
    print(f"  - Tool calling examples: {len(collector.tool_calling_data)}")
    print(f"  - RAG examples: {len(collector.rag_data)}")


if __name__ == "__main__":
    main()
