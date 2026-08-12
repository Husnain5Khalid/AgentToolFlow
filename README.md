# ToolPilot 🤖

**A lightweight Agentic AI system that uses an LLM to intelligently select and execute tools based on a user's query.**

ToolPilot is a learning-focused but professionally structured implementation of a **tool-using AI agent** built with Python and Groq.

The project demonstrates the fundamental architecture behind modern Agentic AI systems:

```text
User
  ↓
Query
  ↓
Agent (Groq LLM)
  ↓
Tool Selection
  ↓
Tool Executor
  ↓
Tool
  ↓
Tool Result
  ↓
Agent
  ↓
Final Answer
  ↓
User
```

---

## 🎯 Project Goal

The goal of ToolPilot is to understand how an AI Agent works **under the hood**, without hiding the architecture behind frameworks such as LangChain or LangGraph.

The project focuses on understanding:

* LLM-based decision making
* Tool calling
* Tool schemas
* Tool execution
* Tool registries
* Agent orchestration
* Passing tool results back to the LLM
* Agent → Tool → Agent workflows
* Clean separation between Agent and Tools

---

## 🧠 How It Works

When a user sends a query, the Agent receives the query and the available tool definitions.

The LLM decides whether a tool is required.

For example:

```text
User:
"What is 25 × 40?"
```

The Agent can decide:

```text
Tool: calculate
Arguments:
{
    "expression": "25 * 40"
}
```

The Tool Executor then finds the corresponding Python function and executes it.

```text
Agent
  ↓
"calculate"
  ↓
Tool Executor
  ↓
calculate("25 * 40")
  ↓
1000
```

The result is then returned to the Agent, which generates the final response:

```text
25 × 40 = 1000.
```

---

## 🏗️ Architecture

```text
                         ┌──────────────┐
                         │     User     │
                         └──────┬───────┘
                                │
                              Query
                                │
                                ▼
                         ┌──────────────┐
                         │    Agent     │
                         │   Groq LLM   │
                         └──────┬───────┘
                                │
                         Tool Decision
                                │
                ┌───────────────┼───────────────┐
                │               │               │
                ▼               ▼               ▼
          ┌──────────┐   ┌────────────┐   ┌──────────┐
          │ Weather  │   │ Calculator │   │ Web      │
          │   Tool   │   │    Tool    │   │ Search   │
          └────┬─────┘   └─────┬──────┘   └────┬─────┘
               │               │               │
               └───────────────┼───────────────┘
                               │
                          Tool Result
                               │
                               ▼
                         ┌──────────────┐
                         │    Agent     │
                         │   Groq LLM   │
                         └──────┬───────┘
                                │
                           Final Answer
                                │
                                ▼
                              User
```

---

## 📁 Project Structure

```text
toolpilot-agent/
│
├── app/
│   ├── __init__.py
│   │
│   ├── agent/
│   │   ├── __init__.py
│   │   └── agent.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── weather.py
│   │   ├── calculator.py
│   │   ├── web_search.py
│   │   └── registry.py
│   │
│   ├── executor/
│   │   ├── __init__.py
│   │   └── executor.py
│   │
│   └── config/
│       ├── __init__.py
│       └── settings.py
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Responsibilities

| Component       | Responsibility                               |
| --------------- | -------------------------------------------- |
| `main.py`       | Application entry point and user interaction |
| `agent.py`      | Agent logic and communication with Groq      |
| `weather.py`    | Weather tool                                 |
| `calculator.py` | Calculator tool                              |
| `web_search.py` | Web-search tool                              |
| `registry.py`   | Maps tool names to Python functions          |
| `executor.py`   | Executes tools requested by the Agent        |
| `settings.py`   | Application configuration                    |
| `.env`          | API keys and environment configuration       |

---

## 🔧 Current Tools

### 1. Weather Tool

```python
get_weather(city)
```

Returns weather information for a specified city.

> Currently implemented as a mock tool for demonstration.

---

### 2. Calculator Tool

```python
calculate(expression)
```

Evaluates a mathematical expression.

Example:

```text
20 / 100 * 50000
```

Result:

```text
10000
```

> The current educational implementation uses `eval()`. A production system should replace this with a safe expression evaluator.

---

### 3. Web Search Tool

```python
search_web(query)
```

Searches for information based on a query.

> Currently implemented as a mock tool. A real search provider can be integrated later.

---

## 🔄 Agent Tool-Calling Flow

A typical interaction looks like this:

```text
User
 │
 │ "What is 20% of 50,000?"
 ▼
