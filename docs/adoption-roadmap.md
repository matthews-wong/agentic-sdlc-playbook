# Adoption Roadmap (30 / 60 / 90 days)

> A pragmatic sequence for introducing agents into a real team's SDLC. It operationalizes the playbook's core rule: **instrument first, gate by consequence, expand coverage, add autonomy last — and let measurement, not enthusiasm, pace each step.**

This is a template, not a mandate. Move faster or slower based on what your [metrics](./governance-and-metrics.md#metrics-that-actually-prove-value) tell you.

## Before day 0 — prerequisites

- A baseline of your delivery metrics (release frequency, lead time, change-failure/rework rate, cost per task). You can't prove improvement without a before.
- Agreement on which actions are irreversible/outward-facing (they will stay human-gated). See [guardrails by blast radius](./governance-and-metrics.md#guardrails-design-for-the-blast-radius).

## Days 0–30 — Instrument and pick one stage

**Goal:** make agent work observable and land value in exactly one stage.

- Stand up the [observability trace](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see) (plan, tool calls, cost, checkpoints, evidence) *before* any autonomy.
- Choose the **single highest-friction stage you can verify** — often test/verify or review, not coding. Automate that one with a [workflow](./patterns/), not a full agent.
- Keep a human at every merge/deploy gate. Require [evidence, not assertion](./governance-and-metrics.md#human-in-the-loop-design) for "done".

**Exit criteria:** you can produce a full trace for any agent run, and the chosen stage shows a measurable improvement without a rise in rework rate.

## Days 30–60 — Add a second and third stage

**Goal:** cross toward the [6+ stage threshold](./agentic-sdlc.md#why-6-stages-is-the-threshold-that-matters) where compounding gains appear.

- Add adjacent stages so hand-offs between agents replace manual serial hops (the actual source of end-to-end gains).
- Introduce a **reviewer agent** in a *separate context* as a first-pass ([reflection](./agentic-workflows.md#reflection)) — but keep the human merge decision.
- Watch for [rubber-stamp review](./anti-patterns.md#4-rubber-stamp-review--the-checkpoint-that-stopped-checking): rate-limit agent output to reviewable volume.

**Exit criteria:** 3+ stages have meaningful agent participation; lead time is down and change-failure rate is flat or better.

## Days 60–90 — Expand coverage, then (carefully) autonomy

**Goal:** reach 6+ stage coverage; grant more autonomy only where measured.

- Push coverage across the remaining stages (plan, operate) using workflows first.
- Only where a stage has a **clear evaluation signal** and iteration measurably helps, promote a workflow to a more autonomous loop ([evaluator-optimizer](./patterns/evaluator-optimizer.md) / [orchestrator-workers](./patterns/orchestrator-workers.md)) — with hard [loop budgets](./anti-patterns.md#7-unbounded-loops--no-budget-no-exit).
- Re-baseline metrics; compare against day 0.

**Exit criteria:** 6+ stages covered; release frequency and defect/rework metrics moved in the right direction *and* cost per completed task is flat or falling.

## The checkpoint that governs the whole roadmap

At every step, ask: **has team throughput moved, or only coding output?** If coding is up 30–40% but end-to-end delivery isn't, the bottleneck moved downstream — stop adding coding autonomy and instrument the new bottleneck. See [the trap to avoid](./governance-and-metrics.md#the-trap-to-avoid).

## See also

- [Agentic SDLC](./agentic-sdlc.md) · [Governance & Metrics](./governance-and-metrics.md) · [Anti-Patterns](./anti-patterns.md)
