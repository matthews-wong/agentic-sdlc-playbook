# Business Case & ROI

> [Governance & metrics](./governance-and-metrics.md) is how you prove agents work *operationally*; this page is how you justify the investment *financially* — and why the return is conditional, not automatic. The headline: the agents that reach production report strong ROI, but **most never reach production.**

## The prize and the catch

Reported enterprise results are real and large — averages around **171–192% ROI** (roughly 3× traditional automation), with named cases like Klarna (~$60M saved) and JPMorgan (450+ deployments). But the number that reframes everything:

> **~88% of AI agents never reach production.** The 171% average is earned by the ~12% that do.

So ROI is **conditional on execution discipline** — the governance, evaluation, observability, security, and reliability this playbook is about. The business case isn't "agents → ROI"; it's "agents *done with these controls* → ROI."

## True cost: the API bill is the small part

A common budgeting error is equating cost with model/API spend. In practice:

> **Model API costs are only ~8–15% of total build cost** for most enterprise agentic systems.

The other 85–92% is integration, human oversight, evaluation and observability infrastructure, security/compliance work, and maintenance — exactly the line items this playbook keeps insisting on. Rough build ranges from 2026 reporting:

| System type | Indicative build cost |
|-------------|----------------------|
| RAG-grounded basic agent | ~$10K–$70K |
| Task-execution agent | ~$70K–$150K |
| Multi-agent enterprise platform | ~$150K–$500K+ |

Treat these as order-of-magnitude, not quotes; TCO benchmarks aren't yet standardized, and hidden integration + oversight costs are where estimates go wrong.

## The four value categories

A rigorous case counts value in four buckets — not just "labor saved":

1. **Direct cost reduction** — labor and process-efficiency gains.
2. **Revenue impact** — faster cycles, better conversion/throughput.
3. **Risk reduction** — fewer errors, better compliance monitoring (ties to [security](./security.md) + [compliance](./compliance-and-regulation.md)).
4. **Strategic optionality** — scaling operations without proportional headcount growth.

Counting only #1 undersells the case; counting all four without evidence oversells it. Anchor each to a measured baseline.

## Build vs. buy

- **Buy** a product to get value fast where one exists — the best [SDLC agent products](./tooling-landscape.md) slot into delivery primitives you already review (issues, PRs, CI).
- **Build** where no product covers your workflow, or where the moat is your own context/data.
- Either way, **budget the 85–92%** (integration + oversight), not just licensing — the classic build-vs-buy miss.

## A CFO-approvable case, step by step

1. **Baseline** today's delivery economics from your [metrics](./governance-and-metrics.md#metrics-that-actually-prove-value): lead time, change-failure/rework rate, cost per completed task.
2. **Pick the value categories** that genuinely apply and can be measured.
3. **Model TCO honestly** — API is ~8–15%; include oversight, eval, and integration.
4. **Phase the spend** against the [adoption roadmap](./adoption-roadmap.md) and [maturity model](./maturity-model.md) — fund L2→L3 first, prove it, then scale.
5. **Gate on production, not demos** — budget releases against the discipline that gets you into the ~12% that ship.

## The honest caveat

If a proposal promises the 171% without funding governance, evaluation, and observability, it's budgeting for the 88% that fail. The differentiator isn't the model — it's the execution discipline this playbook documents.

## Sources

See [references.md](./references.md#business-case--roi). All figures are directional 2026 reporting; model against your own numbers.
