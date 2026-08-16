# Context & Memory Engineering

> For long-horizon agents, **context engineering supersedes prompt engineering** — it owns the full token lifecycle, from the first system-prompt token to the last compacted summary, not just how instructions are worded. Getting this wrong is a top cause of agents that start strong and quietly degrade. This complements [agentic workflows](./agentic-workflows.md) and [cost & performance](./cost-and-performance.md).

## Context rot: more context is not better

Research ("Context Rot") shows model performance **degrades as input token count grows** — across every major model, even on controlled tasks. It's insidious because **the model emits no error**; it just silently attends less accurately to the signal buried under the noise.

**Implication:** stuffing everything into the window hurts. Curate what's in context; treat token budget as an attention budget, not just a cost line.

## Two kinds of memory

| Memory | What it holds | Lifetime |
|--------|---------------|----------|
| **Short-term** | The running conversation: turns, tool calls, tool results | This session |
| **Long-term** | User preferences, project conventions, summaries of past work | Across sessions |

Production systems maintain both, plus a **compaction** step that condenses older turns into a summary once the window starts to fill.

## Compaction: necessary, and quietly dangerous

Compaction keeps long sessions alive, and it works: Anthropic's evals report **context editing alone ≈ +29%**, and **+ a memory tool ≈ +39%**. Practical systems auto-compact near the window limit (Claude Code fires around **~98%** of the effective window).

But there's a trap the research names **governance decay**: compaction can **silently erase safety constraints** — the summary drops the guardrail that was stated 200 turns ago. Mitigations:

- **Pin invariants.** Keep security/governance constraints in a protected region that compaction never summarizes away.
- **Re-assert critical rules** after each compaction rather than trusting they survived.
- Treat a post-compaction agent as a **fresh context** for [review](./anti-patterns.md#5-self-review-blindness) purposes.

## Just-in-time retrieval over pre-loading

Rather than pre-loading everything, pull content into context **only when needed**, using lightweight identifiers — file paths, query strings, IDs — and fetch the underlying content on demand. This keeps the window small (fighting context rot) and cost down (fewer input tokens), and mirrors the [tool use](./patterns/cognitive-patterns.md#tool-use) pattern: the agent holds *references*, tools resolve them.

This also aligns with a [security rule](./security.md): the agent holds references, not secrets or raw sensitive blobs.

## A context/memory checklist

- [ ] The window is **curated**, not maximized — you fight context rot deliberately.
- [ ] Short-term and long-term memory are distinct, with an explicit compaction step.
- [ ] Safety/governance invariants are **pinned** and re-asserted after compaction (guard against governance decay).
- [ ] Retrieval is **just-in-time** via identifiers, not bulk pre-loading.
- [ ] The agent holds references, not secrets, in context.
- [ ] Compaction events are recorded in the [observability trace](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see) — so a post-compaction regression is debuggable.

## Why this ties the playbook together

Context rot and governance decay are *why* the playbook keeps insisting on observability, evidence-over-assertion, and separate-context review: a long-running agent's quality can erode **without any error being thrown.** Engineering context is how you keep a multi-hour agent as trustworthy at turn 500 as at turn 5.

## Sources

See [references.md](./references.md#context--memory). Figures are directional; validate on your workload.
