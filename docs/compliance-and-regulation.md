# Compliance & Regulation

> [Governance & metrics](./governance-and-metrics.md) is the *internal* discipline of running agents well. This page is the *external* one: the regulatory frameworks you may be obligated to meet. Not legal advice — a practitioner's map. Verify specifics with counsel.

## The three frameworks you'll hear about

| Framework | Nature | In one line |
|-----------|--------|-------------|
| **EU AI Act** | **Law** (enforceable, penalties) | Risk-tiered obligations; strongest teeth |
| **NIST AI RMF** | Voluntary framework | Risk-management practices; a good starting point |
| **ISO/IEC 42001** | Certifiable standard | An AI management system you can be audited/certified against |

All three aim to increase trust in AI, but differ in scope, enforcement, and obligations.

## EU AI Act — the timeline that matters

- **Feb 2025** — prohibited practices banned.
- **Aug 2025** — general-purpose AI model governance rules applied.
- **Aug 2, 2026** — **high-risk system obligations (Articles 8–17, 26, 27, 73) and full enforcement penalties are now in force.**

If you build high-risk systems with EU exposure, those obligations are live *today*, not a future problem. A central requirement: **effective human oversight** for high-risk systems — document **who holds decision authority** and provide a clear path to **appeal or correction.** That maps directly onto the playbook's [human checkpoints](./governance-and-metrics.md#human-in-the-loop-design).

## The agentic gap (read this before assuming you're covered)

**None of the three frameworks was designed for agentic AI.** They assume a model that predicts, not an agent that acts across many steps with tools and state. Current status:

- **Singapore's Jan 2026 framework** is (so far) the only governance document addressing autonomous agents directly.
- **NIST** acknowledged the gap in Feb 2026 with an **AI Agent Standards Initiative** (via CAISI); an **AI Agent Interoperability Profile** is planned for Q4 2026.

So: apply the existing frameworks, but expect them to under-specify agent-specific risks (tool misuse, [prompt injection](./security.md), long-horizon [governance decay](./context-and-memory.md#compaction-necessary-and-quietly-dangerous)). Cover those with this playbook's controls, not by assuming the regulation already did.

## A pragmatic sequence (US-centric)

A common ordering that builds reusable groundwork:

1. **NIST AI RMF** for risk management (~3–6 months) — the cheapest way to get structured.
2. **ISO/IEC 42001** for a certifiable management system (~2–4 months more) — turns practice into auditable process.
3. **EU AI Act** layered on if you have European exposure (~2–4 months more) — the legal obligations on top.

Much of the evidence these demand — audit trails, human-oversight records, risk assessments — is the **same [observability trace](./observability.md) and [governance](./governance-and-metrics.md) discipline** you already need. Build it once; report it many ways.

## What compliance concretely asks of an agentic system

- **Audit trails** — a durable, reviewable record of what the agent did and why ([observability](./observability.md)).
- **Human oversight proportionate to risk** — with documented decision authority and an appeal/correction path.
- **Risk assessment & documentation** — especially for high-risk use cases.
- **Data governance** — provenance and handling of what agents read and produce.

## A compliance checklist

- [ ] You know which tier/obligations (if any) apply to *your* use case and jurisdictions.
- [ ] Human oversight for high-risk flows is documented: who decides, how to appeal/correct.
- [ ] Audit trails are durable and reviewable (not just app logs) — reuse the observability trace.
- [ ] Agent-specific risks are covered by controls even where regulation is silent.
- [ ] Framework work is sequenced (RMF → 42001 → EU AI Act) to reuse evidence.
- [ ] Someone owns this — treated as ongoing, since standards are actively evolving.

## Sources & disclaimer

See [references.md](./references.md#compliance--regulation). **This is not legal advice.** Dates and obligations are as reported in 2026 and change; confirm current requirements with qualified counsel.
