# Multi-Agent Systems

> [Orchestrator-workers](./patterns/orchestrator-workers.md) is one shape; this page is the wider map of how multiple agents can be wired together — and, more importantly, **when the extra cost is worth it.** Multi-agent is a capability multiplier and a cost multiplier at the same time.

## First: does it need to be multi-agent?

Coordination isn't free. Reported production overhead: **independent multi-agent setups ~58% extra tokens; centralized ones ~285% extra.** So multi-agent only pays off when the task genuinely benefits from **specialization, parallelism, or critique.** Otherwise a single agent or a plain [workflow](./agentic-workflows.md) wins — reaching for a fleet where one agent would do is [autonomy theater](./anti-patterns.md#1-autonomy-theater--an-agent-where-a-workflow-would-do) with a bigger bill.

## The topologies

| Topology | Shape | Use when | Production reality |
|----------|-------|----------|--------------------|
| **Sequential pipeline** | one agent, chained steps | fixed, known steps | the simplest thing; often enough |
| **Supervisor / orchestrator-worker** | a coordinator dispatches workers | tasks decided at runtime; clear delegation | **~70% of production deployments** |
| **Hierarchical** | stacked supervisors | complex workflows with bounded subproblems, team-owned stages, oversight between phases | for genuinely complex work |
| **Graph** | nodes + conditional edges | structured production workflows needing audit/rollback | a production default |
| **Blackboard** | shared knowledge space; agents read/refine | incremental, diverse-specialist problems | research-mode; rarely beats hierarchy in prod |
| **Debate** | agents critique/argue to consensus | quality via [reflection](./patterns/cognitive-patterns.md#reflection) at test time | great for accuracy-critical answers |
| **Swarm** | peer agents, no central control, emergent | exploratory tasks where decomposition isn't known up front | research/brainstorm; rarely beats hierarchy in prod |

## Choosing one (the honest guidance)

- **Default to graph or hierarchy in production.** Supervisor/orchestrator-worker or a sequential pipeline covers most real systems.
- **Hierarchy** when the work decomposes into clear, bounded subproblems or maps to teams/stages — pairs naturally with the [6+ stage SDLC](./agentic-sdlc.md).
- **Debate** when answer quality matters more than cost: one agent critiques another (a [separate-context reviewer](./patterns/evaluator-optimizer.md)) — it's parallel self-consistency.
- **Swarm and blackboard** are theoretically appealing but **rarely outperform hierarchy or graph in practice.** Reserve them for exploratory research-and-summarize work where the flow genuinely can't be pre-specified.

## Coordination mechanics

- Give each agent a narrow role, its own tools, and clear [handoff/conflict rules](./prompting-and-instructions.md#multi-agent-write-the-handoffs-explicitly) — coordination failures are usually prompt failures.
- Use [A2A](./protocols-mcp-a2a.md) for cross-agent/vendor coordination rather than a private protocol.
- Every agent should carry [reflection + tool use](./patterns/cognitive-patterns.md); the composition is where multi-agent capability actually comes from.
- Cap the whole system's loops and budget ([reliability](./reliability-and-recovery.md)) — multi-agent is where runaway cost hides.

## The cost/benefit test

Adopt multi-agent only if you can name which of these you're buying:

- **Specialization** — sub-tasks genuinely need different tools/prompts/models.
- **Parallelism** — independent sub-tasks that cut wall-clock when run at once.
- **Critique** — an independent reviewer measurably raises quality (debate).

If none clearly applies, the 58–285% overhead is buying you complexity, not capability.

## A multi-agent checklist

- [ ] You can name the specialization / parallelism / critique benefit justifying the overhead.
- [ ] Topology is graph, supervisor, or hierarchy unless the task is genuinely exploratory.
- [ ] Each agent has a narrow role, scoped tools, and written handoff/conflict rules.
- [ ] System-wide loop and token budgets are capped.
- [ ] Coordination uses a standard protocol where it crosses boundaries.

## Sources

See [references.md](./references.md#multi-agent-systems). Overhead figures and topology-share numbers are directional 2026 reporting.
