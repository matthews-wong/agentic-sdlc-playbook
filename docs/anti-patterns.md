# Anti-Patterns

> Most AI production failures between 2024 and 2026 were **architectural, not model-quality, failures.** This catalog names the recurring ways agentic systems go wrong, so you can recognize them before they cost you. Each entry: the smell, why it happens, and the fix.

Cross-references: [when *not* to build an agent](./agentic-workflows.md#when-not-to-build-an-agent) · [governance & metrics](./governance-and-metrics.md).

---

## 1. Autonomy theater — an agent where a workflow would do

**Smell:** you reached for a fully autonomous agent (the model owns the loop) for a task whose steps are actually known and fixed.

**Why it happens:** "agent" is the exciting word; a deterministic [prompt chain](./patterns/prompt-chaining.md) or plain code feels less impressive.

**Cost:** less predictable, harder to debug, more expensive per task — for no gain. This was *the* signature failure of 2024–2026.

**Fix:** climb the [complexity ladder](./patterns/) from the bottom. Use the least autonomy the task forces on you. If the steps are known, define them.

---

## 2. Narrow adoption — automating only coding

**Smell:** coding throughput is up 30–40%, but overall team productivity rose **<10%** and nobody can say why.

**Why it happens:** coding assistants are the easiest thing to adopt, so teams stop there while planning, testing, and release stay manual.

**Cost:** the bottleneck simply moves downstream; end-to-end delivery barely improves (Amdahl's law for delivery).

**Fix:** instrument the whole flow, find the new bottleneck stage (often test/verify or review), and automate *that*. Push toward the [6+ stage threshold](./agentic-sdlc.md#why-6-stages-is-the-threshold-that-matters).

---

## 3. Assertion-as-done — trusting "I completed the task"

**Smell:** the agent reports success; you ship; it wasn't actually done.

**Why it happens:** an LLM will happily claim completion without evidence, and it's tempting to believe it.

**Cost:** silent defects, eroded trust, rework.

**Fix:** require **captured evidence** — test output, a reproduced happy path, a diff that applies — before a task is accepted. "Done" is a verification result, not a sentence. See [governance](./governance-and-metrics.md#human-in-the-loop-design).

---

## 4. Rubber-stamp review — the checkpoint that stopped checking

**Smell:** agents open PRs faster than humans can meaningfully review, so review degrades into clicking "approve."

**Why it happens:** async agents scale output; human review capacity doesn't.

**Cost:** your one real safety gate becomes decorative; defect rate climbs while everyone *feels* productive.

**Fix:** rate-limit agent output to reviewable volume; add an independent [reviewer agent](./patterns/evaluator-optimizer.md) as a first pass; track **rework rate** and **review load**, not PR count.

---

## 5. Self-review blindness

**Smell:** the same agent (same context) that wrote the output also "reviews" it — and approves almost everything.

**Why it happens:** it's the cheapest thing to wire up.

**Cost:** a model is a poor critic of its own reasoning within one context; real errors survive.

**Fix:** review with a **different agent or a fresh context**. [Reflection](./agentic-workflows.md#reflection) works; reflection-in-the-same-breath mostly doesn't.

---

## 6. Flying blind — autonomy before observability

**Smell:** "the agent did something and it broke" — and you can't reconstruct what it did.

**Why it happens:** observability feels like overhead you'll add "later"; autonomy ships first.

**Cost:** every failure is a guessing game; you can't compute the metrics that would tell you if any of this works.

**Fix:** stand up the [observability trace](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see) (plan, tool calls, cost, checkpoints, evidence) **before** expanding autonomy.

---

## 7. Unbounded loops — no budget, no exit

**Smell:** an [evaluator-optimizer](./patterns/evaluator-optimizer.md) or agent loop runs on, burning tokens, never satisfied.

**Why it happens:** the happy path was coded; the "never converges" path wasn't.

**Cost:** runaway cost and latency; sometimes a wrong answer delivered late.

**Fix:** hard round/token/time caps on every loop. Log and surface what was dropped when a cap is hit — silent truncation reads as success.

---

## 8. Blast-radius blindness — same trust for `read file` and `deploy prod`

**Smell:** the agent can trigger irreversible or outward-facing actions (merge, deploy, delete, send email) with the same freedom it reads a file.

**Why it happens:** guardrails were uniform instead of matched to consequence.

**Cost:** a single bad step is unrecoverable.

**Fix:** gate by [blast radius](./governance-and-metrics.md#guardrails-design-for-the-blast-radius) — autonomous for reversible/internal, human checkpoint for irreversible/outward-facing.

---

## 9. Framework-first — ceremony before need

**Smell:** you adopted a heavy agent framework before you had a problem it solves.

**Why it happens:** picking a tool feels like progress.

**Cost:** token overhead, a learning curve, and indirection between you and the behavior — for patterns that were a few lines of code.

**Fix:** start with direct API calls and the [patterns](./patterns/). Adopt a [framework](./tooling-landscape.md) only when state, coordination, or observability becomes the thing you're spending time on.

---

## 10. Vanity metrics — measuring output, not outcomes

**Smell:** dashboards celebrate "lines/PRs/tokens generated."

**Why it happens:** output volume is easy to count.

**Cost:** you optimize for motion, not delivery; more output can *mean* more rework.

**Fix:** measure flow (release frequency, lead time), quality (defect/change-failure/rework rate), and economics (cost per completed task). See [metrics that actually prove value](./governance-and-metrics.md#metrics-that-actually-prove-value).

---

## The one-line summary

Autonomy is a cost you pay for flexibility you can't get otherwise. Pay it deliberately — least first, gated by consequence, measured by outcomes, and never without a trace.
