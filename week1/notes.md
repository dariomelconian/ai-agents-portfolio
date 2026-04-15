# Week 1 Notes — Agentic AI Foundations

---

## Day 1 — Making an Agentic Workflow

3 activities that build on each other:
- Theory
- Frameworks
- Projects

**Timeline:**

| Week | Framework |
|------|-----------|
| 1 | Foundations |
| 2 | OpenAI Agents SDK |
| 3 | CrewAI (low code, crew of agents) |
| 4 | LangGraph (full code, complex) |
| 5 | AutoGen (Microsoft, agent environment) |
| 6 | MCP (Model Context Protocol — Anthropic open source) |

**Infra setup:**
- Cursor for projects
- Cloned instructor repo in `agents-course/agents`
- My projects live in `agents-course/my-projects`
- Setup API keys via `.env`

---

## Day 2 — Agents and Agentic Patterns

> *AI Agents are programs where LLM outputs control the workflow.*

**Hallmarks of an AI Solution:**
- Multiple LLM calls
- LLMs with ability to use Tools
- Environment where different LLMs send information to each other
- A Planner to coordinate activities
- Autonomy — giving the LLM control over what happens

**Agentic Systems (2 subtypes):**
1. **Workflows** — LLMs and tools orchestrated through predefined code paths
2. **Agents** — LLMs dynamically direct their own processes and tool usage

---

### (1) Workflow Design Patterns

#### 1. Prompt Chaining
Decompose into fixed sequential sub-tasks. Output of one LLM feeds into the next.

```
[User Input]
     |
     v
[LLM 1] --> output
               |
               v
           [LLM 2] --> output
                          |
                          v
                      [LLM 3] --> Final Output
```

#### 2. Routing
Direct input to a specialized sub-task based on its type. An initial LLM decides how to route.

```
[User Input]
     |
     v
[Router LLM]
  /    |    \
 v     v     v
[LLM  [LLM  [LLM
 A]    B]    C]
(topic A) (topic B) (topic C)
```

#### 3. Parallelization
Break down tasks and run multiple subtasks concurrently.

```
              [User Input]
            /      |       \
           v       v        v
        [LLM A] [LLM B]  [LLM C]
           \       |       /
            v      v      v
            [Aggregator / Code]
                   |
                   v
             [Final Output]
```

#### 4. Orchestrator-Worker
Like Parallelization, but an LLM (not code) decides how to break down the task.

```
              [User Input]
                   |
                   v
           [Orchestrator LLM]
          (decides how to split)
            /      |       \
           v       v        v
        [Worker [Worker  [Worker
          LLM A]  LLM B]   LLM C]
           \       |       /
            v      v      v
           [Orchestrator LLM]
           (recombines results)
                   |
                   v
             [Final Output]
```

#### 5. Evaluator-Optimizer
LLM output is validated by another in a feedback loop.

```
[User Input]
     |
     v
[Generator LLM] <---------+
     |                    |
     v                    |
  [Draft Output]          | (reject + reason)
     |                    |
     v                    |
[Evaluator LLM]           |
     |                    |
  accept?                 |
  /    \                  |
 yes    no ---------------+
 |
 v
[Final Output]
```

---

### (2) Agents

- More open-ended than workflows
- Has feedback loops (info processed multiple times)
- No fixed path through design (less predictable)

```
[Human Request]
      |
      v
  [LLM Agent] <---------+
      |                 |
      v                 |
[Action on Environment] |
      |                 |
      v                 |
[Feedback from Env] ----+
      |
   (stop when done)
      |
      v
  [Final Output]
```

**Risks of Agent Frameworks:**
- Unpredictable path
- Unpredictable output
- Unpredictable costs (time = money)

**Mitigations:**
- **Monitoring** — visibility of what's happening behind the scenes
- **Guardrails** — ensure agents behave safely, consistently, and within intended boundaries

---

## Day 3 — Orchestrating LLMs

**Cast of characters:**

| Provider | Models | Notes |
|----------|--------|-------|
| OpenAI | `gpt-4o-mini`, `gpt-4o`, `o3-mini` | |
| Anthropic | `claude-3-7-sonnet`, `claude-haiku` | Haiku for cheap |
| Google | `gemini-2.0-flash` | Free at time of writing |
| DeepSeek | `deepseek-v3`, `deepseek-r1` | |
| Groq | `llama3.3` | Open-source, free API |
| Ollama | `llama3.2` | Runs locally on your machine |

**Vellum Leaderboard** — compare cost vs performance across models.

**Lab 2:** Create client instances for all model types (OpenAI through Ollama).

**Ollama notes:**
- Runs a local web service with an OpenAI-compatible endpoint
- High-performance C++ inference
- Check it's running: `http://localhost:11434`

Useful Ollama commands:
```bash
ollama pull <model_name>   # download a model
ollama ls                  # list downloaded models
ollama rm <model_name>     # delete a model
```

---

## Day 4

*(Notes coming soon)*
