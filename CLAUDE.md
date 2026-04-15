# CLAUDE.md — Project Context for Claude Code

## Who I Am
- **Name:** Dario Melconian
- **Current Role:** Data Scientist at BMO (Bank of Montreal), Wealth Management division
- **Background:** Data science + finance domain expertise
- **Goal:** Build a portfolio of AI agent projects to support job search in:
  - Data Science / AI Engineering roles
  - Consulting (McKinsey QuantumBlack, BCG Gamma, Deloitte AI, etc.)
  - Target industries: Tech, Sports Analytics, Consulting, Finance/Fintech

---

## Project Structure

```
agents-course/
├── .env                    ← API keys (OpenAI, Anthropic, Groq) — never commit this
├── agents/                 ← Instructor's repo (ed-donner/agents) — READ ONLY reference
└── my-projects/            ← THIS REPO — Dario's own variations and portfolio work
    ├── CLAUDE.md           ← This file
    ├── README.md
    ├── week1/
    │   └── lab2_refinement_variation.ipynb
    ├── week2/
    ├── week3/
    ├── week4/
    ├── week5/
    └── week6/
```

---

## Course Structure (6 Weeks)
This is the "AI Agents" course by Ed Donner. Each week builds on a different agentic framework:

| Week | Topic | Key Project |
|------|-------|-------------|
| 1 | Foundations — agentic workflows, LLM orchestration | Personal career agent |
| 2 | OpenAI Agents SDK | SDR Agent, Deep Research app |
| 3 | CrewAI | Stock Picker, Engineering Team |
| 4 | LangGraph | Sidekick assistant |
| 5 | AutoGen | Agent Creator |
| 6 | MCP | AI Equity Traders |

---

## Current Project: Week 1 — Lab 2 Variation

**File:** `week1/lab2_refinement_variation.ipynb`

### What it does
A multi-model arena with an iterative refinement loop — an extension of the instructor's parallelization + evaluation pattern.

### Agentic Patterns Demonstrated
1. **Parallelization** — same question sent to all competitor models simultaneously
2. **LLM-as-Judge** — Claude evaluates and ranks responses
3. **Iterative Refinement / Reflection** *(new pattern added by Dario)* — competitors receive Claude's written critique and revise their answers; Claude then re-evaluates

### Model Lineup
| Role | Model | Provider |
|------|-------|----------|
| 🏆 Judge | `claude-sonnet-4-5` | Anthropic |
| Competitor 1 | `gpt-4o-mini` | OpenAI |
| Competitor 2 | `llama3.2` | Ollama (local, free) |
| Competitor 3 | `llama-3.3-70b-versatile` | Groq (free tier) |

### Domain Angle
The question generator is prompted to produce **wealth management / financial reasoning** questions — connecting to Dario's professional background at BMO.

### API Clients
```python
# OpenAI
openai_client = OpenAI()

# Anthropic (judge)
claude_client = Anthropic()

# Groq (OpenAI-compatible)
groq_client = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")

# Ollama (local, OpenAI-compatible)
ollama_client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")
```

### Required `.env` variables
```
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
GROQ_API_KEY=gsk_...
```

---

## How to Help Me (Instructions for Claude Code)

### General principles
- I am comfortable with Python and data science fundamentals
- I am learning agentic AI patterns — explain WHY design decisions are made, not just what
- Always keep the **finance/wealth management domain angle** in mind for variations — it differentiates my portfolio
- Write clean, well-commented code suitable for a public GitHub portfolio
- When I finish a project variation, help me write a strong `README.md` for that folder

### Code style preferences
- Use f-strings, not `.format()`
- Add emoji indicators to print statements (✅ ⏳ 🏆 📝) for readability in notebooks
- Structure notebooks with clear markdown headers for each step
- Include a summary table of agentic patterns used at the end of every notebook

### Git workflow
- Commit messages should be descriptive: `"Add iterative refinement loop to lab2 variation"`
- Each week's work goes in its own folder: `week1/`, `week2/`, etc.
- Never commit `.env` — remind me if I accidentally stage it
- Help me write good commit messages that will read well on GitHub

### Portfolio README guidance
When helping write READMEs for individual projects, always include:
1. What the project does (1-2 sentences)
2. Agentic patterns demonstrated (as a table)
3. Tech stack
4. How to run it
5. A "Commercial Relevance" section connecting it to real-world finance/consulting use cases

---

## Planned Portfolio Variations (by week)

| Week | Instructor Project | My Variation |
|------|--------------------|--------------|
| 1 | Multi-model evaluation | Multi-model arena + iterative refinement (wealth mgmt domain) ✅ |
| 2 | SDR Agent | Prospect research agent for wealth management client acquisition |
| 3 | Stock Picker (CrewAI) | Portfolio rebalancing crew for HNW client profiles |
| 4 | Sidekick (LangGraph) | Financial research assistant with memory |
| 5 | Agent Creator (AutoGen) | Multi-agent earnings call analysis system |
| 6 | AI Equity Traders (MCP) | Extend with risk management + compliance guardrails |

---

## Context for This Conversation
This CLAUDE.md was created during a Claude.ai chat session (claude.ai) that has full course context. For higher-level architecture decisions, portfolio strategy, or course guidance, Dario may reference that thread. Claude Code should focus on in-editor implementation help.
