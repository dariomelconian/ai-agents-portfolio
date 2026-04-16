# AI Agents Portfolio

**By: Dario Melconian** — Data Scientist, BMO Wealth Management

A portfolio of AI agent projects built across 6 weeks of learnings on agentic AI frameworks. Each project demonstrates a distinct agentic design pattern and is grounded in **wealth management / finance domain** scenarios — connecting practical AI engineering to real-world financial use cases.

---

## Portfolio Overview

| Week | Framework | Project | Patterns |
|------|-----------|---------|----------|
| 1 | Anthropic + OpenAI APIs | [Multi-Model Arena with Iterative Refinement](week1/) | Parallelization, LLM-as-Judge, Iterative Refinement |
| 2 | OpenAI Agents SDK | Prospect Research Agent *(coming soon)* | Tool use, Handoffs |
| 3 | CrewAI | Portfolio Rebalancing Crew *(coming soon)* | Multi-agent crews, Role-based agents |
| 4 | LangGraph | Financial Research Assistant *(coming soon)* | Stateful graphs, Memory |
| 5 | AutoGen | Earnings Call Analysis System *(coming soon)* | Agent creation, Group chat |
| 6 | MCP | AI Equity Traders + Risk Guardrails *(coming soon)* | Model Context Protocol |

---

## Week 1 — Multi-Model Arena with Iterative Refinement

**File:** [`week1/multi-model_iterative_refine.ipynb`](week1/multi-model_iterative_refine.ipynb)

A multi-model evaluation arena that extends the standard parallelization + LLM-as-Judge pattern with an **iterative refinement loop**. Three competitor LLMs answer a wealth management question, Claude evaluates and critiques them, the competitors revise based on feedback, and Claude delivers a final verdict.

### Agentic Patterns

| Pattern | Description |
|---------|-------------|
| **Parallelization** | Same question sent to all competitor models simultaneously |
| **LLM-as-Judge** | Claude evaluates and ranks responses with structured JSON output |
| **Iterative Refinement / Reflection** | Competitors receive written critique and revise before final judgment |

### Model Lineup

| Role | Model | Provider |
|------|-------|----------|
| Judge | `claude-sonnet-4-5` | Anthropic |
| Competitor 1 | `gpt-4o-mini` | OpenAI |
| Competitor 2 | `llama3.2` | Ollama (local) |
| Competitor 3 | `llama-3.3-70b-versatile` | Groq (free tier) |

### Tech Stack
- Python, Jupyter Notebook
- `anthropic`, `openai`, `python-dotenv`
- Ollama (local inference), Groq (free API)

### How to Run
1. Clone this repo
2. Copy `.env.example` to `.env` and add your API keys:
   ```
   OPENAI_API_KEY=sk-proj-...
   ANTHROPIC_API_KEY=sk-ant-...
   GROQ_API_KEY=gsk_...
   ```
3. Install dependencies: `pip install anthropic openai python-dotenv`
4. (Optional) Install Ollama and pull `llama3.2` for the local competitor
5. Open and run `week1/multi-model_iterative_refine.ipynb`

### Commercial Relevance
This pattern mirrors real workflows in **wealth management research**: a junior analyst drafts a report, a senior reviewer provides structured feedback, and the analyst submits a revised version for final evaluation. Automating this review loop with LLMs can improve output quality with minimal human intervention — directly applicable in research, compliance, and client reporting workflows.

---

## Setup

### Prerequisites
- Python 3.9+
- API keys for OpenAI, Anthropic, and Groq (all have free tiers)
- (Optional) [Ollama](https://ollama.ai) for local model inference

### API Keys
Get your keys here:
- OpenAI: [platform.openai.com](https://platform.openai.com)
- Anthropic: [console.anthropic.com](https://console.anthropic.com)
- Groq (free): [console.groq.com](https://console.groq.com)

---