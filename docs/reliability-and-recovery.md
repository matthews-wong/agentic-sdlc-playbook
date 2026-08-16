# Reliability & Recovery

> Long-running agents fail in the middle — a tool times out, a rate limit hits, a step half-completes. Reliability is designing so those failures are **safe, resumable, and never silently doubled.** This extends [governance & metrics](./governance-and-metrics.md) into fault tolerance.

## First rule: not every error is a retry

Reliable agents don't treat every error as an invitation to try again. They:

- **Distinguish transient from terminal** — retry a timeout or a 429; do **not** retry a 400 or a validation failure (it'll fail identically).
- **Preserve evidence** — capture structured logs (timestamp, agent ID, input snippet, error code) so scattered failures become patterns you can act on.
- **Stop when the outcome is uncertain** — an ambiguous partial failure escalates; it does not blindly re-run.

## Retry strategy that doesn't make things worse

Naive retries amplify outages. The strong policy combines:

- **Exponential backoff + jitter** — spread retries so you don't synchronize a thundering herd against a recovering service.
- **Retry budgets** — a cap on total retries per task, not just per call, so one flaky dependency can't blow your whole cost/latency budget ([anti-pattern #7](./anti-patterns.md#7-unbounded-loops--no-budget-no-exit)).
- **Circuit breaker** — after N consecutive failures, stop calling the dependency for a cooldown, failing fast instead of cascading.
- **Shared rate-limit controls** — coordinate limits across concurrent agents so parallel work doesn't self-DoS your provider.

## Idempotency: never double a side effect

**Idempotency** = repeating an operation yields the same final result as doing it once. It's the central safeguard, because retries *will* replay side-effectful calls.

- Put an **idempotency key** on every side-effectful tool call (create-PR, send-email, charge, deploy). The downstream system dedupes replays.
- Design tools so a replay with the same key is a no-op that returns the original result.

## Durable state & the saga pattern

For multi-step agents, make progress **survivable**:

- **Record each step's completion in a durable store *before* executing the next** — so a crash resumes from the last good step instead of restarting (and re-doing side effects).
- **Define a compensation action per rollback-able step** (the saga pattern) — if step 4 fails, run the undo for steps 3→1 rather than leaving a half-applied change.
- **Checkpoint** long runs so they're resumable — this is the reliability sibling of [context compaction](./context-and-memory.md#compaction-necessary-and-quietly-dangerous); persist state, not just summarize it.

## When to stop and escalate to a human

Escalate (don't keep retrying) when:

- the same step has **failed validation after ~3 retries**,
- the task involves a **high-value irreversible action** (payment, legal doc, account/data deletion, deploy) — this is the [blast-radius gate](./governance-and-metrics.md#guardrails-design-for-the-blast-radius),
- the agent's **confidence falls below threshold**, or
- a **safety policy violation** is detected.

## A reliability checklist

- [ ] Errors are classified transient vs. terminal; only transient ones retry.
- [ ] Retries use backoff + jitter, a per-task budget, and a circuit breaker.
- [ ] Every side-effectful tool call carries an idempotency key.
- [ ] Multi-step progress is written to durable state before the next step runs.
- [ ] Rollback-able steps have compensation actions (saga).
- [ ] Clear escalation triggers route to a human instead of infinite retry.
- [ ] Failures are logged with enough structure to become patterns, not noise.

## Sources

See [references.md](./references.md#reliability--recovery). Patterns are standard distributed-systems practice applied to agents; validate against your stack.
