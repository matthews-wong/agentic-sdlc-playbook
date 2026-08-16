# Playbook Docs — Index

The full guide set, grouped by where you are in the journey. New here? Read [agentic-sdlc.md](./agentic-sdlc.md) then [agentic-workflows.md](./agentic-workflows.md) first; everything else builds on those two. For a self-assessment of where your team stands, jump to the [maturity model](./maturity-model.md).

## Foundations

- [The Agentic SDLC](./agentic-sdlc.md) — the lifecycle stage-by-stage, roles, human checkpoints, the 6+ stage threshold.
- [Agentic Workflows](./agentic-workflows.md) — workflows vs. agents, cognitive patterns, the five orchestration workflows, when *not* to build an agent.
- [Glossary](./glossary.md) · [FAQ](./faq.md)

## Design — the patterns

- [Pattern Catalog](./patterns/) — the five orchestration workflows with code sketches.
- [Cognitive Patterns](./patterns/cognitive-patterns.md) — reflection, tool use, planning, ReAct.
- [Diagrams](./diagrams.md) — Mermaid visuals for the loop and each workflow.

## Build — designing & writing agents

- [Agentic Coding](./agentic-coding.md) — spec-driven development and the spec→plan→tasks→code loop.
- [Prompting & Instructions](./prompting-and-instructions.md) — system prompts as runbooks, tool descriptions, structured output.
- [RAG & Grounding](./rag-and-grounding.md) — chunking, hybrid retrieval, reranking, citations, agentic RAG.
- Worked examples ([all](../examples/)): [release-notes agent](../examples/release-notes-agent/) (chaining + evaluator-optimizer) · [ticket-triage agent](../examples/ticket-triage-agent/) (routing + parallelization) — both runnable and tested.

## Operate — running agents well

- [Governance & Metrics](./governance-and-metrics.md) — guardrails, observability, HITL, value metrics.
- [Securing Agentic Systems](./security.md) — prompt injection, least privilege, sandboxing, tool-use governance.
- [Evaluating Agents](./evaluating-agents.md) — trajectory vs. final-answer evals, LLM-as-judge limits, regression testing.
- [Observability](./observability.md) — tracing agent runs with OpenTelemetry GenAI conventions.
- [Reliability & Recovery](./reliability-and-recovery.md) — retries, idempotency, durable state, escalation.
- [Cost & Performance](./cost-and-performance.md) — caching, routing, batching, latency.
- [Context & Memory](./context-and-memory.md) — context rot, compaction, governance decay, just-in-time retrieval.

## Adopt & scale

- [Maturity Model](./maturity-model.md) — five-level self-assessment across eight dimensions.
- [Adoption Roadmap](./adoption-roadmap.md) — a 30/60/90-day rollout plan.
- [Team & Operating Model](./team-and-operating-model.md) — roles, new roles, and org patterns.
- [Compliance & Regulation](./compliance-and-regulation.md) — EU AI Act, NIST AI RMF, ISO 42001, the agentic gap.

## Learn from what works (and fails)

- [Anti-Patterns](./anti-patterns.md) — the 10 recurring failure modes.
- [Case Studies](./case-studies.md) — real + reference-architecture examples mapped to the patterns.
- [Tooling Landscape](./tooling-landscape.md) — frameworks vs. products, with selection criteria.
- [Interoperability Protocols: MCP & A2A](./protocols-mcp-a2a.md) — the two-layer connectivity/coordination stack.

## Reference

- [References](./references.md) — every source cited across the playbook.
- [Further Reading](./further-reading.md) — a curated path beyond it.

---
_Back to the [repo README](../README.md)._
