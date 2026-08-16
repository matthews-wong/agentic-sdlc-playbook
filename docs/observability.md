# Observability

> [Governance](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see) says *you cannot govern what you cannot see* and calls for an observability trace. This page is the technical **how**: how to instrument agents with a vendor-neutral standard so a run is traceable, costable, and debuggable.

## The standard: OpenTelemetry GenAI semantic conventions

OpenTelemetry captures **traces, metrics, and logs** for model calls in a **vendor-neutral** format — inference calls, token usage, latency, cost, and agent/tool interactions. The **GenAI semantic conventions** (from OTel's GenAI SIG, active since April 2024) unify attribute names and values for LLM calls, agent steps, vector-DB queries, token usage, cost, and quality metrics.

> **Maturity caveat:** as of early 2026 most GenAI conventions are **experimental** — attribute names can still change. Adopt them, but pin versions and expect churn.

Vendor support is already broad: Datadog added native support (OTel v1.37), Grafana/Loki collect LLM traces, and Google Cloud / AWS / Azure and others adopt the convention — the payoff of a standard is you aren't locked to one backend.

## The trace model: spans mirror the reasoning chain

Instrument an agent so **each step becomes a child span**:

```
span: agent.run (goal, session id)
├─ span: llm.call         (model, input/output tokens, cost, latency)
├─ span: tool.call        (tool name, args, result status)
├─ span: retrieval.query  (query, docs returned)
├─ span: llm.call         (…)
└─ span: compaction       (tokens before/after)   ← see context-and-memory.md
```

The result is a **full trace of the reasoning chain** — the concrete form of the governance "trace of plan, tool calls, cost, checkpoints." The GenAI SIG is extending conventions to **multi-agent** systems too: tasks, actions, agent teams, memory, and artifact tracking.

## Token-based cost attribution

Latency and cost correlate with **token counts, not request counts** — which is why token tracking is a first-class part of the conventions. Emit input/output tokens per span so your dashboards compute [cost per completed task](./cost-and-performance.md), attribute spend to features, and catch a prompt that quietly ballooned.

## The three signals, applied to agents

| Signal | For an agent |
|--------|--------------|
| **Traces** | The step-by-step reasoning/tool chain of one run (debugging, audit) |
| **Metrics** | Aggregates: tokens, cost, latency, error/retry rates, checkpoint outcomes |
| **Logs** | Structured events (tool errors, escalations) correlated to a trace/span id |

## What OTel covers — and where it stops

Crucial boundary: the GenAI conventions standardize **model attributes, token usage, and latency**. They do **not** cover **output evaluation, safety scoring, or content-quality assessment.** So:

- Use **OTel** for the *operational* picture (what happened, how much it cost, what failed) — see this page and [reliability](./reliability-and-recovery.md).
- Use [**evaluation**](./evaluating-agents.md) for the *quality* picture (was the output correct/safe). They're complementary layers; don't expect tracing to tell you the agent was *right*.

## An observability checklist

- [ ] Every agent run is a trace; every LLM/tool/retrieval step is a span.
- [ ] Spans carry token counts (in/out), cost, latency, and status.
- [ ] Instrumentation uses OTel GenAI conventions (versions pinned; churn expected).
- [ ] Logs are correlated to trace/span ids, not free-floating.
- [ ] Compaction and escalation events are recorded (debug post-hoc regressions).
- [ ] Quality is measured via [evals](./evaluating-agents.md), not inferred from traces.

## Sources

See [references.md](./references.md#observability). Convention status is early-2026 and evolving.
