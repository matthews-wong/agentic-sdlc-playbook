# Tooling Landscape

> A map of the tools you'd reach for when building agentic workflows or adopting agents into the SDLC — with selection criteria. This is a decision aid, not an endorsement. Prices, versions, and star counts move fast; **treat every specific here as "verify before you commit."**

## First principle: you may not need a framework

Anthropic's guidance bears repeating before any tool choice: **many agentic patterns are a few lines of code against a model API directly.** A framework earns its place when it removes real, recurring pain — state persistence, retries, multi-agent coordination, observability — not because "everyone uses one." Start with direct API calls and the [patterns](./patterns/); reach for a framework when the [orchestration](./patterns/orchestrator-workers.md) or state management becomes the thing you're spending time on.

## Two layers, don't conflate them

| Layer | What it is | Examples |
|-------|-----------|----------|
| **Agent-building frameworks** | Libraries you use to *build* agentic workflows | Claude Agent SDK, LangGraph, CrewAI, OpenAI Agents SDK, AG2, Strands |
| **SDLC agent products** | Ready-made agents that *do SDLC work* | GitHub Copilot coding agent, IDE agent modes, code-review agents |

You adopt a product to get value fast; you use a framework to build something a product doesn't cover.

## Agent-building frameworks (2026 snapshot)

The landscape consolidated in 2026 around a handful of options, each backed by a frontier lab, hyperscaler, or strong OSS community. Directional characteristics from the sources below:

| Framework | Orchestration model | Strength | Watch-out |
|-----------|--------------------|----------|-----------|
| **Claude Agent SDK** (Anthropic) | Model reasons about tools, chains them, spawns isolated subagents | Robust error handling; safety-first reliability; parallel subagents | Anthropic-model centric |
| **LangGraph** (LangChain) | Directed graph with conditional edges; built-in checkpointing + time-travel | Maps cleanly to production needs (audit trails, rollback); the "safest default" when you need explicit control | Steeper learning curve |
| **CrewAI** | Role-based "crews" with process types | Lowest learning curve; ~20 lines to a working multi-agent prototype | Reported up to ~3× token overhead vs. LangGraph on simple flows |
| **OpenAI Agents SDK** | Production-grade evolution of Swarm; sandbox execution + harness | Solid sandboxed execution | OpenAI-models only |
| **AG2** | Event-driven, async message passing | Community successor to AutoGen; strong when agents write & run code | Newer/community-driven; churn |
| **Strands** (AWS) | AWS-native agent framework | Fits AWS-centric stacks | Ecosystem lock-in |

*(AutoGen itself moved to maintenance mode; AG2 is the community continuation.)*

### Mapping frameworks to the patterns
- Need **explicit, auditable control flow** ([prompt chaining](./patterns/prompt-chaining.md), rollback)? → graph-based (LangGraph).
- Need a **fast multi-agent prototype** ([orchestrator-workers](./patterns/orchestrator-workers.md))? → role-based (CrewAI).
- Agents that **write and execute code**? → sandboxed execution (OpenAI Agents SDK, AG2).
- **Reliability/safety and isolated subagents** as first concerns? → Claude Agent SDK.

## SDLC agent products

- **GitHub Copilot coding agent** — issue → Actions sandbox → PR → human review. See the [case study](./case-studies.md#1-github-copilot-coding-agent--the-issue-to-pr-async-worker).
- **IDE agent modes** (VS Code, JetBrains) — multi-step edits, run commands, iterate on errors in-editor.
- **Code-review agents** — first-pass review on the diff before a human looks.

The through-line: the best products **slot into delivery primitives your team already reviews** (issues, PRs, CI) rather than inventing a new control surface.

## Selection criteria (score candidates on these)

1. **Least-complexity fit** — does it solve *your* problem, or add ceremony? Would direct API calls do?
2. **Control vs. autonomy** — explicit graphs (predictable, auditable) vs. dynamic agent loops (flexible, less predictable). Pick the least autonomy the task needs.
3. **Observability** — can you get a full trace (plan, tool calls, cost) out of the box? If not, you'll build it — count that cost. See [governance & metrics](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see).
4. **State & recovery** — checkpointing, retries, resumability for long/async runs.
5. **Model portability** — locked to one provider's models, or bring-your-own?
6. **Token economy** — overhead per step compounds at scale; measure cost-per-completed-task, not per-call.
7. **Human-in-the-loop hooks** — first-class approval gates at irreversible steps, or bolted on?
8. **Ecosystem fit** — does it live where your code, CI, and cloud already are?

## References

See [references.md](./references.md#tooling-landscape). Framework comparisons drawn from 2026 surveys by [QubitTool](https://qubittool.com/blog/ai-agent-framework-comparison-2026), [Alice Labs](https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026), [Uvik](https://uvik.net/blog/agentic-ai-frameworks/), and [Medium/ATNO](https://medium.com/@atnoforgenai/10-ai-agent-frameworks-you-should-know-in-2026-langgraph-crewai-autogen-more-2e0be4055556). For canonical Claude Agent SDK / Claude API usage, prefer Anthropic's own docs.
