---
name: ai-concepts
description: Show an AI concepts cheat sheet covering LLMs, tokens, prompts, agents, subagents, skills, MCP, hooks, memory, RAG, embeddings, hallucination, and temperature. Use when the user invokes /ai-concepts, asks what an agent/skill/MCP/RAG is, asks for AI terminology to be explained, or wants a refresher on how AI tooling concepts fit together.
---

# AI Concepts Cheat Sheet

Present the cheat sheet below to the user. If they asked about one specific concept, show that section plus the "How it stacks together" diagram; otherwise show the whole thing.

## 1. LLM (Large Language Model)
Core engine. Neural network trained on huge text data. Predicts the next token. Everything else (chat, agents, coding) is built on top of this prediction ability. Examples: Claude, GPT, Gemini, Llama.

## 2. Tokens
LLMs don't read words — they read **tokens** (word chunks). "explanation" ≈ 2-3 tokens. Why it matters:
- You pay per token (input + output)
- Models have a **context window** = max tokens they can hold at once (e.g. 200K tokens ≈ a few books)
- Long conversation fills the window → older parts get summarized or dropped

## 3. Prompt & System Prompt
- **Prompt** = what you send to the model
- **System prompt** = hidden instructions that shape behavior before your message ("You are a helpful coding assistant...")
- **Prompt engineering** = writing prompts that get better output. Key tricks: be specific, give examples, define output format.

## 4. Inference vs Training
- **Training** = building the model (done once, costs millions, needs GPU farms)
- **Fine-tuning** = extra training on specific data to specialize a model
- **Inference** = using the model (what happens every time you chat)

You never train. You do inference.

## 5. Tools / Function Calling
Plain LLM only outputs text. **Tool use** = model can request actions: "run this bash command", "read this file", "search web". The harness executes the tool, feeds the result back, model continues. This is the bridge from "chatbot" to "does actual work".

## 6. Agent
**Agent = LLM + tools + a loop.**

Loop: model thinks → picks tool → gets result → thinks again → repeats until task done. A chatbot answers once; an agent keeps acting until the goal is reached.

Claude Code itself is an agent: it reads files, edits code, runs tests, checks output, retries on failure — all in a loop.

## 7. Subagents (Multi-Agent)
Main agent spawns child agents for subtasks. Why:
- **Parallelism** — three subagents search three parts of a codebase at once
- **Context isolation** — subagent burns its own context window, returns only a summary to the parent
- **Specialization** — a "security reviewer" subagent with narrow instructions outperforms a generalist for that job

## 8. Skills
**Skill = packaged instructions + optional scripts** the agent loads on demand. A playbook: "when doing X, follow these steps."

- Lives as a markdown file (SKILL.md) with a description
- Agent (or you, via `/skill-name`) invokes it → its instructions enter context → agent follows them
- Skill vs subagent: a skill is *knowledge/procedure* loaded into the current agent; a subagent is a *separate worker* with its own context

## 9. MCP (Model Context Protocol)
Open standard for connecting agents to external systems. An **MCP server** exposes tools (query database, control browser, read Figma) in a standard format any agent can consume. Like USB for AI tools.

## 10. Hooks
Scripts that run automatically at events (session start, before tool call, after prompt). Deterministic — the harness runs them, not the model. Use hooks when you need *guaranteed* behavior; instructions to the model are only *probable* behavior.

## 11. Memory & Context Management
- **Context window** = short-term memory, wiped each session
- **CLAUDE.md** = project instructions auto-loaded each session
- **Persistent memory files** = facts the agent saves across sessions
- **Compaction** = when context fills, old conversation gets summarized to make room

## 12. RAG (Retrieval-Augmented Generation)
Model can't know your private data or anything after its training cutoff. RAG = search relevant documents first, stuff them into the prompt, then answer. How "chat with your docs" products work. Agentic variant: agent greps/reads files itself instead of using a vector database.

## 13. Embeddings
Text → vector of numbers capturing meaning. Similar meanings = nearby vectors. Powers semantic search behind RAG ("find docs about auth" matches "login security" even without shared words).

## 14. Hallucination
Model states false things confidently. It predicts plausible text, not verified truth. Mitigations: RAG (ground in real docs), tool use (run the code instead of guessing), asking for citations, verification loops (agent tests its own work).

## 15. Temperature & Sampling
Controls randomness. Low (0) = deterministic, same answer every time — good for code. High (1) = creative, varied — good for brainstorming.

---

## How it stacks together

```
LLM (predicts tokens)
 └─ + system prompt        → assistant with personality/rules
     └─ + tools            → can act on the world
         └─ + loop         → AGENT
             ├─ + skills   → loaded procedures ("how to do X")
             ├─ + subagents→ parallel/specialized workers
             ├─ + MCP      → standard plug for external tools
             ├─ + hooks    → guaranteed automation at events
             └─ + memory   → persists across sessions
```

**One-line versions:**
- **Agent** = model in a loop with tools
- **Skill** = instructions the agent loads when a task matches
- **Subagent** = separate agent spawned for a subtask
- **MCP** = standard connector to external tools
- **Hook** = script that fires automatically on events
- **RAG** = fetch relevant data, then answer
