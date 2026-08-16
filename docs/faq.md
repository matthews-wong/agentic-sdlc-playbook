# FAQ

**Is an "agentic workflow" the same as an "agent"?**
No — and the distinction drives most design decisions. A *workflow* runs through code paths you define (deterministic, auditable). An *agent* lets the model decide its own steps (flexible, less predictable). Use the least autonomy the task needs. See [workflows vs. agents](./agentic-workflows.md#workflows-vs-agents--the-distinction-that-governs-everything).

**Do I need an agent framework to start?**
No. Many patterns are a few lines of code against a model API directly. Adopt a [framework](./tooling-landscape.md) only when state, coordination, or observability becomes the thing you're spending time on.

**We adopted a coding assistant and barely moved team throughput. Why?**
Almost always narrow adoption: coding sped up 30–40% while planning, testing, and release stayed manual, so the bottleneck just moved. The fix is instrumenting the whole flow and automating the *new* bottleneck, not adding more coding autonomy. See [anti-pattern #2](./anti-patterns.md#2-narrow-adoption--automating-only-coding).

**Where do humans stay in the loop?**
At defined gates — plan approval, merge, production promotion — i.e. anything irreversible or outward-facing. Reversible, internal actions can run autonomously. See [guardrails by blast radius](./governance-and-metrics.md#guardrails-design-for-the-blast-radius).

**How do I know if any of this is actually working?**
Measure delivery outcomes, not output volume: release frequency, lead time, defect/change-failure/rework rate, and cost per completed task. If coding output is up but team throughput isn't, read [the trap to avoid](./governance-and-metrics.md#the-trap-to-avoid).

**What's the single highest-leverage pattern to add first?**
[Reflection](./agentic-workflows.md#reflection) — ideally by a *separate* reviewer context. It catches a large share of first-draft errors for very little added complexity.

**Why did so many agent projects fail in 2024–2026?**
Most failures were *architectural, not model-quality*: reaching for autonomy where a workflow would do, no observability, no verification, unbounded loops, uniform guardrails. The whole [anti-patterns catalog](./anti-patterns.md) is about these.

**How autonomous should my agents be?**
As autonomous as the task forces you to be, and no more. Climb the [complexity ladder](./patterns/) from prompt chaining upward, adding autonomy only when a measured need appears — each added layer should remove a specific, observed failure.

**Can I see a real, runnable example?**
Yes — [`examples/release-notes-agent/`](../examples/release-notes-agent/) composes three patterns in ~100 lines and runs with no API key.
