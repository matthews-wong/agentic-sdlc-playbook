# Glossary

Short, opinionated definitions as this playbook uses the terms. Where a term has a dedicated section, it's linked.

- **Agent** — a system where the *model* dynamically directs its own steps and tool use, deciding what to do and when. More capable and less predictable than a workflow. See [workflows vs. agents](./agentic-workflows.md#workflows-vs-agents--the-distinction-that-governs-everything).
- **Agentic SDLC** — a software delivery practice in which AI agents do real, multi-step work across the lifecycle (plan → build → review → test → deploy → operate) between defined human checkpoints. See [agentic-sdlc.md](./agentic-sdlc.md).
- **Workflow** — LLM(s) and tools orchestrated through *predefined code paths you control*. Deterministic and auditable. The five canonical ones are in [agentic-workflows.md](./agentic-workflows.md#the-five-orchestration-workflows).
- **Reflection** — an agent critiquing its own output before finalizing. Most reliable when done by a *separate* context. See [reflection](./agentic-workflows.md#reflection).
- **Tool use** — an agent invoking external systems (files, APIs, code execution) through dynamic calls. With reflection, the most mature pattern.
- **Planning** — decomposing a goal into subgoals and refining over past actions (Plan-Act-Reflect). Powerful but the least predictable cognitive pattern.
- **ReAct** — alternating **Rea**soning and **Act**ing so each action is informed by the last observation. A strong default loop for tool-using agents.
- **Prompt chaining** — a fixed sequence of steps, optionally gated. [Pattern](./patterns/prompt-chaining.md).
- **Routing** — classify an input, then dispatch to a specialized handler. [Pattern](./patterns/routing.md).
- **Parallelization** — fan out independent subtasks (sectioning) or run the same task multiple times (voting), then aggregate. [Pattern](./patterns/parallelization.md).
- **Orchestrator-workers** — a lead agent decomposes a task *at runtime* and delegates to workers, then synthesizes. [Pattern](./patterns/orchestrator-workers.md).
- **Evaluator-optimizer** — a generate ↔ critique loop against explicit criteria; reflection made structural. [Pattern](./patterns/evaluator-optimizer.md).
- **Human checkpoint (gate)** — a point where a human must approve before the agent proceeds; reserved for irreversible or outward-facing actions. See [guardrails](./governance-and-metrics.md#guardrails-design-for-the-blast-radius).
- **Blast radius** — how much damage an action can do and how reversible it is; the basis for how tightly to gate it.
- **Observability trace** — the recorded plan, tool calls, costs, checkpoints, and evidence for an agent run. Prerequisite for governance. See [observability](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see).
- **Evidence (vs. assertion)** — proof a task actually worked (test output, a reproduced happy path), as opposed to the agent merely *claiming* it's done.
- **Stage coverage** — how many SDLC stages have meaningful agent participation; the **6+** threshold is where compounding gains appear. See [why 6+ stages](./agentic-sdlc.md#why-6-stages-is-the-threshold-that-matters).
- **Cost per completed task** — tokens + compute + human review time for one accepted unit of work; the economic metric that matters more than per-call cost.
- **Rework rate** — how often agent output is rejected or reverted at a checkpoint; an early warning that autonomy has outrun verification.
