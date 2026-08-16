# Governance & Metrics

> Governance, measurement, and human-AI collaboration are **core design principles** of the agentic SDLC — not compliance afterthoughts. Organizations that invest early in structured observability, talent development, and end-to-end integration set the new performance benchmark.

## The central claim

Most AI production failures between 2024 and 2026 were **architectural, not model-quality, failures.** Better prompts and bigger models did not fix them; better *structure* did — guardrails, observability, and human checkpoints placed where they matter. This section is about that structure.

## Guardrails: design for the blast radius

Match the control to how reversible and how outward-facing an action is.

| Action class | Example | Control |
|--------------|---------|---------|
| Reversible, internal | Run tests, read a file, draft a plan | Let the agent proceed autonomously |
| Reversible, outward-facing | Open a draft PR, post to a staging channel | Proceed, but log and make it easy to undo |
| Irreversible or high-blast-radius | Merge to main, deploy to prod, delete data, send external comms | **Human checkpoint required** |

Push validation to the edges: validate inputs and tool arguments at the boundary, and keep the agent's core logic trusting a small set of already-checked facts.

## Human-in-the-loop design

- **Checkpoints, not babysitting.** The human reviews at defined gates (plan approval, merge, prod promotion) rather than watching every step. That is the whole point of the agentic model.
- **Evidence over assertion.** An agent reporting "done" is not done. Require captured evidence — test output, a reproduced happy path — before a task is accepted.
- **A reviewer that didn't write the code.** First-pass review by a *different* agent (or a fresh context) catches more than self-review of the same context.

## Observability: you cannot govern what you cannot see

Stand up observability **before** you expand autonomy. At minimum, capture for every agent run:

- The intent/goal and the plan the agent committed to.
- Every tool call with its arguments and result.
- Token and cost accounting per task.
- The human checkpoints hit and their outcomes.
- Final evidence and the accept/reject decision.

This trace is what turns an opaque "the agent did something" into a debuggable, auditable workflow — and it is the raw material for the metrics below.

## Metrics that actually prove value

Vanity metric: "lines of code generated." Real metrics tie to delivery outcomes.

### Flow & throughput

- **Release frequency** — top teams (6+ AI-covered stages) release ~**2×** as often.
- **Lead time for change** — intent to production.
- **Stage coverage** — how many SDLC stages have meaningful agent participation. The **6+ threshold** is where compounding gains appear.

### Quality

- **Defect / change-failure rate** — some 6+ stage samples report **up to 96%** fewer defects. Watch this closely; autonomy without verification moves it the wrong way.
- **Rework rate** — how often agent output is rejected or reverted at checkpoints.

### Economics

- **Cost per completed task** — tokens + compute + human review time. Falling cost-per-task at flat-or-better quality is the signal that autonomy is paying off.
- **Human review load** — trending down as trust and verification mature.

### The trap to avoid

Coding throughput improving 30–40% while overall team productivity rises **<10%** is the signature of narrow adoption. If your dashboards show the first without the second, the bottleneck has moved to an un-automated stage — instrument and address *that*, don't add more coding autonomy.

## A minimal governance checklist

- [ ] Observability trace exists for every agent run before autonomy expands.
- [ ] Every irreversible/outward-facing action sits behind a human checkpoint.
- [ ] "Done" requires captured evidence, not an assertion.
- [ ] Review is performed by a different agent/context than the author.
- [ ] Metrics track delivery outcomes (flow, quality, cost), not output volume.
- [ ] Complexity is added only in response to a measured, observed need.

## See also

- [Agentic SDLC](./agentic-sdlc.md) · [Agentic Workflows](./agentic-workflows.md) · [References](./references.md)
