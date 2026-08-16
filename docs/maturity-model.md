# Agentic SDLC Maturity Model

> A five-level model to locate where your team actually is — and what to build next. It synthesizes the rest of the playbook: each level names the practices, and the links point to the guide that makes it real. **More autonomy is not the goal; the right level for your risk and measurement is.**

## The five levels

| Level | Name | What it looks like | Human role |
|-------|------|--------------------|-----------|
| **1** | **Manual** | No agents; maybe autocomplete | Does all the work |
| **2** | **AI-assisted** | Copilots suggest per prompt; single-stage | Directs every step |
| **3** | **Agent execution + review** | Agents do multi-step tasks; humans gate at checkpoints | Sets intent, reviews at gates |
| **4** | **Orchestrated** | Multiple specialized agents across 6+ stages, coordinated | Owns architecture + checkpoints |
| **5** | **Autonomous operations** | AI is the primary implementer within guardrails | Oversight for strategy, security, verification |

> **The 2026 production frontier is Level 3** — agent execution with human review. Most teams should aim to do L3 *well* (and reach into L4 on well-instrumented stages) before chasing L5. L5 without the lower levels' governance is how the [anti-patterns](./anti-patterns.md) happen.

## What each level requires (don't skip)

- **L1 → L2:** a coding assistant; basic prompting discipline. Watch the [narrow-adoption trap](./anti-patterns.md#2-narrow-adoption--automating-only-coding) — L2 alone barely moves team throughput.
- **L2 → L3:** [observability](./observability.md) first; [human checkpoints](./governance-and-metrics.md#guardrails-design-for-the-blast-radius) at irreversible actions; [evidence-not-assertion](./governance-and-metrics.md#human-in-the-loop-design) verification. Pick one high-friction stage ([roadmap days 0–30](./adoption-roadmap.md#days-030--instrument-and-pick-one-stage)).
- **L3 → L4:** cross the [6+ stage threshold](./agentic-sdlc.md#why-6-stages-is-the-threshold-that-matters); multi-agent [orchestration](./patterns/orchestrator-workers.md) and [protocols](./protocols-mcp-a2a.md); a platform/[operating model](./team-and-operating-model.md); real [evals](./evaluating-agents.md).
- **L4 → L5:** hardened [security](./security.md), [reliability](./reliability-and-recovery.md), and [compliance](./compliance-and-regulation.md); autonomy only where evals prove it and guardrails contain it.

## Self-assessment: score each dimension 1–5

Rate your team on each; your true maturity is closer to the **lowest** dimension than the average (a chain is as strong as its weakest link).

| Dimension | 1 | 3 | 5 | Guide |
|-----------|---|---|---|-------|
| **Autonomy** | manual | agent + review | autonomous in guardrails | [workflows](./agentic-workflows.md) |
| **Stage coverage** | 1 stage | 3 stages | 6+ stages | [SDLC](./agentic-sdlc.md) |
| **Observability** | app logs | per-run traces | full GenAI telemetry | [observability](./observability.md) |
| **Evaluation** | manual spot-check | offline evals | trajectory + regression | [evaluating](./evaluating-agents.md) |
| **Governance/HITL** | ad hoc | gated by blast radius | proportionate + audited | [governance](./governance-and-metrics.md) |
| **Security** | none agent-specific | least-priv + sandbox | full defense stack | [security](./security.md) |
| **Reliability** | best-effort | retries + idempotency | durable + saga | [reliability](./reliability-and-recovery.md) |
| **Org/roles** | individuals + tool | review capacity staffed | platform team + roles | [operating model](./team-and-operating-model.md) |

## How to use this

1. Score the eight dimensions honestly.
2. Find your **weakest** dimension — that's the bottleneck, not your best one.
3. Open that dimension's guide and do the "→ next level" work above.
4. Re-score against your [metrics](./governance-and-metrics.md#metrics-that-actually-prove-value), not your vibes.

Progress is sequential — organizations move through exploration → integration → orchestration → autonomous operations in order. Skipping levels skips the guardrails that make the next one safe.

## Sources

See [references.md](./references.md#maturity-models). Level names vary across frameworks; the progression is the durable part.
