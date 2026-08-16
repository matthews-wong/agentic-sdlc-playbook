# Cost & Performance

> Agents multiply model calls — a single task can fan into planning, tool loops, reflection, and verification. Cost and latency are therefore *architectural*, not a billing afterthought. The metric that matters is **cost per completed task**, not cost per call. This is the optimization companion to [governance & metrics](./governance-and-metrics.md).

## The mindset: optimize the task, not the call

A cheaper per-call model that loops five times to get a right answer can cost more than one capable call. Always measure the **fully-loaded cost of an accepted result** — tokens + retries + tool calls + human review time. Optimize that number.

## The levers (stack them)

Reported results from 2026 practice suggest a combined **~47–80% spend reduction** without degrading UX by stacking these — roughly in order of leverage:

### 1. Prompt caching

Cache the **stable** part of the prompt (system prompt, tool defs, long context) so repeated calls don't re-pay for it. Industry measurements report **~41–80% cost reduction** and **~13–31% faster time-to-first-token**.

> **The rule that makes or breaks it:** keep the stable prefix first and put **dynamic content at the end**, where it doesn't invalidate earlier cache blocks. Structure prompts cache-first.

### 2. Model routing / tiering

Classify task difficulty and route to the smallest model that can do it; escalate only hard cases. This is the [routing pattern](./patterns/routing.md) applied to *cost*. Reported savings **~40–70%**, with routing studies retaining ~95% of frontier-model quality at a fraction of the cost.

### 3. Prompt compression

Trim redundant context, summarize long histories, and pass references instead of full blobs. Fewer input tokens on every call.

### 4. Batching

For non-urgent work — evals, backfills, pipelines, background jobs — use batch APIs (often a **~50% discount**) and trade latency for cost. Perfect for the offline [eval](./evaluating-agents.md) runs.

### 5. Self-hosted levers

Quantization / distillation for models you run yourself, where infra cost dominates.

## Latency, specifically

Cost and latency don't always move together. For responsiveness:

- **[Parallelize](./patterns/parallelization.md) independent work** — fan out concurrent subtasks/tool calls instead of serial chains; wall-clock becomes the slowest branch, not the sum.
- **Stream** where a user is waiting; caching's time-to-first-token gain compounds here.
- **Cap loops** — an unbounded [evaluator-optimizer](./patterns/evaluator-optimizer.md) is a latency *and* cost hazard ([anti-pattern #7](./anti-patterns.md#7-unbounded-loops--no-budget-no-exit)).

## Test orchestration without spending

You don't need live calls to test agent *logic*. The [examples in this repo](../examples/release-notes-agent/) use a deterministic mock backend so the whole workflow — and CI — runs at zero model cost. Reserve real calls (and real spend) for the [evals](./evaluating-agents.md) that actually need them.

## A cost/perf checklist

- [ ] You measure **cost per completed task**, not per call.
- [ ] Prompts are cache-first: stable prefix, dynamic content last.
- [ ] Requests are routed to the smallest capable model; only hard cases escalate.
- [ ] Non-urgent work goes through batch APIs.
- [ ] Independent steps are parallelized; every loop has a budget cap.
- [ ] Agent logic is testable against a mock so CI costs nothing.

## Sources & caveat

See [references.md](./references.md#cost--performance). All percentages are **directional** benchmarks from cited 2026 reporting — measure your own workload before promising a number.
