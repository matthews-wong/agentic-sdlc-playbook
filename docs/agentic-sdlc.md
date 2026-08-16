# The Agentic SDLC

> Software delivery in which AI agents participate meaningfully across the full lifecycle — planning, coding, reviewing, deploying, and operating — pursuing goals across multiple steps without a human directing each one.

## Definition

In an **agentic SDLC**, the developer sets the *intent* and reviews the *result*; the agent handles the multi-step workflow in between. This is the key break from the prior era of "AI-assisted development," where a copilot generated suggestions in response to each prompt but never carried a task to completion on its own.

A useful mental model:

| Era | Human role | AI role | Unit of work |
|-----|-----------|---------|--------------|
| AI-assisted | Directs every step | Suggests completions | A line / a function |
| **Agentic** | Sets intent, reviews at checkpoints | Executes multi-step tasks | A ticket / a feature / an incident response |

## The lifecycle, stage by stage

Agents can take meaningful work in every stage. The pattern that repeats is **agent executes → human reviews at a defined checkpoint**.

### 1. Plan
- Agents draft specs from a goal, decompose epics into tasks, and surface ambiguities as questions.
- Human checkpoint: approve the plan and acceptance criteria before code is written.

### 2. Build
- Agents implement tasks, write tests alongside code, and open pull requests.
- This is the most mature stage today (the 30–40% coding gains come from here) — but on its own it moves the whole-team needle by <10%.

### 3. Review
- Agents perform first-pass code review: style, obvious bugs, security smells, test coverage gaps.
- Human checkpoint: humans still own the merge decision on anything consequential.

### 4. Test & Verify
- Agents generate edge-case tests, run suites, triage failures, and reproduce bugs.
- The highest-leverage under-automated stage — automating it is where the "6+ stages" teams pull ahead.

### 5. Deploy
- Agents prepare release notes, run deployment checklists, and gate on health signals.
- Human checkpoint: production promotion typically stays behind an explicit approval.

### 6. Operate
- Agents watch telemetry, triage alerts, draft incident comms, and propose mitigations.
- The loop closes here: operational findings feed back into the next plan.

## Why "6+ stages" is the threshold that matters

Teams that apply GenAI across **six or more** SDLC stages release nearly **twice as often** and, in some samples, cut defects by **up to 96%**. The disappointing results many organizations report come from applying AI too narrowly — accelerating coding while planning, testing, and release stay manual. Amdahl's law applies to delivery: speeding up one stage while the rest stay serial and human-bound yields small end-to-end gains.

## Roles in an agentic SDLC

Rather than one monolithic "AI developer," mature setups use **specialized agents** with narrow responsibilities, each with its own prompt, tools, and guardrails:

- **Planner** — turns intent into a reviewed plan.
- **Implementer** — writes code and tests for a scoped task.
- **Reviewer** — critiques diffs (ideally an agent that did *not* write the code).
- **Verifier** — proves the change works end to end and reports evidence, not assertions.
- **Operator** — watches production and triages.

An orchestrator routes work between them; humans hold the checkpoints.

## What stays human

- Setting intent, priorities, and acceptance criteria.
- Merge and production-promotion decisions on consequential changes.
- Owning trade-offs the agent surfaces but should not unilaterally resolve.
- Accountability. Governance and human-AI collaboration are *core design principles*, not add-ons.

## Adoption sequence (a pragmatic order)

1. Instrument first — you cannot manage what you cannot measure. Stand up observability before autonomy.
2. Automate the highest-friction stage you can *verify* (often testing/review), not just coding.
3. Add human checkpoints at every irreversible or outward-facing step.
4. Expand stage coverage toward the 6+ threshold.
5. Only then increase agent autonomy — and only where a measured need justifies the reduced predictability.

## See also

- [Agentic Workflows](./agentic-workflows.md) — the patterns that make each agent reliable.
- [Governance & Metrics](./governance-and-metrics.md) — guardrails and how to prove value.
- [References](./references.md) — sources for every claim above.
