# Agentic Workflow Patterns

> The reusable building blocks that make agents reliable. A multi-agent system where each sub-agent uses reflection and tool use is **orders of magnitude** more capable than any single pattern alone — but only if you add complexity deliberately.

## Workflows vs. agents — the distinction that governs everything

- **Workflows** orchestrate LLMs and tools through **predefined code paths**. They are more deterministic and follow patterns you define in advance.
- **Agents** dynamically direct **their own** processes and tool usage, deciding what steps to take and when. More autonomy, less predictability.

Anthropic's core guidance: **find the simplest solution possible, and only increase complexity when needed.** Many of these patterns are a few lines of code against an LLM API directly — you rarely need a heavy framework to start.

## The core cognitive patterns

### Reflection
The agent critically evaluates its own output before finalizing — a self-review loop. Cheap to add, high value: a generate → critique → revise cycle catches a large share of first-draft errors. This is the single most reliable capability multiplier.

### Tool use
The agent interacts with external systems and data sources through dynamic API invocation — reading files, querying databases, calling services, running code. Alongside reflection, this is the most *mature and predictable* pattern.

### Planning
The agent decomposes a large task into subgoals and refines over past actions (Plan-Act, Plan-Act-Reflect). Powerful, but explicitly **less mature and less predictable** than reflection and tool use — treat autonomous planning as the part most likely to go sideways and gate it accordingly.

### ReAct (Reason + Act)
The agent alternates between reasoning steps and actions, interleaving "think" and "do" so each action is informed by observed results. A strong default loop for tool-using agents.

## The five orchestration workflows

From Anthropic's *Building Effective Agents* (Dec 2024). They increase in complexity — pick the least complex one that solves your problem.

| # | Pattern | Shape | Use when |
|---|---------|-------|----------|
| 1 | **Prompt chaining** | Task → step → step → step | The task decomposes into fixed sequential subtasks; you can gate between them |
| 2 | **Routing** | Classify → dispatch to a specialized handler | Inputs fall into distinct categories best handled separately |
| 3 | **Parallelization** | Fan out → run concurrently → aggregate | Subtasks are independent (sectioning) or you want multiple votes (voting) |
| 4 | **Orchestrator-workers** | A lead agent decomposes and delegates to workers | The subtasks aren't known in advance and must be decided at runtime |
| 5 | **Evaluator-optimizer** | Generator ↔ evaluator loop | You have clear evaluation criteria and iteration measurably improves the result |

### Reading the ladder
1–3 are **workflows** (you define the control flow). 4–5 start handing control-flow decisions to the model. Full **agents** sit beyond 5, where the model owns the loop. Climb only as far as the problem forces you.

## Multi-agent orchestration

Multiple specialized agents — each with its own prompt, model, tools, and code — collaborate on problems that exceed single-agent capability. The mechanism combines **role specialization** with **coordination** across agents. Compose it with the cognitive patterns: give each worker reflection and tool use, and route between them with one of the five workflows.

## When *not* to build an agent

Autonomy is a cost, not a goal. Prefer a workflow — or plain code — when:

- The steps are known and fixed → a **prompt chain** or ordinary code is cheaper and more reliable.
- The task is a single well-scoped call → just call the model.
- Errors are expensive and hard to reverse, and you can't gate them → keep a human in the loop instead of adding autonomy.
- You can't evaluate the output → without an evaluation signal, an evaluator-optimizer loop has nothing to optimize against.

The failure mode of 2024–2026 was reaching for autonomous agents where a deterministic workflow would have been more reliable, cheaper, and easier to debug. **Most production failures in that period were architectural, not model-quality, failures.**

## Combining patterns — a worked example

A code-change agent, built least-complex-first:

1. **Route** the incoming ticket by type (bug / feature / chore).
2. For a bug: **prompt-chain** reproduce → locate → fix → test.
3. Each step is a **ReAct** loop with **tool use** (read files, run tests).
4. Wrap the fix step in an **evaluator-optimizer** loop: a reviewer agent (**reflection** by a *different* agent) critiques until tests pass and criteria are met.
5. **Parallelize** independent verification checks (lint, unit, integration) and aggregate.

Every added layer earns its place by removing a specific, observed failure.

## See also

- [Pattern catalog](./patterns/) — each workflow above with a minimal, framework-agnostic code sketch and its trade-offs.
- [Agentic SDLC](./agentic-sdlc.md) — where these patterns get applied across delivery.
- [Governance & Metrics](./governance-and-metrics.md) — keeping autonomous loops safe and measurable.
- [References](./references.md) — sources.