Agent
 │
 │ decides calculator is required
 ▼
Tool Executor
 │
 ▼
Calculator
 │
 │ 10000
 ▼
Tool Result
 │
 ▼
Agent
 │
 │ generates final response
 ▼
User
```

For multiple capabilities:

```text
User
 │
 ▼
Agent
 │
 ├── get_weather()
 │
 └── calculate()
       │
       ▼
   Tool Results
       │
       ▼
     Agent
       │
       ▼
  Final Answer
```

---

## 🛠️ Tech Stack

* **Python**
* **Groq API**
* **LLM Tool Calling**
* **python-dotenv**
* Native Python architecture

No agent framework is required for the core implementation.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>

cd toolpilot-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

Never commit `.env` to Git.

### 5. Run the application

```bash
python main.py
```

---

## 💬 Example Queries

Try queries such as:

```text
What is 25 * 40?
```

```text
What is the weather in Riyadh?
```

```text
What is the weather in Riyadh and what is 20% of 50000?
```

The Agent determines which tool or tools are appropriate for the query.

---

## 🧩 Key Concepts Learned

This project demonstrates the fundamental components of Agentic AI:

### LLM

The LLM acts as the Agent's decision-making component.

### Tool

A tool gives the Agent an external capability.

```text
Agent → Tool
```

### Tool Schema

The schema tells the LLM:

* What the tool is called
* What the tool does
* Which arguments it accepts
* What type those arguments should have

### Tool Registry

The registry connects a tool name selected by the LLM to its actual Python implementation.

```text
"calculate"
     ↓
TOOL_REGISTRY
     ↓
calculate()
```

### Tool Executor

The executor receives the Agent's tool call and executes the corresponding function.

### Agent Loop

The fundamental Agent pattern is:

```text
Observe
   ↓
Decide
   ↓
Act
   ↓
Observe Result
   ↓
Decide Again
   ↓
...
   ↓
Final Answer
```

---

## 🔮 Future Improvements

ToolPilot can be extended into a much more capable Agentic AI platform.

### Phase 1 — Production Tools

* Replace mock weather with a real weather API
* Replace mock search with a real search provider
* Replace `eval()` with a safe calculator
* Add proper error handling
* Add structured logging

### Phase 2 — Agent Loop

Support repeated tool calls:

```text
Agent
 ↓
Tool 1
 ↓
Agent
 ↓
Tool 2
 ↓
Agent
 ↓
Tool 3
 ↓
Agent
 ↓
Final Answer
```

### Phase 3 — Memory

Add:

* Conversation history
* Short-term memory
* Long-term memory
* Persistent storage

### Phase 4 — RAG

Add:

* Document ingestion
* Embeddings
* Vector database
* Retrieval
* Context-aware responses

### Phase 5 — MCP

Introduce **Model Context Protocol (MCP)** so tools can be exposed through a standardized protocol.

The architecture could then evolve toward:

```text
User
 ↓
Agent
 ↓
MCP Client
 ↓
MCP Server
 ├── Weather
 ├── Calculator
 ├── Search
 └── Other Tools
```

### Phase 6 — Multi-Agent Systems

Eventually, ToolPilot could evolve into:

```text
                    Supervisor Agent
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
         Researcher     Coder      Analyst
              │           │           │
              └───────────┼───────────┘
                          ▼
                     Final Answer
```

---

## 🔐 Security Considerations

For a production implementation, several areas require additional security work:

* Never expose API keys
* Validate tool arguments
* Avoid arbitrary `eval()`
* Restrict tool permissions
* Validate external API responses
* Add authentication where required
* Implement rate limiting
* Add logging and monitoring
* Add human approval for sensitive actions
* Prevent prompt injection from untrusted tool data

---

## 📚 What This Project Teaches

ToolPilot intentionally avoids hiding the important concepts behind a framework.

By studying this project, you should understand the relationship between:

```text
LLM
 ↓
Agent
 ↓
Tool Selection
 ↓
Tool Calling
 ↓
Tool Execution
 ↓
Tool Result
 ↓
LLM
 ↓
Final Response
```

Once this architecture is understood, frameworks and protocols such as **LangGraph, LangChain, and MCP** become much easier to learn because you already understand the underlying mechanism.

---

## 📄 License


MIT License
```

---

## ⭐ Project Summary

**ToolPilot** is a minimal Agentic AI implementation designed to demonstrate how an LLM can intelligently select and use external tools to accomplish user requests.

The central idea is simple:

> **The Agent decides. The Executor executes. The Tools provide capabilities.**

## Author:
Husnain Khalid
