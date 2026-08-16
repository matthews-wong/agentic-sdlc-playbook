# Evaluating Agents

> You can't govern or improve what you can't score. But agents aren't unit-testable the way ordinary code is — they're **non-deterministic**, and the *path* matters as much as the answer. This page is how to evaluate them without fooling yourself. It's the measurement companion to [governance & metrics](./governance-and-metrics.md).

## Why agent evaluation is different

Traditional tests assert `f(x) == y`. Agents break that in two ways:

1. **Non-determinism** — the same input can yield different trajectories and outputs across runs.
2. **The trajectory matters** — an agent can reach a right answer via a wrong, expensive, or unsafe path. Scoring only the final message hides that.

So you evaluate at **three layers**:

| Layer | What it scores | Good for |
|-------|----------------|----------|
| **Final-answer** | The last message only | Quick regression on outcome |
| **Trajectory / tool-use** | The whole sequence of steps and tool calls | Catching wrong paths, wasted tools, unsafe actions |
| **Per-turn** | The meaning/quality of each turn in production | Live monitoring |

## LLM-as-judge: powerful, but know where it fits

Use an LLM to judge subjective, context-dependent criteria (task completion, reasoning quality, custom rubrics) — but respect two limits:

- **Cost** — each judgment is a full model call; too expensive to run on *every* production turn.
- **Variance** — the same trajectory can score differently across runs.

**Rule of thumb:** LLM-as-judge is right for **offline scoring on a held-out sample**, where cost and variance are bounded. For **per-turn production** labels, you need something **deterministic and cheap** (rules, classifiers, assertions), not a judge on every turn.

## Regression testing under non-determinism

You still need regression tests — you just build them differently:

- **Build tests from real failures.** Every production incident becomes a fixture. This is your most valuable dataset; benchmarks aren't.
- **Sample, don't exhaustively re-run.** Sampling-based approaches give statistical confidence on non-deterministic workflows without paying to re-evaluate everything on each change.
- **Gate the deterministic scaffold separately.** Much of an agent is ordinary code (routing, parsing, tool wiring). Lock that behind fast, no-LLM regression tests — as the [examples in this repo do](../examples/release-notes-agent/) with a mock backend. It isolates "did my orchestration break?" from "did the model drift?"

## Benchmarks vs. your workflows

Public benchmarks (AgentBench, WebArena, SWE-bench) are useful for **standardized comparison** — is model/framework A broadly better than B? They do **not** represent your production workflows. Ship with:

- a **custom dataset** drawn from your real tasks,
- **trace-based evals** over trajectories, and
- **regression tests built from real failures.**

## How this connects to the rest of the playbook

- Evaluation is what makes an [evaluator-optimizer](./patterns/evaluator-optimizer.md) loop possible — no eval signal, nothing to optimize (that's [anti-pattern territory](./anti-patterns.md#7-unbounded-loops--no-budget-no-exit)).
- It's how "[evidence, not assertion](./governance-and-metrics.md#human-in-the-loop-design)" becomes concrete: a passing eval *is* the evidence.
- It feeds the [metrics that prove value](./governance-and-metrics.md#metrics-that-actually-prove-value) — rework rate and change-failure rate come straight from your eval + production signals.

## A minimal evaluation setup

- [ ] Deterministic scaffold (routing/parsing/tools) covered by fast, no-LLM regression tests.
- [ ] A custom, versioned dataset built from real tasks and past failures.
- [ ] Trajectory-level evals, not just final-answer, for anything with tool use.
- [ ] LLM-as-judge only offline, on a held-out sample, with variance acknowledged.
- [ ] Cheap deterministic labels for per-turn production monitoring.
- [ ] New incidents added as fixtures (a bug fix comes with the eval that would have caught it).

## Sources

See [references.md](./references.md#evaluating-agents). Directional; validate against your own workflows.
