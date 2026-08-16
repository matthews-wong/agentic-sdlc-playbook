# Team & Operating Model

> The [adoption roadmap](./adoption-roadmap.md) is the *time* view of going agentic. This is the *people* view: how roles, skills, and org structure change when small human teams coordinate large groups of agents. Technology rarely blocks agentic SDLC — the operating model does.

## The core pattern: delegate, review, own

Leading teams converge on a simple loop: **delegate** work to agents, **review** the result at defined checkpoints, and **own** the outcome. The org reorganizes around **small human teams coordinating many specialized agents** across the lifecycle — not more humans writing more code.

## The role shift: from creator to curator

The engineer's center of gravity moves from *writing* to *directing*:

| Was | Becomes |
|-----|---------|
| Writing foundational code | Orchestrating a portfolio of agents, components, and services |
| Syntax fluency | **Systems thinking** — architecture, interfaces, trade-offs |
| Author of the change | **Curator**: defines objectives + guardrails, then rigorously validates output |

The scarce skill is no longer producing code; it's **specifying intent precisely, setting guardrails, and evaluating agent output** against business context. Team capability shifts toward **review, prioritization, and auditing** — which is exactly why [evaluation](./evaluating-agents.md) and [governance](./governance-and-metrics.md) become central, not optional.

## New roles that emerge

- **Agentic architect** — designs the multi-agent system: which agents exist, how they coordinate ([orchestration](./patterns/orchestrator-workers.md)), where the human gates sit.
- **Knowledge architect** — curates the context/knowledge network agents draw on (feeds [context & memory](./context-and-memory.md)).
- **Agent reliability engineer** — the SRE for agents: owns [reliability](./reliability-and-recovery.md), [evals](./evaluating-agents.md), and [observability](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see).

## Two organizational patterns (from 2026 practice)

- **Centralized agent platform team.** LinkedIn stood up a fully-funded agent platform team — structured like a storage or ML-infra team — centralizing prompt orchestration, data access, safety evaluations, and deployment. *Use when* many product teams need consistent, safe agent infrastructure; avoids every team reinventing guardrails.
- **Lifecycle "tiger teams."** Red Hat organized SDLC tiger teams mapped to requirements, architecture, security, quality engineering, documentation, and release automation across a 500+ engineer org. *Use when* you're driving agent adoption stage-by-stage across a large org (pairs naturally with the [6+ stage push](./agentic-sdlc.md#why-6-stages-is-the-threshold-that-matters)).

Most orgs end up with **both**: a platform team owning the shared substrate, and embedded/tiger teams applying it per stage or domain.

## Non-negotiables before scaling headcount-of-agents

- **Clear human accountability.** Someone owns each outcome; "the agent did it" is never an answer.
- **Auditability.** The [observability trace](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see) is org infrastructure, not a per-team afterthought.
- **Testing gets *more* important, not less** — the [verification](./evaluating-agents.md) burden rises as authorship shifts to agents.

## A staffing checklist

- [ ] Every agent-produced outcome has a named human owner.
- [ ] Someone owns the agent *platform* (guardrails, evals, data access) — not duplicated per team.
- [ ] Review/audit capacity is staffed to match agent output volume (guards against [rubber-stamp review](./anti-patterns.md#4-rubber-stamp-review--the-checkpoint-that-stopped-checking)).
- [ ] Engineers are supported in the shift to systems thinking / curation, not just handed a tool.
- [ ] Reliability + evaluation are an owned role, not a side task.

## Sources

See [references.md](./references.md#team--operating-model). Org examples and role framing are from 2026 industry reporting; adapt to your scale.
