# Playbook Docs — Index

The full guide set, grouped by where you are in the journey. New here? Read [agentic-sdlc.md](./agentic-sdlc.md) then [agentic-workflows.md](./agentic-workflows.md) first; everything else builds on those two.

## Foundations
- [The Agentic SDLC](./agentic-sdlc.md) — the lifecycle stage-by-stage, roles, human checkpoints, the 6+ stage threshold.
- [Agentic Workflows](./agentic-workflows.md) — workflows vs. agents, cognitive patterns, the five orchestration workflows, when *not* to build an agent.
- [Glossary](./glossary.md) · [FAQ](./faq.md)

## Design — the patterns
- [Pattern Catalog](./patterns/) — the five orchestration workflows with code sketches.
- [Cognitive Patterns](./patterns/cognitive-patterns.md) — reflection, tool use, planning, ReAct.
- [Diagrams](./diagrams.md) — Mermaid visuals for the loop and each workflow.

## Build — worked examples
- [release-notes agent](../examples/release-notes-agent/) — prompt chaining + evaluator-optimizer (runnable, tested).
- [ticket-triage agent](../examples/ticket-triage-agent/) — routing + parallelization (runnable, tested).

## Operate — running agents well
- [Governance & Metrics](./governance-and-metrics.md) — guardrails, observability, HITL, value metrics.
- [Securing Agentic Systems](./security.md) — prompt injection, least privilege, sandboxing, tool-use governance.
- [Evaluating Agents](./evaluating-agents.md) — trajectory vs. final-answer evals, LLM-as-judge limits, regression testing.
- [Cost & Performance](./cost-and-performance.md) — caching, routing, batching, latency.
- [Context & Memory](./context-and-memory.md) — context rot, compaction, governance decay, just-in-time retrieval.

## Advanced & applied
- [Interoperability Protocols: MCP & A2A](./protocols-mcp-a2a.md) — the two-layer connectivity/coordination stack.
- [Adoption Roadmap](./adoption-roadmap.md) — a 30/60/90-day rollout plan.
- [Anti-Patterns](./anti-patterns.md) — the 10 recurring failure modes.
- [Case Studies](./case-studies.md) — real + reference-architecture examples mapped to the patterns.
- [Tooling Landscape](./tooling-landscape.md) — frameworks vs. products, with selection criteria.

## Reference
- [References](./references.md) — every source cited across the playbook.
- [Further Reading](./further-reading.md) — a curated path beyond it.

---
_Back to the [repo README](../README.md)._
