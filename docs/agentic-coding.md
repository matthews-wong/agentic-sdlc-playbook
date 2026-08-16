# Agentic Coding

> The [SDLC guide](./agentic-sdlc.md) covers the whole lifecycle; this is the hands-on inner loop: how a developer actually works *with* a coding agent day to day. The short version — **when agents write the code, the spec is the most leveraged thing a human can produce.**

## Spec-driven development (SDD)

The developers who ship the most with AI write **specs, not just prompts.** Spec-driven development — write a structured, versioned spec first, then let the agent build against it — reportedly prevents the large majority of agentic-coding disasters. The key mental shift: **the spec is the source of truth, not the code.** Code becomes a build artifact of the spec.

This is the opposite of "vibe coding" (prompt → hope). It's prompt engineering grown up into [instruction design](./prompting-and-instructions.md) at the task level.

## What a good spec contains

Keep it a short markdown file — think 4–8 bullets, not a novel — covering:

1. **Outcomes** — what success looks like.
2. **Scope boundaries** — explicitly what's in and *what's out*.
3. **Constraints** — tech, style, performance, security limits.
4. **Prior decisions** — context/ADRs the agent must respect.
5. **Task breakdown** — the work in reviewable chunks.
6. **Verification criteria** — how "done" is proven (usually tests).

## The flow: never jump spec → code

Insert review gates between phases — this is [prompt chaining](./patterns/prompt-chaining.md) with human checkpoints:

```
spec ──▶ (review spec) ──▶ plan ──▶ (review plan) ──▶ tasks ──▶ (review tasks) ──▶ implement ──▶ (review code)
```

- **Review the plan and the tasks before any code is written.** Cheap to steer here; expensive to unwind later.
- **Implement in small groups of tasks — don't one-shot a whole feature phase.** Smaller diffs are reviewable diffs, and they keep the agent from compounding a wrong turn.

## Tests are the spec, executable

Verification criteria should land as **tests**. Tests turn "the agent says it's done" into [evidence, not assertion](./governance-and-metrics.md#human-in-the-loop-design), and they're the deterministic scaffold you can [regression-test](./evaluating-agents.md#regression-testing-under-non-determinism) as the model changes. A bug fix comes with the test that would have caught it.

## Review is now the main event

As authorship shifts to the agent, the developer's time moves to **steering, reviewing, and architectural decisions.** Code review becomes one of the most important steps — worth investing serious time in, and best done by a human (or a [separate-context reviewer agent](./patterns/evaluator-optimizer.md)) rather than the agent that wrote it. Guard against [rubber-stamp review](./anti-patterns.md#4-rubber-stamp-review--the-checkpoint-that-stopped-checking) by keeping diffs small enough to actually read.

## See it in miniature

The repo's [release-notes example](../examples/release-notes-agent/) is this loop in code: a chained extract→group→render with an evaluator (tests) gating "done" — the same spec→build→verify shape at function scale.

## An agentic-coding checklist

- [ ] A short, versioned **spec** exists before the agent writes code.
- [ ] The spec names outcomes, scope (incl. out-of-scope), constraints, and verification criteria.
- [ ] Plan and tasks are **reviewed before** implementation.
- [ ] Work ships in **small task groups**, not one giant diff.
- [ ] Verification criteria are executable **tests**.
- [ ] Code review is a real, time-invested step by a fresh reviewer.

## Sources

See [references.md](./references.md#agentic-coding--spec-driven-development). Figures are directional 2026 reporting.
