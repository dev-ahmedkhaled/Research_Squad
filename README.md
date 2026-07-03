# 🔍 Research Squad

> A multi-agent research pipeline built with LangGraph that autonomously searches the web via DuckDuckGo, generates a structured markdown summary using a local LLM (Ollama/Qwen), and self-evaluates until the result satisfies the original query.

---

## How It Works

Research Squad uses a 3-node LangGraph pipeline where each agent has one job:

```
User Query
    ↓
Research Agent  →  searches DuckDuckGo, improves query on retry
    ↓
Writer Agent    →  generates clean markdown summary with sources
    ↓
Critic Agent    →  judges if the draft answers the original query
    ├── approved → done, output to user
    └── rejected → loop back to Research Agent with new angle
```

No bloated frameworks. No unnecessary abstractions. Just clean state flowing through focused agents.

---

## Stack

| Component | Tool |
|---|---|
| Agent orchestration | LangGraph |
| Web search | DuckDuckGo (`langchain-community`) |
| LLM inference | Ollama (Qwen 3.5 9B, local) |
| State management | TypedDict schema |
| Output format | Markdown with sources section |

---

## Project Structure

```
research-squad/
├── StateSchema.py       # ResearchSchema TypedDict + init_state()
├── research_agent.py    # Web search + query improvement on retry
├── writer_agent.py      # Markdown summary generation
├── critic.py            # Approves or rejects the draft
├── graph.py             # LangGraph pipeline wiring
├── llm_core.py          # Shared Ollama LLM wrapper
└── main.py              # Entry point
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) running locally
- Qwen model pulled: `ollama pull qwen3.5:9b`

### Install dependencies

```bash
pip install langgraph langchain-community langchain-ollama
```

### Run

```bash
python main.py
```

Then enter your research query when prompted. The pipeline will search, write, and self-evaluate until it produces a result it's confident in.

---

## Key Design Decisions

- **One node, one job** — each agent does exactly one thing, making bugs easy to trace
- **Self-improving queries** — on retry, the research agent sees its previous (failed) results and asks the LLM to generate a better search query instead of repeating the same one
- **Local inference** — everything runs on your machine via Ollama, no API keys needed
- **Strict critic output** — critic is prompted to respond with only `"true"` or `"false"` to prevent ambiguous approval logic

---

## Built as a learning project to practice:
- LangGraph state design and conditional edges
- Multi-agent orchestration patterns
- Debugging real agent loops (not just following tutorials)

---

*Part of the path to building [Jarvis](https://github.com/dev-ahmedkhaled) — a long-term ambient AI desktop assistant.*
